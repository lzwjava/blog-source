---
audio: false
generated: true
image: false
lang: de
layout: post
title: Methoden für reine Code-Ausgabe
translated: true
type: note
---

Verstanden – Sie möchten, dass Claude Code (und Ihre „Router“-Workflows, die es aufrufen) **ausschließlich Code** ausgibt, **ohne Inline-Kommentare, Docstrings oder Erklärungen**. Hier sind drei zuverlässige Methoden, um das durchzusetzen, von der weichsten zur strengsten. Keine Tabellen – nur klare Schritte.

---

# 1) Die Regel in `CLAUDE.md` ablegen (global oder pro Projekt)

Claude Code lädt „Memory“-Dateien automatisch und befolgt sie sitzungsübergreifend. Fügen Sie eine kurze, explizite Regel hinzu:

**Global (alle Projekte):** `~/.claude/CLAUDE.md`
**Pro Projekt (eingecheckt):** `./CLAUDE.md`

```md
# Ausgaberegeln
- Bei der Code-Generierung nur Code ausgeben.
- Füge keine Inline-Kommentare, Blockkommentare, Docstrings oder erklärende Texte ein, es sei denn, ich fordere dies ausdrücklich an.
- Halte Nachrichten prägnant; wenn eine Erklärung nötig ist, platziere sie nach dem Code-Block und nur auf ausdrückliche Aufforderung.
```

Tipp: Sie können diese Memories mit `/memory` verwalten und schnell neue hinzufügen, indem Sie eine Nachricht in Claude Code mit `#` beginnen. ([Anthropic][1])

---

# 2) Erstellen Sie einen **benutzerdefinierten Output Style**, der Kommentare verbietet (stärker)

Output Styles modifizieren den **System-Prompt** von Claude Code. Erstellen Sie einen und wechseln Sie zu ihm:

**Erstellen:**

```
/output-style:new Ich möchte einen Output Style, der immer Code ohne Kommentare oder Docstrings ausgibt, keine Erklärungen.
```

Dies erstellt eine Datei unter `~/.claude/output-styles/…`. Sie können sie bearbeiten, um sicherzustellen, dass die Regel eindeutig ist:

```md
---
name: Nur Code (Keine Kommentare)
description: Immer Code ohne Kommentare/Docstrings ausgeben; keine Erklärungen, es sei denn, es wird danach gefragt.
---
# Anweisungen
- Sie coden im "Nur-Code"-Modus.
- Fügen Sie niemals Inline-Kommentare, Blockkommentare oder Docstrings hinzu.
- Fügen Sie keinen erklärenden Text vor oder nach dem Code hinzu, es sei denn, dies wird ausdrücklich angefordert.

## Spezifisches Verhalten
- Wenn eine Aufgabe Tests impliziert, geben Sie die Testdatei(en) nur als Code aus.
- Wenn Klärungsbedarf besteht, fragen Sie kurz, ohne Erklärungen.
```

**Aktivieren:**

```
/output-style "Nur Code (Keine Kommentare)"
```

(Output Styles ändern den System-Prompt direkt; Sie können jederzeit mit `/output-style` wechseln.) ([Anthropic][2])

---

# 3) Einen zusätzlichen System-Prompt zur Laufzeit anhängen (stärkste / pro Sitzung)

Wenn Sie Claude Code über die CLI oder ein Skript starten, fügen Sie hinzu:

```bash
claude --append-system-prompt "Geben Sie immer nur Code aus. Keine Inline-Kommentare, keine Blockkommentare, keine Docstrings, keine Erklärungen, es sei denn, es wird ausdrücklich danach gefragt."
```

Sie können dies auch über `/config` setzen, wenn Sie persistente Projekteinstellungen bevorzugen. (Anthropic weist darauf hin, dass Sie `--append-system-prompt` verwenden können, um das Verhalten von Claude Code zu modifizieren.) ([Anthropic][3])

---

## Wo „router“-weite Regeln platziert werden

* Wenn Ihr „Claude Code Router“ einfach Ihre regulären Claude Code-Sitzungen über verschiedene Repositories hinweg sind, bevorzugen Sie **global memory** (`~/.claude/CLAUDE.md`) oder einen **benutzerdefinierten Output Style**, damit die Regel überall mitgenommen wird. ([Anthropic][1])
* Wenn Sie über ein Skript starten, bauen Sie das `--append-system-prompt`-Flag ein, damit jeder Lauf die Regel erbt. ([Anthropic][3])

---

## Zusätzliche Schutzmaßnahmen (optional, aber nützlich)

* Fügen Sie in der Projekt-Memory eine **„Violations“**-Zeile hinzu, damit das Modell sich selbst überprüft: „Wenn Sie im Begriff sind, Kommentare/Docstrings auszugeben, stoppen Sie und entfernen Sie diese.“
* Wenn Sie manchmal Kommentare *wollen*, fügen Sie Ihrem Prompt ein One-Shot-Override hinzu: „Dieses Mal füge kurze Kommentare hinzu.“

Das war's. Wenn Sie mir sagen, wie Sie Claude Code starten (Desktop, VS Code, JetBrains oder Terminal), kann ich Ihnen einen passenden Code-Snippet für Ihr Setup geben.

[1]: https://docs.anthropic.com/en/docs/claude-code/memory "Manage Claude's memory - Anthropic"
[2]: https://docs.anthropic.com/en/docs/claude-code/output-styles "Output styles - Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/settings "Claude Code settings - Anthropic"