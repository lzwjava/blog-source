---
audio: false
generated: true
lang: ar
layout: post
title: الفول المتخصص ديناميكياً حسب المنطقة
translated: true
type: note
---

### فهم المتطلبات

يبدو أنك تبني تطبيق Spring Boot/Java Spring يحتاج إلى دعم مناطق متعددة (أو "جنسيات") مثل سنغافورة (SG) وهونغ كونغ (HK) وتايوان (TW). تريد تحميل أو حقن حبوب (beans) مختلفة ديناميكيًا، خاصة لفئة `CoreController`، باستخدام ميزات مثل `@Autowired` وإدارة الحبوب.

هذا سيناريو شائع لـ **تعدد المستأجرين** أو **التكوينات الخاصة بالمنطقة**، حيث يختلف السلوك (مثل الخدمات، التكوينات، أو المتحكمات) حسب المنطقة. في Spring، لا يمكنك بسهولة تبديل فئات المتحكمات بالكامل أثناء وقت التشغيل، ولكن يمكنك:

1. استخدام **ملفات Spring الشخصية** لتحميل الحبوب الخاصة بكل بيئة (مثل النشرات المنفصلة أو التفعيل لكل منطقة). هذا يتم في وقت الترجمة أو بدء التشغيل.
2. استخدام **الاختيار في وقت التشغيل** مع نمط الإستراتيجية، حيث تقوم بحقن حبوب متعددة (عبر Map) واختيار المناسب بناءً على معلمة طلب، رأس، أو سياق (مثل منطقة المستخدم).

بما أنك ذكرت "تطوير متعدد الجنسيات" وأمثلة مثل SG/HK/TW، سأفترض أن هذا يحتاج إلى التعامل مع مناطق متعددة في نسخة تطبيق واحدة (تبديل في وقت التشغيل). إذا كان الأمر يتعلق بنشر منفصل لكل منطقة، فإن الملفات الشخصية أبسط.

سأشرح كلا النهجين مع أمثلة على الكود. سنفترض أن `CoreController` تعتمد على خدمة خاصة بمنطقة ما (مثل واجهة `CoreService` مع تطبيقات لكل منطقة). بهذه الطريقة، يبقى المتحكم كما هو، لكن سلوكه يتغير عبر الحبوب المحقونة.

### النهج 1: استخدام ملفات Spring الشخصية لتحميل الحبوب الخاصة بمنطقة ما (وقت بدء التشغيل)

هذا مثالي إذا قمت بنشر نسخ منفصلة لكل منطقة (عبر متغيرات البيئة أو خصائص التطبيق). يتم تحميل الحبوب بشكل مشروط بناءً على الملف الشخصي النشط.

#### الخطوة 1: تعريف الواجهة والتطبيقات
أنشئ واجهة للبرمجة المنطقية الخاصة بالمنطقة:

```java
public interface CoreService {
    String getRegionMessage();
}
```

تطبيقات لكل منطقة:

```java
// SgCoreService.java
@Service
@Profile("sg")  // يتم تحميل هذه الحبة فقط إذا كان الملف الشخصي 'sg' نشطًا
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service
@Profile("hk")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service
@Profile("tw")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### الخطوة 2: الإدخال التلقائي في CoreController
```java
@RestController
public class CoreController {
    private final CoreService coreService;

    @Autowired
    public CoreController(CoreService coreService) {
        this.coreService = coreService;
    }

    @GetMapping("/message")
    public String getMessage() {
        return coreService.getRegionMessage();
    }
}
```

#### الخطوة 3: تفعيل الملفات الشخصية
- في `application.properties` أو عبر سطر الأوامر:
  - شغّل باستخدام `--spring.profiles.active=sg` لحبوب سنغافورة.
  - هذا يضمن إنشاء وإدخال حبة `SgCoreService` فقط.
- للشروط المخصصة beyond الملفات الشخصية، استخدم `@ConditionalOnProperty` (مثل `@ConditionalOnProperty(name = "app.region", havingValue = "sg")`).

هذا النهج بسيط لكنه يتطلب إعادة تشغيل أو تطبيقات منفصلة لكل منطقة. غير مناسب للتعامل مع جميع المناطق في نسخة وقت تشغيل واحدة.

### النهج 2: اختيار الحبة في وقت التشغيل باستخدام @Autowired Map (نمط الإستراتيجية)

لتطبيق واحد يتعامل مع مناطق متعددة ديناميكيًا (مثل الرؤوس بناءً على طلب HTTP مثل `X-Region: sg`)، استخدم Map للحبوب. يمكن لـ Spring إدخال جميع التطبيقات تلقائيًا في Map<String, CoreService>، حيث المفتاح هو اسم الحبة.

#### الخطوة 1: تعريف الواجهة والتطبيقات
نفس ما ورد أعلاه، ولكن بدون `@Profile`:

```java
public interface CoreService {
    String getRegionMessage();
}

// SgCoreService.java
@Service("sgCoreService")  // اسم حبة صريح لمفتاح الـ Map
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service("hkCoreService")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service("twCoreService")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### الخطوة 2: الإدخال التلقائي لـ Map في CoreController
```java
@RestController
public class CoreController {
    private final Map<String, CoreService> coreServices;

    @Autowired  // يقوم Spring بتعبئة الـ Map تلقائيًا بجميع حبوب CoreService، باستخدام أسماء الحبوب كمفاتيح
    public CoreController(Map<String, CoreService> coreServices) {
        this.coreServices = coreServices;
    }

    @GetMapping("/message")
    public String getMessage(@RequestHeader("X-Region") String region) {  // أو استخدم @RequestParam إذا كانت معلمة استعلام
        CoreService service = coreServices.get(region.toLowerCase() + "CoreService");
        if (service == null) {
            throw new IllegalArgumentException("Unsupported region: " + region);
        }
        return service.getRegionMessage();
    }
}
```

- هنا، `@Autowired` على الـ Map تحقن جميع تطبيقات `CoreService` تلقائيًا.
- يجب أن تطابق أسماء الحبوب منطق المفتاح الخاص بك (مثل "sgCoreService").
- للاختيار: استخدم رأس/معلمة طلب لتحديد المنطقة. هذا يجعلها ديناميكية لكل طلب.

#### اختياري: استخدام @Qualifier للإدخال المحدد
إذا أردت حقن حبة محددة يدويًا:

```java
@RestController
public class CoreController {
    @Autowired
    @Qualifier("sgCoreService")  // يحقن فقط حبة SG
    private CoreService sgCoreService;

    // ... وبالمثل للآخرين
}
```
لكن هذا ليس ديناميكيًا؛ استخدم الـ Map للتبديل في وقت التشغيل.

#### الخطوة 3: التكوين وأفضل الممارسات
- في الفئة الرئيسية لـ Spring Boot: `@SpringBootApplication` كافية؛ يفحص Spring عن حبوب `@Service`.
- التعامل مع الافتراضيات: أضف خدمة احتياطية إذا لم تطابق أي منطقة.
- للشروط الأكثر تعقيدًا، استخدم `@ConditionalOnExpression` أو شروط `@Conditional` مخصصة على الحبوب.
- أمان الخيوط: بما أن المتحكمات هي singleton افتراضيًا، فإن الـ Map آمن طالما أن الخدمات بلا حالة.
- الاختبار: استخدم `@SpringBootTest` مع طلبات وهمية لاختبار مناطق مختلفة.

### أي نهج تختار؟
- استخدم **الملفات الشخصية** إذا كانت المناطق منفصلة حسب النشر/البيئة (مثل خوادم مختلفة لـ SG/HK/TW).
- استخدم **Map/الإستراتيجية** لتطبيق موحد يتعامل مع جميع المناطق في وقت التشغيل (أكثر مرونة للخدمات المصغرة).

إذا كان هذا لا يتطابق مع إعدادك الدقيق (مثل إذا كانت `CoreController` نفسها تحتاج إلى أن تكون مختلفة حسب المنطقة)، يمكنك استخدام متحكمات متعددة مع شروط `@RequestMapping` أو مصنع لإنشاء المتحكمات ديناميكيًا — لكن هذا نادر وأكثر تعقيدًا.

إذا قدمت المزيد من التفاصيل (مثل كيف يتم تحديد المنطقة)، يمكنني تحسين هذا!