---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Résoudre les erreurs d'authentification de poussée GitHub Actions
translated: true
type: note
---

Cette erreur 403 signifie que le push s'authentifie en tant que **`lzwjava` sans un jeton qui a un accès en écriture** (souvent parce que le job utilise encore le `GITHUB_TOKEN` par défaut, qui ne peut pas pousser vers un autre dépôt). Corrigez cela en **injectant une véritable credential pour le checkout/push de destination**.

Voici trois méthodes solides — choisissez-en une. Je vais montrer la plus rapide en premier.

---

### Option A — Utiliser un PAT et l'intégrer dans le remote (plus rapide)

1. Créez un **PAT classique** avec le scope `repo` (ou un PAT à granularité fine avec **Contents: Read & Write** pour `lzwjava/lzwjava.github.io`). Enregistrez-le dans le dépôt source en tant que `DEPLOY_TOKEN`.

2. Mettez à jour l'étape de déploiement de votre workflow pour **forcer le remote à utiliser ce jeton** :

```yaml
- name: Check out destination repo
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    token: ${{ secrets.DEPLOY_TOKEN }}
    path: destination
    fetch-depth: 0

- name: Push built site to destination
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll

    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # Force le remote à utiliser le PAT explicitement (évite les conflits credential-helper)
    git remote set-url origin https://${{ secrets.DEPLOY_TOKEN }}@github.com/lzwjava/lzwjava.github.io.git

    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

Si vous voyez toujours une erreur 403, votre PAT manque de scopes ou (si le dépôt était dans une organisation) nécessite une autorisation SSO. Régénérez-le avec le scope `repo` et réessayez.

---

### Option B — Éviter la contamination des credentials : désactiver les credentials par défaut sur le premier checkout

Parfois, le **premier checkout** écrit le `GITHUB_TOKEN` par défaut dans le credential helper et il est réutilisé plus tard. Désactivez-le :

```yaml
- name: Check out source repo
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    persist-credentials: false   # <- important
```

Ensuite, gardez le checkout de destination avec votre PAT comme montré dans l'Option A (vous pouvez sauter la ligne `remote set-url` si cela fonctionne déjà, mais elle est inoffensive).

---

### Option C — Clé de déploiement SSH (très robuste)

1. Sur votre machine : `ssh-keygen -t ed25519 -C "deploy@actions" -f deploy_key`
2. Ajoutez la **clé publique** (`deploy_key.pub`) en tant que **Deploy key** dans `lzwjava/lzwjava.github.io` avec un **accès en écriture**.
3. Ajoutez la **clé privée** (`deploy_key`) en tant que secret `ACTIONS_DEPLOY_KEY` dans le dépôt **source**.

Workflow :

```yaml
- name: Check out destination repo via SSH
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    ssh-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
    path: destination
    fetch-depth: 0

- name: Push built site (SSH)
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

### Diagnostic rapide en cas de nouvel échec

Exécutez ces commandes juste avant de pousser pour voir quelle authentification est réellement configurée :

```bash
cd destination
git remote -v
git config --get user.name
git config --get user.email
git config --get url.https://github.com/.insteadof || true
git config --global --list | sed -n 's/^credential\.helper.*/&/p'
```

Si `remote -v` montre un simple `https://github.com/...` **sans** votre PAT injecté (Option A) ou `git@github.com:` (Option C), vous utilisez toujours la mauvaise credential.

---

### Pièges courants

* Un **PAT à granularité fine** doit explicitement accorder **Contents: Read & Write** **à ce dépôt exact**.
* La **protection de branche** sur `main` peut bloquer les pushes des bots (checks/signatures requis). Si c'est le cas, déployez sur une branche non protégée (par exemple, `gh-pages`) ou ajustez les règles.
* Un **PAT expiré** → régénérez-le.
* **SSO d'organisation** (pas votre cas si c'est un dépôt utilisateur) → autorisez le PAT pour l'organisation.

Faites l'une des trois options ci-dessus et l'erreur 403 disparaîtra.