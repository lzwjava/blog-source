---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-4.5-sonnet
title: Usos y Alternativas de MSVC Build Tools
translated: true
---

¡Las herramientas de compilación de MSVC son realmente masivas! Esto es para lo que realmente se usan:

## Usos principales

**Específicamente para Rust:**
- Compilar crates de Rust que tienen **dependencias de C/C++** (muy común)
- Compilar APIs nativas del sistema Windows
- Enlazar contra bibliotecas de Windows
- Compilar proyectos que usan la crate `cc` o bindgen

**Propósitos generales:**
- Compilar código C/C++ en Windows
- Construir paquetes de Python con extensiones nativas (como numpy, pandas)
- Compilar complementos nativos de Node.js
- Construir cualquier software que necesite un compilador de C/C++ en Windows

## ¿Por qué son tan grandes?

La inflación viene de:
- Windows SDK (encabezados, bibliotecas para cada versión de Windows)
- Múltiples toolchains de compilación (x86, x64, ARM, ARM64)
- Bibliotecas ATL/MFC
- Herramientas de depuración y símbolos
- Componentes del sistema de compilación (MSBuild)

## Alternativas más ligeras

Si solo necesitas Rust:
1. **Usa la toolchain GNU** - instala `rustup` con el target `x86_64-pc-windows-gnu` (necesita MinGW, ~2-3 GB)
2. **WSL2** - Usa la toolchain de Linux completamente
3. **Instalación mínima de MSVC** - Durante la instalación, deselecciona los componentes opcionales que no necesitas

Para código Rust puro sin dependencias de C/C++, no necesitas MSVC en absoluto. Pero, siendo realistas, muchas crates populares (como `openssl-sys`, `ring`, bibliotecas de ventanas) necesitan un compilador de C, así que la mayoría de los desarrolladores de Rust en Windows terminan instalándolo.

Es molesto, pero la toolchain de Microsoft siempre ha sido pesada. La alternativa GNU funciona pero ocasionalmente tiene problemas de compatibilidad con algunas crates.