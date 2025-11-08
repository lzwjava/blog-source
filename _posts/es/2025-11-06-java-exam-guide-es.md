---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía de Estudio para el Examen de Programación en Java
translated: true
type: note
---

Aquí tienes una guía práctica y orientada al examen para la **primera parte de "08553 Introducción a la Programación—Java"**, basada en el plan de estudios del *Examen Nacional de Autoevaluación de Educación Superior de China*. Se centra en conceptos, ejemplos y puntos clave que los principiantes deben dominar.

---

## 1. Visión General del Lenguaje Java

### 1.1 Características de Java

* **Independencia de la Plataforma:** El código Java se compila en *bytecode*, que se ejecuta en cualquier dispositivo con una *Máquina Virtual Java (JVM)* — "Escribe una vez, ejecuta en cualquier lugar".
* **Orientado a Objetos:** Admite *encapsulación, herencia* y *polimorfismo*.
* **Seguro y Robusto:** La gestión automática de memoria (recolección de basura) y la fuerte verificación de tipos reducen los errores.
* **Multihilo:** Admite la ejecución concurrente de múltiples tareas.
* **Librería Estándar Rica (API):** Incluye clases predefinidas para matemáticas, cadenas, archivos, redes, etc.

### 1.2 Versiones y Componentes de Java

* **JDK (Kit de Desarrollo de Java):** Para desarrolladores — incluye el compilador (`javac`), la JVM y herramientas de desarrollo.
* **JRE (Entorno de Ejecución de Java):** Para usuarios finales — incluye JVM + librerías principales.
* **API (Interfaz de Programación de Aplicaciones):** Las librerías de clases integradas de Java, como `java.lang`, `java.util`, `java.io`, etc.

---

## 2. Herramientas de Desarrollo Java (IDE y CLI)

### 2.1 IDEs Comunes

Para el examen, solo necesitas saber su propósito:

* **Eclipse, IntelliJ IDEA, NetBeans:** Se utilizan para escribir, compilar y ejecutar código Java fácilmente.

### 2.2 Flujo de Trabajo por Línea de Comandos

Pasos típicos de compilación y ejecución:

1. **Escribe** tu código en un archivo `.java`, ej. `Hola.java`
2. **Compílalo**:

   ```bash
   javac Hola.java
   ```

   → Produce `Hola.class` (archivo de bytecode)
3. **Ejecútalo**:

   ```bash
   java Hola
   ```

   (Sin la extensión `.class` al ejecutar)

### 2.3 Ejemplo Sencillo

```java
public class Hola {
    public static void main(String[] args) {
        System.out.println("¡Hola, Java!");
    }
}
```

---

## 3. Guías de Estilo de Programación

### 3.1 Convenciones de Nomenclatura

* **Clases:** `CamelCase`, primera letra en mayúscula → `InformacionEstudiante`
* **Variables y Métodos:** `camelCase`, comienzan en minúscula → `nombreEstudiante`, `calcularPuntaje()`
* **Constantes:** Todas en mayúsculas con guiones bajos → `TAMANIO_MAX`

### 3.2 Indentación y Comentarios

* Usa **indentación consistente** (4 espacios es lo típico).
* Escribe **comentarios** claros:

  ```java
  // Este es un comentario de una sola línea
  /* Este es un comentario
     de múltiples líneas */
  ```

### 3.3 Estructura del Código

Sigue una agrupación lógica y legibilidad:

* Cada archivo contiene **una clase pública** con el **mismo nombre** que el archivo.
* Mantén las líneas cortas y significativas; una declaración por línea.

---

## 4. Errores de Programación Comunes y Conceptos Básicos de Depuración

### 4.1 Errores de Sintaxis

Detectados por el compilador:

* Falta el punto y coma `;`
* Llaves `{ }` no coincidentes
* Capitalización incorrecta (Java **distingue entre mayúsculas y minúsculas**)

  ```java
  System.out.println("Hola"); // correcto
  system.out.println("Hola"); // error
  ```

### 4.2 Errores en Tiempo de Ejecución

Ocurren mientras se ejecuta el programa:

* División por cero
* Índice de array fuera de límites
* Excepciones de puntero nulo

### 4.3 Errores Lógicos

El programa se ejecuta pero da una salida incorrecta.
→ Usa **declaraciones de impresión** o **herramientas de depuración** en los IDEs para rastrear los valores de las variables paso a paso.

---

## 5. Puntos Clave para el Examen

* Comprende las funciones y diferencias de **JDK, JRE, JVM**.
* Saber **compilar y ejecutar** Java tanto desde el IDE como desde la línea de comandos.
* Recordar las **reglas básicas de sintaxis** y **estándares de estilo**.
* Ser capaz de **identificar errores comunes** y explicar sus causas.
* Practicar escribiendo pequeños programas que:

  * Impriman mensajes
  * Usen variables y expresiones
  * Sigan la estructura y nomenclatura correctas

---

## 6. Pregunta de Muestra al Estilo de Examen

**Ejemplo 1:**

> ¿Cuál de las siguientes afirmaciones sobre Java es *incorrecta*?
> A. Java admite la independencia de la plataforma a través del bytecode
> B. Los programas Java siempre deben compilarse en código máquina nativo
> C. La JVM ejecuta el bytecode compilado
> D. Los programas Java pueden ejecutarse en cualquier sistema con una JVM instalada

**Respuesta:** B

**Ejemplo 2:**

> ¿Qué comando compila un archivo fuente Java llamado `Prueba.java`?
> A. java Prueba
> B. javac Prueba.java
> C. run Prueba
> D. compile Prueba

**Respuesta:** B

---

¿Te gustaría que continúe con **Parte II: Sintaxis Básica y Tipos de Datos** a continuación (la siguiente sección principal en este curso)? Seguirá la misma estructura clara y orientada al examen.