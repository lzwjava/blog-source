---
audio: false
lang: de
layout: post
title: HTTP-Datei-Uploads
translated: true
---

### Wichtige Punkte
- Die Forschung deutet darauf hin, dass HTTP-Datei-Uploads typischerweise die POST-Methode mit multipart/form-data für Web-Formulare verwenden, was das Hochladen mehrerer Dateien und zusätzlicher Daten ermöglicht.
- Es scheint wahrscheinlich, dass die PUT-Methode ebenfalls Dateien hochladen kann, indem sie den Rohinhalt direkt sendet, was oft in RESTful-APIs aus Gründen der Einfachheit verwendet wird.
- Die Beweise sprechen dafür, dass beide Methoden gültig sind, wobei die Serverkonfiguration und der Anwendungsfall die Wahl bestimmen.

### Übersicht
Das Hochladen von Dateien über HTTP ist eine häufige Aufgabe zum Teilen von Daten im Internet, wie z.B. das Senden von Fotos oder Dokumenten an eine Website. Dies kann auf zwei Hauptweisen erfolgen: durch die Verwendung der POST-Methode mit einem speziellen Format namens multipart/form-data, das sich gut für Web-Formulare eignet, oder durch die Verwendung der PUT-Methode, die einfacher ist und oft in modernen APIs verwendet wird. Jede Methode hat ihre eigene Einrichtung, und die richtige Wahl hängt davon ab, wie der Server eingerichtet ist und was Sie tun möchten.

### Wie es funktioniert
- **POST mit Multipart/Form-Data**: Dies ist wie das Verpacken Ihrer Datei und jeglicher zusätzlicher Informationen (wie eine Beschreibung) in separate Teile, die durch eine eindeutige Begrenzungszeichenfolge gekennzeichnet sind. Es ist üblich für Web-Formulare, bei denen Dateien zum Hochladen ausgewählt werden.
- **PUT-Methode**: Diese sendet den Dateiinhalt direkt an eine bestimmte URL, wie z.B. das Aktualisieren einer Datei auf dem Server. Es ist einfacher, erfordert aber, dass der Server dies unterstützt.

### Unerwartetes Detail
Man könnte nicht erwarten, dass die PUT-Methode, die normalerweise zum Aktualisieren von Daten verwendet wird, auch Datei-Uploads handhaben kann, insbesondere in APIs, was sie zu einer vielseitigen Option jenseits traditioneller Formulare macht.

---

### Umfragehinweis: Detaillierte Erklärung von HTTP-Datei-Uploads

Das Hochladen von Dateien über HTTP ist eine grundlegende Operation in der Webentwicklung, die es Benutzern ermöglicht, Daten wie Bilder, Dokumente oder Medien mit Servern zu teilen. Dieser Vorgang kann durch zwei Hauptmethoden durchgeführt werden: die POST-Methode mit multipart/form-data-Codierung, die häufig für Web-Formulare verwendet wird, und die PUT-Methode, die oft in RESTful-APIs für die direkte Übertragung von Dateiinhalten verwendet wird. Im Folgenden werden diese Methoden eingehend untersucht, einschließlich ihrer Struktur, Implementierung und Überlegungen, um ein umfassendes Verständnis sowohl für technische als auch für nicht-technische Zielgruppen zu bieten.

#### Multipart/Form-Data: Der Standard für Web-Formulare

Der multipart/form-data-Inhaltstyp ist die Standardwahl für HTTP-Datei-Uploads, insbesondere bei der Arbeit mit HTML-Formularen. Diese Methode ermöglicht die gleichzeitige Übertragung mehrerer Dateien und zusätzlicher Formulardaten, wie z.B. Textfelder, innerhalb einer einzigen Anfrage. Der Prozess umfasst das Erstellen eines Anfragekörpers, der in Teile unterteilt ist, die jeweils durch eine eindeutige Begrenzungszeichenfolge getrennt sind, die sicherstellt, dass der Server zwischen den verschiedenen Datenteilen unterscheiden kann.

##### Struktur und Beispiel
Die Anfrage beginnt mit dem Festlegen des `Content-Type`-Headers auf `multipart/form-data; boundary=boundary_string`, wobei `boundary_string` eine zufällig gewählte Zeichenfolge ist, um Konflikte mit dem Dateiinhalt zu vermeiden. Jeder Teil des Körpers enthält Header wie `Content-Disposition`, der das Formularfeldnamen und, für Dateien, den Dateinamen angibt, und `Content-Type`, der den Datentyp angibt (z.B. `text/plain` für Textdateien, `image/jpeg` für JPEG-Bilder). Der Teil endet mit der Begrenzungszeichenfolge, und der letzte Teil wird durch die Begrenzung gefolgt von zwei Bindestrichen markiert.

Betrachten Sie das Hochladen einer Datei namens `example.txt` mit dem Inhalt "Hello, world!" an [dieses Endpunkt](https://example.com/upload), mit dem Formularfeldnamen "file". Die HTTP-Anfrage würde wie folgt aussehen:

```
POST /upload HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=abc123
Content-Length: 101

--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

Hier beträgt die `Content-Length` 101 Bytes, einschließlich der Begrenzung, Header und Dateiinhalt, wobei Zeilenenden typischerweise CRLF (`\r\n`) für eine korrekte HTTP-Formatierung verwenden.

##### Mehrere Dateien und Formularfelder verarbeiten
Diese Methode eignet sich hervorragend für Szenarien, die zusätzliche Metadaten erfordern. Zum Beispiel, wenn eine Datei mit einer Beschreibung hochgeladen wird, kann der Anfragekörper mehrere Teile enthalten:

```
--abc123
Content-Disposition: form-data; name="description"

Dies ist meine Datei
--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

Der Inhalt jedes Teils wird einschließlich aller Zeilenumbrüche beibehalten, und die Begrenzung stellt die Trennung sicher. Diese Flexibilität macht sie ideal für Web-Formulare mit `<input type="file">`-Elementen.

#### PUT-Methode: Direkter Datei-Upload für RESTful-APIs

Die PUT-Methode bietet eine einfachere Alternative, insbesondere in RESTful-API-Kontexten, bei denen das Ziel darin besteht, eine Ressource mit dem Dateiinhalt zu aktualisieren oder zu erstellen. Im Gegensatz zu multipart/form-data sendet PUT den Rohdateiinhalt direkt im Anfragekörper, wodurch der Overhead reduziert und die serverseitige Verarbeitung vereinfacht wird.

##### Struktur und Beispiel
Zum Hochladen von `example.txt` an [diese URL](https://example.com/files/123) würde die Anfrage wie folgt aussehen:

```
PUT /files/123 HTTP/1.1
Host: example.com
Content-Type: text/plain
Content-Length: 13

Hello, world!
```

Hier gibt der `Content-Type` den MIME-Typ der Datei an (z.B. `text/plain`), und `Content-Length` ist die Dateigröße in Bytes. Diese Methode ist effizient für große Dateien, da sie den Codierungsaufwand von multipart/form-data vermeidet, erfordert aber, dass der Server so konfiguriert ist, dass er PUT-Anfragen für Datei-Uploads verarbeitet.

##### Anwendungsfälle und Überlegungen
PUT wird oft in Szenarien wie dem Aktualisieren von Benutzeravataren oder dem Hochladen von Dateien an eine bestimmte Ressource in einer API verwendet. Allerdings unterstützen nicht alle Server PUT für Datei-Uploads standardmäßig, insbesondere in Shared-Hosting-Umgebungen, in denen POST mit multipart/form-data universeller akzeptiert wird. Die Serverkonfiguration, wie z.B. das Aktivieren des PUT-Verbs in Apache, kann erforderlich sein, wie in der [PHP-Dokumentation zur PUT-Methodenunterstützung](https://www.php.net/manual/en/features.file-upload.put-method.php) angegeben.

#### Vergleichende Analyse

Um die Unterschiede zu verdeutlichen, betrachten Sie die folgende Tabelle, die die beiden Methoden vergleicht:

| Aspekt                  | POST mit Multipart/Form-Data          | PUT mit Rohinhalt                  |
|-------------------------|----------------------------------------|---------------------------------------|
| **Anwendungsfall**      | Web-Formulare, mehrere Dateien, Metadaten | RESTful-APIs, einzelne Datei-Updates     |
| **Komplexität**          | Höher (Begrenzungshandhabung, mehrere Teile) | Niedriger (direkter Inhalt)               |
| **Effizienz**          | Mäßig (Codierungsaufwand)           | Höher (keine Codierung)                 |
| **Serverunterstützung**  | Weit verbreitet                      | Kann Konfiguration erfordern            |
| **Beispiel-Header**     | `Content-Type: multipart/form-data; boundary=abc123` | `Content-Type: text/plain`           |
| **Anfragekörper**        | Teile durch Begrenzungen getrennt          | Rohdateiinhalt                     |

Diese Tabelle zeigt, dass multipart/form-data für Web-Interaktionen vielseitiger ist, PUT jedoch für API-gesteuerte Uploads effizienter ist, abhängig von den Serverfähigkeiten.

#### Implementierungsdetails und Stolpersteine

##### Begrenzungsauswahl und Dateiinhalt
Bei multipart/form-data ist die Auswahl einer Begrenzungszeichenfolge entscheidend, um Konflikte mit dem Dateiinhalt zu vermeiden. Wenn die Begrenzung im Inneren der Datei erscheint, kann dies zu Parsing-Fehlern führen. Moderne Bibliotheken handhaben dies, indem sie zufällige Begrenzungen generieren, aber eine manuelle Implementierung erfordert Sorgfalt. Bei Binärdateien wird der Inhalt so wie er ist übertragen, was alle Bytes beibehält, was für die Aufrechterhaltung der Dateiintegrität entscheidend ist.

##### Dateigröße und Leistung
Beide Methoden müssen die Dateigrößenbeschränkungen berücksichtigen, die von Servern auferlegt werden. Multipart/form-data-Anfragen können mit mehreren Dateien groß werden, was möglicherweise Serverbeschränkungen überschreitet oder Speicherprobleme verursacht. PUT, obwohl einfacher, erfordert für große Dateien das Streaming, um das Laden des gesamten Inhalts in den Speicher zu vermeiden, wie in der [HTTPie-Dokumentation zu Datei-Uploads](https://httpie.io/docs/cli/file-upload-forms) besprochen.

##### Fehlerbehandlung und Sicherheit
Nach dem Senden der Anfrage sollten Clients den HTTP-Statuscode überprüfen. Erfolg wird typischerweise durch 200 (OK) oder 201 (Erstellt) angezeigt, während Fehler wie 400 (Ungültige Anfrage) oder 403 (Verweigert) auf Probleme hinweisen. Sicherheit ist entscheidend, da Datei-Uploads für Angriffe wie das Hochladen schädlicher ausführbarer Dateien ausgenutzt werden können. Server sollten Dateitypen validieren, auf Schadsoftware scannen und Upload-Verzeichnisse einschränken, wie in den [Stack Overflow-Diskussionen zur HTTP-Datei-Upload-Sicherheit](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work) dargelegt.

#### Praktische Beispiele in verschiedenen Sprachen

Verschiedene Programmiersprachen bieten Bibliotheken, um HTTP-Datei-Uploads zu vereinfachen. Zum Beispiel handelt die `requests`-Bibliothek von Python multipart/form-data wie folgt:

```python
import requests
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://example.com/upload', files=files)
```

Für PUT kann curl verwendet werden, wie in [Stack Overflow zum Testen von PUT-Uploads](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method) gezeigt:

```bash
curl -X PUT "https://example.com/files/123" --upload-file example.txt
```

Diese Beispiele demonstrieren Abstraktion, aber das Verständnis der zugrunde liegenden HTTP-Struktur ist entscheidend für die Fehlerbehebung und benutzerdefinierte Implementierungen.

#### Fazit

Zusammenfassend lässt sich sagen, dass HTTP-Datei-Uploads durch POST mit multipart/form-data für vielseitige Web-Formularinteraktionen oder PUT für effiziente API-Updates durchgeführt werden können, wobei jede Methode eigene Vorteile und Anforderungen hat. Serverkonfiguration, Dateigröße und Sicherheitsüberlegungen sind entscheidend, um eine robuste Implementierung zu gewährleisten. Für weiterführende Lektüre erkunden Sie die [Medium-Anleitung zu POST-Datei-Uploads](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73) für praktische Beispiele in verschiedenen Sprachen.

### Wichtige Zitate
- [How do you upload your files to a web server Learn web development MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/Upload_files_to_a_web_server)
- [How does HTTP file upload work Stack Overflow](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work)
- [POST a File via HTTP Request The Ultimate Guide by API4AI Medium](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73)
- [HTTP REST API File Uploads Phil Sturgeon](https://philsturgeon.com/http-rest-api-file-uploads/)
- [PHP PUT method support Manual](https://www.php.net/manual/en/features.file-upload.put-method.php)
- [curl Test file upload using HTTP PUT method Stack Overflow](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method)
- [File upload forms HTTPie 3.2.4 latest docs](https://httpie.io/docs/cli/file-upload-forms)