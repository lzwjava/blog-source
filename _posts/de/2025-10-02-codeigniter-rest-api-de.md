---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter REST API Konfigurationsleitfaden
translated: true
type: note
---

Hier folgt eine klare, schrittweise Anleitung zum Verständnis und zur Verwendung der von Ihnen geteilten CodeIgniter REST API-Konfigurationsdatei (`application/config/rest.php`). Diese Datei konfiguriert das Verhalten der REST_Controller-Bibliothek (eine beliebte PHP-Bibliothek zum Erstellen von RESTful APIs in CodeIgniter), wie z.B. Phil Sturgeons REST-Bibliothek (die in einigen Versionen nun als Teil des CodeIgniter-Frameworks weiterentwickelt wird).

Ich werde erklären:
- Was die Bibliothek macht und wichtige Voraussetzungen.
- Wie man sie einrichtet und verwendet.
- Wichtige Konfigurationsoptionen aus Ihrer Datei (mit Beispielen).
- Ein einfaches Anwendungsbeispiel.
- Tipps für häufige Fehlerquellen und Sicherheit.

Wenn Ihre Frage einen spezifischen Aspekt betrifft (z.B. Authentifizierung oder Limits), teilen Sie dies bitte mit, um gezieltere Hilfe zu erhalten!

### 1. **Voraussetzungen und Einrichtung**
   - **Was ist das?** Dies ist die REST_Controller-Bibliothek für CodeIgniter (ein PHP-Framework). Sie ermöglicht es Ihnen, RESTful APIs zu erstellen (z.B. Endpunkte, die auf GET/POST-Anfragen mit JSON/XML antworten), indem Sie Ihre Controller von `REST_Controller` ableiten. Ihre Konfigurationsdatei steuert globale Einstellungen wie Authentifizierung, Antwortformate, Rate Limiting und Sicherheit.
   
   - **Anforderungen:**
     - CodeIgniter 3.x (oder eine kompatible Version; diese Konfiguration ist für ältere Versionen um 3.x).
     - Installieren Sie die REST_Controller-Bibliothek, falls sie noch nicht in Ihrer CodeIgniter-Installation enthalten ist (Sie können sie von GitHub herunterladen: `chriskacerguis/codeigniter-restserver`). Platzieren Sie die Bibliotheksdateien in `application/libraries/` und laden Sie sie in `application/config/autoload.php` automatisch:
       ```php
       $autoload['libraries'] = ['rest_controller'];
       ```
     - Datenbankeinrichtung (optional; benötigt für Funktionen wie API-Schlüssel, Protokollierung oder Limits). Führen Sie die in den Konfigurationskommentaren bereitgestellten SQL-Schemata aus (z.B. für Tabellen wie `keys`, `logs`, `access`, `limits`).
     - Aktivieren Sie Pretty URLs in CodeIgniter (`application/config/routes.php`) für saubere API-Endpunkte wie `/api/users`.
     - Ihre `rest.php` Konfigurationsdatei sollte in `application/config/` platziert und in `application/config/autoload.php` automatisch geladen werden:
       ```php
       $autoload['config'] = ['rest'];
       ```

   - **Grundlegende Installationsschritte:**
     1. CodeIgniter herunterladen und entpacken.
     2. REST_Controller-Bibliotheksdateien hinzufügen.
     3. Kopieren Sie Ihre bereitgestellte `rest.php` nach `application/config/`.
     4. Richten Sie Routen in `routes.php` ein (z.B. `$route['api/(:any)'] = 'api/$1';` um `/api/users` einem Controller zuzuordnen).
     5. Erstellen Sie API-Controller (siehe Beispiel unten).
     6. Testen Sie mit einem Tool wie Postman oder curl.

### 2. **Wichtige Konfigurationsoptionen**
Ich fasse die Haupteinstellungen aus Ihrer Konfigurationsdatei zusammen, gruppiert nach Zweck. Diese steuern das globale Verhalten. Sie können sie an Ihre Bedürfnisse anpassen (z.B. HTTPS aktivieren oder Standardformate ändern).

- **Protokoll und Ausgabe:**
  - `$config['force_https'] = FALSE;`: Erzwingt, dass alle API-Aufrufe HTTPS verwenden. Für Produktionssicherheit auf `TRUE` setzen.
  - `$config['rest_default_format'] = 'json';`: Standardantwortformat (Optionen: json, xml, csv, etc.). Anfragen können dies per URL überschreiben (z.B. `/api/users.format=xml`).
  - `$config['rest_supported_formats']`: Liste der erlaubten Formate. Entfernen Sie unerwünschte aus Sicherheitsgründen.
  - `$config['rest_ignore_http_accept'] = FALSE;`: Ignoriert Client-HTTP-Accept-Header, um Antworten zu beschleunigen (nützlich, wenn Sie immer `$this->rest_format` im Code verwenden).

- **Authentifizierung (Sicherheit):**
  - `$config['rest_auth'] = FALSE;`: Haupt-Authentifizierungsmodus. Optionen:
    - `FALSE`: Keine Authentifizierung erforderlich.
    - `'basic'`: HTTP Basic Auth (Benutzername/Passwort in base64-Headern).
    - `'digest'`: Sicherere Digest-Authentifizierung.
    - `'session'`: Prüft auf eine PHP-Session-Variable.
  - `$config['auth_source'] = 'ldap';`: Wo Anmeldedaten geprüft werden sollen (z.B. Konfigurations-Array, LDAP, benutzerdefinierte Bibliothek).
  - `$config['rest_valid_logins'] = ['admin' => '1234'];`: Einfaches Benutzername/Passwort-Array (wird ignoriert, wenn LDAP verwendet wird).
  - `$config['auth_override_class_method']`: Überschreibt die Authentifizierung für bestimmte Controller/Methoden (z.B. `'users' => 'view' => 'basic'`).
  - `$config['auth_library_class/function']`: Wenn eine benutzerdefinierte Bibliothek verwendet wird, geben Sie die Klasse/Methode zur Validierung an.
  - IP-Kontrollen:
    - `$config['rest_ip_whitelist_enabled/blacklist_enabled']`: Basis-IP-Filterung für Ihre API.
    - Nützlich, um den Zugriff einzuschränken (z.B. Whitelist der IPs Ihrer App).

- **API-Schlüssel (Optionale Sicherheitsebene):**
  - `$config['rest_enable_keys'] = FALSE;`: Aktiviert die API-Schlüsselprüfung (gespeichert in der DB-Tabelle `keys`). Clients müssen Schlüssel in Headern senden (z.B. `X-API-KEY`).
  - `$config['rest_key_column/name/length']`: Passt Schlüsselfelder und Headernamen an.
  - Kombinieren Sie dies mit `$config['rest_enable_access']`, um Schlüssel auf bestimmte Controller/Methoden zu beschränken.

- **Protokollierung und Limits:**
  - `$config['rest_enable_logging/limits'] = FALSE;`: Aktiviert die DB-basierte Protokollierung von Anfragen (URI, Parameter, etc.) oder Rate Limiting (z.B. X Aufrufe pro Stunde pro Schlüssel).
  - Tabellen: `logs`, `limits` (führen Sie das SQL in den Kommentaren aus, um sie zu erstellen).
  - `$config['rest_limits_method']`: Wie Limits angewendet werden (nach API-Schlüssel, URL, etc.).
  - Passen Sie es pro Methode in Controllern an (z.B. `$this->method['get']['limit'] = 100;`).

- **Andere:**
  - `$config['rest_ajax_only'] = FALSE;`: Beschränkt auf AJAX-Anfragen (gibt sonst 505-Fehler zurück).
  - `$config['rest_language'] = 'english';`: Sprache für Fehlermeldungen.

Um zu ändern: Bearbeiten Sie `rest.php` und starten Sie Ihre App neu. Testen Sie Änderungen sorgfältig!

### 3. **Wie man es verwendet: Schritt-für-Schritt-Anwendung**
Sobald eingerichtet, erstellen Sie API-Endpunkte, indem Sie Controller erstellen, die von `REST_Controller` erben. Hier ist der grobe Prozess:

1. **Einen Controller erstellen:**
   - In `application/controllers/` erstellen Sie `Api.php` (oder z.B. `Users.php` für eine spezifische Ressource):
     ```php
     <?php
     defined('BASEPATH') OR exit('No direct script access allowed');
     require_once(APPPATH . 'libraries/REST_Controller.php');

     class Api extends REST_Controller {
         public function __construct() {
             parent::__construct();
             // Optional: Setzen Sie Auth, Limits pro Methode
             $this->load->database();
             $this->method['index_get']['limit'] = 100; // 100 Anfragen/Stunde
         }

         // GET /api
         public function index_get() {
             $data = ['message' => 'Willkommen bei der API', 'status' => 'success'];
             $this->response($data, REST_Controller::HTTP_OK);
         }

         // POST /api/users
         public function users_post() {
             $data = $this->input->post(); // Holt POST-Daten
             if (empty($data['name'])) {
                 $this->response(['error' => 'Name erforderlich'], REST_Controller::HTTP_BAD_REQUEST);
             }
             // Verarbeitung (z.B. Einfügen in die DB)
             $this->response(['message' => 'Benutzer erstellt'], REST_Controller::HTTP_CREATED);
         }

         // PUT /api/users/{id}
         public function users_put($id) {
             $data = $this->put(); // Holt PUT-Daten
             // Aktualisiere Benutzer mit $id
             $this->response(['message' => 'Benutzer aktualisiert'], REST_Controller::HTTP_OK);
         }

         // etc. für DELETE
     }
     ```

2. **Anfragen senden:**
   - Verwenden Sie einen beliebigen HTTP-Client:
     - GET: `curl http://ihredomain.com/api` → Gibt JSON zurück {"message": "Willkommen bei der API", "status": "success"}
     - POST: `curl -X POST http://ihredomain.com/api/users -d "name=John"` → Erstellt einen Benutzer.
   - Fügen Sie Header hinzu, wenn Auth/Schlüssel verwendet werden (z.B. `Authorization: Basic base64(user:pass)` oder `X-API-KEY: yourkey`).

3. **Testen und Debuggen:**
   - Überprüfen Sie CodeIgniter-Logs auf Fehler.
   - Wenn die Authentifizierung fehlschlägt, stellen Sie sicher, dass die Anmeldedaten korrekt gesetzt sind.
   - Für Limits/Protokollierung, fragen Sie Ihre DB-Tabellen ab.

### 4. **Häufige Tipps und Best Practices**
- **Sicherheit:** Verwenden Sie in der Produktion immer HTTPS (`force_https = TRUE`). Aktivieren Sie Schlüssel, wenn Sie sie externen Clients zugänglich machen. Bereinigen Sie Eingaben, um SQL-Injection zu verhindern.
- **Fehler:** Antworten enthalten `status` und `error` Felder (in der Konfiguration anpassbar). Verwenden Sie CodeIgniters Profiler zum Debuggen.
- **Leistung:** Wenn Protokollierung/Limits aktiviert sind, bearbeitet Ihre DB die Abfragen – überwachen Sie auf langsame Performance.
- **Upgrades:** Diese Konfiguration ist für ältere CodeIgniter-Versionen. Für CI 4 verwenden Sie die eingebauten API-Ressourcen (dieses Setup benötigt möglicherweise Anpassungen).
- **Fehlerbehebung:**
  - "Keine Antwort"? Überprüfen Sie Routen, Autoload und Bibliothekspfade.
  - Authentifizierungsprobleme? Überprüfen Sie `$auth_source` und Anmeldedaten.
  - Formatfehler? Stellen Sie sicher, dass Ihr Format in `rest_supported_formats` enthalten ist.
- **Ressourcen:** Dokumentation unter codeigniter-restserver.org. Für CI4-Migration, siehe offizielle Dokumentation.

Wenn dies Ihre genaue Frage nicht beantwortet oder Sie Code für einen spezifischen Anwendungsfall benötigen (z.B. Aktivieren von OAuth), geben Sie bitte mehr Details an!