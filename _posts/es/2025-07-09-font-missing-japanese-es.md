---
audio: false
generated: true
lang: es
layout: post
title: Corrección de glifos faltantes en fuentes japonesas
translated: true
type: note
---

Los errores que estás encontrando indican que la fuente `FandolSong` (tanto las variantes Regular como Bold) utilizada en tu documento LaTeX no contiene los glifos necesarios para ciertos caracteres japoneses, como `ー` (U+30FC, Katakana-Hiragana Prolonged Sound Mark), `専` (U+5C02), `証` (U+8A3C) y `発` (U+767A). Esto está causando que XeLaTeX reporte errores de "Missing character" al compilar tu documento, probablemente `resume-ja.tex` o un archivo relacionado en `latex/ja/resume-ja/`.

La fuente `FandolSong` está diseñada principalmente para texto en chino y carece de soporte completo para caracteres japoneses, lo que explica los glifos faltantes. Para resolver esto, necesitas cambiar a una fuente que admita caracteres japoneses, como `Noto Sans CJK JP` o `IPAGothic`, como se recomendó anteriormente. A continuación, te guiaré para solucionar el problema actualizando la configuración de tu fuente y asegurando la compatibilidad con tu currículum traducido al japonés.

### Por qué sucede esto
- **Limitación de la fuente**: `FandolSong` es una fuente china incluida en TeX Live para la composición tipográfica CJK, pero no incluye todos los caracteres japoneses, especialmente katakana (`ー`) y kanjis comunes utilizados en japonés.
- **XeLaTeX y xeCJK**: Es probable que tu documento utilice el paquete `xeCJK`, que depende de la fuente CJK especificada (`FandolSong` en este caso) para el texto en japonés. Cuando faltan glifos, XeLaTeX registra errores y puede omitir los caracteres en el PDF de salida.
- **Sección traducida**: Dado que estás traduciendo secciones como `blogposts.tex` al japonés, el texto traducido contiene caracteres japoneses que `FandolSong` no puede representar.

### Solución: Cambiar la fuente CJK
Necesitas actualizar la configuración de fuente de tu documento LaTeX para usar una fuente compatible con japonés. Dado que tu mensaje anterior indicaba un sistema Linux y un bloque de configuración de fuentes, asumiré que estás usando XeLaTeX con `xeCJK` y la estructura `ifthenelse` para la selección de fuentes.

#### Paso 1: Instalar una fuente compatible con japonés
Asegúrate de que haya una fuente con soporte para japonés instalada en tu sistema Linux. La fuente recomendada es `Noto Sans CJK JP`, que está ampliamente disponible y admite todos los glifos japoneses necesarios.

Para instalar `Noto Sans CJK JP` en Ubuntu/Debian:
```bash
sudo apt-get install fonts-noto-cjk
```
En Fedora:
```bash
sudo dnf install google-noto-cjk-fonts
```
En Arch Linux:
```bash
sudo pacman -S noto-fonts-cjk
```

Alternativamente, puedes usar `IPAGothic` o `IPAexGothic`:
```bash
sudo apt-get install fonts-ipaexfont
```

Verifica que la fuente esté instalada:
```bash
fc-list :lang=ja | grep Noto
```
Deberías ver entradas como `Noto Sans CJK JP` o `Noto Serif CJK JP`. Si usas fuentes IPA:
```bash
fc-list :lang=ja | grep IPA
```

#### Paso 2: Actualizar la configuración de fuente en LaTeX
Modifica la configuración de fuente en tu documento LaTeX (probablemente `resume-ja.tex` o un archivo de preámbulo compartido) para usar una fuente compatible con japonés. Basándome en tu configuración de fuente anterior, así es como puedes actualizar la configuración:

```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    % Fuentes Linux
    \setCJKmainfont{Noto Sans CJK JP} % Fuente principal para japonés
    \setCJKsansfont{Noto Sans CJK JP} % Fuente sans-serif para japonés
    \setCJKmonofont{Noto Sans Mono CJK JP} % Fuente monoespacio para japonés
    \setmainfont{Liberation Serif} % Fuente para inglés
}
```

Si `Noto Sans Mono CJK JP` no está disponible, puedes usar `Source Code Pro` o `DejaVu Sans Mono` para texto monoespacio no CJK, pero asegúrate de que los bloques de código en japonés usen una fuente CJK:
```latex
\setCJKmonofont{Noto Sans CJK JP}
```

Si prefieres `IPAGothic`:
```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{IPAexGothic}
    \setCJKsansfont{IPAexGothic}
    \setCJKmonofont{IPAexMincho} % O Noto Sans CJK JP para monoespacio
    \setmainfont{Liberation Serif}
}
```

#### Paso 3: Verificar el uso de xeCJK
Asegúrate de que tu documento LaTeX use el paquete `xeCJK` y aplique la configuración de fuente correctamente. Un ejemplo mínimo para `resume-ja.tex` podría verse así:

```latex
\documentclass[a4paper]{article}
\usepackage{xeCJK}
\usepackage{ifthenelse}

% Detección del sistema de fuentes
\newcommand{\fontsystem}{linux}

\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}

\begin{document}

% Texto en japonés de blogposts.tex
\section{ブログ投稿}
こんにちは、私の名前は李智维です。最新の技術に関する記事を書いています。

% Texto en inglés
\section{Introduction}
Hello, my name is Zhiwei Li.

\end{document}
```

Si tu currículum usa una plantilla como `awesome-cv`, asegúrate de que el preámbulo incluya `xeCJK` y la configuración de fuente anterior. Por ejemplo, en `awesome-cv.cls` o `resume-ja.tex`, agrega:

```latex
\RequirePackage{xeCJK}
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}
```

#### Paso 4: Recompilar el documento
Navega al directorio del currículum en japonés y recompila:
```bash
cd latex/ja/resume-ja
xelatex resume-ja.tex
```

Revisa el archivo de registro (`resume-ja.log`) en busca de errores de "Missing character". Si la fuente está configurada correctamente, estos errores deberían desaparecer y el PDF debería mostrar caracteres japoneses como `ー`, `専`, `証` y `発` correctamente.

#### Paso 5: Depurar si los errores persisten
Si aún ves errores de "Missing character":
1. **Confirmar el nombre de la fuente**: Asegúrate de que el nombre de la fuente coincida exactamente con el listado en `fc-list`. Por ejemplo, algunos sistemas listan `Noto Sans CJK JP Regular` en lugar de `Noto Sans CJK JP`. Ajusta la configuración en LaTeX:
   ```latex
   \setCJKmainfont{Noto Sans CJK JP Regular}
   ```
2. **Verificar la configuración de xeCJK**: Asegúrate de que `xeCJK` se cargue antes de la configuración de fuentes y de que ningún otro paquete anule la fuente CJK. Por ejemplo, evita cargar `fontspec` con configuraciones conflictivas.
3. **Probar con un documento mínimo**: Crea un archivo LaTeX mínimo con texto en japonés para aislar el problema:
   ```latex
   \documentclass{article}
   \usepackage{xeCJK}
   \setCJKmainfont{Noto Sans CJK JP}
   \begin{document}
   こんにちは、専ー証発
   \end{document}
   ```
   Compila con `xelatex` y verifica si hay errores.
4. **Fuente de respaldo**: Si `Noto Sans CJK JP` no funciona, prueba con `Source Han Sans JP` o `IPAexGothic`. Lista las fuentes disponibles con `fc-list :lang=ja` y actualiza la configuración en consecuencia.

#### Paso 6: Actualizar la sección traducida
Dado que estás usando el script de Python para traducir secciones como `blogposts.tex`, asegúrate de que el archivo traducido (`latex/ja/resume-ja/blogposts.tex`) esté incluido en `resume-ja.tex` mediante `\input{blogposts}`. El script que proporcionaste ya reemplaza el archivo correctamente, por lo que no se necesitan cambios allí. Simplemente vuelve a ejecutar la traducción si es necesario:
```bash
python translate_section.py --section blogposts.tex --lang ja --kind resume
```

Luego, recompila `resume-ja.tex` para incorporar la sección actualizada.

### Notas adicionales
- **Pesos de fuente**: `Noto Sans CJK JP` admite múltiples pesos (Regular, Bold, etc.), por lo que `\textbf{}` debería funcionar para el texto en japonés. Si usas `IPAexGothic`, asegúrate de que la variante bold (`IPAexGothic Bold`) esté disponible o ajusta la configuración.
- **Compatibilidad con la plantilla**: Si estás usando una plantilla como `awesome-cv`, verifica si anula la configuración de fuentes en el archivo `.cls`. Es posible que necesites aplicar la configuración de `xeCJK` en el documento principal (`resume-ja.tex`).
- **Salida PDF**: Inspecciona el PDF generado para asegurarte de que los caracteres japoneses se representen correctamente. Si los caracteres aparecen como cuadros, la fuente sigue siendo incorrecta o no está incrustada correctamente.
- **Caché de fuentes del sistema**: Después de instalar nuevas fuentes, actualiza la caché de fuentes:
  ```bash
  fc-cache -fv
  ```

### Ejemplo de salida
Después de aplicar la solución, tu `blogposts.tex` en `latex/ja/resume-ja/` podría contener texto en japonés como:
```latex
\section{ブログ投稿}
\item 技術ブログ: 最新のAI技術について書いています。専門的な内容をわかりやすく説明します。
```
Cuando se compile con `Noto Sans CJK JP`, caracteres como `ー`, `専`, `証` y `発` deberían representarse correctamente en el PDF.

Si encuentras más errores o necesitas ayuda con una parte específica de la plantilla del currículum, por favor comparte el código LaTeX relevante (por ejemplo, el preámbulo de `resume-ja.tex` o la configuración de fuentes de la plantilla), y ¡puedo proporcionar una solución más específica!