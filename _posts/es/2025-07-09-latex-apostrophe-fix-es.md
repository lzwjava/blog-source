---
audio: false
generated: true
lang: es
layout: post
title: Corrección del Renderizado del Apóstrofo en LaTeX
translated: true
type: note
---

El problema que estás experimentando con el apóstrofo en "HSBC's" probablemente esté relacionado con cómo LaTeX maneja ciertos caracteres de comillas/apóstrofes en la salida PDF. Aquí hay varias formas de mejorar el renderizado:

## 1. Usar el apóstrofo correcto de LaTeX
Reemplaza el apóstrofo recto (') con el apóstrofo propio de LaTeX:
```latex
\item {Backend Engineer outsourced to HSBC Bank under TEKsystems, developing and optimizing backend systems for the \href{https://www.google.com/search?q=Finance+Timezone+Platform+HSBC}{Finance Transformation Platform} in HSBC's Enterprise Technology Department.}
```
Cambiar a:
```latex
\item {Backend Engineer outsourced to HSBC Bank under TEKsizer, developing and optimizing backend systems for the \href{https://www.google.com/search?q=Finance+Transformation+Platform+HSBC}{Finance Transformation Platform} in HSBC's Enterprise Technology Department.}
```

## 2. Usar el comando `\textquotesingle`
```latex
HSBC\textquotesingle{}s
```

## 3. Usar el enfoque `\textasciigrave` y `\textquotesingle`
```latex
HSBC\textquotesingle{}s
```

## 4. Agregar el paquete `textcomp`
Agrega esto a tu preámbulo:
```latex
\usepackage{textcomp}
```
Luego usa:
```latex
HSBC\textquotesingle{}s
```

## 5. Usar codificación UTF-8 (si aún no lo está)
Asegúrate de que tu documento use codificación UTF-8:
```latex
\usepackage[utf8]{inputenc}
```

## 6. Probar el paquete `babel` para mejor tipografía
```latex
\usepackage[british]{babel}
```

## Solución más confiable:
Para los mejores resultados, recomiendo usar la combinación de acento grave y apóstrofo, que es la forma tradicional de LaTeX para una tipografía adecuada:

```latex
\item {Backend Engineer outsourced to HSBC Bank under TEKsystems, developing and optimizing backend systems for the \href{https://www.google.com/search?q=Finance+Transformation+Platform+HSBC}{Finance Transformation Platform} in HSBC`s Enterprise Technology Department.}
```

Esto se renderizará con el espaciado y curvatura tipográficos correctos en la salida PDF. El acento grave (`) seguido del apóstrofo (') crea la apariencia correcta para las formas posesivas en LaTeX.