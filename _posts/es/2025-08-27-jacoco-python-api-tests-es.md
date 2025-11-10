---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de JaCoCo para Pruebas de API en Python
translated: true
type: note
---

Buena pregunta — este es un problema clásico de integración entre **herramientas de cobertura de código Java** (JaCoCo) y **harnesses de prueba que no son Java** (como `unittest` de Python que accede a tus endpoints REST).

---

### Por qué JaCoCo funciona con JUnit pero no directamente con pruebas de Python

* JaCoCo funciona adjuntando un **agente Java** (`-javaagent:jacocoagent.jar`) a la JVM.
* Cuando tus pruebas se ejecutan **dentro de la misma JVM** (JUnit, TestNG, etc.), JaCoCo puede ver qué clases y métodos se cargan/ejecutan y generar informes de cobertura detallados.
* Si usas `unittest` de Python + `requests` para acceder a tus endpoints de API, estás ejercitando el **servidor en ejecución** desde fuera de la JVM.
  Eso significa que JaCoCo no ve la cobertura automáticamente, a menos que el propio proceso del servidor tenga el agente adjunto.

---

### Cómo puedes obtener una cobertura precisa con JaCoCo y pruebas de Python

No necesitas cambiar a JUnit. Todavía puedes usar JaCoCo, pero debes **adjuntar el agente a la JVM donde se ejecuta tu gran proyecto Java (el servidor)**, no al ejecutor de pruebas.

1. **Ejecuta tu aplicación Java con el agente de JaCoCo**
   Añade el agente al inicio de tu servidor Java:

   ```bash
   java -javaagent:/ruta/a/jacocoagent.jar=destfile=jacoco-it.exec,output=file,append=false \
        -jar miservidor.jar
   ```

   Esto recopilará datos de ejecución (`jacoco-it.exec`) mientras tus pruebas de Python acceden a los endpoints.

2. **Ejecuta tus pruebas de Python normalmente**

   ```bash
   python -m unittest discover tests/
   ```

   Dado que el servidor ya se está ejecutando con el agente, todas las clases y métodos accedidos por las peticiones HTTP quedarán registrados.

3. **Apaga el servidor**
   El archivo `.exec` se vaciará.

4. **Genera un informe de cobertura**
   Usa el plugin de Maven o la CLI para convertir el archivo `.exec` en informes HTML/XML:

   ```bash
   mvn jacoco:report -Djacoco.dataFile=jacoco-it.exec
   ```

   o con la CLI:

   ```bash
   java -jar jacococli.jar report jacoco-it.exec \
        --classfiles target/classes \
        --sourcefiles src/main/java \
        --html report
   ```

---

### Dos modos de prueba con JaCoCo

* **Pruebas unitarias (en la JVM con JUnit):** funciona listo para usar con el plugin de Maven (`prepare-agent` + `report`).
* **Pruebas de integración (clientes externos como Python):** requiere iniciar la JVM con el agente, luego fusionar los datos `.exec` de nuevo en los informes.

---

### Sobre tu idea de log4j

Contar declaraciones de log por archivo es extremadamente básico:

* No todos los métodos registran logs.
* Los logs no cubren condicionales o ramas.
* La cobertura no es confiable.

JaCoCo, en cambio, mide **cobertura de clase, método, línea y rama** — una granularidad mucho más fina.

---

✅ **Respuesta:** Sí, puedes usar absolutamente el enfoque de JaCoCo incluso si tus pruebas están en Python. El truco es **adjuntar JaCoCo al proceso Java bajo prueba** (tu servidor), no al ejecutor de pruebas. Luego genera el informe después. De esta manera obtendrás la misma cobertura a nivel de método y de rama que con JUnit.

---

¿Quieres que redacte un **ejemplo de configuración de Maven** que configure un perfil especial para "pruebas de integración" con JaCoCo, para que puedas ejecutar tu servidor, acceder a él con pruebas de Python y luego generar la cobertura con un solo comando?