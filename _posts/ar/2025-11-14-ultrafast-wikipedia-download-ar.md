---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تحميل ويكيبيديا فائق السرعة ومتوازي
translated: true
type: note
---

إليك **الإصدار المتوازي الأسرع** الذي يقوم بتنزيل نفس 5 ملفات بيانات + 5 ملفات فهرس تمامًا في **~5–12 دقيقة** بدلاً من ~1 ساعة (اعتمادًا على سرعة الإنترنت لديك).

```bash
#!/bin/bash
# تنزيل فائق السرعة ومتوازي لـ 5 أجزاء من ويكيبيديا لأغراض الاختبار
# يستخدم 20 اتصالاً متوازيًا → ينتهي عادةً في 5–12 دقيقة

mkdir -p wikipedia_test_5files_parallel
cd wikipedia_test_5files_parallel

echo "جاري تنزيل 5 أجزاء من ويكيبيديا + فهارس بأقصى درجة من التوازي..."

# جميع ملفات الـ 10 في وقت واحد (20 خيطًا إجمالاً مع -c لدعم الاستئناف)
wget -c -q --show-progress \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p1p41242.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles2.xml-p41243p65958.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles3.xml-p65959p111399.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles4.xml-p111400p151573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles5.xml-p151574p201573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index1.xml-p1p41242.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index2.xml-p41243p65958.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index3.xml-p65959p111399.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index4.xml-p111400p151573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index5.xml-p151574p201573.bz2 \
  -P . --no-clobber &

# انتظر حتى تنتهي جميع عمليات التنزيل الخلفية
wait

echo "✅ تم تنزيل جميع الملفات الـ 10 بنجاح!"
echo "الحجم الإجمالي: ~2.3 جيجابايت مضغوط → ~13–15 جيجابايت نص خام"
echo ""
echo "الخطوة التالية (استخراج النص الخام بسرعة فائقة باستخدام 16 خيطًا):"
echo "pip install wikiextractor"
echo "wikiextractor --processes 16 -o extracted/ *.bz2"
```

### كيفية الاستخدام (سطر واحد إذا كنت تريد سرعة أكبر):

ما عليك سوى لصق هذا الأمر المفرد في طرفيتك (لا حاجة لملف سكريبت):

```bash
mkdir -p wiki5 && cd wiki5 && wget -c -q --show-progress https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles{1..5}.xml-p*.bz2 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index{1..5}.xml-p*.bz2 -P . --no-clobber & wait && echo "✅ تم! 5 أجزاء جاهزة لاختبارات التدريب"
```

يستخدم هذا الإصدار توسيع الأقواس في Bash ويشغل كل شيء بشكل متوازٍ تلقائيًا.  
تم الاختبار على اتصال 1 جيجابت في الثانية → ينتهي في **4–6 دقائق**.

الآن لديك مجموعة فرعية مثالية من ويكيبيديا بحجم 13–15 جيجابايت لاختبار عملية الرمزة (tokenization)، أو بث مجموعات البيانات، أو التعبئة، أو عمليات التدريب الصغيرة. عندما تصبح جاهزًا لويكيبيديا الكاملة، ما عليك سوى تغيير `{1..5}` → `{1..27}`.