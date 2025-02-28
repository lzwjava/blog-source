---
audio: false
lang: de
layout: post
title: Verwenden von Postman-Funktionen
translated: true
---

Postman ist eine weit verbreitete **API-Entwicklungs- und Testplattform**, die den Prozess des Bauens, Testens und Dokumentierens von APIs vereinfacht. Sie bietet eine benutzerfreundliche Oberfläche und einen robusten Satz von Tools, die verschiedene Protokolle unterstützen, einschließlich **HTTP, REST, GraphQL, WebSockets und mehr**. Egal, ob Sie allein oder im Team arbeiten, Postman bietet Funktionen wie Echtzeit-Zusammenarbeit, automatisiertes Testen und Umgebungsverwaltung, um Ihre API-Workflows zu optimieren. Diese Anleitung führt Sie durch die wichtigsten Funktionen von Postman und bietet Schritt-für-Schritt-Anweisungen, wie Sie diese effektiv nutzen können.

---

### Wichtige Funktionen von Postman

Postman bietet eine Vielzahl von Funktionen, die entwickelt wurden, um die API-Entwicklung einfacher und effizienter zu gestalten:

- **Anfrageerstellung**: Erstellen und Senden Sie HTTP-Anfragen einfach.
- **Sammlungsverwaltung**: Organisieren Sie Anfragen in Sammlungen für eine bessere Verwaltung.
- **Umgebungsvariablen**: Verwalten Sie Konfigurationen für verschiedene Umgebungen (z. B. Entwicklung, Staging, Produktion).
- **Authentifizierung**: Behandeln Sie verschiedene Authentifizierungsmethoden nahtlos.
- **Testen**: Schreiben und führen Sie Tests durch, um API-Antworten zu validieren.
- **Mocking**: Simulieren Sie API-Antworten für Testzwecke.
- **Dokumentation**: Generieren und teilen Sie API-Dokumentation automatisch.
- **Zusammenarbeit**: Teilen Sie Sammlungen und Umgebungen mit Teammitgliedern.

Im Folgenden werden wir jede dieser Funktionen im Detail erkunden.

---

### 1. **Anfrageerstellung**
Die Anfrageerstellung ist die Kernfunktionalität von Postman, die es Ihnen ermöglicht, HTTP-Anfragen einfach zu erstellen und zu senden.

- **Wie man es verwendet**:
  - Öffnen Sie Postman und klicken Sie auf **Neu** > **Anfrage**.
  - Wählen Sie die HTTP-Methode (z. B. `GET`, `POST`, `PUT`, `DELETE`) aus dem Dropdown-Menü.
  - Geben Sie die API-Endpunkt-URL in die Adressleiste ein (z. B. `https://api.example.com/users`).
  - Fügen Sie **Header** (z. B. `Content-Type: application/json`) im **Header**-Tab hinzu.
  - Für Methoden wie `POST` oder `PUT` fügen Sie den Anfragekörper im **Body**-Tab hinzu (wählen Sie das Format, z. B. `JSON`, `form-data`, usw.).
  - Klicken Sie auf **Senden**, um die Anfrage auszuführen und die Antwort im unteren Bereich anzuzeigen.

- **Tipp**: Verwenden Sie den **Params**-Tab, um Abfrageparameter (z. B. `?id=123`) zu Ihrer URL für `GET`-Anfragen hinzuzufügen.

---

### 2. **Sammlungsverwaltung**
Sammlungen helfen Ihnen, verwandte Anfragen zu organisieren, sodass es einfacher ist, mehrere Anfragen gemeinsam zu verwalten und auszuführen.

- **Wie man es verwendet**:
  - Klicken Sie auf **Neu** > **Sammlung**, um eine neue Sammlung zu erstellen.
  - Geben Sie der Sammlung einen Namen (z. B. "Benutzer-API") und eine optionale Beschreibung.
  - Fügen Sie Anfragen zur Sammlung hinzu, indem Sie sie aus der Seitenleiste ziehen oder auf **Anfrage hinzufügen** innerhalb der Sammlung klicken.
  - Um die gesamte Sammlung auszuführen, klicken Sie auf die **...** neben dem Sammlungsnamen und wählen Sie **Sammlung ausführen**. Dies öffnet den **Sammlungsausführer**, in dem Sie alle Anfragen nacheinander oder parallel ausführen können.

- **Tipp**: Verwenden Sie Ordner innerhalb von Sammlungen, um Anfragen weiter nach Funktionalität zu organisieren (z. B. "Authentifizierung", "Benutzerverwaltung").

---

### 3. **Umgebungsvariablen**
Umgebungsvariablen ermöglichen es Ihnen, verschiedene Konfigurationen (z. B. Basis-URLs, API-Schlüssel) für verschiedene Umgebungen zu verwalten, ohne jede Anfrage manuell zu ändern.

- **Wie man es verwendet**:
  - Klicken Sie auf das **Auge**-Symbol in der oberen rechten Ecke, um den **Umgebungsmanager** zu öffnen.
  - Klicken Sie auf **Hinzufügen**, um eine neue Umgebung (z. B. "Entwicklung", "Produktion") zu erstellen.
  - Definieren Sie Schlüssel-Wert-Paare (z. B. `base_url: https://api.example.com`) für jede Umgebung.
  - In Ihren Anfragen verwenden Sie Variablen, indem Sie sie in doppelte geschweifte Klammern setzen, wie `{{base_url}}/users`.
  - Wechseln Sie zwischen Umgebungen, indem Sie die gewünschte aus dem Dropdown-Menü in der oberen rechten Ecke auswählen.

- **Tipp**: Verwenden Sie **Globale Variablen** für Werte, die über Umgebungen hinweg konstant bleiben, wie API-Schlüssel.

---

### 4. **Authentifizierung**
Postman vereinfacht die Handhabung verschiedener Authentifizierungsmethoden und stellt sicher, dass Sie sicher auf Ihre APIs zugreifen können.

- **Wie man es verwendet**:
  - Gehen Sie im Anfrage-Tab zum **Authentifizierung**-Tab.
  - Wählen Sie den Authentifizierungstyp aus dem Dropdown-Menü (z. B. **Basic Auth**, **Bearer Token**, **OAuth 2.0**, **API Key**).
  - Füllen Sie die erforderlichen Anmeldeinformationen oder Tokens aus (z. B. Benutzername und Passwort für Basic Auth oder ein Token für Bearer Token).
  - Postman wird die Authentifizierungsdetails automatisch zu den Anfrage-Headern hinzufügen.

- **Beispiel**:
  - Für **Bearer Token** fügen Sie Ihr Token ein, und Postman wird es im `Authorization`-Header als `Bearer <token>` einfügen.

---

### 5. **Testen**
Der Test-Framework von Postman ermöglicht es Ihnen, JavaScript-Tests zu schreiben, um API-Antworten zu validieren und sicherzustellen, dass Ihre APIs wie erwartet funktionieren.

- **Wie man es verwendet**:
  - Gehen Sie im Anfrage-Tab zum **Tests**-Tab.
  - Schreiben Sie JavaScript-Code, um die Antwort zu validieren. Zum Beispiel:
    ```javascript
    pm.test("Statuscode ist 200", function () {
        pm.response.to.have.status(200);
    });
    ```
  - Nach dem Senden der Anfrage überprüfen Sie die **Testergebnisse** im Antwortbereich, um zu sehen, ob die Tests bestanden wurden oder fehlgeschlagen sind.

- **Tipp**: Verwenden Sie die integrierten Snippets von Postman (z. B. "Statuscode ist 200", "Antwortkörper: JSON-Wertprüfung"), um häufige Tests schnell hinzuzufügen.

---

### 6. **Mocking**
Mocking ermöglicht es Ihnen, API-Antworten zu simulieren, was nützlich ist, wenn die tatsächliche API noch in der Entwicklung ist oder nicht verfügbar ist.

- **Wie man es verwendet**:
  - Erstellen Sie eine neue Sammlung oder verwenden Sie eine bestehende.
  - Klicken Sie auf die **...** neben der Sammlung und wählen Sie **Sammlung mocken**.
  - Definieren Sie simulierte Antworten für jede Anfrage in der Sammlung (z. B. Beispiel-JSON-Daten).
  - Postman wird eine Mock-Server-URL (z. B. `https://<mock-id>.mock.pstmn.io`) generieren, die Sie verwenden können, um Anfragen zu senden und simulierte Antworten zu erhalten.

- **Tipp**: Verwenden Sie Mocking, um Frontend-Entwicklern zu ermöglichen, unabhängig zu arbeiten, ohne auf das Backend warten zu müssen.

---

### 7. **Dokumentation**
Postman kann automatisch Dokumentation für Ihre APIs basierend auf den Anfragen in Ihren Sammlungen generieren.

- **Wie man es verwendet**:
  - Öffnen Sie eine Sammlung und klicken Sie auf das **...**-Symbol.
  - Wählen Sie **Dokumentation anzeigen**, um eine Dokumentationsseite zu generieren.
  - Passen Sie die Dokumentation an, indem Sie Beschreibungen, Beispiele und Tags für jede Anfrage hinzufügen.
  - Teilen Sie die Dokumentation, indem Sie sie öffentlich veröffentlichen oder den Link mit Ihrem Team teilen.

- **Tipp**: Halten Sie Ihre Dokumentation aktuell, indem Sie sie mit den Änderungen in Ihrer Sammlung synchronisieren.

---

### 8. **Zusammenarbeit**
Die Zusammenarbeitsfunktionen von Postman ermöglichen es Teams, effizient an API-Projekten zu arbeiten.

- **Wie man es verwendet**:
  - Erstellen Sie einen **Team-Arbeitsbereich**, indem Sie auf **Arbeitsbereiche** > **Arbeitsbereich erstellen** klicken.
  - Laden Sie Teammitglieder per E-Mail oder Link in den Arbeitsbereich ein.
  - Teilen Sie Sammlungen, Umgebungen und andere Ressourcen im Arbeitsbereich.
  - Verwenden Sie **Versionskontrolle**, um Sammlungen zu verzweigen, Änderungen vorzunehmen und Updates über Pull-Anfragen zu integrieren.

- **Tipp**: Verwenden Sie **Kommentare** zu Anfragen oder Sammlungen, um Änderungen zu besprechen und Feedback direkt in Postman zu geben.

---

### Zusätzliche Tipps zur effektiven Nutzung von Postman

- **Verwenden Sie Skripte**: Nutzen Sie **Pre-request-Skripte**, um Daten oder Bedingungen (z. B. Generieren eines Zeitstempels) vor dem Senden einer Anfrage einzurichten.
- **Überwachen Sie APIs**: Richten Sie **Monitore** ein, um Sammlungen in geplanten Intervallen auszuführen und die API-Gesundheit oder -Verfügbarkeit zu überprüfen.
- **Integrieren Sie mit CI/CD**: Verwenden Sie **Newman**, das Postman-Befehlszeilen-Tool, um Sammlungen in Ihren CI/CD-Pipelines (z. B. Jenkins, GitHub Actions) auszuführen.
- **Erkunden Sie Postman Flows**: Verwenden Sie **Flows**, um komplexe API-Workflows visuell zu erstellen und zu automatisieren, ohne Code zu schreiben.
- **Sichern Sie sensible Daten**: Speichern Sie sensible Informationen wie API-Schlüssel im **Postman Vault** für sicheren Zugriff.

---

### Fazit

Postman ist eine leistungsstarke Plattform, die über einfaches API-Testen hinausgeht und ein umfassendes Werkzeugset für API-Entwicklung, Zusammenarbeit und Automatisierung bietet. Durch das Beherrschen von Funktionen wie Anfrageerstellung, Umgebungsverwaltung, Testen und Mocking können Sie Ihre Produktivität erheblich steigern und Ihre API-Workflows optimieren. Egal, ob Sie ein einzelner Entwickler sind oder Teil eines großen Teams, die intuitive Oberfläche und die fortschrittlichen Fähigkeiten von Postman machen es zu einem unverzichtbaren Werkzeug für die moderne API-Entwicklung. Beginnen Sie noch heute, diese Funktionen zu erkunden, um das volle Potenzial Ihrer API-Projekte zu entfalten!