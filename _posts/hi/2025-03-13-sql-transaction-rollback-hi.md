---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग में एसक्यूएल ट्रांजैक्शन रोलबैक एक्सेप्शन
translated: true
type: note
---

आपके प्रश्न के अनुसार, जब `DataSourceUtils.java` एक `DataSource` से JDBC कनेक्शन प्राप्त करता है और उसके बाद `SqlTransactionRollbackException` होता है, तो इसे कैसे पकड़ें और संबंधित डेटाबेस लॉक का विस्तृत विश्लेषण प्रस्तुत करें, आइए इसे व्यवस्थित रूप से समझते हैं।

### SqlTransactionRollbackException को पकड़ना (Catching the SqlTransactionRollbackException)

एक Spring-आधारित एप्लिकेशन में, `DataSourceUtils.java` Spring Framework के अंदर एक utility class है जो एक `DataSource` से JDBC कनेक्शन प्राप्त करने और प्रबंधित करने में सहायता करती है। विशेष रूप से, `DataSourceUtils.getConnection(DataSource)` method एक कनेक्शन प्राप्त करती है, या तो connection pool से एक नया कनेक्शन लेकर या मौजूदा transactional कनेक्शन का पुन: उपयोग करके, यदि वह पहले से ही current thread के transaction context से जुड़ा हुआ है।

आपके द्वारा वर्णित परिदृश्य इंगित करता है कि कनेक्शन सफलतापूर्वक प्राप्त होने के बाद, एक `SqlTransactionRollbackException` thrown होती है। चूंकि `SqlTransactionRollbackException` Spring की exception hierarchy में एक standard exception नहीं है (Spring आमतौर पर `TransactionException`, `UnexpectedRollbackException`, या `DeadlockLoserDataAccessException` जैसे exceptions का उपयोग करता है), मैं मानूंगा कि यह एक custom application-specific exception है जो तब thrown होती है जब कोई transaction database-related issue, जैसे कि lock conflict, के कारण roll back हो जाता है।

यह exception संभवतः connection retrieval के दौरान ही नहीं होती (जो विफल होने पर आमतौर पर `CannotGetJdbcConnectionException` throw करेगी), बल्कि transaction के भीतर subsequent database operations के दौरान होती है - जैसे SQL statements execute करना - जिसमें कोई समस्या आती है जिसके लिए rollback आवश्यक हो जाता है।

इस exception को पकड़ने के लिए, आपको उस code को एक `try-catch` block में wrap करना होगा जो transactional operation शुरू करता है। यहां बताया गया है कि आप इसे कैसे कर सकते हैं:

#### Declarative Transaction Management के साथ उदाहरण
यदि आप transactions को manage करने के लिए Spring के `@Transactional` annotation का उपयोग कर रहे हैं, तो exception उस method से thrown होगी जहां transaction परिभाषित है। उदाहरण के लिए:

```java
@Service
public class MyService {
    @Autowired
    private MyDao myDao;

    @Transactional
    public void performDatabaseOperation() {
        myDao.updateData(); // मान लें कि यह lock issue के कारण rollback का कारण बनता है
    }
}
```

इस service method को call करते समय, आप `SqlTransactionRollbackException` को पकड़ सकते हैं:

```java
@Autowired
private MyService myService;

public void executeOperation() {
    try {
        myService.performDatabaseOperation();
    } catch (SqlTransactionRollbackException e) {
        // Exception को handle करें
        System.err.println("Transaction rolled back due to: " + e.getMessage());
        // वैकल्पिक रूप से operation को retry करें या user को notify करें
    }
}
```

#### Programmatic Transaction Management के साथ उदाहरण
यदि आप `TransactionTemplate` या `PlatformTransactionManager` का उपयोग करके programmatically transactions manage कर रहे हैं, तो आप transaction execution के आसपास exception को पकड़ेंगे:

```java
@Autowired
private TransactionTemplate transactionTemplate;

public void executeOperation() {
    try {
        transactionTemplate.execute(status -> {
            // Database operations perform करें
            myDao.updateData();
            return null;
        });
    } catch (SqlTransactionRollbackException e) {
        // Exception को handle करें
        System.err.println("Transaction rolled back due to: " + e.getMessage());
    }
}
```

#### विचारणीय बिंदु
- **Exception Hierarchy**: यदि `SqlTransactionRollbackException` एक custom exception है, तो इसके superclass को verify करें। यदि यह Spring के `DataAccessException` को extend करती है, तो आप इसके बजाय `DataAccessException` को पकड़ सकते हैं और specific type check कर सकते हैं:
  ```java
  catch (DataAccessException e) {
      if (e instanceof SqlTransactionRollbackException) {
          // SqlTransactionRollbackException को specifically handle करें
      }
  }
  ```
- **Transaction Context**: Exception संभवतः connection fetch होने के बाद उत्पन्न होती है, जब transaction manager या JDBC driver कोई issue (जैसे, rollback-only state या database error) detect करता है। इस प्रकार, इसे service या caller level पर पकड़ना उचित है।

### डेटाबेस लॉक का विस्तृत विश्लेषण (Detailed Analysis of the Database Lock)

आपके query में "this kind of database lock" का उल्लेख, rollback exception के साथ मिलकर, दृढ़ता से एक **deadlock** से संबंधित होने का सुझाव देता है - एक सामान्य डेटाबेस लॉकिंग issue जो transaction rollbacks का कारण बन सकता है। आइए इसका विस्तृत विश्लेषण करें।

#### Deadlock क्या है? (What is a Deadlock?)
एक deadlock डेटाबेस में तब होता है जब दो या दो से अधिक transactions आगे बढ़ने में असमर्थ होते हैं क्योंकि प्रत्येक एक lock रखता है जिसकी दूसरे को आवश्यकता होती है, जिससे एक cyclic dependency बन जाती है। उदाहरण के लिए:

- **Transaction T1**:
  1. `TableA` पर एक exclusive lock प्राप्त करता है।
  2. `TableB` पर एक exclusive lock प्राप्त करने का प्रयास करता है (प्रतीक्षा करता है क्योंकि T2 उसे रखता है)।
- **Transaction T2**:
  1. `TableB` पर एक exclusive lock प्राप्त करता है।
  2. `TableA` पर एक exclusive lock प्राप्त करने का प्रयास करता है (प्रतीक्षा करता है क्योंकि T1 उसे रखता है)।

यहां, T1, T2 के `TableB` को release करने की प्रतीक्षा करता है, और T2, T1 के `TableA` को release करने की प्रतीक्षा करता है, जिसके परिणामस्वरूप deadlock होता है।

#### Deadlock कैसे Rollbacks का कारण बनते हैं (How Deadlocks Lead to Rollbacks)
अधिकांश relational databases (जैसे, MySQL, PostgreSQL, Oracle) में deadlock detection mechanisms होते हैं। जब एक deadlock की पहचान की जाती है:
1. डेटाबेस एक "victim" transaction का चयन करता है (अक्सर वह जिसने सबसे कम काम किया हो या configurable policy के आधार पर)।
2. Victim transaction को roll back कर दिया जाता है, जिससे उसके locks release हो जाते हैं।
3. डेटाबेस एप्लिकेशन को एक specific error code (जैसे, MySQL error 1213, PostgreSQL error 40P01) के साथ एक `SQLException` throw करता है।
4. Spring में, इस `SQLException` को आमतौर पर `DeadlockLoserDataAccessException` में translate किया जाता है। यदि आपका एप्लिकेशन इसके बजाय `SqlTransactionRollbackException` throw करता है, तो यह ऐसी घटना के आसपास एक custom wrapper हो सकता है।

आपके परिदृश्य में, `DataSourceUtils` द्वारा कनेक्शन fetch करने के बाद, transaction के भीतर एक database operation deadlock का सामना करता है, जिससे rollback होता है और `SqlTransactionRollbackException` thrown होती है।

#### शामिल लॉक के प्रकार (Lock Types Involved)
- **Shared Locks**: read operations के लिए उपयोग किए जाते हैं; कई transactions एक ही resource पर shared locks रख सकते हैं।
- **Exclusive Locks**: write operations के लिए उपयोग किए जाते हैं; केवल एक transaction एक exclusive lock रख सकता है, और यह दूसरों द्वारा रखे गए shared और exclusive locks दोनों के साथ conflict करता है।
Deadlocks में आमतौर पर exclusive locks शामिल होते हैं, क्योंकि वे अधिक प्रतिबंधात्मक होते हैं।

#### Deadlocks क्यों होते हैं (Why Deadlocks Happen)
Deadlocks निम्न कारणों से उत्पन्न होते हैं:
- **असंगत लॉकिंग क्रम (Inconsistent Locking Order)**: Transactions resources (जैसे, tables, rows) को different sequences में access करते हैं।
- **लंबे transactions (Long Transactions)**: Extended periods के लिए locks रखने से conflicts की संभावना बढ़ जाती है।
- **उच्च समवर्तीता (High Concurrency)**: एक ही डेटा पर एक साथ काम करने वाले कई transactions।

#### उदाहरण परिदृश्य (Example Scenario)
मान लें कि आपके एप्लिकेशन में दो methods दो tables को update करते हैं:

```java
@Transactional
public void updateUserAndOrder1() {
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Alice", 1); // users row को lock करता है
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Shipped", 1); // orders row को lock करता है
}

@Transactional
public void updateUserAndOrder2() {
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Processed", 1); // orders row को lock करता है
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Bob", 1); // users row को lock करता है
}
```

यदि ये methods concurrently चलती हैं, तो `updateUserAndOrder1` `users` को lock कर सकता है जबकि `orders` की प्रतीक्षा कर रहा हो, और `updateUserAndOrder2` `orders` को lock कर सकता है जबकि `users` की प्रतीक्षा कर रहा हो, जिससे deadlock हो जाता है।

#### Deadlocks को Handle और Prevent करना (Handling and Preventing Deadlocks)
1. **Exception को पकड़ें (Catch the Exception)**:
   जैसा कि पहले दिखाया गया है, `SqlTransactionRollbackException` को handle करने के लिए `try-catch` block का उपयोग करें। आप कर सकते हैं:
   - Debugging के लिए error log करें।
   - Operation को retry करें (infinite loops से बचने के लिए सावधानी के साथ):
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
             throw e; // Max retries के बाद फिर से throw करें
         }
     }
     ```

2. **संगत लॉकिंग क्रम सुनिश्चित करें (Ensure Consistent Locking Order)**:
   Tables को एक ही क्रम में access करने के लिए code को modify करें (जैसे, हमेशा `orders` से पहले `users` को lock करें)।

3. **लॉक अवधि को कम से कम करें (Minimize Lock Duration)**:
   Non-transactional logic को `@Transactional` boundaries के बाहर move करके transactions को छोटा रखें।

4. **उपयुक्त Isolation Levels का उपयोग करें (Use Appropriate Isolation Levels)**:
   यदि एप्लिकेशन की आवश्यकताएं अनुमति देती हैं तो transaction isolation level को adjust करें (जैसे, `SERIALIZABLE` के बजाय `READ_COMMITTED`), हालांकि यह deadlocks को पूरी तरह से खत्म नहीं करता है।

5. **डेटाबेस-विशिष्ट सुविधाएँ (Database-Specific Features)**:
   - Deadlock detection logging को enable करें (जैसे, MySQL का `innodb_print_all_deadlocks`)।
   - जहां संभव हो row-level locking का उपयोग करें, हालांकि row level पर भी deadlocks हो सकते हैं।

#### Deadlocks का विश्लेषण (Analyzing Deadlocks)
Specific deadlock का निदान करने के लिए:
- **डेटाबेस लॉग्स (Database Logs)**: Deadlock details (जैसे, involved transactions, locked resources) के लिए database server logs check करें।
- **Spring Debugging**: Spring transaction logging को enable करें (`logging.level.org.springframework.transaction=DEBUG`) ताकि transaction events का पता लगाया जा सके।
- **एप्लिकेशन ट्रेसिंग (Application Tracing)**: Exception की ओर ले जाने वाले operations के sequence को log करें।

### निष्कर्ष (Conclusion)

`SqlTransactionRollbackException` को पकड़ने के लिए, transactional operation को invoke करने वाले code के चारों ओर एक `try-catch` block रखें, जैसे कि `@Transactional` से चिह्नित service method। Database lock के लिए - संभवतः एक deadlock - सुनिश्चित करें कि transactions resources को एक संगत क्रम में access करते हैं, transactions को छोटा रखें, और transient failures के लिए retry logic पर विचार करें। Deadlocks cyclic lock dependencies के कारण होते हैं, और जबकि databases उन्हें एक victim transaction को roll back करके resolve करते हैं, proactive design उनकी घटना को कम कर सकता है।

---

जब एक Spring एप्लिकेशन में `SqlTransactionRollbackException` से निपटते हैं - विशेष रूप से एक ऐसे परिदृश्य में जहां एक अन्य transaction एक lock रखता है, जिससे connection fetch failures होती हैं और लगभग 20 failed attempts के बाद exception thrown होती है - तो इस issue को handle करने और संभावित रूप से कम करने के लिए आप कई strategies अपना सकते हैं। यह exception आमतौर पर transaction rollback के दौरान उत्पन्न होती है जब database locks या concurrency issues operation को सफलतापूर्वक पूरा करने से रोकते हैं। नीचे, मैं इस समस्या के समाधान के लिए एक व्यापक दृष्टिकोण रेखांकित करता हूं, जो prevention, handling, और recovery पर केंद्रित है।

---

### समस्या को समझना (Understanding the Problem)
`SqlTransactionRollbackException` (या Spring में अधिक संभावना `TransactionRollbackException` की, क्योंकि पूर्व Spring का standard exception नहीं है) इंगित करता है कि एक transaction को roll back नहीं किया जा सका, संभवतः क्योंकि एक अन्य transaction आवश्यक database resources पर lock रखता है। यह lock contention transaction manager को कनेक्शन fetch करने में विफल होने का कारण बनता है, कई बार (आपके मामले में लगभग 20 बार) retry करता है, और अंततः exception throw करता है जब rollback पूरा नहीं किया जा सकता है। यह एक concurrency issue, जैसे lock contention या deadlock, का सुझाव देता है, जो Spring के transaction management द्वारा internally retry करने और हार मानने से पहले compounded हो जाता है।

---

### Exception को Handle करने की Strategies (Strategies to Handle the Exception)

#### 1. Short Transactions के साथ Lock Contention को कम से कम करें (Minimize Lock Contention with Short Transactions)
Long-running transactions lock contention की संभावना बढ़ाते हैं, क्योंकि वे extended periods के लिए database locks रखते हैं, अन्य transactions को block करते हैं। इस जोखिम को कम करने के लिए:

- **Short-Lived Transactions डिजाइन करें (Design Short-Lived Transactions)**: सुनिश्चित करें कि आपकी `@Transactional` methods अपने database operations जल्दी से करें और promptly commit या roll back करें। Transaction scope के भीतर time-consuming business logic या external calls को शामिल करने से बचें।
- **बड़े Transactions को तोड़ें (Break Down Large Transactions)**: यदि एक single transaction में multiple operations शामिल हैं, तो जहां संभव हो इसे छोटे, independent transactions में विभाजित करने पर विचार करें। इससे locks को रखे जाने की अवधि कम हो जाती है।

#### 2. डेटाबेस Queries को Optimize करें (Optimize Database Queries)
Poorly optimized queries आवश्यकता से अधिक समय तक locks रखकर lock contention को बढ़ा सकते हैं। इसे संबोधित करने के लिए:

- **Queries का विश्लेषण और Optimization करें (Analyze and Optimize Queries)**: Slow queries की पहचान करने के लिए database profiling tools का उपयोग करें। उपयुक्त indexes जोड़ें, unnecessary table scans से बचें, और locked rows के scope को कम से कम करें (जैसे, precise `WHERE` clauses का उपयोग करें)।
- **Overly Broad Locks से बचें (Avoid Overly Broad Locks)**: `SELECT ... FOR UPDATE` जैसे statements के साथ सावधान रहें, जो explicitly rows को lock करते हैं और अन्य transactions को block कर सकते हैं। उनका उपयोग केवल तभी करें जब आवश्यक हो और सुनिश्चित करें कि वे कम से कम rows को प्रभावित करते हैं।

#### 3. Transaction Settings को Adjust करें (Adjust Transaction Settings)
Spring का `@Transactional` annotation transaction behavior को fine-tune करने के लिए attributes प्रदान करता है। जबकि ये सीधे तौर पर rollback failures को हल नहीं करेंगे, वे concurrency को manage करने में मदद कर सकते हैं:

- **Isolation Level**: Default isolation level (`DEFAULT`) आमतौर पर database के default (अक्सर `READ_COMMITTED`) पर मैप होता है। इसे `REPEATABLE_READ` या `SERIALIZABLE` तक बढ़ाने से data consistency सुनिश्चित हो सकती है लेकिन lock contention खराब हो सकता है। इसके विपरीत, `READ_COMMITTED` या lower (यदि supported) के साथ बने रहने से locking issues कम हो सकते हैं, आपके use case के आधार पर। सही संतुलन खोजने के लिए सावधानीपूर्वक test करें।
- **Propagation Behavior**: Default `REQUIRED` एक existing transaction में शामिल होता है या एक नया शुरू करता है। `REQUIRES_NEW` का उपयोग current transaction को suspend करता है और एक fresh transaction शुरू करता है, संभावित रूप से locked transaction के साथ conflicts से बचता है। हालांकि, यह rollback-specific issues को संबोधित नहीं कर सकता है।
- **Timeout**: `@Transactional(timeout = 10)` में एक `timeout` value (सेकंड में) सेट करें ताकि transactions तेजी से fail हो जाएं यदि वे locks की प्रतीक्षा कर रहे हैं। यह prolonged retries को रोकता है लेकिन root cause को ठीक नहीं करता है।

उदाहरण:
```java
@Transactional(timeout = 5, propagation = Propagation.REQUIRES_NEW)
public void performDatabaseOperation() {
    // आपका code यहाँ
}
```

#### 4. Retry Logic लागू करें (सावधानी के साथ) (Implement Retry Logic (With Caution))
चूंकि exception multiple internal retries (लगभग 20) के बाद होती है, Spring का transaction manager संभवतः पहले से ही issue को handle करने का प्रयास कर रहा है। हालांकि, आप एक higher level पर custom retry logic लागू कर सकते हैं:

- **Spring Retry का उपयोग करना (Using Spring Retry)**:
  `TransactionRollbackException` पर retry करने के लिए एक service method को `@Retryable` से annotate करें। Attempts की संख्या और retries के बीच delay निर्दिष्ट करें। Retries exhaust होने के बाद failure को handle करने के लिए इसे एक `@Recover` method के साथ pair करें।
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
          // Database operations जो fail हो सकते हैं
      }

      @Recover
      public void recover(TransactionRollbackException e) {
          // Error log करें, admins को notify करें, या corrective action लें
          System.err.println("All retries failed: " + e.getMessage());
      }
  }
  ```
  **नोट**: प्रत्येक retry एक नया transaction शुरू करता है, जो ideal नहीं हो सकता है यदि retries में atomicity आवश्यक है। यदि संभव हो तो इसे `@Transactional` method के बाहर apply करें।

- **TransactionTemplate के साथ Manual Retry (Manual Retry with TransactionTemplate)**:
  अधिक नियंत्रण के लिए, अपने transactional code को एक retry loop में wrap करने के लिए `TransactionTemplate` का उपयोग करें:
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
                          // Transactional code यहाँ
                      }
                  });
                  return; // सफलता, loop से बाहर निकलें
              } catch (TransactionRollbackException e) {
                  if (i == MAX_RETRIES - 1) {
                      throw e; // Max retries के बाद फिर से throw करें
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
  **सावधानी**: Retrying issue को हल नहीं कर सकता है यदि lock बना रहता है, और यदि rollback से पहले partial changes apply हो जाते हैं तो यह inconsistent states की ओर ले जा सकता है। सुनिश्चित करें कि retries idempotent या safe हैं।

#### 5. Exception को Gracefully Handle करें (Handle the Exception Gracefully)
यदि persistent locks के कारण rollback विफल हो जाता है, तो database state inconsistent हो सकता है, जिसके लिए सावधानीपूर्वक handling की आवश्यकता होती है:

- **पकड़ें और लॉग करें (Catch and Log)**:
  Transactional call को एक try-catch block में wrap करें, exception को log करें, और administrators को notify करें:
  ```java
  try {
      myService.performTransactionalWork();
  } catch (TransactionRollbackException e) {
      // Error लॉग करें
      logger.error("Transaction rollback failed after retries: " + e.getMessage(), e);
      // Admins को notify करें (जैसे, email या monitoring system के माध्यम से)
      alertSystem.notify("Critical: Transaction rollback failure");
      // Gracefully fail करें या safe state में प्रवेश करें
      throw new RuntimeException("Operation failed due to transaction issues", e);
  }
  ```

- **सुरक्षित रूप से विफल करें (Fail Safely)**: यदि transaction की state अनिश्चित है, तो इस पर निर्भर further operations को रोकें और manual intervention की आवश्यकता का संकेत दें।

#### 6. डेटाबेस सुविधाओं का लाभ उठाएं (Leverage Database Features)
Lock-related issues को कम करने के लिए database settings को tune करें:

- **Lock Timeout**: Lock waits पर quickly timeout करने के लिए database को configure करें (जैसे, SQL Server में `SET LOCK_TIMEOUT 5000` या MySQL में `innodb_lock_wait_timeout`)। यह transaction को जल्दी fail कर देता है, जिससे Spring exception को sooner handle कर सकता है।
- **Deadlock Detection**: सुनिश्चित करें कि database की deadlock detection enabled और configured है ताकि conflicts को automatically एक transaction को roll back करके resolve किया जा सके।
- **Optimistic Locking**: यदि JPA का उपयोग कर रहे हैं, तो optimistic locking का उपयोग करने के लिए entities पर `@Version` apply करें, जिससे physical lock contention कम होता है:
  ```java
  @Entity
  public class MyEntity {
      @Id
      private Long id;
      @Version
      private Integer version;
      // अन्य fields
  }
  ```
  यह conflict detection को commit time पर shift कर देता है लेकिन सीधे तौर पर rollback failures को संबोधित नहीं कर सकता है।

#### 7. Monitor और Investigate करें (Monitor and Investigate)
इस exception की frequent occurrences एक underlying issue का संकेत देती हैं:

- **Monitoring जोड़ें (Add Monitoring)**: इन exceptions और उनकी frequency को track करने के लिए Spring Boot Actuator या logging framework जैसे tools का उपयोग करें।
- **Logs का विश्लेषण करें (Analyze Logs)**: Patterns (जैसे, locks का कारण बनने वाले specific queries या transactions) के लिए database और application logs check करें।
- **Concurrency को Tune करें (Tune Concurrency)**: यदि contention बना रहता है, तो अपने एप्लिकेशन के concurrency model या database design पर पुनर्विचार करें।

---

### Rollback क्यों विफल होता है (Why Rollback Fails)
20 attempts के बाद rollback failure यह सुझाव देती है कि Spring का transaction manager rollback operation को retry करता है जब यह एक locked resource या lost connection का सामना करता है, अंततः हार मान लेता है। यह निम्न से उपत्पन्न हो सकता है:

- **Persistent Locks**: एक अन्य transaction एक lock रखता है जो retry window के भीतर release नहीं होता है।
- **Connection Issues**: Database connection pool (जैसे, HikariCP) कनेक्शन fetch करने के लिए अपने retries exhaust कर देता है।
- **Database Misconfiguration**: Database या connection pool में timeout या retry settings बहुत aggressive या insufficient हैं।

---

### अनुशंसित दृष्टिकोण (Recommended Approach)
यहां उपरोक्त strategies को जोड़ते हुए एक व्यावहारिक समाधान दिया गया है:

1. **Transactions और Queries को Optimize करें**: Lock duration को कम करने के लिए transactions को छोटा और queries efficient रखें।
2. **Transaction Timeout सेट करें**: यदि locks बने रहते हैं तो fast fail करने के लिए `@Transactional(timeout = 5)` का उपयोग करें।
3. **Retry और Recovery के साथ Handle करें**:
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
                       logger.error("Failed after {} attempts: {}", maxAttempts, e.getMessage(), e);
                       alertSystem.notify("Transaction rollback failure");
                       throw e;
                   }
                   try {
                       Thread.sleep(1000); // Retry करने से पहले प्रतीक्षा करें
                   } catch (InterruptedException ie) {
                       Thread.currentThread().interrupt();
                   }
               }
           }
       }

       @Transactional
       private void performTransactionalWork() {
           // Database operations
           repository.save(someEntity);
       }
   }
   ```
4. **Monitor और Adjust करें**: Exception को log करें, alerts सेट करें, और lock contention के causes की जांच करें।

---

### निष्कर्ष (Conclusion)
Spring में `SqlTransactionRollbackException` को handle करने के लिए जब एक अन्य transaction lock रखता है, जिससे connection fetch failures और repeated attempts होती हैं, तो short transactions और optimized queries के माध्यम से lock contention को कम करने, आवश्यकतानुसार transaction settings को adjust करने, एक higher level पर सतर्क retry logic लागू करने, और exception को appropriately logging और notifying करके handle करने पर ध्यान केंद्रित करें। यह system stability और data integrity सुनिश्चित करता है जबकि monitoring और tuning के माध्यम से root cause को समय के साथ संबोधित करता है।

---

IBM DB2 Java driver (विशेष रूप से JDBC driver) के साथ काम करते समय, robust database interaction के लिए transaction rollback scenarios को handle करना आवश्यक है। Query `SqlTransactionRollbackException` को संदर्भित करती है, जो एक slight misspelling प्रतीत होती है। Standard JDBC में, विशेष रूप से version 4.0 onward से (modern IBM DB2 drivers जैसे `db2jcc4.jar` द्वारा supported), correct exception **`SQLTransactionRollbackException`** है। यह exception `SQLException` की एक subclass है और तब thrown होती है जब एक database transaction automatically rolled back हो जाती है, जैसे कि deadlocks या timeouts के मामलों में।

यहां बताया गया है कि IBM DB2 JDBC driver का उपयोग करते समय अपने Java code में `SQLTransactionRollbackException` को effectively कैसे handle करें:

### Exception को Handle करने का दृष्टिकोण (Approach to Handling the Exception)

1. **Try-Catch Block का उपयोग करें (Use a Try-Catch Block)**: अपने transactional database operations को एक `try` block में wrap करें और `SQLTransactionRollbackException` को catch करें ताकि उन मामलों को handle किया जा सके जहां transaction database द्वारा rolled back हो जाती है।
2. **उचित कार्रवाई करें (Take Appropriate Action)**: अपने एप्लिकेशन की आवश्यकताओं के आधार पर, आप error को log कर सकते हैं, transaction को retry कर सकते हैं (यदि issue transient है, जै