---
audio: false
generated: true
lang: es
layout: post
title: Convenciones de Código de Oracle para el Lenguaje de Programación Java
translated: true
type: note
---

## 1. Organización de Archivos

### 1.1 Nombres de Archivos
- Los archivos fuente deben tener la extensión `.java`
- Los nombres de los archivos fuente deben coincidir exactamente con el nombre de la clase pública en el archivo
- Ejemplos:
  - `MyClass.java` contiene una clase pública llamada `MyClass`
  - `CircleShape.java` contiene una clase pública llamada `CircleShape`

### 1.2 Estructura de Archivos
1. Comentarios iniciales
2. Sentencia package
3. Sentencias import
4. Declaraciones de clase e interfaz

## 2. Formato y Sangría

### 2.1 Sangría
- Usar 4 espacios para la sangría (no tabs)
- Sangrar las líneas de continuación con 8 espacios
- Las llaves deben alinearse verticalmente

### 2.2 Longitud de Línea
- La longitud máxima de línea recomendada es de 80 caracteres
- Para sentencias largas, dividir las líneas en un nivel lógico superior

### 2.3 Ajuste de Líneas
- Dividir la línea antes de un operador
- Alinear la nueva línea con el inicio de la expresión en el mismo nivel

## 3. Comentarios

### 3.1 Comentarios de Archivo
- Cada archivo fuente debe comenzar con un bloque de comentarios:
  ```java
  /*
   * Nombre de la Clase
   * 
   * Información de la Versión
   * 
   * Fecha
   * 
   * Aviso de Copyright
   */
  ```

### 3.2 Comentarios de Implementación
- Usar `/* */` para comentarios multilínea
- Usar `//` para comentarios de una sola línea
- Los comentarios deben explicar el "porqué", no el "qué"

### 3.3 Comentarios de Documentación
- Usar comentarios estilo Javadoc para clases, interfaces, métodos
- Incluir:
  - Descripción breve
  - `@param` para parámetros del método
  - `@return` para valores de retorno
  - `@throws` para excepciones

## 4. Declaraciones

### 4.1 Número por Línea
- Una declaración por línea
- Recomendado:
  ```java
  int level;        // Correcto
  int size;         // Correcto
  
  // Evitar:
  int level, size;  // No recomendado
  ```

### 4.2 Inicialización
- Inicializar las variables en la declaración cuando sea posible
- Agrupar declaraciones relacionadas

## 5. Sentencias

### 5.1 Sentencias Simples
- Una sentencia por línea
- Usar un espacio después de las comas
- Usar espacios alrededor de los operadores

### 5.2 Sentencias Compuestas
- Las llaves se usan con las sentencias `if`, `else`, `for`, `while`, `do`, incluso para bloques de una sola línea

### 5.3 Sentencias Return
- Preferir return explícito
- Evitar `else` innecesario después de `return`

## 6. Convenciones de Nombrado

### 6.1 Nombres de Paquetes
- Todo en minúsculas
- Prefijo único, a menudo el dominio de la empresa invertido
- Ejemplo: `com.company.project`

### 6.2 Nombres de Clases
- UpperCamelCase
- Sustantivo o frase sustantiva
- Ejemplos: `DataProcessor`, `HttpClient`

### 6.3 Nombres de Interfaces
- Similares a los nombres de clases
- Considerar describir un comportamiento
- Ejemplos: `Runnable`, `Serializable`

### 6.4 Nombres de Métodos
- lowerCamelCase
- Verbo o frase verbal
- Ejemplos: `calculateTotal()`, `sendMessage()`

### 6.5 Nombres de Variables
- lowerCamelCase
- Significativos y descriptivos
- Evitar nombres de una sola letra excepto para variables temporales

### 6.6 Nombres de Constantes
- TODO_EN_MAYÚSCULAS con guiones bajos
- Ejemplo: `MAX_VALUE`, `COLOR_RED`

## 7. Prácticas de Programación

### 7.1 Visibilidad
- Usar la menor visibilidad posible
- Preferir `private` sobre `public`
- Usar métodos de acceso para los campos de clase

### 7.2 Alcance de Variables
- Declarar variables en el alcance más pequeño posible
- Inicializar variables cerca de su primer uso

### 7.3 Manejo de Excepciones
- Incluir siempre un mensaje en las excepciones
- Capturar excepciones específicas
- Usar try-catch-finally apropiadamente

## 8. Mejores Prácticas

### 8.1 Evitar Números Mágicos
- Usar constantes con nombre en lugar de números literales
- Mejorar la legibilidad y mantenibilidad del código

### 8.2 Preferir Inmutabilidad
- Usar `final` para variables que no cambian
- Crear clases inmutables cuando sea posible

## Conclusión
Estas convenciones tienen como objetivo mejorar la legibilidad, mantenibilidad y consistencia del código en los proyectos Java.