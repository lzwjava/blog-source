---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Resolución de Dependencias en Maven Multi-Módulo
translated: true
type: note
---

Sí, eso es correcto: en un proyecto multi-módulo de Maven, cuando un módulo (por ejemplo, un módulo EAR) depende de otro (por ejemplo, un módulo WAR), Maven resuelve la dependencia del repositorio local `.m2/repository` por defecto, no directamente del directorio `target/` del otro módulo. Esto se debe a que Maven trata las dependencias entre módulos como referencias estándar a artefactos (como librerías externas), por lo que el artefacto dependiente debe estar instalado (o al menos empaquetado y ser descubrible a través del reactor de construcción).

### Por qué sucede esto
- **Resolución del Repositorio Local**: El mecanismo de resolución de dependencias de Maven busca los artefactos primero en el repositorio local. El directorio `target/` solo se usa temporalmente durante la construcción de un único módulo, pero para referencias entre módulos, espera que el artefacto esté "publicado" (instalado).
- **Las Construcciones del Reactor Ayudan, Pero No Siempre Son Suficientes**: Si ejecutas `mvn package` (o `mvn install`) desde la **raíz del POM padre**, el reactor de Maven construye automáticamente los módulos en orden topológico. Resuelve las dependencias entre módulos sobre la marcha sin necesidad de instalaciones explícitas, extrayendo la salida fresca del directorio `target/` del otro módulo durante la sesión. Pero si construyes el módulo dependiente (por ejemplo, el EAR) **de forma independiente** (por ejemplo, `cd ear-module && mvn package`), no verá el `target/` del WAR—fallará a menos que el artefacto WAR ya esté en `.m2`.

### Para el Empaquetado WAR-a-EAR Específicamente
En un proyecto EAR:
- El plugin EAR (`maven-ear-plugin`) espera el WAR (y otros módulos) como artefactos resueltos para incluirlos en el archivo EAR (por ejemplo, mediante `<modules>` en el POM del EAR).
- Si el WAR no está instalado, obtendrás errores como "Could not resolve dependencies" o módulos faltantes en el EAR.

**Solución**: Sí, generalmente necesitas ejecutar `mvn install` (o al menos `mvn package` en una construcción completa del reactor) en el módulo "original" (dependencia) primero si estás construyendo de forma independiente. Las mejores prácticas:
1. **Preferido: Construir desde el Padre**: `mvn clean install` en la raíz del proyecto. Esto instala todo en `.m2` y maneja el orden automáticamente.
2. **Si Construyes Módulos por Separado**:
   - `cd war-module && mvn clean install` (instala el JAR WAR en `.m2`).
   - Luego `cd ear-module && mvn clean package` (o `install`—los EARs a menudo solo necesitan `package`).
3. **Evitar Referencias Directas a Target**: No busques soluciones alternativas con `<systemPath>` o rutas de archivo a `target/`—es frágil y omite las sumas de comprobación y transitividad de Maven.

Este comportamiento no ha cambiado en las versiones recientes de Maven (hasta 3.9.x a partir de 2025). Para más detalles, consulta la guía oficial de multi-módulo.

[Introducción al Ciclo de Vida de Construcción - Proyectos Multi-módulo](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#multi-module)  
[Documentación del Plugin Maven EAR](https://maven.apache.org/plugins/maven-ear-plugin/ear-mojo.html)