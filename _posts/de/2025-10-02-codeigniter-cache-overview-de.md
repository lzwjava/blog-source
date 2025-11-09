---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Übersicht des CodeIgniter-Cache-Systems
translated: true
type: note
---

### Übersicht der CodeIgniter Cache-Bibliothek

Die `CI_Cache`-Klasse von CodeIgniter ist ein flexibles Caching-System, das eine einheitliche Schnittstelle zum Speichern und Abrufen von Daten über verschiedene Backends (wie In-Memory, Dateibasiert oder externe Dienste) bietet. Sie erweitert `CI_Driver_Library`, welche Treiber dynamisch lädt. Die Klasse abstrahiert Cache-Operationen, sodass Entwickler Backends einfach über die Konfiguration wechseln können, ohne Anwendungscode zu ändern. Alle Methoden delegieren an den aktiven "Adapter" (eine Treiberklasse), mit Fallback-Unterstützung für Zuverlässigkeit.

Das System betont Leistung, Portabilität und Fehlertoleranz – z.B. verwendet es standardmäßig einen "Dummy"-Treiber (No-Op), wenn andere fehlschlagen, um sicherzustellen, dass die App nicht aufgrund von Cache-Problemen abstürzt.

### Unterstützte Cache-Treiber und Adapter

Die Klasse unterstützt mehrere Treiber, definiert in `$valid_drivers`:
- **apc**: Verwendet PHP's APC (Alternative PHP Cache) für In-Memory-Speicher (schnell, eingebaut).
- **dummy**: Ein Platzhalter, der nichts tut (gibt immer TRUE oder FALSE zurück); wird als Fallback für Entwicklung/Test verwendet.
- **file**: Speichert Daten als serialisierte Dateien in einem Verzeichnis (angegeben durch `$_cache_path`), geeignet für Seiten mit geringem Traffic.
- **memcached**: Schnittstelle zum Memcached-Dienst für verteiltes, In-Memory-Caching (hohe Leistung, skalierbar).
- **redis**: Schnittstelle zu Redis, einem weiteren In-Memory-Schlüssel-Wert-Speicher mit Funktionen wie Pub/Sub und atomaren Operationen.
- **wincache**: Windows-spezifisch für IIS (verwendet Microsoft WinCache).

Jeder Treiber ist eine separate Klasse (z.B. `CI_Cache_memcached`), die Methoden wie `get()`, `save()`, etc. implementiert. Die Bibliothek lädt den Treiber dynamisch basierend auf dem `$config['adapter']`-Array, das an den Konstruktor übergeben wird.

### Initialisierung und Konfiguration

- **Konstruktor**: Nimmt ein `$config`-Array mit Schlüsseln für `adapter` (primärer Treiber), `backup` (Fallback-Treiber) und `key_prefix` (Zeichenkette, die allen Cache-Schlüsseln vorangestellt wird, für Namespacing/Isolierung).
  - Beispielkonfiguration: `array('adapter' => 'redis', 'backup' => 'file', 'key_prefix' => 'myapp_')`.
- **Fallback-Logik**: Nach der Initialisierung wird geprüft, ob der primäre Adapter unterstützt wird, mittels `is_supported($driver)` (was die `is_supported()`-Methode des Treibers aufruft und auf erforderliche PHP-Erweiterungen oder Dienste testet).
  - Wenn der Primäre fehlschlägt, wird auf den Backup-Treiber gewechselt. Wenn beide fehlschlagen, wird ein Fehler protokolliert und standardmäßig auf "Dummy" zurückgegriffen (über `log_message()`).
  - Dies stellt sicher, dass der Cache immer einen funktionierenden Adapter hat und verhindert Abstürze.

Der `$_cache_path` wird für dateibasierte Treiber gesetzt, aber er wird hier nicht initialisiert – wahrscheinlich wird dies in der Datei-Treiber-Klasse gehandhabt.

### Wichtige Methoden und deren Funktionsweise

Methoden stellen den `key_prefix` IDs für eindeutige Scoping voran (z.B. `'myapp_user123'`) und delegieren an den aktiven Adapter. Alle Operationen geben bei Erfolg/Misserfolg Booleans, Arrays oder gemischte Daten zurück.

- **get($id)**: Ruft zwischengespeicherte Daten anhand der ID ab.
  - Beispiel: `$data = $cache->get('user_profile');` – ruft die `get()`-Methode des Adapters auf.
  - Wenn der Schlüssel existiert und nicht abgelaufen ist, werden die Daten zurückgegeben; andernfalls wird FALSE zurückgegeben.
  - Keine direkte TTL-Erzwingung hier; wird vom Treiber gehandhabt (z.B. Redis oder Memcached erzwingen TTL intern).

- **save($id, $data, $ttl = 60, $raw = FALSE)**: Speichert Daten mit einer Time-to-Live (TTL) in Sekunden.
  - Beispiel: `$cache->save('user_profile', $profile_data, 3600);` – speichert mit 1-Stunden-Ablauf.
  - Das `$raw`-Flag (standardmäßig false) gibt an, ob Daten serialisiert sind – Treiber handhaben Serialisierung falls nötig (z.B. werden Arrays/Objekte zu Strings).
  - Gibt TRUE bei Erfolg zurück, was bedingte Logik erleichtert (z.B. Daten generieren und cachen, wenn das Speichern fehlschlägt).

- **delete($id)**: Entfernt einen bestimmten Cache-Eintrag.
  - Beispiel: `$cache->delete('user_profile');` – dauerhafte Entfernung.

- **increment($id, $offset = 1)** und **decrement($id, $offset = 1)**: Atomare Operationen für numerische Werte (nützlich für Zähler).
  - Beispiel: `$new_counter = $cache->increment('hits', 5);` – erhöht um 5, falls vom Treiber unterstützt (z.B. Redis/Memcached sind atomar; dateibasierte können es simulieren).
  - Nicht alle Treiber unterstützen raw/inc/dec (Dummy schlägt immer fehl); gibt den neuen Wert oder FALSE zurück.

- **clean()**: Löscht alle Cache-Daten für den aktuellen Treiber.
  - Beispiel: `$cache->clean();` – nützlich zum Leeren nach Updates.
  - Der Typ "user" zielt auf benutzerspezifische Daten ab, nicht auf System-Caches.

- **cache_info($type = 'user')**: Gibt Metadaten über den Cache zurück (z.B. Server-Statistiken, Schlüsselanzahlen oder Dateipfade).
  - Beispiel: `$info = $cache->cache_info();` – ein Array mit Details vom Treiber.

- **get_metadata($id)**: Ruft Details über einen bestimmten zwischengespeicherten Eintrag ab (z.B. Ablaufzeit, Größe).
  - Beispiel: `$meta = $cache->get_metadata('key');` – hilft beim Debuggen oder Optimieren.

- **is_supported($driver)**: Prüft die Verfügbarkeit eines Treibers (ergebnisse werden mittels eines statischen `$support`-Arrays zwischengespeichert, um wiederholte Prüfungen zu vermeiden).

### Zusätzliche Mechanismen

- **Schlüssel-Präfixing**: Wird automatisch auf alle IDs angewendet (z.B. für App-Isolierung oder Multi-Tenancy). Wird über die Konfiguration aktiviert, um Schlüssel-Kollisionen über verschiedene Umgebungen hinweg zu verhindern.
- **Protokollierung**: Verwendet `log_message()` für Debug-/Fehlermeldungen (z.B. Fallbacks), integriert in CodeIgniters Protokollierungssystem.
- **Flexibilität und Fehlertoleranz**: Durch die Abstraktion der Backends kann man mit minimalen Änderungen von Datei-Caching (günstig, lokal) zu Redis (schnell, verteilt) wechseln. Der Dummy-Fallback bedeutet, dass Cache-Fehler die App nicht anhalten – Methoden geben einfach FALSE zurück, sodass der Code fortfahren kann (z.B. Abruf aus der DB stattfindet).
- **Leistungshinweise**: Treiber wie APC/Redis sind In-Memory (schneller Zugriff, Sub-Millisekunde). Dateibasiert ist langsamer aufgrund von Disk-I/O. TTLs werden generell von den Treibern eingehalten, außer in seltenen, treiberspezifischen Grenzfällen.

Dieses Design macht das Caching von CodeIgniter modular und zuverlässig. Für Details zu bestimmten Treibern, siehe die Treiberdateien (z.B. `Cache_memcached.php`). Konsultieren Sie immer die offizielle CodeIgniter-Dokumentation für versionsspezifische Nuancen, da dieser Code aus einer älteren Version stammt (ca. 2.0-3.x). Wenn Sie eine bestimmte Methode oder einen Treiber im Sinn haben, kann ich tiefer eintauchen!