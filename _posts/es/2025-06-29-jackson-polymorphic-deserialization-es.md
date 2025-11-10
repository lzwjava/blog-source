---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Descripción General de la Deserialización Polimórfica de Jackson
translated: true
type: note
---

### Descripción General de la Deserialización Polimórfica de Jackson

Jackson es una librería Java para la serialización y deserialización de JSON. La deserialización polimórfica permite a Jackson instanciar automáticamente la subclase correcta de una clase base durante la deserialización, basándose en la información de tipo incrustada en el JSON. Esto es útil cuando se trabaja con jerarquías de herencia, asegurando que se cree el tipo de objeto correcto a partir de los datos JSON.

Componentes clave:
- **@JsonTypeInfo**: Anotaciones que controlan dónde y cómo se almacena la información de tipo en el JSON.
- **@JsonSubTypes**: Anotaciones que enumeran las subclases (subtipos) y sus identificadores.
- La resolución de subtipos de Jackson maneja el mapeo.

Sin estas anotaciones, Jackson por defecto deserializaría todos los objetos como la clase base, perdiendo potencialmente datos específicos de la subclase.

### Cómo Funciona Paso a Paso

1. **Anotaciones en la Clase Base**:
   - Usa `@JsonTypeInfo` para especificar dónde se incrusta la información de tipo (por ejemplo, como una propiedad en el objeto JSON).
   - Ejemplo:
     ```java
     @JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "@type")
     @JsonSubTypes({
         @JsonSubType(value = Cat.class, name = "cat"),
         @JsonSubType(value = Dog.class, name = "dog")
     })
     public abstract class Animal {
         public String name;
     }
     ```
     - `use = JsonTypeInfo.Id.NAME`: Usa un nombre (identificador de cadena) para el tipo.
     - `include = JsonTypeInfo.As.PROPERTY`: Añade la información de tipo como una propiedad ("@type") en el objeto JSON.
     - `@JsonSubTypes`: Mapea los nombres de las subclases a sus clases Java (por ejemplo, "cat" → Cat.class).

2. **Proceso de Serialización**:
   - Al serializar un objeto Cat o Dog, Jackson añade el identificador de tipo al JSON.
   - Salida de ejemplo: `{"@type": "cat", "name": "Whiskers", "purr": true}` (si Cat tiene un campo "purr").

3. **Proceso de Deserialización**:
   - Jackson lee el JSON y verifica la información de tipo (por ejemplo, la propiedad "@type").
   - Mapea el identificador ("cat") de vuelta a la subclase registrada (Cat.class) usando `@JsonSubTypes`.
   - Instancia la subclase correcta y popula sus campos.
   - Si no hay coincidencia o falta la información de tipo, por defecto usa la clase base o lanza excepciones (configurable via `defaultImpl`).

4. **Formatos de Información de Tipo Soportados**:
   - `@JsonTypeInfo.As.PROPERTY`: El tipo como un campo (por ejemplo, `{"@type": "cat", ...}`).
   - `@JsonTypeInfo.As.WRAPPER_OBJECT`: Envuelve el objeto en un contenedor con el tipo como clave (por ejemplo, `{"cat": {...}}`).
   - `@JsonTypeInfo.As.WRAPPER_ARRAY`: Usa un formato de array.
   - `@JsonTypeInfo.As.EXTERNAL_PROPERTY`: Información de tipo en un campo separado (avanzado, para estructuras similares a XML).

### Configuración Avanzada y Casos Límite

- **Mapeadores de Nombres Personalizados**: Usa `@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)` para incrustar el nombre de clase completamente calificado directamente en el JSON (por ejemplo, `{"@class": "com.example.Cat", ...}`), lo que puede ser frágil durante refactorizaciones.
- **Implementación por Defecto**: Añade `defaultImpl = Animal.class` para retroceder si falta la información de tipo.
- **Visibilidad y Mix-Ins**: Aplica anotaciones a través de clases mix-in si no puedes modificar las clases fuente.
- **Manejo de Errores**: Si la información de tipo no coincide con un subtipo registrado, Jackson lanza una `JsonMappingException`. Esto se puede manejar con deserializadores personalizados.
- **Rendimiento**: Sobrecarga mínima durante la deserialización debido a búsquedas eficientes, pero incrustar información de tipo aumenta el tamaño de la carga útil JSON.

Para documentación completa, consulta la guía oficial de Jackson: [Polymorphic Type Handling](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization). Esta característica ha sido estable desde Jackson 2.x, con conceptos similares en otras librerías JSON como Gson. Si necesitas personalizar más, extiende `PolymorphicTypeValidator` para seguridad en entradas no confiables.