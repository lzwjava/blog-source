---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح الرموز المفقودة في الخط الياباني
translated: true
type: note
---

الأخطاء التي تواجهها تشير إلى أن الخط `FandolSong` (كلا النوعين العادي والعريض) المستخدم في مستند LaTeX الخاص بك لا يحتوي على الرموز الرسومية (glyphs) اللازمة لبعض الأحرف اليابانية، مثل `ー` (U+30FC، علامة إطالة صوت الكاتاكانا-هيراغانا)، `専` (U+5C02)، `証` (U+8A3C)، و `発` (U+767A). هذا يتسبب في قيام XeLaTeX بالإبلاغ عن أخطاء "Missing character" عند تجميع مستندك، على الأرجح `resume-ja.tex` أو ملف ذي صلة في `latex/ja/resume-ja/`.

خط `FandolSong` مصمم في الأساس للنص الصيني ويخلو من الدعم الكامل للأحرف اليابانية، مما يفسر اختفاء الرموز الرسومية. لحل هذه المشكلة، تحتاج إلى التبديل إلى خط يدعم الأحرف اليابانية، مثل `Noto Sans CJK JP` أو `IPAGothic`، كما أوصى سابقًا. أدناه، سأرشدك خلال عملية إصلاح المشكلة عن طريق تحديث تكوين الخط وضمان التوافق مع سيرتك الذاتية المترجمة إلى اليابانية.

### لماذا يحدث هذا
- **قيد الخط**: `FandolSong` هو خط صيني مدرج في TeX Live لتنضيد النصوص CJK ولكنه لا يتضمن جميع الأحرف اليابانية، خاصة الكاتاكانا (`ー`) والكانجي الشائع الاستخدام في اليابانية.
- **XeLaTeX و xeCJK**: من المرجح أن مستندك يستخدم حزمة `xeCJK`، التي تعتمد على خط CJK المحدد (`FandolSong` في هذه الحالة) للنص الياباني. عندما تختفي الرموز الرسومية، يسجل XeLaTeX أخطاء وقد يحذف الأحرف في ملف PDF الناتج.
- **القسم المترجم**: نظرًا لأنك تترجم أقسامًا مثل `blogposts.tex` إلى اليابانية، فإن النص المترجم يحتوي على أحرف يابانية لا يمكن لـ `FandolSong` عرضها.

### الحل: تغيير خط CJK
تحتاج إلى تحديث تكوين الخط في مستند LaTeX الخاص بك لاستخدام خط متوافق مع اليابانية. نظرًا لأن رسالتك السابقة أشارت إلى نظام Linux وكود تكوين للخطوط، سأفترض أنك تستخدم XeLaTeX مع `xeCJK` وبنية `ifthenelse` لاختيار الخط.

#### الخطوة 1: تثبيت خط متوافق مع اليابانية
تأكد من تثبيت خط يدعم اليابانية على نظام Linux الخاص بك. الخط الموصى به هو `Noto Sans CJK JP`، وهو متاح على نطاق واسع ويدعم جميع الرموز الرسومية اليابانية اللازمة.

لتثبيت `Noto Sans CJK JP` على Ubuntu/Debian:
```bash
sudo apt-get install fonts-noto-cjk
```
على Fedora:
```bash
sudo dnf install google-noto-cjk-fonts
```
على Arch Linux:
```bash
sudo pacman -S noto-fonts-cjk
```

بدلاً من ذلك، يمكنك استخدام `IPAGothic` أو `IPAexGothic`:
```bash
sudo apt-get install fonts-ipaexfont
```

تحقق من تثبيت الخط:
```bash
fc-list :lang=ja | grep Noto
```
يجب أن ترى إدخالات مثل `Noto Sans CJK JP` أو `Noto Serif CJK JP`. إذا كنت تستخدم خطوط IPA:
```bash
fc-list :lang=ja | grep IPA
```

#### الخطوة 2: تحديث تكوين خط LaTeX
قم بتعديل تكوين الخط في مستند LaTeX الخاص بك (على الأرجح `resume-ja.tex` أو ملف تمهيدي مشترك) لاستخدام خط متوافق مع اليابانية. بناءً على إعداد الخط السابق الخاص بك، إليك كيفية تحديث التكوين:

```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    % خطوط Linux
    \setCJKmainfont{Noto Sans CJK JP} % الخط الرئيسي لليابانية
    \setCJKsansfont{Noto Sans CJK JP} % الخط Sans-serif لليابانية
    \setCJKmonofont{Noto Sans Mono CJK JP} % الخط Monospace لليابانية
    \setmainfont{Liberation Serif} % الخط الإنجليزي
}
```

إذا كان `Noto Sans Mono CJK JP` غير متوفر، يمكنك استخدام `Source Code Pro` أو `DejaVu Sans Mono` للنص غير CJK أحادي المسافة، ولكن تأكد من استخدام كتل الكود اليابانية لخط CJK:
```latex
\setCJKmonofont{Noto Sans CJK JP}
```

إذا كنت تفضل `IPAGothic`:
```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{IPAexGothic}
    \setCJKsansfont{IPAexGothic}
    \setCJKmonofont{IPAexMincho} % أو Noto Sans CJK JP للنص أحادي المسافة
    \setmainfont{Liberation Serif}
}
```

#### الخطوة 3: التحقق من استخدام xeCJK
تأكد من أن مستند LaTeX الخاص بك يستخدم حزمة `xeCJK` ويطبق إعدادات الخط بشكل صحيح. قد يبدو المثال البسيط لـ `resume-ja.tex` كما يلي:

```latex
\documentclass[a4paper]{article}
\usepackage{xeCJK}
\usepackage{ifthenelse}

% كشف نظام الخط
\newcommand{\fontsystem}{linux}

\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}

\begin{document}

% النص الياباني من blogposts.tex
\section{ブログ投稿}
こんにちは、私の名前は李智维です。最新の技術に関する記事を書いています。

% النص الإنجليزي
\section{Introduction}
Hello, my name is Zhiwei Li.

\end{document}
```

إذا كانت سيرتك الذاتية تستخدم قالبًا مثل `awesome-cv`، فتأكد من أن التمهيد يتضمن `xeCJK` وإعدادات الخط المذكورة أعلاه. على سبيل المثال، في `awesome-cv.cls` أو `resume-ja.tex`، أضف:

```latex
\RequirePackage{xeCJK}
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}
```

#### الخطوة 4: إعادة تجميع المستند
انتقل إلى دليل السيرة الذاتية اليابانية وأعد التجميع:
```bash
cd latex/ja/resume-ja
xelatex resume-ja.tex
```

تحقق من ملف السجل (`resume-ja.log`) بحثًا عن أخطاء "Missing character". إذا تم تعيين الخط بشكل صحيح، فيجب أن تختفي هذه الأخطاء، ويجب أن يعرض ملف PDF الأحرف اليابانية مثل `ー`، `専`، `証`، و `発` بشكل صحيح.

#### الخطوة 5: تصحيح الأخطاء إذا استمرت
إذا كنت لا تزال ترى أخطاء "Missing character":
1. **تأكيد اسم الخط**: تأكد من تطابق اسم الخط تمامًا كما هو مدرج في `fc-list`. على سبيل المثال، تسجل بعض الأنظمة `Noto Sans CJK JP Regular` بدلاً من `Noto Sans CJK JP`. اضبط تكوين LaTeX:
   ```latex
   \setCJKmainfont{Noto Sans CJK JP Regular}
   ```
2. **تحقق من تكوين xeCJK**: تأكد من تحميل `xeCJK` قبل إعدادات الخط وأنه لا توجد حزمة أخرى تتجاوز خط CJK. على سبيل المثال، تجنب تحميل `fontspec` مع إعدادات متضاربة.
3. **اختبار مستند بسيط**: أنشئ ملف LaTeX بسيط يحتوي على نص ياباني لعزل المشكلة:
   ```latex
   \documentclass{article}
   \usepackage{xeCJK}
   \setCJKmainfont{Noto Sans CJK JP}
   \begin{document}
   こんにちは、専ー証発
   \end{document}
   ```
   قم بالتجميع باستخدام `xelatex` وتحقق من الأخطاء.
4. **خط احتياطي**: إذا لم يعمل `Noto Sans CJK JP`، جرب `Source Han Sans JP` أو `IPAexGothic`. اعرض الخطوط المتاحة باستخدام `fc-list :lang=ja` وقم بتحديث التكوين وفقًا لذلك.

#### الخطوة 6: تحديث القسم المترجم
نظرًا لأنك تستخدم البرنامج النصي Python لترجمة أقسام مثل `blogposts.tex`، تأكد من تضمين الملف المترجم (`latex/ja/resume-ja/blogposts.tex`) في `resume-ja.tex` عبر `\input{blogposts}`. البرنامج النصي الذي قدمته يستبدل الملف بشكل صحيح بالفعل، لذلك ليست هناك حاجة لإجراء تغييرات هناك. ما عليك سوى إعادة تشغيل الترجمة إذا لزم الأمر:
```bash
python translate_section.py --section blogposts.tex --lang ja --kind resume
```

ثم أعد تجميع `resume-ja.tex` لدمج القسم المحدث.

### ملاحظات إضافية
- **أوزان الخط**: يدعم `Noto Sans CJK JP` أوزانًا متعددة (عادي، عريض، إلخ)، لذا يجب أن يعمل `\textbf{}` للنص الياباني. إذا كنت تستخدم `IPAexGothic`، فتأكد من توفر النوع العريض (`IPAexGothic Bold`) أو اضبط التكوين.
- **توافق القالب**: إذا كنت تستخدم قالبًا مثل `awesome-cv`، فتحقق مما إذا كان يتجاوز إعدادات الخط في ملف `.cls`. قد تحتاج إلى تطبيق إعدادات `xeCJK` في المستند الرئيسي (`resume-ja.tex`) بدلاً من ذلك.
- **إخراج PDF**: افحص ملف PDF المُنشأ للتأكد من عرض الأحرف اليابانية بشكل صحيح. إذا ظهرت الأحرف كصناديق، فلا يزال الخط غير صحيح أو غير مضمن بشكل صحيح.
- **ذاكرة التخزين المؤقت للخطوط في النظام**: بعد تثبيت خطوط جديدة، قم بتحديث ذاكرة التخزين المؤقت للخطوط:
  ```bash
  fc-cache -fv
  ```

### مثال على الإخراج
بعد تطبيق الإصلاح، قد يحتوي `blogposts.tex` الخاص بك في `latex/ja/resume-ja/` على نص ياباني مثل:
```latex
\section{ブログ投稿}
\item 技術ブログ: 最新のAI技術について書いています。専門的な内容をわかりやすく説明します。
```
عند تجميعه مع `Noto Sans CJK JP`، يجب أن تعرض الأحرف مثل `ー`، `専`، `証`، و `発` بشكل صحيح في ملف PDF.

إذا واجهت المزيد من الأخطاء أو كنت بحاجة إلى مساعدة في جزء محدد من قالب السيرة الذاتية، فيرجى مشاركة كود LaTeX ذي الصلة (على سبيل المثال، تمهيدية `resume-ja.tex` أو إعدادات الخط في القالب)، ويمكنني تقديم إصلاح مستهدف أكثر!