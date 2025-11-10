---
audio: false
generated: true
lang: es
layout: post
title: Tipografías Configurables en LaTeX
translated: true
type: note
---

Puedes hacer la fuente configurable creando variables al inicio de tu documento LaTeX. Aquí hay algunos enfoques:

## Método 1: Variables Simples (Recomendado)

## Método 2: Usando condicionales para diferentes sistemas

Permíteme crear una versión más sofisticada con detección automática del sistema operativo:

## Método 3: Usando archivo de configuración separado

También puedes crear un archivo separado para la configuración de fuentes:

Y luego en tu documento principal:

## Alternativas Comunes de Fuentes para Linux

Aquí hay algunas buenas alternativas de fuentes para sistemas Linux:

**Para fuentes chinas/CJK:**
- `Noto Sans CJK SC` (recomendado)
- `Source Han Sans SC`
- `WenQuanYi Micro Hei`
- `Droid Sans Fallback`

**Para fuentes en inglés:**
- `Liberation Serif` (alternativa a Times New Roman)
- `DejaVu Serif`
- `Linux Libertine`
- `TeX Gyre Termes`

## Uso

1. **Método 1** es el más simple - solo descomenta las líneas de fuentes para Linux cuando sea necesario
2. **Método 2** te permite cambiar solo una variable (`\fontsystem`) para alternar entre diferentes sistemas
3. **Método 3** mantiene la configuración de fuentes separada, facilitando el mantenimiento de diferentes versiones

¡Elige el método que mejor se adapte a tu flujo de trabajo!