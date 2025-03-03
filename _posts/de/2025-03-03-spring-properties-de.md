---
audio: false
generated: true
lang: de
layout: post
title: Eigenschaften Datei Auswahl in Spring Boot
translated: true
---

In einem Spring Boot Maven-Projekt haben Sie zwei Properties-Dateien, `appProperties.properties` und `appProperties-hk.properties`, die sich unter `src/main/resources` befinden. Um zu steuern, welche Properties-Datei verwendet wird, insbesondere um die Verwendung der `-hk`-Properties zu spezifizieren, können Sie die Konfigurationsmechanismen von Spring Boot nutzen. Hier ist, wie Sie dies tun können:

### Lösung

1. **Erstellen Sie eine `application.properties`-Datei**
   - Standardmäßig sucht Spring Boot nach `application.properties` oder `application.yml` in `src/main/resources`, um Konfigurationseinstellungen zu laden.
   - Um Ihre benutzerdefinierten Properties-Dateien (`appProperties.properties` und `appProperties-hk.properties`) zu verwenden, müssen Sie Spring Boot anweisen, nach Dateien mit dem Basisnamen `appProperties` anstatt dem Standard `application` zu suchen.
   - Fügen Sie die folgende Zeile zu einer neuen `application.properties`-Datei in `src/main/resources` hinzu:

     ```properties
     spring.config.name=appProperties
     ```

   - Diese Einstellung weist Spring Boot an, `appProperties.properties` als die Basis-Konfigurationsdatei zu laden, und es wird auch automatisch nach profil-spezifischen Varianten wie `appProperties-{profile}.properties` suchen, wenn ein Profil aktiv ist.

2. **Verwenden Sie Spring-Profiles, um die `-hk`-Properties zu spezifizieren**
   - Spring Boot unterstützt Profile, die es ermöglichen, zusätzliche oder überschreibende Properties-Dateien basierend auf dem aktiven Profil zu laden.
   - Da Ihre Datei `appProperties-hk.properties` heißt, folgt sie dem Muster `appProperties-{profile}.properties`. Hier kann "hk" als Profilname behandelt werden.
   - Um `appProperties-hk.properties` zu verwenden, aktivieren Sie das "hk"-Profil beim Starten Ihrer Anwendung. Spring Boot wird dann sowohl `appProperties.properties` als auch `appProperties-hk.properties` laden, wobei die Eigenschaften in `appProperties-hk.properties` alle übereinstimmenden Eigenschaften in `appProperties.properties` überschreiben.

3. **Aktivieren des "hk"-Profils**
   - **Über die Kommandozeile**: Wenn Sie Ihre Spring Boot-Anwendung ausführen, geben Sie das aktive Profil mit dem Argument `--spring.profiles.active` an. Zum Beispiel:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     Ersetzen Sie `myapp.jar` durch den Namen der von Maven erzeugten JAR-Datei Ihrer Anwendung.

   - **Über Maven**: Wenn Sie die Anwendung mit dem Ziel `spring-boot:run` ausführen, konfigurieren Sie das Profil in Ihrer `pom.xml`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     Führen Sie dann aus:
     ```bash
     mvn spring-boot:run
     ```

   - **Über Systemeigenschaft**: Legen Sie das Profil als JVM-Argument fest:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **Über Umgebungsvariable**: Exportieren Sie das Profil in Ihrer Umgebung (z.B. in einem Unix-ähnlichen System):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### So funktioniert es
- Mit `spring.config.name=appProperties` in `application.properties` verwendet Spring Boot `appProperties` als Basisnamen für Konfigurationsdateien.
- Wenn kein Profil aktiv ist, wird nur `appProperties.properties` geladen.
- Wenn das "hk"-Profil aktiviert wird (z.B. über `--spring.profiles.active=hk`), lädt Spring Boot sowohl `appProperties.properties` als auch `appProperties-hk.properties`. Eigenschaften, die in `appProperties-hk.properties` definiert sind, haben Vorrang vor denen in `appProperties.properties`, falls es Duplikate gibt.

### Abschlussschritte
- Stellen Sie sicher, dass sich sowohl `appProperties.properties` als auch `appProperties-hk.properties` in `src/main/resources` befinden.
- Fügen Sie `application.properties` mit `spring.config.name=appProperties` zu `src/main/resources` hinzu.
- Führen Sie Ihre Anwendung mit dem aktivierten "hk"-Profil aus, um die `-hk`-Properties zu verwenden.

Dieser Ansatz entspricht den Spring Boot-Konventionen und ist eine typische und einfache Möglichkeit, um zu steuern, welche Properties-Datei in Ihrem Projekt verwendet wird. Um spezifisch die `-hk`-Properties zu verwenden, aktivieren Sie einfach das "hk"-Profil, wie oben beschrieben.