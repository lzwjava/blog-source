---
lang: hant
layout: post
title: mathjax2mobi：将MathJax HTML转换为电子书
---

### 项目简介

本项目旨在开发一款高效、易用的任务管理工具，帮助用户更好地组织和跟踪日常任务。通过简洁的界面和强大的功能，用户可以轻松创建、分配和监控任务进度，从而提高工作效率和团队协作能力。

首先，我来大致介绍一下项目的情况。

![费曼在线](assets/images/feynman/feynman_online.jpg)

<img src="/assets/images/feynman/change.JPG" alt="改变" style="zoom:50%;" />

![latex](assets/images/feynman/latex.JPG)

![epub_black](assets/images/feynman/epub_black.JPG)

![epub_beautiful](assets/images/feynman/epub_beautiful.JPG)

项目完成后，心中洋溢着喜悦。于是，我写下了这样一段话。

经过一整天的编程努力，终于成功制作出了精美的费曼物理讲义电子书！费曼物理讲义原本公开在网络上，采用`LaTeX`进行渲染。`LaTeX`常用于撰写学术论文，其对数学公式的呈现效果尤为出色。而网络版则借助了`MathJax`这一库，将`LaTeX`源代码转换为`HTML`代码，生成了大量的`div`和`span`标签。然而，电子书格式并不支持这种呈现方式。于是，我的思路是抓取网页内容，逆向解析`MathJax`的渲染过程，然后将公式替换为`SVG`图片。这一过程中遇到了不少挑战：首先，源代码中包含了大量自定义的`LaTeX`宏，需要逐一添加；其次，内嵌多个`SVG`图片时会出现问题。单个`SVG`尚能正常显示，但数量一多，便可能触发浏览器与`SVG`之间的某些诡异Bug。解决方法是，将`SVG`保存为文件，再通过`img`标签引入。此外，公式还分为两种类型：一种是嵌入文本中的公式，另一种是单独成行的公式。最终，克服了种种困难，我如愿以偿地获得了这本排版精美的电子书！

### 查询的资料

这里记录了在解决项目过程中所查阅的资料。由于这是一个教程，旨在向学生展示完成一个项目的大致体验。

![](assets/images/feynman/s1.PNG)

![](assets/images/feynman/s2.PNG)

![](assets/images/feynman/s3.PNG)

![](assets/images/feynman/s4.PNG)

![](assets/images/feynman/s5.PNG)

![](assets/images/feynman/s6.PNG)

![](assets/images/feynman/s7.PNG)

![](assets/images/feynman/s8.PNG)

### 启动项目

费曼物理学讲义已经在网上公开供阅读。我打算在`Kindle`上阅读它。不过，由于其中包含大量数学公式，其原稿很可能是用`LaTeX`编写的。网站使用`MathJax`这个库来将`LaTeX`格式的内容渲染到网页上。

舉個例子。

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

上面是截取的一段`html`代码。在这一块`html`代码中，`script`标签下包含的是`LaTeX`的原样文本。`MathJax`将其转换为许多`span`标签，以便在网页上正确显示数学公式。

我们现在有个思路，就是把`MathJax`的显示方式改为`SVG`图片。

从 GitHub 上找到一个项目 `tuxu/latex2svg`。

```python
from latex2svg import latex2svg
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

試著運行，但出錯了。

```shell
    raise RuntimeError('未找到latex')
RuntimeError: 未找到latex
```

查看代码。

```python
    # 運行 LaTeX 並創建 DVI 文件
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('未找到 latex')
```

原来这也依赖于`latex`命令。

安裝一下。

```shell
brew install --cask mactex
==> 注意事項
您必須重新啟動終端機窗口，以使 MacTex CLI 工具的安裝生效。
或者，Bash 和 Zsh 用戶可以運行以下命令：
  eval "$(/usr/libexec/path_helper)"
==> 正在下載 http://mirror.ctan.org/systems/mac/mactex/mactex-20200407.pkg
==> 正在從 https://mirrors.aliyun.com/CTAN/systems/mac/mactex/mactex-20200407.pkg 下載
######################################################################## 100.0%
所有公式依賴項已滿足。
==> 正在安裝 Cask mactex
==> 正在運行 mactex 的安裝程序；可能需要您的密碼。
installer: 套件名稱是 MacTeX
installer: 選擇更改文件 '/private/tmp/choices20210315-4643-5884ro.xml' 已應用
installer: 正在基礎路徑 / 安裝
installer: 安裝成功。
🍺  mactex 已成功安裝！
```

安裝成功。

```shell
% latex
這是 pdfTeX，版本 3.14159265-2.6-1.40.21 (TeX Live 2020) (預載格式=latex)
 已啟用受限的 \write18。
**
```

```python
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

這段程式碼的功能是將 LaTeX 數學表達式 `\( e^{i \pi} + 1 = 0 \)` 轉換為 SVG 格式的圖像，並輸出其深度和 SVG 內容。以下是程式碼的解釋：

1. `latex2svg(r'\( e^{i \pi} + 1 = 0 \)')`：這行代碼使用 `latex2svg` 函數將 LaTeX 表達式轉換為 SVG 格式。`r` 表示原始字符串，避免轉義字符的影響。

2. `out['depth']`：這行代碼輸出 SVG 圖像的深度信息。

3. `out['svg']`：這行代碼輸出 SVG 圖像的內容。

這段程式碼的輸出將包括 SVG 圖像的深度和 SVG 圖像本身的內容。

```python
svg = open('1.svg', 'w')
svg.write(out['svg'])
svg.close()
```

翻譯成繁體中文：

```python
svg = open('1.svg', 'w')
svg.write(out['svg'])
svg.close()
```

這段程式碼的功能是打開一個名為 `1.svg` 的文件，並將 `out['svg']` 的內容寫入該文件，然後關閉文件。這段程式碼在繁體中文環境中的功能和寫法與英文環境中相同，因此不需要進行翻譯。

可以生成`svg`了。

所以尝试将`MathJax`中获取的`LaTeX`文本全部生成一遍。

```python
from bs4 import BeautifulSoup
from latex2svg import latex2svg
```

文件 = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
内容 = 文件.read()

soup = BeautifulSoup(content)

```python
mathjaxs = soup.findAll('script', {'type': 'math/tex'})
for mathjax in mathjaxs:
    print(mathjax.string)
    out = latex2svg(mathjax.string)
    print(out['svg'])
```

這段程式碼的功能是從網頁中找出所有類型為 `math/tex` 的 `<script>` 標籤，並將其中的 LaTeX 數學公式轉換為 SVG 格式的圖像。以下是程式碼的逐步解釋：

1. **`soup.findAll('script', {'type': 'math/tex'})`**:
   - 這行程式碼使用 BeautifulSoup 的 `findAll` 方法來查找所有類型為 `math/tex` 的 `<script>` 標籤。
   - `soup` 是一個 BeautifulSoup 物件，代表解析後的 HTML 文檔。
   - `findAll` 方法返回一個包含所有符合條件的標籤的列表。

2. **`for mathjax in mathjaxs:`**:
   - 這行程式碼開始一個迴圈，遍歷所有找到的 `<script>` 標籤。

3. **`print(mathjax.string)`**:
   - 這行程式碼打印出當前 `<script>` 標籤中的文本內容，即 LaTeX 數學公式。

4. **`out = latex2svg(mathjax.string)`**:
   - 這行程式碼將 LaTeX 數學公式轉換為 SVG 格式的圖像。
   - `latex2svg` 是一個假設存在的函數，負責將 LaTeX 公式轉換為 SVG。
   - 轉換結果存儲在 `out` 變數中。

5. **`print(out['svg'])`**:
   - 這行程式碼打印出轉換後的 SVG 圖像內容。
   - `out['svg']` 假設是 `latex2svg` 函數返回的字典中的一個鍵，對應的值是 SVG 圖像的字符串表示。

總結來說，這段程式碼的目的是從網頁中提取 LaTeX 數學公式，並將其轉換為 SVG 圖像，然後打印出這些圖像的內容。

可惜出错了。

```python
    raise CalledProcessError(self.returncode, self.args, self.stdout,
subprocess.CalledProcessError: 命令 '['latex', '-interaction', 'nonstopmode', '-halt-on-error', 'code.tex']' 返回了非零退出狀態 1。
```

具体是哪个公式出错了呢？

```latex
\tfrac{1}{2}mv^2
```

翻譯為：

```latex
\frac{1}{2}mv^2
```

這是動能公式，表示物體的動能等於其質量 \( m \) 乘以速度 \( v \) 的平方的一半。

## LaTeX

LaTeX 是一种基于 TeX 的排版系统，广泛用于生成高质量的科技和数学文档。它由 Leslie Lamport 在 1980 年代初期开发，主要用于处理复杂的数学公式和排版需求。LaTeX 通过使用标记语言来定义文档的结构和格式，使得用户可以专注于内容而非排版细节。

### 主要特点
1. **高质量的排版**：LaTeX 生成的文档具有专业级的排版质量，特别是在数学公式和科学文献方面。
2. **跨平台**：LaTeX 可以在多种操作系统上运行，包括 Windows、macOS 和 Linux。
3. **开源**：LaTeX 是免费且开源的，拥有庞大的用户社区和丰富的资源。
4. **强大的扩展性**：通过使用各种宏包（packages），用户可以扩展 LaTeX 的功能，以满足特定的排版需求。

### 基本语法
LaTeX 文档通常以 `.tex` 为扩展名，以下是一个简单的 LaTeX 文档示例：

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{示例文档}
\author{作者姓名}
\date{\today}

\begin{document}

\maketitle

\section{引言}
这是一个简单的 LaTeX 文档示例。

\section{数学公式}
LaTeX 非常适合排版数学公式，例如：
\[
E = mc^2
\]

\end{document}
```

### 常用命令
- `\documentclass{...}`：定义文档类型（如 article、report、book 等）。
- `\usepackage{...}`：加载宏包以扩展功能。
- `\title{...}`、`\author{...}`、`\date{...}`：定义文档的标题、作者和日期。
- `\begin{document}` 和 `\end{document}`：文档内容的开始和结束。
- `\section{...}`：定义章节标题。

### 编译 LaTeX 文档
LaTeX 文档需要通过编译生成最终的 PDF 文件。常用的编译工具有：
- **pdflatex**：直接生成 PDF 文件。
- **latex** + **dvips** + **ps2pdf**：生成 DVI 文件，再转换为 PDF。
- **xelatex**：支持 Unicode 和现代字体，适合处理多语言文档。

### 学习资源
- [LaTeX 项目官方网站](https://www.latex-project.org/)
- [Overleaf](https://www.overleaf.com/)：在线 LaTeX 编辑器，适合初学者。
- [CTAN](https://www.ctan.org/)：Comprehensive TeX Archive Network，提供大量的 LaTeX 宏包和文档。

LaTeX 虽然有一定的学习曲线，但一旦掌握，它将极大地提高文档排版的效率和质量。

来学习一下`LaTeX`。

```latex
\documentclass[12pt]{article}
\usepackage{lingmacros}
\usepackage{tree-dvips}
\begin{document}
```

\section*{论文笔记}

别忘了包含主题化的例子。
它们看起来像这样：

{\small
\enumsentence{主题化自句子主语：\\ 
\shortex{7}{a 约翰$_i$ [a & 清楚 & [el & 
  {\bf l-}爱 & er & 他$_i$ & a 玛丽]]}
{ & {\bf R-}清楚 & {\sc 补语} & 
  {\bf IR}.{\sc 3s}-爱   & P & 他 & }
{约翰，（显然）玛丽爱（他）。}}
}

\subsection*{如何处理话题化}

我将假设一个如 (\ex{1}) 所示的树形结构。

{\small
\enumsentence{A$'$投射的结构：\\ [2ex]
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

\subsection*{情绪}

当话题存在时，以及当WH移位发生时，语气会发生变化。\emph{非现实}语气出现在Comp位置有非主语话题或WH短语时。\emph{现实}语气则出现在Comp位置有主语话题或WH短语时。

\end{document}
```

在网上找到了一段样例的`LaTeX`源码。

```shell
% latex code.tex
這是 pdfTeX，版本 3.14159265-2.6-1.40.21 (TeX Live 2020) (預載格式=latex)
 啟用了受限的 \write18。
進入擴展模式
(./code.tex
LaTeX2e <2020-02-02> 補丁級別 5
L3 編程層 <2020-03-06>
(/usr/local/texlive/2020/texmf-dist/tex/latex/base/article.cls
文檔類別：article 2019/12/20 v1.4l 標準 LaTeX 文檔類別
(/usr/local/texlive/2020/texmf-dist/tex/latex/base/size12.clo))
(/usr/local/texlive/2020/texmf-dist/tex/latex/tree-dvips/lingmacros.sty)
(/usr/local/texlive/2020/texmf-dist/tex/latex/tree-dvips/tree-dvips.sty
tree-dvips 版本 .91，1995年5月16日
) (/usr/local/texlive/2020/texmf-dist/tex/latex/l3backend/l3backend-dvips.def)
(./code.aux) [1] (./code.aux) )
輸出寫入 code.dvi (1 頁，3416 字節)。
記錄寫入 code.log。
```

![latex](assets/images/feynman/latex.png)

来对照源码和渲染后的效果，看看能学到什么。

```latex
\begin{document}
\end{document}
```

这样来把文档包裹起来。

```latex
\section*{论文笔记}
```

這表示`section`標題開頭。

```latex
\subsection*{如何处理主题化}
```

這表示子標題。

```latex
\shortex{7}{a John$_i$ [a & kltukl & [el & 
  {\bf l-}oltoir & er & ngii$_i$ & a Mary]]}
```

這段代碼是使用 LaTeX 排版的一個例子，通常用於語言學中的語法分析。它展示了一個句子的結構，其中包含了一些特定的標記和符號。以下是這段代碼的翻譯和解釋：

- `\shortex{7}`：這是一個命令，用於創建一個語法分析的例子，數字 `7` 可能表示某種格式或對齊方式。
- `a John$_i$`：這部分表示句子中的主語 "John"，下標 `$_i$` 可能表示這是一個變量或特定的語法標記。
- `[a & kltukl & [el & {\bf l-}oltoir & er & ngii$_i$ & a Mary]]`：這是一個嵌套的結構，表示句子的其他部分。每個 `&` 符號分隔不同的成分，`{\bf l-}oltoir` 中的 `{\bf l-}` 可能表示某種強調或特定的語法標記。

整體來看，這段代碼展示了一個句子的語法結構，可能用於語言學研究中的語法分析或句法樹的表示。具體的語言和語法規則需要根據上下文來進一步解釋。

![短例](assets/images/feynman/shortex.png)

可见`$_i$`來表示下標。`{\bf l-}`來表示加粗。

```latex
\enumsentence{A$'$ 投射的結構：\\ [2ex]
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

<img src="/assets/images/feynman/node.png" alt="节点" style="zoom:50%;" />

注意到使用`nodeconnect`來表示連線。

要将 LaTeX 公式转换为 SVG 格式，可以使用多种工具和方法。以下是几种常见的方式：

### 1. 使用 `MathJax` 和 `Node.js`
`MathJax` 是一个流行的 JavaScript 库，用于在网页上渲染数学公式。你可以使用 `MathJax` 和 `Node.js` 将 LaTeX 公式转换为 SVG。

#### 步骤：
1. 安装 `MathJax` 和 `Node.js`：
   ```bash
   npm install mathjax
   ```

2. 创建一个 JavaScript 文件（例如 `convert.js`）：
   ```javascript
   const { mathjax } = require('mathjax-full/js/mathjax');
   const { TeX } = require('mathjax-full/js/input/tex');
   const { SVG } = require('mathjax-full/js/output/svg');
   const { liteAdaptor } = require('mathjax-full/js/adaptors/liteAdaptor');
   const { RegisterHTMLHandler } = require('mathjax-full/js/handlers/html');

   const adaptor = liteAdaptor();
   RegisterHTMLHandler(adaptor);

   const tex = new TeX();
   const svg = new SVG();

   const html = mathjax.document('', {
       InputJax: tex,
       OutputJax: svg
   });

   const equation = '\\frac{a}{b} + \\sqrt{c}';
   const node = html.convert(equation, {
       display: true
   });

   console.log(adaptor.outerHTML(node));
   ```

3. 运行脚本：
   ```bash
   node convert.js
   ```

   这将输出 SVG 代码，你可以将其保存为 `.svg` 文件。

### 2. 使用 `LaTeX` 和 `dvisvgm`
如果你已经安装了 LaTeX 发行版（如 TeX Live 或 MiKTeX），你可以使用 `dvisvgm` 工具将 LaTeX 文档转换为 SVG。

#### 步骤：
1. 创建一个 LaTeX 文件（例如 `equation.tex`）：
   ```latex
   \documentclass{standalone}
   \usepackage{amsmath}
   \begin{document}
   \[
   \frac{a}{b} + \sqrt{c}
   \]
   \end{document}
   ```

2. 编译 LaTeX 文件为 DVI 格式：
   ```bash
   latex equation.tex
   ```

3. 使用 `dvisvgm` 将 DVI 文件转换为 SVG：
   ```bash
   dvisvgm equation.dvi
   ```

   这将生成一个 `equation.svg` 文件。

### 3. 使用在线工具
如果你不想在本地安装任何工具，可以使用在线工具将 LaTeX 公式转换为 SVG。以下是一些常用的在线工具：

- [MathJax Demo](https://www.mathjax.org/#demo)
- [QuickLaTeX](https://www.quicklatex.com/)
- [CodeCogs LaTeX Editor](https://www.codecogs.com/latex/eqneditor.php)

这些工具通常允许你输入 LaTeX 公式并直接生成 SVG 图像。

### 4. 使用 `Pandoc` 和 `wkhtmltopdf`
`Pandoc` 是一个强大的文档转换工具，结合 `wkhtmltopdf` 可以将 LaTeX 文档转换为 SVG。

#### 步骤：
1. 安装 `Pandoc` 和 `wkhtmltopdf`：
   ```bash
   sudo apt-get install pandoc wkhtmltopdf
   ```

2. 创建一个 LaTeX 文件（例如 `equation.tex`）：
   ```latex
   \documentclass{standalone}
   \usepackage{amsmath}
   \begin{document}
   \[
   \frac{a}{b} + \sqrt{c}
   \]
   \end{document}
   ```

3. 使用 `Pandoc` 将 LaTeX 文件转换为 HTML：
   ```bash
   pandoc equation.tex -o equation.html
   ```

4. 使用 `wkhtmltopdf` 将 HTML 转换为 SVG：
   ```bash
   wkhtmltoimage --format svg equation.html equation.svg
   ```

   这将生成一个 `equation.svg` 文件。

### 总结
以上是几种将 LaTeX 公式转换为 SVG 的常见方法。你可以根据自己的需求选择合适的方法。如果你需要频繁地进行转换，建议使用本地工具如 `MathJax` 或 `dvisvgm`。如果只是偶尔需要转换，使用在线工具可能更为方便。

继续项目。

```latex
\documentclass[16pt]{article}
\usepackage{amsmath}
\begin{document}
```

\[\tfrac{1}{2}mv^2\] 表示的是物体的动能，其中 \(m\) 是物体的质量，\(v\) 是物体的速度。这个公式表明，物体的动能与其质量和速度的平方成正比。

\end{document}
```

<img src="/assets/images/feynman/frac.png" alt="frac" style="zoom:50%;" />

這樣可以正確地被渲染。在程式碼裡無法被渲染，可能是因為沒有加上`\usepackage{amsmath}`。

```latex
\documentclass[12pt,preview]{standalone}
```

\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{newtxtext}
\usepackage[libertine]{newtxmath}

\begin{document}
\begin{preview}
\tfrac{1}{2}mv^2
\end{preview}
\end{document}
```

```shell
! 缺少 $ 插入。
<插入的文本>
                $
l.12 \tfrac{1}{2}
                 mv^2
```

這樣出錯了。而改成這樣就可以了。

```latex
\[\tfrac{1}{2}mv^2\]
```

翻譯成繁體中文為：

```latex
\[\tfrac{1}{2}mv^2\]
```

這是一個物理公式，表示動能（Kinetic Energy），其中：
- \( m \) 是物體的質量，
- \( v \) 是物體的速度。

公式的意思是：動能等於物體質量的一半乘以速度的平方。

進行各種試探。

```python
from bs4 import BeautifulSoup
from latex2svg import latex2svg
```

文件 = open('费曼物理学讲义 第一卷 第十三章：功与势能 (A).html')
内容 = 文件.read()

soup = BeautifulSoup(content, features="lxml")

```python
mathjaxs = soup.findAll('script', {'type': 'math/tex'})
for mathjax in mathjaxs:
    print(mathjax.string)
    wrap = '$' + mathjax.string + '$'
    # 如果 mathjax.string 包含 'frac'，则 wrap = '$' + mathjax.string + '$'
    # if 'frac' in mathjax.string:
    #     wrap = '$' + mathjax.string + '$'
    if 'FLP' in mathjax.string:
        continue
    elif 'Fig' in mathjax.string:
        continue
    elif 'eps' in mathjax.string:
        continue
    out = latex2svg(wrap)
    # print(out)
    node = BeautifulSoup(out['svg'], features="lxml")
    svg = node.find('svg')
    mathjax.insert_after(svg)
    # print(out['svg'])
    # break
    # mathjax.replaceWith(out['svg'])    
    
    # print(dir(mathjax))
    # break
    
    # out = latex2svg(wrap)    
    # print(out['svg'])
```

# print(len(soup.contents))
    
output_file = open('out.html', 'w')
output_file.write(soup.prettify())
output_file.close()
# print(soup.contents)

# out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
# print(out['depth'])
# print(out['svg'])

# svg = open('1.svg', 'w')
# svg.write(out['svg'])
# svg.close()

```
```

這些我都在試探什麼呢。

```python
    if 'FLP' in mathjax.string:
        continue
    elif '圖' in mathjax.string:  # 'Fig' 翻譯為 '圖'
        continue
    elif 'eps' in mathjax.string:
        continue
```

这里在解析到`latex`源码中包含`FLP`、`Fig`、`eps`时，转换过程出现了错误。

例如，在`HTML`中，有這樣的腳本：

```html
<script type="math/tex" id="MathJax-Element-11">\FLPF\cdot\FLPv</script>
```

解析拿到：

```latex
\FLPF\cdot\FLPv
```

這段 LaTeX 代碼表示向量 \(\mathbf{F}\) 與向量 \(\mathbf{v}\) 的點積（內積）。在數學中，點積是兩個向量之間的一種運算，結果是一個標量（純量）。具體來說，\(\mathbf{F} \cdot \mathbf{v}\) 表示向量 \(\mathbf{F}\) 和向量 \(\mathbf{v}\) 的點積。

如果你需要將這段代碼翻譯成其他語言或解釋其含義，請告訴我！

在代码转换过程中出现了错误。也就是说，`latex2svg.py` 出错了。这里我们使用 `latex` 程序来进行转换。

`code.tex` 是一个文件名，通常用于存储与编程相关的 LaTeX 文档。LaTeX 是一种基于 TeX 的排版系统，广泛用于生成高质量的科技和数学文档。`code.tex` 文件可能包含用于排版代码、算法、数学公式或其他技术内容的 LaTeX 代码。

如果你需要翻译 `code.tex` 文件中的内容，请提供文件的具体内容，我将帮助你进行翻译。

```latex
\documentclass[12pt,preview]{standalone}
```

\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{newtxtext}
\usepackage[libertine]{newtxmath}

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
! 未定义的命令序列。
l.13     \FLPF
              \cdot\FLPv
?
```

这到底是什么问题。我后来才注意到在`html`中的这段代码。

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

这意味着在网页渲染时，已经为`MathJax`配置了宏。因此，在我们的`latex`转换源码中也应当加入相应的宏定义。现在就来添加它们吧。

```latex
\documentclass[12pt,preview]{standalone}
```

\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{newtxtext}
\usepackage[libertine]{newtxmath}

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

這樣就對了。

![fv1](assets/images/feynman/fv1.png)

### 分析代码

在分析代码时，通常需要遵循以下步骤：

1. **理解代码的功能**：
   - 首先，明确代码的总体目标是什么。它是在处理数据、执行计算、还是控制某个设备？
   - 了解代码的输入和输出是什么。

2. **阅读代码结构**：
   - 查看代码的整体结构，包括函数、类、模块等。
   - 注意代码的缩进和格式，这有助于理解代码的逻辑结构。

3. **逐行分析**：
   - 逐行阅读代码，理解每一行代码的作用。
   - 注意变量名、函数名和类名，它们通常能提供关于代码功能的线索。

4. **调试和测试**：
   - 如果可能，运行代码并观察其行为。
   - 使用调试工具逐步执行代码，查看变量的值和程序的流程。

5. **查找文档和注释**：
   - 阅读代码中的注释，它们通常提供了关于代码功能的额外信息。
   - 查找相关的文档或API参考，了解使用的库或框架。

6. **优化和改进**：
   - 识别代码中的潜在问题，如性能瓶颈、安全漏洞或可读性问题。
   - 提出改进建议，如重构代码、优化算法或增加错误处理。

7. **总结和报告**：
   - 总结代码的功能和结构。
   - 报告发现的问题和改进建议。

### 示例代码分析

假设我们有以下Python代码：

```python
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]
result = calculate_sum(numbers)
print("The sum is:", result)
```

**分析步骤**：

1. **理解代码的功能**：
   - 这段代码的功能是计算一个列表中所有数字的总和。

2. **阅读代码结构**：
   - 代码定义了一个函数 `calculate_sum`，该函数接受一个列表 `numbers` 作为参数。
   - 函数内部使用一个 `for` 循环遍历列表中的每个数字，并将其累加到 `total` 变量中。
   - 最后，函数返回 `total` 的值。

3. **逐行分析**：
   - `def calculate_sum(numbers):` 定义了一个函数 `calculate_sum`。
   - `total = 0` 初始化一个变量 `total`，用于存储累加的结果。
   - `for number in numbers:` 遍历列表 `numbers` 中的每个元素。
   - `total += number` 将当前元素的值加到 `total` 上。
   - `return total` 返回累加的结果。
   - `numbers = [1, 2, 3, 4, 5]` 定义了一个包含数字的列表。
   - `result = calculate_sum(numbers)` 调用 `calculate_sum` 函数，并将结果存储在 `result` 变量中。
   - `print("The sum is:", result)` 打印出计算结果。

4. **调试和测试**：
   - 运行代码，输出应为 `The sum is: 15`，这是列表 `[1, 2, 3, 4, 5]` 的总和。

5. **查找文档和注释**：
   - 代码中没有注释，但变量名和函数名清晰地表达了代码的功能。

6. **优化和改进**：
   - 代码已经非常简洁和高效，没有明显的优化空间。
   - 可以增加一些错误处理，例如检查输入是否为列表或列表中的元素是否为数字。

7. **总结和报告**：
   - 代码成功地计算了列表中所有数字的总和。
   - 代码结构清晰，易于理解。
   - 建议增加输入验证以提高代码的健壮性。

通过以上步骤，我们可以全面地分析和理解代码的功能和结构。

来看看最终的代码。

```python
import subprocess
from bs4 import BeautifulSoup
from latex2svg import latex2svg
```

```python
def clean_mathjax(soup, name, cls):
    # 查找所有具有指定類名的元素
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        # 移除這些元素
        preview.decompose()
        
def clean_script(soup):
    # 查找所有的 script 標籤
    scripts = soup.findAll('script')
    for s in scripts:
        # 移除這些 script 標籤
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

這段程式碼定義了兩個函數：`wrap_latex` 和 `wrap_svg`。

1. `wrap_latex` 函數用於處理 LaTeX 格式的數學表達式。如果 `equation` 參數為 `True`，則直接使用 `mathjax.string`；否則，將 `mathjax.string` 用 `$` 符號包裹起來，表示這是一個行內數學表達式。此外，函數還會將字符串中的 `label` 替換為 `tag`。

2. `wrap_svg` 函數用於處理 SVG 圖像。如果 `equation` 參數為 `True`，則將 SVG 圖像包裹在一個居中的 `div` 標籤中；否則，直接返回 SVG 圖像。

這兩個函數通常用於將數學表達式和圖像嵌入到網頁中，並根據需要進行格式化。

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

def main():    
    # 打开包含物理学讲义内容的HTML文件
    file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
    content = file.read()
    
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(content, features="lxml")
    
    # 清理MathJax相关的标签
    clean_mathjax(soup, 'span', 'MathJax')
    clean_mathjax(soup, 'div', 'MathJax_Display')
    clean_mathjax(soup, 'span', 'MathJax_Preview')
    
    # 查找所有内联数学公式的MathJax脚本
    mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    # 将内联数学公式转换为SVG格式
    to_svg(mathjaxs, equation=False)
    
    # 查找所有显示模式的数学公式的MathJax脚本
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    # 将显示模式的数学公式转换为SVG格式
    to_svg(mathjaxs, equation=True)
    
    # 清理HTML中的脚本标签
    clean_script(soup)
    
    # 将处理后的HTML内容写入输出文件
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()

主函数()
```

当我们想转换整本电子书时，可以先以一页作为试验。

```python
    file = open('費曼物理學講義 第一卷 第十三章：功與位能 (A).html')
    content = file.read()
```

這裡便是下載了一個頁面。

`MathJax` 生成了很多的 `div` 和 `span`。意思是比如 `T+U=const`。MathJax 这样来生成。

```html
<span class="MathJax">T</span>
<span class="MathJax">+</span>
<span class="MathJax">U</span>
<span class="MathJax">=</span>
<span class="MathJax">常數</span>
```

这些内容很烦人，也会干扰我们的文本。既然已经有了`svg`，就不再需要这些了。

```python
def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()
```

翻譯成繁體中文：

```python
def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()
```

這段程式碼的功能是從 HTML 文檔中移除所有指定名稱和類別的元素。具體來說，它會找到所有符合條件的元素並將其從文檔樹中刪除。

```python
clean_mathjax(soup, 'span', 'MathJax')
clean_mathjax(soup, 'div', 'MathJax_Display')
clean_mathjax(soup, 'span', 'MathJax_Preview')
```

```traditional_chinese
clean_mathjax(soup, 'span', 'MathJax')
clean_mathjax(soup, 'div', 'MathJax_Display')
clean_mathjax(soup, 'span', 'MathJax_Preview')
```

把它们都去掉。

```python
    mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    to_svg(mathjaxs, equation=False)
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    to_svg(mathjaxs, equation=True)
```

這段代碼的功能是從HTML文檔中提取MathJax格式的數學表達式，並將其轉換為SVG格式的圖像。具體來說：

1. `soup.findAll('script', {'type': 'math/tex'})`：這行代碼使用BeautifulSoup庫查找所有`<script>`標籤，其`type`屬性為`math/tex`，這些標籤通常包含行內數學公式。

2. `to_svg(mathjaxs, equation=False)`：這行代碼將找到的行內數學公式轉換為SVG圖像，`equation=False`表示這些是行內公式。

3. `soup.findAll('script', {'type': 'math/tex; mode=display'})`：這行代碼查找所有`<script>`標籤，其`type`屬性為`math/tex; mode=display`，這些標籤通常包含獨立的數學公式。

4. `to_svg(mathjaxs, equation=True)`：這行代碼將找到的獨立數學公式轉換為SVG圖像，`equation=True`表示這些是獨立公式。

總的來說，這段代碼的目的是將HTML文檔中的MathJax數學表達式轉換為SVG圖像，以便在網頁上顯示。

注意到這裡分成兩種的`script`。

```latex
m\frac{dv}{dt} = F
```

翻譯成繁體中文為：

```latex
m\frac{dv}{dt} = F
```

這表示質量 \( m \) 乘以速度 \( v \) 對時間 \( t \) 的導數等於作用力 \( F \)。這是牛頓第二運動定律的數學表達式。

這是內嵌形式的。

```latex
\begin{equation}
\underset{\text{动能}}{\tfrac{1}{2}mv^2}+
\underset{\text{势能}}{\vphantom{\tfrac{1}{2}}mgh}=\text{常数},\notag
```

這是成段形式的。

当采用内嵌形式时，转换需在表达式两侧添加`$`或`[]`。否则，可能会出现错误。

```latex
\begin{document}
\begin{preview}
\tfrac{1}{2}mv^2
\end{preview}
\end{document}
```

```shell
! 缺少 $ 插入。
<插入的文本>
                $
l.26 \tfrac{1}{2}
                 mv^2
```

應該改成這樣：

```latex
\begin{document}
\begin{preview}
$\tfrac{1}{2}mv^2$
\end{preview}
\end{document}
```

這段 LaTeX 代碼定義了一個文檔，其中包含一個預覽環境，顯示了動能公式 $\tfrac{1}{2}mv^2$。公式表示物體的動能，其中 $m$ 是質量，$v$ 是速度。

接下来看看如何将`latex`转换成`svg`。

```python
    if equation:
        svg_prefix = 'eq_'
    else:
        svg_prefix = 'in_'
```

翻譯成繁體中文：

```python
    if equation:
        svg_prefix = 'eq_'
    else:
        svg_prefix = 'in_'
```

這段代碼的意思是：如果 `equation` 為真（即條件成立），則將 `svg_prefix` 設置為 `'eq_'`；否則，將 `svg_prefix` 設置為 `'in_'`。

```shell
% tree svgs
svgs
├── eq_0.svg
├── eq_1.svg
├── in_0.svg
```

翻譯成繁體中文：

```shell
% tree svgs
svgs
├── eq_0.svg
├── eq_1.svg
├── in_0.svg
```

（注：文件結構和名稱在翻譯後保持不變，因為這些是文件名和目錄結構，通常不需要翻譯。）

這樣來保存`svg`。

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

這段程式碼的功能是將 LaTeX 數學表達式包裝在適當的標記中。如果 `equation` 參數為 `True`，則直接使用 `mathjax.string`；否則，將 `mathjax.string` 包裝在 `$` 符號中。此外，程式碼還會將字串中的 `label` 替換為 `tag`，並返回處理後的字串。

这里来对`latex`源码进行一些调整。注意到`label`变成了`tag`。

![标签](assets/images/feynman/tag.png)

注意右邊的`(Eq:I:13:14)`。如果是`label`的話，則沒解析成功。這會顯示的是`(1)`。這裡將就用`tag`表示一下，暫時沒有深究。

接着就进行调用`latex2svg.py`。

```python
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err    
```

翻譯成繁體中文：

```python
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err    
```

這段程式碼的功能是嘗試將 LaTeX 字串轉換為 SVG 圖像，並將結果存儲在 `out` 變數中。如果轉換過程中發生錯誤（例如，子程序執行失敗），則會捕獲該錯誤並重新拋出。

看看 `latex2svg.py`。

```python
    # 運行 LaTeX 並創建 DVI 文件
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('未找到 latex')
```

這裡是在調用`latex`命令。

```shell
% latex --help
用法：pdftex [選項]... [TEX檔案名[.tex]] [命令]
   或：pdftex [選項]... \首行內容
   或：pdftex [選項]... &格式 參數
  在TEX檔案名上運行pdfTeX，通常生成TEX檔案名.pdf。
```

```python
    try:
        ret = subprocess.run(shlex.split(params['dvisvgm_cmd']+' code.dvi'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory, env=env)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('未找到 dvisvgm')
```

這裡是在調用`dvisvgm`命令。

```shell
% dvisvgm
dvisvgm 2.9.1
```

此程序将TeX/LaTeX生成的DVI文件，以及EPS和PDF文件转换为基于XML的可缩放矢量图形格式SVG。

用法：dvisvgm [選項] DVI檔案
       dvisvgm --eps [選項] EPS檔案
       dvisvgm --pdf [選項] PDF檔案
```

上面提到的`latex`自定义宏应该写在哪里呢？这里需要修改一下`latex2svg.py`文件。具体来说，就是修改`default_preamble`部分。

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

转换成功后，写入到文件中。

```python
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
```

翻譯成繁體中文：

```python
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
```

這段程式碼的功能是打開一個名為 `svgs/{svg_prefix}{i}.svg` 的文件，並將 `out['svg']` 的內容寫入該文件，然後關閉文件。這裡的 `{svg_prefix}` 和 `{i}` 是變數，會根據實際情況被替換成具體的值。

继续。

```python
        node = BeautifulSoup('<img>', features="lxml")
        img = node.find('img')
        img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'
        img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'
```

這裡構造一個`img`標籤。

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

翻譯成繁體中文如下：

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

這段程式碼的功能是根據 `equation` 參數的值來決定如何包裝 SVG 圖像。如果 `equation` 為真，則將 SVG 圖像包裝在一個居中對齊的 `div` 標籤中；否則，直接返回 SVG 圖像。

如果是一段独立的`LaTeX`，那么用`div`包裹起来，并且居中显示。

```python
mathjax.insert_after(p)
``` 

這段程式碼的意思是將 `mathjax` 插入到元素 `p` 的後面。在繁體中文中，可以理解為：

```python
mathjax.insert_after(p)
```

這段程式碼的作用是將 `mathjax` 插入到元素 `p` 的後面。

这里将`div`标签或`img`标签添加到原来的`script`后面。

```python
def clean_script(soup):
    scripts = soup.findAll('script')
    for s in scripts:
        s.decompose()    
        
clean_script(soup)
```

這段程式碼的功能是從一個 BeautifulSoup 物件中移除所有的 `<script>` 標籤。具體來說：

1. `soup.findAll('script')`：找到所有 `<script>` 標籤。
2. `s.decompose()`：將每個找到的 `<script>` 標籤從 DOM 樹中移除。

最後，`clean_script(soup)` 這行代碼執行了這個清理操作。

将所有`latex`替换为`svg`后，就不再需要`script`了。将它们删除，这样会更整洁一些。

最後，再將修改後的整個`html`寫入到一個檔案裡。

```python
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()    
```

翻譯成繁體中文：

```python
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()    
```

這段程式碼的功能是將經過美化的 HTML 內容寫入到名為 `out.html` 的檔案中。

接着使用`pandoc`工具，将其转换为`epub`格式。

```shell
pandoc -s -r html out.html -o feynman.epub
``` 

這行命令的意思是使用 `pandoc` 工具將 `out.html` 文件轉換為 `feynman.epub` 電子書格式。具體參數解釋如下：

- `-s`：生成一個完整的文檔（包括頭部和尾部）。
- `-r html`：指定輸入文件的格式為 HTML。
- `out.html`：輸入的 HTML 文件。
- `-o feynman.epub`：指定輸出的 EPUB 文件名為 `feynman.epub`。

这会打开，就是精美的电子书了。

为什么不直接嵌入`svg`标签，而是用`img`来引入呢？也就是说这样写：

```html
<p></p>
<svg></svg>
<p></p>
```

有个很奇怪的`bug`。当有很多的`svg`文件时，会出现这样的情况。

<img src="/assets/images/feynman/svg_p1.png" alt="svg_p1" style="zoom:40%;" />

后来发现使用`img`标签引入`svg`文件就能解决问题。至于为什么会这样，我还没完全弄明白。当我单独拿出这个`svg`文件并用浏览器查看时，显示是正常的。看来问题可能出在浏览器同时渲染大量`svg`文件时，会出现错误。

### 最后

至于将`epub`格式转换为`mobi`，可以使用`Kindle`的官方工具`Kindle Previewer 3`。需要注意的是，这里仅涉及单章内容的转换。

该项目的代码托管在[feynman-lectures-mobi@lzwjava](https://github.com/lzwjava/feynman-lectures-mobi)。

如何将所有的页面抓取并整理成电子书呢？这个问题我们稍后再谈。不过，单是费曼物理讲义中的这一章，就足够我们细细研读了。好了，现在让我们拿起Kindle，开始阅读吧。