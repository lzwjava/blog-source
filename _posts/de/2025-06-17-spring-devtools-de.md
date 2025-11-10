---
audio: false
generated: true
lang: de
layout: post
title: Spring Boot DevTools Für Automatischen Neustart
translated: true
type: note
---

Wenn Sie eine Spring Boot-Anwendung mit `mvn spring-boot:run` ausführen, sind Datei-Beobachter und Auto-Restart- oder Hot-Reload-Funktionen standardmäßig nicht aktiviert. Sie können sie jedoch aktivieren, indem Sie die `spring-boot-devtools`-Abhängigkeit zu Ihrem Projekt hinzufügen. Dieses Modul bietet Funktionen wie automatische Neustarts und LiveReload für eine schnellere Entwicklung.

### Details
1. **Standardverhalten Ohne DevTools**:
   - Die Ausführung von `mvn spring-boot:run` ohne `spring-boot-devtools` beinhaltet keine Datei-Beobachter oder Auto-Restart-Funktion. Sie müssen die Anwendung manuell stoppen und neu starten, um Änderungen an Java-Klassen, statischen Ressourcen oder Templates zu übernehmen.
   - Statische Ressourcen (z.B. HTML, CSS, JS) erfordern möglicherweise einen vollständigen Rebuild oder Neustart, sofern nicht anders konfiguriert.

2. **Mit `spring-boot-devtools`**:
   - **Datei-Beobachter**: DevTools überwacht den Classpath auf Änderungen an Java-Dateien, Properties und bestimmten Ressourcen (z.B. `/resources`, `/static`, `/templates`).
   - **Auto-Restart**: Wenn sich eine Datei auf dem Classpath ändert (z.B. eine Java-Klasse oder Properties-Datei), löst DevTools einen automatischen Neustart der Anwendung aus. Dieser ist schneller als ein Kaltstart, da zwei Classloader verwendet werden: einen für unveränderte Third-Party-Bibliotheken (Basis-Classloader) und einen anderen für Ihren Anwendungscode (Restart-Classloader).[](https://docs.spring.io/spring-boot/reference/using/devtools.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - **LiveReload**: Änderungen an statischen Ressourcen (z.B. HTML, CSS, JS in `/static`, `/public` oder `/templates`) oder Templates (z.B. Thymeleaf) lösen eine Browser-Aktualisierung aus, anstelle eines vollständigen Neustarts, sofern Sie eine LiveReload-Browser-Erweiterung installiert haben (unterstützt für Chrome, Firefox, Safari).[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)
   - **Ausschlüsse**: Standardmäßig lösen Ressourcen in `/META-INF/maven`, `/META-INF/resources`, `/resources`, `/static`, `/public` und `/templates` keinen Neustart aus, aber sehr wohl einen LiveReload. Sie können dies mit `spring.devtools.restart.exclude` anpassen.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

3. **Einrichtung für DevTools**:
   Fügen Sie Ihrem `pom.xml` die folgende Abhängigkeit hinzu:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
   - Das `<optional>true</optional>` stellt sicher, dass DevTools nicht in Produktions-Builds enthalten ist.[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)
   - Führen Sie die Anwendung mit `mvn spring-boot:run` aus. DevTools aktiviert automatisch die Datei-Überwachung und den Auto-Restart.

4. **Verhalten in IDEs**:
   - **Eclipse**: Das Speichern von Änderungen (Strg+S) löst automatisch einen Build aus, den DevTools erkennt und die Anwendung neu startet.[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)
   - **IntelliJ IDEA**: Sie müssen manuell einen Build auslösen (Strg+F9 oder "Make Project"), damit DevTools Änderungen erkennt, sofern Sie keinen Auto-Build konfigurieren. Alternativ können Sie "Build project automatically" in den IntelliJ-Einstellungen aktivieren, um nahtlose Neustarts zu ermöglichen.[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-restart-and-live-reload-in-intellij-idea)
   - Für LiveReload installieren Sie die Browser-Erweiterung von http://livereload.com/extensions/ und aktivieren sie.[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)

5. **Alternative: Spring Loaded**:
   - Anstelle von DevTools können Sie Spring Loaded für erweitertes Hot-Swapping verwenden (z.B. Methodensignatur-Änderungen). Fügen Sie es dem `spring-boot-maven-plugin` hinzu:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <dependencies>
             <dependency>
                 <groupId>org.springframework</groupId>
                 <artifactId>springloaded</artifactId>
                 <version>1.2.8.RELEASE</version>
             </dependency>
         </dependencies>
     </plugin>
     ```
   - Spring Loaded ist weniger empfehlenswert als DevTools, da es nicht so aktiv gepflegt wird und möglicherweise nicht alle Frameworks unterstützt.[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/howto-hotswapping.html)

6. **Hot-Reloading Statischer Ressourcen**:
   - Ohne DevTools können Sie Hot-Reloading für statische Ressourcen aktivieren, indem Sie die `addResources`-Property des `spring-boot-maven-plugin` setzen:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <addResources>true</addResources>
         </configuration>
     </plugin>
     ```
   - Dies fügt `src/main/resources` zum Classpath hinzu und ermöglicht die direkte Bearbeitung statischer Dateien, ist aber weniger umfassend als DevTools.[](https://docs.spring.io/spring-boot/maven-plugin/run.html)

7. **Einschränkungen**:
   - DevTools kann Classloading-Probleme in Multi-Modul-Projekten verursachen. Wenn dies passiert, versuchen Sie, den Restart mit `spring.devtools.restart.enabled=false` zu deaktivieren, oder verwenden Sie JRebel für erweitertes Reloading.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)
   - Für Dateien außerhalb des Classpaths verwenden Sie `spring.devtools.restart.additional-paths`, um zusätzliche Verzeichnisse zu überwachen.[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - LiveReload erfordert eine Browser-Erweiterung und funktioniert möglicherweise nicht für alle Front-End-Setups (z.B. React mit Webpack).[](https://stackoverflow.com/questions/49888724/hot-reload-for-spring-boot-backend-frontend)
   - Wenn Neustarts langsam sind, passen Sie `spring.devtools.restart.poll-interval` und `spring.devtools.restart.quiet-period` an, um die Datei-Überwachung zu optimieren.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

### Schritte für eine Einfache App
1. Erstellen Sie eine einfache Spring Boot-App (z.B. mit Spring Initializr und `spring-boot-starter-web`).
2. Fügen Sie die `spring-boot-devtools`-Abhängigkeit zur `pom.xml` hinzu.
3. Führen Sie `mvn spring-boot:run` aus.
4. Modifizieren Sie eine Java-Datei, Properties-Datei oder statische Ressource (z.B. HTML in `src/main/resources/static`).
5. Beobachten Sie den Auto-Restart (für Java/Properties) oder die Browser-Aktualisierung (für statische Ressourcen mit aktiviertem LiveReload).

### Beispiel
Für eine einfache App mit einem REST-Controller:
```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```
- Fügen Sie DevTools hinzu, führen Sie `mvn spring-boot:run` aus und ändern Sie den Rückgabewert der `hello()`-Methode. Die App startet automatisch neu.
- Fügen Sie eine `index.html` in `src/main/resources/static` hinzu, installieren Sie die LiveReload-Erweiterung und ändern Sie das HTML. Der Browser aktualisiert sich ohne Neustart.

### Fazit
Für eine einfache Spring Boot-App ist das Hinzufügen von `spring-boot-devtools` der einfachste Weg, um Datei-Beobachter, Auto-Restart und Hot-Reloading zu aktivieren. Verwenden Sie `mvn spring-boot:run` mit DevTools für eine nahtlose Entwicklungserfahrung. Wenn Sie erweitertes Hot-Swapping benötigen, ziehen Sie Spring Loaded oder JRebel in Betracht, aber DevTools ist für die meisten Fälle ausreichend.[](https://www.geeksforgeeks.org/hot-reload-with-spring-boot-devtools/)[](https://docs.spring.io/spring-boot/how-to/hotswapping.html)

---

Unten finden Sie ein Beispiel, wie Sie `spring-boot-devtools` für Datei-Überwachung, Auto-Restart und Hot-Reloading in Ihrer Spring Boot-Anwendung mit einer `application.yml`-Datei konfigurieren. Diese Konfiguration ist auf Ihr `blog-server`-Projekt zugeschnitten, basierend auf den von Ihnen bereitgestellten Logs, die zeigen, dass DevTools aktiv ist und `target/classes` überwacht.

### `application.yml` Konfiguration
```yaml
spring:
  devtools:
    restart:
      # Auto-Restart aktivieren (Standard: true)
      enabled: true
      # Zusätzliche Verzeichnisse, die auf Neustarts überwacht werden sollen (z.B. benutzerdefinierter Config-Ordner)
      additional-paths:
        - /home/lzw/Projects/blog-server/config
      # Dateien/Verzeichnisse, die keinen Neustart auslösen sollen (Standard-Ausschlüsse beibehalten)
      exclude: static/**,public/**,templates/**,logs/**,generated/**
      # Abfrageintervall für Dateiänderungen (in Millisekunden, Standard: 1000)
      poll-interval: 1000
      # Ruheperiode nach Dateiänderungen vor dem Neustart (in Millisekunden, Standard: 400)
      quiet-period: 400
      # Optional: Datei zum manuellen Auslösen von Neustarts
      trigger-file: .restart
    livereload:
      # LiveReload für Browser-Aktualisierung bei Änderungen an statischen Ressourcen aktivieren (Standard: true)
      enabled: true
```

### Erklärung der Einstellungen
- **`spring.devtools.restart.enabled`**: Aktiviert den Auto-Restart, wenn sich Classpath-Dateien ändern (z.B. `target/classes`, wie in Ihrem Log zu sehen: `file:/home/lzw/Projects/blog-server/target/classes/`).
- **`spring.devtools.restart.additional-paths`**: Überwacht zusätzliche Verzeichnisse (z.B. `/home/lzw/Projects/blog-server/config`) auf Änderungen, um Neustarts auszulösen.
- **`spring.devtools.restart.exclude`**: Verhindert Neustarts bei Änderungen in `static/`, `public/`, `templates/`, `logs/` oder `generated/` Verzeichnissen, erlaubt aber gleichzeitig LiveReload für statische Ressourcen (z.B. HTML, CSS, JS).
- **`spring.devtools.restart.poll-interval`**: Legt fest, wie oft DevTools auf Dateiänderungen prüft (1000ms = 1 Sekunde).
- **`spring.devtools.restart.quiet-period`**: Wartet 400ms nach Erkennen einer Änderung, um sicherzustellen, dass keine weiteren Änderungen anstehen, bevor der Neustart erfolgt.
- **`spring.devtools.restart.trigger-file`**: Ermöglicht manuelle Neustarts durch Aktualisieren von `.restart` (z.B. `touch /home/lzw/Projects/blog-server/.restart`).
- **`spring.devtools.livereload.enabled`**: Aktiviert den LiveReload-Server, der Browser-Aktualisierungen für Änderungen in `static/` oder `templates/` auslöst (erfordert eine LiveReload-Browser-Erweiterung).

### Schritte zur Anwendung
1. Erstellen oder aktualisieren Sie `src/main/resources/application.yml` mit der obigen Konfiguration.
2. Stellen Sie sicher, dass `spring-boot-devtools` in Ihrer `pom.xml` enthalten ist:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
3. Führen Sie `mvn spring-boot:run` aus. DevTools überwacht `target/classes` und `/home/lzw/Projects/blog-server/config` (falls hinzugefügt), startet die App bei Änderungen an Java- oder Properties-Dateien neu und aktualisiert den Browser bei Änderungen an statischen Ressourcen.
4. Installieren Sie für LiveReload eine Browser-Erweiterung (z.B. von http://livereload.com/extensions/) oder integrieren Sie einen LiveReload-Client in Ihr Front-End.

### Hinweise
- Ihre Logs zeigen einen schnellen Start (0,8 Sekunden), daher sollten das standardmäßige `poll-interval` und `quiet-period` in Ordnung sein. Passen Sie sie an (z.B. `poll-interval: 500`), wenn sich Neustarts in einem größeren Projekt träge anfühlen.
- Wenn Sie LiveReload nicht benötigen (z.B. bei Verwendung eines separaten Front-End-Dev-Servers), setzen Sie `livereload.enabled: false`.
- Für manuelle Neustarts erstellen Sie `.restart` in Ihrem Projektstammverzeichnis und aktualisieren Sie es bei Bedarf.

Diese YAML-Konfiguration sollte nahtlos mit Ihrem Setup funktionieren und die Datei-Überwachungs- und Auto-Restart-Funktionen, die Sie bereits sehen, verbessern.