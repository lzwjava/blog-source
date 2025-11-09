---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter Routing Leitfaden
translated: true
type: note
---

### Übersicht über CodeIgniter Routing

CodeIgniters Routing-System ermöglicht es Ihnen, URLs (URIs) bestimmten Controller-Klassen und Methoden zuzuordnen und überschreibt dabei das Standard-URL-Muster `example.com/controller/method/id/`. Dies ist nützlich, um SEO-freundliche URLs zu erstellen, RESTful APIs zu behandeln oder einfach die Verarbeitung von Anfragen anzupassen.

Der bereitgestellte Code-Ausschnitt stammt aus der `routes.php` Konfigurationsdatei von CodeIgniter. Er definiert ein assoziatives Array `$route`, in dem jeder Schlüssel einem URI-Muster entspricht und der Wert entweder ein String (`controller/method`) oder ein Array ist, das unterschiedliche Verhaltensweisen nach HTTP-Methode (z.B. GET, POST) spezifiziert. Dieser Aufbau unterstützt sowohl Standard-Routing als auch methodenspezifisches Routing.

Ich werde aufschlüsseln, **wie Routen definiert werden**, **wie sie funktionieren** und **wie man sie verwendet**, basierend auf dem Standardverhalten von CodeIgniter und dem Beispiel in Ihrem Code. Für vollständige Details lesen Sie bitte den offiziellen CodeIgniter User Guide zum Thema Routing: https://codeigniter.com/userguide4/general/routing.html.

#### 1. **Wie man Routen definiert**
Routen werden in `application/config/routes.php` als Array definiert. Sie fügen Einträge zu `$route[]` hinzu. Hier ist die Syntax:

- **Grundlegende Route**: Ordnet jede HTTP-Methode einem Controller/Methoden-Paar zu.
  ```
  $route['uri_segment'] = 'controller/method';
  ```
  - Beispiel: `$route['login'] = 'users/login';` bedeutet, dass jede Anfrage an `/login` zu `Users::login()` geroutet wird.

- **Methodenspezifische Route**: Für RESTful APIs können Sie unterschiedliche Controller/Methoden pro HTTP-Methode (GET, POST, PUT, etc.) angeben. Dies verwendet ein Array.
  ```
  $route['uri_segment'] = array(
      'METHOD1' => 'controller/method1',
      'METHOD2' => 'controller/method2'
  );
  ```
  - Beispiel aus Ihrem Code: `$route['self'] = array('POST' => 'users/update', 'GET' => 'users/self');` bedeutet:
    - POST an `/self` → `Users::update()`.
    - GET an `/self` → `Users::self()`.

- **Wildcard-Platzhalter**: Verwenden Sie regex-ähnliche Muster, um dynamische Teile der URL zu erfassen (die als Parameter an die Methode übergeben werden).
  - `(:any)`: Matcht beliebige Zeichen (außer Schrägstrichen) – z.B. für Slugs oder Strings.
  - `(:num)` oder `(\d+)`: Matcht nur Ziffern – für IDs.
  - Benutzerdefinierte Regex: In Klammern einschließen, z.B. `(foo|bar)` für spezifische Matches.
  - Beispiele aus Ihrem Code:
    - `$route['users/(\d+)']['GET'] = 'users/one/$1';`: GET `/users/123` routet zu `Users::one(123)`.
    - `$route['lives/(\d+)/notify'] = 'lives/notifyLiveStart/$1';`: Jede Methode an `/lives/123/notify` routet zu `Lives::notifyLiveStart(123)`.

- **Reservierte Routen**:
  - `$route['default_controller'] = 'welcome';`: Der Controller, der geladen wird, wenn keine URI angegeben ist (z.B. Root-URL → `Welcome` Controller).
  - `$route['404_override'] = 'errors/page_missing';`: Der Controller/Methoden-Paar für nicht gematchte Routen (benutzerdefinierte 404).
  - `$route['translate_uri_dashes'] = FALSE;`: Wenn TRUE, werden Bindestriche in URIs zu Unterstrichen für Controller/Methoden-Namen konvertiert (z.B. `my-controller` → `my_controller`).

- **Reihenfolge ist wichtig**: Routen werden in der Reihenfolge ihres Erscheinens gematcht. Definieren Sie spezifische Routen (mit Wildcards) vor allgemeinen, um Konflikte zu vermeiden.
- **HTTP-Methoden**: Wenn nicht angegeben, gilt eine Route für alle Methoden. Ihr Code verwendet Arrays für Spezifität, was großartig für APIs ist.

**Tipps zum Definieren von Routen in Ihrem Code**:
- Fügen Sie neue Routen am Ende hinzu, vor `$route['translate_uri_dashes']`.
- Testen Sie mit Tools wie Postman für API-Routen, um sicherzustellen, dass der korrekte Controller/die korrekte Methode aufgerufen wird.
- Für komplexe Apps, gruppieren Sie Routen nach Abschnitten (wie Sie es mit Kommentaren wie `// users` getan haben).

#### 2. **Wie Routen funktionieren**
CodeIgniters Router verarbeitet jede eingehende Anfrage in dieser Reihenfolge:
1. **Parse der URI**: Zerlegt die URL in Segmente (z.B. `/users/123/edit` → Segmente: `users`, `123`, `edit`).
2. **Match gegen Routen**: Prüft das `$route` Array von oben nach unten. Es sucht zuerst nach exakten Matches, dann nach Mustern mit Wildcards.
   - Wenn ein Match gefunden wird, wird es dem spezifizierten Controller/Methoden-Paar zugeordnet und übergibt dynamische Teile (z.B. `123`) als Methodenargumente.
   - Wenn kein Match gefunden wird, fällt es auf das Standardmuster zurück (`Controller::method/id/`).
3. **Lade Controller & Methode**: CodeIgniter instanziiert den Controller, ruft die Methode auf und übergibt alle URI-Segmente oder erfassten Gruppen.
4. **Methodenspezifische Behandlung**: Wenn die Route ein Array ist (wie in Ihrem Code), prüft es die HTTP-Methode (GET, POST, etc.) der Anfrage.
5. **Fallback**: Nicht gematchte Anfragen lösen einen 404-Fehler aus, oder die `$route['404_override']`, falls gesetzt.

**Beispielablauf**:
- Anfrage: `POST https://example.com/lives`
- Matcht: `$route['lives']['POST'] = 'lives/create';`
- Ergebnis: Ruft `Lives::create()` ohne Argumente auf.
- Wenn die Anfrage `GET https://example.com/lives/456` wäre, würde sie `$route['lives/(\d+)']['GET'] = 'lives/one/$1';` matchen → `Lives::one(456)`.

**Wichtige Mechaniken**:
- **Dynamische Parameter**: Erfasste Gruppen (z.B. `$1`) werden als Argumente an die Methode übergeben. Stellen Sie sicher, dass Ihre Controllermethode diese erwartet.
- **Sicherheit**: Routen helfen, den direkten Zugriff auf sensible Controller zu verhindern, indem URLs verschleiert werden.
- **Performance**: Einfache Array-Lookups; kein großer Overhead, es sei denn, Sie haben hunderte von Routen.

#### 3. **Wie man Routen verwendet**
Routen zu verwenden bedeutet, sie wie oben beschrieben einzurichten und sie dann in Ihrer Anwendung (Controller, Views, etc.) zu nutzen.

- **In Controllern**: Gehen Sie davon aus, dass die Route das URL-Mapping übernimmt; schreiben Sie Methoden, die geroutete Anfragen erwarten.
  - Beispiel: Für `$route['login']['POST'] = 'users/login';` erstellen Sie einen `Users.php` Controller mit einer `login()` Methode, die POST-Daten verarbeitet (z.B. via `$this->input->post()`).

- **URLs generieren**: Verwenden Sie CodeIgniters `site_url()` oder `base_url()` mit Ihren Routen-Schlüsseln für Links/Buttons.
  - Beispiel: In einer View, `<a href="<?= site_url('login'); ?>">Login</a>` zeigt auf die geroutete URL, aber Ihr Code definiert, welcher Controller aufgerufen wird.

- **Routen testen**:
  - Verwenden Sie Ihren Webbrowser oder API-Tools (z.B. Postman), um URLs wie `/users/register` aufzurufen.
  - Prüfen Sie `application/logs/log-{date}.php` auf Fehler, wenn Routen fehlschlagen.
  - Debugging hinzufügen: Setzen Sie temporär `$route['404_override']` zurück und verwenden Sie var_dump in einem Test-Controller, um Parameter zu sehen.

- **RESTful Verwendung (wie in Ihrem Code)**: Ihre Routen sind für eine API-ähnliche Struktur eingerichtet. Zum Beispiel:
  - Eine Ressource erstellen: Senden Sie POST an `/lives` → Erstellt ein Live-Event.
  - Lesen: GET `/lives/123` → Holt Live-Event #123.
  - Aktualisieren: POST `/lives/123` → Aktualisiert Live-Event #123.

- **Häufige Fallstricke & Tipps**:
  - **Duplikate**: Vermeiden Sie überlappende Routen (z.B. `lives` und `lives/(\d+)`); setzen Sie spezifische Routen zuerst.
  - **Methoden nicht spezifiziert**: Wenn eine Route ein String ist, funktioniert sie für alle HTTP-Methoden. Verwenden Sie Arrays für Präzision.
  - **Für die Entwicklung**: Aktivieren Sie CodeIgniters Profiler (`$this->output->enable_profiler(TRUE);`) in einem Controller, um das Routing zu debuggen.
  - **Versionskontrolle**: Ihre routes.php befindet sich in der Versionskontrolle – Änderungen wirken sich live auf das Routing aus.
  - **Erweiterungen**: Wenn Sie erweiterte Funktionen benötigen (z.B. Namespace-Support), ziehen Sie CodeIgniter 4 oder Drittanbieter-Bibliotheken in Betracht, da CI 3 (Ihr Code) älter ist.

Wenn Sie spezifische Fragen zu einer Route in Ihrer Datei haben (z.B. warum `(\d+)` verwendet wird oder wie man eine neue hinzufügt), geben Sie bitte mehr Details an! Für das CodeIgniter-Setup stellen Sie sicher, dass `CI_VERSION` in Ihrer index.php definiert ist.