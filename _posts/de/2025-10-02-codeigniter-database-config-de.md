---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter Datenbankkonfigurationsübersicht
translated: true
type: note
---

### Übersicht der CodeIgniter-Datenbankkonfiguration

Diese PHP-Datei ist ein Konfigurationsskript für die Datenbankkonnektivität von CodeIgniter. Sie definiert Verbindungseinstellungen für verschiedene Datenbankgruppen (z. B. 'default', 'lzwjava', 'leo66', 'testing'), was es der Anwendung ermöglicht, basierend auf der Umgebung (Entwicklung, Testing, Produktion) zwischen ihnen zu wechseln. Die Variable `$active_group` bestimmt, welche Verbindungsgruppe standardmäßig verwendet wird.

Wichtige Komponenten:
- **$query_builder**: Auf `TRUE` gesetzt, um das Laden der Query Builder-Klasse zu aktivieren, die eine objektorientierte Möglichkeit zum Erstellen von SQL-Abfragen bietet.
- **$db[][]**: Ein assoziatives Array, in dem jedes Unterarray (z. B. 'default') detaillierte Konfigurationsoptionen für eine Datenbankverbindung enthält.

Die `$active_group` wird dynamisch basierend auf der `ENVIRONMENT`-Konstante (z. B. über eine switch-Anweisung) gesetzt, um unterschiedliche Einstellungen für verschiedene Bereitstellungsphasen sicherzustellen. Im Folgenden werde ich jede Konfigurationsoption im Detail erklären, unter Bezugnahme auf die CodeIgniter-Dokumentation und die Standardverwendung. Beachten Sie, dass echte sensible Werte (wie Anmeldedaten) hier aus Sicherheitsgründen weggelassen werden; in der Praxis sollten diese sicher gespeichert werden, z. B. über Umgebungsvariablen.

### Detaillierte Konfigurationsoptionen

Jede Datenbankgruppe ist ein Array mit den folgenden Schlüsseln. Die meisten sind einfache Einstellungen, aber einige (wie `encrypt`) unterstützen Unteroptionen für erweiterte Funktionen.

- **dsn** (string): Der vollständige Data Source Name (DSN)-String, der die Verbindung beschreibt. Dies ist eine Alternative zur separaten Angabe von Hostname, Benutzername usw. Es ist nützlich für komplexe Setups wie ODBC. Falls angegeben, überschreibt es die einzelnen Host-/Anmeldefelder. Beispielformat: `'dsn' => 'mysql:host=yourhost;dbname=yourdatabase'`.

- **hostname** (string): Die Adresse des Datenbankservers (z. B. 'localhost' oder eine IP wie '127.0.0.1'). Dies identifiziert, wo die Datenbank läuft, und ermöglicht Verbindungen über TCP/IP oder Sockets.

- **username** (string): Der Kontoname, der zur Authentifizierung beim Datenbankserver verwendet wird. Dies sollte einem gültigen Benutzer im Datenbankmanagementsystem entsprechen.

- **password** (string): Der geheime Schlüssel, der mit dem Benutzernamen für die Authentifizierung gepaart ist. Bewahren Sie diesen immer sicher auf, um eine Preisgabe zu verhindern.

- **database** (string): Der spezifische Datenbankname, zu dem Sie auf dem Server eine Verbindung herstellen möchten. Alle Abfragen zielen standardmäßig auf diese Datenbank, sofern nicht anders angegeben.

- **dbdriver** (string): Gibt den zu verwendenden Datenbanktreiber an (z. B. 'mysqli' für MySQL). Gängige Treiber sind 'cubrid', 'ibase', 'mssql', 'mysql', 'mysqli', 'oci8', 'odbc', 'pdo', 'postgre', 'sqlite', 'sqlite3' und 'sqlsrv'. 'mysqli' ist eine moderne, sichere Wahl für MySQL.

- **dbprefix** (string): Ein optionales Präfix, das Tabellennamen hinzugefügt wird, wenn der Query Builder von CodeIgniter verwendet wird (z. B. wird 'mytable' zu 'prefix_mytable', wenn es auf 'prefix_' gesetzt ist). Dies hilft, Tabellen im Shared Hosting oder in Multi-Tenant-Apps zu namespace.

- **pconnect** (boolean): Aktiviert persistente Verbindungen (`TRUE`) oder reguläre Verbindungen (`FALSE`). Persistente Verbindungen wiederverwenden denselben Link, was die Leistung für hoch belastete Apps verbessert, aber sie können Serverressourcen erschöpfen, wenn sie übermäßig genutzt werden.

- **db_debug** (boolean): Steuert, ob Datenbankfehler zur Fehlerbehebung angezeigt werden (`TRUE`). Deaktivieren (`FALSE`) in der Produktion, um zu vermeiden, dass sensible Fehlerdetails an Benutzer weitergegeben werden.

- **cache_on** (boolean): Aktiviert (`TRUE`) oder deaktiviert (`FALSE`) das Zwischenspeichern von Abfragen. Wenn aktiviert, werden Ergebnisse gespeichert, um wiederholte Abfragen zu beschleunigen.

- **cachedir** (string): Der Dateipfad zum Verzeichnis, in dem zwischengespeicherte Abfrageergebnisse gespeichert werden. Muss vom Webserver beschreibbar sein. In Kombination mit `cache_on` reduziert dies die Datenbanklast.

- **char_set** (string): Die Zeichenkodierung für die Datenbankkommunikation (z. B. 'utf8mb4' für moderne Unicode-Unterstützung). Stellt die Datenintegrität für mehrsprachige Apps sicher.

- **dbcollat** (string): Die Kollation für das Sortieren und Vergleichen von Zeichen (z. B. 'utf8mb4_unicode_ci' für case-insensitive Unicode). Dies dient als Fallback für älteres PHP/MySQL; wird sonst ignoriert.

- **swap_pre** (string): Ein Tabellenpräfix, um `dbprefix` dynamisch zu ersetzen. Nützlich zum Austauschen von Präfixen in bestehenden Apps ohne Umbenennung von Tabellen.

- **encrypt** (boolean oder array): Für Verschlüsselungsunterstützung. Für 'mysql' (veraltet), 'sqlsrv' und 'pdo/sqlsrv', verwenden Sie `TRUE`/`FALSE` zum Aktivieren/Deaktivieren von SSL. Für 'mysqli' und 'pdo/mysql' verwenden Sie ein Array mit SSL-Unteroptionen:
  - 'ssl_key': Pfad zur privaten Schlüsseldatei (z. B. für Client-Zertifikate).
  - 'ssl_cert': Pfad zur öffentlichen Schlüsselzertifikatsdatei.
  - 'ssl_ca': Pfad zur Zertifizierungsstellendatei (validiert Serverzertifikat).
  - 'ssl_capath': Pfad zu einem Verzeichnis vertrauenswürdiger CA-Zertifikate im PEM-Format.
  - 'ssl_cipher': Doppelpunkt-getrennte Liste erlaubter Chiffren (z. B. 'AES128-SHA').
  - 'ssl_verify': Nur für 'mysqli'; `TRUE` zum Überprüfen von Serverzertifikaten, `FALSE` zum Überspringen (weniger sicher; für selbstsignierte Zertifikate verwenden).

- **compress** (boolean): Aktiviert die clientseitige Komprimierung für MySQL-Verbindungen, reduziert den Netzwerkverkehr (nur MySQL; wird von anderen Treibern ignoriert).

- **stricton** (boolean): Erzwingt 'Strict Mode'-Verbindungen (`TRUE`), die strikte SQL-Regeln durchsetzt, um Fehler frühzeitig zu erkennen (z. B. ungültige Datentypen). Nützlich während der Entwicklung.

- **ssl_options** (array): Erweiterte SSL-Konfigurationsoptionen für Treiber wie 'pdo'. Ermöglicht die Feinabstimmung von Verschlüsselungsparametern, die nicht von `encrypt` abgedeckt werden.

- **failover** (array): Backup-Verbindungsarray(s) für automatisches Umschalten, wenn die primäre Verbindung fehlschlägt. Jedes Element spiegelt die Hauptkonfiguration wider (z. B. alternativer Hostname/Port). Beispiel: `array(array('hostname' => 'backuphost', ...))`.

- **save_queries** (boolean): Speichert ausgeführte Abfragen im Speicher zur Fehlerbehebung (`TRUE`). Bietet Zugriff auf Methoden wie `$this->db->last_query()`, kann aber die Speichernutzung erhöhen; deaktivieren (`FALSE`) in der Produktion, um Ressourcen zu sparen.

### Datenbankgruppen und Umgebungswechsel

- **default**: Das Basis-Konfigurationsarray, das als Vorlage dient. Es ist auf 'Produktion'-Standardeinstellungen gesetzt (z. B. kein Debugging, gesicherte Einstellungen).
- **lzwjava**: Erbt von der Basis, überschreibt aber den Benutzernamen mit einem anderen Wert (Passwort leer gelassen, was keine Authentifizierung oder Standard impliziert).
- **leo66**: Erbt Basiseinstellungen, ändert aber den Hostnamen auf Local Loopback, Benutzername/Passwort auf Standardwerte und fügt einen Port hinzu (3306, Standard für MySQL).
- **testing**: Eine dedizierte Gruppe für Testumgebungen; erbt die Basis-Konfiguration.

Die `switch`-Anweisung aktiviert die entsprechende Gruppe basierend auf `ENVIRONMENT`:
- Entwicklung: Verwendet 'lzwjava'.
- Testing: Verwendet 'testing'.
- Produktion: Verwendet 'default'.

Dieses Setup fördert die Flexibilität für lokale Entwicklung, Tests und Live-Bereitstellungen. Sanieren Sie immer Eingaben, um SQL-Injection zu verhindern, und ziehen Sie in Betracht, Anmeldedaten zur Sicherheit in Umgebungsvariablen zu verschieben. Für vollständige Dokumentationen lesen Sie bitte das offizielle Benutzerhandbuch von CodeIgniter zu Datenbankverbindungen. Wenn Sie eine bestimmte Option oder Gruppe näher erläutern möchten, lassen Sie es mich wissen!