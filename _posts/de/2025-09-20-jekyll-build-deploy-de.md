---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Automatisierter Jekyll-Build- und Bereitstellungs-Workflow
translated: true
type: note
---

Das kannst du komplett in GitHub Actions erledigen: Baue die Seite auf dem Runner, checke dann das Ziel-Repo in einen Unterordner aus und übertrage die Inhalte von `_site/` dorthin.

Unten findest du einen direkt einsetzbaren Workflow, den du zu deinem **Quell**-Repo hinzufügen kannst (wo deine Python-Skripte und Jekyll-Inhalte liegen):

```yaml
# .github/workflows/build-and-deploy.yml
name: Jekyll erstellen und in externes Repo bereitstellen

on:
  push:
    branches: [ main ]
  workflow_dispatch:

# Wir verwenden ein PAT für den Push ins Ziel-Repo
permissions:
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Quell-Repo auschecken
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Ruby einrichten
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: Jekyll-Abhängigkeiten installieren
        run: |
          bundle install --jobs 4 --retry 3

      - name: Python einrichten
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Python-Abhängigkeiten installieren
        if: hashFiles('requirements.txt') != ''
        run: pip install -r requirements.txt

      - name: Lokale Workflow-Pipeline ausführen (CI-Modus)
        env:
          # Füge hier alle Schlüssel hinzu, die deine Skripte benötigen
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        run: |
          # Führe genau die gleichen Schritte aus, die dein Skript orchestriert.
          # Wenn du möchtest, kannst du dein Skript direkt aufrufen:
          python scripts/workflow_local.py
          # Oder, wenn du explizite Schritte bevorzugst:
          # python scripts/generate/update_notes_link.py
          # python scripts/translation/update_lang.py --max_files 9 --model gemini-flash --commits 1000
          # python -m unittest discover -s tests/workflow
          # python scripts/release/update_release.py

      - name: Jekyll erstellen (nach _site)
        run: |
          # Falls dein Python-Modul DEFAULT_DESTINATION anderswo setzt, kannst du es hier trotzdem überschreiben.
          bundle exec jekyll build --destination _site

      - name: Ziel-Repo auschecken
        uses: actions/checkout@v4
        with:
          repository: lzwjava/lzwjava.github.io   # <-- deine DESTINATION_REPO_URL Zieladresse
          token: ${{ secrets.WORKFLOW_ACCESS_TOKEN }}      # <-- PAT mit "repo"-Bereich
          path: destination
          fetch-depth: 0

      - name: Erstellte Seite ins Ziel-Repo synchronisieren
        run: |
          mkdir -p destination/_site
          rsync -av --delete _site/ destination/_site/
          cd destination
          # Optional: Sicherstellen, dass Pages Jekyll nicht erneut verarbeitet
          touch _site/.nojekyll

          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit --amend --no-edit
            # Branch anpassen, falls dein Ziel etwas anderes verwendet (z.B. gh-pages)
            git push --force-with-lease origin HEAD:main
          else
            echo "Keine Änderungen zum Bereitstellen."
          fi

      - name: (Optional) Erstellte Seite als Artefakt hochladen
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site
```

### Was du einrichten musst

*   **PAT für den Ziel-Push**: Erstelle einen klassischen Personal Access Token mit `repo`-Bereich in deinem GitHub-Account (oder verwende einen feingranularen Token, der Schreibzugriff auf das Ziel-Repo gewährt). Speichere ihn in den Einstellungen des Quell-Repos als `WORKFLOW_ACCESS_TOKEN` (d.h. `Settings → Secrets and variables → Actions → New repository secret`).
*   **Branch- und Repo-Namen**: Setze im Schritt `Ziel-Repo auschecken` den `repository:`-Wert auf das externe Repo (es kann öffentlich oder privat sein). Im Push-Befehl setze den Branch, auf dem du bereitstellen möchtest (oft `main` oder `gh-pages`).
*   **GitHub Pages Einstellungen** (falls du aus dem Ziel-Repo bereitstellst): Wähle in den **Settings → Pages** dieses Repos den korrekten **Branch** (z.B. `main` / root) und behalte `CNAME`/Custom Domain bei, wie gewünscht.
*   **Historienerwartungen**: Der Deploy-Schritt ändert den letzten Commit und verwendet `--force-with-lease`; stelle sicher, dass dieser Branch für Deploy-Artefakte reserviert ist, sodass das Überschreiben der Historie akzeptabel ist.

### Hinweise zu deinem Python-Skript

*   Du brauchst `open_destination_repo_in_browser()` im CI nicht, es ist also in Ordnung, es unverändert zu lassen; es wird hier einfach nicht aufgerufen. Der Workflow pushed direkt vom Runner.
*   Du brauchst auch `push_destination_repo()` im CI nicht. Der Workflow übernimmt den zweiten Checkout und Push, sodass du dein Skript für lokale Läufe unverändert lassen kannst.
*   Falls dein `build_site()` in ein anderes `DEFAULT_DESTINATION` schreibt, kannst du dies trotzdem überschreiben, indem du den oben gezeigten expliziten Jekyll-Build-Schritt ausführst, der nach `_site/` schreibt. Der Deploy-Schritt synchronisiert von `_site/`.

### Privates Ziel-Repo?

*   Das ist in Ordnung. GitHub Pages bedient nur öffentliche Repos (oder öffentliche Branches in Organisationen mit aktivierten Pages), aber wenn dein Ziel lediglich darin besteht, Artefakte aus irgendeinem Grund in ein privates Repo zu pushen, funktioniert das Obige trotzdem. Wenn du Pages-Hosting möchtest, stelle sicher, dass das Ziel-Repo/Branch für Pages konfiguriert ist (öffentlich, wo erforderlich) oder verwende einen alternativen Host (z.B. Cloudflare Pages, Netlify) und stelle dort bereit.

Das war's – du baust jetzt auf GitHub's Runnern und überträgst `_site/` in ein anderes Repo in der Cloud.