---
audio: false
generated: false
image: true
lang: fr
layout: post
title: 'mathjax2mobi : Convertir des fichiers HTML avec MathJax en livres électroniques'
translated: true
---

### Présentation du projet

Commençons par un aperçu général du projet.

![feynman_online](assets/images/feynman/feynman_online.jpg)

<img src="/assets/images/feynman/change.JPG" alt="changement" style="zoom:50%;" />

![latex](assets/images/feynman/latex.JPG)

![epub_black](assets/images/feynman/epub_black.JPG)

![epub_beautiful](assets/images/feynman/epub_beautiful.JPG)

Après avoir terminé le projet, je me sens un peu heureux. J'ai écrit ce passage.

Après une journée entière à coder, j'ai enfin obtenu un magnifique livre électronique des "Feynman Lectures on Physics" ! Les "Feynman Lectures on Physics" sont disponibles en ligne, rendues en `latex`. Les gens utilisent souvent `latex` pour écrire des articles, car il est excellent pour le rendu des formules mathématiques. Disponibles en ligne, elles utilisent la bibliothèque `mathjax`. Cela transforme le code source `latex` en code `html`, générant de nombreuses balises `div` et `span`. Cependant, les livres électroniques ne supportent pas cette méthode. L'idée était donc de scraper les pages web, de faire un rendu inverse de `mathjax`, puis de remplacer par des images `svg`. Plusieurs problèmes sont apparus : d'abord, le code source contient de nombreuses macros `latex` personnalisées qui doivent être ajoutées ; ensuite, l'intégration de nombreux `svg` pose des problèmes. Si un seul `svg` ne pose pas de problème, en revanche, plusieurs peuvent causer des soucis. C'est probablement un bug bizarre entre le navigateur et `svg`. La solution était donc de sauvegarder les `svg` en fichiers et de les inclure via des balises `img`. Les formules se divisent en deux types : celles qui sont au milieu du texte et celles qui sont sur une ligne à part. Ainsi, au final, j'ai obtenu un magnifique livre électronique !

### Documentation consultée

Voici les ressources consultées pour résoudre les problèmes rencontrés lors du projet. Comme il s'agit d'un tutoriel, cela permet aux étudiants de voir à quoi ressemble l'expérience de réalisation d'un projet.

![](assets/images/feynman/s1.PNG)

![](assets/images/feynman/s2.PNG)

![](assets/images/feynman/s3.PNG)

![](assets/images/feynman/s4.PNG)

![](assets/images/feynman/s5.PNG)

![](assets/images/feynman/s6.PNG)

![](assets/images/feynman/s7.PNG)

![](assets/images/feynman/s8.PNG)

### Démarrer le projet

Les cours de physique de Feynman sont désormais disponibles en ligne pour une lecture publique. Je souhaite les lire sur mon `Kindle`. Cependant, comme ils contiennent de nombreuses formules mathématiques, leur version originale a probablement été réalisée avec `LaTeX`. Ils utilisent la bibliothèque `MathJax` pour afficher le contenu au format `LaTeX` sur les pages web.

Voici un exemple.

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

Voici un extrait de code `html`. Dans ce bloc de code `html`, le texte brut `latex` se trouve sous la balise `script`. `mathjax` le transforme en de nombreuses balises `span` pour l'affichage.

Nous avons maintenant une idée. Il s'agit de modifier la méthode d'affichage de `mathjax` pour utiliser des images `svg`.

J'ai trouvé un projet sur GitHub appelé `tuxu/latex2svg`.

```python
from latex2svg import latex2svg
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

Essayez de l'exécuter, mais une erreur s'est produite.

```shell
    raise RuntimeError('latex non trouvé')
RuntimeError: latex non trouvé
```

Regardons le code.

```python
    # Exécuter LaTeX et créer un fichier DVI
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('latex non trouvé')
```

Cela dépend également de la commande `latex`.

Installez-le.

```shell
brew install --cask mactex
==> Caveats
Vous devez redémarrer votre fenêtre de terminal pour que l'installation des outils CLI de MacTex prenne effet.
Alternativement, les utilisateurs de Bash et Zsh peuvent exécuter la commande :
  eval "$(/usr/libexec/path_helper)"
==> Téléchargement de http://mirror.ctan.org/systems/mac/mactex/mactex-20200407.pkg
==> Téléchargement depuis https://mirrors.aliyun.com/CTAN/systems/mac/mactex/mactex-20200407.pkg
######################################################################## 100.0%
Toutes les dépendances des formules sont satisfaites.
==> Installation du Cask mactex
==> Exécution de l'installateur pour mactex ; votre mot de passe peut être nécessaire.
installer: Le nom du package est MacTeX
installer: fichier de modifications des choix '/private/tmp/choices20210315-4643-5884ro.xml' appliqué
installer: Installation au chemin de base /
installer: L'installation a réussi.
🍺  mactex a été installé avec succès !
```

Installation réussie.

```shell
% latex
Ceci est pdfTeX, Version 3.14159265-2.6-1.40.21 (TeX Live 2020) (format préchargé=latex)
 \write18 restreint activé.
**
```

```python
out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
print(out['depth'])
print(out['svg'])
```

```python
svg = open('1.svg', 'w')
svg.write(out['svg'])
svg.close()
```

Il est maintenant possible de générer des `svg`.

Alors, essayons de générer tous les textes `latex` obtenus dans `mathjax`.

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

Malheureusement, une erreur s'est produite.

```python
    raise CalledProcessError(self.returncode, self.args, self.stdout,
subprocess.CalledProcessError: La commande '['latex', '-interaction', 'nonstopmode', '-halt-on-error', 'code.tex']' a retourné un statut de sortie non nul : 1.
```

Quelle formule exactement est incorrecte ?

```latex
\tfrac{1}{2}mv^2
```

## LaTeX

LaTeX est un système de composition de documents largement utilisé dans les domaines académiques et scientifiques. Il permet de créer des documents de haute qualité avec une mise en page précise, en particulier pour les formules mathématiques complexes. Voici un exemple simple de code LaTeX pour créer un document de base :

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{Exemple de document LaTeX}
\author{Auteur}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}
Ceci est un exemple de document LaTeX. Il montre comment structurer un document avec des sections, des sous-sections et des formules mathématiques.

\subsection{Formules mathématiques}
La formule de l'équation quadratique est donnée par :
\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

\end{document}
```

Ce code produit un document avec un titre, une introduction, et une formule mathématique. LaTeX est particulièrement utile pour les documents contenant des équations, des tableaux et des références croisées.

Apprenons un peu de `latex`.

```latex
\documentclass[12pt]{article}
\usepackage{lingmacros}
\usepackage{tree-dvips}
\begin{document}
```

\section*{Notes pour mon article}

N'oubliez pas d'inclure des exemples de topicalisation.
Ils ressemblent à ceci :

{\small
\enumsentence{Topicalisation à partir du sujet de la phrase :\\ 
\shortex{7}{a John$_i$ [a & kltukl & [el & 
  {\bf l-}oltoir & er & ngii$_i$ & a Mary]]}
{ & {\bf R-}clair & {\sc comp} & 
  {\bf IR}.{\sc 3s}-aimer   & P & lui & }
{John, (c'est) clair que Mary l'aime.}}
}

\subsection*{Comment gérer la topicalisation}

Je vais simplement supposer une structure arborescente comme (\ex{1}).

{\small
\enumsentence{Structure des Projections de A$'$:\\ [2ex]
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

\subsection*{Humeur}

Le mode change lorsqu'il y a un thème, ainsi que lorsqu'il y a un mouvement WH. \emph{Irrealis} est le mode lorsqu'il y a un thème non sujet ou une phrase WH dans Comp. \emph{Realis} est le mode lorsqu'il y a un thème sujet ou une phrase WH.

```latex
\end{document}
```

J'ai trouvé un exemple de code source `latex` sur Internet.

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

Examinons le code source et le rendu final pour voir ce que nous pouvons apprendre.

```latex
\begin{document}
\end{document}
```

Voici comment envelopper le document.

```latex
\section*{Notes pour mon article}
```

Cela indique le début du titre de la `section`.

```latex
\subsection*{Comment gérer la topicalisation}
```

Cela indique un sous-titre.

```latex
\shortex{7}{a John$_i$ [a & kltukl & [el & 
  {\bf l-}oltoir & er & ngii$_i$ & a Mary]]}
```

![shortex](assets/images/feynman/shortex.png)

On peut voir `$_i$` pour représenter l'indice. `{\bf l-}` pour représenter le texte en gras.

```latex
\enumsentence{Structure of A$'$ Projections:\\ [2ex]
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

Notez que `nodeconnect` est utilisé pour représenter les connexions.

### Conversion de LaTeX en SVG

La conversion de LaTeX en SVG (Scalable Vector Graphics) est une tâche courante pour ceux qui souhaitent intégrer des formules mathématiques ou des diagrammes complexes dans des pages web ou des présentations. SVG est un format vectoriel qui permet de redimensionner les images sans perte de qualité, ce qui le rend idéal pour les formules mathématiques.

Voici quelques méthodes pour convertir du LaTeX en SVG :

#### 1. Utilisation de `dvisvgm`
`dvisvgm` est un outil en ligne de commande qui convertit les fichiers DVI (Device Independent) générés par LaTeX en fichiers SVG.

1. Compilez votre fichier LaTeX en DVI :
   ```bash
   latex fichier.tex
   ```
2. Convertissez le fichier DVI en SVG :
   ```bash
   dvisvgm fichier.dvi
   ```

#### 2. Utilisation de `MathJax`
`MathJax` est une bibliothèque JavaScript qui permet de rendre des formules mathématiques en LaTeX directement dans le navigateur. Vous pouvez également utiliser `MathJax` pour générer des fichiers SVG.

1. Incluez `MathJax` dans votre page HTML :
   ```html
   <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
   <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
   ```
2. Utilisez `MathJax` pour convertir une formule LaTeX en SVG :
   ```html
   <div id="math"></div>
   <script>
     MathJax.tex2svgPromise('\\frac{a}{b}').then(function(svg) {
       document.getElementById('math').appendChild(svg);
     });
   </script>
   ```

#### 3. Utilisation de `LaTeX.js`
`LaTeX.js` est une bibliothèque JavaScript qui permet de compiler du LaTeX en HTML ou SVG directement dans le navigateur.

1. Incluez `LaTeX.js` dans votre page HTML :
   ```html
   <script src="https://cdn.jsdelivr.net/npm/latex.js/dist/latex.min.js"></script>
   ```
2. Utilisez `LaTeX.js` pour convertir une formule LaTeX en SVG :
   ```html
   <div id="math"></div>
   <script>
     const latex = new LaTeX();
     const svg = latex.toSVG('\\frac{a}{b}');
     document.getElementById('math').innerHTML = svg;
   </script>
   ```

#### 4. Utilisation de `Overleaf`
`Overleaf` est un éditeur LaTeX en ligne qui permet de compiler des documents LaTeX et de les exporter en différents formats, y compris SVG.

1. Créez un document LaTeX sur `Overleaf`.
2. Compilez le document.
3. Téléchargez le fichier PDF généré.
4. Utilisez un outil comme `pdf2svg` pour convertir le PDF en SVG.

#### Conclusion
La conversion de LaTeX en SVG peut être réalisée de plusieurs manières, en fonction de vos besoins et de votre environnement de travail. Que vous utilisiez des outils en ligne de commande comme `dvisvgm`, des bibliothèques JavaScript comme `MathJax` ou `LaTeX.js`, ou des services en ligne comme `Overleaf`, vous avez plusieurs options pour intégrer des formules mathématiques en LaTeX dans vos projets web.

Continuer le projet.

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

Cela peut être correctement rendu. Dans le code, il est possible que cela ne soit pas rendu correctement, peut-être parce que `\usepackage{amsmath}` n'a pas été ajouté.

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
! Missing $ inserted.
<inserted text>
                $
l.12 \tfrac{1}{2}
                 mv^2
```

*Note : Le message d'erreur est en anglais, il est donc laissé tel quel. La traduction en français serait :*

```shell
! $ manquant inséré.
<texte inséré>
                $
l.12 \tfrac{1}{2}
                 mv^2
```

Cela a causé une erreur. En revanche, en modifiant comme suit, cela fonctionne.

```latex
\[\tfrac{1}{2}mv^2\]
```

Effectuer diverses tentatives d'exploration.

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

```python
# out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
# print(out['depth'])
# print(out['svg'])
```

Traduction en français :

```python
# out = latex2svg(r'\( e^{i \pi} + 1 = 0 \)')
# print(out['depth'])
# print(out['svg'])
```

Le code reste en anglais car il s'agit d'un exemple de code Python. Les commentaires et les noms de variables ne sont pas traduits.

```python
# svg = open('1.svg', 'w')
# svg.write(out['svg'])
# svg.close()
```

```

En quoi est-ce que je suis en train de tâtonner ?

```python
    if 'FLP' in mathjax.string:
        continue
    elif 'Fig' in mathjax.string:
        continue
    elif 'eps' in mathjax.string:
        continue
```

Lors de l'analyse du code source `latex`, une erreur s'est produite lors du processus de conversion lorsqu'il a rencontré `FLP`, `Fig` ou `eps`.

Par exemple, dans le `HTML`, on peut trouver un script comme celui-ci :

```html
<script type="math/tex" id="MathJax-Element-11">\FLPF\cdot\FLPv</script>
```

Analyse des résultats obtenus :

```latex
\FLPF\cdot\FLPv
```

*Note : Le code LaTeX ci-dessus n'a pas été traduit car il s'agit d'une notation mathématique standard. La traduction de formules mathématiques n'est généralement pas nécessaire, car elles sont universellement comprises dans leur forme originale.*

Lors de la conversion dans le code, une erreur s'est produite. Plus précisément, `latex2svg.py` a échoué. Ici, nous utilisons le programme `latex` pour effectuer la conversion.

`code.tex` :

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
! Séquence de contrôle non définie.
l.13     \FLPF
              \cdot\FLPv
?
```

Quel était donc ce problème ? Ce n'est que plus tard que j'ai remarqué ce morceau de code dans le fichier `html`.

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

Cela signifie que lors du rendu de la page web, des macros ont été définies pour `MathJax`. Par conséquent, nous devrions également les ajouter dans notre code source de conversion `latex`. Ajoutons-les.

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

C'est comme ça qu'il faut faire.

![fv1](assets/images/feynman/fv1.png)

### Analyse du code

Voici le code final :

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

Lorsque nous souhaitons convertir un livre électronique entier, nous pouvons d'abord essayer avec une seule page.

```python
    file = open('The Feynman Lectures on Physics Vol. I Ch. 13_ Work and Potential Energy (A).html')
    content = file.read()
```

Voici où vous pouvez télécharger une page.

`MathJax` génère de nombreux éléments `div` et `span`. Par exemple, pour l'expression `T+U=const`, MathJax la génère de cette manière.

```html
<span class="MathJax">T</span>
<span class="MathJax">+</span>
<span class="MathJax">U</span>
<span class="MathJax">=</span>
<span class="MathJax">const</span>
```

Ces éléments sont gênants et peuvent perturber notre texte. Puisque nous avons déjà des `svg`, nous n'avons pas besoin de ceux-ci.

```python
def clean_mathjax(soup, name, cls):
    previews = soup.findAll(name, {'class': cls})
    for preview in previews:
        preview.decompose()
```

```python
    clean_mathjax(soup, 'span', 'MathJax')
    clean_mathjax(soup, 'div', 'MathJax_Display')
    clean_mathjax(soup, 'span', 'MathJax_Preview')
```

Supprimez-les tous.

```python
    mathjaxs = soup.findAll('script', {'type': 'math/tex'})
    to_svg(mathjaxs, equation=False)
    
    mathjaxs = soup.findAll('script', {'type': 'math/tex; mode=display'})   
    to_svg(mathjaxs, equation=True)
```

Notez qu'il y a deux types de `script` ici.

```latex
m(dv/dt)=F
```

*Note :* L'équation est en notation mathématique standard et ne nécessite pas de traduction. Elle représente la deuxième loi de Newton, où \( m \) est la masse, \( \frac{dv}{dt} \) est l'accélération, et \( F \) est la force.

Voici la forme intégrée.

```latex
\begin{equation}
\underset{\text{Énergie cinétique}}{\tfrac{1}{2}mv^2}+
\underset{\text{Énergie potentielle}}{\vphantom{\tfrac{1}{2}}mgh}=\text{constante},\notag
```

Ceci est sous forme de paragraphe.

Lors de l'utilisation de la forme intégrée, la conversion doit être entourée de `$` ou de `[]` de part et d'autre de l'expression. Sinon, des erreurs peuvent survenir.

```latex
\begin{document}
\begin{preview}
\tfrac{1}{2}mv^2
\end{preview}
\end{document}
```

```shell
! Missing $ inserted.
<inserted text>
                $
l.26 \tfrac{1}{2}
                 mv^2
```

*Note : Le message d'erreur est en anglais et ne nécessite pas de traduction, car il s'agit d'un message technique lié à LaTeX. Cependant, voici une explication en français :*

**Explication :**  
Cette erreur LaTeX indique qu'un symbole `$` est manquant. Dans LaTeX, les expressions mathématiques doivent être encadrées par des symboles `$` (pour le mode mathématique en ligne) ou `$$` (pour le mode mathématique centré). Ici, l'expression `\tfrac{1}{2} mv^2` doit être placée entre `$` pour être correctement interprétée. Par exemple :

```latex
$\tfrac{1}{2} mv^2$
```

Cela résoudra l'erreur.

Il faut le modifier comme ceci :

```latex
\begin{document}
\begin{preview}
$\tfrac{1}{2}mv^2$
\end{preview}
\end{document}
```

Voyons ensuite comment convertir `latex` en `svg`.

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

Voici comment enregistrer un fichier `svg`.

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

Voici quelques ajustements apportés au code source `latex`. Notez que `label` est devenu `tag`.

![tag](assets/images/feynman/tag.png)

Remarquez à droite le `(Eq:I:13:14)`. S'il s'agissait d'un `label`, il n'aurait pas été correctement interprété. Cela afficherait `(1)`. Ici, nous utilisons temporairement `tag` pour représenter cela, sans approfondir davantage pour le moment.

Ensuite, on procède à l'appel de `latex2svg.py`.

```python
        out = {}
        try:
            out = latex2svg(wrap)   
        except subprocess.CalledProcessError as err:
            raise err    
```

Regardez `latex2svg.py`.

```python
    # Exécuter LaTeX et créer un fichier DVI
    try:
        ret = subprocess.run(shlex.split(params['latex_cmd']+' code.tex'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('latex non trouvé')
```

Ici, nous appelons la commande `latex`.

```shell
 % latex --help
Usage: pdftex [OPTION]... [TEXNAME[.tex]] [COMMANDS]
   or: pdftex [OPTION]... \FIRST-LINE
   or: pdftex [OPTION]... &FMT ARGS
  Exécute pdfTeX sur TEXNAME, créant généralement TEXNAME.pdf.
```

```python
    try:
        ret = subprocess.run(shlex.split(params['dvisvgm_cmd']+' code.dvi'),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=working_directory, env=env)
        ret.check_returncode()
    except FileNotFoundError:
        raise RuntimeError('dvisvgm non trouvé')
```

Ici, on appelle la commande `dvisvgm`.

```shell
% dvisvgm
dvisvgm 2.9.1
```

Ce programme convertit les fichiers DVI, tels que ceux créés par TeX/LaTeX, ainsi que les fichiers EPS et PDF, au format de graphiques vectoriels évolutifs basé sur XML, SVG.

Utilisation : dvisvgm [options] fichier_dvi
       dvisvgm --eps [options] fichier_eps
       dvisvgm --pdf [options] fichier_pdf
```

Où écrire les macros personnalisées `latex` mentionnées ci-dessus ? Il faut modifier ici le fichier `latex2svg.py`. Modifiez le `default_preamble`.

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

Une fois la conversion réussie, écrivez dans le fichier.

```python
        f = open(f'svgs/{svg_prefix}{i}.svg', 'w')
        f.write(out['svg'])
        f.close()
```

Continuez.

```python
        node = BeautifulSoup('<img>', features="lxml")
        img = node.find('img')
        img.attrs['src'] = f'./svgs/{svg_prefix}{i}.svg'
        img.attrs['style'] = 'vertical-align: middle; margin: 0.5em 0;'
```

Voici comment construire une balise `img`.

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

Si c'est un `latex` sur une seule ligne, alors enveloppez-le avec une `div` et centrez-le.

```python
mathjax.insert_after(p)
```

Ici, on ajoute la balise `div` ou la balise `img` après le `script` d'origine.

```python
def clean_script(soup):
    scripts = soup.findAll('script')
    for s in scripts:
        s.decompose()    
        
clean_script(soup)
```

Après avoir remplacé tous les `latex` par des `svg`, vous n'avez plus besoin des `script`. Supprimez-les pour un code plus propre.

Enfin, écrivez le `html` modifié dans son intégralité dans un fichier.

```python
    output_file = open('out.html', 'w')
    output_file.write(soup.prettify())
    output_file.close()    
```

Ensuite, utilisez l'outil `pandoc` pour convertir en `epub`.

```shell
pandoc -s -r html out.html -o feynman.epub
```

Cela ouvrira un bel ebook.

Pourquoi ne pas directement intégrer la balise `svg` au lieu d'utiliser `img` pour l'inclure ? Autrement dit, pourquoi écrire ceci :

```html
<p></p>
<svg></svg>
<p></p>
```

Il y a un `bug` très étrange. Lorsqu'il y a beaucoup de `svg`, une situation comme celle-ci peut se produire.

<img src="/assets/images/feynman/svg_p1.png" alt="svg_p1" style="zoom:40%;" />

J'ai découvert plus tard qu'il suffisait d'utiliser la balise `img` pour l'intégrer. Quant à la raison pour laquelle cela fonctionne ainsi, je n'ai pas vraiment compris. Lorsque j'ai extrait ce `svg` individuel et que je l'ai visualisé dans le navigateur, il n'y avait aucun problème. Il semble donc que l'erreur se produit lorsque le navigateur essaie de rendre un très grand nombre de `svg` à la fois.

### Enfin

Quant à la conversion d'un fichier `epub` en `mobi`, vous pouvez utiliser l'outil officiel de `Kindle`, `Kindle Previewer 3`. Notez qu'il s'agit ici d'un seul chapitre.

Le code du projet se trouve sur [feynman-lectures-mobi@lzwjava](https://github.com/lzwjava/feynman-lectures-mobi).

Comment capturer et organiser toutes les pages pour en faire un livre électronique ? Nous en parlerons plus tard. Mais pour l'instant, ce chapitre des "Leçons de physique de Feynman" est déjà suffisant pour vous occuper. Alors, prenons notre Kindle et commençons à lire.