---
audio: false
generated: true
lang: de
layout: post
title: Nutzung von httpmine
translated: true
type: note
---

Ich nehme an, Sie meinten "httpmime.jar" und nicht "httpmine.jar", da "httpmime" eine bekannte Bibliothek von Apache HttpComponents ist, die zur Verarbeitung von MIME-Multipart-Entitäten in HTTP-Anfragen (z.B. für Datei-Uploads) verwendet wird. Falls ich mich irre, klären Sie mich bitte auf! So verwenden Sie die `httpmime.jar` in einem Java-Projekt:

---

### Was ist `httpmime.jar`?
Die `httpmime.jar` ist Teil des Apache HttpComponents-Projekts. Sie erweitert die Funktionalität von `httpclient.jar` um Unterstützung für multipart/form-data-Anfragen, die häufig für das Hochladen von Dateien oder das Senden komplexer Daten über HTTP verwendet werden.

Um sie zu verwenden, benötigen Sie auch ihre Abhängigkeiten, wie `httpclient.jar` und `httpcore.jar`, da `httpmime` auf diesen Bibliotheken aufbaut.

---

### Schritte zur Verwendung von `httpmime.jar` in Ihrem Java-Projekt

#### 1. **JAR-Datei herunterladen**
- Besuchen Sie die [Apache HttpComponents Downloads-Seite](https://hc.apache.org/downloads.cgi) oder das Maven Repository für `httpmime` (z.B. [Version 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)).
- Laden Sie die `httpmime-<Version>.jar`-Datei herunter (z.B. `httpmime-4.5.14.jar`).
- Sie benötigen außerdem:
  - `httpclient-<Version>.jar` (z.B. `httpclient-4.5.14.jar`)
  - `httpcore-<Version>.jar` (z.B. `httpcore-4.4.16.jar`)
- Stellen Sie sicher, dass die Versionen kompatibel sind (prüfen Sie die [Projektabhängigkeiten](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)).

Alternativ, wenn Sie Maven oder Gradle verwenden, überspringen Sie den manuellen Download und fügen Sie es über Ihr Build-Tool hinzu (siehe Schritt 2).

#### 2. **JAR zum Projekt hinzufügen**
- **Manuelle Methode (Ohne Build-Tools):**
  - Platzieren Sie die heruntergeladenen `httpmime.jar`-, `httpclient.jar`- und `httpcore.jar`-Dateien in einem Ordner (z.B. `lib/` in Ihrem Projektverzeichnis).
  - Wenn Sie eine IDE wie Eclipse oder IntelliJ verwenden:
    - **Eclipse**: Rechtsklick auf Ihr Projekt > Properties > Java Build Path > Libraries > Add External JARs > Wählen Sie die JARs aus > Apply.
    - **IntelliJ**: File > Project Structure > Modules > Dependencies > "+" > JARs or directories > Wählen Sie die JARs aus > OK.
  - Wenn Sie von der Kommandozeile aus ausführen, schließen Sie die JARs in Ihren Classpath ein:
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" YourClass.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." YourClass
    ```

- **Maven verwenden (Empfohlen):**
  Fügen Sie dies zu Ihrer `pom.xml` hinzu:
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- Verwenden Sie die neueste Version -->
  </dependency>
  ```
  Maven lädt automatisch `httpclient` und `httpcore` als transitive Abhängigkeiten.

- **Gradle verwenden:**
  Fügen Sie dies zu Ihrer `build.gradle` hinzu:
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **Code schreiben, um `httpmime` zu verwenden**
Hier ist ein Beispiel für die Verwendung von `httpmime` zum Hochladen einer Datei über eine multipart HTTP POST-Anfrage:

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
        // Einen HTTP-Client erstellen
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // Die URL definieren, an die die Anfrage gesendet werden soll
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // Die Multipart-Entität aufbauen
        File file = new File("path/to/your/file.txt"); // Ersetzen Sie mit Ihrem Dateipfad
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // Datei hinzufügen
        builder.addTextBody("description", "This is a test file"); // Textfeld hinzufügen (optional)

        // Die Entität der POST-Anfrage zuweisen
        httpPost.setEntity(builder.build());

        // Die Anfrage ausführen
        HttpResponse response = httpClient.execute(httpPost);

        // Den Antwortstatus ausgeben
        System.out.println("Response Code: " + response.getStatusLine().getStatusCode());

        // Aufräumen
        httpClient.close();
    }
}
```

#### 4. **Wichtige Klassen und Verwendung**
- **`MultipartEntityBuilder`**: Wird verwendet, um die Multipart-Entität zu konstruieren. Sie können Dateien (`addPart`), Text (`addTextBody`) oder Binärdaten (`addBinaryBody`) hinzufügen.
- **`FileBody`**: Stellt eine hochzuladende Datei dar.
- **`CloseableHttpClient`**: Der HTTP-Client aus `httpclient.jar` zum Ausführen der Anfrage.

#### 5. **Ihr Programm ausführen**
- Wenn Sie eine IDE verwenden, führen Sie das Programm einfach aus.
- Wenn Sie die Kommandozeile verwenden, kompilieren und führen Sie es mit dem oben gezeigten Classpath aus.

#### 6. **Fehlerbehebung**
- **ClassNotFoundException**: Stellen Sie sicher, dass alle erforderlichen JARs (`httpmime`, `httpclient`, `httpcore`) in Ihrem Classpath sind.
- **Versionskonflikt**: Verwenden Sie kompatible Versionen der JARs (z.B. `httpmime-4.5.14` mit `httpclient-4.5.14` und `httpcore-4.4.16`).
- **Android-Projekte**: Android hat sein eigenes `org.apache.http`-Paket, das zu Konflikten führen kann. Schließen Sie entweder die eingebaute Version aus oder verwenden Sie eine neu verpackte JAR (z.B. über JarJar).

---

### Beispiel-Anwendungsfall
Wenn Sie eine Datei auf einen Server hochladen (wie eine REST API), vereinfacht `httpmime` die Erstellung der `multipart/form-data`-Anfrage, die ein Standard für Datei-Uploads ist.

Lassen Sie mich wissen, wenn Sie Erklärungen oder Hilfe bei einem bestimmten Szenario benötigen!