---
audio: false
generated: true
lang: es
layout: post
title: Procesamiento Javax Json
translated: true
type: note
---

Explicaré cómo usar el paquete `javax.json`, que forma parte de la API de Java para JSON Processing (JSON-P) para trabajar con datos JSON en Java. Aquí tienes una guía completa:

1. Primero, añade la dependencia a tu proyecto (si usas Maven):
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- Implementación (como GlassFish) -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. Ejemplos básicos de uso de `javax.json`:

a) Crear un objeto JSON:
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // Crear un objeto JSON
        JsonObject jsonObject = Json.createObjectBuilder()
            .add("name", "John Doe")
            .add("age", 30)
            .add("isStudent", false)
            .add("address", Json.createObjectBuilder()
                .add("street", "123 Main St")
                .add("city", "New York"))
            .build();

        System.out.println(jsonObject.toString());
    }
}
```

b) Crear un array JSON:
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) Analizar JSON desde una cadena:
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// Acceder a los valores
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) Escribir JSON a una cadena:
```java
import javax.json.JsonWriter;
import java.io.StringWriter;

JsonObject jsonObject = Json.createObjectBuilder()
    .add("title", "Example")
    .build();

StringWriter stringWriter = new StringWriter();
JsonWriter jsonWriter = Json.createWriter(stringWriter);
jsonWriter.writeObject(jsonObject);
jsonWriter.close();

String result = stringWriter.toString();
```

3. Clases e Interfaces Clave:
- `Json`: Clase factory para crear constructores y lectores JSON
- `JsonObject`: Representa un objeto JSON
- `JsonArray`: Representa un array JSON
- `JsonObjectBuilder`: Construye objetos JSON
- `JsonArrayBuilder`: Construye arrays JSON
- `JsonReader`: Lee JSON desde una fuente de entrada
- `JsonWriter`: Escribe JSON a una fuente de salida

4. Manejo de diferentes tipos de valores JSON:
```java
JsonObject obj = // ... algún objeto JSON
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// Verificar si la clave existe y manejar null
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. Ejemplo de API de streaming (para JSON grande):
```java
import javax.json.stream.JsonParser;
import java.io.StringReader;

String json = "{\"name\":\"John\",\"scores\":[1,2,3]}";
JsonParser parser = Json.createParser(new StringReader(json));
while (parser.hasNext()) {
    JsonParser.Event event = parser.next();
    switch (event) {
        case KEY_NAME:
            System.out.println("Clave: " + parser.getString());
            break;
        case VALUE_STRING:
            System.out.println("Cadena: " + parser.getString());
            break;
        case VALUE_NUMBER:
            System.out.println("Número: " + parser.getBigDecimal());
            break;
    }
}
parser.close();
```

Consejos:
- Siempre cierra `JsonReader`, `JsonWriter` y `JsonParser` cuando termines
- Maneja `javax.json.JsonException` para posibles errores de análisis
- Usa la API de streaming (`JsonParser`) para documentos JSON grandes
- La API es inmutable - los constructores crean nuevas instancias

Esto cubre lo básico del uso de `javax.json`. ¡Déjame saber si necesitas ejemplos más específicos o tienes un caso de uso particular en mente!