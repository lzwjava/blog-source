---
audio: true
generated: true
lang: de
layout: post
title: Verwendung von SpringRunner in Java-Tests
translated: true
---

Um `SpringRunner` mit JUnit's `@RunWith`-Runner in Java-Tests zu verwenden, befolgen Sie diese Schritte. Beachten Sie, dass ich annehme, dass "SpringRuner" in Ihrer Anfrage ein Tippfehler ist und Sie `SpringRunner` meinen. Hier ist eine vollständige Anleitung:

### Schritt 1: Spring Test-Abhängigkeit hinzufügen
Um `SpringRunner` zu verwenden, benötigen Sie das Spring Test-Modul in Ihrem Projekt. Wenn Sie Maven verwenden, fügen Sie diese Abhängigkeit zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

Ersetzen Sie `${spring.version}` durch die Version von Spring, die Sie verwenden (z.B. `5.3.22`). Wenn Sie Gradle verwenden, fügen Sie dies zu Ihrer `build.gradle` hinzu:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

Dies stellt sicher, dass `SpringRunner` und andere Spring-Test-Utilities verfügbar sind.

### Schritt 2: Testklasse mit `@RunWith(SpringRunner.class)` annotieren
Die `@RunWith`-Annotation weist JUnit an, einen bestimmten Runner anstelle des Standard-Runners zu verwenden. Für die Spring-Integration verwenden Sie `SpringRunner`, der Teil des Spring TestContext Frameworks ist. Fügen Sie diese Annotation zu Ihrer Testklasse hinzu:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // Testcode geht hier hin
}
```

`SpringRunner` ermöglicht Spring-Funktionen wie Dependency Injection und Context-Loading in Ihren Tests. Beachten Sie, dass `@RunWith` eine JUnit 4-Annotation ist, sodass diese Vorgehensweise voraussetzt, dass Sie JUnit 4 verwenden. Für JUnit 5 würden Sie `@ExtendWith(SpringExtension.class)` verwenden, aber Ihre Erwähnung des "RunWith runners" deutet auf JUnit 4 hin.

### Schritt 3: Spring Application Context mit `@ContextConfiguration` konfigurieren
Um Spring-verwaltete Beans in Ihren Tests zu verwenden, müssen Sie einen Spring Application Context laden. Die `@ContextConfiguration`-Annotation gibt an, wie dies zu tun ist. Wenn Sie beispielsweise eine Konfigurationsklasse (z.B. `AppConfig`) haben, verwenden Sie:

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // Testcode geht hier hin
}
```

Wenn Ihre Konfiguration in einer XML-Datei (z.B. `applicationContext.xml`) vorliegt, verwenden Sie:

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

Dies weist `SpringRunner` an, welche Beans und Konfigurationen für den Test zu laden sind.

### Schritt 4: Spring Beans mit `@Autowired` injizieren
Sobald der Context geladen ist, können Sie Spring-verwaltete Beans in Ihre Testklasse mit `@Autowired` injizieren. Wenn Sie beispielsweise einen Service namens `MyService` haben:

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // Testmethoden gehen hier hin
}
```

Dies ermöglicht es Ihnen, das injizierte Bean in Ihren Tests zu verwenden.

### Schritt 5: Testmethoden mit `@Test` definieren
Definieren Sie Ihre Testmethoden mit JUnit's `@Test`-Annotation. Zum Beispiel:

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Erwartetes Ergebnis", result);
    }
}
```

Die `@Test`-Annotation markiert Methoden, die JUnit als Tests ausführen soll. Mit `SpringRunner` können diese Methoden mit dem Spring Context interagieren.

### Beispiel: Alles zusammenfassen
Hier ist ein vollständiges Beispiel:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// Konfigurationsklasse für den Test
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// Serviceklasse zum Testen
class MyService {
    public String doSomething() {
        return "Hallo, Spring!";
    }
}

// Testklasse
@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Hallo, Spring!", result);
    }
}
```

### Zusätzliche Hinweise
- **Zweck**: `SpringRunner` ist ideal für Integrationstests, bei denen Sie die Dependency Injection oder Context-Funktionen von Spring benötigen. Für Unit-Tests sollten Sie Mockito oder einfaches JUnit in Betracht ziehen.
- **Häufige Probleme**: Stellen Sie sicher, dass die `spring-test`-Abhängigkeit enthalten ist, andernfalls erhalten Sie Fehler wie `ClassNotFoundException`. Überprüfen Sie auch, dass `@ContextConfiguration` auf eine gültige Konfiguration verweist.
- **Optionale Annotationen**: Verwenden Sie `@Transactional` für Tests, die die Datenbank ändern (um Änderungen zurückzusetzen) oder `@ActiveProfiles`, um ein Profil anzugeben (z.B. "test").

Diese Einrichtung ermöglicht es Ihnen, JUnit-Tests mit der Testunterstützung von Spring auszuführen und Funktionen wie Dependency Injection und Context-Management zu nutzen.