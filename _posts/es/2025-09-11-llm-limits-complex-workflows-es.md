---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Límites de los LLM en Flujos de Trabajo Complejos
translated: true
type: note
---

¡Tienes toda la razón! Los LLM (incluyéndome a mí) sobresalen en **tareas pequeñas y enfocadas**—como explicar un concepto único, generar un fragmento de código corto o depurar un error específico—pero tienen dificultades con **flujos de trabajo complejos y de múltiples pasos** que implican:

1.  **Múltiples configuraciones interconectadas** (por ejemplo, archivos Maven `pom.xml`, argumentos del agente Jacoco, integración de pruebas en Python).
2.  **Dependencias con estado** (por ejemplo, "Primero actualiza `module-A/pom.xml`, luego ejecuta `mvn test` con estos flags, luego fusiona los reportes").
3.  **Interacciones entre sistemas** (por ejemplo, Java + Python + herramientas de CI como Jenkins/GitHub Actions).
4.  **Cambio de contexto** (por ejemplo, "Ahora olvida la parte de Java—¿cómo analizamos el XML de Jacoco en Python?").

---

### **Por qué los LLM Fallan en Flujos de Trabajo Complejos**
1.  **Sin Memoria Persistente**: No "recordamos" pasos anteriores a menos que nos lo recuerdes explícitamente (e incluso así, las ventanas de contexto son limitadas).
2.  **Pensamiento Lineal**: Generamos respuestas paso a paso pero no podemos rastrear dinámicamente las dependencias (por ejemplo, "¿Ejecutaste `mvn clean` antes que el agente?").
3.  **Sobre-Optimización para Respuestas Únicas**: Estamos entrenados para dar *una* respuesta completa, no una guía iterativa.
4.  **Sin Entorno de Ejecución**: No podemos ejecutar comandos para verificar si `jacoco:prepare-agent` realmente funcionó en tu configuración.

---

### **Mejor Enfoque: "Dividir y Verificar"**
Para problemas como **Jacoco + Maven multi-módulo + pruebas en Python**, divídelo en **pasos atómicos** y verifica cada uno. Ejemplo:

#### **Paso 1: Verificar la Configuración del Agente Jacoco (Lado Java)**
```bash
# En UN módulo (por ejemplo, module-A):
mvn clean test -Pcoverage
```
-   **Verifica**: ¿Existe `target/site/jacoco/index.html`?
-   **Depuración**: Si no, comparte el fragmento del `pom.xml` para Jacoco y el registro de error.

#### **Paso 2: Generar Reporte Combinado (Multi-Módulo)**
```bash
mvn jacoco:report-aggregate
```
-   **Verifica**: ¿Se creó `target/site/jacoco-aggregate/index.html`?
-   **Depuración**: Si falta, verifica las rutas `<module>` en el `pom.xml` padre.

#### **Paso 3: Exportar para Python (XML/CSV)**
```bash
# Convertir el binario de Jacoco a XML
java -jar jacoco-cli.jar report jacoco.exec --xml output.xml
```
-   **Verifica**: ¿Contiene `output.xml` etiquetas `<package>`?
-   **Depuración**: Si está vacío, asegúrate de que las pruebas se ejecutaron con el agente (`-javaagent:jacocoagent.jar`).

#### **Paso 4: Integración con Python**
```python
import xml.etree.ElementTree as ET
tree = ET.parse("output.xml")
coverage = tree.find(".//counter[@type='LINE'][@covered]")
print(f"Líneas cubiertas: {coverage.get('covered')}/{coverage.get('missed')}")
```
-   **Verifica**: ¿El script devuelve los números esperados?
-   **Depuración**: Si no, comparte la estructura del XML y el error de Python.

---

### **Cómo Trabajar con LLMs Efectivamente**
1.  **Aísla el Problema**:
    -   *"Aquí está mi `pom.xml` para el módulo-A. ¿Por qué `jacoco:prepare-agent` no añade el argumento de VM?"*
    -   *(Mejor que: "Ayúdame a configurar Jacoco para 5 módulos + Python.")*

2.  **Comparte Contexto Mínimo Reproducible**:
    -   Registros de error, fragmentos de configuración (no archivos completos) y **lo que has intentado**.

3.  **Depuración Iterativa**:
    -   **Tú**: "El Paso 1 falló con `No tests run`. Aquí está el registro."
    -   **LLM**: "Añade metas `<test>` a tu `maven-surefire-plugin`."
    -   **Tú**: "Ahora el Paso 2 funciona, pero el reporte está vacío..."

4.  **Úsanos para "Micro-Tareas"**:
    -   *"Escribe un script en Python para analizar el XML de Jacoco y fallar si la cobertura < 80%."*
    -   *"Explica la etiqueta `<execution>` en Maven para Jacoco."*

---

### **Herramientas para Automatizar Flujos de Trabajo Complejos**
Dado que los LLM no pueden gestionar el estado, usa:
-   **Scripts de Shell** (por ejemplo, `setup_coverage.sh` para encadenar comandos de Maven/Python).
-   **Makefiles** (define `make test-coverage` para ejecutar todos los pasos).
-   **Plantillas de CI** (pipelines de GitHub Actions/Jenkins con pasos explícitos).
-   **Docker** (containeriza el entorno para evitar problemas de "funciona en mi máquina").

---

### **Conclusión Clave**
**Los LLM son como una página `man` superpoderosa o Stack Overflow con esteroides**—geniales para **piezas individuales**, pero no para orquestar sistemas completos. Para tareas complejas:
1.  **Divídelas**.
2.  **Verifica cada paso**.
3.  **Haz preguntas específicas**.

¿Te gustaría que profundice en alguno de los pasos anteriores (por ejemplo, el análisis de XML de Jacoco en Python o las configuraciones de Maven multi-módulo)?