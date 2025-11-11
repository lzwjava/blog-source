---
audio: false
generated: true
lang: de
layout: post
title: HTTP-Clients in Spring
translated: true
type: note
---

Um die Frage "wie man FeignClient, Spring RestClient oder Spring WebClient verwendet" zu beantworten, erkläre ich, wie jedes dieser Spring-Tools für HTTP-Anfragen genutzt werden kann, mit Fokus auf Einrichtung und Grundlagen. Diese gehören alle zum Spring-Ökosystem für die Interaktion mit RESTful Services, erfüllen aber je nach den Anforderungen Ihrer Anwendung unterschiedliche Zwecke. Im Folgenden finden Sie eine klare, schrittweise Anleitung für jedes Tool zusammen mit einfachen Beispielen.

---

### **1. FeignClient verwenden**
FeignClient ist ein deklarativer REST-Client von Spring Cloud. Er ermöglicht es Ihnen, HTTP-Clients als Interfaces mit Annotationen zu definieren, was besonders in Microservices-Architekturen nützlich ist, in denen Sie andere Services aufrufen müssen.

#### **Schritte zur Verwendung von FeignClient**
1.  **Abhängigkeiten hinzufügen**: Fügen Sie Spring Cloud-Abhängigkeiten zu Ihrem Projekt hinzu. Wenn Sie Maven verwenden, fügen Sie den Spring Cloud Starter für Feign zu Ihrer `pom.xml` hinzu:
    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-openfeign</artifactId>
    </dependency>
    ```
    Stellen Sie sicher, dass Sie auch ein Dependency-Management-Block für Spring Cloud haben, der eine kompatible Version angibt.

2.  **Feign Clients aktivieren**: Kommentieren Sie Ihre Hauptanwendungsklasse oder eine Konfigurationsklasse mit `@EnableFeignClients`, um die Feign-Unterstützung zu aktivieren:
    ```java
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.cloud.openfeign.EnableFeignClients;

    @SpringBootApplication
    @EnableFeignClients
    public class MyApplication {
        public static void main(String[] args) {
            SpringApplication.run(MyApplication.class, args);
        }
    }
    ```

3.  **Das FeignClient-Interface definieren**: Erstellen Sie ein Interface, das mit `@FeignClient` kommentiert ist, geben Sie den Service-Namen oder die URL an und definieren Sie Methoden, die den REST-Endpoints entsprechen:
    ```java
    import org.springframework.cloud.openfeign.FeignClient;
    import org.springframework.web.bind.annotation.GetMapping;
    import java.util.List;

    @FeignClient(name = "user-service", url = "http://localhost:8080")
    public interface UserClient {
        @GetMapping("/users")
        List<User> getUsers();
    }
    ```
    Hier ist `name` ein logischer Name für den Client und `url` die Basis-URL des Zielservices. Die `@GetMapping`-Annotation verweist auf den `/users`-Endpoint.

4.  **Client injizieren und verwenden**: Autowiren Sie das Interface in Ihrem Service oder Controller und rufen Sie seine Methoden auf, als wären sie lokal:
    ```java
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Service;
    import java.util.List;

    @Service
    public class UserService {
        @Autowired
        private UserClient userClient;

        public List<User> fetchUsers() {
            return userClient.getUsers();
        }
    }
    ```

#### **Wichtige Punkte**
- FeignClient ist standardmäßig synchron.
- Es ist ideal für Microservices mit Service Discovery (z.B. Eureka), wenn Sie die `url` weglassen und Spring Cloud die Auflösung überlassen.
- Fehlerbehandlung kann mit Fallbacks oder Circuit Breakern (z.B. Hystrix oder Resilience4j) hinzugefügt werden.

---

### **2. Spring RestClient verwenden**
Spring RestClient ist ein synchroner HTTP-Client, der in Spring Framework 6.1 als moderne Alternative zum veralteten `RestTemplate` eingeführt wurde. Er bietet eine flüssige API zum Erstellen und Ausführen von Anfragen.

#### **Schritte zur Verwendung von RestClient**
1.  **Abhängigkeiten**: RestClient ist in `spring-web` enthalten, das Teil von Spring Boots `spring-boot-starter-web` ist. Typischerweise sind keine zusätzlichen Abhängigkeiten nötig:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```

2.  **Eine RestClient-Instanz erstellen**: Instanziieren Sie `RestClient` mit seiner statischen `create()`-Methode oder passen Sie es mit einem Builder an:
    ```java
    import org.springframework.web.client.RestClient;

    RestClient restClient = RestClient.create();
    ```
    Für benutzerdefinierte Konfigurationen (z.B. Timeouts) verwenden Sie `RestClient.builder()`.

3.  **Eine Anfrage erstellen und ausführen**: Verwenden Sie die flüssige API, um die HTTP-Methode, URI, Header und Body anzugeben, und rufen Sie dann die Antwort ab:
    ```java
    import org.springframework.http.MediaType;
    import org.springframework.web.client.RestClient;
    import java.util.List;

    public class UserService {
        private final RestClient restClient;

        public UserService() {
            this.restClient = RestClient.create();
        }

        public List<User> fetchUsers() {
            return restClient.get()
                .uri("http://localhost:8080/users")
                .accept(MediaType.APPLICATION_JSON)
                .retrieve()
                .body(new ParameterizedTypeReference<List<User>>() {});
        }
    }
    ```
    - `get()` spezifiziert die HTTP-Methode.
    - `uri()` setzt den Endpoint.
    - `accept()` setzt den erwarteten Content-Type.
    - `retrieve()` führt die Anfrage aus, und `body()` extrahiert die Antwort, wobei `ParameterizedTypeReference` für generische Typen wie Listen verwendet wird.

4.  **Die Antwort verarbeiten**: Die Antwort wird direkt zurückgegeben, da RestClient synchron ist. Für mehr Kontrolle (z.B. Statuscodes) verwenden Sie `toEntity()`:
    ```java
    import org.springframework.http.ResponseEntity;

    ResponseEntity<List<User>> response = restClient.get()
        .uri("http://localhost:8080/users")
        .accept(MediaType.APPLICATION_JSON)
        .retrieve()
        .toEntity(new ParameterizedTypeReference<List<User>>() {});
    List<User> users = response.getBody();
    ```

#### **Wichtige Punkte**
- RestClient ist synchron und eignet sich daher für traditionelle, blockierende Anwendungen.
- Er wirft Exceptions (z.B. `RestClientException`) bei HTTP-Fehlern, die Sie abfangen und behandeln können.
- Es ist ein Ersatz für `RestTemplate` mit einer intuitiveren API.

---

### **3. Spring WebClient verwenden**
Spring WebClient ist ein reaktiver, nicht-blockierender HTTP-Client, der in Spring WebFlux eingeführt wurde. Er ist für asynchrone Operationen konzipiert und integriert sich mit reaktiven Streams (Mono und Flux).

#### **Schritte zur Verwendung von WebClient**
1.  **Abhängigkeiten hinzufügen**: Fügen Sie die WebFlux-Abhängigkeit zu Ihrem Projekt hinzu:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```

2.  **Eine WebClient-Instanz erstellen**: Instanziieren Sie `WebClient` mit einer Basis-URL oder Standardeinstellungen:
    ```java
    import org.springframework.web.reactive.function.client.WebClient;

    WebClient webClient = WebClient.create("http://localhost:8080");
    ```
    Verwenden Sie `WebClient.builder()` für benutzerdefinierte Konfigurationen (z.B. Codecs, Filter).

3.  **Eine Anfrage erstellen und ausführen**: Verwenden Sie die flüssige API, um die Anfrage zu konstruieren und eine reaktive Antwort abzurufen:
    ```java
    import org.springframework.http.MediaType;
    import org.springframework.web.reactive.function.client.WebClient;
    import reactor.core.publisher.Mono;
    import java.util.List;

    public class UserService {
        private final WebClient webClient;

        public UserService(WebClient webClient) {
            this.webClient = webClient;
        }

        public Mono<List<User>> fetchUsers() {
            return webClient.get()
                .uri("/users")
                .accept(MediaType.APPLICATION_JSON)
                .retrieve()
                .bodyToFlux(User.class)
                .collectList();
        }
    }
    ```
    - `bodyToFlux(User.class)` verarbeitet einen Stream von `User`-Objekten.
    - `collectList()` konvertiert den `Flux<User>` in ein `Mono<List<User>>`.

4.  **Auf die Antwort subscriben**: Da WebClient reaktiv ist, müssen Sie auf das `Mono` oder `Flux` subscriben, um die Anfrage auszulösen:
    ```java
    Mono<List<User>> usersMono = fetchUsers();
    usersMono.subscribe(users -> System.out.println(users));
    ```
    Alternativ können Sie es in einer reaktiven Pipeline verketten oder blockieren (in reaktiven Kontexten nicht empfohlen):
    ```java
    List<User> users = fetchUsers().block();
    ```

#### **Wichtige Punkte**
- WebClient ist nicht-blockierend und ideal für reaktive Anwendungen, die mit Spring WebFlux gebaut wurden.
- Verwenden Sie `Mono` für Einzelwert-Antworten und `Flux` für Mehrwert-Antworten.
- Fehlerbehandlung kann mit Operatoren wie `onErrorResume()` oder `retry()` durchgeführt werden.

---

### **Vergleich und wann man was verwendet**
- **FeignClient**: Verwenden Sie für deklarative, interface-basierte Clients in Microservices-Setups. Er ist synchron und vereinfacht Service-zu-Service-Aufrufe.
- **RestClient**: Verwenden Sie für synchrone HTTP-Anfragen in traditionellen, blockierenden Spring-Anwendungen. Er ist eine moderne Alternative zu `RestTemplate`.
- **WebClient**: Verwenden Sie für reaktive, nicht-blockierende HTTP-Anfragen in WebFlux-basierten Anwendungen oder bei der Handhabung von hoher Parallelität.

---

### **Beispiel: Aufruf eines POST-Endpoints**
Angenommen, Sie müssen einen Benutzer erstellen, indem Sie `POST /users` mit einem `User`-Objekt aufrufen.

#### **FeignClient**
```java
@FeignClient(name = "user-service", url = "http://localhost:8080")
public interface UserClient {
    @PostMapping("/users")
    User createUser(@RequestBody User user);
}

@Service
public class UserService {
    @Autowired
    private UserClient userClient;

    public User createUser(User user) {
        return userClient.createUser(user);
    }
}
```

#### **RestClient**
```java
@Service
public class UserService {
    private final RestClient restClient = RestClient.create();

    public User createUser(User user) {
        return restClient.post()
            .uri("http://localhost:8080/users")
            .contentType(MediaType.APPLICATION_JSON)
            .body(user)
            .retrieve()
            .body(User.class);
    }
}
```

#### **WebClient**
```java
@Service
public class UserService {
    private final WebClient webClient;

    public UserService(WebClient webClient) {
        this.webClient = WebClient.create("http://localhost:8080");
    }

    public Mono<User> createUser(User user) {
        return webClient.post()
            .uri("/users")
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(user)
            .retrieve()
            .bodyToMono(User.class);
    }
}
```

---

### **Zusammenfassung**
- **FeignClient**: Definieren Sie ein Interface, aktivieren Sie es und verwenden Sie es wie eine lokale Bean.
- **RestClient**: Bauen Sie Anfragen flüssig auf und erhalten Sie Antworten synchron.
- **WebClient**: Bauen Sie Anfragen flüssig auf, rufen Sie reaktive Streams ab und verarbeiten Sie sie asynchron.

Wählen Sie basierend auf der Architektur Ihrer Anwendung: FeignClient für Microservices, RestClient für blockierende Apps und WebClient für reaktive Apps. Jedes folgt einem einfachen Einrichtungs- und Verwendungsmuster, wie oben gezeigt.