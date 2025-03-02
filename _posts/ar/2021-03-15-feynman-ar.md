---
audio: false
generated: false
lang: ar
layout: post
title: 'mathjax2mobi: تحويل MathJax HTML إلى كتب إلكترونية'
translated: true
---

### نظرة عامة على المشروع

دعونا أولاً نلقي نظرة عامة على حالة المشروع.

![فاينمان_أونلاين](assets/images/feynman/feynman_online.jpg)

<img src="/assets/images/feynman/change.JPG" alt="التغيير" style="zoom:50%;" />

![لَاتِكْس](assets/images/feynman/latex.JPG)

![epub_black](assets/images/feynman/epub_black.JPG)

![epub_beautiful](assets/images/feynman/epub_beautiful.JPG)

بعد الانتهاء من المشروع، شعرت ببعض السعادة. كتبت هذه الجملة.

كتبت الكود طوال اليوم، وأخيرًا حصلت على كتاب إلكتروني جميل لمحاضرات فيزياء فاينمان! محاضرات فيزياء فاينمان متاحة على الإنترنت، وهي مكتوبة باستخدام `latex` الذي يتميز بعرض رائع للمعادلات الرياضية. وعندما يتم نشرها على الإنترنت، يتم استخدام مكتبة `mathjax` لتحويل كود `latex` إلى كود `html`، مما ينتج عنه الكثير من علامات `div` و `span`. لكن الكتب الإلكترونية لا تدعم هذه الطريقة. لذا، كانت الفكرة هي استخراج صفحات الويب، وعكس عملية عرض `mathjax`، ثم استبدالها بصور `svg`. واجهت العديد من المشاكل، أولها أن الكود يحتوي على الكثير من وحدات `latex` المخصصة التي يجب إضافتها؛ وثانيًا، أن تضمين الكثير من صور `svg` يسبب مشاكل. إذا كانت الصورة واحدة فلا مشكلة، ولكن عند وجود الكثير منها تظهر مشاكل. ربما يكون هذا بسبب بعض الأخطاء الغريبة في المتصفحات و `svg`. الحل كان ببساطة حفظ `svg` كملفات واستخدام علامة `img` لإدراجها. المعادلات أيضًا تنقسم إلى نوعين: معادلات داخل النص ومعادلات منفردة في سطر خاص. وهكذا، حصلت أخيرًا على كتاب إلكتروني جميل!

### البيانات التي تم البحث عنها

هنا يتم تسجيل المواد التي تم الوصول إليها أثناء حل المشروع. نظرًا لأن هذا برنامج تعليمي، فسأعرض للطلاب تجربة كيفية تنفيذ مشروع بشكل عام.

![](assets/images/feynman/s1.PNG)

![](assets/images/feynman/s2.PNG)

![](assets/images/feynman/s3.PNG)

![](assets/images/feynman/s4.PNG)

![](assets/images/feynman/s5.PNG)

![](assets/images/feynman/s6.PNG)

![](assets/images/feynman/s7.PNG)

![](assets/images/feynman/s8.PNG)

### بدء المشروع

محاضرات فينمان في الفيزياء أصبحت متاحة للقراءة على الإنترنت. أرغب في قراءتها على جهاز `Kindle`. ومع ذلك، نظرًا لاحتوائها على العديد من الصيغ الرياضية، فإن المسودة الأصلية ربما تم إعدادها باستخدام `latex`. يتم استخدام مكتبة `mathjax` لعرض محتوى بتنسيق `latex` على صفحات الويب.

لنأخذ مثالًا.

```html
<span class="MathJax_Preview" style="color: inherit; display: none;">
</span>
<div class="MathJax_Display">
    <span class="MathJax MathJax_FullWidth" id="MathJax-Element-10-Frame" tabindex="0" style="">
              <span class="mi" id="MathJax-Span-159" style="font-family: MathJax_Math-italic;">d<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;">
                </span>  
    </span>
</div>
<script type="math/tex; mode=display" id="MathJax-Element-10">\begin{equation}
\label{Eq:I:13:3}
dT/dt = Fv.
\end{equation}
</script>
```

في الأعلى مقتطف من كود `html`. في هذا الجزء من كود `html`، يوجد نص `latex` كما هو تحت علامة `script`. يقوم `mathjax` بتحويله إلى العديد من علامات `span` لعرضه.

لدينا الآن فكرة. وهي تغيير طريقة عرض `mathjax` إلى صور `svg`.

وجدت مشروعًا على GitHub باسم `tuxu/latex2svg`.

```python
from latex2svg import latex2svg
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

حاولت التشغيل، لكن حدث خطأ.

```shell
    raise RuntimeError('latex not found')
RuntimeError: latex not found
```

انظر إلى الكود.

```python
    # تشغيل LaTeX وإنشاء ملف DVI
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('latex غير موجود')
```

يبدو أن هذا يعتمد أيضًا على أمر `latex`.

قم بالتثبيت.

```shell
brew install --cask mactex
==> ملاحظات
يجب عليك إعادة تشغيل نافذة الطرفية الخاصة بك حتى يتم تفعيل تثبيت أدوات MacTex CLI.
بدلاً من ذلك، يمكن لمستخدمي Bash و Zsh تشغيل الأمر:
  eval "$(/usr/libexec/path_helper)"
==> جاري التحميل http://mirror.ctan.org/systems/mac/mactex/mactex-20200407.pkg
==> جاري التحميل من https://mirrors.aliyun.com/CTAN/systems/mac/mactex/mactex-20200407.pkg
######################################################################## 100.0%
تم تلبية جميع تبعيات الصيغة.
==> جاري تثبيت Cask mactex
==> جاري تشغيل المثبت لـ mactex؛ قد يلزم إدخال كلمة المرور الخاصة بك.
installer: اسم الحزمة هو MacTeX
installer: تم تطبيق ملف تغييرات الاختيارات '/private/tmp/choices20210315-4643-5884ro.xml'
installer: جاري التثبيت في المسار الأساسي /
installer: تم التثبيت بنجاح.
🍺  تم تثبيت mactex بنجاح!
```

تم التثبيت بنجاح.

```shell
% latex
هذا هو pdfTeX، الإصدار 3.14159265-2.6-1.40.21 (TeX Live 2020) (تنسيق مسبق التحميل=latex)
 تم تمكين \write18 المقيد.
**
```

```python
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

في الكود أعلاه، يتم استخدام الدالة `latex2svg` لتحويل التعبير الرياضي \( e^{i \pi} + 1 = 0 \) إلى صيغة SVG. بعد ذلك، يتم طباعة عمق الصورة (`depth`) ورمز SVG الناتج (`svg`).

```python
svg = open('1.svg', 'w')
svg.write(out['svg'])
svg.close()
```

يمكن الآن إنشاء ملفات `svg`.

لذا، جرب إنشاء نص `latex` الذي تحصل عليه من `mathjax`.

```python
from bs4 import BeautifulSoup
from latex2svg import latex2svg
```

```python
file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
content = file.read()
```

```python
soup = BeautifulSoup(content)
```

```python
mathjaxs = soup.findAll('script', {'type': 'math/tex'})
for mathjax in mathjaxs:
    print(mathjax.string)
    out = latex2svg(mathjax.string)
    print(out['svg'])
```

للأسف حدث خطأ.

```python
    raise CalledProcessError(self.returncode, self.args, self.stdout,
subprocess.CalledProcessError: الأمر '['latex', '-interaction', 'nonstopmode', '-halt-on-error', 'code.tex']' أعاد حالة خروج غير صفرية 1.
```

أي صيغة محددة كانت خاطئة؟

```latex
\tfrac{1}{2}mv^2
```

## لاتيكس

لاتيكس (LaTeX) هو نظام لإعداد المستندات عالية الجودة، يستخدم بشكل شائع في الأوساط الأكاديمية والعلمية لإنتاج أوراق بحثية وكتب وعروض تقديمية. يتميز لاتيكس بقدرته على التعامل مع المعادلات الرياضية المعقدة والرموز العلمية بسهولة، مما يجعله الخيار المفضل للعديد من الباحثين والطلاب.

### مثال بسيط في لاتيكس

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{عنوان المستند}
\author{اسم المؤلف}
\date{\today}

\begin{document}

\maketitle

\section{مقدمة}
هذا مثال بسيط لمستند لاتيكس. يمكنك كتابة النصوص وإضافة المعادلات الرياضية بسهولة.

\section{معادلة رياضية}
هنا معادلة رياضية بسيطة:

\[
E = mc^2
\]

\end{document}
```

في هذا المثال، يتم إنشاء مستند بسيط يحتوي على عنوان ومقدمة ومعادلة رياضية. يمكنك تعديل النصوص وإضافة المزيد من الأقسام حسب الحاجة.

لنتعلم `latex`.

```latex
\documentclass[12pt]{article}
\usepackage{lingmacros}
\usepackage{tree-dvips}
\begin{document}
```

\section*{ملاحظات حول ورقة البحث الخاصة بي}

لا تنسَ تضمين أمثلة على التخصيص الموضعي.  
تبدو هكذا:

{\small
\enumsentence{التركيز من خلال الموضوع الجملة:\\
\shortex{7}{a John$_i$ [a & kltukl & [el & 
  {\bf l-}oltoir & er & ngii$_i$ & a Mary]]}
{ & {\bf R-}clear & {\sc comp} & 
  {\bf IR}.{\sc 3s}-love   & P & him & }
{جون، (من) الواضح أن ماري تحبه.}}
}

\subsection*{كيفية التعامل مع التوبيكالايزيشن (التركيز على موضوع الجملة)}

سأفترض ببساطة بنية شجرة مثل (\ex{1}).

{\small
\enumsentence{هيكل إسقاطات A$'$:\\ [2ex]
\begin{tabular}[t]{cccc}
    & \node{i}{CP}\\ [2ex]
    \node{ii}{Spec} &   &\node{iii}{C$'$}\\ [2ex]
        &\node{iv}{C} & & \node{v}{SAgrP}
\end{tabular}
\nodeconnect{i}{ii}
\nodeconnect{i}{iii}
\nodeconnect{iii}{iv}
\nodeconnect{iii}{v}
}
}

\subsection*{المزاج}

يتغير المزاج عندما يكون هناك موضوع، وكذلك عندما يكون هناك حركة WH. \emph{Irrealis} هو المزاج عندما يكون هناك موضوع غير فاعل أو عبارة WH في Comp. \emph{Realis} هو المزاج عندما يكون هناك موضوع فاعل أو عبارة WH.

```latex
\end{document}
```

عثرت على نموذج لشفرة `latex` على الإنترنت.

```shell
% latex code.tex
This is pdfTeX, Version 3.14159265-2.6-1.40.21 (TeX Live 2020) (preloaded format=latex)
 restricted \write18 enabled.
entering extended mode
(./code.tex
LaTeX2e <2020-02-02> patch level 5
L3 programming layer <2020-03-06>
(/usr/local/texlive/2020/texmf-dist/tex/latex/base/article.cls
Document Class: article 2019/12/20 v1.4l Standard LaTeX document class
(/usr/local/texlive/2020/texmf-dist/tex/latex/base/size12.clo))
(/usr/local/texlive/2020/texmf-dist/tex/latex/tree-dvips/lingmacros.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/tree-dvips/tree-dvips.sty
tree-dvips version .91 of May 16, 1995
) (/usr/local/texlive/2020/texmf-dist/tex/latex/l3backend/l3backend-dvips.def)
(./code.aux) [1] (./code.aux) )
Output written on code.dvi (1 page, 3416 bytes).
Transcript written on code.log.
```

![latex](assets/images/feynman/latex.png)

لنلقِ نظرة على الكود المصدري والنتيجة المقدمة بعد التصيير، لنرى ما يمكننا تعلمه.

```latex
\begin{document}
\end{document}
```

هكذا يتم تغليف المستند.

```latex
\section*{ملاحظات لورقتي البحثية}
```

هذا يشير إلى بداية عنوان `section`.

```latex
\subsection*{كيفية التعامل مع التوبيكاليزيشن (التركيز على الموضوع)}
```

هذا يشير إلى العنوان الفرعي.

```latex
\shortex{7}{a John$_i$ [a & kltukl & [el & 
  {\bf l-}oltoir & er & ngii$_i$ & a Mary]]}
```

![shortex](assets/images/feynman/shortex.png)

يمكن استخدام `$_i$` لتمثيل الحروف السفلية. واستخدام `{\bf l-}` لتمثيل النص الغامق.

```latex
\enumsentence{هيكل إسقاطات A$'$:\\ [2ex]
\begin{tabular}[t]{cccc}
    & \node{i}{CP}\\ [2ex]
    \node{ii}{Spec} &   &\node{iii}{C$'$}\\ [2ex]
        &\node{iv}{C} & & \node{v}{SAgrP}
\end{tabular}
\nodeconnect{i}{ii}
\nodeconnect{i}{iii}
\nodeconnect{iii}{iv}
\nodeconnect{iii}{v}
}
```

<img src="/assets/images/feynman/node.png" alt="node" style="zoom:50%;" />

لاحظ استخدام `nodeconnect` للإشارة إلى الاتصال بين العقد.

### تحويل LaTeX إلى SVG

لتحويل معادلات LaTeX إلى صور بتنسيق SVG، يمكنك استخدام أدوات مختلفة. فيما يلي بعض الطرق الشائعة:

#### 1. استخدام `MathJax` مع `svg` كتنسيق إخراج
يمكنك استخدام `MathJax` لتحويل معادلات LaTeX إلى SVG مباشرة في المتصفح. إليك مثال بسيط:

```html
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
```

ثم يمكنك كتابة معادلات LaTeX داخل عناصر `script` من نوع `math/tex`:

```html
<script type="math/tex">E = mc^2</script>
```

#### 2. استخدام `LaTeX` مع `dvisvgm`
إذا كنت تريد تحويل ملفات LaTeX إلى SVG محليًا، يمكنك استخدام `dvisvgm`. أولاً، قم بتحويل ملف LaTeX إلى DVI باستخدام `latex`:

```bash
latex input.tex
```

ثم قم بتحويل ملف DVI إلى SVG باستخدام `dvisvgm`:

```bash
dvisvgm input.dvi
```

#### 3. استخدام `pandoc` مع `MathJax`
يمكنك أيضًا استخدام `pandoc` لتحويل مستندات LaTeX إلى HTML مع معادلات SVG:

```bash
pandoc input.tex -o output.html --mathjax
```

#### 4. استخدام `MathJax-Node`
إذا كنت تريد تحويل معادلات LaTeX إلى SVG برمجيًا باستخدام Node.js، يمكنك استخدام `mathjax-node`:

```bash
npm install mathjax-node
```

ثم يمكنك استخدام الكود التالي لتحويل معادلة LaTeX إلى SVG:

```javascript
const mjAPI = require("mathjax-node");
mjAPI.config({
  MathJax: {
    svg: {
      fontCache: 'global'
    }
  }
});
mjAPI.start();

mjAPI.typeset({
  math: 'E = mc^2',
  format: 'TeX',
  svg: true,
}, function (data) {
  if (!data.errors) {
    console.log(data.svg);
  }
});
```

هذه بعض الطرق الشائعة لتحويل معادلات LaTeX إلى SVG. يمكنك اختيار الطريقة التي تناسب احتياجاتك بناءً على البيئة التي تعمل فيها.

استمرار المشروع.

```latex
\documentclass[16pt]{article}
\usepackage{amsmath}
\begin{document}
```

\[\tfrac{1}{2}mv^2\]

```latex
\end{document}
```

<img src="/assets/images/feynman/frac.png" alt="frac" style="zoom:50%;" />

هذا يمكن أن يتم عرضه بشكل صحيح. في الكود، قد لا يتم عرضه بشكل صحيح، ربما لأنه لم يتم إضافة `\usepackage{amsmath}`.

```latex
\documentclass[12pt,preview]{standalone}
```

```latex
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{newtxtext}
\usepackage[libertine]{newtxmath}
```

```latex
\begin{document}
\begin{preview}
\tfrac{1}{2}mv^2
\end{preview}
\end{document}
```

```shell
! تم إدخال علامة $ مفقودة.
<النص المُدخل>
                $
l.12 \tfrac{1}{2}
                 mv^2
```

هذا خطأ. وبعد التعديل إلى ما يلي، سيعمل بشكل صحيح.

```latex
\[\tfrac{1}{2}mv^2\]
```

هذا التعبير الرياضي يمثل الطاقة الحركية لجسم ما، حيث:
- \( m \) هي كتلة الجسم.
- \( v \) هي سرعة الجسم.
- \(\tfrac{1}{2}mv^2\) هي الطاقة الحركية للجسم.

إجراء اختبارات مختلفة.

```python
from bs4 import BeautifulSoup
from latex2svg import latex2svg
```

```python
file = open('The Feynman Lectures on Physics Vol. I Ch. 13: Work and Potential Energy (A).html')
content = file.read()
```

```python
soup = BeautifulSoup(content, features="lxml")
```

```python
mathjaxs = soup.findAll('script', {'type': 'math/tex'})
for mathjax in mathjaxs:
    print(mathjax.string)
    wrap = '$' + mathjax.string + '$'
    # إذا كانت 'frac' موجودة في النص الرياضي
    # wrap = '$' + mathjax.string + '$'
    if 'FLP' in mathjax.string:
        continue
    elif 'Fig' in mathjax.string:
        continue
    elif 'eps' in mathjax.string:
        continue
    out = latex2svg(wrap)
    # طباعة الناتج
    node = BeautifulSoup(out['svg'], features="lxml")
    svg = node.find('svg')
    mathjax.insert_after(svg)
    # طباعة SVG الناتج
    # break
    # mathjax.replaceWith(out['svg'])    
    
    # طباعة خصائص mathjax
    # break
    
    # out = latex2svg(wrap)    
    # طباعة SVG الناتج
```

```python
# طباعة عدد العناصر داخل soup
print(len(soup.contents))

# فتح ملف الإخراج للكتابة
output_file = open('out.html', 'w')
# كتابة المحتوى المنسق لـ soup في الملف
output_file.write(soup.prettify())
# إغلاق الملف بعد الانتهاء من الكتابة
output_file.close()

# طباعة محتويات soup (معلّق)
# print(soup.contents)
```

```python
# out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
# print(out['depth'])
# print(out['svg'])
```

في الكود أعلاه، يتم استخدام الدالة `latex2svg` لتحويل معادلة لاتيكس إلى صيغة SVG. يتم تمرير المعادلة \( e^{i \pi} + 1 = 0 \) كسلسلة نصية إلى الدالة. الناتج `out` هو قاموس يحتوي على معلومات حول الصورة الناتجة، بما في ذلك العمق (`depth`) والصيغة SVG (`svg`). يتم طباعة هذه القيم باستخدام `print`.

```python
# svg = open('1.svg', 'w')
# svg.write(out['svg'])
# svg.close()
```

```

أنا أختبر كل هذه الأشياء لأي سبب؟

```python
    if 'FLP' in mathjax.string:
        continue
    elif 'Fig' in mathjax.string:
        continue
    elif 'eps' in mathjax.string:
        continue
```

تم الاحتفاظ بالكود كما هو لأنه يحتوي على أسماء متغيرات وشروط منطقية لا تحتاج إلى ترجمة.

هنا عند التحليل إلى وجود `FLP` و`Fig` و`eps` في مصدر `latex`، حدث خطأ في عملية التحويل.

على سبيل المثال، في `HTML`، قد تجد نصًا برمجيًا مثل هذا:

```html
<script type="math/tex" id="MathJax-Element-11">\FLPF\cdot\FLPv</script>
```

تحليل الحصول على:

```latex
\FLPF\cdot\FLPv
```

**ملاحظة:** النص الموجود في الكود هو رمز رياضي يستخدم في لغة LaTeX لتمثيل الضرب النقطي بين متجه القوة \(\FLPF\) ومتجه السرعة \(\FLPv\). لا يتم ترجمة الرموز الرياضية أو الأكواد البرمجية.

عندما حدث خطأ أثناء التحويل في الكود. أي أن `latex2svg.py` قد فشل. هنا يتم استخدام برنامج `latex` لإجراء التحويل.

```tex
\documentclass{article}
\usepackage{listings}
\usepackage{xcolor}

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}

\lstset{style=mystyle}

\begin{document}

\begin{lstlisting}[language=Python]
def hello_world():
    print("Hello, world!")
\end{lstlisting}

\end{document}
```

```latex
\documentclass[12pt,preview]{standalone}
```

```latex
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{newtxtext}
\usepackage[libertine]{newtxmath}
```

```latex
\begin{document}
\begin{preview}
\begin{equation}
    \FLPF\cdot\FLPv
\end{equation}
\end{preview}
\end{document}
```

```shell
$latex code.tex
! تسلسل تحكم غير معروف.
l.13     \FLPF
              \cdot\FLPv
؟
```

ما هي هذه المشكلة بالتحديد. لاحظت لاحقًا هذا الجزء من الكود في `html`.

```html
<script type="text/x-mathjax-config;executed=true">
      MathJax.Hub.Config({
        TeX: {
          Macros: {
            FLPvec: ["\\boldsymbol{#1}", 1], 
            Figvec: ["\\mathbf{#1}", 1], 
            FLPC: ["\\FLPvec{C}", 0], 
            FLPF: ["\\FLPvec{F}", 0], 
            FLPa: ["\\FLPvec{a}", 0], 
            FLPb: ["\\FLPvec{b}", 0], 
            FLPr: ["\\FLPvec{r}", 0], 
            FLPs: ["\\FLPvec{s}", 0], 
            FLPv: ["\\FLPvec{v}", 0], 
            ddt: ["\\frac{d#1}{d#2}", 2], 
            epsO: ["\\epsilon_0", 0], 
            FigC: ["\\Figvec{C}", 0]
          }
        }
      });
</script>
```

هذا يعني أنه عند عرض الصفحة، تم تعيين وحدات الماكرو لـ `MathJax`. لذلك يجب علينا أيضًا إضافتها في كود تحويل `latex`. دعنا نضيفها.

```latex
\documentclass[12pt,preview]{standalone}
```

```latex
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{newtxtext}
\usepackage[libertine]{newtxmath}
```

\newcommand{\FLPvec}[1]{\boldsymbol{#1}}
\newcommand{\Figvec}[1]{\mathbf{#1}}
\newcommand{\FLPC}{\FLPvec{C}}
\newcommand{\FLPF}{\FLPvec{F}}
\newcommand{\FLPa}{\FLPvec{a}}
\newcommand{\FLPb}{\FLPvec{a}}
\newcommand{\FLPr}{\FLPvec{r}}
\newcommand{\FLPs}{\FLPvec{s}}
\newcommand{\FLPv}{\FLPvec{v}}
\newcommand{\ddt}[2]{\frac{d#1}{d#2}}
\newcommand{\epsO}{\epsilon_0}
\newcommand{\FigC}{\Figvec{C}}
\begin{document}
\begin{preview}
\begin{equation}
    \FLPF\cdot\FLPv
\end{equation}
\end{preview}
\end{document}
```

هذا صحيح.

![fv1](assets/images/feynman/fv1.png)

### تحليل الكود

لنلقِ نظرة على الكود النهائي.

```python
import subprocess
from bs4 import BeautifulSoup
from latex2svg import latex2svg
```

```python
def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()
        
def clean_script(soup):
    scripts = soup.findAll('script')
    for s in scripts:
        s.decompose()    
```

```python
def wrap_latex(mathjax, equation = False):
    wrap = ''
    if equation:
        wrap = mathjax.string
    else:
        wrap = '$' + mathjax.string + '$'
    wrap = wrap.replace('label', 'tag')
    return wrap
 
def wrap_svg(svg, equation):
    if equation:
        p = BeautifulSoup(f'<div style="text-align:center;"></div>', features="lxml")
        p.div.append(svg)
        return p.div
    else:
        return svg
```

```python
def to_svg(mathjaxs, equation=False):
    if equation:
        svg_prefix = 'eq_'
    else:
        svg_prefix = 'in_'
    i = 0
    for mathjax in mathjaxs:     
        print(mathjax.string)
        wrap = wrap_latex(mathjax, equation=equation)   
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err      
            
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
        
        node = BeautifulSoup('<img>', features="lxml")
        img = node.find('img')
        img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'
        img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'
        
        p = wrap_svg(img, equation)
        mathjax.insert_after(p)
        i +=1
```

ترجمة الكود أعلاه:

```python
def to_svg(mathjaxs, equation=False):
    if equation:
        svg_prefix = 'eq_'
    else:
        svg_prefix = 'in_'
    i = 0
    for mathjax in mathjaxs:     
        print(mathjax.string)
        wrap = wrap_latex(mathjax, equation=equation)   
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err      
            
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
        
        node = BeautifulSoup('<img>', features="lxml")
        img = node.find('img')
        img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'
        img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'
        
        p = wrap_svg(img, equation)
        mathjax.insert_after(p)
        i +=1
```

ملاحظة: الكود يبدو أنه يقوم بتحويل معادلات LaTeX إلى صور SVG وحفظها في ملفات، ثم إدراجها في مستند HTML باستخدام BeautifulSoup. الترجمة الحرفية للكود لا تغير من وظيفته، لذا تم ترك الكود كما هو مع شرح بسيط للوظيفة.

```python
def main():    
    file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
    content = file.read()
    
    soup = BeautifulSoup(content, features="lxml")
    clean_mathjax(soup, 'span', 'MathJax')
    clean_mathjax(soup, 'div', 'MathJax_Display')
    clean_mathjax(soup, 'span', 'MathJax_Preview')
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    to_svg(mathjaxs, equation=False)
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    to_svg(mathjaxs, equation=True)
    
    clean_script(soup)
    
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()    
```

```main()
```

عندما نرغب في تحويل كتاب إلكتروني بالكامل، يمكننا أولاً تجربة صفحة واحدة.

```python
    file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
    content = file.read()
```

هنا تم تنزيل صفحة واحدة.

`MathJax` يُنشئ الكثير من عناصر `div` و `span`. على سبيل المثال، المعادلة `T+U=const` يتم إنشاؤها بواسطة MathJax بهذه الطريقة.

```html
<span class="MathJax">T</span>
<span class="MathJax">+</span>
<span class="MathJax">U</span>
<span class="MathJax">=</span>
<span class="MathJax">ثابت</span>
```

هذه الأشياء مزعجة وقد تؤثر على نصنا. نظرًا لأن لدينا بالفعل `svg`، فلا نحتاج إلى هذه الأشياء.

```python
def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()
```

تمت ترجمة الكود إلى:

```python
def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()
```

ملاحظة: الكود بقي كما هو لأنه مكتوب بلغة برمجة (Python) ولا يتم ترجمته.

```python
clean_mathjax(soup, 'span', 'MathJax')
clean_mathjax(soup, 'div', 'MathJax_Display')
clean_mathjax(soup, 'span', 'MathJax_Preview')
```

قم بإزالتها جميعًا.

```python
    mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    to_svg(mathjaxs, equation=False)
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    to_svg(mathjaxs, equation=True)
```

**ملاحظة:** الكود أعلاه مكتوب بلغة Python ويستخدم مكتبة BeautifulSoup لاستخراج عناصر النصوص الرياضية من صفحة ويب وتحويلها إلى صيغة SVG. لا يحتاج الكود إلى ترجمة حيث أن الأوامر والمتغيرات مكتوبة بالإنجليزية وهي جزء من بناء الجملة البرمجية.

لاحظ أن هناك نوعين من `script` هنا.

```latex
m(dv/dt)=F
```

**ترجمة المعادلة:**

تُعبر المعادلة عن القانون الثاني لنيوتن للحركة، حيث:
- \( m \) هي كتلة الجسم.
- \( \frac{dv}{dt} \) هي معدل تغير السرعة بالنسبة للزمن (التسارع).
- \( F \) هي القوة المؤثرة على الجسم.

**الصيغة الرياضية:**
\[ m \frac{dv}{dt} = F \]

**التفسير:**
القوة المؤثرة على جسم ما تساوي كتلة الجسم مضروبة في تسارعه.

هذا هو النموذج المضمن.

```latex
\begin{equation}
\underset{\text{الطاقة الحركية}}{\tfrac{1}{2}mv^2}+
\underset{\text{الطاقة الكامنة}}{\vphantom{\tfrac{1}{2}}mgh}=\text{ثابت},\notag
```

هذا هو النص بشكل فقرات.

عند استخدام الصيغة المضمنة، يجب إضافة `$` أو `[]` حول التعبير. وإلا فقد يحدث خطأ.

```latex
\begin{document}
\begin{preview}
\tfrac{1}{2}mv^2
\end{preview}
\end{document}
```

```shell
! تم إدخال علامة $ مفقودة.
<النص المُدخل>
                $
l.26 \tfrac{1}{2}
                 mv^2
```

يجب أن يتم تغييره إلى هذا:

```latex
\begin{document}
\begin{preview}
$\tfrac{1}{2}mv^2$
\end{preview}
\end{document}
```

لنرى الآن كيفية تحويل `latex` إلى `svg`.

```python
    if equation:
        svg_prefix = 'eq_'
    else:
        svg_prefix = 'in_'
```

```shell
% tree svgs
svgs
├── eq_0.svg
├── eq_1.svg
├── in_0.svg
```

هكذا يتم حفظ `svg`.

```python
def wrap_latex(mathjax, equation = False):
    wrap = ''
    if equation:
        wrap = mathjax.string
    else:
        wrap = '$' + mathjax.string + '$'
    wrap = wrap.replace('label', 'tag')
    return wrap
```

هنا سنقوم بإجراء بعض التعديلات على كود `latex`. لاحظ أن `label` قد تحولت إلى `tag`.

![علامة](assets/images/feynman/tag.png)

لاحظ `(Eq:I:13:14)` على الجانب الأيمن. إذا كان `label`، فإنه لم يتم تحليله بنجاح. سيظهر هذا كـ `(1)`. هنا نستخدم `tag` للإشارة إليه مؤقتًا، ولم نتعمق في البحث بعد.

ثم يتم استدعاء `latex2svg.py`.

```python
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err    
```

**ملاحظة:** الكود الموجود في الملف الأصلي مكتوب بلغة Python ولا يحتاج إلى ترجمة، حيث أن الأكواد البرمجية تبقى كما هي بغض النظر عن اللغة المستخدمة في الوثيقة.

اطلع على `latex2svg.py`.

```python
    # تشغيل LaTeX وإنشاء ملف DVI
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('latex غير موجود')
```

هنا يتم استدعاء أمر `latex`.

```shell
 % latex --help
الاستخدام: pdftex [خيار]... [اسم الملف[.tex]] [أوامر]
   أو: pdftex [خيار]... \السطر الأول
   أو: pdftex [خيار]... &تنسيق ARGS
  تشغيل pdfTeX على اسم الملف، عادةً ما يتم إنشاء اسم الملف.pdf.
```

```python
    try:
        ret = subprocess.run(shlex.split(params['dvisvgm_cmd']+' code.dvi'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory, env=env)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('لم يتم العثور على dvisvgm')
```

هنا يتم استدعاء أمر `dvisvgm`.

```shell
% dvisvgm
dvisvgm 2.9.1
```

هذا البرنامج يحول ملفات DVI، التي يتم إنشاؤها بواسطة TeX/LaTeX، بالإضافة إلى ملفات EPS وPDF، إلى تنسيق SVG القائم على XML والذي يعتبر تنسيقًا متجهيًا قابلًا للتحجيم.

الاستخدام: dvisvgm [خيارات] ملف_dvi
       dvisvgm --eps [خيارات] ملف_eps
       dvisvgm --pdf [خيارات] ملف_pdf
```

أين تكتب وحدات الماكرو المخصصة لـ `latex` التي تم ذكرها أعلاه؟ هنا يجب تعديل `latex2svg.py`. قم بتعديل `default_preamble`.

```python
default_preamble = r"""
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{newtxtext}
\usepackage[libertine]{newtxmath}
```

\newcommand{\FLPvec}[1]{\boldsymbol{#1}}
\newcommand{\Figvec}[1]{\mathbf{#1}}
\newcommand{\FLPC}{\FLPvec{C}}
\newcommand{\FLPF}{\FLPvec{F}}
\newcommand{\FLPa}{\FLPvec{a}}
\newcommand{\FLPb}{\FLPvec{a}}
\newcommand{\FLPr}{\FLPvec{r}}
\newcommand{\FLPs}{\FLPvec{s}}
\newcommand{\FLPv}{\FLPvec{v}}
\newcommand{\ddt}[2]{\frac{d#1}{d#2}}
\newcommand{\epsO}{\epsilon_0}
\newcommand{\FigC}{\Figvec{C}}
"""
```

بعد التحويل بنجاح، يتم الكتابة إلى الملف.

```python
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
```

استمر.

```python
        node = BeautifulSoup('<img>', features="lxml")
        img = node.find('img')
        img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'
        img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'
```

**ترجمة الكود إلى العربية:**

```python
        node = BeautifulSoup('<img>', features="lxml")  # إنشاء كائن BeautifulSoup من وسم <img>
        img = node.find('img')  # البحث عن وسم <img> داخل الكائن
        img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'  # تعيين السمة 'src' لمسار ملف SVG
        img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'  # تعيين السمة 'style' لتنسيق الصورة
```

**ملاحظة:** تم الحفاظ على الكود الأصلي كما هو لأنه يتضمن أسماء مكتبات ووظائف محددة (مثل `BeautifulSoup`) والتي لا يتم ترجمتها عادةً. تمت إضافة التعليقات باللغة العربية لشرح الكود.

هنا نقوم بإنشاء وسم `img`.

```python
def wrap_svg(svg, equation):
    if equation:
        p = BeautifulSoup(f'<div style="text-align:center;"></div>', features="lxml")
        p.div.append(svg)
        return p.div
    else:
        return svg
      
p = wrap_svg(img, equation)
```

تمت ترجمة الكود أعلاه إلى:

```python
def wrap_svg(svg, equation):
    if equation:
        p = BeautifulSoup(f'<div style="text-align:center;"></div>', features="lxml")
        p.div.append(svg)
        return p.div
    else:
        return svg
      
p = wrap_svg(img, equation)
```

ملاحظة: الكود لم يتغير لأنه يحتوي على أسماء متغيرات ودوال بالإنجليزية، ولم يتم تغييرها وفقًا للتعليمات.

إذا كانت `latex` عبارة عن فقرة واحدة، فقم بتغليفها باستخدام `div` وتوسيطها.

```python
mathjax.insert_after(p)
```

هنا يتم إضافة وسم `div` أو وسم `img` بعد وسم `script` الأصلي.

```python
def clean_script(soup):
    scripts = soup.findAll('script')
    for s in scripts:
        s.decompose()    
        
clean_script(soup)
```

**ترجمة الكود إلى العربية:**

```python
def تنظيف_النصي(soup):
    النصوص = soup.findAll('script')
    for نص in النصوص:
        نص.decompose()    
        
تنظيف_النصي(soup)
```

في هذا الكود، يتم تعريف دالة `تنظيف_النصي` التي تقوم بإزالة جميع عناصر النصوص البرمجية (`script`) من كائن `soup` الذي يمثل وثيقة HTML. يتم استخدام `findAll` للعثور على جميع العناصر من نوع `script`، ثم يتم استخدام `decompose` لإزالة كل عنصر نصي من الوثيقة.

بعد استبدال جميع عناصر `latex` بـ `svg`، لن تكون هناك حاجة إلى `script`. قم بحذفها لجعل الكود أكثر نظافة.

أخيرًا، يتم كتابة `html` المعدل بالكامل في ملف.

```python
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()    
```

ثم استخدم أداة `pandoc` لتحويلها إلى صيغة `epub`.

```shell
pandoc -s -r html out.html -o feynman.epub
```

سيتم فتح كتاب إلكتروني جميل.

لماذا لا يتم تضمين علامة `svg` مباشرة، بدلاً من استخدام `img` لإدراجها؟ أي بكتابة مثل هذا:

```html
<p></p>
<svg></svg>
<p></p>
```

هناك `bug` غريب جدًا. عندما يكون هناك الكثير من ملفات `svg`، يحدث شيء مثل هذا.

<img src="/assets/images/feynman/svg_p1.png" alt="svg_p1" style="zoom:40%;" />

لاحقًا اكتشفت أنه يمكن استخدام `img` لإدراج الصور. أما عن سبب ذلك، لم أفهمه تمامًا. عندما أخذت هذا الـ `svg` الفردي وعرضته في المتصفح، لم تكن هناك مشكلة. يبدو أن المشكلة تحدث عندما يقوم المتصفح بعرض عدد كبير جدًا من ملفات `svg` في نفس الوقت.

### الختام

أما بالنسبة لكيفية تحويل `epub` إلى `mobi`، يمكنك استخدام الأداة الرسمية من `Kindle` وهي `Kindle Previewer 3`. لاحظ أن هذا مجرد فصل واحد.

كود المشروع موجود في [feynman-lectures-mobi@lzwjava](https://github.com/lzwjava/feynman-lectures-mobi).

كيف يمكن استخراج جميع الصفحات وتنظيمها في كتاب إلكتروني؟ سنتحدث عن ذلك لاحقًا. ولكن هذا الفصل من محاضرات فينمان في الفيزياء كافٍ للقراءة. حسنًا، لنبدأ القراءة على جهاز Kindle.