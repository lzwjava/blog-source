---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مجموعات بيانات OpenWebText وويكيبيديا عبر التورنت
translated: true
type: note
---

### مجموعات بيانات OpenWebText عبر التورنت

OpenWebText هو نسخة مفتوحة المصدر لمجموعة بيانات WebText من OpenAI، وتتكون من ~38 جيجابايت من النصوص المنظفة المستخرجة من روابط Reddit عالية السمعة (في الغالب صفحات ويب تم جلبها وتصفيتها للحصول على جودة عالية). إنها مجموعة نصوص واسعة النطاق وشائعة الاستخدام لتدريب نماذج اللغة. بينما لا تكون النصوص الكاملة التي تم جلبها متاحة دائمًا بشكل مباشر كتورنت واحد، إليك الخيارات الموثوقة:

- **قائمة عناوين URL (مصفاة، ~480 ميجابايت)**: قائمة مصفاة تحتوي على ~26 مليون عنوان URL تم استخدامها لجلب بيانات OpenWebText. يمكنك استخدام هذه القائمة لتنزيل النصوص ومعالجتها بنفسك.
  - التورنت: [OpenWebText-urls-26M-filtered.xz](https://academictorrents.com/details/f5161721b322bca66ed74da32b963c1066e64312)
  - المصدر: Academic Torrents (يتم توزيعه من قبل المجتمع).

- **قائمة عناوين URL (كاملة، ~1.75 جيجابايت)**: قائمة عناوين URL الكاملة بعد إزالة التكرارات من مشاركات Reddit.
  - التورنت: [WebText dataset urls.txt.tar.gz](https://academictorrents.com/details/15f3494b2991e75194d3af72bf7afa5025a7abc3)
  - المصدر: Academic Torrents (يتم توزيعه من قبل المجتمع).

- **النسخة المُجزأة (~16 جيجابايت)**: ملفات نصية مُجزأة باستخدام GPT-2 من مجموعة النصوص التي تم جلبها (395 ملفًا، جاهزة لتدريب النماذج).
  - التورنت: [OpenWebText (Gokaslan's distribution, 2019), GPT-2 Tokenized](https://academictorrents.com/details/36c39b25657ce1639ccec0a91cf242b42e1f01db)
  - المصدر: Academic Torrents (يتم توزيعه من قبل OSUOSL والمجتمع).

للحصول على مجموعة النصوص الخام الكاملة، تحقق من الموقع الرسمي للتنزيلات المباشرة (غير المعتمدة على التورنت) أو استخدم عناوين URL المذكورة أعلاه مع نصوص الجلب من [مستودع OpenWebText على GitHub](https://github.com/eukaryote31/openwebtext). تتوفر نسخة محسنة، OpenWebText2 (~بمقياس التيرابايت المتعدد)، عبر [مستودع EleutherAI](https://github.com/EleutherAI/openwebtext2) ولكنها تستخدم البث بدلاً من التورنت.

### مجموعات بيانات Wikipedia عبر التورنت

مجموعات بيانات Wikipedia هي تصديرات شهرية بصيغة XML لقاعدة البيانات الكاملة (المقالات، المراجعات، البيانات الوصفية). النسخة الإنجليزية ضخمة الحجم (~20-25 جيجابايت مضغوطة للملخصات، وصولاً إلى 100+ جيجابايت لسجل التعديلات الكامل). يتم الحفاظ على التورنت من قبل المجتمع (غير رسمي ولكن تم التحقق منه مقابل المجاميع الاختبارية الرسمية) ويتم توزيعها من خوادم ويكيميديا لضمان الموثوقية. تحقق دائمًا من تنزيلاتك مقابل مجاميع الاختبار من [dumps.wikimedia.org](https://dumps.wikimedia.org/enwiki/latest/).

المركز الرئيسي لملفات التورنت هو [صفحة تورنتات مجموعات بيانات Meta-Wiki](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki)، والتي تسرد أحدث مجموعات بيانات Wikipedia الإنجليزية (مثل، enwiki-20251101). إليك ملخصًا لأحدثها:

| تاريخ المجموعة | نوع الملف | الحجم المضغوط | رابط التورنت | ملاحظات |
|-----------|-----------|-----------------|--------------|-------|
| 2025-11-01 | Pages-Articles (XML, للملخصات فقط) | ~22 ج.ب | [enwiki-20251101-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | بتنسيق Multistream؛ الأسهل لاستخراج النص. |
| 2025-11-01 | Pages-Articles-History (XML, جميع المراجعات) | ~120 ج.ب | [enwiki-20251101-pages-meta-history*.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | يتضمن جميع التعديلات؛ مقسم إلى تيارات لتسهيل التعامل. |
| 2025-10-01 | Pages-Articles (XML, للملخصات فقط) | ~21 ج.ب | [enwiki-20251001-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | الشهر السابق؛ جيد للمقارنة التاريخية. |

- **المجموعة الكاملة**: تصفح جميع تورنتات Wikipedia الإنجليزية التاريخية على [مجموعة Wikipedia في Academic Torrents](https://academictorrents.com/collection/wikipedia) (تتضمن مجموعات بيانات قديمة تعود إلى ~2010).
- **تنسيق Kiwix ZIM**: إذا كنت تريد Wikipedia قابلة للتصفح بدون اتصال بالإنترنت (HTML، ~100 جيجابايت)، جرب [wikipedia_en_all_maxi_2024-01.zim.torrent](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2024-01.zim.torrent) – يتم توزيعه من قبل المجتمع، ولكن تحقق من وجود تحديثات لعام 2025 على [تنزيلات Kiwix](https://download.kiwix.org/zim/wikipedia/).

لمعالجة هذه الملفات وتحويلها إلى نص عادي، استخدم أدوات مثل `wikiextractor` من Python. تقلل التورنتات من الحمل على الخوادم وتسمح باستئمال التنزيلات المنقطعة – استخدم عميلاً مثل qBittorrent. إذا كنت بحاجة إلى مجموعات بيانات للغات أخرى أو مجموعات فرعية، فإن صفحة Meta-Wiki تحتوي على عوامل تصفية.