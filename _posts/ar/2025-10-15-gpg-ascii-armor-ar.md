---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: شرح الترميز الآسكي لـ GPG
translated: true
type: note
---

في GPG (GNU Privacy Guard)، يشير مصطلح "armor" إلى الترميز ASCII، وهو تنسيق يقوم بتحويل البيانات الثنائية لـ OpenPGP (مثل الملفات المشفرة، أو التواقيع، أو المفاتيح) إلى تمثيل نصي يمكن للبشر قراءته. يُعد هذا مفيدًا لنقل البيانات عبر قنوات نصية فقط، مثل البريد الإلكتروني، دون حدوث تلف — على غرار كيفية عمل uuencode أو base64، ولكن مع إضافة رؤوس (مثل "-----BEGIN PGP MESSAGE-----") ومجموعات تدقيق للسلامة.

يمكنك تمكينه باستخدام الخيار `--armor` (أو `-a`) أثناء استخدام أوامر مثل التشفير (`gpg -a -e file.txt`) أو تصدير المفتاح (`gpg --armor --export keyid`)، والذي يُخرج النتيجة بهذا التنسيق النصي المُدرع بدلاً من البيانات الثنائية الخام.

## المراجع
- [What is the armored option for in GnuPG?](https://unix.stackexchange.com/questions/623375/what-is-the-armored-option-for-in-gnupg)
- [Exchanging keys - GnuPG](https://www.gnupg.org/gph/en/manual/x56.html)
- [13. ASCII armor - Notes on OpenPGP](https://openpgp.dev/book/armor.html)
- [GPG Input and Output (Using the GNU Privacy Guard)](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Input-and-Output.html)