---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter Hooks Überblick
translated: true
type: note
---

### Was sind Hooks in CodeIgniter?

Hooks in CodeIgniter sind eine Möglichkeit, die Funktionalität des Frameworks zu erweitern, ohne dessen Kern-Dateien zu modifizieren. Sie ermöglichen es, benutzerdefinierten Code an bestimmten Punkten im Ausführungszyklus auszuführen, wie z. B. vor oder nach dem Laden von Controllern, beim Überschreiben der Ausgabe oder beim Caching. Dies erhält die Upgrade-Fähigkeit, indem Ihr Code von der offiziellen Codebasis getrennt wird.

Hooks werden in `application/config/hooks.php` definiert und in `application/config/config.php` aktiviert, indem `$config['enable_hooks'] = TRUE;` gesetzt wird.

### Hooks aktivieren

1. Öffnen Sie `application/config/config.php`.
2. Setzen Sie die Konfigurationsvariable:
   ```php
   $config['enable_hooks'] = TRUE;
   ```
   Dies weist CodeIgniter an, die Hook-Datei zu prüfen und auszuführen.

### Hooks definieren

Hooks werden als ein Array von Arrays in `application/config/hooks.php` konfiguriert. Jedes Hook-Array spezifiziert:
- `class`: (Erforderlich) Der Klassenname (muss mit dem Dateinamen übereinstimmen).
- `function`: (Erforderlich) Der Methodenname in der Klasse.
- `filename`: (Erforderlich) Der Dateiname der Klasse (ohne .php).
- `filepath`: (Optional) Der Ordnerpfad zur Datei, standardmäßig `application/hooks/`.
- `params`: (Optional) Ein Array von Parametern, die an die Methode übergeben werden sollen.

Platzieren Sie Ihre Hook-Klassen in `application/hooks/`.

### Hook-Punkte

CodeIgniter bietet diese vordefinierten Punkte, an denen Hooks ausgeführt werden können:
- **pre_system**: Läuft, bevor das System geladen wird (noch nichts anderes ist gelaufen).
- **pre_controller**: Läuft direkt bevor der Controller aufgerufen wird.
- **post_controller_constructor**: Läuft, nachdem der Controller instanziiert wurde, aber bevor seine Methoden ausgeführt werden.
- **post_controller**: Läuft, nachdem der Controller beendet ist.
- **display_override**: Läuft anstelle der Ausgabe an den Browser (überschreibt _display create/exit controller file).
- **cache_override**: Läuft anstelle des Ladens des Caches (überschreibt _display the cache).
- **post_system**: Läuft, nachdem die Webseite vollständig an den Browser gesendet wurde.

### Beispiel zur Verwendung

Angenommen, Sie möchten jede Anfrage protokollieren, bevor der Controller läuft. Erstellen Sie einen Hook für `pre_controller`.

1. Erstellen Sie die Datei `application/hooks/my_hook.php`:
   ```php
   <?php
   class My_hook {
       public function log_request() {
           // Beispiel: In eine Datei oder Datenbank protokollieren
           log_message('info', 'Controller about to be called: ' . $this->uri->uri_string());
       }
   }
   ```

2. Fügen Sie in `application/config/hooks.php` hinzu:
   ```php
   $hook['pre_controller'] = array(
       'class' => 'My_hook',
       'function' => 'log_request',
       'filename' => 'my_hook.php',
       'filepath' => 'hooks', // Optional, standardmäßig application/hooks/
       'params' => array() // Optionale Parameter
   );
   ```

Jetzt wird jedes Mal, wenn ein Controller kurz vor der Ausführung steht, `log_request` ausgeführt.

### Best Practices
- Verwenden Sie Hooks sparsam; erweitern Sie wenn möglich Controller oder verwenden Sie Libraries.
- Testen Sie Hooks immer in einer Entwicklungsumgebung, um sicherzustellen, dass sie nicht in die Kernlogik eingreifen.
- Weitere Details finden Sie im offiziellen CodeIgniter Benutzerhandbuch zu Hooks.