---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Aktivieren des Java-SSL-TLS-Debugging
translated: true
type: note
---

### Aktivierung der SSL/TLS-Debug-Funktion in Java

Um eine detaillierte Protokollierung für SSL/TLS-bezogene Aktivitäten in Java zu aktivieren (z. B. Handshakes, Zertifikatsvalidierung, Schlüsselaustausch), verwenden Sie die JVM-Systemeigenschaft `-Djavax.net.debug`. Dies gibt Debug-Informationen auf der Konsole (stdout/stderr) aus, wenn Ihre Java-Anwendung läuft.

#### Schritt-für-Schritt-Anleitung

1. **Wählen Sie den Debug-Level**:
   - Verwenden Sie `ssl` für grundlegende SSL/TLS-Handshake-Details.
   - Verwenden Sie `ssl:handshake` für ausführliche Handshake-Meldungen (einschließlich Cipher Suites und Zertifikate).
   - Verwenden Sie `all` für umfassendes Debugging (schließt SSL plus andere Netzwerkprotokolle ein – sparsam verwenden, da es sehr ausführlich ist).
   - Allgemeine Empfehlung: Beginnen Sie mit `ssl:handshake:verbose,keymanager:trustmanager` für gezielte SSL-Einblicke.

2. **Setzen Sie die Eigenschaft beim Ausführen Ihrer Java-Anwendung**:
   - **Kommandozeilen-Ausführung** (z. B. via `java`-Befehl):
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar
     ```
     Ersetzen Sie `your-app.jar` mit Ihrer tatsächlichen Anwendung oder Klasse (z. B. `com.example.Main`).

   - **In einer IDE (z. B. IntelliJ IDEA, Eclipse)**:
     - Gehen Sie zu den Run/Debug-Konfigurationen.
     - Fügen Sie `-Djavax.net.debug=ssl:handshake` zum Feld **VM-Optionen** hinzu.
     - Führen Sie die Konfiguration aus oder debuggen Sie sie.

   - **In einem Build-Tool (z. B. Maven oder Gradle)**:
     - **Maven** (in `pom.xml` unter `<build><plugins><plugin>` für surefire):
       ```xml
       <configuration>
         <argLine>-Djavax.net.debug=ssl:handshake</argLine>
       </configuration>
       ```
     - **Gradle** (in `build.gradle`):
       ```groovy
       test {
         jvmArgs '-Djavax.net.debug=ssl:handshake'
       }
       ```

3. **Erfassen Sie die Logs**:
   - Die Ausgabe erscheint in Ihrer Konsole/ihrem Terminal.
   - Leiten Sie sie zur einfacheren Überprüfung in eine Datei um:
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar > ssl-debug.log 2>&1
     ```
   - Achten Sie auf Zeilen, die mit `***` beginnen (z. B. `*** ClientHello` für Handshake-Starts) oder Präfixe wie `javax.net.ssl`.

4. **Deaktivieren Sie es**:
   - Entfernen Sie einfach das `-D`-Flag, wenn Sie fertig sind – es ist standardmäßig nicht gesetzt, um Leistungseinbußen zu vermeiden.

#### Beispiel für einen Ausgabeausschnitt
Wenn aktiviert, sehen Sie in etwa folgendes:
```
*** ServerHello, TLSv1.2
RandomCookie:  GMT: 1731000000 bytes = { ... }
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
Compression Method: 0
***
```

#### Tipps
- Dies funktioniert für Java 8+ (einschließlich 11, 17, 21). In neueren Versionen können Sie auch `-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3` für protokollspezifische Logs aktivieren.
- Hohe Ausführlichkeit kann Ihre App verlangsamen und die Logs überfluten – testen Sie in einer Entwicklungsumgebung.
- Wenn Sie ein Framework wie Spring Boot verwenden, fügen Sie es zu `application.properties` hinzu: `debug=true` (allgemein) oder über Kommandozeilen-Argumente.

Weitere Details finden Sie in der offiziellen Oracle-Dokumentation: [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names).