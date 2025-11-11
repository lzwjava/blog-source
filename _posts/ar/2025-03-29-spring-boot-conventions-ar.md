---
audio: false
generated: true
lang: ar
layout: post
title: اتفاقيات ترميز جافا باستخدام سبرينغ بوت
translated: true
type: note
---

## 1. المبادئ الأساسية
- اتبع اصطلاحات كود جافا القياسية
- أولوية للقراءة وسهولة الصيانة
- الاتساق عبر نظام سبرينغ البيئي
- المحاذاة مع أفضل ممارسات جافا الأساسية

## 2. تنسيق الكود

### الإرشادات العامة
- استخدم التنسيق الافتراضي لـ IntelliJ IDEA
- مسافة بادئة 4 فراغات (ليس علامات Tab)
- أقصى طول للسطر 120 حرفًا
- استخدم نمط الأقواس القياسي في جافا

### قواعد تنسيق محددة
- سطر فارغ بين الدوال
- لا توجد مسافات زائدة في نهاية السطور
- استخدم نهايات الأسطر بنمط Unix (LF)

## 3. اصطلاحات التسمية

### تسمية الفئات
- استخدم أسماء وصفيّة وذات معنى
- استخدم UpperCamelCase
- أمثلة:
  - `ConfigurationProperties`
  - `AutoConfigurationImportSelector`
  - `SpringApplication`

### تسمية الدوال
- استخدم lowerCamelCase
- فعل أو عبارات فعلية
- أمثلة:
  - `configure()`
  - `registerBeanDefinitions()`
  - `isEnabledByDefault()`

## 4. ممارسات التعليقات التوضيحية (Annotations)

### ترتيب التعليقات التوضيحية
- الترتيب القياسي للتعليقات التوضيحية:
  1. تعليقات Override (`@Override`)
  2. تعليقات النطاق (`@Component`، `@Service`)
  3. تعليقات حقن التبعية
  4. تعليقات المعاملات
  5. تعليقات المشروع المخصصة

### وضع التعليقات التوضيحية
```java
@Component
@Transactional
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

## 5. حقن التبعية

### طريقة الحقن المفضلة
- حقن عبر المُنشئ
- تجنب الحقن عبر الحقول
- استخدم `@Autowired` على المُنشئ

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

## 6. التسجيل (Logging)
- استخدم SLF4J للتسجيل
- استخدم `private static final Logger` أو Lombok's `@Slf4j`

```java
@Slf4j
@Service
public class UserService {
    public void processUser(User user) {
        log.info("Processing user: {}", user.getUsername());
    }
}
```

## 7. معالجة الأخطاء
- استخدم استثناءات محددة
- قدم رسائل خطأ ذات معنى
- استخدم `@ControllerAdvice` للمعالجة العالمية للاستثناءات

## 8. التهيئة
- استخدم `application.yml` بدلاً من `application.properties`
- استخدم تهيئات محددة حسب الـ profile
- خارج قيم التهيئة

## 9. الاختبار
- استخدم JUnit 5
- استفد من أدوات اختبار Spring Boot
- اتبع نمط Arrange-Act-Assert

## 10. موارد إضافية
- [Spring Boot GitHub Coding Style](https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.md)
- [Spring Framework Guidelines](https://github.com/spring-projects/spring-framework/wiki/Code-Style)