---
audio: false
generated: true
image: false
lang: de
layout: post
title: Markdown zu Folien leicht gemacht
translated: true
type: note
---

Marp CLI ermöglicht es Ihnen, Markdown-Dateien in Folien (HTML, PDF, PPTX) umzuwandeln. Es ist besonders nützlich, wenn Sie Präsentationen in reinem Markdown mit minimalem Formatierungsaufwand schreiben möchten.

Hier ist eine Schritt-für-Schritt-Anleitung:

---

### 1. Marp CLI installieren

Sie benötigen zuerst Node.js.

```bash
npm install -g @marp-team/marp-cli
```

Installation überprüfen:

```bash
marp --version
```

---

### 2. Eine Markdown-Präsentation schreiben

Erstellen Sie eine Datei, zum Beispiel `slides.md`.

```markdown
---
marp: true
theme: default
paginate: true
---

# Hallo, Marp!

---

## Folie 2

- Aufzählungspunkt 1
- Aufzählungspunkt 2
```

Wichtige Punkte:

* `---` (YAML-Frontmatter) aktiviert Marp und die Konfiguration.
* `---` (zwischen Inhalten) trennt Folien.

---

### 3. Vorschau im Browser

Starten Sie einen lokalen Server mit Auto-Reload:

```bash
marp -p slides.md
```

Öffnen Sie [http://localhost:8080](http://localhost:8080) in Ihrem Browser.

---

### 4. Folien exportieren

Generieren Sie verschiedene Formate:

* HTML (selbstständig):

  ```bash
  marp slides.md -o slides.html
  ```

* PDF:

  ```bash
  marp slides.md -o slides.pdf
  ```

* PowerPoint (PPTX):

  ```bash
  marp slides.md -o slides.pptx
  ```

---

### 5. Nützliche Optionen

* **Auf Änderungen überwachen** (automatischer Neuaufbau):

  ```bash
  marp -w slides.md
  ```

* **Theme festlegen** (default, gaia, uncover oder Ihre benutzerdefinierte CSS-Datei):

  ```bash
  marp --theme-set ./my-theme.css slides.md -o slides.html
  ```

* **Sprechernotizen einfügen**:

  ```markdown
  ---
  marp: true
  ---

  # Titel

  <!--
  Das sind Sprechernotizen
  -->
  ```

---

### 6. Editor-Integration

* VSCode hat eine [Marp-Erweiterung](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode).
* Sie zeigt Live-Vorschauen während der Bearbeitung von Markdown an.

---

👉 Mit diesem Setup können Sie in wenigen Minuten von einer einfachen `.md`-Datei zu einer ausgefeilten Präsentation gelangen.

Möchten Sie, dass ich Ihnen eine **einsatzbereite Markdown-Vorlagendatei** (mit Titelfolie, Agenda, Inhalt und Schlussfolie) gebe, damit Sie sofort loslegen können?