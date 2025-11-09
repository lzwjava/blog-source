---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Konfigurationsleitfaden für CodeIgniter Transliteration
translated: true
type: note
---

### Zweck in CodeIgniter
Dies ist eine Konfigurationsdatei (mit dem Namen `foreign_characters.php` in CodeIgniter) aus der **Text Helper**-Bibliothek. Sie wird für **Transliteration** verwendet, einen Prozess, der Nicht-ASCII-Zeichen (akzentuierte, diakritische oder fremdsprachige Zeichen) in ihre nächsten ASCII-Entsprechungen umwandelt (z.B. ä → ae, ñ → n). Dies hilft bei Aufgaben wie URL-Slugs, datenbanksicheren Zeichenketten oder plattformübergreifender Kompatibilität, bei denen Sonderzeichen Probleme verursachen könnten.

- Sie ist Teil der älteren CodeIgniter-Versionen (vor 4.x); in CI4 wurde eine ähnliche Funktionalität in Helper oder globale Funktionen verschoben.
- Das Array verwendet Regex-Muster (z.B. `/ä|æ|ǽ/` für ä, æ oder ǽ), um Zeichen durch einfache englische Buchstaben zu ersetzen.
- Wichtige Funktionen, die dies verwenden: `convert_accented_characters()` im Text Helper, die durch dieses Array iteriert und einen `preg_replace` durchführt.

Dies ist kein Framework-Kerncode, sondern ein Hilfsprogramm, das oft in Installationen unter `application/config/foreign_characters.php` zu finden ist.

### Repräsentierte Sprachen und Zeichensätze
Das Array deckt Zeichen aus mehreren Schriften und Sprachen ab, um eine breite Transliteration zu ermöglichen. Hier ist eine Aufschlüsselung nach Kategorie, inklusive Beispiele (aus dem Code) und ihren Sprachen/Quellen:

- **Latein (Westeuropäisch)**: Diakritische Zeichen, die in romanischen und germanischen Sprachen üblich sind.
  - Akzente (z.B. ÀÁÂ → A, àáâ → a) für Französisch, Spanisch, Portugiesisch, Katalanisch.
  - Umlaute (z.B. Ä → Ae, ä → ae, Ü → Ue) für Deutsch, Schwedisch.
  - Ligaturen (z.B. æ → ae für Dänisch/Norwegisch, œ → oe für Französisch).
  - Besonderheiten (z.B. ñ → n für Spanisch, ł → l für Polnisch, þ → th für Isländisch).

- **Griechisch (Hellenisch)**: Kyrillisch-ähnliche Buchstaben für das griechische Alphabet.
  - Z.B. Γ → G, Δ → Dj, Η → I, Ν → N, Ο → O, Ρ → R, Σ → S, Τ → T (altgriechisch/modernes Griechisch).

- **Kyrillisch (Slawisch und Osteuropäisch)**: Basierend auf Russisch, Ukrainisch, Belarussisch usw.
  - Grundlagen: А → A, Б → B, В → V, Г → G, Д → D, Ж → Zh, З → Z, П → P, Р → R, С → S, Т → T, Ф → F, Х → Kh, Ц → Ts, Ч → Ch, Ш → Sh, Щ → Shch, Ъ/Ь (weiche/harte Zeichen) → gelöscht (keine Entsprechung), Ю → Yu, Я → Ya.
  - Extras: Ё/ё → Yo/yo (Russisch), Є/є → Ye/ye (Ukrainisch), Ї/ї → Yi/yi (Ukrainisch), Й → Y (Varianten in Russisch/Ukrainisch).

- **Andere Symbole/Zeichen**:
  - ß → ss (Deutsches "scharfes S").
  - ½ → (normalerweise entfernt oder ignoriert, nicht in diesem Array, aber ähnlich).
  - Mathematische/Griechische Extras: ξ → ks, π → p, β → v, μ → m, ψ → ps (verwendet für wissenschaftliche Transliteration).

Dies deckt ~90 % der gängigen Nicht-ASCII-Zeichen in internationalen Webinhalten ab. Wenn ein Zeichen nicht aufgeführt ist, wird es möglicherweise unverändert behandelt oder entfernt. Die Reihenfolge ist wichtig (verarbeitet via `preg_replace`), um sicherzustellen, dass Ersetzungen mit mehreren Zeichen zuerst stattfinden. Für moderne Apps sollte die UTF-8-Unterstützung gegenüber der Transliteration priorisiert werden. Wenn Sie dies anpassen oder erweitern müssen, befindet es sich in der Helper-Datei.