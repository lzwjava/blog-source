---
audio: false
generated: true
lang: es
layout: post
title: Guía de Estilo de Java de Google
translated: true
type: note
---

## 1. Conceptos Básicos de Archivos Fuente
- **Nomenclatura de Archivos**:
  - Los archivos fuente se nombran con el nombre, sensible a mayúsculas y minúsculas, de la clase de nivel superior que contienen
  - Los archivos deben usar codificación UTF-8
  - Se desaconseja el uso de caracteres especiales en los nombres de archivo

## 2. Estructura del Archivo Fuente
### Organización del Archivo Fuente
1. Sentencia del paquete
2. Sentencias de importación
3. Exactamente una clase de nivel superior

### Reglas de las Sentencias de Importación
- No usar importaciones con comodín (`*`)
- Las importaciones estáticas están permitidas
- Las importaciones se organizan en un orden específico:
  - Todas las importaciones estáticas
  - Todas las importaciones no estáticas
  - Las importaciones dentro de cada grupo se ordenan alfabéticamente

## 3. Pautas de Formato

### Sangría y Llaves
- Usar 2 espacios para la sangría (no tabs)
- Las llaves se usan con las sentencias `if`, `else`, `for`, `do` y `while`, incluso para bloques de una sola línea
- Se recomienda el estilo K&R para la colocación de llaves
  ```java
  public void method() {
    if (condition) {
      // Bloque de código
    }
  }
  ```

### Longitud de Línea y Ajuste
- La longitud máxima de línea es de 100 caracteres
- Se prefieren los saltos de línea en divisiones sintácticas de nivel superior
- Al romper cadenas de llamadas a métodos, la ruptura ocurre antes del `.`

## 4. Convenciones de Nomenclatura

### Reglas Generales
- **Paquetes**: Minúsculas, sin guiones bajos
- **Clases**: UpperCamelCase
- **Métodos**: lowerCamelCase
- **Constantes**: UPPER_SNAKE_CASE
- **Campos no constantes**: lowerCamelCase
- **Parámetros**: lowerCamelCase
- **Variables Locales**: lowerCamelCase

### Prácticas Específicas de Nomenclatura
- Evitar abreviaturas
- Los nombres de excepción deben terminar con `Exception`
- Las clases de prueba se nombran `TestClassName`

## 5. Prácticas de Programación

### Reglas del Lenguaje Java
- **Excepciones**:
  - Capturar excepciones específicas
  - Evitar bloques `catch` vacíos
  - Incluir siempre un mensaje de error detallado
- **Palabra Clave Final**:
  - Usar `final` para los parámetros de método
  - Preferir objetos inmutables
- **Anotaciones**:
  - `@Override` es obligatorio para métodos que sobrescriben
  - Usar las anotaciones estándar apropiadamente

### Estructura del Código
- Preferir la composición sobre la herencia
- Mantener los métodos cortos y enfocados
- Una sentencia por línea
- Evitar el anidamiento profundo de condicionales

## 6. Comentarios y Documentación

### Pautas para Javadoc
- Todas las clases y métodos públicos deben tener Javadoc
- Los comentarios de Javadoc comienzan con `/**`
- Incluir descripción, parámetros, valores de retorno y excepciones
- Usar las etiquetas `@param`, `@return`, `@throws`

### Comentarios en Línea
- Usar con moderación
- Explicar el "porqué", no el "qué"
- Mantener los comentarios concisos y significativos

## 7. Consideraciones de Control de Versiones
- Evitar confirmar código comentado
- Usar las funciones del sistema de control de versiones en lugar de comentarios en el código para rastrear cambios

## 8. Consideraciones de Rendimiento
- Preferir bucles `for` mejorados
- Usar `StringBuilder` para la concatenación de cadenas
- Cerrar recursos usando try-with-resources
- Evitar crear objetos innecesarios

## 9. Principios de Pruebas
- Escribir pruebas unitarias
- Aspirar a una alta cobertura de código
- Usar JUnit para las pruebas
- Simular (mock) dependencias externas
- Probar casos límite y condiciones de error

## 10. Herramientas Adicionales
- Google proporciona un formateador de Java y herramientas de análisis estático
- Se pueden usar CheckStyle y Error Prone para hacer cumplir las pautas de estilo

## Conclusión
La Guía de Estilo de Java de Google proporciona un conjunto completo de pautas para garantizar código Java consistente, legible y mantenible en todos los proyectos.