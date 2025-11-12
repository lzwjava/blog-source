---
audio: false
generated: true
lang: ar
layout: post
title: استثناء التراجع عن معاملة SQL في سبرينغ
translated: true
type: note
---

لمعالجة استفسارك حول التقاط `SqlTransactionRollbackException` الذي يحدث بعد أن يحصل `DataSourceUtils.java` على اتصال JDBC من `DataSource` وتقديم تحليل مفصل لقفل قاعدة البيانات المرتبط، دعنا نقسم هذا بشكل منهجي.

### التقاط SqlTransactionRollbackException

في تطبيق يعتمد على Spring، فإن `DataSourceUtils.java` هو فئة أدوات داخل إطار عمل Spring تسهل استرجاع وإدارة اتصالات JDBC من `DataSource`. على وجه التحديد، تحصل طريقة `DataSourceUtils.getConnection(DataSource)` على اتصال، إما عن طريق جلب اتصال جديد من مجموعة الاتصالات أو إعادة استخدام اتصال معاملات موجود إذا كان مرتبطًا بالفعل بسياق المعاملة الحالي للخيط.

يشير السيناريو الذي وصفته إلى أنه بعد جلب الاتصال بنجاح، يتم إلقاء `SqlTransactionRollbackException`. نظرًا لأن `SqlTransactionRollbackException` ليس استثناءً قياسيًا في التسلسل الهرمي لاستثناءات Spring (تستخدم Spring عادةً استثناءات مثل `TransactionException`، أو `UnexpectedRollbackException`، أو `DeadlockLoserDataAccessException`)، سأفترض أنه استثناء مخصص محدد للتطبيق يتم إلقاؤه عندما يتم التراجع عن معاملة بسبب مشكلة متعلقة بقاعدة البيانات، مثل تعارض في القفل.

من المرجح أن يحدث هذا الاستثناء ليس أثناء استرجاع الاتصال نفسه (والذي من شأنه عادةً أن يلقي `CannotGetJdbcConnectionException` إذا فشل)، ولكن أثناء عمليات قاعدة البيانات اللاحقة داخل معاملة - مثل تنفيذ عبارات SQL - التي تواجه مشكلة تستدعي التراجع.

للقبض على هذا الاستثناء، تحتاج إلى لف الكود الذي يبدأ العملية المعاملية في كتلة `try-catch`. إليك كيف يمكنك القيام بذلك:

#### مثال مع إدارة المعاملات التقريرية
إذا كنت تستخدم شرح Spring `@Transactional` لإدارة المعاملات، فسيتم إلقاء الاستثناء من الطريقة التي تم فيها تعريف المعاملة. على سبيل المثال:

```java
@Service
public class MyService {
    @Autowired
    private MyDao myDao;

    @Transactional
    public void performDatabaseOperation() {
        myDao.updateData(); // افترض أن هذا يسبب تراجعًا بسبب مشكلة قفل
    }
}
```

عند استدعاء طريقة الخدمة هذه، يمكنك التقاط `SqlTransactionRollbackException`:

```java
@Autowired
private MyService myService;

public void executeOperation() {
    try {
        myService.performDatabaseOperation();
    } catch (SqlTransactionRollbackException e) {
        // معالجة الاستثناء
        System.err.println("تم التراجع عن المعاملة بسبب: " + e.getMessage());
        // إعادة محاولة العملية أو إخطار المستخدم اختياريًا
    }
}
```

#### مثال مع إدارة المعاملات البرمجية
إذا كنت تدير المعاملات برمجيًا باستخدام `TransactionTemplate` أو `PlatformTransactionManager`، فستقوم بالتقاط الاستثناء حول تنفيذ المعاملة:

```java
@Autowired
private TransactionTemplate transactionTemplate;

public void executeOperation() {
    try {
        transactionTemplate.execute(status -> {
            // تنفيذ عمليات قاعدة البيانات
            myDao.updateData();
            return null;
        });
    } catch (SqlTransactionRollbackException e) {
        // معالجة الاستثناء
        System.err.println("تم التراجع عن المعاملة بسبب: " + e.getMessage());
    }
}
```

#### الاعتبارات
- **التسلسل الهرمي للاستثناءات**: إذا كان `SqlTransactionRollbackException` استثناءً مخصصًا، فتحقق من فئته الأصلية. إذا كان يمتد لـ `DataAccessException` الخاص بـ Spring، فيمكنك عندئذٍ اصطياد `DataAccessException` بدلاً من ذلك والتحقق من النوع المحدد:
  ```java
  catch (DataAccessException e) {
      if (e instanceof SqlTransactionRollbackException) {
          // معالجة SqlTransactionRollbackException على وجه التحديد
      }
  }
  ```
- **سياق المعاملة**: من المرجح أن ينشأ الاستثناء بعد جلب الاتصال، عندما يكتشف مدير المعاملات أو برنامج تشغيل JDBC مشكلة (مثل حالة التراجع فقط أو خطأ في قاعدة البيانات). وبالتالي، فإن اصطياده على مستوى الخدمة أو المتصل هو المناسب.

### التحليل المفصل لقفل قاعدة البيانات

يشير ذكر "هذا النوع من قفل قاعدة البيانات" في استفسارك، مقترنًا باستثناء التراجع، بقوة إلى وجود صلة بـ **deadlock** - وهي مشكلة قفل شائعة في قاعدة البيانات يمكن أن تؤدي إلى تراجع المعاملات. دعنا نحلل هذا بالتفصيل.

#### ما هو deadlock؟
يحدث deadlock في قاعدة البيانات عندما لا تستطيع معاملتان أو أكثر المتابعة لأن كل منهما تحتفظ بقفل يحتاجه الآخر، مما يخلق تبعية دورية. على سبيل المثال:

- **المعاملة T1**:
  1. تحصل على قفل حصري على `TableA`.
  2. تحاول الحصول على قفل حصري على `TableB` (تنتظر لأن T2 تحتفظ به).
- **المعاملة T2**:
  1. تحصل على قفل حصري على `TableB`.
  2. تحاول الحصول على قفل حصري على `TableA` (تنتظر لأن T1 تحتفظ به).

هنا، تنتظر T1 حتى تطلق T2 `TableB`، وتنتظر T2 حتى تطلق T1 `TableA`، مما يؤدي إلى deadlock.

#### كيف تؤدي حالات deadlock إلى التراجعات
تمتلك معظم قواعد البيانات العلائقية (مثل MySQL، PostgreSQL، Oracle) آليات كشف عن deadlock. عند تحديد deadlock:
1. تختار قاعدة البيانات معاملة "ضحية" (غالبًا المعاملة التي تم إنجاز أقل عمل فيها أو بناءً على سياسة قابلة للتكوين).
2. يتم التراجع عن المعاملة الضحية، مما يؤدي إلى إطلاق أقفالها.
3. تلقى قاعدة البيانات `SQLException` برمز خطأ محدد (مثل خطأ MySQL 1213، خطأ PostgreSQL 40P01) إلى التطبيق.
4. في Spring، يتم عادةً ترجمة `SQLException` هذا إلى `DeadlockLoserDataAccessException`. إذا ألقى تطبيقك `SqlTransactionRollbackException` بدلاً من ذلك، فقد يكون غلافًا مخصصًا حول مثل هذا الحدث.

في سيناريوك، بعد أن يحصل `DataSourceUtils` على الاتصال، تواجه عملية قاعدة البيانات داخل المعاملة deadlock، مما يؤدي إلى التراجع وإلقاء `SqlTransactionRollbackException`.

#### أنواع الأقفال المشاركة
- **الأقفال المشتركة**: تُستخدم لعمليات القراءة؛ يمكن لمعاملات متعددة الاحتفاظ بأقفال مشتركة على نفس المورد.
- **الأقفال الحصرية**: تُستخدم لعمليات الكتابة؛ يمكن لمعاملة واحدة فقط الاحتفاظ بقفل حصري، ويتعارض مع كل من الأقفال المشتركة والحصرية التي يحتفظ بها الآخرون.
عادةً ما تتضمن حالات deadlock أقفالًا حصرية، لأنها أكثر تقييدًا.

#### لماذا تحدث حالات deadlock
تنشأ حالات deadlock بسبب:
- **ترتيب القفل غير المتسق**: المعاملات التي تصل إلى الموارد (مثل الجداول، الصفوف) بتسلسلات مختلفة.
- **المعاملات الطويلة**: الاحتفاظ بالأقفال لفترات طويلة يزيد من فرص التعارض.
- **التزامن العالي**: تشغيل معاملات متعددة على نفس البيانات في وقت واحد.

#### مثال على سيناريو
لنفترض أن طريقتين في تطبيقك تقومان بتحديد جدولين:

```java
@Transactional
public void updateUserAndOrder1() {
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Alice", 1); // يقفل صف users
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Shipped", 1); // يقفل صف orders
}

@Transactional
public void updateUserAndOrder2() {
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Processed", 1); // يقفل صف orders
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Bob", 1); // يقفل صف users
}
```

إذا تم تشغيل هذه الطرق في وقت واحد، فقد يقفل `updateUserAndOrder1` `users` أثناء انتظار `orders`، وقد يقفل `updateUserAndOrder2` `orders` أثناء انتظار `users`، مما يتسبب في deadlock.

#### معالجة ومنع حالات deadlock
1. **التقاط الاستثناء**:
   كما هو موضح سابقًا، استخدم كتلة `try-catch` لمعالجة `SqlTransactionRollbackException`. قد تقوم بما يلي:
   - تسجيل الخطأ لتصحيح الأخطاء.
   - إعادة محاولة العملية (بحذر لتجنب الحلقات اللانهائية):
     ```java
     int retries = 3;
     for (int i = 0; i < retries; i++) {
         try {
             myService.performDatabaseOperation();
             break;
         } catch (SqlTransactionRollbackException e) {
             if (i < retries - 1) {
                 Thread.sleep(1000 * (i + 1)); // Exponential backoff
                 continue;
             }
             throw e; // إعادة الإلقاء بعد الحد الأقصى من المحاولات
         }
     }
     ```

2. **ضمان ترتيب قفل متسق**:
   قم بتعديل الكود للوصول إلى الجداول بنفس التسلسل (مثل قفل `users` دائمًا قبل `orders`).

3. **تقليل مدة القفل**:
   حافظ على إبقاء المعاملات قصيرة عن طريق نقل المنطق غير المعامل خارج حدود `@Transactional`.

4. **استخدام مستويات العزل المناسبة**:
   اضبط مستوى عزل المعاملة (مثل `READ_COMMITTED` بدلاً من `SERIALIZABLE`) إذا سمحت متطلبات التطبيق، على الرغم من أن هذا لا يلغي حالات deadlock تمامًا.

5. **ميزات محددة لقاعدة البيانات**:
   - تمكين تسجيل كشف deadlock (مثل `innodb_print_all_deadlocks` في MySQL).
   - استخدم القفل على مستوى الصف حيثما أمكن، على الرغم من أن حالات deadlock يمكن أن تحدث على مستوى الصف.

#### تحليل حالات deadlock
لتشخيص deadlock المحدد:
- **سجلات قاعدة البيانات**: تحقق من سجلات خادم قاعدة البيانات للحصول على تفاصيل deadlock (مثل المعاملات المشاركة، الموارد المقفلة).
- **تصحيح أخطاء Spring**: قم بتمكين تسجيل معاملات Spring (`logging.level.org.springframework.transaction=DEBUG`) لتتبع أحداث المعاملة.
- **تتبع التطبيق**: سجل تسلسل العمليات المؤدية إلى الاستثناء.

### الخلاصة
للقبض على `SqlTransactionRollbackException`، ضع كتلة `try-catch` حول الكود الذي يستدعي العملية المعاملية، مثل طريقة خدمة محددة بـ `@Transactional`. بالنسبة لقفل قاعدة البيانات - المرجح أنه deadlock - تأكد من وصول المعاملات إلى الموارد بترتيب متسق، حافظ على المعاملات قصيرة، وفكر في منطق إعادة المحاولة للأعطال العابرة. تحدث حالات deadlock بسبب التبعيات الدورية للقفل، وبينما تحلها قواعد البيانات عن طريق التراجع عن معاملة ضحية، فإن التصميم الاستباقي يمكن أن يقلل من حدوثها.

---

عند التعامل مع `SqlTransactionRollbackException` في تطبيق Spring - خاصة في سيناريو حيث تحتفظ معاملة أخرى بقفل، مما يؤدي إلى فشل في جلب الاتصال وإلقاء الاستثناء بعد حوالي 20 محاولة فاشلة - هناك عدة استراتيجيات يمكنك استخدامها لمعالجة هذه المشكلة والتخفيف من حدتها محتملاً. ينشأ هذا الاستثناء عادة أثناء التراجع عن المعاملة عندما تمنع أقفال قاعدة البيانات أو مشاكل التزامن إكمال العملية بنجاح. أدناه، أقدم نهجًا شاملاً لمعالجة هذه المشكلة، مع التركيز على الوقاية والمعالجة والتعافي.

---

### فهم المشكلة
يشير `SqlTransactionRollbackException` (أو على الأرجح `TransactionRollbackException` في Spring، حيث أن الأول ليس استثناءً قياسيًا في Spring) إلى أنه لا يمكن التراجع عن معاملة، ربما لأن معاملة أخرى تحتفظ بقفل على موارد قاعدة البيانات المطلوبة. يتسبب هذا التعارض في القفل في فشل مدير المعاملات في جلب اتصال، وإعادة المحاولة عدة مرات (حوالي 20 في حالتك)، وإلقاء الاستثناء في النهاية عندما لا يمكن إكمال التراجع. يشير هذا إلى مشكلة تزامن، مثل تعارض في القفل أو deadlock، تفاقم بسبب إعادة محاولة إدارة معاملات Spring داخليًا قبل الاستسلام.

---

### استراتيجيات لمعالجة الاستثناء

#### 1. تقليل تعارض القفل بمعاملات قصيرة
تزيد المعاملات طويلة الأمد من احتمالية تعارض القفل، لأنها تحتفظ بأقفال قاعدة البيانات لفترات طويلة، مما يعيق المعاملات الأخرى. لتقليل هذه المخاطر:

- **تصميم معاملات قصيرة العمر**: تأكد من أن طرقك `@Transactional` تنفذ عمليات قاعدة البيانات بسرعة وتلتزم أو تتراجع على الفور. تجنب تضمين منطق أعمال يستغرق وقتًا طويلاً أو استدعاءات خارجية ضمن نطاق المعاملة.
- **تقسيم المعاملات الكبيرة**: إذا كانت المعاملة الواحدة تتضمن عمليات متعددة، ففكر في تقسيمها إلى معاملات أصغر مستقلة حيثما أمكن. هذا يقلل من المدة التي يتم فيها الاحتفاظ بالأقفال.

#### 2. تحسين استعلامات قاعدة البيانات
يمكن للاستعلامات غير المحسنة أن تفاقم تعارض القفل عن طريق الاحتفاظ بالأقفال لفترة أطول من اللازم. لمعالجة هذا:

- **تحليل وتحسين الاستعلامات**: استخدم أدوات تحليل قاعدة البيانات لتحديد الاستعلامات البطيئة. أضف فهارس مناسبة، وتجنب فحوصات الجدول غير الضرورية، وقلل نطاق الصفوف المقفلة (مثل استخدام عبارات `WHERE` دقيقة).
- **تجنب الأقفال الواسعة جدًا**: كن حذرًا مع العبارات مثل `SELECT ... FOR UPDATE`، التي تقفل الصفوف صراحةً ويمكن أن تعيق المعاملات الأخرى. استخدمها فقط عند الضرورة وتأكد من أنها تؤثر على أقل عدد ممكن من الصفوف.

#### 3. ضبط إعدادات المعاملة
يوفر شرح Spring `@Transactional` سمات لضبط سلوك المعاملة بدقة. بينما لن تحل هذه بشكل مباشر أعطال التراجع، يمكنها المساعدة في إدارة التزامن:

- **مستوى العزل**: مستوى العزل الافتراضي (`DEFAULT`) يعادل عادةً الافتراضي لقاعدة البيانات (غالبًا `READ_COMMITTED`). زيادة المستوى إلى `REPEATABLE_READ` أو `SERIALIZABLE` قد يضمن اتساق البيانات ولكن يمكن أن يزيد من تعارض القفل. على العكس، البقاء مع `READ_COMMITTED` أو أقل (إذا كان مدعومًا) قد يقلل من مشاكل القفل، اعتمادًا على حالة الاستخدام. اختبر بعناية للعثور على التوازن الصحيح.
- **سلوك الانتشار**: الافتراضي `REQUIRED` ينضم إلى معاملة موجودة أو يبدأ معاملة جديدة. استخدام `REQUIRES_NEW` يوقف المعاملة الحالية ويبدأ معاملة جديدة، مما قد يتجنب التعارضات مع معاملة مقفلة. ومع ذلك، قد لا يعالج مشاكل التراجع المحددة.
- **الوقت المتاح**: عيّن قيمة `timeout` (بالثواني) في `@Transactional(timeout = 10)` لفشل المعاملات بشكل أسرع إذا كانت تنتظر على أقفال. هذا يمنع إعادة المحاولة المطولة ولكن لا يحل السبب الجذري.

مثال:
```java
@Transactional(timeout = 5, propagation = Propagation.REQUIRES_NEW)
public void performDatabaseOperation() {
    // الكود الخاص بك هنا
}
```

#### 4. تنفيذ منطق إعادة المحاولة (بحذر)
نظرًا لأن الاستثناء يحدث بعد محاولات داخلية متعددة (حوالي 20)، فمن المرجح أن مدير معاملات Spring يحاول بالفعل معالجة المشكلة. ومع ذلك، يمكنك تنفيذ منطق إعادة محاولة مخصص على مستوى أعلى:

- **باستخدام Spring Retry**:
   علق طريقة خدمة بـ `@Retryable` لإعادة المحاولة على `TransactionRollbackException`. حدد عدد المحاولات والتأخير بينها. قم بإقرانها بطريقة `@Recover` للتعامل مع الفشل بعد استنفاد المحاولات.
  ```java
  import org.springframework.retry.annotation.Backoff;
  import org.springframework.retry.annotation.Retryable;
  import org.springframework.retry.annotation.Recover;
  import org.springframework.transaction.annotation.Transactional;

  @Service
  public class MyService {

      @Retryable(value = TransactionRollbackException.class, maxAttempts = 3, backoff = @Backoff(delay = 1000))
      public void executeOperation() {
          performTransactionalWork();
      }

      @Transactional
      private void performTransactionalWork() {
          // عمليات قاعدة البيانات التي قد تفشل
      }

      @Recover
      public void recover(TransactionRollbackException e) {
          // تسجيل الخطأ، إخطار المسؤولين، أو اتخاذ إجراء تصحيحي
          System.err.println("فشلت جميع محاولات إعادة المحاولة: " + e.getMessage());
      }
  }
  ```
  **ملاحظة**: تبدأ كل محاولة إعادة معاملة جديدة، مما قد لا يكون مثاليًا إذا كانت الذرية عبر محاولات إعادة المحاولة مطلوبة. طبق هذا خارج طريقة `@Transactional` إذا أمكن.

- **إعادة المحاولة اليدوية مع TransactionTemplate**:
   لمزيد من التحكم، استخدم `TransactionTemplate` للف الكود المعاملي في حلقة إعادة محاولة:
  ```java
  import org.springframework.transaction.PlatformTransactionManager;
  import org.springframework.transaction.TransactionStatus;
  import org.springframework.transaction.support.TransactionCallbackWithoutResult;
  import org.springframework.transaction.support.TransactionTemplate;

  @Service
  public class MyService {
      private final TransactionTemplate transactionTemplate;
      private static final int MAX_RETRIES = 3;
      private static final long RETRY_DELAY_MS = 1000;

      public MyService(PlatformTransactionManager transactionManager) {
          this.transactionTemplate = new TransactionTemplate(transactionManager);
      }

      public void executeWithRetry() {
          for (int i = 0; i < MAX_RETRIES; i++) {
              try {
                  transactionTemplate.execute(new TransactionCallbackWithoutResult() {
                      @Override
                      protected void doInTransactionWithoutResult(TransactionStatus status) {
                          // الكود المعاملي هنا
                      }
                  });
                  return; // النجاح، الخروج من الحلقة
              } catch (TransactionRollbackException e) {
                  if (i == MAX_RETRIES - 1) {
                      throw e; // إعادة الإلقاء بعد الحد الأقصى للمحاولات
                  }
                  try {
                      Thread.sleep(RETRY_DELAY_MS);
                  } catch (InterruptedException ie) {
                      Thread.currentThread().interrupt();
                  }
              }
          }
      }
  }
  ```
  **تحذير**: قد لا تحل إعادة المحاولة المشكلة إذا استمر القفل، وقد تؤدي إلى حالات غير متسقة إذا تم تطبيق تغييرات جزئية قبل فشل التراجع. تأكد من أن محاولات إعادة المحاولة متكررة أو آمنة.

#### 5. معالجة الاستثناء بأمان
إذا فشل التراجع بسبب أقفال مستمرة، فقد تصبح حالة قاعدة البيانات غير متسقة، مما يتطلب معالجة دقيقة:

- **التقاط وتسجيل**:
   لف الاستدعاء المعاملي في كتلة try-catch، سجل الاستثناء، وأخطر المسؤولين:
  ```java
  try {
      myService.performTransactionalWork();
  } catch (TransactionRollbackException e) {
      // تسجيل الخطأ
      logger.error("فشل التراجع عن المعاملة بعد محاولات إعادة المحاولة: " + e.getMessage(), e);
      // إخطار المسؤولين (عبر البريد الإلكتروني أو نظام المراقبة مثلاً)
      alertSystem.notify("حرج: فشل في التراجع عن المعاملة");
      // الفشل بأمان أو الدخول في حالة آمنة
      throw new RuntimeException("فشلت العملية بسبب مشاكل في المعاملة", e);
  }
  ```

- **الفشل بأمان**: إذا كانت حالة المعاملة غير مؤكدة، أوقف العمليات الإضافية التي تعتمد عليها وأشر إلى الحاجة إلى تدخل يدوي.

#### 6. الاستفادة من ميزات قاعدة البيانات
اضبط إعدادات قاعدة البيانات للتخفيف من المشاكل المتعلقة بالقفل:

- **انتهاء وقت القفل**: قم بتكوين قاعدة البيانات لتنتهي صلاحية وقت الانتظار على القفل بسرعة (مثل `SET LOCK_TIMEOUT 5000` في SQL Server أو `innodb_lock_wait_timeout` في MySQL). هذا يفشل المعاملة في وقت مبكر، مما يسمح لـ Spring بمعالجة الاستثناء عاجلاً.
- **كشف deadlock**: تأكد من تمكين كشف deadlock في قاعدة البيانات وتكوينه لحل التعارضات عن طريق التراجع عن معاملة واحدة تلقائيًا.
- **القفل التفاؤلي**: إذا كنت تستخدم JPA، طبق `@Version` على الكيانات لاستخدام القفل التفاؤلي، مما يقلل من تعارض القفل المادي:
  ```java
  @Entity
  public class MyEntity {
      @Id
      private Long id;
      @Version
      private Integer version;
      // حقول أخرى
  }
  ```
  هذا يحول اكتشاف التعارض إلى وقت الالتزام ولكن قد لا يعالج أعطال التراجع مباشرة.

#### 7. المراقبة والتحقيق
يشير التكرار المتكرر لهذا الاستثناء إلى وجود مشكلة أساسية:

- **إضافة المراقبة**: استخدم أدوات مثل Spring Boot Actuator أو إطار عمل تسجيل لتتبع هذه الاستثناءات وتكرارها.
- **تحليل السجلات**: تحقق من سجلات قاعدة البيانات والتطبيق للبحث عن أنماط (مثل استعلامات أو معاملات محددة تسبب أقفال).
- **ضبط التزامن**: إذا استمر التعارض، راجع نموذج التزامن لتطبيقك أو تصميم قاعدة البيانات.

---

### لماذا يفشل التراجع
يشير فشل التراجع بعد 20 محاولة إلى أن مدير معاملات Spring يعيد محاولة عملية التراجع عندما يواجه موردًا مقفلاً أو اتصالاً مفقودًا، ويستسلم في النهاية. يمكن أن ينبع هذا من:

- **أقفال مستمرة**: معاملة أخرى تحتفظ بقفل لا يتم إطلاقه خلال نافذة إعادة المحاولة.
- **مشاكل في الاتصال**: مجموعة اتصالات قاعدة البيانات (مثل HikariCP) تستنفد محاولاتها لجلب اتصال.
- **إعداد خاطئ لقاعدة البيانات**: إعدادات الوقت المتاح أو إعادة المحاولة في قاعدة البيانات أو مجموعة الاتصالات عدوانية جدًا أو غير كافية.

---

### النهج الموصى به
إليك حلاً عملياً يجمع بين الاستراتيجيات المذكورة أعلاه:

1. **تحسين المعاملات والاستعلامات**: حافظ على المعاملات قصيرة والاستعلامات فعالة لتقليل مدة القفل.
2. **تعيين وقت متاح للمعاملة**: استخدم `@Transactional(timeout = 5)` للفشل بسرعة إذا استمرت الأقفال.
3. **المعالجة مع إعادة المحاولة والتعافي**:
   ```java
   @Service
   public class MyService {
       @Autowired
       private MyRepository repository;

       public void executeOperationWithRetry() {
           int maxAttempts = 3;
           for (int i = 0; i < maxAttempts; i++) {
               try {
                   performTransactionalWork();
                   return;
               } catch (TransactionRollbackException e) {
                   if (i == maxAttempts - 1) {
                       logger.error("فشل بعد {} محاولات: {}", maxAttempts, e.getMessage(), e);
                       alertSystem.notify("فشل في التراجع عن المعاملة");
                       throw e;
                   }
                   try {
                       Thread.sleep(1000); // الانتظار قبل إعادة المحاولة
                   } catch (InterruptedException ie) {
                       Thread.currentThread().interrupt();
                   }
               }
           }
       }

       @Transactional
       private void performTransactionalWork() {
           // عمليات قاعدة البيانات
           repository.save(someEntity);
       }
   }
   ```
4. **المراقبة والضبط**: سجل الاستثناء، أنشئ تنبيهات، وتحقق من أسباب تعارض القفل.

---

### الخلاصة
لمعالجة `SqlTransactionRollbackException` في Spring عندما تحتفظ معاملة أخرى بقفل، مما يتسبب في فشل جلب الاتصال ومحاولات متكررة، ركز على تقليل تعارض القفل من خلال المعاملات القصيرة والاستعلامات المحسنة، وضبط إعدادات المعاملة حسب الحاجة، وتنفيذ منطق إعادة محاولة حذر على مستوى أعلى، ومعالجة الاستثناء عن طريق التسجيل والإخطار بشكل مناسب. يضمن هذا استقرار النظام وسلامة البيانات مع معالجة السبب الجذري بمرور الوقت من خلال المراقبة والضبط.

---

عند العمل مع برنامج تشغيل IBM DB2 Java (على وجه التحديد برنامج تشغيل JDBC)، فإن معالجة سيناريوهات التراجع عن المعاملات أمر ضروري للتفاعل القوي مع قاعدة البيانات. يشير الاستعلام إلى `SqlTransactionRollbackException`، والذي يبدو أنه خطأ إملائي طفيف. في JDBC القياسي، خاصة من الإصدار 4.0 فصاعدًا (المدعوم من برامج تشغيل IBM DB2 الحديثة مثل `db2jcc4.jar`)، فإن الاستثناء الصحيح هو **`SQLTransactionRollbackException`**. هذا الاستثناء هو فئة فرعية من `SQLException` ويتم إلقاؤه عندما يتم التراجع عن معاملة قاعدة البيانات تلقائيًا، كما في حالات deadlocks أو انتهاء المهلة.

إليك كيفية معالجة `SQLTransactionRollbackException` بشكل فعال في كود Java الخاص بك عند استخدام برنامج تشغيل IBM DB2 JDBC:

### نهج معالجة الاستثناء

1. **استخدم كتلة Try-Catch**: لف عمليات قاعدة البيانات المعاملية في كتلة `try` والقم بالتقاط `SQLTransactionRollbackException` لمعالجة الحالات التي تتراجع فيها قاعدة البيانات عن المعاملة.
2. **اتخذ الإجراء المناسب**: اعتمادًا على متطلبات تطبيقك، قد تقوم بتسجيل الخطأ، أو إعادة محاولة المعاملة (إذا كانت المشكلة عابرة، مثل deadlock)، أو إخطار المستخدم بالفشل.
3. **تأكد من تنظيف الموارد**: قم بإدارة موارد قاعدة البيانات بشكل صحيح (مثل إغلاق الاتصال) في كتلة `finally` لتجنب تسرب الموارد.
4. **التراجع لبرامج التشغيل القديمة**: إذا كنت تستخدم برنامج تشغيل DB2 أقدم لا يدعم JDBC 4.0، فقد تحتاج إلى التقاط `SQLException` والتحقق من رمز الخطأ (مثل `-911` للتراجع الناتج عن deadlock في DB2).

### مثال على الكود

إليك مثالاً عمليًا يوضح كيفية معالجة `SQLTransactionRollbackException`:

```java
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.SQLTransactionRollbackException;
import javax.sql.DataSource;

public class DB2TransactionExample {
    public void performTransaction(DataSource dataSource) {
        Connection conn = null;
        try {
            // الحصول على اتصال وتعطيل الالتزام التلقائي لبدء معاملة
            conn = dataSource.getConnection();
            conn.setAutoCommit(false);

            // تنفيذ عمليات قاعدة البيانات هنا
            // على سبيل المثال، تنفيذ عبارات مثل INSERT، UPDATE، إلخ.

            // إذا نجحت جميع العمليات، قم بالالتزام بالمعاملة
            conn.commit();
        } catch (SQLTransactionRollbackException e) {
            // معالجة الحالة التي تراجعت فيها قاعدة البيانات عن المعاملة
            System.err.println("تم التراجع عن المعاملة بواسطة قاعدة البيانات: " + e.getMessage());
            System.err.println("حالة SQL: " + e.getSQLState() + ", رمز الخطأ: " + e.getErrorCode());
            // مثال: حالة SQL '40001' ورمز الخطأ -911 يشيران إلى deadlock أو انتهاء مهلة في DB2
            // إعادة محاولة المعاملة أو إخطار المستخدم اختياريًا
        } catch (SQLException e) {
            // معالجة استثناءات SQL الأخرى
            System.err.println("خطأ SQL: " + e.getMessage());
            // محاولة التراجع يدويًا إذا كانت المعاملة لا تزال نشطة
            if (conn != null) {
                try {
                    conn.rollback();
                    System.out.println("تم التراجع عن المعاملة يدويًا.");
                } catch (SQLException rollbackEx) {
                    System.err.println("فشل التراجع: " + rollbackEx.getMessage());
                }
            }
        } finally {
            // تنظيف الموارد
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // استعادة السلوك الافتراضي
                    conn.close();
                } catch (SQLException closeEx) {
                    System.err.println("فشل في إغلاق الاتصال: " + closeEx.getMessage());
                }
            }
        }
    }
}
```

### النقاط الرئيسية في الكود

- **التقاط `SQLTransactionRollbackException`**: هذا يلتقط على وجه التحديد الحالات التي تتراجع فيها DB2 عن المعاملة (مثل بسبب deadlock، يُشار إليه برمز الخطأ `-911` أو حالة SQL `40001`).
- **التقاط `SQLException` العام**: يعمل هذا كتراجع لأخطاء قاعدة البيانات الأخرى، مما يضمن معالجة أوسع للأخطاء.
- **التراجع اليدوي**: إذا حدث `SQLException` ولم يتم التراجع عن المعاملة تلقائيًا، يمكنك محاولة التراجع يدويًا.
- **إدارة الموارد**: تضمن كتلة `finally` إغلاق الاتصال، مما يمنع تسرب الموارد.

### اعتبارات إضافية

- **إصدار برنامج التشغيل**: تأكد من أنك تستخدم برنامج تشغيل IBM DB2 متوافق مع JDBC 4.0 (مثل `db2jcc4.jar`). قد تلقى برامج التشغيل الأقدم (مثل `db2jcc.jar`) `SQLException` فقط، مما يتطلب منك التحقق من رمز الخطأ يدويًا. على سبيل المثال:
  ```java
  catch (SQLException e) {
      if (e.getErrorCode() == -911) {
          // معالجة التراجع عن المعاملة بسبب deadlock أو انتهاء مهلة
      }
  }
  ```
- **حالة SQL ورموز الخطأ**: تستخدم DB2 حالة SQL `40001` لأعطال التسلسل (مثل deadlocks) ورمز الخطأ `-911` عندما يتم التراجع عن المعاملة تلقائيًا. يشير رمز الخطأ `-913` إلى فشل في العبارة بسبب deadlock، ولكن تبقى المعاملة نشطة ما لم يتم التراجع عنها صراحة.
- **منطق إعادة المحاولة**: للمشاكل العابرة مثل deadlocks، قد تنفذ آلية إعادة محاولة:
  ```java
  int maxRetries = 3;
  for (int attempt = 1; attempt <= maxRetries; attempt++) {
      try {
          performTransaction(dataSource);
          break; // النجاح، الخروج من الحلقة
      } catch (SQLTransactionRollbackException e) {
          if (attempt == maxRetries) {
              throw e; // إعادة الإلقاء بعد الحد الأقصى للمحاولات
          }
          Thread.sleep(1000 * attempt); // الانتظار قبل إعادة المحاولة
      }
  }
  ```

### الخلاصة

لمعالجة `SQLTransactionRollbackException` (بشكل صحيح `SQLTransactionRollbackException`) في برنامج تشغيل IBM DB2 Java، استخدم كتلة `try-catch` للقبض على هذا الاستثناء المحدد لسيناريوهات التراجع عن المعاملة. اجمعها مع إدارة مناسبة للموارد، وإذا لزم الأمر، منطق تراجع لبرامج التشغيل القديمة عن طريق التحقق من رموز الأخطاء مثل `-911`. يضمن هذا النهج أن تطبيقك يتعامل بأمان مع التراجعات عن المعاملات مع الحفاظ على سلامة قاعدة البيانات وتجربة المستخدم.