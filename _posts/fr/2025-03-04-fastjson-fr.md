---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de FastJson
translated: true
---

FastJSON est une bibliothèque de traitement JSON haute performance pour Java, développée par Alibaba. Elle est largement utilisée pour analyser des chaînes JSON en objets Java, sérialiser des objets Java en JSON et gérer les données JSON de manière efficace. Voici un guide sur la manière d'utiliser FastJSON en fonction de ses fonctionnalités principales.

### Étape 1: Ajouter FastJSON à votre projet
Pour utiliser FastJSON, vous devez l'inclure dans votre projet. Si vous utilisez Maven, ajoutez la dépendance suivante à votre `pom.xml` :

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- Utilisez la dernière version disponible -->
</dependency>
```

Pour Gradle, ajoutez ceci à votre `build.gradle` :

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

Vérifiez le [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) pour la dernière version.

### Étape 2: Utilisation de base
Voici comment utiliser FastJSON pour des tâches courantes comme la sérialisation et la désérialisation.

#### 1. **Sérialisation des objets Java en JSON**
Vous pouvez convertir un objet Java en une chaîne JSON en utilisant `JSON.toJSONString()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // Créer un objet échantillon
        User user = new User("Alice", 25);

        // Sérialiser en chaîne JSON
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// Classe échantillon User
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters et setters (nécessaires pour que FastJSON fonctionne correctement)
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**Sortie :**
```json
{"age":25,"name":"Alice"}
```

#### 2. **Désérialisation de JSON en objets Java**
Vous pouvez analyser une chaîne JSON en un objet Java en utilisant `JSON.parseObject()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";

        // Désérialiser en objet User
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**Sortie :**
```
Name: Alice, Age: 25
```

#### 3. **Analyse de JSON en une liste**
Si votre JSON représente une liste d'objets, utilisez `JSON.parseArray()`.

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";

        // Désérialiser en List<User>
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**Sortie :**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### Étape 3: Fonctionnalités avancées
FastJSON offre des options de personnalisation supplémentaires :

#### 1. **Personnalisation de la sérialisation**
Vous pouvez contrôler la manière dont les champs sont sérialisés en utilisant les options `SerializerFeature`.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);

        // Utiliser PrettyFormat pour une sortie lisible
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**Sortie :**
```json
{
	"age":25,
	"name":"Alice"
}
```

Options courantes `SerializerFeature` :
- `WriteNullListAsEmpty` : Les listes vides sont écrites comme `[]` au lieu de `null`.
- `WriteMapNullValue` : Inclure les champs avec des valeurs `null` dans la sortie.

#### 2. **Gestion des objets complexes**
Pour les objets imbriqués, assurez-vous que les classes internes ont des getters/setters appropriés.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        Address address = new Address("123 Main St", "NY");
        User user = new User("Alice", 25, address);

        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);

        User parsedUser = JSON.parseObject(jsonString, User.class);
        System.out.println(parsedUser.getAddress().getCity());
    }
}

class User {
    private String name;
    private int age;
    private Address address;

    public User(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public Address getAddress() { return address; }
    public void setAddress(Address address) { this.address = address; }
}

class Address {
    private String street;
    private String city;

    public Address(String street, String city) {
        this.street = street;
        this.city = city;
    }

    public String getStreet() { return street; }
    public void setStreet(String street) { this.street = street; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
}
```

**Sortie :**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### Étape 4: Notes et bonnes pratiques
- **Sécurité** : FastJSON a eu des vulnérabilités dans les anciennes versions (par exemple, exécution de code à distance). Utilisez toujours la dernière version et évitez d'activer `Feature.SupportAutoType` sauf si nécessaire.
- **Performance** : FastJSON est optimisé pour la vitesse, mais testez-le avec votre cas d'utilisation spécifique pour de grands ensembles de données.
- **Documentation** : Consultez la page GitHub officielle de [FastJSON](https://github.com/alibaba/fastjson) pour plus de détails.

Faites-moi savoir si vous avez besoin d'aide pour un cas d'utilisation spécifique ou pour le dépannage !