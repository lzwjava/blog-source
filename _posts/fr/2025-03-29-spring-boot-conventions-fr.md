---
audio: false
generated: true
lang: fr
layout: post
title: Conventions de codage Java Spring Boot
translated: true
type: note
---

## 1. Principes fondamentaux
- Suivre les conventions de code Java standard
- Privilégier la lisibilité et la maintenabilité
- Cohérence dans l'écosystème Spring
- S'aligner sur les bonnes pratiques Java de base

## 2. Formatage du code

### Règles générales
- Utiliser le formatage par défaut d'IntelliJ IDEA
- Indentation de 4 espaces (pas de tabulations)
- Longueur maximale de ligne de 120 caractères
- Utiliser le style d'accolades Java standard

### Règles de formatage spécifiques
- Ligne vide entre les méthodes
- Pas d'espaces de fin de ligne
- Utiliser les fins de ligne de style Unix (LF)

## 3. Conventions de nommage

### Nommage des classes
- Utiliser des noms descriptifs et significatifs
- Utiliser le UpperCamelCase
- Exemples :
  - `ConfigurationProperties`
  - `AutoConfigurationImportSelector`
  - `SpringApplication`

### Nommage des méthodes
- Utiliser le lowerCamelCase
- Verbe ou phrases verbales
- Exemples :
  - `configure()`
  - `registerBeanDefinitions()`
  - `isEnabledByDefault()`

## 4. Pratiques d'annotation

### Ordre des annotations
- Ordre standard pour les annotations :
  1. Annotations de redéfinition (`@Override`)
  2. Annotations de portée (`@Component`, `@Service`)
  3. Annotations d'injection de dépendances
  4. Annotations transactionnelles
  5. Annotations personnalisées du projet

### Placement des annotations
```java
@Component
@Transactional
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

## 5. Injection de dépendances

### Méthode d'injection préférée
- Injection par constructeur
- Éviter l'injection par champ
- Utiliser `@Autowired` sur le constructeur

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

## 6. Journalisation
- Utiliser SLF4J pour la journalisation
- Utiliser `private static final Logger` ou `@Slf4j` de Lombok

```java
@Slf4j
@Service
public class UserService {
    public void processUser(User user) {
        log.info("Processing user: {}", user.getUsername());
    }
}
```

## 7. Gestion des erreurs
- Utiliser des exceptions spécifiques
- Fournir des messages d'erreur significatifs
- Utiliser `@ControllerAdvice` pour la gestion globale des exceptions

## 8. Configuration
- Utiliser `application.yml` plutôt que `application.properties`
- Utiliser des configurations spécifiques aux profils
- Externaliser les valeurs de configuration

## 9. Tests
- Utiliser JUnit 5
- Tirer parti des utilitaires de test Spring Boot
- Suivre le modèle Arrange-Act-Assert

## 10. Ressources supplémentaires
- [Spring Boot GitHub Coding Style](https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.md)
- [Spring Framework Guidelines](https://github.com/spring-projects/spring-framework/wiki/Code-Style)