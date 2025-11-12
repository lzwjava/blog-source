---
audio: false
generated: true
lang: fr
layout: post
title: API Java pour RocksDB
translated: true
type: note
---

Pour utiliser la bibliothèque `org.rocksdb`, qui est l'API Java pour RocksDB—une base de données embarquée haute performance pour les données clé-valeur—vous devez suivre ces étapes. RocksDB est optimisé pour un stockage et une récupération rapides, ce qui le rend idéal pour les applications nécessitant un accès rapide aux données par des clés connues. Voici un guide complet pour commencer :

---

### 1. **Ajouter la Dépendance**
Pour utiliser `org.rocksdb` dans votre projet Java, vous devez inclure la dépendance RocksDB JNI (Java Native Interface). Si vous utilisez Maven, ajoutez ceci à votre fichier `pom.xml` :

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

Pour Gradle, ajoutez ceci à votre `build.gradle` :

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**Remarque** : Vérifiez [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) pour la dernière version, car `7.10.2` pourrait ne pas être la version actuelle.

---

### 2. **Charger la Bibliothèque Native**
RocksDB repose sur du code natif C++, vous devez donc charger la bibliothèque native avant de l'utiliser. Ajoutez cette ligne au début de votre code :

```java
RocksDB.loadLibrary();
```

Si vous oubliez cette étape, des erreurs d'exécution se produiront.

---

### 3. **Ouvrir une Base de Données**
Pour commencer à utiliser RocksDB, vous devez ouvrir une instance de base de données en spécifiant un chemin de fichier où la base de données sera stockée. Utilisez la classe `Options` pour configurer les paramètres, comme la création de la base de données si elle n'existe pas :

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/chemin/vers/db");
```

- **`options`** : Configure le comportement de la base de données (par exemple, `setCreateIfMissing(true)` garantit que la base de données est créée si elle n'existe pas).
- **`/chemin/vers/db`** : Remplacez ceci par un chemin de répertoire valide sur votre système où résideront les fichiers de la base de données.

---

### 4. **Effectuer les Opérations de Base**
RocksDB est un magasin clé-valeur, et ses opérations principales sont `put`, `get` et `delete`. Les clés et les valeurs sont stockées sous forme de tableaux d'octets, vous devrez donc convertir les données (par exemple, les chaînes de caractères) en octets.

- **Put** : Insérer ou mettre à jour une paire clé-valeur.
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get** : Récupérer la valeur associée à une clé.
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // Affiche "value"
  } else {
      System.out.println("Key not found");
  }
  ```

- **Delete** : Supprimer une paire clé-valeur.
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **Fermer la Base de Données**
Fermer correctement la base de données est essentiel pour libérer les ressources. La manière la plus simple est d'utiliser un bloc try-with-resources, qui ferme automatiquement la base de données lorsque vous avez terminé :

```java
try (RocksDB db = RocksDB.open(options, "/path/to/db")) {
    // Effectuer les opérations ici
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **Gérer les Exceptions**
Les opérations RocksDB peuvent lever `RocksDBException`, incluez donc toujours une gestion des exceptions pour éviter les fuites de ressources ou la corruption des données :

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **Options de Configuration**
Vous pouvez affiner les performances de RocksDB en utilisant la classe `Options`. Par exemple :

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // Buffer d'écriture de 64 Mo
```

Les options courantes incluent :
- `setWriteBufferSize` : Contrôle la mémoire utilisée pour les écritures.
- `setMaxOpenFiles` : Limite le nombre de fichiers ouverts.
- `setCompactionStyle` : Ajuste la façon dont les données sont compactées sur le disque.

Explorez la [documentation RocksDB](https://github.com/facebook/rocksdb/wiki) pour plus d'options.

---

### 8. **Exemple Simple**
Voici un exemple complet qui montre comment ouvrir une base de données, stocker une paire clé-valeur et la récupérer :

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // Charger la bibliothèque native
        Options options = new Options().setCreateIfMissing(true);
        
        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // Mettre une paire clé-valeur
            db.put("hello".getBytes(), "world".getBytes());
            
            // Obtenir la valeur
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // Affiche "world"
            } else {
                System.out.println("Key not found");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**Sortie** : `world`

---

### Considérations Clés
- **Nature Embarquée** : RocksDB s'exécute dans le processus de votre application, et non comme un serveur séparé.
- **Tableaux d'Octets** : Les clés et les valeurs sont des `byte[]`, vous devrez donc gérer la sérialisation/désérialisation pour les objets complexes.
- **Performance** : RocksDB excelle avec un stockage rapide (par exemple, les SSD) et est utilisé dans des systèmes haute performance comme ceux de Facebook, où il a été développé.
- **Non Relationnel** : C'est un magasin clé-valeur, pas une base de données relationnelle—pas de SQL ou de jointures.

---

### Pièges Courants
- **Oublier `RocksDB.loadLibrary()`** : Conduit à une `UnsatisfiedLinkError`.
- **Gestion Impropre des Ressources** : Ne pas fermer la base de données peut causer des problèmes, surtout sur les systèmes aux ressources limitées.
- **Erreurs de Type de Données** : Passer des chaînes de caractères ou des objets directement au lieu de les convertir en `byte[]`.

---

### Pour Aller Plus Loin
- **Fonctions Avancées** : Explorez les transactions, les instantanés (snapshots) ou les familles de colonnes pour des cas d'utilisation plus complexes.
- **Ressources** : Consultez l'[API Java RocksDB](https://github.com/facebook/rocksdb/tree/main/java) et le [Wiki RocksDB](https://github.com/facebook/rocksdb/wiki) pour une documentation détaillée et des exemples.

Ce guide fournit une base solide pour utiliser `org.rocksdb`. Si vous avez besoin d'aide avec des fonctionnalités spécifiques ou des cas d'utilisation, n'hésitez pas à demander !