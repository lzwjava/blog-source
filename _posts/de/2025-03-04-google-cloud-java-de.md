---
audio: false
generated: true
lang: de
layout: post
title: Google Cloud Java Client
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Sie zur Verwendung von `com.google.cloud` in Java eine Java-Entwicklungsumgebung einrichten, Abhängigkeiten der Google Cloud Client-Bibliothek einbinden, die Authentifizierung konfigurieren und die Bibliotheken zur Interaktion mit Google Cloud-Diensten verwenden müssen.
- Recherchen deuten darauf hin, dass die Authentifizierung automatisch auf Google Cloud-Plattformen gehandhabt oder manuell für die lokale Entwicklung unter Verwendung von Dienstkonto-Anmeldedaten eingerichtet werden kann.
- Die Hinweise sprechen dafür, Maven oder Gradle für die Verwaltung von Abhängigkeiten zu verwenden, wobei Beispiele für Cloud Storage als gängiger Anwendungsfall bereitgestellt werden.

### Einrichten Ihrer Entwicklungsumgebung
Stellen Sie zunächst sicher, dass Sie ein Java Development Kit (JDK) Version 8 oder höher installiert haben, zusammen mit einem Build-Tool wie Maven oder Gradle. Diese Tools helfen bei der Verwaltung Ihrer Projektabhängigkeiten und Build-Prozesse.

### Einbinden von Abhängigkeiten
Fügen Sie Ihrem Projekt die Abhängigkeiten der Google Cloud Client-Bibliothek hinzu. Fügen Sie für Maven die Bill of Materials (BOM) und spezifische Dienstbibliotheken in Ihre `pom.xml`-Datei ein. Zum Beispiel, um Cloud Storage zu verwenden:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Ersetzen Sie "latest_version" durch die tatsächliche Version aus dem [Google Cloud Java Client-Bibliotheken GitHub-Repository](https://github.com/googleapis/google-cloud-java).

### Konfigurieren der Authentifizierung
Die Authentifizierung wird oft automatisch durchgeführt, wenn Ihre Anwendung auf Google Cloud-Plattformen wie Compute Engine oder App Engine läuft. Für die lokale Entwicklung setzen Sie die Umgebungsvariable `GOOGLE_APPLICATION_CREDENTIALS` auf den Pfad zu einer JSON-Schlüsseldatei eines Dienstkontos oder konfigurieren sie programmatisch.

### Verwenden der Bibliotheken
Sobald eingerichtet, importieren Sie die notwendigen Klassen, erstellen Sie ein Dienstobjekt und führen Sie API-Aufrufe durch. Zum Beispiel, um Buckets in Cloud Storage aufzulisten:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Ein unerwartetes Detail ist, dass die Bibliotheken verschiedene Google Cloud-Dienste unterstützen, jeder mit seinem eigenen Unterpaket unter `com.google.cloud`, wie z.B. `com.google.cloud.bigquery` für BigQuery, und damit Funktionalität weit über Storage hinaus bieten.

---

### Umfragehinweis: Umfassende Anleitung zur Verwendung von `com.google.cloud` in Java

Dieser Hinweis bietet eine detaillierte Erkundung der Verwendung der Google Cloud Java Client-Bibliotheken, mit speziellem Fokus auf das Paket `com.google.cloud`, um mit Google Cloud-Diensten zu interagieren. Er erweitert die direkte Antwort, indem er alle relevanten Details aus der Recherche enthält, klar und tiefgehend organisiert, geeignet für Entwickler, die ein gründliches Verständnis suchen.

#### Einführung in die Google Cloud Java Client-Bibliotheken
Die Google Cloud Java Client-Bibliotheken, zugänglich unter dem Paket `com.google.cloud`, bieten idiomatische und intuitive Schnittstellen für die Interaktion mit Google Cloud-Diensten wie Cloud Storage, BigQuery und Compute Engine. Diese Bibliotheken sind darauf ausgelegt, Boilerplate-Code zu reduzieren, Low-Level-Kommunikationsdetails zu handhaben und sich nahtlos in Java-Entwicklungspraktiken zu integrieren. Sie sind besonders nützlich für die Entwicklung Cloud-nativer Anwendungen, die Tools wie Spring, Maven und Kubernetes nutzen, wie in der offiziellen Dokumentation hervorgehoben.

#### Einrichten der Entwicklungsumgebung
Zu Beginn wird ein Java Development Kit (JDK) Version 8 oder höher benötigt, um die Kompatibilität mit den Bibliotheken sicherzustellen. Die empfohlene Distribution ist Eclipse Temurin, eine Open-Source, Java SE TCK-zertifizierte Option, wie in Setup-Anleitungen vermerkt. Zusätzlich ist ein Build-Automatisierungstool wie Maven oder Gradle essentiell für die Verwaltung von Abhängigkeiten. Die Google Cloud CLI (`gcloud`) kann ebenfalls installiert werden, um über die Kommandozeile mit Ressourcen zu interagieren und so Bereitstellungs- und Überwachungsaufgaben zu erleichtern.

#### Verwalten von Abhängigkeiten
Die Abhängigkeitsverwaltung wird durch die von Google Cloud bereitgestellte Bill of Materials (BOM) vereinfacht, die hilft, Versionen über mehrere Bibliotheken hinweg zu verwalten. Für Maven fügen Sie Folgendes zu Ihrer `pom.xml` hinzu:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Für Gradle gelten ähnliche Konfigurationen, um Versionskonsistenz sicherzustellen. Die Versionsnummer sollte gegen das [Google Cloud Java Client-Bibliotheken GitHub-Repository](https://github.com/googleapis/google-cloud-java) auf die neuesten Updates überprüft werden. Dieses Repository listet auch unterstützte Plattformen auf, einschließlich x86_64, Mac OS X, Windows und Linux, weist aber auf Einschränkungen bei Android und Raspberry Pi hin.

#### Authentifizierungsmechanismen
Authentifizierung ist ein kritischer Schritt, wobei die Optionen je nach Umgebung variieren. Auf Google Cloud-Plattformen wie Compute Engine, Kubernetes Engine oder App Engine werden Anmeldedaten automatisch abgeleitet, was den Prozess vereinfacht. Für andere Umgebungen, wie die lokale Entwicklung, sind folgende Methoden verfügbar:

- **Dienstkonto (Empfohlen):** Generieren Sie eine JSON-Schlüsseldatei aus der Google Cloud Console und setzen Sie die Umgebungsvariable `GOOGLE_APPLICATION_CREDENTIALS` auf deren Pfad. Alternativ können Sie sie programmatisch laden:
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **Lokale Entwicklung/Test:** Verwenden Sie das Google Cloud SDK mit `gcloud auth application-default login` für temporäre Anmeldedaten.
- **Bestehendes OAuth2-Token:** Verwenden Sie `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` für spezifische Anwendungsfälle.

Die Reihenfolge der Priorität für die Projekt-ID-Spezifikation umfasst Service-Optionen, die Umgebungsvariable `GOOGLE_CLOUD_PROJECT`, App Engine/Compute Engine, JSON-Anmeldedatendatei und Google Cloud SDK, wobei `ServiceOptions.getDefaultProjectId()` hilft, die Projekt-ID abzuleiten.

#### Verwenden der Client-Bibliotheken
Sobald Abhängigkeiten und Authentifizierung eingerichtet sind, können Entwickler die Bibliotheken verwenden, um mit Google Cloud-Diensten zu interagieren. Jeder Dienst hat sein eigenes Unterpaket unter `com.google.cloud`, wie z.B. `com.google.cloud.storage` für Cloud Storage oder `com.google.cloud.bigquery` für BigQuery. Hier ist ein detailliertes Beispiel für Cloud Storage:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Dieses Beispiel listet alle Buckets auf, aber die Bibliothek unterstützt Operationen wie das Hochladen von Objekten, das Herunterladen von Dateien und das Verwalten von Bucket-Richtlinien. Für andere Dienste gelten ähnliche Muster, mit detaillierten Methoden, die in den jeweiligen Javadocs verfügbar sind, wie z.B. die für BigQuery unter [Google Cloud Java reference docs](https://googleapis.dev/java/google-cloud-clients/latest/).

#### Erweiterte Funktionen und Überlegungen
Die Bibliotheken unterstützen erweiterte Funktionen wie Long-Running Operations (LROs) unter Verwendung von `OperationFuture`, mit konfigurierbaren Timeouts und Wiederholungsrichtlinien. Beispielsweise beinhalten die Standardwerte für AI Platform (v3.24.0) eine anfängliche Wiederholungsverzögerung von 5000ms, einen Multiplikator von 1.5, eine maximale Wiederholungsverzögerung von 45000ms und ein Gesamt-Timeout von 300000ms. Proxy-Konfiguration wird ebenfalls unterstützt, unter Verwendung von `https.proxyHost` und `https.proxyPort` für HTTPS/gRPC, mit benutzerdefinierten Optionen für gRPC via `ProxyDetector`.

API-Schlüssel-Authentifizierung ist für einige APIs verfügbar, manuell gesetzt via Headern für gRPC oder REST, wie in Beispielen für den Language Service gezeigt. Testen wird mit bereitgestellten Tools erleichtert, detailliert in der TESTING.md des Repositorys, und IDE-Plugins für IntelliJ und Eclipse verbessern die Entwicklung mit Bibliotheksintegration.

#### Unterstützte Plattformen und Einschränkungen
Die Bibliotheken sind mit verschiedenen Plattformen kompatibel, wobei HTTP-Clients überall und gRPC-Clients auf x86_64, Mac OS X, Windows und Linux unterstützt werden. Sie werden jedoch nicht auf Android, Raspberry Pi oder App Engine Standard Java 7 unterstützt, außer für Datastore, Storage und BigQuery. Unterstützte Umgebungen umfassen Windows x86_64, Mac OS X x86_64, Linux x86_64, GCE, GKE, GAE Std J8, GAE Flex und Alpine Linux (Java 11+).

#### Ressourcen und Weiterführende Literatur
Für zusätzliche Anleitungen bietet das [Google Cloud Java Client-Bibliotheken GitHub-Repository](https://github.com/googleapis/google-cloud-java) Code-Beispiele, Beitrittsrichtlinien und Troubleshooting-Ressourcen. Tutorials wie die auf [Baeldung](https://www.baeldung.com/java-google-cloud-storage) bieten praktische Beispiele, z.B. zur Verwendung von Cloud Storage, während die offizielle Dokumentation unter [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) breitere App-Entwicklungskonzepte abdeckt.

#### Tabelle: Wichtige Konfigurationsdetails

| **Aspekt**               | **Details**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Java-Version             | Erfordert Java 8 oder höher.                                                                    |
| Abhängigkeitsverwaltung  | Verwenden Sie BOM für Versionskonsistenz, z.B. Maven `libraries-bom`.                           |
| Authentifizierungsmethoden | Automatisch auf GCE/GKE/GAE, manuell via `GOOGLE_APPLICATION_CREDENTIALS` oder programmatisch.  |
| Unterstützte Plattformen | HTTP-Clients überall, gRPC auf x86_64, Mac OS X, Windows, Linux; nicht auf Android, Raspberry Pi.|
| Beispiel-Dienst          | Cloud Storage: `com.google.cloud.storage`, Methoden für Bucket-Auflistung, Objektverwaltung.    |

Diese umfassende Anleitung stellt sicher, dass Entwickler alle notwendigen Informationen haben, um `com.google.cloud` in Java effektiv zu verwenden, behandelt Setup, Authentifizierung, Verwendung und erweiterte Funktionen, mit Verweisen auf autoritative Quellen für weitere Erkundungen.

#### Wichtige Zitate
- [Google Cloud Java Client-Bibliotheken GitHub-Repository detaillierter Code und Setup](https://github.com/googleapis/google-cloud-java)
- [Google Cloud-Dokumentation für Java-Entwicklungsüberblick](https://cloud.google.com/products/anthos)
- [Baeldung Tutorial zu Google Cloud Storage mit Java praktische Beispiele](https://www.baeldung.com/java-google-cloud-storage)