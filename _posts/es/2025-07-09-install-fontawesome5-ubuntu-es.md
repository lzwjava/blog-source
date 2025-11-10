---
audio: false
generated: true
lang: es
layout: post
title: Cómo instalar FontAwesome5 en LaTeX en Ubuntu
translated: true
type: note
---

Para instalar FontAwesome5 para LaTeX en Ubuntu, tienes varias opciones:

## Método 1: Usando tlmgr (TeX Live Manager)

Si tienes TeX Live instalado, puedes usar el gestor de paquetes:

```bash
sudo tlmgr update --self
sudo tlmgr install fontawesome5
```

## Método 2: Usando el gestor de paquetes apt

Ubuntu proporciona FontAwesome5 a través de sus repositorios:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

Esto instala una colección completa de fuentes que incluye FontAwesome5.

## Método 3: Instalación manual

Si los métodos anteriores no funcionan, puedes instalar manualmente:

1. Descarga el paquete FontAwesome5 desde CTAN
2. Extráelo en tu directorio texmf local:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
cd ~/texmf/tex/latex/fontawesome5
# Extrae el paquete descargado aquí
```

3. Actualiza la base de datos de TeX:
```bash
texhash ~/texmf
```

## Usando FontAwesome5 en LaTeX

Una vez instalado, puedes usarlo en tus documentos de LaTeX:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome \quad Icono de inicio
\faEnvelope \quad Icono de correo
\faGithub \quad Icono de GitHub
\end{document}
```

## Resolución de problemas

Si encuentras problemas:

1. Comprueba si tu instalación de TeX Live está actualizada:
```bash
tlmgr --version
```

2. Verifica que el paquete esté instalado:
```bash
tlmgr info fontawesome5
```

3. Asegúrate de usar XeLaTeX o LuaLaTeX para tener soporte completo de Unicode con FontAwesome5.

El enfoque más fácil suele ser el Método 2 usando `apt install texlive-fonts-extra` ya que maneja las dependencias automáticamente.