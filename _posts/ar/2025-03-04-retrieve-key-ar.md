---
audio: false
generated: true
lang: ar
layout: post
title: استرجاع مفتاح من مساحة اسم في سياق تنفيذ
translated: true
---

لاستخدام سياق تنفيذ للحصول على مفتاح من مساحة الاسم، يعتمد النهج على الإطار أو النظام الذي تعمل معه، حيث يمكن أن يكون "سجل التنفيذ" و"مساحة الاسم" معاني مختلفة حسب السياق. نظرًا لأنك لم تحدد إطارًا معينًا، سأقدم دليلًا عامًا يمكنك تعديلها حسب احتياجاتك، بالإضافة إلى مثال ملموس على افتراض سيناريو شائع مثل تطبيق مبني على Java (مثل Spring). إذا لم يتطابق هذا مع إعدادك، فلا تتردد في تقديم مزيد من التفاصيل!

### الخطوات العامة لاسترجاع مفتاح من مساحة الاسم في سياق تنفيذ

يشير سياق التنفيذ عادةً إلى كائن أو بنية يحتفظ بالبيانات ذات الصلة بالتدفق الحالي للإنشاء - مثل خيط أو طلب أو معامل. مساحة الاسم في ذلك السياق هي طريقة لتنظيم البيانات، غالبًا كمنطقة اسمية أو مجموعة من أزواج المفتاح والقيمة. إليك كيفية التعامل مع ذلك:

1. **الوصول إلى السياق الحالي للإنشاء**
   - حدد كيفية الحصول على السياق في تطبيقك. قد يكون ذلك من خلال:
     - طريقة ثابتة (مثل `Context.getCurrent()`).
     - متغير محلي للخيط (مثل `ThreadLocal<Context>`).
     - حقن الاعتماد، إذا كان إطارك (مثل Spring) يدير السياق.
   - تأكد من توفر السياق في نطاق تنفيذك الحالي.

2. **التنقل إلى مساحة الاسم**
   - بعد الحصول على السياق، حدد كيفية تمثيل المساحات الاسمية. قد تكون مساحة الاسم:
     - مكالمة محددة مثل `context.getNamespace("myNamespace")`.
     - خريطة مدمجة أو بنية داخل السياق (مثل `context.get("myNamespace")` الذي يعيد `Map`).
     - نطاق مباشر إذا لم يتم فصل المساحات الاسمية بشكل صريح.
   - تحقق من واجهة السياق لفهم بنيته.

3. **استرجاع قيمة المفتاح**
   - من مساحة الاسم، استخدم طريقة مثل `get("myKey")` لاسترجاع القيمة المرتبطة بالمفتاح.
   - قم بمعالجة الحالات التي قد يكون فيها السياق أو مساحة الاسم غير متاحة (مثل التحقق من القيم `null`).

### مثال: استخدام سياق تنفيذ مخصص في Java العادي

فرض أنك تعمل مع فئة `ExecutionContext` مخصصة في تطبيق Java، حيث السياق متاح بشكل ثابت ويحتوي على مساحات الاسم كجماعات أزواج المفتاح والقيمة. إليك كيفية تنفيذ ذلك:

```java
// فئة ExecutionContext الافتراضية
public class ExecutionContext {
    private Map<String, Map<String, Object>> namespaces = new HashMap<>();

    // طريقة ثابتة للحصول على السياق الحالي (قد تكون مبنية على ThreadLocal في الممارسة)
    private static ExecutionContext current = new ExecutionContext();
    public static ExecutionContext getCurrent() {
        return current;
    }

    // طريقة للحصول على مساحة الاسم
    public Map<String, Object> getNamespace(String namespaceName) {
        return namespaces.getOrDefault(namespaceName, new HashMap<>());
    }

    // لأغراض الإعداد (ليس جزء من الاسترجاع)
    public void setValue(String namespaceName, String key, Object value) {
        namespaces.computeIfAbsent(namespaceName, k -> new HashMap<>()).put(key, value);
    }
}

// مثال الاستخدام
public class MyClass {
    public void retrieveKeyFromNamespace() {
        // الخطوة 1: الوصول إلى السياق الحالي للإنشاء
        ExecutionContext context = ExecutionContext.getCurrent();

        if (context != null) {
            // الخطوة 2: الحصول على مساحة الاسم
            Map<String, Object> ns = context.getNamespace("myNamespace");

            // الخطوة 3: استرجاع القيمة للمفتاح
            Object value = ns.get("myKey");

            if (value != null) {
                System.out.println("القيمة: " + value);
            } else {
                System.out.println("لم يتم العثور على المفتاح 'myKey' في مساحة الاسم 'myNamespace'");
            }
        } else {
            System.out.println("سياق التنفيذ غير متاح");
        }
    }

    public static void main(String[] args) {
        // إعداد للتدريب
        ExecutionContext.getCurrent().setValue("myNamespace", "myKey", "مرحبًا بالعالم!");

        new MyClass().retrieveKeyFromNamespace();
    }
}
```

**الخرج:**
```
القيمة: مرحبًا بالعالم!
```

#### شرح:
- **الخطوة 1:** `ExecutionContext.getCurrent()` يوفر السياق الحالي. في تطبيق حقيقي، قد يستخدم `ThreadLocal` لضمان السياقات الخاصة بالخيط.
- **الخطوة 2:** `getNamespace("myNamespace")` يسترجع `Map` يمثل مساحة الاسم.
- **الخطوة 3:** `ns.get("myKey")` يسترجع القيمة المرتبطة بـ `"myKey"`.

### مثال بديل: تطبيق Spring Web

إذا كنت تعمل في تطبيق Spring Web، قد يشير "سياق التنفيذ" إلى نطاق الطلب أو الجلسة، ويمكن أن تكون "مساحة الاسم" هي السجلات المخزنة في تلك الأوساط. إليك كيفية الوصول إلى مفتاح:

```java
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import javax.servlet.http.HttpServletRequest;

public class MyClass {
    public Object getKeyFromRequestScope(String key) {
        // الخطوة 1: الوصول إلى السياق الحالي للإنشاء (سجلات الطلب)
        ServletRequestAttributes attributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();

        if (attributes != null) {
            HttpServletRequest request = attributes.getRequest();

            // الخطوة 2: مساحة الاسم هي النطاق نفسه للطلب
            // الخطوة 3: استرجاع المفتاح
            return request.getAttribute(key);
        }
        return null; // السياق غير متاح
    }
}
```

- **مساحة الاسم:** هنا، النطاق للطلب يعمل كمساحة الاسم.
- **استرجاع المفتاح:** `request.getAttribute(key)` يسترجع القيمة.

لنطاق الجلسة، استبدل `request.getAttribute(key)` بـ `request.getSession().getAttribute(key)`.

### ملاحظات مهمة
- **واجهات محددة للإطار:** الطريقة الدقيقة للوصول إلى السياق والمساحة الاسمية تعتمد على إطارك. على سبيل المثال:
  - في Spring، استخدم `ApplicationContext`، `RequestContextHolder` أو `Environment` لأوساط مختلفة.
  - في نظام مخصص، استشهاد بالوثائق.
- **معالجة القيم `null`:** دائمًا تحقق من القيم `null` لتجنب الأخطاء في وقت التشغيل.
- **الأمان في الخيط:** إذا كان السياق مشتركًا بين الخيوط، تأكد من التزامن المناسب أو استخدام التخزين المحلي للخيط.

إذا كنت تستخدم إطارًا معينًا أو لديك تعريفًا مختلفًا لـ "سياق التنفيذ" و"مساحة الاسم"، يرجى تقديم مزيد من التفاصيل، وسأقوم بتخصيص الإجابة بشكل أكبر! حتى الآن، يجب أن يساعدك هذا النهج العام على استرجاع مفتاح من مساحة الاسم داخل سياق تنفيذ.