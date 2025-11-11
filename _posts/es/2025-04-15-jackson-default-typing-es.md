---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Explicación del Tipado Predeterminado de Jackson
translated: true
type: note
---

### ¿Qué es la Tipificación Predeterminada en ObjectMapper de Jackson?

El `ObjectMapper` de Jackson es una clase central en la biblioteca Jackson JSON para Java, responsable de serializar objetos Java a JSON y deserializar JSON de vuelta a objetos. La "tipificación predeterminada" es una característica que mejora el manejo de tipos polimórficos (por ejemplo, cuando un campo puede contener diferentes subclases). Funciona incrustando información de tipo en la salida JSON durante la serialización, la cual el mapper utiliza durante la deserialización para crear una instancia de la clase concreta correcta.

Sin la tipificación predeterminada, Jackson depende del tipo declarado (por ejemplo, una clase base abstracta o una interfaz), y podrías necesitar una configuración personalizada como anotaciones `@JsonTypeInfo` para especificar subtipos. Habilitar la tipificación predeterminada proporciona un respaldo global o semi-global para el polimorfismo, particularmente útil para colecciones o mapas con tipos mixtos.

### ¿Cómo Funciona?

Habilitar la tipificación predeterminada modifica el proceso de serialización:
1.  **Serialización**: Al serializar un grafo de objetos, Jackson agrega un campo especial `@class` o metadatos similares al JSON para indicar el tipo de tiempo de ejecución de los objetos polimórficos. Esto ocurre solo para tipos donde el tipo declarado no especifica completamente la clase concreta (por ejemplo, una `List` que contiene objetos `String` e `Integer`, o campos de clase abstracta).

2.  **Deserialización**: Durante la deserialización, el mapper utiliza esta información de tipo incrustada para buscar y crear una instancia de la clase exacta. Aprovecha la `TypeFactory` de Jackson para resolver tipos dinámicamente.

Para habilitarla, llamas a uno de estos métodos en una instancia de `ObjectMapper`:
- `mapper.enableDefaultTyping()`: Un método obsoleto que habilita la inclusión de tipificación polimórfica de tiempo constante (susceptible a problemas de seguridad).
- `mapper.activateDefaultTyping(ObjectMapper.DefaultTyping policy)`: Una alternativa más segura y recomendada, introducida en Jackson 2.10. Permite especificar un valor de enumeración `DefaultTyping`, como:
  - `JAVA_LANG_OBJECT`: Incluye tipificación para todas las referencias `Object`.
  - `NON_CONCRETE_AND_ARRAYS`: Incluye tipificación para tipos abstractos/no concretos y arrays.
  - `NON_FINAL`: Incluye tipificación para clases no finales.

Ejemplo de uso:
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import static com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping;

ObjectMapper mapper = new ObjectMapper();
mapper.activateDefaultTyping(DefaultTyping.NON_CONCRETE_AND_ARRAYS);
```

Sin habilitarla, si serializas una `List<Object>` con tipos mixtos, el JSON podría omitir los detalles de tipo, lo que lleva a errores de deserialización. Con ella habilitada, el JSON incluye pistas de tipo, por ejemplo: `[{"@class": "java.lang.String", "value": "hello"}, {"@class": "java.lang.Integer", "value": 42}]`.

### Consideraciones de Seguridad y Limitaciones

-   **Vulnerabilidades**: Habilitar la tipificación predeterminada a ciegas (especialmente el antiguo `enableDefaultTyping()`) puede exponer los sistemas a ataques como la extracción de datos, ya que permite deserializar clases arbitrarias mediante JSON manipulado. Jackson limita esto por defecto en versiones más recientes, permitiendo solo tipos comunes a menos que se personalice.
-   **Adecuación al Caso de Uso**: Es mejor para entornos confiables con datos polimórficos (por ejemplo, APIs internas). Para APIs públicas, prefiere anotaciones de tipo explícitas o serializadores/deserializadores personalizados para una mejor seguridad.
-   **Rendimiento**: Añade una sobrecarga menor debido a la información de tipo incrustada, lo que aumenta el tamaño del JSON.

Si esto se relaciona con un "object mapper" diferente (por ejemplo, el de Elasticsearch u otra biblioteca), proporciona más contexto para una explicación adaptada. Para más detalles, consulta la documentación oficial de Jackson.