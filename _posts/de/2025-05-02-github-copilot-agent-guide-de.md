---
audio: false
generated: true
image: false
lang: de
layout: post
model: deepseek/deepseek-v3.2-exp
title: GitHub Copilot Agent-Modus Anleitung
translated: true
type: note
---

Sicherlich. Hier ist eine umfassende Anleitung zum Agent Mode von GitHub Copilot, die erklärt, was es ist, wie es funktioniert, wie man es verwendet und welche Best Practices es gibt.

---

### **Umfassende Anleitung zum GitHub Copilot Agent Mode**

#### **1. Was ist der Agent Mode? Eine einfache Analogie**

Stellen Sie sich GitHub Copilot in zwei verschiedenen Modi vor:

*   **Standard Copilot (Co-pilot):** Ihr **Pair Programmer**. Er sitzt neben Ihnen und macht Vorschläge Zeile für Zeile oder Funktion für Funktion. Sie sitzen immer noch am Steuer, bestimmen die übergeordnete Richtung, Architektur und Logik. Sie nehmen seine Vorschläge an, lehnen sie ab oder bearbeiten sie, wie Sie es für richtig halten.
*   **Agent Mode (Auto-pilot):** Ihr **Lehrling-Programmierer**. Sie geben ihm eine übergeordnete Aufgabe (ein "Prompt"), und er übernimmt das Steuer. Er plant, schreibt, bearbeitet und testet Code autonom, um die Aufgabe zu erledigen, und nimmt oft mehrere Änderungen in verschiedenen Dateien vor, ohne für jeden Schritt Ihre Intervention zu benötigen.

**Im Wesentlichen ist der Agent Mode eine fortschrittliche, zielorientierte Funktion, die es Copilot ermöglicht, komplexe, mehrstufige Programmieraufgaben auf Basis einer einzigen natürlichen Sprachaufforderung auszuführen.**

---

#### **2. Wie funktioniert der Agent Mode? Die zugrunde liegende Mechanik**

Der Agent Mode ist nicht nur ein schlauerer Autovervollständiger; es ist ein Wandel in der Art und Weise, wie Copilot mit Ihrer Codebasis interagiert. Hier ist eine Aufschlüsselung des Prozesses:

**Schritt 1: Der Benutzer initiiert die Aufgabe**
Sie rufen den Agent Mode auf, typischerweise indem Sie einen Kommentar in Ihrem Code mit einem bestimmten Slash-Befehl beginnen. Der gebräuchlichste ist `/fix` für von Copilot identifizierte Probleme, aber der leistungsfähigere Befehl ist oft etwas wie `/explain` oder eine dedizierte Tastenbindung, um den Agent-Chat zu öffnen.

**Schritt 2: Aufgabenanalyse und Planung**
Der Agent fängt nicht einfach an zu tippen. Zuerst analysiert er Ihre Eingabe und Ihre Codebasis.
*   **Er liest Ihre aktuelle Datei und verwandte Dateien**, um den Kontext zu verstehen.
*   **Er formuliert einen Plan.** Intern unterteilt er Ihre übergeordnete Anfrage ("füge Benutzerauthentifizierung hinzu") in kleinere, handhabbare Teilaufgaben ("1. Prüfe auf vorhandene Auth-Bibliothek. 2. Erstelle eine `login`-Funktion. 3. Erstelle eine `verifyToken`-Middleware. 4. Aktualisiere die Hauptroute.").

**Schritt 3: Iterative Ausführung und "Denken"**
Dies ist der Kern des Agent Mode. Der Agent tritt in eine Schleife ein:
*   **Code-Generierung:** Er schreibt Code, um die erste Teilaufgabe zu erledigen.
*   **Code-Ausführung (Simulation):** Er führt den Code nicht *tatsächlich* in Ihrer Umgebung aus, sondern verwendet seine riesigen Trainingsdaten und internen Modelle, um zu *simulieren*, was der Code tun würde, und prüft auf Syntaxfehler, offensichtliche Logikfehler und Typinkongruenzen.
*   **Selbstüberprüfung und Korrektur:** Er überprüft seinen eigenen generierten Code. Wenn er "glaubt", dass etwas falsch ist, wird er diesen Teil umschreiben. Sie können diesen Prozess oft als "Denken..." oder "Planen..."-Indikator in der Benutzeroberfläche sehen.
*   **Wiederholen:** Er fährt mit der nächsten Teilaufgabe fort und verwendet dabei den Kontext des gerade geschriebenen Codes.

**Schritt 4: Präsentation und Freigabe**
Sobald der Agent seine geplante Abfolge von Aktionen abgeschlossen hat, präsentiert er Ihnen eine Zusammenfassung der Änderungen.
*   Er zeigt Ihnen einen Diff (die klassischen grünen Hinzufügungen/roten Löschungen) aller Dateien, die er geändert hat.
*   Er liefert eine Erklärung in natürlicher Sprache, was er getan hat und warum.
*   Sie haben die Möglichkeit, die Lösung **Anzunehmen**, **Abzulehnen** oder manchmal **Neu zu generieren**.

**Schlüsseltechnologien, die dies ermöglichen:**
*   **Large Language Models (LLMs):** Eine leistungsfähigere, spezialisierte Version des GPT-Modells, das Code und Planung versteht.
*   **Workspace Awareness:** Der Agent Mode hat breitere "Berechtigungen", mehrere Dateien in Ihrem Projekt zu lesen und zu analysieren, nicht nur die, an der Sie gerade arbeiten.
*   **Reasoning and Planning Architectures:** Fortschrittliche Techniken wie Chain-of-Thought (CoT) oder Tree-of-Thought (ToT), die es dem Modell ermöglichen, Probleme logisch aufzuschlüsseln.

---

#### **3. Verwendung: Wie und wann man den Agent Mode verwendet**

**Wie man ihn aktiviert:**
Die genaue Methode kann je nach IDE (VS Code, JetBrains, etc.) und Copilot-Plan (Pro, Business) variieren. Häufige Methoden sind:
*   Verwendung eines **Slash-Befehls** (z.B. `/fix`, `/tests`) in einem Kommentar.
*   Eingabe einer natürlichen Sprachaufforderung im dedizierten **Copilot Chat**-Bereich und Anweisung, als Agent zu handeln.
*   Eine spezifische Tastenbindung, um die agentische Aufgabeneingabe auszulösen.

**Ideale Anwendungsfälle für den Agent Mode:**

1.  **Komplexes Refactoring:**
    *   **Prompt:** "`/refactor Refaktoriere die `calculatePrice`-Funktion, um das Strategie-Muster zu verwenden. Erstelle separate Klassen für `RegularPricing`, `MemberPricing` und `SalePricing`."`
    *   *Warum es funktioniert:* Dies ist eine mehrstufige Aufgabe, die das Erstellen neuer Dateien/Klassen, das Ändern bestehender Funktionssignaturen und das Aktualisieren von Aufrufen der Funktion beinhaltet.

2.  **Implementieren wohldefinierter Features:**
    *   **Prompt:** "`Füge einen neuen API-Endpunkt `POST /api/v1/books` hinzu, der einen JSON-Body mit `title`, `author` und `isbn` akzeptiert, die Eingabe validiert und sie in der `books`-Tabelle der Datenbank speichert.`"
    *   *Warum es funktioniert:* Das Feature hat eine klare Struktur (REST-API, Validierung, DB-Interaktion), die der Agent zerlegen kann.

3.  **Schreiben umfassender Tests:**
    *   **Prompt:** "`/tests Generiere Unit-Tests für die `UserService`-Klasse, die alle öffentlichen Methoden und Edge Cases wie ungültige E-Mail-Formate und doppelte Benutzer abdeckt."`
    *   *Warum es funktioniert:* Der Agent kann die `UserService`-Klasse analysieren, verstehen, was jede Methode tut, und systematisch Testfälle für Erfolgs- und Fehlerpfade erstellen.

4.  **Debuggen und Beheben komplexer Probleme:**
    *   **Prompt:** "`/fix Ich erhalte eine 'NullPointerException' in Zeile 47 von `PaymentProcessor.java`, wenn die Methode `user.getProfile()` null zurückgibt.`"
    *   *Warum es funktioniert:* Der Agent kann den Codefluss verfolgen, die Grundursache identifizieren (fehlende Nullprüfungen) und eine robuste Lösung vorschlagen, möglicherweise indem er Nullsicherheit in anderen verwandten Codebereichen hinzufügt.

5.  **Generieren von Boilerplate-Code:**
    *   **Prompt:** "`Erstelle ein neues React-Komponentengerüst namens `ProductCard`, das `product`-Props (mit `name`, `imageUrl`, `price`) entgegennimmt und sie in einer Karte mit einem Button anzeigt.`"
    *   *Warum es funktioniert:* Während Standard-Copilot dies kann, kann der Agent sicherstellen, dass Konsistenz mit den vorhandenen Komponentenmustern und der Struktur Ihres Projekts gewahrt bleibt.

**Wann man den Agent Mode vermeiden (oder mit Vorsicht verwenden) sollte:**

*   **Vage oder schlecht abgegrenzte Aufgaben:** "Mache die App besser." Der Agent wird ohne ein klares, umsetzbares Ziel scheitern.
*   **Aufgaben, die tiefgehende Geschäftslogik erfordern:** "Implementiere die Quartalssteuerberechnungsregel für die EMEA-Region." Sofern diese Logik nicht in Ihrem Code dokumentiert ist, wird der Agent wahrscheinlich falsche Regeln erfinden.
*   **Architekturentscheidungen:** "Sollen wir eine Microservices- oder Monolith-Architektur verwenden?" Dies ist eine strategische Entscheidung, die menschliches Urteilsvermögen erfordert.
*   **Kritischer, sicherheitsrelevanter Code:** Nehmen Sie Code, der sich auf Authentifizierung, Verschlüsselung oder Zahlungen bezieht, niemals blind ohne eine gründliche, von Menschen durchgeführte Sicherheitsüberprüfung an.

---

#### **4. Best Practices für eine effektive Nutzung**

1.  **Schreiben Sie detaillierte, spezifische Prompts:** Die Qualität der Ausgabe ist direkt proportional zur Qualität der Eingabe. Geben Sie Kontext, Einschränkungen und das gewünschte Ergebnis an.
    *   **Schlecht:** "Füge einen Button hinzu."
    *   **Gut:** "Füge in der `UserProfile.jsx`-Komponente oben rechts einen roten 'Delete Account'-Button hinzu. Wenn er angeklickt wird, soll er die vorhandene `deleteUserAccount`-Funktion aus dem `userService` aufrufen und die aktuelle `userId` übergeben."

2.  **Überprüfen Sie alle Änderungen gewissenhaft:** **Sie sind immer noch für den Code verantwortlich.** Betrachten Sie die Ausgabe des Agents als einen ersten Entwurf. Prüfen Sie auf:
    *   Logische Fehler.
    *   Sicherheitslücken.
    *   Leistungsineffizienzen.
    *   Einhaltung der Codierungsstandards Ihres Teams.

3.  **Verwenden Sie ihn für die "ersten 80 %":** Der Agent Mode ist fantastisch, um den Großteil einer repetitiven oder gut verstandenen Aufgabe schnell zu erledigen. Erwarten Sie, die letzten 20 % selbst zu verfeinern.

4.  **Iterieren Sie über die Lösung:** Wenn das erste Ergebnis nicht perfekt ist, lehnen Sie es nicht einfach ab. Nutzen Sie den Chat, um Feedback zu geben: "Das ist gut, aber fügen Sie bitte nun dem von Ihnen erstellten API-Endpunkt eine Fehlerbehandlung hinzu."

5.  **Halten Sie Ihre Codebasis sauber:** Der Agent funktioniert besser, wenn Ihr Projekt gut strukturiert und Ihr Code sauber ist. Eine unordentliche Codebasis kann ihn verwirren und zu schlechten Ergebnissen führen.

### **Zusammenfassung: Standard Copilot vs. Agent Mode**

| Merkmal | Standard Copilot (Co-pilot) | Agent Mode (Auto-pilot) |
| :--- | :--- | :--- |
| **Rolle** | Pair Programmer | Lehrling-Programmierer |
| **Interaktion** | Zeile für Zeile, Inline-Vorschläge | Zielorientiert, Chat-gesteuerte Befehle |
| **Umfang** | Einzelne Datei, aktueller Kontext | Mehrere Dateien, gesamter Workspace |
| **Kontrolle** | Sie haben feingranulare Kontrolle über jeden Vorschlag | Sie delegieren eine Aufgabe und überprüfen das Endergebnis |
| **Am besten für** | Tägliches Programmieren, schnelle Snippets, Gedanken vervollständigen | Komplexe Features, Refactoring, Schreiben von Test-Suiten, Bugfixes |

Der Agent Mode stellt einen bedeutenden Sprung in Richtung einer autonomeren Softwareentwicklung dar. Indem Sie seine Mechanik verstehen und ihn strategisch einsetzen, können Sie mühsame und komplexe Programmieraufgaben abgeben und sich so auf höherwertiges Design, Problemlösung und Innovation konzentrieren.