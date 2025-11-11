---
audio: false
generated: true
lang: de
layout: post
title: Tasten in Ubuntu 24.04 neu belegen
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Sie die linke Strg- und die Feststelltaste in Ubuntu 24.04 mit GNOME Tweaks, einem grafischen Tool, oder über die Befehlszeile mit `gsettings` vertauschen können.
- Recherchen deuten darauf hin, dass beide Methoden sitzungsübergreifend bestehen bleiben und sie somit für den täglichen Gebrauch zuverlässig sind.
- Die Beweislage tendiert dahin, dass GNOME Tweaks benutzerfreundlich ist, während die Befehlszeilenmethode mehr Kontrolle für fortgeschrittene Benutzer bietet.

#### Verwendung von GNOME Tweaks
GNOME Tweaks bietet eine einfache Oberfläche zum Vertauschen der Tasten:
- Installieren Sie es bei Bedarf mit `sudo apt install gnome-tweak-tool`.
- Öffnen Sie Tweaks, gehen Sie zu "Tastatur & Maus", klicken Sie auf "Zusätzliche Tastaturoptionen" und wählen Sie unter "Strg-Position" die Option "Strg und Feststelltaste vertauschen".

#### Verwendung der Befehlszeile
Für einen technischen Ansatz verwenden Sie das Terminal:
- Führen Sie `gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swapcaps']"` aus, um die Tasten dauerhaft zu vertauschen.

#### Unerwartetes Detail
Anders als bei Windows PowerToys, das eine fein abgestimmte Neubelegung von Tasten erlaubt, tauschen die Methoden in Ubuntu primär die linke Strg-Taste mit der Feststelltaste aus, was möglicherweise andere Tastenkombinationen beeinflusst, auf die Sie angewiesen sind.

---

### Umfragenotiz: Detaillierte Analyse zum Tastentausch in Ubuntu 24.04

Dieser Abschnitt bietet eine umfassende Untersuchung zum Vertauschen der linken Strg- und der Feststelltaste in Ubuntu 24.04, ähnlich der Funktionalität, die PowerToys unter Windows bietet. Die Analyse stützt sich auf verschiedene Quellen, um Genauigkeit und Tiefe zu gewährleisten und richtet sich sowohl an anfängerfreundliche als auch an fortgeschrittene Lösungen suchende Benutzer.

#### Hintergrund und Kontext
Ubuntu 24.04, Codename "Noble Numbat", ist ein Long Term Support (LTS) Release, das weiterhin die GNOME Desktop-Umgebung, speziell Version 46, verwendet. Benutzer, die mit Windows vertraut sind, erwarten möglicherweise ähnliche Anpassungsmöglichkeiten, wie sie etwa von PowerToys bereitgestellt werden, die das Vertauschen spezifischer Tasten wie der linken Strg- und der Feststelltaste erlauben. Unter Linux wird die Tastaturanpassung typischerweise durch Tools wie GNOME Tweaks oder Befehlszeilenprogramme verwaltet, die Flexibilität bieten, aber im Vergleich zu Windows unterschiedliche Ansätze erfordern.

Die Anfrage des Benutzers, die linke Strg- und die Feststelltaste zu vertauschen, ist unter Entwicklern und Power-Usern üblich, insbesondere bei denen, die an Emacs- oder Vim-Workflows gewöhnt sind, bei denen Strg häufig verwendet wird. Diese Analyse untersucht sowohl grafische als auch Befehlszeilenmethoden, um Persistenz über Sitzungen hinweg und Kompatibilität mit Ubuntu 24.04 sicherzustellen.

#### Methoden zum Vertauschen der Tasten

##### Methode 1: Verwendung von GNOME Tweaks
GNOME Tweaks ist ein grafisches Tool, das die Anpassung des Desktops, einschließlich Tastatureinstellungen, vereinfacht. Basierend auf verfügbarer Dokumentation unterstützt es das Vertauschen von Tasten über seine Oberfläche. Die Schritte sind wie folgt:

1.  **Installation:** Falls nicht bereits installiert, können Benutzer GNOME Tweaks über das Ubuntu Software Center oder durch Ausführen des Befehls installieren:
    ```bash
    sudo apt install gnome-tweak-tool
    ```
    Dies stellt sicher, dass das Tool verfügbar ist, und es ist Teil der Standard-Repositories für Ubuntu 24.04.

2.  **Zugriff auf Tastatureinstellungen:** Öffnen Sie GNOME Tweaks über das Anwendungsmenü oder indem Sie "Tweaks" in der Aktivitätenübersicht suchen. Navigieren Sie im linken Menü zum Abschnitt "Tastatur & Maus".

3.  **Zusätzliche Tastaturoptionen:** Klicken Sie auf "Zusätzliche Tastaturoptionen", um auf erweiterte Tastatureinstellungen zuzugreifen. Suchen Sie in diesem Menü den Abschnitt "Strg-Position", von dem erwartet wird, dass er eine Option namens "Strg und Feststelltaste vertauschen" enthält. Wählen Sie diese Option aus, um die linke Strg-Taste mit der Feststelltaste zu vertauschen.

4.  **Persistenz:** Änderungen, die über GNOME Tweaks vorgenommen werden, sind typischerweise über Neustarts hinweg persistent, da sie die in der `dconf`-Datenbank gespeicherten GNOME-Einstellungen modifizieren, die benutzerspezifisch sind und beim Login angewendet werden.

Diese Methode ist benutzerfreundlich, besonders für diejenigen, die mit Befehlszeilentools nicht vertraut sind, und entspricht den Erwartungen von Windows-Benutzern an eine grafische Oberfläche. Sie beruht jedoch auf der Annahme, dass die Option "Strg und Feststelltaste vertauschen" in GNOME Tweaks für Ubuntu 24.04 verfügbar ist, basierend auf historischer Dokumentation aus Quellen wie [Ask Ubuntu: How do I remap the Caps Lock and Ctrl keys?](https://askubuntu.com/questions/33774/how-do-i-remap-the-caps-lock-and-ctrl-keys) und [Opensource.com: How to swap Ctrl and Caps Lock keys in Linux](https://opensource.com/article/18/11/how-swap-ctrl-and-caps-lock-your-keyboard), die auf Kontinuität in der Funktionalität hindeuten.

##### Methode 2: Verwendung der `gsettings` Befehlszeile
Für Benutzer, die die Kontrolle über die Befehlszeile bevorzugen oder auf Probleme mit GNOME Tweaks stoßen, bietet der `gsettings`-Befehl einen direkten Weg, Tastaturoptionen zu modifizieren. Diese Methode nutzt das GNOME-Einstellungssystem und gewährleistet Persistenz. Der Ablauf ist wie folgt:

1.  **Terminal öffnen:** Greifen Sie auf das Terminal via Strg + Alt + T oder über die Aktivitätenübersicht zu.

2.  **Tastaturoption setzen:** Führen Sie den folgenden Befehl aus, um die linke Strg- und die Feststelltaste zu vertauschen:
    ```bash
    gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swapcaps']"
    ```
    Dieser Befehl modifiziert den Schlüssel `xkb-options` unter `org.gnome.desktop.input-sources` und fügt die Option "ctrl:swapcaps" hinzu, eine Standard-XKB-Option zum Vertauschen von Strg und Feststelltaste.

3.  **Verifikation und Persistenz:** Testen Sie nach Ausführung des Befehls das Tastenverhalten durch Drücken der linken Strg- und der Feststelltaste. Die Änderungen sind sitzungsübergreifend persistent, da sie in der `dconf`-Datenbank des Benutzers gespeichert und beim Login angewendet werden.

Diese Methode ist besonders nützlich für fortgeschrittene Benutzer oder in automatisierten Setups, wie z.B. Skripten für mehrere Benutzerkonfigurationen. Sie wird durch Quellen wie [EmacsWiki: Moving The Ctrl Key](https://www.emacswiki.org/emacs/MovingTheCtrlKey) unterstützt, die XKB-Optionen und ihre Auswirkungen detailliert beschreiben.

#### Vergleich der Methoden
Um Benutzern bei der Wahl der geeigneten Methode zu helfen, vergleicht die folgende Tabelle GNOME Tweaks und `gsettings` basierend auf Benutzerfreundlichkeit, erforderlicher technischer Expertise und Persistenz:

| **Aspekt**              | **GNOME Tweaks**                     | **gsettings Befehlszeile**       |
|-------------------------|--------------------------------------|----------------------------------|
| **Benutzerfreundlichkeit** | Hoch (grafische Oberfläche)          | Mittel (Terminalkenntnisse nötig) |
| **Technische Expertise** | Niedrig (geeignet für Anfänger)      | Mittel (geeignet für Fortgeschrittene) |
| **Persistenz**          | Automatisch (in dconf gespeichert)   | Automatisch (in dconf gespeichert) |
| **Installation nötig**  | Kann Installation erfordern          | Keine zusätzliche Installation nötig |
| **Flexibilität**        | Begrenzt auf GUI-Optionen            | Hoch (kann mehrere Optionen kombinieren) |

Diese Tabelle hebt hervor, dass GNOME Tweaks ideal für Benutzer ist, die Einfachheit suchen, während `gsettings` Flexibilität für diejenigen bietet, die mit der Befehlszeile vertraut sind.

#### Überlegungen und Einschränkungen
-   **Spezifität für linke Strg:** Von beiden Methoden wird erwartet, dass sie die linke Strg-Taste mit der Feststelltaste vertauschen, da "ctrl:swapcaps" typischerweise die linke Strg-Taste in Standard-XKB-Konfigurationen betrifft. Benutzer sollten das Verhalten dennoch überprüfen, da je nach Tastaturlayout möglicherweise beide Strg-Tasten betroffen sein könnten.
-   **Auswirkung auf Tastenkombinationen:** Das Vertauschen der Tasten kann bestehende Tastenkombinationen beeinflussen, wie z.B. Strg+C zum Kopieren oder Strg+V zum Einfügen. Benutzer sollten kritische Tastenkombinationen nach der Konfiguration testen, um Kompatibilität sicherzustellen, insbesondere in Anwendungen wie Terminals oder IDEs.
-   **Mögliche Probleme:** Während keine spezifischen Berichte gefunden wurden, dass die Option "Strg und Feststelltaste vertauschen" in Ubuntu 24.04 nicht funktioniert, sollten Benutzer sich möglicher Bugs bewusst sein, wie in allgemeinen Tastaturproblemen wie [Keyboard Issue with Ubuntu 24.04: Caps Lock Reversed After Login](https://ubuntuforums.org/showthread.php?t=2497465) vermerkt. Falls Probleme auftreten, bietet die Befehlszeilenmethode einen Fallback.

#### Unerwartetes Detail: Vergleich mit Windows PowerToys
Anders als Windows PowerToys, das eine fein abgestimmte Neubelegung von Tasten bietet und spezifische Tasten wie die linke Strg ohne Beeinflussung anderer anvisieren kann, sind die Methoden in Ubuntu stärker standardisiert. Die Option "Strg und Feststelltaste vertauschen" in GNOME Tweaks oder "ctrl:swapcaps" in `gsettings` tauscht primär die linke Strg mit der Feststelltaste aus, was möglicherweise andere Tastaturverhalten beeinflusst. Dieser Unterschied könnte Benutzer überraschen, die identische Funktionalität erwarten, und unterstreicht die Notwendigkeit von Tests nach der Konfiguration.

#### Fazit
Sowohl GNOME Tweaks als auch `gsettings` bieten viable Methoden, um die linke Strg- und die Feststelltaste in Ubuntu 24.04 zu vertauschen, wobei sie Persistenz und Kompatibilität mit dem Workflow des Benutzers gewährleisten. GNOME Tweaks bietet einen grafischen, anfängerfreundlichen Ansatz, während `gsettings` fortgeschrittene Benutzer anspricht, die Kontrolle über die Befehlszeile suchen. Benutzer sollten das Verhalten nach der Konfiguration überprüfen und mögliche Auswirkungen auf Tastenkombinationen bedenken, insbesondere angesichts der Unterschiede zu Windows PowerToys.

### Wichtige Zitate
-   [How do I remap the Caps Lock and Ctrl keys Ask Ubuntu](https://askubuntu.com/questions/33774/how-do-i-remap-the-caps-lock-and-ctrl-keys)
-   [How to swap Ctrl and Caps Lock keys in Linux Opensource.com](https://opensource.com/article/18/11/how-swap-ctrl-and-caps-lock-your-keyboard)
-   [Moving The Ctrl Key EmacsWiki](https://www.emacswiki.org/emacs/MovingTheCtrlKey)
-   [Keyboard Issue with Ubuntu 24.04: Caps Lock Reversed After Login Ubuntu Forums](https://ubuntuforums.org/showthread.php?t=2497465)