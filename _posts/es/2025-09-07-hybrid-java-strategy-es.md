---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Estrategia de Desarrollo Híbrido de Java
translated: true
type: note
---

Resumen: para bases de código Java grandes, lo mejor es un enfoque **híbrido**. Usa **VS Code** como tu cockpit centrado en IA (Claude Code + Copilot = iteración más rápida y menos código repetitivo), y mantén **IntelliJ IDEA** a mano para la "cirugía mayor" (refactorizaciones profundas, inspecciones, asistentes avanzados de Spring/Gradle/Maven). No tienes que elegir una sola religión. 🙂

Así es como lo veo—sin tablas, solo lo esencial:

### Donde VS Code brilla

* **Flujo de trabajo con IA**: Las finalizaciones en línea de Copilot siguen siendo mejores en VS Code, y el razonamiento a nivel de repositorio de Claude Code se siente más ágil allí. Ideal para redactar servicios, tests, mappers, SQL y rediseños rápidos.
* **Ligero y modular**: Solo añades lo que necesitas. Los tiempos de inicio en frío y el uso de memoria son más amigables en monorepositorios enormes.
* **"Ir a" + LSP**: Con las extensiones de Java, "Ir a Definición/Implementación", la jerarquía de tipos, la jerarquía de llamadas y la búsqueda de símbolos son lo suficientemente sólidas para el día a día.

Extensiones recomendadas (busca por ID):

* `vscjava.vscode-java-pack` (incluye la mayoría de las siguientes)
* `redhat.java` (Language Support for Java)
* `vscjava.vscode-java-debug` / `vscjava.vscode-java-test`
* `vscjava.vscode-maven` / `vscjava.vscode-gradle`
* `vscjava.vscode-spring-boot-dashboard` + `vscjava.vscode-spring-initializr`
* `sonarsource.sonarlint-vscode` (comprobaciones estáticas)
* `streetsidesoftware.code-spell-checker` (sorprendentemente útil en JavaDocs)
* Claude Code + GitHub Copilot

Ajustes de rendimiento para proyectos grandes (pon en `.vscode/settings.json`):

```json
{
  "java.maxConcurrentBuilds": 4,
  "java.jdt.ls.vmargs": "-Xms512m -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication",
  "java.errors.incompleteClasspath.severity": "ignore",
  "java.referencesCodeLens.enabled": false,
  "java.implementationsCodeLens.enabled": false,
  "files.watcherExclude": {
    "**/target/**": true,
    "**/.gradle/**": true,
    "**/node_modules/**": true
  }
}
```

Consejos:

* Importa como **Gradle** o **Maven** (evita builds mixtos si puedes).
* Habilita el **Spring Boot Dashboard** para ejecutar y depurar múltiples servicios.
* Deja que Claude/Copilot redacte clases y tests, pero usa **SonarLint** y tus unit tests como barreras de seguridad.

### Donde IntelliJ IDEA aún gana

* **Profundidad y precisión en refactorización**: Renombrar/mover/extraer a través de jerarquías enormes, APIs con muchos genéricos, Lombok, configuraciones XML, incluso el wiring de beans de Spring—el modelo semántico de IDEA es difícil de superar.
* **Inspecciones y correcciones rápidas**: Las inspecciones de código integradas (y la búsqueda/reemplazo estructural) detectan olores más sutiles que la mayoría de configuraciones de VS Code.
* **UML y ventajas de navegación**: Flujo de datos hacia/desde aquí, diagramas de dependencias y ámbitos de búsqueda avanzados ahorran tiempo en dominios complejos.

Patrón práctico:

* Haz la **exploración, scaffolding y ediciones repetitivas** en VS Code con Claude/Copilot.
* Cuando necesites una **refactorización no trivial** (ej. dividir un módulo core, cambiar contratos de API en 40 módulos, migrar configuración de Spring), abre el mismo repositorio en IDEA, deja que indexe una vez, haz la refactorización de forma segura, haz push y vuelve a VS Code.

### Sobre "Codex"

Los antiguos modelos **Codex** de OpenAI se descontinuaron hace tiempo. Hoy usarás principalmente **GitHub Copilot** (con tecnología de OpenAI internamente) y **Claude Code**. Considera "Codex" como histórico—tu stack actual debería ser **Copilot + Claude Code**.

### Análisis estático y calidad en VS Code

* **SonarLint** en VS Code te da una sensación cercana a IDEA; combínalo con una puerta de calidad SonarQube/SonarCloud en tu CI.
* Añade **SpotBugs** y **Checkstyle** mediante plugins de Gradle/Maven para que la calidad se ejecute en CI (no solo localmente).
* Usa el explorador de tests **JUnit** y la extensión **Coverage Gutters** para mantener un ciclo rojo-verde ajustado.

### Específicos de Spring/empresa

* Las **herramientas Spring** de VS Code son buenas para ejecutar/depurar, endpoints de actuator y sugerencias de propiedades. Para auto-configuración compleja o meta-anotaciones, IDEA aún resuelve las cosas de forma más fiable—úsala cuando las anotaciones parezcan "misteriosas".
* Para monstruos **Gradle** multi-módulo: mantén el daemon y las builds paralelas activadas, y considera usar composite builds para limitar el tamaño del workspace.

### Flujo de trabajo con IA que escala

* **Copilot en línea** para ediciones diminutas mientras escribes.
* Chat de **Claude Code** para razonamiento a nivel de repositorio ("¿cuáles son los efectos secundarios si cambio el constructor de `LedgerPosting`?" / "redacta un PR para reemplazar nuestro retry personalizado por resilience4j").
* Pídele al modelo que produzca **planes de refactorización + listas de comprobación**; luego aplica los cambios en commits pequeños y revisables.
* Mantén la **salida del modelo bajo test**: exige diffs de tests unitarios/de integración en el mismo PR que generó la IA.

### Entonces... ¿en cuál deberías vivir?

* Si tu día es **codificar + iterar + muchas asistencias de IA** → usar **VS Code** como editor principal se siente mejor ahora mismo.
* Si tu día es **arquitecturar + grandes refactorizaciones + depurar casos límite del framework** → mantén **IntelliJ** abierto para esos momentos.
* Muchos ingenieros senior alternan entre ambos. Eso no es ineficiencia; es usar la herramienta correcta para el nivel de riesgo adecuado.

Si quieres, puedo generar una **configuración de bootstrap Java para VS Code** (extensions.json, settings.json, configuraciones de tasks/launch recomendadas) ajustada para tu monorepositorio—y una breve lista de comprobación para IDEA para los momentos de "traer la artillería pesada".