---
audio: false
generated: true
lang: fr
layout: post
title: Comment Fonctionnent Les Propriétés Dans Spring Boot
translated: true
type: note
---

Explorons le fonctionnement des propriétés dans Spring Boot, y compris l'utilisation des fichiers YAML ou `.properties`, la façon de les remplacer avec des arguments de ligne de commande comme `-D`, les différentes méthodes pour initialiser les propriétés et comment les tester efficacement.

---

### **Fonctionnement des propriétés dans Spring Boot**
Spring Boot fournit un système flexible pour gérer la configuration d'une application via des propriétés, qui sont des paires clé-valeur. Ces propriétés peuvent être définies dans de multiples sources, et Spring Boot les résout selon un ordre de priorité spécifique. Cela vous permet de personnaliser votre application pour différents environnements ou scénarios de déploiement. Les propriétés sont chargées dans l'**Environnement Spring**, les rendant accessibles dans toute votre application.

Les principales sources de propriétés incluent :
- Les fichiers de configuration (par ex., `application.properties` ou `application.yml`)
- Les arguments de ligne de commande (par ex., `--server.port=8081`)
- Les propriétés système (par ex., `-Dserver.port=8081`)
- Les variables d'environnement
- Le code Java (par ex., via `@Value` ou `@ConfigurationProperties`)

---

### **Utilisation des fichiers YAML ou Properties**
Spring Boot prend en charge deux formats principaux pour les fichiers de configuration, tous deux généralement placés dans `src/main/resources` :

#### **1. Fichiers `.properties`**
Il s'agit d'un format simple et plat de paires clé-valeur :
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

#### **2. Fichiers `.yml` ou `.yaml`**
Il s'agit d'un format structuré et hiérarchique utilisant l'indentation :
```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
```

**Points clés :**
- Utilisez `.properties` pour les configurations simples et `.yml` pour les configurations imbriquées ou complexes.
- Les fichiers spécifiques à un profil (par ex., `application-dev.yml`) peuvent être utilisés pour des paramètres spécifiques à un environnement.
- Exemple : Définir `server.port=8080` change le port sur lequel votre application Spring Boot s'exécute.

---

### **Utilisation des arguments de ligne de commande pour remplacer les propriétés**
Vous pouvez remplacer les propriétés définies dans les fichiers de configuration en utilisant des arguments de ligne de commande de deux manières :

#### **1. Utilisation de `--` pour les propriétés Spring Boot**
Passez les propriétés directement lors de l'exécution de l'application :
```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/testdb
```
Celles-ci ont priorité sur les fichiers de configuration.

#### **2. Utilisation de `-D` pour les propriétés système**
Définissez les propriétés système avec `-D`, que Spring Boot reconnaît également :
```bash
java -Dserver.port=8081 -Dspring.datasource.url=jdbc:mysql://localhost:3306/testdb -jar myapp.jar
```
Les propriétés système remplacent également les valeurs des fichiers de configuration.

---

### **Différentes méthodes pour initialiser les propriétés**
Spring Boot offre plusieurs méthodes pour définir ou initialiser les propriétés au-delà des fichiers et des arguments de ligne de commande :

#### **1. Variables d'environnement**
Les propriétés peuvent être définies via des variables d'environnement. Par exemple :
- Définissez `SERVER_PORT=8081` dans votre environnement, et Spring Boot le mappe à `server.port`.
- **Convention de nommage :** Convertissez les noms de propriétés en majuscules et remplacez les points (`.`) par des traits de soulignement (`_`), par ex., `spring.datasource.url` devient `SPRING_DATASOURCE_URL`.

#### **2. Code Java**
Vous pouvez initialiser les propriétés de manière programmatique :
- **Utilisation de `@Value`** : Injecte une propriété spécifique dans un champ.
  ```java
  @Value("${server.port}")
  private int port;
  ```
- **Utilisation de `@ConfigurationProperties`** : Lie un groupe de propriétés à un objet Java.
  ```java
  @Component
  @ConfigurationProperties(prefix = "app")
  public class AppProperties {
      private String name;
      // getters and setters
  }
  ```
  Cela lie les propriétés comme `app.name` au champ `name`.

#### **3. Valeurs par défaut**
Fournissez des valeurs de repli si une propriété n'est pas définie :
- Avec `@Value` : `@Value("${server.port:8080}")` utilise `8080` si `server.port` n'est pas défini.
- Dans les fichiers de configuration : Définissez les valeurs par défaut dans `application.properties` ou YAML.

---

### **Priorité des propriétés**
Spring Boot résout les propriétés à partir de multiples sources dans cet ordre (la priorité la plus élevée remplace la plus basse) :
1. Arguments de ligne de commande (`--property=value`)
2. Propriétés système (`-Dproperty=value`)
3. Variables d'environnement
4. Fichiers de configuration (`application.properties` ou `application.yml`)
5. Valeurs par défaut dans le code

**Exemple :** Si `server.port=8080` est dans `application.properties` mais que vous exécutez `java -jar myapp.jar --server.port=8081`, le port sera `8081`.

---

### **Comment tester les propriétés**
Tester les propriétés garantit que votre application se comporte comme prévu. Voici les approches courantes :

#### **1. Utilisation de `@TestPropertySource`**
Remplacez les propriétés dans les tests unitaires :
```java
@SpringBootTest
@TestPropertySource(properties = {"server.port=9090"})
public class MyTest {
    // Code de test
}
```

#### **2. Utilisation de `application-test.properties`**
Placez un fichier spécifique aux tests dans `src/test/resources` :
```properties
server.port=9090
```
Spring Boot charge ce fichier automatiquement pendant les tests.

#### **3. Remplacements programmatiques**
Définissez les propriétés dans la configuration du test :
```java
@SpringBootTest
public class MyTest {
    @BeforeEach
    public void setup() {
        System.setProperty("server.port", "9090");
    }
}
```

#### **4. Utilisation de `@ActiveProfiles`**
Activez les propriétés spécifiques à un profil :
- Définissez `application-test.yml` avec les paramètres de test.
- Utilisez :
  ```java
  @SpringBootTest
  @ActiveProfiles("test")
  public class MyTest {
      // Code de test
  }
  ```

---

### **Résumé**
- **Fichiers de configuration** : Utilisez `application.properties` ou `application.yml` pour les paramètres par défaut.
- **Arguments de ligne de commande** : Remplacez avec `--property=value` ou `-Dproperty=value`.
- **Méthodes d'initialisation** : Tirez parti des variables d'environnement, du code Java (`@Value`, `@ConfigurationProperties`) ou des valeurs par défaut.
- **Test** : Utilisez `@TestPropertySource`, les fichiers spécifiques aux tests, les remplacements programmatiques ou les profils.

Ceci couvre les bases du travail avec les propriétés dans Spring Boot. Faites-moi savoir si vous souhaitez plus de détails !