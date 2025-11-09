---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Übersicht der Copilot Enterprise Modelloptionen
translated: true
type: note
---

Sie fragen nach dem Modell, das für **Copilot Enterprise** verwendet wird, insbesondere ob es sich um GPT-4.1, GPT-4o oder etwas anderes handelt. Hier ist der aktuelle und relevante Stand von **September 2025**:

---

### Welche Modelle sind für Copilot Enterprise verfügbar?

#### GitHub Copilot Enterprise & Copilot Chat

* **Standardmäßig** läuft GitHub Copilot Enterprise (und Copilot Chat) **auf GPT-4o**, was schnellere Antworten und verbesserte Qualität bietet. ([Reddit][1])
* Seit neuerem ist **GPT-4.1** verfügbar – Administratoren müssen es jedoch explizit **über eine Richtlinie in den Copilot-Einstellungen aktivieren**. Sobald es aktiviert ist, können Benutzer GPT-4.1 im Modellauswahlmenü sowohl in VS Code als auch auf github.com auswählen. ([The GitHub Blog][2])

#### Visual Studio Copilot

* Seit **Juni 2025** verwendet der Copilot in Visual Studio **standardmäßig GPT-4.1** anstelle von GPT-4o. Tests von Microsoft zeigten, dass GPT-4.1 **schnellere Antworten, höhere Qualität der Vorschläge und größere Effizienz** liefert. ([Visual Studio Magazine][3], [Microsoft Learn][4])

#### Microsoft 365 Copilot (Office-Produktivitätstools)

* Microsoft hat begonnen, **GPT-5** in das größere Copilot-Ökosystem zu integrieren – einschließlich Microsoft 365 Copilot, GitHub Copilot, Copilot Studio und mehr – über einen neuen "**Smart Mode**", der Aufgaben automatisch basierend auf dem Bedarf dem geeignetsten Modell zuweist, was die Argumentationsfähigkeit, Kontexttreue und Interaktionsqualität verbessert. ([The Verge][5])
* Zusätzlich kündigte Microsoft die Integration von Anthropics **Claude Sonnet 4** für erweiterte Aufgaben wie Präsentationsdesign und Tabellenkalkulationsautomatisierung an, während für andere Funktionen weiterhin **GPT-5** (neben verbleibenden GPT-basierten Routen) verwendet wird. ([New York Post][6])

---

### Zusammenfassung — Welches Modell ist das richtige für **Copilot Enterprise**?

* **GitHub Copilot Enterprise / Copilot Chat**:

  * Standard: **GPT-4o**
  * Optional: **GPT-4.1** (wenn vom Admin aktiviert)
* **Visual Studio Copilot**: Standard ist jetzt **GPT-4.1**
* **Microsoft 365 Copilot**: Nutzt **GPT-5 Smart Mode** mit leistungsstärkerer Routing-Funktionalität und Fähigkeiten – und integriert zudem **Claude Sonnet 4** für ausgewählte Unternehmensaufgaben.

---

### Kurzübersicht (ohne breite Tabellen, wie von Ihnen gewünscht):

* **GPT-4o**: Standard in GitHub Copilot Enterprise; bekannt für Geschwindigkeit und Qualität im Enterprise-Chat.
* **GPT-4.1**: Leistungsstärkerer Nachfolger – besser bei Code, Befolgung von Anweisungen und langen Kontexten. Verfügbar in GitHub Copilot, wenn aktiviert, und jetzt Standard in Visual Studio Copilot. ([OpenAI][7])
* **GPT-5**: Neuestes Modell, integriert in M365 Copilot via Smart Mode über alle Copilot-Plattformen hinweg für intelligentere Modellauswahl. ([The Verge][5])
* **Claude Sonnet 4**: Wurde hauptsächlich für Office-Aufgaben wie PowerPoint- und Excel-Automatisierung hinzugefügt, ergänzend zu GPT-5. ([New York Post][6])

---

### Was können Sie als Nächstes tun?

* Wenn Sie **Administrator** für GitHub Copilot Enterprise sind, prüfen Sie Ihre Einstellungen, um **GPT-4.1 zu aktivieren**, falls Ihre Benutzer von dessen Leistungsverbesserungen profitieren sollen.
* Wenn Sie **Visual Studio Copilot** verwenden, nutzen Sie bereits standardmäßig **GPT-4.1**.
* Für **Microsoft 365 Copilot** profitieren Sie vom Rollout des **GPT-5 Smart Mode** und den **Claude Sonnet 4**-Integrationen. Es ist keine Aktion erforderlich – dies ist bereits Teil der Service-Ebenen.

Lassen Sie mich wissen, wenn Sie Hilfe bei der Konfiguration dieser Einstellungen oder bei der Navigation durch die Modelloptionen in der spezifischen Umgebung Ihres Unternehmens benötigen!

[1]: https://www.reddit.com/r/GithubCopilot/comments/1dx2iq1/github_copilot_enterprise_on_gpt4o/?utm_source=chatgpt.com "GitHub Copilot Enterprise on GPT-4o : r/GithubCopilot"
[2]: https://github.blog/changelog/2025-04-14-openai-gpt-4-1-now-available-in-public-preview-for-github-copilot-and-github-models/?utm_source=chatgpt.com "OpenAI GPT-4.1 now available in public preview for GitHub ..."
[3]: https://visualstudiomagazine.com/articles/2025/06/26/new-default-model-for-visual-studio-copilot-so-how-do-you-choose.aspx?utm_source=chatgpt.com "New Default Model for Visual Studio Copilot, So How Do ..."
[4]: https://learn.microsoft.com/en-us/visualstudio/ide/copilot-select-add-models?view=vs-2022&utm_source=chatgpt.com "Using AI models in Copilot Chat - Visual Studio (Windows)"
[5]: https://www.theverge.com/news/753984/microsoft-copilot-gpt-5-model-update?utm_source=chatgpt.com "Microsoft brings GPT-5 to Copilot with new smart mode"
[6]: https://nypost.com/2025/09/10/business/microsoft-to-add-anthropic-ai-models-as-rift-with-openai-grows-report/?utm_source=chatgpt.com "Microsoft to add Anthropic AI models - as rift with OpenAI grows: report"
[7]: https://openai.com/index/gpt-4-1/?utm_source=chatgpt.com "Introducing GPT-4.1 in the API"