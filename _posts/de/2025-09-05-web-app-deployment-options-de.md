---
audio: false
generated: true
image: false
lang: de
layout: post
title: Bereitstellungsoptionen für Webanwendungen erklärt
translated: true
type: note
---

Verstanden – lassen Sie mich diese Optionen klar für Sie erläutern.

### Option 1: Schnelle Entwicklungseinrichtung (Empfohlen)

Dies ist der einfachste Weg, um das Projekt während der Entwicklung zu starten.
Wenn Ihre `pom.xml` einen Tomcat- oder Jetty-Plugin enthält, können Sie die App direkt ausführen mit:

```bash
mvn tomcat7:run
```

oder

```bash
mvn jetty:run
```

Dies startet die Web-App in einem eingebetteten Tomcat/Jetty, ohne eine WAR-Datei zu erstellen oder manuell bereitzustellen. Wenn Sie das Plugin noch nicht haben, müssten Sie es zuerst in der `pom.xml` hinzufügen.

---

### Option 2: WAR-Datei erstellen und bereitstellen

Dies ist der "traditionellere" Ansatz. Sie packen die Anwendung in eine WAR-Datei:

```bash
mvn clean package
```

Dies erzeugt etwas wie `target/playground-server-1.0.war`.
Sie kopieren dann diese WAR-Datei in den `webapps/`-Ordner eines eigenständigen Tomcat/Jetty-Servers, starten den Server neu und rufen die bereitgestellte App im Browser auf.

---

### Option 3: Eingebetteten Server verwenden (Manuelle Einrichtung)

Aktuell startet Ihre `Application.main()`-Methode nur den Spring-Kontext – sie startet keinen echten Web-Server.
Wenn Sie möchten, dass die App selbst Tomcat startet (ohne einen externen Server zu benötigen), müssten Sie Ihre Hauptklasse so ändern, dass sie eine eingebettete Tomcat-Instanz programmatisch einrichtet und startet.

Dies gibt Ihnen eine eigenständige, ausführbare JAR-Datei, erfordert aber zusätzlichen Setup-Code.

---

### Option 4: Spring Boot Migration

Dieses Projekt hat **einiges an Spring Boot Test-Setup**, ist aber noch keine echte Spring Boot App. Deshalb funktioniert der Befehl:

```bash
mvn spring-boot:run
```

nicht.

Falls gewünscht, können Sie migrieren:

* Fügen Sie die richtigen Spring Boot Starter Dependencies hinzu.
* Ändern Sie Ihre Hauptklasse zu `@SpringBootApplication`.
* Dann könnten Sie die App einfach mit `mvn spring-boot:run` oder sogar `java -jar target/app.jar` ausführen.

Dies ist der modernste Ansatz, erfordert jedoch einige Änderungen an Ihrem Code und der `pom.xml`.

---

✅ **Kurz gesagt**:

* Wenn Sie nur schnell testen möchten → verwenden Sie **Option 1**.
* Wenn Sie auf einem existierenden Server bereitstellen → verwenden Sie **Option 2**.
* Wenn Sie eine eigenständige App ohne externen Tomcat möchten → verwenden Sie **Option 3**.
* Wenn Sie langfristig modernisieren und vereinfachen möchten → verwenden Sie **Option 4**.

---

Möchten Sie, dass ich Ihnen den **exakten `pom.xml`-Ausschnitt** für Option 1 (Tomcat/Jetty-Plugin) zeige, damit Sie sofort `mvn tomcat7:run` ausführen können?