---
audio: false
generated: true
image: false
lang: de
layout: post
title: Grundlagen der Fenstersteuerung mit PyWin32
translated: true
type: note
---

Hier ist eine Anleitung zur Arbeit mit **PyWin32-Fenstern** – mit Schwerpunkt auf ihren Eigenschaften, Aktivierung und Behandlung des unteren Bereichs.

---

## 1. Was ist ein Fenster in PyWin32?

In PyWin32 bezieht sich ein "Fenster" auf jedes GUI-Element, das von der Windows API verwaltet wird und über ein **Handle (HWND)** verfügt. Dies kann ein Top-Level-Anwendungsfenster, ein Dialogfeld oder sogar ein Steuerelement innerhalb eines Formulars sein.

Typischerweise interagieren Sie mit Fenstern über:

* `win32gui` – Low-Level-Funktionen für Fenster-Handles, Eigenschaften und Nachrichten.
* `win32con` – Konstanten für Windows-Nachrichten und -Stile.
* `win32api` – Allgemeine Windows-API-Funktionen.

---

## 2. Häufige Fenstereigenschaften

Ein Fenster verfügt über viele Attribute, die Sie abfragen oder ändern können:

* **Handle (HWND)**: Eindeutiger Bezeichner des Fensters.
* **Titel (Beschriftung)**: Text, der in der Titelleiste angezeigt wird (`win32gui.GetWindowText(hwnd)`).
* **Klassenname**: Registrierte Klasse des Fensters (`win32gui.GetClassName(hwnd)`).
* **Stile**: Definiert, wie sich das Fenster verhält/aussieht (`GetWindowLong` mit `GWL_STYLE`).
* **Position & Größe**: Rechteckkoordinaten über `GetWindowRect(hwnd)` oder `MoveWindow`.
* **Sichtbarkeit**: Ob das Fenster angezeigt wird (`IsWindowVisible`).
* **Aktivierungszustand**: Ob es Eingaben akzeptiert (`IsWindowEnabled`).
* **Parent/Owner**: Hierarchie der Fenster (`GetParent(hwnd)`).

---

## 3. Fensteraktivierung

Um ein Fenster in den Vordergrund zu holen oder es aktiv zu machen:

* **SetForegroundWindow(hwnd)** – macht das Fenster zum aktiven Fenster.
* **SetActiveWindow(hwnd)** – aktiviert das Fenster, garantiert aber nicht, dass es im Vordergrund bleibt.
* **BringWindowToTop(hwnd)** – bringt es über andere Fenster.
* **ShowWindow(hwnd, flag)** – zeigt/versteckt/minimiert/maximiert das Fenster, abhängig vom `flag` (wie `SW_SHOW`, `SW_MINIMIZE`, `SW_RESTORE`).

---

## 4. "Unterer Bereich" (Z-Reihenfolge & Platzierung)

Fenster sind in einer Z-Reihenfolge geschichtet:

* **Topmost** – immer über anderen (`SetWindowPos` mit `HWND_TOPMOST`).
* **Bottom** – kann ein Fenster hinter alle anderen schieben, indem `SetWindowPos(hwnd, win32con.HWND_BOTTOM, …)` verwendet wird.
* **NoActivate** – Sie können ein Fenster anzeigen oder positionieren, ohne es zu aktivieren (mit Flags wie `SWP_NOACTIVATE`).

Dies ist oft nützlich, wenn Sie möchten, dass ein Hintergrund-Dienstprogrammfenster geöffnet bleibt, aber nicht den Fokus stiehlt.

---

## 5. Typische Funktionen, die Sie verwenden werden

Hier sind einige wichtige PyWin32-Funktionen mit Beispielen:

```python
import win32gui
import win32con

# Fenster anhand des Titels finden
hwnd = win32gui.FindWindow(None, "Unbenannt - Editor")

# Eigenschaften abrufen
title = win32gui.GetWindowText(hwnd)
rect = win32gui.GetWindowRect(hwnd)  # (links, oben, rechts, unten)

# Fenster aktivieren
win32gui.SetForegroundWindow(hwnd)

# Nach hinten verschieben (hinter andere)
win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# Anzeigen/wiederherstellen
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
```

---

## 6. Ereignis-/Nachrichtenbehandlung

Sie können auch in Fensterereignisse (Aktivierung, Größenänderung, Schließen) einhaken, indem Sie verwenden:

* `SetWindowLong` zum Unterklassen.
* `SendMessage` / `PostMessage` zum Simulieren von Aktionen.
* Nachrichten wie `WM_ACTIVATE`, `WM_SIZE` usw.

---

✅ Zusammenfassend:

* **Eigenschaften**: Titel, Klasse, Größe, Stil, Sichtbarkeit, Aktivierungszustand.
* **Aktivierung**: verwenden Sie `SetForegroundWindow`, `BringWindowToTop`.
* **Unterer Bereich**: Verwalten Sie die Z-Reihenfolge mit `SetWindowPos` und `HWND_BOTTOM`.

Möchten Sie, dass ich auch ein **praktisches Skript** hinzufüge, das alle Top-Level-Fenster mit ihren Eigenschaften (Titel, Position, Z-Reihenfolge) auflistet und es Ihnen ermöglicht, diese interaktiv zu aktivieren oder nach hinten zu senden?