---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل تحميل مجموعة بيانات أوبن ويب تكست
translated: true
type: note
---

### تحليل المشكلة
خطأ `RepositoryNotFoundError` (401 خطأ عميل) يؤكد أن المستودع `openwebtext` **غير موجود** على Hugging Face. هذا هو سبب فشل التحميل — Hugging Face لا يمكنه العثور على المستودع على الرابط `https://huggingface.co/openwebtext`. جزء "اسم مستخدم أو كلمة مرور غير صالحة" هو رسالة خطأ عامة من طبقة المصادقة في Hugging Face، لكنه غير ذي صلة هنا لأن المستودع ببساطة غير موجود. مجموعة البيانات OpenWebText (التي تحاول الوصول إليها) هي مجموعة نصوص عامة من عصر GPT-2، لكنها غير مستضافة كمستودع قياسي على Hugging Face. بدلاً من ذلك، يتم توزيعها عبر المرايا، أو التورنت، أو التحميلات المباشرة من المصادر الأكاديمية أو GitHub.

- **خلفية عن OpenWebText**: تم إنشاؤها لمحاكاة مجموعة البيانات المستخدمة في ورقة GPT-2 (من عناوين URL في محفوظات Pushshift لـ Reddit، وتمت تصفيتها لضمان الجودة). المجموعة الكاملة هي حوالي ~40 جيجابايت من النص، مقسمة إلى مجموعات فرعية مثل `urlsf_subset00.tar` (أحد 14 أرشيف مضغوط، كل منها بحجم ~3-5 جيجابايت). تحتوي هذه الأرشيفات على ملفات نصية خام لتدريب نماذج مثل nanoGPT.
- لا يوجد مستودع رسمي على Hugging Face: بعد التحقق، لا توجد تحميلات مباشرة للمجموعات الفرعية الكاملة تحت `openwebtext` أو ما شابه (على سبيل المثال، لدى EleutherAI مستودعات ذات صلة ولكن ليس البيانات الخام). يركز Hugging Face على النماذج/مجموعات البيانات ذات التراخيص، وOpenWebText في المجال العام ولكنها مستضافة في مكان آخر لتجنب تكاليف النطاق الترددي.

### طريقة التحميل الصحيحة
استخدم **تحميلات HTTP المباشرة** أو **التورنت** من المرايا الموثوقة. المصدر الأكثر موثوقية هو مرآة GitHub بواسطة Skylion007 (جهد مجتمعي لاستضافة المجموعة المنقحة). إليك كيفية الحصول على `urlsf_subset00.tar` (وغيرها إذا لزم الأمر):

1. **التحميل المباشر من المرآة** (موصى به للسرعة):
   - رابط الأساس: `http://skylion007.github.io/OpenWebTextCorpus/`
   - ملف محدد: `http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar`
   - أمر التحميل (باستخدام `wget` أو `curl`؛ قم بتثبيتهما إذا لزم الأمر عبر `sudo apt install wget`):
     ```
     cd ~/projects/nanoGPT  # أو مجلد الهدف الخاص بك
     wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
     ```
     - يحفظ هذا الملف كـ `./urlsf_subset00.tar` (~3.3 جيجابايت). إنها مرآة HTTP، لذا لا حاجة للمصادقة، وهي سريعة (مباشرة من GitHub Pages).
     - للمجموعة الكاملة (جميع المجموعات الفرعية): اذكرها من الصفحة وقم بالتحميل في حلقة، أو استخدم سكريبت:
       ```bash
       for i in {00..13}; do
         wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset${i}.tar
       done
       ```
     - بديل باستخدام `curl` (إذا لم يكن `wget` متوفرًا):
       ```
       curl -O http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
       ```

2. **تحميل التورنت** (الأفضل للملفات الكبيرة، يمكن استئنافه، وفعال من حيث النطاق الترددي):
   - التورنت الرسمي لجميع المجموعات الفرعية: رابط Magnet من مستودع Gwern الأصلي أو Academic Torrents.
   - رابط Magnet (انسخه وألصقه في عميل مثل qBittorrent أو Transmission أو `aria2c`):
     ```
     magnet:?xt=urn:btih:5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e&dn=OpenWebTextCorpus
     ```
   - أو ملف .torrent مباشر: حمله من [academictorrents.com](https://academictorrents.com/details/5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e) أو ابحث عن "OpenWebTextCorpus torrent".
   - قم بتثبيت عميل تورنت إذا لزم الأمر:
     - Ubuntu/Debian: `sudo apt install qbittorrent-nox` (بدون واجهة) أو استخدم الواجهة الرسومية.
     - ثم شغل: `qbittorrent-nox` وأضف رابط Magnet.
   - المتوقع: يقوم بتحميل جميع الأرشيفات الـ 14 (~40 جيجابايت إجمالاً) إلى المجلد الذي اخترته. اختر فقط `urlsf_subset00.tar` إذا أردت جزءًا.

3. **استنساخ GitHub (إذا أردت بنية المستودع)**:
   - بيانات وصفية المجموعة موجودة على GitHub: `https://github.com/skylion007/OpenWebTextCorpus`
   - استنسخ للحصول على ملف README/الوثائق (وليس البيانات):
     ```
     git clone https://github.com/skylion007/OpenWebTextCorpus.git
     ```
   - روابط البيانات موجودة في ملف README — وتشير إلى نفس المرايا المذكورة أعلاه.

### بعد التحميل
- **استخراج الأرشيف المضغوط**:
  ```
  mkdir -p ./openwebtext/subsets
  tar -xvf urlsf_subset00.tar -C ./openwebtext/subsets
  ```
  - يقوم هذا بفك ضغط ~100,000+ ملف نصي (مثل `0.txt`, `1.txt`) إلى `./openwebtext/subsets/`. كل ملف هو نص صفحة ويب منقح.
- **للتكامل مع nanoGPT**:
   - لدى NanoGPT (مستودع Andrej Karpathy) مثال `openwebtext` في book/data prep. استخدم السكريبت الخاص بهم لدمج/معالجة الملفات:
     ```python
     # من nanoGPT's data/openwebtext/prepare.py (عدل كما تحتاج)
     import os
     import glob

     input_dir = './openwebtext/subsets'
     output_file = './openwebtext/input.txt'

     with open(output_file, 'w') as out:
         for txt_file in sorted(glob.glob(os.path.join(input_dir, '*.txt'))):
             with open(txt_file, 'r') as f:
                 out.write(f.read())
     ```
   - ينشئ هذا ملف `input.txt` واحد ضخم للتدريب. كن حذرًا — مجموعة OpenWebText الكاملة تحتاج مساحة تخزين/ذاكرة وصول عشوائي كبيرة.
- **التحقق من السلامة**: كل أرشيف مضغوط له checksum MD5 في ملف README الخاص بالمرآة (على سبيل المثال، للمجموعة الفرعية 00: تحقق مقابل الـ hash المقدم باستخدام `md5sum urlsf_subset00.tar`).

### إذا استمرت المشاكل
- **هل المرآة معطلة؟** جرب مصدر Gwern الأصلي: `https://www.gwern.net/OpenWebTextCorpus` (روابط إلى AWS S3 أو التورنت).
- **ملاحظات قانونية/الوصول**: OpenWebText في المجال العام (تم جمعها من الويب المفتوح)، لكن احترم ملف robots.txt في استخدامك. لا حاجة للمصادقة على Hugging Face هنا.
- **بدائل على Hugging Face**: إذا أردت بيانات مشابهة مستضافة على Hugging Face، تحقق من `wikitext`، أو `bookcorpus`، أو مجموعات فرعية من `pile` (مثل `repo_id="EleutherAI/pile"` مع `hf download`). للحصول على OpenWebText بالضبط، التزم بالمرايا.
- **نصائح للقرص/السرعة**: هذه الملفات ضخمة — استخدم أقراص SSD، وراقب باستخدام `du -sh` أو `htop`. إذا كنت في الصين أو منطقة مقيدة، استخدم VPN للوصول الأسرع.

إذا نجح التحميل لكنك واجهت أخطاء في الاستخراج/المعالجة، أو تحتاج مساعدة في الخطوة التالية لـ nanoGPT، الصق التفاصيل!