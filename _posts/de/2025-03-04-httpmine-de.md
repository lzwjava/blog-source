---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von Httpmine
translated: true
---

Ich nehme an, dass Sie "httpmime.jar" statt "httpmine.jar" meinten, da "httpmime" eine bekannte Bibliothek von Apache HttpComponents ist, die zur Verarbeitung von MIME-Multipart-Entitäten in HTTP-Anfragen (z.B. Datei-Uploads) verwendet wird. Wenn ich das falsch verstanden habe, bitte um Klärung! Hier ist, wie man `httpmime.jar` in einem Java-Projekt verwendet:

---

### Was ist `httpmime.jar`?
`httpmime.jar` ist Teil des Apache HttpComponents-Projekts. Es erweitert die Funktionalität von `httpclient.jar`, indem es Unterstützung für `multipart/form-data`-Anfragen bietet, die häufig zum Hochladen von Dateien oder zum Senden komplexer Daten über HTTP verwendet werden.

Um es zu verwenden, benötigen Sie auch dessen Abhängigkeiten wie `httpclient.jar` und `httpcore.jar`, da `httpmime` auf diesen Bibliotheken aufbaut.

---

### Schritte zur Verwendung von `httpmime.jar` in Ihrem Java-Projekt

#### 1. **Herunterladen der JAR-Datei**
- Besuchen Sie die [Apache HttpComponents Download-Seite](https://hc.apache.org/downloads.cgi) oder das Maven-Repository für `httpmime` (z.B. [Version 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)).
- Laden Sie die `httpmime-<version>.jar`-Datei (z.B. `httpmime-4.5.14.jar`) herunter.
- Sie benötigen auch:
  - `httpclient-<version>.jar` (z.B. `httpclient-4.5.14.jar`)
  - `httpcore-<version>.jar` (z.B. `httpcore-4.4.16.jar`)
- Stellen Sie sicher, dass die Versionen kompatibel sind (überprüfen Sie die [Projektabhängigkeiten](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)).

Alternativ, wenn Sie Maven oder Gradle verwenden, überspringen Sie den manuellen Download und fügen Sie es über Ihr Build-Tool hinzu (siehe Schritt 2).

#### 2. **Fügen Sie die JAR-Datei zu Ihrem Projekt hinzu**
- **Manuelle Methode (ohne Build-Tools):**
  - Platzieren Sie die heruntergeladenen `httpmime.jar`, `httpclient.jar` und `httpcore.jar`-Dateien in einem Ordner (z.B. `lib/` in Ihrem Projektverzeichnis).
  - Wenn Sie eine IDE wie Eclipse oder IntelliJ verwenden:
    - **Eclipse**: Klicken Sie mit der rechten Maustaste auf Ihr Projekt > Eigenschaften > Java Build Path > Bibliotheken > Externe JARs hinzufügen > Wählen Sie die JARs aus > Übernehmen.
    - **IntelliJ**: Datei > Projektstruktur > Module > Abhängigkeiten > "+" > JARs oder Verzeichnisse > Wählen Sie die JARs aus > OK.
  - Wenn Sie von der Befehlszeile aus ausführen, schließen Sie die JARs in Ihren Klassenpfad ein:
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" YourClass.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." YourClass
    ```

- **Verwendung von Maven (empfohlen):**
  Fügen Sie dies zu Ihrer `pom.xml` hinzu:
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- Verwenden Sie die neueste Version -->
  </dependency>
  ```
  Maven wird `httpclient` und `httpcore` automatisch als transitive Abhängigkeiten herunterladen.

- **Verwendung von Gradle:**
  Fügen Sie dies zu Ihrer `build.gradle` hinzu:
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **Schreiben Sie Code zur Verwendung von `httpmime`**
Hier ist ein Beispiel zur Verwendung von `httpmime`, um eine Datei über eine multipart HTTP POST-Anfrage hochzuladen:

```java
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.HttpResponse;
import java.io.File;

public class FileUploadExample {
    public static void main(String[] args) throws Exception {
        // Erstellen Sie einen HTTP-Client
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // Definieren Sie die URL, an die die Anfrage gesendet werden soll
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // Bauen Sie die multipart-Entität
        File file = new File("path/to/your/file.txt"); // Ersetzen Sie durch Ihren Dateipfad
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // Fügen Sie die Datei hinzu
        builder.addTextBody("description", "Dies ist eine Testdatei"); // Fügen Sie ein Textfeld hinzu (optional)

        // Setzen Sie die Entität für die POST-Anfrage
        httpPost.setEntity(builder.build());

        // Führen Sie die Anfrage aus
        HttpResponse response = httpClient.execute(httpPost);

        // Drucken Sie den Antwortstatus
        System.out.println("Antwortcode: " + response.getStatusLine().getStatusCode());

        // Aufräumen
        httpClient.close();
    }
}
```

#### 4. **Wichtige Klassen und Verwendung**
- **`MultipartEntityBuilder`**: Wird verwendet, um die multipart-Entität zu erstellen. Sie können Dateien (`addPart`), Text (`addTextBody`) oder binäre Daten (`addBinaryBody`) hinzufügen.
- **`FileBody`**: Stellt eine hochzuladende Datei dar.
- **`CloseableHttpClient`**: Der HTTP-Client aus `httpclient.jar`, um die Anfrage auszuführen.

#### 5. **Führen Sie Ihr Programm aus**
- Wenn Sie eine IDE verwenden, führen Sie einfach das Programm aus.
- Wenn Sie die Befehlszeile verwenden, kompilieren und führen Sie es mit dem oben gezeigten Klassenpfad aus.

#### 6. **Fehlerbehebung**
- **ClassNotFoundException**: Stellen Sie sicher, dass alle erforderlichen JARs (`httpmime`, `httpclient`, `httpcore`) in Ihrem Klassenpfad sind.
- **Versionskonflikt**: Verwenden Sie kompatible Versionen der JARs (z.B. `httpmime-4.5.14` mit `httpclient-4.5.14` und `httpcore-4.4.16`).
- **Android-Projekte**: Android hat sein eigenes `org.apache.http`-Paket, das möglicherweise Konflikte verursacht. Entweder schließen Sie die eingebaute Version aus oder verwenden Sie eine neu verpackte JAR (z.B. über JarJar).

---

### Beispielanwendung
Wenn Sie eine Datei auf einen Server (z.B. eine REST-API) hochladen, vereinfacht `httpmime` das Erstellen der `multipart/form-data`-Anfrage, die ein Standard für Datei-Uploads ist.

Lassen Sie mich wissen, wenn Sie eine Klärung oder Hilfe bei einem bestimmten Szenario benötigen!