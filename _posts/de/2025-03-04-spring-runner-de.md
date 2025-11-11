---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von SpringRunner in Java-Tests
translated: true
type: note
---

Um `SpringRunner` mit JUnit's `@RunWith`-Runner in Java-Tests zu verwenden, befolgen Sie diese Schritte. Ich nehme an, dass "SpringRuner" in Ihrer Anfrage ein Tippfehler ist und Sie `SpringRunner` meinen. Hier ist eine vollständige Anleitung:

### Schritt 1: Fügen Sie die Spring Test-Abhängigkeit hinzu
Um `SpringRunner` zu verwenden, benötigen Sie das Spring Test-Modul in Ihrem Projekt. Wenn Sie Maven verwenden, fügen Sie diese Abhängigkeit zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

Ersetzen Sie `${spring.version}` mit der Version von Spring, die Sie verwenden (z.B. `5.3.22`). Wenn Sie Gradle verwenden, fügen Sie dies zu Ihrer `build.gradle` hinzu:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

Dies stellt sicher, dass `SpringRunner` und andere Spring-Test-Hilfsmittel verfügbar sind.

### Schritt 2: Kommentieren Sie die Testklasse mit `@RunWith(SpringRunner.class)`
Die `@RunWith`-Annotation weist JUnit an, einen bestimmten Runner anstelle des Standard-Runners zu verwenden. Für die Spring-Integration verwenden Sie `SpringRunner`, der Teil des Spring TestContext Frameworks ist. Fügen Sie diese Annotation zu Ihrer Testklasse hinzu:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // Testcode kommt hier hin
}
```

`SpringRunner` aktiviert Spring-Funktionen wie Dependency Injection und Context Loading in Ihren Tests. Beachten Sie, dass `@RunWith` eine JUnit 4-Annotation ist, daher geht dieser Ansatz davon aus, dass Sie JUnit 4 verwenden. Für JUnit 5 würden Sie stattdessen `@ExtendWith(SpringExtension.class)` verwenden, aber Ihre Erwähnung von "RunWith runner" deutet auf JUnit 4 hin.

### Schritt 3: Konfigurieren Sie den Spring Application Context mit `@ContextConfiguration`
Um Spring-verwaltete Beans in Ihren Tests zu verwenden, müssen Sie einen Spring Application Context laden. Die `@ContextConfiguration`-Annotation gibt an, wie dies zu tun ist. Wenn Sie beispielsweise eine Konfigurationsklasse haben (z.B. `AppConfig`), verwenden Sie:

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // Testcode kommt hier hin
}
```

Wenn Ihre Konfiguration in einer XML-Datei ist (z.B. `applicationContext.xml`), verwenden Sie:

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

Dies teilt `SpringRunner` mit, welche Beans und Konfigurationen für den Test geladen werden sollen.

### Schritt 4: Injizieren Sie Spring Beans mit `@Autowired`
Sobald der Context geladen ist, können Sie Spring-verwaltete Beans mit `@Autowired` in Ihre Testklasse injizieren. Wenn Sie beispielsweise einen Service namens `MyService` haben:

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // Testmethoden kommen hier hin
}
```

Dies erlaubt Ihnen, die injizierte Bean in Ihren Tests zu verwenden.

### Schritt 5: Schreiben Sie Testmethoden mit `@Test`
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
        assertEquals("Expected result", result);
    }
}
```

Die `@Test`-Annotation kennzeichnet Methoden, die JUnit als Tests ausführen soll. Mit `SpringRunner` können diese Methoden mit dem Spring Context interagieren.

### Beispiel: Alles zusammenfügen
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
        return "Hello, Spring!";
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
        assertEquals("Hello, Spring!", result);
    }
}
```

### Zusätzliche Hinweise
- **Zweck**: `SpringRunner` ist ideal für Integrationstests, bei denen Sie Spring's Dependency Injection oder Context-Funktionen benötigen. Für Unit-Tests ziehen Sie Mockito oder einfaches JUnit in Betracht.
- **Häufige Probleme**: Stellen Sie sicher, dass die `spring-test`-Abhängigkeit enthalten ist, sonst erhalten Sie Fehler wie `ClassNotFoundException`. Vergewissern Sie sich auch, dass `@ContextConfiguration` auf eine gültige Konfiguration verweist.
- **Optionale Annotationen**: Verwenden Sie `@Transactional` für Tests, die die Datenbank ändern (um Änderungen zurückzurollen) oder `@ActiveProfiles`, um ein Profil anzugeben (z.B. "test").

Dieses Setup ermöglicht es Ihnen, JUnit-Tests mit Spring's Testunterstützung auszuführen und nutzt Funktionen wie Dependency Injection und Context Management.