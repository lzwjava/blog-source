---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة JWT Java
translated: true
---

لاستخدام مكتبة `com.nimbusds.jwt` في Java لاستخراج معلومات مثل تاريخ انتهاء الصلاحية، تاريخ الإصدار، ومطالب أخرى من رمز الويب JSON (JWT)، اتبع الخطوات التالية. يتوقع هذا الحل أنك تعمل مع JWT موقعة، وهو النوع الأكثر شيوعًا، ويركز على تقديم نهج واضح وممارس لتحقيق هدفك.

---

## المتطلبات الأساسية

أولاً، تأكد من إضافة مكتبة Nimbus JOSE + JWT إلى مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- استبدل بالنسخة الأخيرة -->
</dependency>
```

يمكنك التحقق من أحدث النسخة على [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt).

---

## خطوات استخراج تاريخ انتهاء الصلاحية، تاريخ الإصدار، ومطالب أخرى

هنا كيفية تحليل JWT واستخراج تاريخ انتهاء الصلاحية، تاريخ الإصدار، ومطالب إضافية باستخدام مكتبة `com.nimbusds.jwt`:

1. **تحليل سلسلة JWT**: استخدم طريقة `SignedJWT.parse()` لتحويل سلسلة JWT إلى كائن `SignedJWT`.
2. **الحصول على مجموعة المطالب**: الوصول إلى المطالب (أزواج المفتاح-القيمة) من JWT باستخدام `getJWTClaimsSet()`.
3. **استخراج المطالب المحددة**:
   - استخدم `getExpirationTime()` للحصول على تاريخ انتهاء الصلاحية (`exp` المطلب).
   - استخدم `getIssueTime()` للحصول على تاريخ الإصدار (`iat` المطلب).
   - استخدم `getSubject()`، `getClaim()`، أو طرق أخرى للحصول على المطالب الإضافية.
4. **معالجة الأخطاء**: احاط منطق التحليل في كتلة try-catch لإدارة مشاكل التحليل المحتملة.

---

## مثال من الكود

هنا مثال كامل من Java يوضح كيفية استخراج تاريخ انتهاء الصلاحية، تاريخ الإصدار، ومطلب إضافي (مثل الموضوع) من JWT:

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // استبدل هذه السلسلة بسلسلة JWT الفعلية الخاصة بك
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // الخطوة 1: تحليل سلسلة JWT
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // الخطوة 2: الحصول على مجموعة المطالب
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // الخطوة 3: استخراج تاريخ انتهاء الصلاحية وتاريخ الإصدار
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // مثال على مطلب آخر

            // الخطوة 4: عرض النتائج
            if (expirationDate != null) {
                System.out.println("تاريخ انتهاء الصلاحية: " + expirationDate);
            } else {
                System.out.println("لم يتم تعيين تاريخ انتهاء الصلاحية.");
            }

            if (issuedDate != null) {
                System.out.println("تاريخ الإصدار: " + issuedDate);
            } else {
                System.out.println("لم يتم تعيين تاريخ الإصدار.");
            }

            if (subject != null) {
                System.out.println("الموضوع: " + subject);
            } else {
                System.out.println("لم يتم تعيين الموضوع.");
            }

        } catch (ParseException e) {
            System.out.println("JWT غير صالح: " + e.getMessage());
        }
    }
}
```

---

## شرح الكود

### 1. **الاستيرادات**
- `SignedJWT`: يمثل JWT الموقعة ويوفر طرقًا لتحليلها ومعالجتها.
- `JWTClaimsSet`: يحتوي على المطالب من حمولات JWT.
- `ParseException`: يُلقى إذا كانت سلسلة JWT غير صحيحة أو لا يمكن تحليلها.
- `Date`: يستخدم لتمثيل أوقات انتهاء الصلاحية وتاريخ الإصدار.

### 2. **تحليل JWT**
- طريقة `SignedJWT.parse(jwtString)` تأخذ سلسلة JWT (مثل `header.payload.signature`) وتعيد كائن `SignedJWT`. إذا كان JWT غير صالح، فإنه يلقى `ParseException`.

### 3. **الوصول إلى المطالب**
- `signedJWT.getJWTClaimsSet()` يسترجع مجموعة المطالب، والتي تحتوي على جميع المطالب من حمولات JWT.

### 4. **استخراج المطالب المحددة**
- **`getExpirationTime()`**: يعيد المطلب `exp` ككائن `Date` (أو `null` إذا لم يكن موجودًا). يمثل هذا متى ينتهي السجل.
- **`getIssueTime()`**: يعيد المطلب `iat` ككائن `Date` (أو `null` إذا لم يكن موجودًا). يشير هذا إلى متى تم إصدار السجل.
- **`getSubject()`**: يعيد المطلب `sub` كسلسلة (أو `null` إذا لم يكن موجودًا)، مثال على مطلب قياسي آخر. يمكنك أيضًا استخدام `getClaim("key")` لاسترجاع المطالب المخصصة ككائن.

### 5. **معالجة الأخطاء**
- كتلة try-catch تضمن أن إذا كان JWT غير صحيح أو غير صالح، فإن البرنامج يعالج الخطأ بشكل رقيق من خلال طباعة رسالة خطأ.

---

## ملاحظات

- **JWT الموقعة مقابل غير الموقعة**: يستخدم هذا المثال `SignedJWT` للرموز الموقعة. إذا كان لديك JWT غير موقعة، استخدم `PlainJWT.parse(jwtString)` بدلاً من ذلك. لمزيد من النهج العام، يمكنك استخدام `JWTParser.parse(jwtString)` ثم التحقق من النوع (`SignedJWT`، `PlainJWT`، إلخ.) باستخدام `instanceof`.
- **تحقق من التوقيع**: لا يثبت هذا الكود توقيع JWT. في بيئة الإنتاج، يجب عليك التحقق من التوقيع باستخدام `signedJWT.verify(verifier)` مع مفتاح مناسب لضمان صحة السجل.
- **التحقق من `null`**: دائمًا تحقق من `null` عند استرجاع المطالب، حيث أنها اختيارية ويمكن أن لا تكون موجودة في كل JWT.
- **المطالب المخصصة**: لاسترجاع المطالب غير القياسية، استخدم `claimsSet.getClaim("claimName")`، الذي يعيد كائن يمكنك إرجاعه إلى النوع المناسب (مثل `String`، `Integer`).

---

## مثال على الإخراج

لسلسلة JWT المثال أعلاه:
```
تاريخ انتهاء الصلاحية: Wed Jan 17 19:52:02 UTC 2018
تاريخ الإصدار: Wed Jan 17 19:50:22 UTC 2018
الموضوع: 1234567890
```

---

يوفر هذا النهج طريقة بسيطة وفعالة لاستخراج تاريخ انتهاء الصلاحية، تاريخ الإصدار، ومطالب أخرى من JWT باستخدام مكتبة `com.nimbusds.jwt`. استبدل `jwtString` برمزك الخاص واستعد الكود حسب احتياجاتك!