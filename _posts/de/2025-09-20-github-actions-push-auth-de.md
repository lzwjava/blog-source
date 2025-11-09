---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Behebung von GitHub Actions Push-Authentifizierungsfehlern
translated: true
type: note
---

Dieser 403-Fehler bedeutet, dass der Push sich als **`lzwjava` ohne ein Token mit Schreibzugriff** authentifiziert (oft weil der Job noch das standardmäßige `GITHUB_TOKEN` verwendet, das nicht in ein anderes Repository pushen kann). Behebe das, indem du **echte Anmeldedaten für den Ziel-Checkout/Push injectest**.

Hier sind drei zuverlässige Methoden – wähle eine aus. Ich zeige zuerst die schnellste.

---

### Option A — Verwende ein PAT und bette es in den Remote ein (schnellste)

1.  Erstelle ein **klassisches PAT** mit `repo` Scope (oder ein feingranulares PAT mit **Contents: Read & Write** für `lzwjava/lzwjava.github.io`). Speichere es im Quell-Repository als `DEPLOY_TOKEN`.

2.  Aktualisiere den Deploy-Schritt in deinem Workflow, um **den Remote zu zwingen, dieses Token zu verwenden**:

```yaml
- name: Ziel-Repository auschecken
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    token: ${{ secrets.DEPLOY_TOKEN }}
    path: destination
    fetch-depth: 0

- name: Erstellte Seite zum Ziel pushen
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll

    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # Erzwinge, dass der Remote das PAT explizit verwendet (vermeidet Konflikte mit dem Credential-Helper)
    git remote set-url origin https://${{ secrets.DEPLOY_TOKEN }}@github.com/lzwjava/lzwjava.github.io.git

    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

Wenn du immer noch einen 403-Fehler siehst, fehlen deinem PAT die nötigen Scopes oder (wenn das Repository in einer Organisation wäre) benötigt es SSO-Autorisierung. Generiere es mit `repo` Scope neu und versuche es erneut.

---

### Option B — Vermeide Credential-Bleeding: Deaktiviere die Standard-Anmeldedaten beim ersten Checkout

Manchmal schreibt der **erste Checkout** das standardmäßige `GITHUB_TOKEN` in den Credential-Helper und es wird später wiederverwendet. Deaktiviere dies:

```yaml
- name: Quell-Repository auschecken
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    persist-credentials: false   # <- wichtig
```

Behalte dann den Ziel-Checkout mit deinem PAT wie in Option A gezeigt bei (du kannst die `remote set-url` Zeile überspringen, wenn es bereits funktioniert, aber sie ist harmlos).

---

### Option C — SSH Deploy Key (sehr robust)

1.  Auf deinem Rechner: `ssh-keygen -t ed25519 -C "deploy@actions" -f deploy_key`
2.  Füge den **public Key** (`deploy_key.pub`) als **Deploy key** in `lzwjava/lzwjava.github.io` mit **Write access** hinzu.
3.  Füge den **private Key** (`deploy_key`) als `ACTIONS_DEPLOY_KEY` Secret im **Quell-**Repository hinzu.

Workflow:

```yaml
- name: Ziel-Repository per SSH auschecken
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    ssh-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
    path: destination
    fetch-depth: 0

- name: Erstellte Seite pushen (SSH)
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll
    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

---

### Schnelle Diagnose, wenn es erneut fehlschlägt

Führe diese Befehle direkt vor dem Push aus, um zu sehen, welche Auth tatsächlich konfiguriert ist:

```bash
cd destination
git remote -v
git config --get user.name
git config --get user.email
git config --get url.https://github.com/.insteadof || true
git config --global --list | sed -n 's/^credential\.helper.*/&/p'
```

Wenn `remote -v` einen einfachen `https://github.com/...` **ohne** dein injiziertes PAT (Option A) oder `git@github.com:` (Option C) anzeigt, verwendest du immer noch die falschen Anmeldedaten.

---

### Häufige Fallstricke

*   **Feingranulares PAT** muss explizit **Contents: Read & Write** **für genau dieses Repository** gewähren.
*   **Branch Protection** auf `main` kann Bot-Pushes blockieren (erforderliche Checks/Signaturen). In diesem Fall, deploye auf einen ungeschützten Branch (z.B. `gh-pages`) oder passe die Regeln an.
*   **Abgelaufenes PAT** → neu generieren.
*   **Org SSO** (trifft nicht zu, da es ein User-Repo ist) → autorisiere das PAT für die Organisation.

Führe eine der drei oben genannten Optionen aus und der 403-Fehler wird verschwinden.