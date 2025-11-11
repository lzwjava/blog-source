---
audio: false
generated: true
lang: de
layout: post
title: Spring-Boot-Java-Codierkonventionen
translated: true
type: note
---

## 1. Kernprinzipien
- Befolgen Sie die standardmäßigen Java Code Conventions
- Lesbarkeit und Wartbarkeit priorisieren
- Konsistenz im gesamten Spring-Ökosystem
- Anpassung an Java-Best-Practices

## 2. Code-Formatierung

### Allgemeine Richtlinien
- Verwenden Sie IntelliJ IDEA Standard-Formatierung
- 4 Leerzeichen Einrückung (keine Tabs)
- Maximale Zeilenlänge von 120 Zeichen
- Verwenden Sie standardmäßigen Java-Brace-Stil

### Spezifische Formatierungsregeln
- Leerzeile zwischen Methoden
- Keine nachgestellten Leerzeichen
- Verwenden Sie Unix-Zeilenenden (LF)

## 3. Namenskonventionen

### Klassennamen
- Verwenden Sie beschreibende, aussagekräftige Namen
- Verwenden Sie UpperCamelCase
- Beispiele:
  - `ConfigurationProperties`
  - `AutoConfigurationImportSelector`
  - `SpringApplication`

### Methodennamen
- Verwenden Sie lowerCamelCase
- Verb oder Verbphrasen
- Beispiele:
  - `configure()`
  - `registerBeanDefinitions()`
  - `isEnabledByDefault()`

## 4. Annotation-Praktiken

### Annotation-Reihenfolge
- Standardreihenfolge für Annotationen:
  1. Override-Annotationen (`@Override`)
  2. Scope-Annotationen (`@Component`, `@Service`)
  3. Dependency Injection-Annotationen
  4. Transaktionale Annotationen
  5. Benutzerdefinierte Projektannotationen

### Annotation-Platzierung
```java
@Component
@Transactional
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

## 5. Dependency Injection

### Bevorzugte Injectionsmethode
- Konstruktor-Injection
- Feld-Injection vermeiden
- Verwenden Sie `@Autowired` am Konstruktor

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

## 6. Logging
- Verwenden Sie SLF4J für Logging
- Verwenden Sie `private static final Logger` oder Lomboks `@Slf4j`

```java
@Slf4j
@Service
public class UserService {
    public void processUser(User user) {
        log.info("Processing user: {}", user.getUsername());
    }
}
```

## 7. Fehlerbehandlung
- Verwenden Sie spezifische Exceptions
- Geben Sie aussagekräftige Fehlermeldungen an
- Verwenden Sie `@ControllerAdvice` für globale Exception-Behandlung

## 8. Konfiguration
- Verwenden Sie `application.yml` statt `application.properties`
- Verwenden Sie profil-spezifische Konfigurationen
- Externalisieren Sie Konfigurationswerte

## 9. Testing
- Verwenden Sie JUnit 5
- Nutzen Sie Spring Boot Test Utilities
- Befolgen Sie das Arrange-Act-Assert-Pattern

## 10. Zusätzliche Ressourcen
- [Spring Boot GitHub Coding Style](https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.md)
- [Spring Framework Guidelines](https://github.com/spring-projects/spring-framework/wiki/Code-Style)