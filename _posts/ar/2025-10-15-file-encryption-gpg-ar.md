---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تشفير الملفات باستخدام جي بي جي
translated: true
type: note
---

### تشفير ملف باستخدام مفتاح GPG الخاص بك

يظهر سرد مفتاح GPG الخاص بك مفتاحًا عامًا (pub) مع البصمة `982740390B5D33E90B6B6133892BC5A4789B71CD` المرتبطة ببريدك الإلكتروني `lzwjava@gmail.com`. لتشفير ملف باستخدام هذا المفتاح (بحيث يمكنك فقط فك تشفيره باستخدام مفتاحك الخاص)، اتبع هذه الخطوات في الطرفية:

1. **انتقل إلى الدليل** الذي يحتوي على الملف الذي تريد تشفيره (مثلًا، إذا كان ملفك هو `secret.txt`):
   ```
   cd ~/path/to/your/file
   ```

2. **قم بتشفير الملف** باستخدام الخيار `--encrypt` وحدد المستلم (بريدك الإلكتروني أو معرف المفتاح). هذا ينشئ ملف `.gpg` مشفر.
   
   - باستخدام بريدك الإلكتروني (أبسط):
     ```
     gpg --encrypt --recipient lzwjava@gmail.com secret.txt
     ```
   
   - باستخدام معرف المفتاح (البصمة الكاملة):
     ```
     gpg --encrypt --recipient 982740390B5D33E90B6B6133892BC5A4789B71CD secret.txt
     ```
   
   هذا يُنتج `secret.txt.gpg`، وهو النسخة المشفرة. الملف الأصلي `secret.txt` يبقى دون تغيير.

3. **تحقق من التشفير** (اختياري):
   ```
   gpg --list-packets secret.txt.gpg
   ```
   هذا يعرض تفاصيل عن الحزمة المشفرة.

### فك تشفير الملف (للرجوع إليه لاحقًا)

لفك تشفيره مرة أخرى (ممكن فقط باستخدام مفتاحك الخاص وكلمة المرور):
```
gpg --decrypt secret.txt.gpg > secret.txt.decrypted
```
أدخل كلمة المرور عندما يُطلب منك.

### نصائح
- **التشفير المتماثل** (إذا كنت لا تحتاج إلى مفتاح مستلم، فقط كلمة مرور): استخدم `gpg -c secret.txt` بدلاً من ذلك.
- **قم بتشفير الملف والتوقيع عليه** (لإثبات أنه منك): أضف `--sign` إلى أمر التشفير، مثل `gpg --encrypt --sign --recipient lzwjava@gmail.com secret.txt`.
- إذا واجهت أخطاء (مثل عدم الثقة بالمفتاح)، شغِّل `gpg --edit-key lzwjava@gmail.com` واستخدم `trust` لتعيينه إلى "ultimate".
- دائمًا احفظ نسخة احتياطية من دليل `~/.gnupg` لسلامة المفاتيح.

لمزيد من التفاصيل، راجع دليل GPG: [GPG Documentation](https://www.gnupg.org/documentation/manpage.html).