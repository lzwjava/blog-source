---
audio: false
generated: true
image: false
lang: es
layout: post
title: Comparación de Liberty Agent y JaCoCo Agent
translated: true
type: note
---

En WebSphere Liberty (WLP), el `ws-javaagent.jar` es el agente de instrumentación Java propio de IBM. Se utiliza principalmente para la monitorización en tiempo de ejecución, diagnósticos e integración con herramientas como Application Performance Management (APM), Health Center o las capacidades de monitorización propias de Liberty. Cuando lo habilita, Liberty puede recopilar automáticamente métricas de profiling, recolección de basura, hilos y otras a nivel de la JVM.

El `jacocoagent.jar` de JaCoCo, por otro lado, es específicamente un **agente de cobertura de código**. Su propósito es instrumentar el bytecode en tiempo de ejecución para que las ejecuciones de pruebas o de la aplicación produzcan datos de cobertura (por ejemplo, qué clases, métodos y ramas se ejecutaron).

Por lo tanto, la distinción es:

*   **`ws-javaagent.jar`** → monitorización general, profiling, diagnósticos para Liberty y herramientas de IBM.
*   **`jacocoagent.jar`** → informes de cobertura de código/pruebas, independiente de Liberty.

No deberías reemplazar el agente de JaCoCo con el de Liberty. Si tu objetivo son los **informes de cobertura de pruebas** (para pipelines de CI, SonarQube, informes de Maven/Gradle, etc.), debes seguir usando el **agente de JaCoCo**. El agente de Liberty no generará archivos de cobertura `.exec` de JaCoCo.

Pero *puedes* ejecutar ambos al mismo tiempo si es necesario — Java admite múltiples argumentos `-javaagent`. Por ejemplo:

```bash
-javaagent:/ruta/al/ws-javaagent.jar
-javaagent:/ruta/al/jacocoagent.jar=destfile=jacoco.exec,output=file
```

👉 En resumen:
Usa **`jacocoagent.jar`** para la cobertura.
Usa **`ws-javaagent.jar`** si necesitas diagnósticos/profiling de Liberty.
Cumplen propósitos diferentes y no son intercambiables.

¿Quieres que también te muestre cómo configurarlos juntos en un archivo de opciones de la JVM del servidor Liberty?