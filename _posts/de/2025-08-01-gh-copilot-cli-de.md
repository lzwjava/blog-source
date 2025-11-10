---
audio: false
generated: true
image: false
lang: de
layout: post
title: GitHub Copilot CLI-Integration
translated: true
type: note
---

Sie können GitHub Copilot nicht direkt als Plugin von der Befehlszeile aus mit einer Syntax wie `code --plugin copilot "hi"` aufrufen, um eine Antwort zu erhalten. Allerdings bietet GitHub Copilot eine Integration in die Befehlszeile über die GitHub CLI mit der `gh copilot`-Erweiterung, die eine chat-ähnliche Oberfläche für Befehlsvorschläge und Erklärungen bereitstellt. Dies ist nicht genau dasselbe wie ein generisches Plugin, das über den `code`-Befehl aufgerufen wird, erfüllt aber einen ähnlichen Zweck für Befehlszeileninteraktionen.

### Details zu GitHub Copilot in der CLI
- **Voraussetzungen**: Sie benötigen ein GitHub Copilot-Abonnement, die installierte GitHub CLI (`gh`) und die installierte `gh-copilot`-Erweiterung. Anweisungen zur Einrichtung finden Sie im GitHub CLI-Repository oder in der Dokumentation [GitHub CLI Installation](https://cli.github.com/) und [Installation von GitHub Copilot in der CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).
- **Verwendung**: Nach der Einrichtung können Sie Befehle wie folgt verwenden:
  - `gh copilot suggest -t shell "hi"`, um einen Shell-Befehlsvorschlag zu erhalten.
  - `gh copilot explain "hi"`, um eine Erklärung eines Befehls zu erhalten.
  - Beispiel: Die Ausführung von `gh copilot suggest -t shell "say hello"` könnte `echo "hello"` oder einen Text-zu-Sprache-Befehl wie `say "hello"` auf macOS vorschlagen, abhängig vom Kontext.
- **Einschränkungen**: Die CLI-Oberfläche ist für befehlzeilenbezogene Aufgaben konzipiert (z.B. Shell-, Git- oder GitHub CLI-Befehle) und unterstützt keine generischen Konversationsantworten wie ein Chatbot. Sie unterstützt außerdem nur englische Eingabeaufforderungen [Verantwortungsvolle Nutzung von GitHub Copilot in der CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use/copilot-in-the-cli)[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)
- **Interaktiver Modus**: Nach Ausführung eines `suggest`-Befehls startet Copilot eine interaktive Sitzung, in der Sie den Vorschlag verfeinern, ihn ausführen (kopiert in die Zwischenablage) oder bewerten können. Für eine automatische Ausführung müssen Sie den Alias `ghcs` einrichten [Verwendung von GitHub Copilot in der Befehlszeile](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).[](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)[](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

### Warum `code --plugin copilot "hi"` nicht funktioniert
- **Visual Studio Code CLI**: Der `code`-Befehl (für VS Code) unterstützt Optionen wie `--install-extension` zum Installieren von Erweiterungen, hat aber kein `--plugin`-Flag, um Erweiterungen direkt mit einer Eingabe wie `"hi"` aufzurufen. Erweiterungen wie GitHub Copilot operieren typischerweise innerhalb des VS Code-Editors, bieten Inline-Vorschläge oder Chat-Oberflächen und nicht als eigenständige CLI-Tools [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview).[](https://code.visualstudio.com/docs/copilot/overview)
- **Copilots Architektur**: Das GitHub Copilot-Plugin für VS Code kommuniziert mit einem Language Server und dem GitHub-Backend für Code-Vervollständigungen und Chat. Es gibt keinen öffentlichen API- oder CLI-Mechanismus, um beliebige Zeichenketten wie `"hi"` direkt von der Befehlszeile an das Plugin zu übergeben und eine Antwort zu erhalten [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- **Alternative für generische Eingaben**: Wenn Sie eine Eingabeaufforderung wie `"hi"` an Copilot senden und eine Antwort erhalten möchten, müssten Sie Copilot Chat innerhalb von VS Code oder einer anderen unterstützten IDE verwenden oder andere AI-CLI-Tools erkunden, die konversationelle Eingabeaufforderungen unterstützen (z.B. Microsofts AI Shell für Azure CLI) [Verwenden von Microsoft Copilot in Azure mit AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)

### Workaround für Ihr Ziel
Wenn Ihr Ziel ist, einen AI-Assistenten wie Copilot von der Befehlszeile aus mit einer Eingabeaufforderung wie `"hi"` aufzurufen und eine Antwort zu erhalten, können Sie:
1. **`gh copilot` für Befehlszeilenaufgaben verwenden**:
   - Installieren Sie GitHub CLI und die Copilot-Erweiterung.
   - Führen Sie `gh copilot suggest -t shell "greet with hi"` aus, um einen Befehl wie `echo "hi"` zu erhalten.
   - Dies ist auf Befehlszeilenkontexte beschränkt, daher könnte `"hi"` allein keine sinnvolle Antwort liefern, es sei denn, es wird als Befehlsanfrage formuliert.
2. **VS Codes Copilot Chat verwenden**:
   - Öffnen Sie VS Code, verwenden Sie die Copilot Chat-Oberfläche (zugänglich über `⌃⌘I` oder das Chat-Symbol) und geben Sie `"hi"` ein, um eine konversationelle Antwort zu erhalten.
   - Dies erfordert manuelle Interaktion innerhalb des Editors, keine CLI-Aufrufe [GitHub Copilot in VS Code Spickzettel](https://code.visualstudio.com/docs/copilot/copilot-cheat-sheet).[](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
3. **Andere AI-CLI-Tools erkunden**:
   - **AI Shell**: Microsofts AI Shell ermöglicht natürlichsprachige Eingabeaufforderungen in der CLI für Azure-bezogene Aufgaben. Sie können es installieren und Eingabeaufforderungen wie `"hi"` versuchen, obwohl es für Azure CLI- und PowerShell-Befehle optimiert ist [Verwenden von Microsoft Copilot in Azure mit AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)
   - **Benutzerdefinierte Skripte**: Sie könnten ein Skript schreiben, um mit der API eines AI-Modells zu interagieren (z.B. OpenAIs API, falls zugänglich), um Eingabeaufforderungen wie `"hi"` zu verarbeiten. Die GitHub Copilot-API ist jedoch nicht öffentlich für eine solche Nutzung verfügbar [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
4. **Plugin-Verhalten simulieren**:
   - Erstellen Sie ein Shell-Skript oder einen Alias, der Eingaben an `gh copilot suggest` oder ein anderes AI-CLI-Tool weiterleitet.
   - Beispiel:
     ```bash
     alias ai='gh copilot suggest -t shell'
     ai "greet with hi"
     ```
     Dies würde einen Befehl wie `echo "hi"` oder ähnliches vorschlagen.

### Programmgesteuerter Aufruf
Wenn Sie nach einer Möglichkeit suchen, Copilot-ähnliche Funktionalität programmgesteuert aufzurufen (wie Ihr Beispiel impliziert), beachten Sie:
- GitHub Copilot stellt keine öffentliche API für den direkten programmgesteuerten Zugriff bereit. Einige Community-Projekte haben den Language Server reverse-engineered oder Proxies verwendet, um Vorschläge abzufangen, aber diese sind komplex und riskant (z.B. potenzielle Kontosperrungen) [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- Sie könnten Open-Source-Alternativen oder andere AI-Modelle mit CLI-Integrationen erkunden (z.B. Hugging Faces CLI-Tools oder lokale LLMs wie LLaMA mit benutzerdefinierten Wrappern).

### Fazit
Während `code --plugin copilot "hi"` nicht unterstützt wird, können Sie ähnliche Funktionalität mit `gh copilot` für Befehlszeilenaufgaben oder Copilot Chat in VS Code für konversationelle Eingabeaufforderungen erreichen. Für eine generische CLI-AI-Erfahrung ziehen Sie Tools wie AI Shell oder benutzerdefinierte Skripte mit anderen AI-APIs in Betracht. Überprüfen Sie immer Vorschläge, da Copilots CLI-Antworten Fehler oder Verzerrungen aus den Trainingsdaten enthalten können [Verantwortungsvolle Nutzung von GitHub Copilot in der CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)

Wenn Sie einen spezifischen Anwendungsfall haben (z.B. konversationelle KI vs. Befehlsgenerierung), lassen Sie es mich wissen, und ich kann die Lösung weiter anpassen!