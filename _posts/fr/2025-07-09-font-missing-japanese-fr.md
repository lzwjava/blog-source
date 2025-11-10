---
audio: false
generated: true
lang: fr
layout: post
title: Correction des glyphes manquants dans les polices japonaises
translated: true
type: note
---

Les erreurs que vous rencontrez indiquent que la police `FandolSong` (à la fois les variantes Regular et Bold) utilisée dans votre document LaTeX ne contient pas les glyphes nécessaires pour certains caractères japonais, tels que `ー` (U+30FC, Katakana-Hiragana Prolonged Sound Mark), `専` (U+5C02), `証` (U+8A3C), et `発` (U+767A). Cela provoque des erreurs "Missing character" de la part de XeLaTeX lors de la compilation de votre document, probablement `resume-ja.tex` ou un fichier associé dans `latex/ja/resume-ja/`.

La police `FandolSong` est principalement conçue pour le texte chinois et ne prend pas entièrement en charge les caractères japonais, ce qui explique les glyphes manquants. Pour résoudre ce problème, vous devez passer à une police qui prend en charge les caractères japonais, telle que `Noto Sans CJK JP` ou `IPAGothic`, comme recommandé précédemment. Ci-dessous, je vais vous guider pour corriger le problème en mettant à jour votre configuration de police et en assurant la compatibilité avec votre CV traduit en japonais.

### Pourquoi cela arrive
- **Limitation de la police** : `FandolSong` est une police chinoise incluse dans TeX Live pour la composition CJK mais n'inclut pas tous les caractères japonais, en particulier les katakana (`ー`) et les kanji courants utilisés en japonais.
- **XeLaTeX et xeCJK** : Votre document utilise probablement le package `xeCJK`, qui s'appuie sur la police CJK spécifiée (`FandolSong` dans ce cas) pour le texte japonais. Lorsque des glyphes sont manquants, XeLaTeX enregistre des erreurs et peut omettre les caractères dans le PDF de sortie.
- **Section traduite** : Étant donné que vous traduisez des sections comme `blogposts.tex` en japonais, le texte traduit contient des caractères japonais que `FandolSong` ne peut pas restituer.

### Solution : Changer la police CJK
Vous devez mettre à jour la configuration de police de votre document LaTeX pour utiliser une police compatible avec le japonais. Étant donné que votre message précédent indiquait un système Linux et un bloc de configuration de police, je suppose que vous utilisez XeLaTeX avec `xeCJK` et la structure `ifthenelse` pour la sélection des polices.

#### Étape 1 : Installer une police compatible avec le japonais
Assurez-vous qu'une police prenant en charge le japonais est installée sur votre système Linux. La police recommandée est `Noto Sans CJK JP`, qui est largement disponible et prend en charge tous les glyphes japonais nécessaires.

Pour installer `Noto Sans CJK JP` sur Ubuntu/Debian :
```bash
sudo apt-get install fonts-noto-cjk
```
Sur Fedora :
```bash
sudo dnf install google-noto-cjk-fonts
```
Sur Arch Linux :
```bash
sudo pacman -S noto-fonts-cjk
```

Alternativement, vous pouvez utiliser `IPAGothic` ou `IPAexGothic` :
```bash
sudo apt-get install fonts-ipaexfont
```

Vérifiez que la police est installée :
```bash
fc-list :lang=ja | grep Noto
```
Vous devriez voir des entrées comme `Noto Sans CJK JP` ou `Noto Serif CJK JP`. Si vous utilisez les polices IPA :
```bash
fc-list :lang=ja | grep IPA
```

#### Étape 2 : Mettre à jour la configuration des polices LaTeX
Modifiez la configuration des polices dans votre document LaTeX (probablement `resume-ja.tex` ou un fichier de préambule partagé) pour utiliser une police compatible avec le japonais. Sur la base de votre configuration de police précédente, voici comment mettre à jour la configuration :

```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    % Polices Linux
    \setCJKmainfont{Noto Sans CJK JP} % Police principale pour le japonais
    \setCJKsansfont{Noto Sans CJK JP} % Police sans-serif pour le japonais
    \setCJKmonofont{Noto Sans Mono CJK JP} % Police à chasse fixe pour le japonais
    \setmainfont{Liberation Serif} % Police anglaise
}
```

Si `Noto Sans Mono CJK JP` n'est pas disponible, vous pouvez utiliser `Source Code Pro` ou `DejaVu Sans Mono` pour le texte non-CJk à chasse fixe, mais assurez-vous que les blocs de code en japonais utilisent une police CJK :
```latex
\setCJKmonofont{Noto Sans CJK JP}
```

Si vous préférez `IPAGothic` :
```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{IPAexGothic}
    \setCJKsansfont{IPAexGothic}
    \setCJKmonofont{IPAexMincho} % Ou Noto Sans CJK JP pour la chasse fixe
    \setmainfont{Liberation Serif}
}
```

#### Étape 3 : Vérifier l'utilisation de xeCJK
Assurez-vous que votre document LaTeX utilise le package `xeCJK` et applique correctement les paramètres de police. Un exemple minimal pour `resume-ja.tex` pourrait ressembler à :

```latex
\documentclass[a4paper]{article}
\usepackage{xeCJK}
\usepackage{ifthenelse}

% Détection du système de polices
\newcommand{\fontsystem}{linux}

\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}

\begin{document}

% Texte japonais de blogposts.tex
\section{ブログ投稿}
こんにちは、私の名前は李智维です。最新の技術に関する記事を書いています。

% Texte anglais
\section{Introduction}
Hello, my name is Zhiwei Li.

\end{document}
```

Si votre CV utilise un template comme `awesome-cv`, assurez-vous que le préambule inclut `xeCJK` et les paramètres de police ci-dessus. Par exemple, dans `awesome-cv.cls` ou `resume-ja.tex`, ajoutez :

```latex
\RequirePackage{xeCJK}
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}
```

#### Étape 4 : Recompiler le document
Accédez au répertoire du CV japonais et recompilez :
```bash
cd latex/ja/resume-ja
xelatex resume-ja.tex
```

Vérifiez le fichier journal (`resume-ja.log`) pour les erreurs "Missing character". Si la police est correctement définie, ces erreurs devraient disparaître et le PDF devrait afficher correctement les caractères japonais comme `ー`, `専`, `証`, et `発`.

#### Étape 5 : Déboguer si les erreurs persistent
Si vous voyez toujours des erreurs "Missing character" :
1.  **Confirmer le nom de la police** : Assurez-vous que le nom de la police correspond exactement à celui listé dans `fc-list`. Par exemple, certains systèmes listent `Noto Sans CJK JP Regular` au lieu de `Noto Sans CJK JP`. Ajustez la configuration LaTeX :
    ```latex
    \setCJKmainfont{Noto Sans CJK JP Regular}
    ```
2.  **Vérifier la configuration xeCJK** : Assurez-vous que `xeCJK` est chargé avant les paramètres de police et qu'aucun autre package ne remplace la police CJK. Par exemple, évitez de charger `fontspec` avec des paramètres conflictuels.
3.  **Tester un document minimal** : Créez un fichier LaTeX minimal avec du texte japonais pour isoler le problème :
    ```latex
    \documentclass{article}
    \usepackage{xeCJK}
    \setCJKmainfont{Noto Sans CJK JP}
    \begin{document}
    こんにちは、専ー証発
    \end{document}
    ```
    Compilez avec `xelatex` et vérifiez les erreurs.
4.  **Police de secours** : Si `Noto Sans CJK JP` ne fonctionne pas, essayez `Source Han Sans JP` ou `IPAexGothic`. Listez les polices disponibles avec `fc-list :lang=ja` et mettez à jour la configuration en conséquence.

#### Étape 6 : Mettre à jour la section traduite
Étant donné que vous utilisez le script Python pour traduire des sections comme `blogposts.tex`, assurez-vous que le fichier traduit (`latex/ja/resume-ja/blogposts.tex`) est inclus dans `resume-ja.tex` via `\input{blogposts}`. Le script que vous avez fourni remplace déjà le fichier correctement, donc aucun changement n'est nécessaire là-bas. Il suffit de relancer la traduction si nécessaire :
```bash
python translate_section.py --section blogposts.tex --lang ja --kind resume
```

Puis recompilez `resume-ja.tex` pour incorporer la section mise à jour.

### Notes supplémentaires
- **Graisses de police** : `Noto Sans CJK JP` prend en charge plusieurs graisses (Regular, Bold, etc.), donc `\textbf{}` devrait fonctionner pour le texte japonais. Si vous utilisez `IPAexGothic`, assurez-vous que la variante bold (`IPAexGothic Bold`) est disponible ou ajustez la configuration.
- **Compatibilité du template** : Si vous utilisez un template comme `awesome-cv`, vérifiez s'il remplace les paramètres de police dans le fichier `.cls`. Vous devrez peut-être appliquer les paramètres `xeCJK` dans le document principal (`resume-ja.tex`) à la place.
- **Sortie PDF** : Inspectez le PDF généré pour vous assurer que les caractères japonais sont correctement restitués. Si les caractères apparaissent comme des carrés, la police est toujours incorrecte ou n'est pas correctement intégrée.
- **Cache des polices système** : Après avoir installé de nouvelles polices, mettez à jour le cache des polices :
  ```bash
  fc-cache -fv
  ```

### Exemple de sortie
Après avoir appliqué la correction, votre `blogposts.tex` dans `latex/ja/resume-ja/` pourrait contenir du texte japonais comme :
```latex
\section{ブログ投稿}
\item 技術ブログ: 最新のAI技術について書いています。専門的な内容をわかりやすく説明します。
```
Lorsqu'il est compilé avec `Noto Sans CJK JP`, les caractères comme `ー`, `専`, `証`, et `発` devraient être correctement restitués dans le PDF.

Si vous rencontrez d'autres erreurs ou avez besoin d'aide pour une partie spécifique du template de CV, veuillez partager le code LaTeX pertinent (par exemple, le préambule de `resume-ja.tex` ou les paramètres de police du template), et je pourrai fournir une correction plus ciblée !