---
audio: false
generated: true
lang: fr
layout: post
title: Traitement JSON en Java
translated: true
type: note
---

Pour utiliser le package `com.fasterxml.jackson` dans un projet Java pour le traitement JSON, vous pouvez exploiter la bibliothèque Jackson, qui est largement utilisée pour convertir des objets Java en JSON et vice versa. Voici un guide étape par étape pour commencer, en supposant que vous travaillez avec un projet basé sur Maven. Ce guide se concentre sur le module `jackson-databind`, qui fournit des fonctionnalités de haut niveau pour la databinding JSON.

---

### 1. Ajouter la dépendance Jackson à votre projet
Pour utiliser le package `com.fasterxml.jackson`, vous devez inclure la bibliothèque Jackson dans votre projet. Si vous utilisez Maven, ajoutez la dépendance suivante à votre fichier `pom.xml` :

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- Remplacer par la dernière version -->
</dependency>
```

- **Note** : Vérifiez le [Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) pour la dernière version, car elle peut être plus récente que 2.12.5.
- Le module `jackson-databind` dépend de `jackson-core` et `jackson-annotations`, donc vous n'avez pas besoin de les ajouter séparément sauf si vous avez des besoins spécifiques.

Après avoir ajouté la dépendance, exécutez `mvn install` ou actualisez votre projet dans votre IDE pour télécharger la bibliothèque.

---

### 2. Créer une instance `ObjectMapper`
La classe `ObjectMapper` du package `com.fasterxml.jackson.databind` est l'outil principal pour les opérations JSON. Elle est thread-safe et coûteuse en ressources à instancier, il est donc préférable de créer une seule instance réutilisable :

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

Placez ceci dans une classe où vous effectuerez les opérations JSON.

---

### 3. Convertir un objet Java en JSON (Sérialisation)
Pour convertir un objet Java en une chaîne JSON, utilisez la méthode `writeValueAsString`. Voici un exemple :

#### Définir une classe Java
Créez une classe avec les champs que vous souhaitez sérialiser. Assurez-vous qu'elle a des getters et des setters, car Jackson les utilise par défaut pour accéder aux champs privés :

```java
public class MyClass {
    private String field1;
    private int field2;

    public MyClass(String field1, int field2) {
        this.field1 = field1;
        this.field2 = field2;
    }

    public String getField1() {
        return field1;
    }

    public void setField1(String field1) {
        this.field1 = field1;
    }

    public int getField2() {
        return field2;
    }

    public void setField2(int field2) {
        this.field2 = field2;
    }
}
```

#### Sérialiser en JSON
Utilisez `ObjectMapper` pour convertir l'objet en JSON :

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        MyClass obj = new MyClass("value1", 123);
        String json = mapper.writeValueAsString(obj);
        System.out.println(json);
    }
}
```

**Sortie** :
```json
{"field1":"value1","field2":123}
```

---

### 4. Convertir JSON en objet Java (Désérialisation)
Pour convertir une chaîne JSON en objet Java, utilisez la méthode `readValue` :

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // Affiche "value1"
    }
}
```

- **Gestion des erreurs** : La méthode `readValue` lance une `JsonProcessingException` (une exception vérifiée) si le JSON est mal formé ou ne correspond pas à la structure de la classe. Gérez-la avec un bloc try-catch ou déclarez-la dans la signature de la méthode :

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. Personnaliser le traitement JSON avec des annotations
Jackson fournit des annotations pour personnaliser la façon dont les champs sont sérialisés ou désérialisés. Ajoutez ces annotations de `com.fasterxml.jackson.annotation` à votre classe :

#### Renommer un champ
Utilisez `@JsonProperty` pour mapper un champ Java à un nom de champ JSON différent :

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // Constructeur, getters, setters
}
```

**Sortie** :
```json
{"name":"value1","field2":123}
```

#### Ignorer un champ
Utilisez `@JsonIgnore` pour exclure un champ de la sérialisation :

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // Constructeur, getters, setters
}
```

**Sortie** :
```json
{"field1":"value1"}
```

#### Formater les dates
Utilisez `@JsonFormat` pour spécifier comment les dates sont sérialisées :

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // Constructeur, getters, setters
}
```

**Sortie** (exemple) :
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. Gérer les scénarios avancés
Voici quelques fonctionnalités supplémentaires que vous pourriez trouver utiles :

#### Afficher le JSON de manière lisible
Pour une sortie JSON lisible, utilisez `writerWithDefaultPrettyPrinter` :

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**Sortie** :
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### Ignorer les propriétés inconnues
Si le JSON contient des champs absents de votre classe Java, configurez `ObjectMapper` pour les ignorer :

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### Travailler avec des fichiers
Lire depuis ou écrire dans un fichier :

```java
// Écrire dans un fichier
mapper.writeValue(new File("output.json"), obj);

// Lire depuis un fichier
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### Gérer les listes ou les génériques
Pour les collections, utilisez `TypeReference` pour préserver les informations de type générique :

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. Manipulation dynamique de JSON avec `JsonNode`
Si vous ne souhaitez pas mapper le JSON à une classe spécifique, utilisez `JsonNode` pour une approche basée sur un arbre :

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // Retourne "value1"
```

Vous pouvez également construire du JSON dynamiquement :

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### Résumé
Pour utiliser le package `com.fasterxml.jackson` :
1. Ajoutez la dépendance `jackson-databind` à votre `pom.xml`.
2. Créez une seule instance `ObjectMapper` pour la réutiliser.
3. Utilisez `writeValueAsString` pour convertir les objets Java en JSON et `readValue` pour convertir le JSON en objets Java.
4. Personnalisez le comportement avec des annotations comme `@JsonProperty`, `@JsonIgnore` et `@JsonFormat`.
5. Gérez les exceptions (par exemple, `JsonProcessingException`) et configurez `ObjectMapper` pour des besoins spécifiques (par exemple, ignorer les propriétés inconnues).
6. Explorez les fonctionnalités avancées comme l'impression lisible, les E/S de fichiers, ou `JsonNode` pour la manipulation dynamique de JSON.

Avec ces étapes, vous pouvez traiter efficacement le JSON dans votre application Java en utilisant la bibliothèque Jackson.