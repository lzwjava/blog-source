---
audio: false
generated: true
lang: es
layout: post
title: Corrección del Modo de Usuario de tlmgr en TeX Live
translated: true
type: note
---

El error indica que el modo usuario de `tlmgr` no está inicializado en tu sistema Debian/Ubuntu. Este es un problema común con las instalaciones de TeX Live desde los repositorios de Ubuntu. Aquí te mostramos cómo solucionarlo:

## Solución 1: Inicializar el modo usuario de tlmgr

Primero, inicializa el modo usuario:

```bash
tlmgr init-usertree
```

Si eso no funciona, prueba con:

```bash
tlmgr --usermode init-usertree
```

## Solución 2: Usar apt en su lugar (Recomendado para Ubuntu)

Ya que estás en Ubuntu/Debian, a menudo es más fácil usar el gestor de paquetes del sistema:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

Esto instalará FontAwesome5 junto con otros paquetes de fuentes.

## Solución 3: Verificar si FontAwesome5 ya está instalado

Puede que ya lo tengas instalado. Pruébalo creando un archivo LaTeX simple:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome
\end{document}
```

Compílalo con:
```bash
pdflatex test.tex
```

## Solución 4: Si necesitas la última versión

Si específicamente necesitas la última versión de FontAwesome5, puedes:

1. Descargar el paquete manualmente desde CTAN
2. Instalarlo en tu directorio texmf local:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
# Extrae el paquete descargado en este directorio
texhash ~/texmf
```

## Comprobación rápida

Para ver qué paquetes de TeX tienes actualmente instalados:

```bash
dpkg -l | grep texlive
```

Para la mayoría de los usuarios, `sudo apt install texlive-fonts-extra` es la solución más simple y evita por completo los problemas del modo usuario de tlmgr.