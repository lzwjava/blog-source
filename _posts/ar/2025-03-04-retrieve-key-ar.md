---
audio: false
generated: true
lang: ar
layout: post
title: استرجاع مفتاح من نطاق في سياق تنفيذ
translated: true
type: note
---

لاستخدام سياق التنفيذ للحصول على مفتاح من مساحة الاسم، يعتمد النهج على الإطار أو النظام المحدد الذي تعمل معه، حيث أن مصطلحي "سياق التنفيذ" و"مساحة الاسم" يمكن أن يحملا معاني مختلفة حسب السياق. بما أنك لم تحدد إطار عمل معين، سأقدم إرشادات عامة يمكنك تكييفها مع وضعك، إلى جانب مثال عملي يفترض سيناريو شائعًا مثل تطبيق يعتمد على جافا (مثل Spring). إذا كان هذا لا يتطابق مع إعداداتك، فلا تتردد في توضيح المزيد!

### الخطوات العامة لاسترداد مفتاح من مساحة اسم في سياق تنفيذ

يشير سياق التنفيذ عادةً إلى كائن أو بنية تحتفظ ببيانات ذات صلة بتدفق التنفيذ الحالي—مثل مؤشر ترابط، طلب، أو معاملة. وتمثل مساحة الاسم داخل ذلك السياق طريقة لتنظيم البيانات، غالبًا كنطاق مسمى أو مجموعة من أزواج المفتاح-القيمة. إليك كيف يمكنك التعامل مع هذا:

1. **الوصول إلى سياق التنفيذ الحالي**
   - حدد كيفية الحصول على سياق التنفيذ في تطبيقك. قد يكون هذا من خلال:
     - طريقة ثابتة (مثل `Context.getCurrent()`).
     - متغير محلي للمؤشر الترابط (مثل `ThreadLocal<Context>`).
     - حقن التبعية، إذا كان إطار العمل الخاص بك (مثل Spring) يدير السياق.
   - تأكد من أن السياق متاح في نطاق التنفيذ الحالي الخاص بك.

2. **التنقل إلى مساحة الاسم**
   - بمجرد الحصول على السياق، حدد كيف يتم تمثيل مساحات الأسماء. يمكن أن تكون مساحة الاسم:
     - استدعاء طريقة محددة مثل `context.getNamespace("myNamespace")`.
     - خريطة متداخلة أو بنية داخل السياق (مثل `context.get("myNamespace")` تُرجع `Map`).
     - نطاق مباشر إذا لم تكن مساحات الأسماء منفصلة بشكل صريح.
   - تحقق من واجهة برمجة التطبيقات (API) للسياق لفهم هيكله.

3. **استرداد قيمة المفتاح**
   - من مساحة الاسم، استخدم طريقة مثل `get("myKey")` لجلب القيمة المرتبطة بالمفتاح.
   - تعامل مع الحالات التي قد يكون فيها السياق أو مساحة الاسم غير متاح (مثل فحوصات القيمة null).

### مثال: استخدام سياق تنفيذ مخصص في جافا العادية

لنفترض أنك تعمل مع فئة `ExecutionContext` مخصصة في تطبيق جافا، حيث يمكن الوصول إلى السياق بشكل ثابت ويحتوي على مساحات أسماء كمجموعات من أزواج المفتاح-القيمة. إليك كيف يمكنك تنفيذ ذلك:

```java
// فئة سياق التنفيذ الافتراضية
public class ExecutionContext {
    private Map<String, Map<String, Object>> namespaces = new HashMap<>();

    // طريقة ثابتة للحصول على السياق الحالي (يمكن أن تعتمد على ThreadLocal عمليًا)
    private static ExecutionContext current = new ExecutionContext();
    public static ExecutionContext getCurrent() {
        return current;
    }

    // طريقة للحصول على مساحة اسم
    public Map<String, Object> getNamespace(String namespaceName) {
        return namespaces.getOrDefault(namespaceName, new HashMap<>());
    }

    // لأغراض الإعداد (ليس جزءًا من الاسترداد)
    public void setValue(String namespaceName, String key, Object value) {
        namespaces.computeIfAbsent(namespaceName, k -> new HashMap<>()).put(key, value);
    }
}

// مثال الاستخدام
public class MyClass {
    public void retrieveKeyFromNamespace() {
        // الخطوة 1: الوصول إلى سياق التنفيذ الحالي
        ExecutionContext context = ExecutionContext.getCurrent();

        if (context != null) {
            // الخطوة 2: الحصول على مساحة الاسم
            Map<String, Object> ns = context.getNamespace("myNamespace");

            // الخطوة 3: استرداد قيمة المفتاح
            Object value = ns.get("myKey");

            if (value != null) {
                System.out.println("Value: " + value);
            } else {
                System.out.println("Key 'myKey' not found in namespace 'myNamespace'");
            }
        } else {
            System.out.println("Execution context is not available");
        }
    }

    public static void main(String[] args) {
        // الإعداد لأغراض التوضيح
        ExecutionContext.getCurrent().setValue("myNamespace", "myKey", "Hello, World!");
        
        new MyClass().retrieveKeyFromNamespace();
    }
}
```

**النتيجة:**
```
Value: Hello, World!
```

#### الشرح:
- **الخطوة 1:** `ExecutionContext.getCurrent()` توفر السياق الحالي. في تطبيق حقيقي، قد يستخدم هذا `ThreadLocal` لضمان سياقات محددة للمؤشر الترابط.
- **الخطوة 2:** `getNamespace("myNamespace")` تسترجع `Map` تمثل مساحة الاسم.
- **الخطوة 3:** `ns.get("myKey")` تجلب القيمة المرتبطة بـ `"myKey"`.

### مثال بديل: تطبيق ويب Spring

إذا كنت تعمل في تطبيق ويب Spring، فقد يشير "سياق التنفيذ" إلى نطاق الطلب أو الجلسة، ويمكن أن تكون "مساحة الاسم" هي السمات المخزنة في تلك النطاقات. إليك كيفية الوصول إلى مفتاح:

```java
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import javax.servlet.http.HttpServletRequest;

public class MyClass {
    public Object getKeyFromRequestScope(String key) {
        // الخطوة 1: الوصول إلى سياق التنفيذ الحالي (سمات الطلب)
        ServletRequestAttributes attributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        
        if (attributes != null) {
            HttpServletRequest request = attributes.getRequest();
            
            // الخطوة 2: مساحة الاسم هي نطاق الطلب نفسه
            // الخطوة 3: استرداد المفتاح
            return request.getAttribute(key);
        }
        return null; // السياق غير متاح
    }
}
```

- **مساحة الاسم:** هنا، يعمل نطاق الطلب كمساحة الاسم.
- **استرداد المفتاح:** `request.getAttribute(key)` يحصل على القيمة.

لنطاق الجلسة، استبدل `request.getAttribute(key)` بـ `request.getSession().getAttribute(key)`.

### الاعتبارات الرئيسية
- **واجهات برمجة التطبيقات الخاصة بالإطار:** تعتمد الطريقة الدقيقة للوصول إلى السياق ومساحة الاسم على إطار العمل الخاص بك. على سبيل المثال:
  - في Spring، استخدم `ApplicationContext`، أو `RequestContextHolder`، أو `Environment` لسياقات مختلفة.
  - في نظام مخصص، راجع وثائقه.
- **معالجة القيم الفارغة:** تحقق دائمًا من القيم null لتجنب أخطاء وقت التشغيل.
- **سلامة المؤشرات الترابطية:** إذا كان السياق مشتركًا عبر المؤشرات الترابطية، فاحرص على التزامن المناسب أو استخدم التخزين المحلي للمؤشر الترابط.

إذا كنت تستخدم إطار عمل محددًا أو لديك تعريف مختلف لـ "سياق التنفيذ" و"مساحة الاسم" في ذهنك، يرجى تقديم المزيد من التفاصيل، وسأتمكن من تخصيص الإجابة بشكل أكبر! في الوقت الحالي، يجب أن يساعدك هذا النهج العام في استرداد مفتاح من مساحة اسم داخل سياق تنفيذ.