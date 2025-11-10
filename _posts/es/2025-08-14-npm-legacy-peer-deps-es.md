---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Comprender el indicador --legacy-peer-deps de npm
translated: true
type: note
---

### Resumen
La opción `--legacy-peer-deps` es una bandera utilizada con npm (Node Package Manager) para controlar cómo se manejan las dependencias peer durante la instalación de paquetes. Las dependencias peer son dependencias que un paquete espera que otro proporcione, pero que no se instalan automáticamente en las versiones más recientes de npm.

### Comportamiento
- **npm Estándar (v7+)**: Por defecto, aplica estrictamente los requisitos de las dependencias peer. Si un paquete declara una dependencia peer que no se cumple, npm advierte o falla la instalación para prevenir conflictos.
- **Con --legacy-peer-deps**: Vuelve al comportamiento anterior (de npm v3~v6), donde las dependencias peer faltantes se instalan automáticamente, incluso si esto conduce a duplicados o incompatibilidades. Esto puede resolver algunos problemas con paquetes legacy pero puede causar bugs.

### Ejemplo de Uso
En una terminal, ejecutarías:
```
npm install some-package --legacy-peer-deps
```
Esto se usa frecuentemente para proyectos que dependen de librerías antiguas que no han actualizado sus declaraciones de dependencias peer, como se ve en muchas configuraciones de React o Angular anteriores al manejo estricto de peers en npm.

### Cuándo Usarlo
Úsalo con moderación, ya que omite las salvaguardas y podría conducir a un "infierno de dependencias". Prefiere actualizar los paquetes o usar `--force`/`--save-dev` como alternativas mejores. Para más detalles, consulta la documentación oficial de npm sobre dependencias peer.