---
audio: false
generated: true
lang: fr
layout: post
title: Exceptions Spring Boot
translated: true
type: note
---

Lorsque vous travaillez avec Spring Boot ou l'écosystème plus large du Spring Framework, les développeurs rencontrent fréquemment des exceptions dues à des problèmes de configuration, des erreurs d'exécution ou une utilisation incorrecte des API. Vous trouverez ci-dessous une liste des exceptions courantes que vous pourriez rencontrer, ainsi que leurs causes typiques et des solutions potentielles. Ces exceptions sont regroupées par catégorie pour plus de clarté.

---

### **1. Exceptions liées à la configuration**

- **`org.springframework.beans.factory.BeanCreationException`** :
  - **Cause** : Un bean n'a pas pu être créé en raison de dépendances manquantes, d'une mauvaise configuration ou d'erreurs d'instanciation.
  - **Exemple** : Absence d'annotation `@Component`, `@Service` ou dépendance `@Autowired` introuvable.
  - **Résolution** : Vérifier les définitions des beans, s'assurer que les dépendances sont disponibles et vérifier les annotations.

- **`org.springframework.beans.factory.NoSuchBeanDefinitionException`** :
  - **Cause** : Spring ne trouve pas un bean du type ou du nom demandé dans le contexte d'application.
  - **Exemple** : Tenter d'utiliser `@Autowired` sur un bean qui n'est pas défini ou scanné.
  - **Résolution** : S'assurer que le bean est annoté (par exemple, avec `@Component`) et se trouve dans le chemin de scan des composants.

- **`org.springframework.context.ApplicationContextException`** :
  - **Cause** : Échec général de l'initialisation du contexte d'application Spring.
  - **Exemple** : Configuration invalide dans `application.properties` ou erreur de syntaxe dans une classe `@Configuration`.
  - **Résolution** : Examiner la stack trace pour trouver la cause racine (par exemple, une propriété invalide ou une ressource manquante).

- **`org.springframework.beans.factory.UnsatisfiedDependencyException`** :
  - **Cause** : Une dépendance requise par un bean ne peut pas être satisfaite.
  - **Exemple** : Dépendance circulaire ou implémentation manquante pour une interface.
  - **Résolution** : Rompre les dépendances circulaires (par exemple, utiliser `@Lazy`) ou fournir la dépendance manquante.

---

### **2. Exceptions liées au Web et REST**

- **`org.springframework.web.bind.MissingServletRequestParameterException`** :
  - **Cause** : Un paramètre de requête obligatoire est manquant dans une requête HTTP.
  - **Exemple** : `@RequestParam("id")` est spécifié, mais le client n'a pas envoyé `id`.
  - **Résolution** : Rendre le paramètre optionnel (`required = false`) ou s'assurer que le client l'inclut.

- **`org.springframework.http.converter.HttpMessageNotReadableException`** :
  - **Cause** : Le corps de la requête ne peut pas être désérialisé (par exemple, JSON mal formé).
  - **Exemple** : Envoi d'un JSON invalide à un endpoint avec `@RequestBody`.
  - **Résolution** : Valider le contenu de la requête et s'assurer qu'il correspond à la structure de l'objet cible.

- **`org.springframework.web.method.annotation.MethodArgumentTypeMismatchException`** :
  - **Cause** : Un argument de méthode ne peut pas être converti vers le type attendu.
  - **Exemple** : Passer une chaîne comme `"abc"` à un paramètre attendant un `int`.
  - **Résolution** : Valider la saisie ou utiliser des convertisseurs personnalisés.

- **`org.springframework.web.servlet.NoHandlerFoundException`** :
  - **Cause** : Aucun mapping de contrôleur n'existe pour l'URL demandée.
  - **Exemple** : Une faute de frappe dans `@RequestMapping` ou contrôleur manquant.
  - **Résolution** : Vérifier les mappings des endpoints et s'assurer que les contrôleurs sont scannés.

---

### **3. Exceptions d'accès aux données (Spring Data/JPA/Hibernate)**

- **`org.springframework.dao.DataIntegrityViolationException`** :
  - **Cause** : Une opération de base de données viole une contrainte (par exemple, clé unique ou clé étrangère).
  - **Exemple** : Insertion d'une valeur de clé primaire en double.
  - **Résolution** : Vérifier l'unicité des données ou gérer l'exception de manière appropriée.

- **`org.springframework.orm.jpa.JpaSystemException`** :
  - **Cause** : Erreur d'exécution générale liée à JPA, encapsulant souvent une exception Hibernate.
  - **Exemple** : Violation de contrainte ou problème de connexion.
  - **Résolution** : Examiner l'exception imbriquée (par exemple, `SQLException`) pour plus de détails.

- **`org.hibernate.LazyInitializationException`** :
  - **Cause** : Tentative d'accès à une entité chargée de manière différée (lazy) en dehors d'une session active.
  - **Exemple** : Accès à une relation `@OneToMany` après la fin de la transaction.
  - **Résolution** : Utiliser le chargement immédiat (eager), récupérer dans la requête (par exemple, avec `JOIN FETCH`) ou s'assurer qu'une session est ouverte.

- **`org.springframework.dao.InvalidDataAccessApiUsageException`** :
  - **Cause** : Utilisation incorrecte des API Spring Data ou JDBC.
  - **Exemple** : Passage d'un paramètre null à une requête attendant une valeur.
  - **Résolution** : Valider les paramètres des requêtes et l'utilisation de l'API.

---

### **4. Exceptions liées à la sécurité**

- **`org.springframework.security.access.AccessDeniedException`** :
  - **Cause** : L'utilisateur authentifié ne dispose pas des permissions pour une ressource.
  - **Exemple** : Accès à un endpoint sécurisé sans le rôle requis.
  - **Résolution** : Vérifier `@PreAuthorize` ou la configuration de sécurité et ajuster les rôles/autorisations.

- **`org.springframework.security.authentication.BadCredentialsException`** :
  - **Cause** : L'authentification a échoué en raison d'un nom d'utilisateur ou d'un mot de passe incorrect.
  - **Exemple** : L'utilisateur saisit de mauvaises informations d'identification dans un formulaire de connexion.
  - **Résolution** : S'assurer que les informations d'identification sont correctes ; personnaliser la gestion des erreurs pour le feedback utilisateur.

- **`org.springframework.security.authentication.DisabledException`** :
  - **Cause** : Le compte utilisateur est désactivé.
  - **Exemple** : Une implémentation `UserDetails` retourne `isEnabled() == false`.
  - **Résolution** : Activer le compte ou mettre à jour le statut de l'utilisateur.

---

### **5. Exceptions d'exécution diverses**

- **`java.lang.IllegalStateException`** :
  - **Cause** : Spring rencontre un état invalide pendant l'exécution.
  - **Exemple** : Appel d'une méthode sur un bean qui n'a pas été entièrement initialisé.
  - **Résolution** : Vérifier les méthodes de cycle de vie ou l'ordre d'initialisation des beans.

- **`org.springframework.transaction.TransactionException`** :
  - **Cause** : Un problème est survenu pendant la gestion des transactions.
  - **Exemple** : Rollback d'une transaction dû à une exception non gérée.
  - **Résolution** : S'assurer d'une utilisation correcte de `@Transactional` et gérer les exceptions au sein de la transaction.

- **`java.lang.NullPointerException`** :
  - **Cause** : Tentative d'accès à une référence d'objet nulle.
  - **Exemple** : Une dépendance `@Autowired` n'a pas été injectée en raison d'une mauvaise configuration.
  - **Résolution** : Ajouter des vérifications de nullité ou déboguer pourquoi la dépendance est manquante.

---

### **6. Exceptions spécifiques à Spring Boot**

- **`org.springframework.boot.context.embedded.EmbeddedServletContainerException`** (versions antérieures) ou **`org.springframework.boot.web.server.WebServerException`** (versions plus récentes) :
  - **Cause** : Échec du démarrage du serveur web embarqué (par exemple, Tomcat, Jetty).
  - **Exemple** : Port déjà utilisé (par exemple, `8080`).
  - **Résolution** : Changer le port dans `application.properties` (`server.port=8081`) ou libérer le port occupé.

- **`org.springframework.boot.autoconfigure.jdbc.DataSourceProperties$DataSourceBeanCreationException`** :
  - **Cause** : Échec de la configuration de la source de données.
  - **Exemple** : `spring.datasource.url/username/password` manquant ou incorrect.
  - **Résolution** : Vérifier les propriétés de la source de données dans `application.properties` ou `application.yml`.

- **`org.springframework.boot.SpringApplication - Application run failed`** :
  - **Cause** : Échec générique lors du démarrage de Spring Boot.
  - **Exemple** : Mauvaise configuration, beans manquants ou conflits de dépendances.
  - **Résolution** : Vérifier la stack trace complète pour identifier la cause racine.

---

### **Bonnes pratiques pour gérer les exceptions**

1. **Gestion globale des exceptions** :
   - Utiliser `@ControllerAdvice` avec `@ExceptionHandler` pour intercepter et gérer les exceptions de manière cohérente dans toute votre application.
   - Exemple :
     ```java
     @ControllerAdvice
     public class GlobalExceptionHandler {
         @ExceptionHandler(DataIntegrityViolationException.class)
         public ResponseEntity<String> handleDataIntegrityViolation() {
             return ResponseEntity.status(HttpStatus.CONFLICT).body("Une violation d'intégrité des données s'est produite.");
         }
     }
     ```

2. **Journalisation** :
   - Journaliser les exceptions avec un framework comme SLF4J/Logback pour faciliter le débogage.

3. **Exceptions personnalisées** :
   - Définir des exceptions spécifiques à l'application et les mapper vers des statuts HTTP appropriés.

4. **Validation** :
   - Utiliser `@Valid` et la validation de beans (par exemple, `@NotNull`) pour détecter les erreurs tôt et éviter les exceptions d'exécution.

5. **Débogage** :
   - Activer la journalisation détaillée (`logging.level.org.springframework=DEBUG`) dans `application.properties` pour tracer les problèmes.

---

### **Conclusion**

Ces exceptions sont parmi les plus courantes que vous rencontrerez en utilisant Spring Boot ou le Spring Framework. Comprendre leurs causes et leurs résolutions peut accélérer significativement le développement et le débogage. Si vous êtes confronté à une exception spécifique et avez besoin d'une analyse plus approfondie, n'hésitez pas à partager les détails, et je fournirai une explication adaptée !