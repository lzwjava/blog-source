---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter Benutzer-Agent-Konfigurationsarrays
translated: true
type: note
---

### Übersicht
Dieser PHP-Codeausschnitt ist Teil des CodeIgniter-Frameworks (ein PHP-Webframework), speziell aus der Konfigurationsdatei der User Agent Class. Er definiert vier Arrays (`$platforms`, `$browsers`, `$mobiles` und `$robots`), die Fragmente aus User-Agent-Strings menschenlesbaren Namen für Browser, Betriebssysteme, Mobilgeräte und Webcrawler/Bots zuordnen. Der Code wird verwendet, um den Typ des Geräts, Browsers oder Bots, der eine Website besucht, basierend auf dem vom Client gesendeten HTTP-User-Agent-Header zu analysieren und zu identifizieren.

Die Arrays sind assoziativ (Schlüssel-Wert-Paare), wobei die Schlüssel Teilzeichenketten aus den User-Agent-Strings sind (Groß-/Kleinschreibung wird ignoriert) und die Werte die entsprechenden Anzeigenamen sind. Die User-Agent-Bibliothek von CodeIgniter verwendet diese zur Erkennung, z. B. um festzustellen, ob ein Besucher Android nutzt, Chrome verwendet oder ein Suchbot ist.

### $platforms Array
Dieses Array identifiziert Betriebssysteme oder Plattformen. Die Schlüssel sind Teilzeichenketten, die im User-Agent-Header vorkommen könnten, und die Werte sind saubere Anzeigenamen.

- **Beispieleinträge**:
  - `'windows nt 10.0'` → `'Windows 10'`
  - `'android'` → `'Android'`
  - `'os x'` → `'Mac OS X'`
- **Zweck**: Hilft bei der Erkennung des Client-Betriebssystems (z. B. Windows, iOS, Linux) für Analysen, Content-Anpassung oder Feature-Optimierungen.
- **Hinweis**: Die Reihenfolge ist für die Genauigkeit wichtig, da sich einige Teilzeichenketten überschneiden könnten (z. B. `'windows'` als Auffangposition am Ende).

### $browsers Array
Identifiziert Webbrowser. Browser melden oft mehrere Identifikatoren, daher priorisiert die Reihenfolge Subtypen zuerst (gemäß Kommentar).

- **Beispieleinträge**:
  - `'Chrome'` → `'Chrome'`
  - `'MSIE'` → `'Internet Explorer'`
  - `'Firefox'` → `'Firefox'`
  - Sonderfall: `'Opera.*?Version'` (regex-ähnliche Übereinstimmung) für modernes Opera, das sich als "Opera/9.80" mit einer Version meldet.
- **Zweck**: Ermittelt den Browser (z. B. Chrome, Safari), um browserspezifische Funktionen bereitzustellen oder Weiterleitungen durchzuführen.
- **Regex-Hinweis**: Einige Schlüssel verwenden einfache Regex-Muster (z. B. `.*?` für Wildcard-Matching), die in der Bibliothek behandelt werden.

### $mobiles Array
Ordnet Kennzeichen aus User-Agent-Strings für Mobilgeräte, Telefone und verwandte Geräte/Browser zu. Es ist umfangreicher und enthält Telefone, Tablets, Spielkonsolen und Fallback-Kategorien.

- **Strukturierte Abschnitte**:
  - Telefone/Hersteller: `'iphone'` → `'Apple iPhone'`, `'samsung'` → `'Samsung'`.
  - Betriebssysteme: `'android'` → `'Android'`, `'symbian'` → `'Symbian'`.
  - Browser: `'opera mini'` → `'Opera Mini'`, `'fennec'` → `'Firefox Mobile'`.
  - Sonstige/Fallback: `'mobile'` → `'Generic Mobile'` für nicht erkannte mobile Indikatoren.
- **Zweck**: Kennzeichnet Mobilgeräte für responsives Design, mobile Funktionen oder App-Weiterleitungen. Enthält veraltete Einträge (einige als veraltet auskommentiert).

### $robots Array
Listet gängige Webcrawler und Bots auf. Schlüssel sind Teilzeichenketten aus Bot-User-Agent-Strings.

- **Beispieleinträge**:
  - `'googlebot'` → `'Googlebot'`
  - `'bingbot'` → `'Bing'`
  - `'yandex'` → `'YandexBot'`
- **Zweck**: Identifiziert Crawler für die SEO-Behandlung, z. B. um Bots anderen Content zu servieren (z. B. ohne Werbung) oder Bot-Traffic zu protokollieren.

### Verwendung in CodeIgniter
- Die User Agent Class lädt diese Datei und verwendet Methoden wie `is_browser()`, `is_mobile()`, `is_robot()` und `platform()`, um den User-Agent-String zu analysieren.
- Sie führt eine Suche ohne Beachtung der Groß-/Kleinschreibung durch diese Arrays durch, um Schlüssel mit dem String abzugleichen.
- Bei Diskrepanzen (z. B. neue Geräte/Browser, die nicht aufgeführt sind) müssten diese Arrays manuell oder über Community-Erweiterungen aktualisiert werden.

### Zusätzliche Hinweise
- **Sicherheit**: Dies dient rein der Datenerfassung; es wird kein schädlicher Code ausgeführt. User-Agent-Strings können gefälscht werden, daher sollte man sich nicht für kritische Sicherheitsprüfungen darauf verlassen.
- **Aktualisierungen**: CodeIgniter-Versionen können Einträge hinzugefügt/geändert haben; dies sieht aus wie eine ältere Momentaufnahme (z. B. Edge als 'Spartan' ist veraltet).
- **Testmöglichkeit**: In einem PHP-Skript könnte man dies laden und `strpos` oder Regex verwenden, um einen Beispiel-User-Agent-String abzugleichen.

Wenn Sie einen bestimmten Teil erläutern möchten oder eine Frage zur Implementierung haben, lassen Sie es mich wissen!