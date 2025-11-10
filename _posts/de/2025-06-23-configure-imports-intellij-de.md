---
audio: false
generated: true
lang: de
layout: post
title: Konfigurieren von Single-Class-Imports in IntelliJ IDEA
translated: true
type: note
---

IntelliJ IDEA bietet Einstellungen, um zu steuern, wie es mit Imports umgeht, einschließlich der Verhinderung der Verwendung von Wildcards. So können Sie es konfigurieren, damit immer Single-Class-Imports verwendet werden:

1.  **Öffnen Sie die Einstellungen (Settings/Preferences):**
    * **Windows/Linux:** `Strg + Alt + S`
    * **macOS:** `Cmd + ,` (Komma)

2.  **Navigieren Sie zu Code Style für Java:**
    * Klicken Sie im linken Bereich des Einstellungsdialogs auf:
        `Editor` -> `Code Style` -> `Java`

3.  **Gehen Sie zum Tab "Imports":**
    * Wählen Sie auf der rechten Seite den Tab `Imports`.

4.  **Konfigurieren Sie die Import-Einstellungen:**
    Hier sehen Sie einige wichtige Einstellungen:

    * **`Use single class import`**: **Aktivieren Sie diese Checkbox.** Dies ist die Haupteinstellung, die IntelliJ anweist, individuelle Klassenimporte Wildcard-Imports vorzuziehen.

    * **`Class count to use import with '*'`**: Diese Einstellung legt fest, wie viele Klassen aus einem einzelnen Package importiert werden müssen, bevor IntelliJ automatisch auf einen Wildcard-Import umschaltet (z.B. `java.util.*`). Um Wildcard-Imports effektiv zu deaktivieren, **setzen Sie diesen Wert auf eine sehr hohe Zahl**, wie `999` oder `9999`. Dies stellt sicher, dass Sie die Schwelle für einen Wildcard-Import praktisch nie erreichen.

    * **`Names count to use static import with '*'`**: Dies ähnelt der obigen Einstellung, gilt jedoch für statische Imports. Setzen Sie auch diesen Wert auf eine hohe Zahl (z.B. `999` oder `9999`), um Wildcard-Statikimporte zu verhindern.

    * **`Packages to Use Imports with '*'`**: Diese Tabelle listet Packages auf, für die IntelliJ *immer* Wildcard-Imports verwendet, unabhängig von den anderen Einstellungen. **Stellen Sie sicher, dass diese Tabelle leer ist**, wenn Sie Wildcard-Imports vollständig vermeiden möchten. Wenn Sie Einträge wie `java.util.*` oder `java.awt.*` sehen, entfernen Sie diese.

5.  **Änderungen übernehmen:**
    * Klicken Sie auf `Apply` und dann auf `OK`, um Ihre Änderungen zu speichern.

**Nachdem Sie diese Änderungen vorgenommen haben:**

* Wenn Sie die "Auto Import"-Funktion verwenden (z.B. durch Drücken von `Alt + Enter` bei einer nicht aufgelösten Klasse), fügt IntelliJ nun individuelle Klassenimporte anstelle von Wildcards ein.
* Wenn Sie bestehende Dateien mit Wildcard-Imports haben, können Sie die Aktion "Optimize Imports" (`Strg + Alt + O` unter Windows/Linux, `Cmd + Option + O` auf macOS) verwenden, um diese gemäß Ihren neuen Einstellungen in Single-Class-Imports umzuwandeln.

Indem Sie diese Schritte befolgen, können Sie effektiv verhindern, dass IntelliJ IDEA Wildcard-Imports für Java-Dateien verwendet.