---
audio: false
generated: false
lang: es
layout: post
title: mathjax2mobi：Convertir MathJax HTML a libros electrónicos
translated: true
---

### Descripción del Proyecto

Primero, hablemos brevemente sobre la situación del proyecto.

![feynman_online](assets/images/feynman/feynman_online.jpg)

<img src="/assets/images/feynman/change.JPG" alt="cambio" style="zoom:50%;" />

![latex](assets/images/feynman/latex.JPG)

![epub_negro](assets/images/feynman/epub_black.JPG)

![epub_beautiful](assets/images/feynman/epub_beautiful.JPG)

Después de terminar el proyecto, me sentí un poco feliz. Escribí este pequeño párrafo.

Después de un día entero escribiendo código, ¡finalmente obtuve un hermoso libro electrónico de las Lecciones de Física de Feynman! Las Lecciones de Física de Feynman están disponibles públicamente en la web, renderizadas en `LaTeX`. La gente suele usar `LaTeX` para escribir artículos académicos, ya que es excelente para renderizar fórmulas matemáticas. Al estar disponibles en la web, se utiliza la biblioteca `MathJax`. Esta convierte el código fuente de `LaTeX` en código `HTML`, generando muchos elementos `div` y `span`. Sin embargo, los libros electrónicos no soportan este método. Entonces, la idea fue extraer las páginas web, revertir el renderizado de `MathJax` y luego reemplazarlo con imágenes `SVG`. Surgieron varios problemas: primero, el código fuente tiene muchas macros personalizadas de `LaTeX` que necesitaban ser añadidas; segundo, incrustar muchos `SVG` causaba problemas. Si era un solo `SVG`, no había problema, pero con muchos, surgían errores. Probablemente se trataba de algún extraño bug entre el navegador y los `SVG`. La solución fue guardar los `SVG` como archivos e incluirlos mediante la etiqueta `img`. Además, las fórmulas se dividen en dos tipos: las que están dentro del texto y las que están en una línea separada. ¡Así que, al final, obtuve un hermoso libro electrónico!

### Información consultada

Aquí se documentan los recursos consultados durante la resolución del proyecto. Dado que se trata de un tutorial, se muestra a los estudiantes una idea general de cómo es la experiencia de llevar a cabo un proyecto.

![](assets/images/feynman/s1.PNG)

![](assets/images/feynman/s2.PNG)

![](assets/images/feynman/s3.PNG)

![](assets/images/feynman/s4.PNG)

![](assets/images/feynman/s5.PNG)

![](assets/images/feynman/s6.PNG)

![](assets/images/feynman/s7.PNG)

![](assets/images/feynman/s8.PNG)

### Iniciar el proyecto

Las conferencias de física de Feynman ya están disponibles para leer en línea. Me gustaría leerlas en mi `Kindle`. Sin embargo, dado que contienen muchas fórmulas matemáticas, el manuscrito original probablemente fue creado usando `LaTeX`. Utilizan la biblioteca `MathJax` para mostrar el contenido en formato `LaTeX` en la página web.

Por ejemplo.

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

Arriba se muestra un fragmento de código `html`. En este bloque de código `html`, debajo de la etiqueta `script`, se encuentra el texto original en `LaTeX`. `MathJax` lo convierte en múltiples etiquetas `span` para mostrarlo.

Ahora tenemos una idea. Consiste en cambiar el método de visualización de `mathjax` a imágenes `svg`.

Encontré un proyecto en GitHub llamado `tuxu/latex2svg`.

```python
from latex2svg import latex2svg
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

Intenta ejecutarlo, pero ocurrió un error.

```shell
    raise RuntimeError('latex no encontrado')
RuntimeError: latex no encontrado
```

Mira el código.

```python
    # Ejecutar LaTeX y crear archivo DVI
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('latex no encontrado')
```

Esto también depende del comando `latex`.

Instálalo.

```shell
brew install --cask mactex
==> Advertencias
Debes reiniciar la ventana de tu terminal para que la instalación de las herramientas CLI de MacTex surta efecto.
Alternativamente, los usuarios de Bash y Zsh pueden ejecutar el comando:
  eval "$(/usr/libexec/path_helper)"
==> Descargando http://mirror.ctan.org/systems/mac/mactex/mactex-20200407.pkg
==> Descargando desde https://mirrors.aliyun.com/CTAN/systems/mac/mactex/mactex-20200407.pkg
######################################################################## 100.0%
Todas las dependencias de la fórmula están satisfechas.
==> Instalando Cask mactex
==> Ejecutando el instalador para mactex; es posible que se necesite tu contraseña.
installer: El nombre del paquete es MacTeX
installer: Se aplicaron cambios en el archivo de opciones '/private/tmp/choices20210315-4643-5884ro.xml'
installer: Instalando en la ruta base /
installer: La instalación fue exitosa.
🍺  ¡mactex se instaló correctamente!
```

Instalación exitosa.

```shell
% latex
This is pdfTeX, Version 3.14159265-2.6-1.40.21 (TeX Live 2020) (preloaded format=latex)
 restricted \write18 enabled.
**
```

```python
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

En este código, se utiliza la función `latex2svg` para convertir una expresión matemática en LaTeX a un formato SVG. Luego, se imprimen dos valores: la profundidad (`depth`) y el código SVG (`svg`) generado. No se realizan cambios en el código, ya que los nombres de las funciones y variables deben permanecer en inglés.

```python
svg = open('1.svg', 'w')
svg.write(out['svg'])
svg.close()
```

Se puede generar `svg`.

Así que intenta generar todos los textos `latex` obtenidos en `mathjax`.

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

Lamentablemente, ocurrió un error.

```python
    raise CalledProcessError(self.returncode, self.args, self.stdout,
subprocess.CalledProcessError: El comando '['latex', '-interaction', 'nonstopmode', '-halt-on-error', 'code.tex']' devolvió un estado de salida no cero: 1.
```

¿Cuál fórmula específica está incorrecta?

```latex
\tfrac{1}{2}mv^2
```

## LaTeX

LaTeX es un sistema de composición tipográfica de alta calidad, ampliamente utilizado para la producción de documentos técnicos y científicos. A diferencia de los procesadores de texto tradicionales, LaTeX se basa en un enfoque de marcado, donde el contenido se escribe en texto plano con comandos que indican la estructura y el formato del documento.

### Características principales de LaTeX

1. **Calidad tipográfica**: LaTeX produce documentos con un aspecto profesional, especialmente en lo que respecta a la disposición de fórmulas matemáticas.
2. **Separación de contenido y formato**: El autor se concentra en el contenido, mientras que LaTeX se encarga del diseño y la maquetación.
3. **Amplia comunidad y recursos**: Existen numerosos paquetes y plantillas que extienden las capacidades de LaTeX.
4. **Compatibilidad multiplataforma**: Los documentos de LaTeX pueden ser compilados en diferentes sistemas operativos.

### Ejemplo básico de un documento en LaTeX

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{Ejemplo de documento en LaTeX}
\author{Autor}
\date{\today}

\begin{document}

\maketitle

\section{Introducción}
Este es un ejemplo básico de un documento en LaTeX. Aquí puedes escribir el contenido de tu documento.

\section{Matemáticas}
LaTeX es especialmente conocido por su capacidad para manejar ecuaciones matemáticas. Por ejemplo, la ecuación de la relatividad de Einstein:

\[ E = mc^2 \]

\end{document}
```

### Compilación del documento

Para compilar un documento de LaTeX, generalmente se utiliza un editor como **TeXShop**, **TeXworks**, o un entorno de desarrollo integrado (IDE) como **Overleaf**. El proceso de compilación convierte el archivo `.tex` en un archivo PDF listo para su visualización o impresión.

### Conclusión

LaTeX es una herramienta poderosa para la creación de documentos técnicos y científicos. Aunque tiene una curva de aprendizaje inicial, su capacidad para producir documentos de alta calidad y su flexibilidad lo convierten en una opción preferida para muchos profesionales y académicos.

Si estás interesado en aprender más sobre LaTeX, te recomiendo explorar recursos en línea como [Overleaf](https://www.overleaf.com/) o [LaTeX Project](https://www.latex-project.org/).

Vamos a aprender un poco sobre `latex`.

```latex
\documentclass[12pt]{article}
\usepackage{lingmacros}
\usepackage{tree-dvips}
\begin{document}
```

\section*{Notas para mi artículo}

No olvides incluir ejemplos de topicalización.
Se ven así:

{\small
\enumsentence{Topicalización del sujeto oracional:\\ 
\shortex{7}{a John$_i$ [a & kltukl & [el & 
  {\bf l-}oltoir & er & ngii$_i$ & a Mary]]}
{ & {\bf R-}claro & {\sc comp} & 
  {\bf IR}.{\sc 3s}-amar   & P & él & }
{John, (es) claro que Mary lo ama.}}
}

\subsection*{Cómo manejar la topicalización}

Asumiré una estructura de árbol como (\ex{1}).

{\small
\enumsentence{Estructura de las Proyecciones de A$'$:\\ [2ex]
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

\subsection*{Estado de ánimo}

El modo cambia cuando hay un tema, así como cuando
hay movimiento WH. \emph{Irrealis} es el modo cuando
hay un tema no sujeto o una frase WH en Comp.
\emph{Realis} es el modo cuando hay un tema sujeto
o una frase WH.

```latex
\end{document}
```

Encontré un ejemplo de código fuente en `LaTeX` en línea.

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

Vamos a mirar el código fuente y el resultado renderizado para ver qué podemos aprender.

```latex
\begin{document}
\end{document}
```

Así es como se envuelve el documento.

```latex
\section*{Notas para mi artículo}
```

Esto indica el comienzo de un título de `section`.

```latex
\subsection*{Cómo manejar la topicalización}
```

Esto representa un subtítulo.

```latex
\shortex{7}{a John$_i$ [a & kltukl & [el & 
  {\bf l-}oltoir & er & ngii$_i$ & a Mary]]}
```

![shortex](assets/images/feynman/shortex.png)

Se puede usar `$_i$` para representar subíndices. `{\bf l-}` para representar texto en negrita.

```latex
\enumsentence{Estructura de las Proyecciones de A$'$:\\ [2ex]
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

<img src="/assets/images/feynman/node.png" alt="nodo" style="zoom:50%;" />

Observa que `nodeconnect` se utiliza para representar las conexiones.

### Convertir LaTeX a SVG

Si necesitas convertir ecuaciones o fórmulas escritas en LaTeX a imágenes en formato SVG (Scalable Vector Graphics), hay varias herramientas y métodos que puedes utilizar. A continuación, te presento algunas opciones:

#### 1. **Usando `MathJax` y `dvisvgm`**
   - **MathJax** es una biblioteca JavaScript que permite renderizar ecuaciones LaTeX en la web.
   - **dvisvgm** es una herramienta de línea de comandos que convierte archivos DVI (generados por LaTeX) a SVG.

   **Pasos:**
   1. Escribe tu ecuación en un archivo `.tex`.
   2. Compila el archivo `.tex` a DVI usando `latex`.
   3. Convierte el archivo DVI a SVG usando `dvisvgm`.

   **Ejemplo:**
   ```bash
   latex equation.tex
   dvisvgm equation.dvi
   ```

#### 2. **Usando `Pandoc`**
   - **Pandoc** es una herramienta de conversión de documentos que puede convertir archivos LaTeX a HTML con SVG incrustado.

   **Pasos:**
   1. Escribe tu ecuación en un archivo `.tex`.
   2. Usa Pandoc para convertir el archivo `.tex` a HTML.

   **Ejemplo:**
   ```bash
   pandoc -s equation.tex -o equation.html
   ```

#### 3. **Usando `LaTeX` y `pdf2svg`**
   - **pdf2svg** es una herramienta que convierte archivos PDF a SVG.

   **Pasos:**
   1. Escribe tu ecuación en un archivo `.tex`.
   2. Compila el archivo `.tex` a PDF usando `pdflatex`.
   3. Convierte el archivo PDF a SVG usando `pdf2svg`.

   **Ejemplo:**
   ```bash
   pdflatex equation.tex
   pdf2svg equation.pdf equation.svg
   ```

#### 4. **Usando `Overleaf`**
   - **Overleaf** es un editor de LaTeX en línea que permite exportar documentos a varios formatos, incluyendo SVG.

   **Pasos:**
   1. Escribe tu ecuación en Overleaf.
   2. Compila el documento.
   3. Exporta el documento como SVG.

#### 5. **Usando `Inkscape`**
   - **Inkscape** es un editor de gráficos vectoriales que puede importar archivos PDF generados por LaTeX y exportarlos como SVG.

   **Pasos:**
   1. Escribe tu ecuación en un archivo `.tex`.
   2. Compila el archivo `.tex` a PDF usando `pdflatex`.
   3. Abre el archivo PDF en Inkscape.
   4. Exporta el archivo como SVG.

#### 6. **Usando `MathJax` en línea**
   - Si necesitas una solución rápida y no quieres instalar software, puedes usar herramientas en línea como [MathJax](https://www.mathjax.org/) o [QuickLaTeX](https://www.quicklatex.com/) para renderizar ecuaciones LaTeX directamente en SVG.

   **Pasos:**
   1. Escribe tu ecuación en LaTeX en la herramienta en línea.
   2. Descarga la imagen SVG generada.

### Conclusión
Convertir ecuaciones LaTeX a SVG es un proceso sencillo con las herramientas adecuadas. Dependiendo de tus necesidades y preferencias, puedes elegir entre soluciones locales o en línea. ¡Espero que esta guía te haya sido útil!

Continuar con el proyecto.

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

Esto se puede renderizar correctamente. En el código, es posible que no se renderice porque no se ha añadido `\usepackage{amsmath}`.

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

\begin{document}
\begin{preview}
\tfrac{1}{2}mv^2
\end{preview}
\end{document}
```

```shell
! Falta un $ insertado.
<texto insertado>
                $
l.12 \tfrac{1}{2}
                 mv^2
```

Así es como salió mal. Y al cambiarlo de esta manera, funciona.

```latex
\[\tfrac{1}{2}mv^2\]
```

El código LaTeX anterior representa la fórmula de la energía cinética, que se traduce al español como:

```latex
\[\tfrac{1}{2}mv^2\]
```

Esta fórmula sigue siendo la misma en español, ya que es una expresión matemática universal.

Realizar diversas pruebas y exploraciones.

```python
from bs4 import BeautifulSoup
from latex2svg import latex2svg
```

```python
file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
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

```python
# print(len(soup.contents))
    
output_file = open('out.html', 'w')
output_file.write(soup.prettify())
output_file.close()
# print(soup.contents)
```

Traducción al español:

```python
# print(len(soup.contents))
    
output_file = open('out.html', 'w')
output_file.write(soup.prettify())
output_file.close()
# print(soup.contents)
```

Nota: El código no necesita traducción, ya que es un bloque de código en Python. Las instrucciones y los nombres de las funciones y variables deben permanecer en inglés para mantener la funcionalidad del código.

```python
# out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
# print(out['depth'])
# print(out['svg'])
```

Traducción al español:

```python
# out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
# print(out['depth'])
# print(out['svg'])
```

En este código, se utiliza la función `latex2svg` para convertir una expresión LaTeX en un gráfico SVG. Luego, se imprime la profundidad (`depth`) y el código SVG (`svg`) del resultado. El código LaTeX utilizado es \( e^{i \pi} + 1 = 0 \), que es la famosa identidad de Euler.

```python
# svg = open('1.svg', 'w')
# svg.write(out['svg'])
# svg.close()
```

```

¿Qué estoy explorando en todo esto?

```python
    if 'FLP' in mathjax.string:
        continue
    elif 'Fig' in mathjax.string:
        continue
    elif 'eps' in mathjax.string:
        continue
```

Aquí, cuando se analiza el código fuente de `latex` y se encuentran `FLP`, `Fig`, `eps`, el proceso de conversión falla.

Por ejemplo, en `HTML`, hay un script como este:

```html
<script type="math/tex" id="MathJax-Element-11">\FLPF\cdot\FLPv</script>
```

Análisis obtenido:

```latex
\FLPF\cdot\FLPv
```

*Nota: La expresión en LaTeX no se traduce, ya que es un código matemático que debe permanecer en su forma original para mantener su significado y funcionalidad.*

Cuando ocurre un error al convertir en el código, es decir, cuando `latex2svg.py` falla, aquí se utiliza el programa `latex` para realizar la conversión.

`code.tex`:

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
! Secuencia de control no definida.
l.13     \FLPF
              \cdot\FLPv
?
```

¿Cuál es exactamente el problema? Más tarde me di cuenta de este fragmento de código en el `html`.

```html
<script type="text/x-mathjax-config;executed=true">
      MathJax.Hub.Config({
        TeX: {
          Macros: {
            FLPvec: ["\\boldsymbol{#1}", 1], Figvec: ["\\mathbf{#1}", 1], FLPC: ["\\FLPvec{C}", 0], FLPF: ["\\FLPvec{F}", 0], FLPa: ["\\FLPvec{a}", 0], FLPb: ["\\FLPvec{b}", 0], FLPr: ["\\FLPvec{r}", 0], FLPs: ["\\FLPvec{s}", 0], FLPv: ["\\FLPvec{v}", 0], ddt: ["\\frac{d#1}{d#2}", 2], epsO: ["\\epsilon_0", 0], FigC: ["\\Figvec{C}", 0]
          }
        }
      });
</script>
```

Esto indica que al renderizar la página, se han configurado macros para `MathJax`. Por lo tanto, también deberíamos agregarlas en nuestro código fuente de conversión de `latex`. Vamos a añadirlas.

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

Así es como debe ser.

![fv1](assets/images/feynman/fv1.png)

### Análisis del Código

Echemos un vistazo al código final.

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

Este código define una función `to_svg` que convierte expresiones LaTeX en imágenes SVG y las inserta en un documento. Aquí está la traducción al español del código:

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

Este código define una función `to_svg` que convierte expresiones LaTeX en imágenes SVG y las inserta en un documento. La función toma una lista de expresiones LaTeX (`mathjaxs`) y un indicador booleano (`equation`) que determina si la expresión es una ecuación o no. Luego, genera archivos SVG y los inserta en el documento como imágenes.

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

main()
```

Cuando queremos convertir un libro electrónico completo, podemos probar primero con una página.

```python
    file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
    content = file.read()
```

Aquí se ha descargado una página.

`MathJax` genera muchos `div` y `span`. Por ejemplo, `T+U=const` se genera de la siguiente manera por MathJax.

```html
<span class="MathJax">T</span>
<span class="MathJax">+</span>
<span class="MathJax">U</span>
<span class="MathJax">=</span>
<span class="MathJax">const</span>
```

Estos son bastante molestos y también pueden afectar nuestro texto. Como ya tenemos `svg`, no necesitamos estos.

```python
def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()
```

    clean_mathjax(soup, 'span', 'MathJax')
    clean_mathjax(soup, 'div', 'MathJax_Display')
    clean_mathjax(soup, 'span', 'MathJax_Preview')
```

Elimínalos todos.

```python
    mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    to_svg(mathjaxs, equation=False)
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    to_svg(mathjaxs, equation=True)
```

Observa que aquí se dividen en dos tipos de `script`.

```latex
m(dv/dt)=F
```

*Nota: La ecuación es una expresión matemática y no requiere traducción, ya que es universal en el ámbito de la física.*

Esto es en formato incrustado.

```latex
\begin{equation}
\underset{\text{E.C.}}{\tfrac{1}{2}mv^2}+
\underset{\text{E.P.}}{\vphantom{\tfrac{1}{2}}mgh}=\text{const},\notag
```

Esto está en forma de párrafo.

Cuando se utiliza la forma incrustada, la conversión debe incluir `$` o `[]` alrededor de la expresión. De lo contrario, podría ocurrir un error.

```latex
\begin{document}
\begin{preview}
\tfrac{1}{2}mv^2
\end{preview}
\end{document}
```

```shell
! Falta $ insertado.
<texto insertado>
                $
l.26 \tfrac{1}{2}
                 mv^2
```

Debe cambiarse a esto:

```latex
\begin{document}
\begin{preview}
$\tfrac{1}{2}mv^2$
\end{preview}
\end{document}
```

A continuación, veamos cómo convertir `latex` a `svg`.

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

Así es como se guarda un `svg`.

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

Aquí vamos a hacer algunos ajustes al código fuente de `latex`. Nota que `label` se ha cambiado a `tag`.

![etiqueta](assets/images/feynman/tag.png)

Observa el `(Eq:I:13:14)` a la derecha. Si se trata de una `label`, no se ha analizado correctamente. Esto mostrará `(1)`. Aquí se utiliza `tag` para representarlo temporalmente, sin profundizar más por ahora.

Luego se procede a llamar a `latex2svg.py`.

```python
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err    
```

El código anterior no necesita traducción, ya que es un bloque de código en Python y los nombres de las funciones y excepciones deben permanecer en inglés. Sin embargo, si necesitas una explicación en español, aquí está:

```python
        out = {}  # Inicializa un diccionario vacío
        try:
            out = latex2svg(wrap)  # Intenta convertir LaTeX a SVG
        except subprocess.CalledProcessError as err:
            raise err  # Si hay un error, lo lanza
```

Mira `latex2svg.py`.

```python
    # Ejecutar LaTeX y crear archivo DVI
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('latex no encontrado')
```

Aquí se está llamando al comando `latex`.

```shell
 % latex --help
Uso: pdftex [OPCIÓN]... [NOMBRE_TEX[.tex]] [COMANDOS]
   o: pdftex [OPCIÓN]... \PRIMERA_LÍNEA
   o: pdftex [OPCIÓN]... &FMT ARGS
  Ejecuta pdfTeX en NOMBRE_TEX, generalmente creando NOMBRE_TEX.pdf.
```

```python
    try:
        ret = subprocess.run(shlex.split(params['dvisvgm_cmd']+' code.dvi'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory, env=env)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('dvisvgm no encontrado')
```

Aquí se está llamando al comando `dvisvgm`.

```shell
% dvisvgm
dvisvgm 2.9.1
```

Este programa convierte archivos DVI, creados por TeX/LaTeX, así como archivos EPS y PDF, al formato de gráficos vectoriales escalables basado en XML, SVG.

Uso: dvisvgm [opciones] archivo_dvi
       dvisvgm --eps [opciones] archivo_eps
       dvisvgm --pdf [opciones] archivo_pdf
```

¿Dónde se escriben las macros personalizadas de `latex` mencionadas anteriormente? Aquí hay que modificar el archivo `latex2svg.py`. Cambia el `default_preamble`.

```python
default_preamble = r"""
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
"""
```

Después de la conversión exitosa, se escribe en el archivo.

```python
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
```

Continúa.

```python
        node = BeautifulSoup('<img>', features="lxml")
        img = node.find('img')
        img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'
        img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'
```

Aquí se construye una etiqueta `img`.

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

Si es un `latex` de un solo párrafo, entonces envuélvelo en un `div` y centra el contenido.

```python
mathjax.insert_after(p)
```

Aquí se añaden las etiquetas `div` o `img` después del `script` original.

```python
def limpiar_script(soup):
    scripts = soup.findAll('script')
    for s in scripts:
        s.decompose()    
        
limpiar_script(soup)
```

Después de reemplazar todos los `latex` con `svg`, ya no necesitas el `script`. Elimínalos para que todo quede más limpio.

Finalmente, escribe el `html` modificado en un archivo.

```python
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()    
```

Luego, utiliza la herramienta `pandoc` para convertirlo a `epub`.

```shell
pandoc -s -r html out.html -o feynman.epub
```

Esto abrirá un hermoso libro electrónico.

¿Por qué no incrustar directamente la etiqueta `svg` y usar `img` para importarla? Es decir, escribir así:

```html
<p></p>
<svg></svg>
<p></p>
```

Hay un `bug` muy extraño. Cuando hay muchos archivos `svg`, ocurre algo como esto.

<img src="/assets/images/feynman/svg_p1.png" alt="svg_p1" style="zoom:40%;" />

Luego descubrí que podía usar `img` para incluirlo. No estoy seguro de por qué funciona de esta manera. Cuando saqué este único `svg` y lo abrí en el navegador, no hubo problemas. Parece que el error ocurre cuando el navegador intenta renderizar muchos `svg` a la vez.

### Finalmente

En cuanto a cómo convertir `epub` a `mobi`, puedes usar la herramienta oficial de `Kindle`, `Kindle Previewer 3`. Ten en cuenta que esto es solo un capítulo.

El código del proyecto se encuentra en [feynman-lectures-mobi@lzwjava](https://github.com/lzwjava/feynman-lectures-mobi).

¿Cómo capturar y organizar todas las páginas en un libro electrónico? Lo explicaré más adelante. Pero este capítulo de las Lecciones de Física de Feynman ya es suficiente para leer. Bien, tomemos nuestro Kindle y comencemos a leer.