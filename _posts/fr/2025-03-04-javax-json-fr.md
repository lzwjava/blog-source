---
audio: false
generated: true
lang: fr
layout: post
title: Traitement JSON Javax
translated: true
type: note
---

Je vais expliquer comment utiliser le package `javax.json`, qui fait partie de l'API Java pour le traitement JSON (JSON-P) pour travailler avec des données JSON en Java. Voici un guide complet :

1. D'abord, ajoutez la dépendance à votre projet (si vous utilisez Maven) :
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- Implémentation (comme GlassFish) -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. Exemples de base d'utilisation de `javax.json` :

a) Créer un objet JSON :
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // Créer un objet JSON
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

b) Créer un tableau JSON :
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) Analyser JSON à partir d'une chaîne :
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// Accéder aux valeurs
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) Écrire JSON en chaîne :
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

3. Classes et interfaces clés :
- `Json` : Classe factory pour créer des builders et readers JSON
- `JsonObject` : Représente un objet JSON
- `JsonArray` : Représente un tableau JSON
- `JsonObjectBuilder` : Construit des objets JSON
- `JsonArrayBuilder` : Construit des tableaux JSON
- `JsonReader` : Lit JSON depuis une source d'entrée
- `JsonWriter` : Écrit JSON vers une source de sortie

4. Gestion des différents types de valeurs JSON :
```java
JsonObject obj = // ... un objet JSON
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// Vérifier si la clé existe et gérer null
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. Exemple d'API streaming (pour JSON volumineux) :
```java
import javax.json.stream.JsonParser;
import java.io.StringReader;

String json = "{\"name\":\"John\",\"scores\":[1,2,3]}";
JsonParser parser = Json.createParser(new StringReader(json));
while (parser.hasNext()) {
    JsonParser.Event event = parser.next();
    switch (event) {
        case KEY_NAME:
            System.out.println("Clé : " + parser.getString());
            break;
        case VALUE_STRING:
            System.out.println("Chaîne : " + parser.getString());
            break;
        case VALUE_NUMBER:
            System.out.println("Nombre : " + parser.getBigDecimal());
            break;
    }
}
parser.close();
```

Conseils :
- Toujours fermer `JsonReader`, `JsonWriter` et `JsonParser` quand vous avez terminé
- Gérez `javax.json.JsonException` pour les erreurs d'analyse potentielles
- Utilisez l'API streaming (`JsonParser`) pour les documents JSON volumineux
- L'API est immuable - les builders créent de nouvelles instances

Ceci couvre les bases de l'utilisation de `javax.json`. Faites-moi savoir si vous avez besoin d'exemples plus spécifiques ou si vous avez un cas d'utilisation particulier en tête !