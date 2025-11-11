---
audio: false
generated: true
lang: de
layout: post
title: Eigenschaften-Dateiauswahl in Spring Boot
translated: true
type: note
---

In einem Spring Boot Maven-Projekt haben Sie zwei Properties-Dateien, `appProperties.properties` und `appProperties-hk.properties`, die sich unter `src/main/resources` befinden. Um zu steuern, welche Properties-Datei verwendet wird, insbesondere um die Verwendung der `-hk`-Properties festzulegen, können Sie die Konfigurationsmechanismen von Spring Boot nutzen. So können Sie vorgehen:

### Lösung

1. **Erstellen einer `application.properties`-Datei**
   - Standardmäßig sucht Spring Boot nach `application.properties` oder `application.yml` in `src/main/resources`, um Konfigurationseinstellungen zu laden.
   - Um Ihre benutzerdefinierten Properties-Dateien (`appProperties.properties` und `appProperties-hk.properties`) zu verwenden, müssen Sie Spring Boot mitteilen, nach Dateien mit dem Basisnamen `appProperties` anstelle des Standardnamens `application` zu suchen.
   - Fügen Sie die folgende Zeile zu einer neuen `application.properties`-Datei in `src/main/resources` hinzu:

     ```properties
     spring.config.name=appProperties
     ```

   - Diese Einstellung weist Spring Boot an, `appProperties.properties` als Basis-Konfigurationsdatei zu laden. Es sucht automatisch nach profilspezifischen Varianten wie `appProperties-{profile}.properties`, wenn ein Profil aktiv ist.

2. **Verwenden von Spring Profiles, um die `-hk`-Properties festzulegen**
   - Spring Boot unterstützt Profile, die es Ihnen ermöglichen, zusätzliche oder überschreibende Properties-Dateien basierend auf dem aktiven Profil zu laden.
   - Da Ihre Datei `appProperties-hk.properties` heißt, folgt sie dem Muster `appProperties-{profile}.properties`. Hier kann "hk" als Profilname behandelt werden.
   - Um `appProperties-hk.properties` zu verwenden, aktivieren Sie das "hk"-Profil beim Ausführen Ihrer Anwendung. Spring Boot lädt dann sowohl `appProperties.properties` als auch `appProperties-hk.properties`, wobei Properties in `appProperties-hk.properties` eventuell vorhandene gleiche Properties in `appProperties.properties` überschreiben.

3. **So aktivieren Sie das "hk"-Profil**
   - **Über die Kommandozeile**: Geben Sie beim Ausführen Ihrer Spring Boot-Anwendung das aktive Profil mit dem Argument `--spring.profiles.active` an. Zum Beispiel:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     Ersetzen Sie `myapp.jar` durch den Namen Ihrer Anwendungs-JAR-Datei, die von Maven generiert wurde.

   - **Über Maven**: Wenn Sie die Anwendung mit dem `spring-boot:run`-Goal ausführen, konfigurieren Sie das Profil in Ihrer `pom.xml`:
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

   - **Über System Property**: Setzen Sie das Profil als JVM-Argument:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **Über Environment Variable**: Exportieren Sie das Profil in Ihrer Umgebung (z.B. in einem Unix-ähnlichen System):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### Funktionsweise
- Mit `spring.config.name=appProperties`, gesetzt in `application.properties`, verwendet Spring Boot `appProperties` als Basisnamen für Konfigurationsdateien.
- Wenn kein Profil aktiv ist, wird nur `appProperties.properties` geladen.
- Wenn das "hk"-Profil aktiviert ist (z.B. via `--spring.profiles.active=hk`), lädt Spring Boot sowohl `appProperties.properties` als auch `appProperties-hk.properties`. Properties, die in `appProperties-hk.properties` definiert sind, haben Vorrang vor denen in `appProperties.properties`, falls es Duplikate gibt.

### Finale Schritte
- Stellen Sie sicher, dass sich sowohl `appProperties.properties` als auch `appProperties-hk.properties` in `src/main/resources` befinden.
- Fügen Sie `application.properties` mit `spring.config.name=appProperties` zu `src/main/resources` hinzu.
- Führen Sie Ihre Anwendung mit dem aktivierten "hk"-Profil aus, um die `-hk`-Properties zu verwenden.

Dieser Ansatz entspricht den Spring Boot-Konventionen und ist eine typische und unkomplizierte Methode, um zu steuern, welche Properties-Datei in Ihrem Projekt verwendet wird. Um speziell die `-hk`-Properties zu verwenden, aktivieren Sie einfach das "hk"-Profil wie oben beschrieben.