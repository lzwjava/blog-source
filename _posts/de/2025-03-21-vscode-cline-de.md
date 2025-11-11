---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von Cline in VSCode
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Cline in VSCode verwendet werden kann, indem man die Erweiterung installiert, ein Konto erstellt und über natürliche Sprachbefehle interagiert.
- Recherchen deuten darauf hin, dass die Konfiguration eines API-Anbieters, wie z. B. OpenRouter, die Funktionalität verbessert und einen API-Schlüssel erfordert.
- Die Beweislage deutet stark darauf hin, dass Cline erweiterte Funktionen wie Code-Generierung und Terminalbefehle unterstützt, mit optionaler Einrichtung für bestimmte Modelle.

---

### Installation und Einrichtung

Um mit Cline in VSCode zu beginnen, stellen Sie zunächst sicher, dass VSCode von [dieser Website](https://code.visualstudio.com) installiert ist. Öffnen Sie dann VSCode, gehen Sie zur Erweiterungsansicht (klicken Sie auf das Erweiterungssymbol oder drücken Sie `Strg+Umschalt+X` unter Windows/Linux bzw. `Befehl+Umschalt+X` unter macOS), suchen Sie nach "Cline" und klicken Sie auf "Installieren". Klicken Sie nach der Installation auf das Cline-Symbol in der Aktivitätsleiste oder verwenden Sie die Befehlspalette (`Strg+Umschalt+P` oder `Befehl+Umschalt+P`), um Cline zu öffnen. Melden Sie sich dann an, indem Sie ein Konto auf [app.cline.bot](https://app.cline.bot) erstellen, das mit kostenlosen Guthaben startet und keine Kreditkarte benötigt.

### Verwendung von Cline

Sobald eingerichtet, interagieren Sie mit Cline, indem Sie natürliche Sprachbefehle in das Chat-Fenster eingeben, wie z. B. "Generiere eine Funktion, um ein Array zu sortieren" oder "Erstelle einen neuen Projektordner namens 'hello-world' mit einer einfachen Webseite, die 'Hello World' in großem, blauem Text anzeigt". Cline kann Code generieren, erklären, Fehler debuggen und sogar Terminalbefehle mit Ihrer Erlaubnis ausführen, z. B. das Installieren von Paketen. Überprüfen Sie alle Änderungen, bevor Sie sie anwenden, da KI-Vorschläge gelegentlich fehlerhaft sein können.

### Konfiguration des API-Anbieters

Für erweiterte Funktionalität können Sie einen API-Anbieter wie OpenRouter konfigurieren. Besorgen Sie sich einen API-Schlüssel von [OpenRouter.ai](https://openrouter.ai), geben Sie dann in den Cline-Einstellungen die Basis-URL (z. B. `https://openrouter.ai/api/v1`) und die Modell-ID (z. B. `deepseek/deepseek-chat`) ein und fügen Sie Ihren API-Schlüssel ein. Dies ermöglicht den Zugriff auf bestimmte Modelle, was die Leistung potenziell verbessert, aber es ist optional, da Cline standardmäßig mit voreingestellten Modellen funktioniert.

---

---

### Umfragehinweis: Umfassende Anleitung zur Verwendung von Cline in VSCode

Dieser Abschnitt bietet eine detaillierte Untersuchung der Verwendung von Cline, einem KI-gestützten Programmierassistenten, innerhalb von Visual Studio Code (VSCode). Er erweitert die direkte Antwort durch eine gründliche Überprüfung von Installation, Einrichtung, Verwendung und erweiterten Konfigurationen. Die Analyse basiert auf aktuellen webbasierten Recherchen und gewährleistet Genauigkeit und Relevanz Stand 21. März 2025.

#### Hintergrund zu Cline und VSCode-Integration

Cline ist ein quelloffener KI-Programmierassistent, der entwickelt wurde, um die Produktivität von Entwicklern durch Funktionen wie Code-Generierung, Debugging und Ausführung von Terminalbefehlen innerhalb von VSCode zu steigern. Er unterstützt mehrere KI-Modelle und kann mit verschiedenen API-Anbietern konfiguriert werden, was ihn zu einer flexiblen Alternative zu Tools wie GitHub Copilot macht. Benutzer können mit Cline über natürliche Sprachbefehle interagieren, und er passt sich projektspezifischen Bedürfnissen durch benutzerdefinierte Anweisungen und Einstellungen an.

#### Schritt-für-Schritt-Installation und -Einrichtung

Um Cline in VSCode zu verwenden, befolgen Sie diese detaillierten Schritte:

1.  **Installieren Sie VSCode**:
    *   Laden Sie VSCode von der offiziellen Website herunter und installieren Sie es: [diese Website](https://code.visualstudio.com). Stellen Sie sicher, dass Sie das Ausführen von Erweiterungen erlauben, wenn Sie beim Start dazu aufgefordert werden.

2.  **Installieren Sie die Cline-Erweiterung**:
    *   Öffnen Sie VSCode und navigieren Sie zur Erweiterungsansicht, indem Sie auf das Erweiterungssymbol in der Aktivitätsleiste klicken oder `Strg+Umschalt+X` (Windows/Linux) bzw. `Befehl+Umschalt+X` (macOS) drücken.
    *   Geben Sie in die Suchleiste "Cline" ein, um die Erweiterung zu finden.
    *   Klicken Sie auf die Schaltfläche "Installieren" neben der Cline-Erweiterung, entwickelt von saoudrizwan, verfügbar im [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev).

3.  **Öffnen Sie Ihren Cline-Ordner**:
    *   Für eine strukturierte Einrichtung öffnen Sie den "Cline"-Ordner in Ihrem Dokumentenverzeichnis:
        *   Auf macOS: `/Users/[Ihr-Benutzername]/Documents/Cline`
        *   Unter Windows: `C:\Users\\[Ihr-Benutzername]\Documents\Cline`
    *   Dieser Schritt wird zur Projektorganisation empfohlen, ist aber für die grundlegende Nutzung optional.

4.  **Erstellen Sie ein Cline-Konto und melden Sie sich an**:
    *   Klicken Sie nach der Installation auf das Cline-Symbol in der Aktivitätsleiste, um die Erweiterung zu öffnen, oder verwenden Sie die Befehlspalette (`Strg+Umschalt+P` oder `Befehl+Umschalt+P`) und geben Sie "Cline: Open In New Tab" für eine bessere Ansicht ein.
    *   Klicken Sie in der Cline-Oberfläche auf "Sign In", was Sie zu [app.cline.bot](https://app.cline.bot) weiterleitet, um ein Konto zu erstellen. Dieser Prozess beginnt mit kostenlosen Guthaben, und es wird keine Kreditkarte benötigt, was es für neue Benutzer zugänglich macht.

#### Konfiguration von API-Anbietern für erweiterte Funktionalität

Cline unterstützt eine breite Palette von API-Anbietern, um verschiedene KI-Modelle zu nutzen, die für verbesserte Leistung und Zugriff auf bestimmte Modelle konfiguriert werden können. Der Konfigurationsprozess ist optional, wird aber für Benutzer empfohlen, die erweiterte Funktionen suchen. So richten Sie es ein:

*   **Unterstützte API-Anbieter**: Cline integriert sich mit Anbietern wie OpenRouter, Anthropic, OpenAI, Google Gemini, AWS Bedrock, Azure und GCP Vertex sowie mit jeder OpenAI-kompatiblen API oder lokalen Modellen über LM Studio/Ollama.
*   **Konfigurationsschritte**:
    *   Öffnen Sie die Cline-Erweiterung in VSCode und greifen Sie auf die Einstellungen zu, normalerweise über ein Zahnradsymbol oder über das Einstellungsmenü von VSCode.
    *   Wählen Sie Ihren bevorzugten API-Anbieter. Um beispielsweise OpenRouter zu verwenden:
        *   Besorgen Sie sich einen API-Schlüssel von [OpenRouter.ai](https://openrouter.ai) und aktivieren Sie Ausgabelimits zur Kostenkontrolle.
        *   Geben Sie die Basis-URL ein: `https://openrouter.ai/api/v1`.
        *   Geben Sie die Modell-ID an, z. B. `deepseek/deepseek-chat` für DeepSeek Chat.
        *   Fügen Sie den API-Schlüssel in das dafür vorgesehene Feld ein und speichern Sie die Einstellungen.
    *   Für lokale Setups, z. B. die Verwendung von Ollama:
        *   Installieren Sie Ollama von [ollama.com](https://ollama.com).
        *   Laden Sie das gewünschte Modell herunter, z. B. `ollama pull deepseek-r1:14b`, und konfigurieren Sie Cline mit der Basis-URL `http://localhost:11434` und der entsprechenden Modell-ID.

*   **Leistungsüberlegungen**: Die Wahl des Modells beeinflusst die Leistung in Abhängigkeit von der Hardware. Die folgende Tabelle skizziert die Hardwareanforderungen für verschiedene Modellgrößen:

| **Modellgröße** | **Benötigter RAM** | **Empfohlene GPU**      |
|-----------------|--------------------|-------------------------|
| 1,5B           | 4 GB               | Integriert              |
| 7B             | 8–10 GB            | NVIDIA GTX 1660         |
| 14B            | 16 GB+             | RTX 3060/3080           |
| 70B            | 40 GB+             | RTX 4090/A100           |

*   **Kostenüberlegungen**: Für cloudbasierte Anbieter wie OpenRouter belaufen sich die Kosten auf etwa 0,01 US-Dollar pro einer Million Eingabe-Tokens. Detaillierte Preise finden Sie unter [OpenRouter pricing](https://openrouter.ai/pricing). Lokale Setups mit Ollama sind kostenlos, erfordern jedoch ausreichende Hardware.

#### Verwendung von Cline für Programmierunterstützung

Sobald installiert und konfiguriert, bietet Cline eine Reihe von Funktionen zur Unterstützung bei Programmieraufgaben. So verwenden Sie es effektiv:

*   **Interaktion mit Cline**:
    *   Öffnen Sie das Cline-Chat-Fenster, indem Sie auf das Cline-Symbol in der Aktivitätsleiste klicken oder die Befehlspalette verwenden, um es in einem neuen Tab zu öffnen.
    *   Geben Sie natürliche Sprachbefehle ein, um Unterstützung anzufordern. Beispiele sind:
        *   "Generiere eine Funktion, um ein Array zu sortieren."
        *   "Erkläre diesen Code-Ausschnitt."
        *   "Erstelle einen neuen Projektordner namens 'hello-world' und erstelle eine einfache Webseite, die 'Hello World' in großem, blauem Text anzeigt."
    *   Geben Sie bei komplexen Aufgaben Kontext an, wie Projektziele oder spezifische Aktionen, um genauere Antworten zu erhalten.

*   **Erweiterte Funktionen**:
    *   **Code-Generierung und -Bearbeitung**: Cline kann Code generieren und Dateien bearbeiten. Verwenden Sie Befehle wie "Please edit /path/to/file.js" oder "@dateiname", um Dateien anzugeben. Es zeigt Änderungen in einer Diff-Ansicht zur Überprüfung an, bevor sie angewendet werden, und gewährleistet so die Kontrolle über Änderungen.
    *   **Ausführung von Terminalbefehlen**: Cline kann Terminalbefehle mit Benutzererlaubnis ausführen, z. B. das Installieren von Paketen oder das Ausführen von Build-Skripts. Sie können beispielsweise fragen: "Installiere die neueste Version von Node.js", und Cline wird vor dem Fortfahren bestätigen.
    *   **Benutzerdefinierte Anweisungen**: Legen Sie benutzerdefinierte Anweisungen in den Cline-Einstellungen fest, um sein Verhalten zu steuern, z. B. die Durchsetzung von Coding-Standards, die Definition von Fehlerbehandlungspräferenzen oder die Festlegung von Dokumentationspraktiken. Diese können projektspezifisch sein und in einer `.clinerules`-Datei im Projektstammverzeichnis gespeichert werden.

*   **Änderungen überprüfen und anwenden**: Überprüfen Sie immer KI-generierten Code, bevor Sie ihn anwenden, da er gelegentlich plausibel, aber falsch sein kann. Cline's Checkpoint-System ermöglicht es Ihnen, Änderungen bei Bedarf rückgängig zu machen und so einen kontrollierten Fortschritt zu gewährleisten.

#### Zusätzliche Tipps und Best Practices

Um den Nutzen von Cline zu maximieren, beachten Sie Folgendes:

*   **Fragen stellen**: Wenn Sie unsicher sind, geben Sie Ihre Frage direkt in den Cline-Chat ein. Zum Beispiel: "Wie behebe ich diesen Fehler?" Geben Sie zusätzlichen Kontext, wie Screenshots oder kopierte Fehlermeldungen, für eine bessere Unterstützung an.
*   **Nutzungslimits und Transparenz**: Cline verfolgt die gesamten Token und API-Nutzungskosten für den gesamten Aufgabenzyklus und einzelne Anfragen und hält Sie so über die Ausgaben informiert, was besonders für cloudbasierte Anbieter nützlich ist.
*   **Community-Support**: Für weitere Unterstützung treten Sie der Cline-Discord-Community unter [diesem Link](https://discord.gg/cline) bei, wo Sie Troubleshooting-Guides finden und sich mit anderen Benutzern vernetzen können.
*   **Modellauswahl**: Wählen Sie Modelle basierend auf Ihren Bedürfnissen, mit Optionen wie Anthropic Claude 3.5-Sonnet, DeepSeek Chat und Google Gemini 2.0 Flash, die jeweils unterschiedliche Stärken für Programmieraufgaben bieten.

#### Unerwartetes Detail: Flexibilität bei der Modellbereitstellung

Ein interessanter Aspekt von Cline ist seine Flexibilität bei der Unterstützung sowohl cloudbasierter als auch lokaler Modellbereitstellungen. Während die meisten Benutzer erwarten könnten, dass cloudbasierte KI-Assistenten dominieren, ermöglicht Clines Integration lokaler Setups über Ollama kostenlose, datenschutzorientierte Programmierunterstützung, vorausgesetzt, Sie verfügen über ausreichende Hardware. Dieser duale Ansatz spricht unterschiedliche Benutzerbedürfnisse an, von budgetbewussten Entwicklern bis hin zu denen, die Datensicherheit priorisieren, und ist besonders für Open-Source-Enthusiasten relevant.

#### Fazit

Zusammenfassend lässt sich sagen, dass die Verwendung von Cline in VSCode die Installation der Erweiterung, die Erstellung eines Kontos und die Interaktion über natürliche Sprachbefehle zur Programmierunterstützung umfasst. Die Konfiguration eines API-Anbieters, wie z. B. OpenRouter, verbessert die Funktionalität durch den Zugriff auf bestimmte Modelle, mit optionalen lokalen Setups über Ollama zur Kosteneinsparung. Clines erweiterte Funktionen, wie Code-Generierung, Ausführung von Terminalbefehlen und benutzerdefinierte Anweisungen, machen ihn zu einem leistungsstarken Tool für Entwickler, wobei eine sorgfältige Überprüfung der KI-generierten Ausgaben empfohlen wird. Stand 21. März 2025 bietet dieser Leitfaden einen umfassenden Ansatz zur Nutzung von Cline für eine gesteigerte Programmierproduktivität.

---

### Wichtige Zitate

-   [Cline Offizielle Website Getting Started for New Coders](https://docs.cline.bot/getting-started/getting-started-new-coders)
-   [Cline AI Autonomous Coding Agent for VS Code](https://cline.bot/)
-   [Cline GitHub Repository](https://github.com/cline/cline)
-   [How to Use DeepSeek R1 in Visual Studio Code with Cline](https://apidog.com/blog/free-deepseek-r1-vscode-cline/)
-   [VSCode Marketplace Cline Extension](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)
-   [Cline Discord Community](https://discord.gg/cline)
-   [OpenRouter AI Platform](https://openrouter.ai)
-   [Ollama Official Website](https://ollama.com)
-   [OpenRouter AI Pricing](https://openrouter.ai/pricing)