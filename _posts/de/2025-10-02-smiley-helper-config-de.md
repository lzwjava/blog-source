---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Konfiguration des CodeIgniter Smiley-Helpers
translated: true
type: note
---

### Übersicht
Dies ist eine PHP-Konfigurationsdatei aus dem CodeIgniter Web-Framework, speziell für den **Emoticons/Smileys Helper**. CodeIgniter ist ein PHP MVC-Framework zum Erstellen von Web-Apps. Diese Datei definiert eine Reihe von Smiley-/Emoticon-Zuordnungen, die vom `smiley_helper` des Frameworks verwendet werden, um textbasierte Emoticons (wie `:-)`) automatisch durch HTML-`<img>`-Tags zu ersetzen, die entsprechende GIF-Bilder anzeigen.

Die Datei stellt sicher, dass der direkte Zugriff über `defined('BASEPATH') OR exit('No direct script access allowed');` blockiert wird, eine Sicherheitsmaßnahme in CodeIgniter, um unerlaubte direkte Skriptausführung zu verhindern.

### Wichtige Komponenten
- **Zweck**: Wandelt reine Text-Emoticons in benutzer-generierten Inhalten (z.B. Forenbeiträge oder Kommentare) in visuelle Bilder um, für eine bessere Benutzererfahrung.
- **Datenstruktur**: `$smileys` ist ein assoziatives PHP-Array mit folgender formaler Struktur:
  ```
  $smileys = array(
      'smiley_code' => array('image_file', 'width', 'height', 'alt_text'),
      // ...
  );
  ```
  - **smiley_code**: Das zu suchende Textmuster (z.B. `:-)`, `:lol:`, `>:(`).
  - **image_file**: Name der GIF-Datei im Smiley-Verzeichnis (standardmäßig `application/views/smileys/` in CodeIgniter).
  - **width/height**: Abmessungen in Pixel für den `<img>`-Tag (hier sind alle `'19'`, was auf 19x19px GIFs hinweist).
  - **alt_text**: Alternativtext für Barrierefreiheit/Bildschirmleser, der die Emotion beschreibt.

- **Verwendung in CodeIgniter**: Lade den Helper mit `$this->load->helper('smiley');`, dann rufe Funktionen wie `parse_smileys($text)` für Zeichenketten auf, die Emoticon-Codes enthalten. Dies ersetzt Codes durch `<img>`-Tags, z. B.:
  - Eingabe: `I'm happy :)`  
    Ausgabe: `I'm happy <img src="http://example.com/smileys/smile.gif" width="19" height="19" alt="smile">`

### Übersicht der Einträge
Das Array enthält 40+ Zuordnungen, gruppiert nach Emotionstyp. Die meisten Bilder sind 19x19px GIFs. Hier ist eine zusammengefasste Übersicht (mit Beispielen):

| Smiley-Code(s) | Bild | Alt-Text | Anmerkungen |
|---------------|-------|----------|-------|
| `:-)`, `:)` | grin.gif, smile.gif | grin, smile | Positive Grinsen und Lächeln. |
| `:lol:`, `:cheese:` | lol.gif, cheese.gif | LOL, cheese | Lautes Lachen/Daumen hoch, käsiges Grinsen. |
| `;-)`, `;)` | wink.gif | wink | Zwinkern. |
| `:smirk:`, `:roll:` | smirk.gif, rolleyes.gif | smirk, rolleyes | Sarkasmus/weise nickend. |
| `:-S`, `:wow:`, `:bug:` | confused.gif, surprise.gif, bigsurprise.gif | confused, surprised, big surprise | Verwirrung/Überraschung. |
| `:-P`, `%-P`, `;-P`, `:P` | tongue_laugh.gif, etc. | tongue laugh, etc. | Varianten mit herausgestreckter Zunge (lachend, zwinkernd, spöttisch). |
| `:blank:`, `:long:`, `:ohh:`, `:grrr:`, `:gulp:`, `8-/` | Verschiedene | blank stare, long face, ohh, grrr, gulp, oh oh | Neutrale oder verärgerte Gesichter. |
| `:down:`, `:red:`, `:sick:`, `:shut:` | Verschiedene | downer, red face, sick, shut eye | Traurig, verlegen, krank. |
| `:-/`, `>:(` (`:mad:`), `>:-(` (`:angry:`) | hmm.gif, mad.gif, angry.gif | hmmm, mad, angry | Verwirrt, sauer, wütend. |
| `:zip:`, `:kiss:` | zip.gif, kiss.gif | zipper, kiss | Mund zu, Kuss. |
| `:ahhh:`, `:coolsmile:`, `-:coolsmirk:`, `:coolgrin:`, `:coolhmm:`, `:coolmad:`, `:coolcheese:` | shock.gif, shade_smile.gif, etc. | shock, cool smile, cool smirk, cool grin, cool hmm, cool mad, cool cheese | Schockiert oder "coole"/Sonnenbrillen-Varianten. |
| `:vampire:`, `:snake:` | vampire.gif, snake.gif | vampire, snake | Thematisierte Emoticons. |
| `:exclaim:`, `:question:` | exclaim.gif, question.gif | exclaim, question | Entsprechungen von Satzzeichen (!, ?). |

### Erweiterung und Anpassung
- **Smileys hinzufügen**: Füge neue Einträge an, z.B. `':fire:' => array('fire.gif', '19', '19', 'fire');`.
- **Bilder ändern**: Aktualisiere Dateinamen, wenn GIFs durch PNGs/JPGs ersetzt werden (passe Breite/Höhe entsprechend an).
- **Verzeichnis**: Stelle sicher, dass die Bilder im CodeIgniter Smiley-Pfad existieren.
- **Einschränkungen**: Alle Bilder hier haben die gleiche Größe; echte Implementierungen könnten variieren. Dieses Array definiert nur die Zuordnungen – die Ersetzungslogik liegt im Helper selbst.

Wenn Sie eine spezifische Frage zur Anpassung oder Verwendung in CodeIgniter haben, geben Sie bitte mehr Details an!