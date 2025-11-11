---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة جافا لـ JWT
translated: true
type: note
---

لاستخدام مكتبة `com.nimbusds.jwt` في جافا لاستخراج معلومات مثل تاريخ انتهاء الصلاحية، وتاريخ الإصدار، والمطالبات الأخرى من رمز ويب JSON (JWT)، اتبع الخطوات الموضحة أدناه. يفترض هذا الحل أنك تعمل مع JWT موقَّع، وهو النوع الأكثر شيوعًا، ويركز على تقديم نهج عملي واضح لتحقيق هدفك.

---

## المتطلبات الأساسية

أولاً، تأكد من إضافة مكتبة Nimbus JOSE + JWT إلى مشروعك. إذا كنت تستخدم Maven، فقم بتضمين الاعتمادية التالية في ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- استبدل بأحدث إصدار -->
</dependency>
```

يمكنك التحقق من أحدث إصدار على [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt).

---

## خطوات استخراج تاريخ انتهاء الصلاحية، وتاريخ الإصدار، والمطالبات الأخرى

إليك كيف يمكنك تحليل JWT واسترداد تاريخ انتهاء الصلاحية، وتاريخ الإصدار، والمطالبات الإضافية باستخدام مكتبة `com.nimbusds.jwt`:

1.  **تحليل سلسلة JWT**: استخدم الدالة `SignedJWT.parse()` لتحويل سلسلة JWT إلى كائن `SignedJWT`.
2.  **الحصول على مجموعة المطالبات**: الوصول إلى المطالبات (أزواج المفتاح-القيمة) من JWT باستخدام `getJWTClaimsSet()`.
3.  **استخراج مطالبات محددة**:
    *   استخدم `getExpirationTime()` للحصول على تاريخ انتهاء الصلاحية (مطالبة `exp`).
    *   استخدم `getIssueTime()` للحصول على تاريخ الإصدار (مطالبة `iat`).
    *   استخدم `getSubject()` أو `getClaim()` أو دوال أخرى للمطالبات الإضافية.
4.  **معالجة الأخطاء**: لف منطق التحليل داخل كتلة try-catch لإدارة مشاكل التحليل المحتملة.

---

## مثال على الكود

أدناه مثال كامل في جافا يوضح كيفية استخراج تاريخ انتهاء الصلاحية، وتاريخ الإصدار، ومطالبة إضافية (مثل subject) من JWT:

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // استبدل هذا بسلسلة JWT الفعلية الخاصة بك
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // الخطوة 1: تحليل سلسلة JWT
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // الخطوة 2: الحصول على مجموعة المطالبات
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // الخطوة 3: استخراج تواريخ انتهاء الصلاحية وتواريخ الإصدار
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // مثال على مطالبة أخرى

            // الخطوة 4: عرض النتائج
            if (expirationDate != null) {
                System.out.println("Expiration date: " + expirationDate);
            } else {
                System.out.println("No expiration date set.");
            }

            if (issuedDate != null) {
                System.out.println("Issued date: " + issuedDate);
            } else {
                System.out.println("No issued date set.");
            }

            if (subject != null) {
                System.out.println("Subject: " + subject);
            } else {
                System.out.println("No subject set.");
            }

        } catch (ParseException e) {
            System.out.println("Invalid JWT: " + e.getMessage());
        }
    }
}
```

---

## شرح الكود

### 1. **الاستيرادات**
*   `SignedJWT`: يمثل JWT موقَّعًا ويوفر دوال لتحليله ومعالجته.
*   `JWTClaimsSet`: يحتوي على المطالبات من payload الـ JWT.
*   `ParseException`: يتم إلقاؤها إذا كانت سلسلة JWT غير صحيحة أو لا يمكن تحليلها.
*   `Date`: يستخدم لتمثيل وقت انتهاء الصلاحية ووقت الإصدار.

### 2. **تحليل JWT**
*   تقوم الدالة `SignedJWT.parse(jwtString)` بأخذ سلسلة JWT (مثل `header.payload.signature`) وإرجاع كائن `SignedJWT`. إذا كان JWT غير صالح، فإنها تلقى استثناء `ParseException`.

### 3. **الوصول إلى المطالبات**
*   `signedJWT.getJWTClaimsSet()` تسترجع مجموعة المطالبات، التي تحتوي على جميع المطالبات من payload الـ JWT.

### 4. **استخراج مطالبات محددة**
*   **`getExpirationTime()`**: تُرجع مطالبة `exp` ككائن `Date` (أو `null` إذا لم تكن موجودة). هذا يمثل موعد انتهاء صلاحية الرمز.
*   **`getIssueTime()`**: تُرجع مطالبة `iat` ككائن `Date` (أو `null` إذا لم تكن موجودة). هذا يشير إلى وقت إصدار الرمز.
*   **`getSubject()`**: تُرجع مطالبة `sub` كـ `String` (أو `null` إذا لم تكن موجودة)، وهي مثال على مطالبة قياسية أخرى. يمكنك أيضًا استخدام `getClaim("key")` لاسترداد مطالبات مخصصة ككائن `Object`.

### 5. **معالجة الأخطاء**
*   تضمن كتلة try-catch أنه في حالة كون JWT تالفًا أو غير صالح، يقوم البرنامج بمعالجة الخطأ بأمان من خلال طباعة رسالة خطأ.

---

## ملاحظات

*   **JWT الموقَّعة مقابل غير الموقَّعة**: يستخدم هذا المثال `SignedJWT` للرموز الموقَّعة. إذا كان لديك JWT غير موقَّع، فاستخدم `PlainJWT.parse(jwtString)` بدلاً من ذلك. للحصول على نهج أكثر عمومية، يمكنك استخدام `JWTParser.parse(jwtString)` ثم التحقق من النوع (`SignedJWT`، `PlainJWT`، إلخ) باستخدام instanceof.
*   **التحقق من التوقيع**: هذا الكود لا يتحقق من توقيع JWT. في بيئة الإنتاج، يجب عليك التحقق من التوقيع باستخدام `signedJWT.verify(verifier)` مع مفتاح مناسب لضمان صحة الرمز.
*   **التحقق من القيم الفارغة**: تحقق دائمًا من `null` عند استرداد المطالبات، لأنها اختيارية وقد لا تكون موجودة في كل JWT.
*   **المطالبات المخصصة**: للوصول إلى المطالبات غير القياسية، استخدم `claimsSet.getClaim("claimName")`، والتي تُرجع `Object` يمكنك تحويله إلى النوع المناسب (مثل `String`، `Integer`).

---

## نموذج للإخراج

لـ JWT المثال أعلاه:
```
Expiration date: Wed Jan 17 19:52:02 UTC 2018
Issued date: Wed Jan 17 19:50:22 UTC 2018
Subject: 1234567890
---

يوفر هذا النهج طريقة بسيطة وفعالة لاستخراج تاريخ انتهاء الصلاحية، وتاريخ الإصدار، والمطالبات الأخرى من JWT باستخدام مكتبة `com.nimbusds.jwt`. استبدل `jwtString` بالرمز الخاص بك وقم بتكييف الكود ليناسب احتياجاتك المحددة!