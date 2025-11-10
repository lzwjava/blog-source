---
audio: false
generated: true
lang: es
layout: post
title: Plantillas de Reemplazo Estructural de IntelliJ
translated: true
type: note
---

Aquí hay 10 ejemplos de plantillas de Reemplazo Estructural de IntelliJ, categorizados para mayor claridad. Estas pueden ser increíblemente poderosas para refactorizar, hacer cumplir estándares de código y automatizar transformaciones de código comunes.

**Refactorización y Simplificación Básica:**

1.  **Reemplazar `if (condition) return true; else return false;` con `return condition;`**

      * **Plantilla de Búsqueda:**
        ```java
        if ($CONDITION$) {
            return true;
        } else {
            return false;
        }
        ```
      * **Plantilla de Reemplazo:**
        ```java
        return $CONDITION$;
        ```
      * **Contexto:** Simplifica sentencias booleanas de retorno.

2.  **Reemplazar `if (condition) { statement; }` con `if (!condition) { continue/break/return; }` (Cláusula de Guarda)**

      * **Plantilla de Búsqueda:**
        ```java
        if ($CONDITION$) {
            $STATEMENTS$;
        }
        ```
      * **Plantilla de Reemplazo:** (Esta es más una sugerencia de transformación, normalmente ajustarías manualmente la parte interna)
        ```java
        if (!$CONDITION$) {
            // Considera usar continue, break o return aquí
        }
        $STATEMENTS$;
        ```
      * **Contexto:** Fomenta el uso de cláusulas de guarda para un flujo de código más limpio. Normalmente usarías una acción "Reemplazar con" después de encontrar la estructura.

**Operaciones con Colecciones y Streams:**

3.  **Reemplazar `for (Type item : collection) { if (item.getProperty() == value) { ... } }` con Stream `filter`**

      * **Plantilla de Búsqueda:**
        ```java
        for ($TYPE$ $ITEM$ : $COLLECTION$) {
            if ($ITEM$.$METHOD$($VALUE$)) {
                $STATEMENTS$;
            }
        }
        ```
      * **Plantilla de Reemplazo:**
        ```java
        $COLLECTION$.stream()
            .filter($ITEM$ -> $ITEM$.$METHOD$($VALUE$))
            .forEach($ITEM$ -> $STATEMENTS$); // O .map().collect(), etc.
        ```
      * **Contexto:** Migrar de bucles tradicionales a Java Streams para filtrado. Este es un ejemplo general; es probable que necesites plantillas más específicas para `map`, `collect`, etc.

4.  **Reemplazar `new ArrayList<>().add(item1); new ArrayList<>().add(item2);` con `List.of(item1, item2);`**

      * **Plantilla de Búsqueda:** (Esto podría requerir múltiples plantillas para distinto número de llamadas `add`, o un regex más complejo. Un enfoque simple para 2 elementos):
        ```java
        java.util.ArrayList<$TYPE$> $LIST$ = new java.util.ArrayList<>();
        $LIST$.add($ITEM1$);
        $LIST$.add($ITEM2$);
        ```
      * **Plantilla de Reemplazo:**
        ```java
        java.util.List<$TYPE$> $LIST$ = java.util.List.of($ITEM1$, $ITEM2$);
        ```
      * **Contexto:** Usar `List.of()` de Java 9+ para listas inmutables.

**Manejo de Errores y Gestión de Recursos:**

5.  **Reemplazar `try { ... } catch (Exception e) { e.printStackTrace(); }` con un registro (logging) más específico**

      * **Plantilla de Búsqueda:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            $EXCEPTION$.printStackTrace();
        }
        ```
      * **Plantilla de Reemplazo:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            // Reemplaza con tu framework de logging preferido, ej.:
            // logger.error("Ocurrió un error", $EXCEPTION$);
            throw new RuntimeException($EXCEPTION$); // O relanza una excepción específica
        }
        ```
      * **Contexto:** Fomenta un registro de errores adecuado en lugar de solo imprimir trazas de pila.

6.  **Reemplazar `try { ... } finally { closeable.close(); }` con `try-with-resources`**

      * **Plantilla de Búsqueda:**
        ```java
        java.io.Closeable $CLOSEABLE$ = null;
        try {
            $CLOSEABLE$ = $INITIALIZATION$;
            $STATEMENTS$;
        } finally {
            if ($CLOSEABLE$ != null) {
                $CLOSEABLE$.close();
            }
        }
        ```
      * **Plantilla de Reemplazo:**
        ```java
        try ($CLOSEABLE$ = $INITIALIZATION$) {
            $STATEMENTS$;
        }
        ```
      * **Contexto:** Modernizar la gestión de recursos para usar `try-with-resources` (Java 7+).

**Estructura de Clases y Métodos:**

7.  **Encontrar campos que pueden ser `final`**

      * **Plantilla de Búsqueda:**
        ```java
        class $CLASS$ {
            $TYPE$ $FIELD$;
        }
        ```
      * **Plantilla de Reemplazo:** (Esto es más para encontrar, y luego usar una corrección rápida)
        ```java
        class $CLASS$ {
            // Considera hacer esto final si solo se asigna una vez
            final $TYPE$ $FIELD$;
        }
        ```
      * **Contexto:** Identificar oportunidades para mejorar la inmutabilidad. Configurarías un filtro para mostrar solo campos sin múltiples asignaciones.

8.  **Reemplazar `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);` con una utilidad de logger personalizada**

      * **Plantilla de Búsqueda:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = org.slf4j.LoggerFactory.getLogger($CLASS_NAME$.class);
        ```
      * **Plantilla de Reemplazo:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = com.yourcompany.util.LoggerProvider.getLogger(); // O un getLogger($CLASS_NAME$.class) más específico de tu utilidad
        ```
      * **Contexto:** Hacer cumplir un patrón de inicialización de logging específico en tu base de código.

**Anotaciones y Código Repetitivo (Boilerplate):**

9.  **Agregar `@Override` a métodos que sobrescriben métodos de la superclase (si falta)**

      * **Plantilla de Búsqueda:** (Esto es más complejo y a menudo se maneja mejor con las inspecciones integradas de IntelliJ, pero para demostración)
        ```java
        class $CLASS$ {
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **Plantilla de Reemplazo:** (De nuevo, para encontrar y luego aplicar una corrección rápida)
        ```java
        class $CLASS$ {
            @Override // Agregar si sobrescribe un método de la superclase
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **Contexto:** Hacer cumplir las buenas prácticas y detectar errores tipográficos. Usarías un filtro para verificar si el método existe en una superclase/interfaz.

10. **Reemplazar métodos `getter/setter` repetitivos con anotaciones de Lombok**

      * **Plantilla de Búsqueda:** (Para un solo getter, esto sería muy repetitivo para una clase)
        ```java
        public $TYPE$ get$PROPERTY_NAME$() {
            return this.$FIELD_NAME$;
        }
        ```
      * **Plantilla de Reemplazo:** (Esto es conceptual, ya que eliminarías el getter y agregarías `@Getter` al campo o clase)
        ```java
        // Considera reemplazar con @lombok.Getter en el campo:
        // @lombok.Getter
        // private $TYPE$ $FIELD_NAME$;
        ```
      * **Contexto:** Automatizar la transición a Lombok. Para una clase completa, podrías apuntar a la clase misma y sugerir anotaciones `@Data` o `@Getter/@Setter` basándote en la presencia de estos métodos. Esta es una de las transformaciones más avanzadas y potencialmente de múltiples pasos.

**Cómo Usarlas en IntelliJ:**

1.  Ve a `Analyze` -> `Inspect Code...`
2.  En la ventana `Inspection Profile`, haz clic en los `...` junto al nombre del perfil para editarlo.
3.  Navega a `Java` -> `General` -> `Structural Search Inspection`.
4.  Haz clic en el botón `+` para agregar una nueva plantilla de búsqueda/reemplazo.
5.  Define tu `Plantilla de Búsqueda` y `Plantilla de Reemplazo`.
6.  Usa la pestaña `Variables` para definir restricciones para tus variables (ej., tipo, texto, conteo).
7.  Ejecuta la inspección en tu código. IntelliJ sugerirá reemplazos o resaltará hallazgos.

Estos ejemplos demuestran la versatilidad de la Búsqueda y Reemplazo Estructural. Cuanto más específicas y restringidas sean tus plantillas, más precisos y útiles serán los reemplazos.