---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Flux de Travail Automatisé de Construction et de Déploiement Jekyll
translated: true
type: note
---

Vous pouvez réaliser cela entièrement dans GitHub Actions : construire le site sur le runner, puis extraire le dépôt de destination dans un sous-dossier et pousser le contenu de `_site/` vers celui-ci.

Voici un workflow prêt à l'emploi que vous pouvez ajouter à votre dépôt **source** (où résident vos scripts Python et votre contenu Jekyll) :

```yaml
# .github/workflows/build-and-deploy.yml
name: Construire & Déployer Jekyll vers un Dépôt Externe

on:
  push:
    branches: [ main ]
  workflow_dispatch:

# Nous utiliserons un PAT pour l'écriture vers le dépôt de destination
permissions:
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Check out du dépôt source
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Configurer Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: Installer les dépendances Jekyll
        run: |
          bundle install --jobs 4 --retry 3

      - name: Configurer Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Installer les dépendances Python
        if: hashFiles('requirements.txt') != ''
        run: pip install -r requirements.txt

      - name: Exécuter votre pipeline de workflow local (mode CI)
        env:
          # ajoutez ici toutes les clés dont vos scripts ont besoin
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        run: |
          # Exécutez exactement les mêmes étapes que votre script orchestre.
          # Si vous le souhaitez, vous pouvez appeler votre script directement :
          python scripts/workflow_local.py
          # Ou, si vous préférez des étapes explicites :
          # python scripts/generate/update_notes_link.py
          # python scripts/translation/update_lang.py --max_files 9 --model gemini-flash --commits 1000
          # python -m unittest discover -s tests/workflow
          # python scripts/release/update_release.py

      - name: Construire Jekyll (vers _site)
        run: |
          # Si votre module Python définit DEFAULT_DESTINATION ailleurs, vous pouvez toujours le remplacer ici.
          bundle exec jekyll build --destination _site

      - name: Check out du dépôt de destination
        uses: actions/checkout@v4
        with:
          repository: lzwjava/lzwjava.github.io   # <-- votre cible DESTINATION_REPO_URL
          token: ${{ secrets.WORKFLOW_ACCESS_TOKEN }}      # <-- PAT avec le scope "repo"
          path: destination
          fetch-depth: 0

      - name: Synchroniser le site construit vers le dépôt de destination
        run: |
          mkdir -p destination/_site
          rsync -av --delete _site/ destination/_site/
          cd destination
          # Optionnel : s'assurer que Pages ne retraite pas le site avec Jekyll
          touch _site/.nojekyll

          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit --amend --no-edit
            # ajustez la branche si votre destination utilise autre chose (par ex., gh-pages)
            git push --force-with-lease origin HEAD:main
          else
            echo "Aucun changement à déployer."
          fi

      - name: (Optionnel) Téléverser l'artefact du site construit
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site
```

### Ce que vous devez configurer

* **PAT pour l'écriture vers la destination** : créez un Personal Access Token classique avec le scope `repo` sur votre compte GitHub (ou utilisez un token à granularité fine accordant un accès en écriture au dépôt de destination). Enregistrez-le dans les paramètres du dépôt source sous le nom `WORKFLOW_ACCESS_TOKEN` (c'est-à-dire `Settings → Secrets and variables → Actions → New repository secret`).
* **Noms des branches et des dépôts** : dans l'étape `Check out du dépôt de destination`, définissez `repository:` sur le dépôt externe (il peut être public ou privé). Dans la commande push, définissez la branche vers laquelle vous souhaitez déployer (souvent `main` ou `gh-pages`).
* **Paramètres GitHub Pages** (si vous servez le site depuis le dépôt de destination) : dans les **Settings → Pages** de ce dépôt, choisissez la **Branch** correcte (par ex., `main` / racine), et conservez `CNAME`/le domaine personnalisé comme vous le souhaitez.
* **Attentes concernant l'historique** : l'étape de déploiement modifie le dernier commit et utilise `--force-with-lease` ; assurez-vous que cette branche est dédiée aux artefacts de déploiement afin que la réécriture de l'historique soit acceptable.

### Notes concernant votre script Python

* Vous n'avez pas besoin de `open_destination_repo_in_browser()` en CI, donc il est correct de le laisser tel quel ; il ne sera simplement pas appelé ici. Le workflow pousse directement depuis le runner.
* Vous n'avez pas non plus besoin de `push_destination_repo()` en CI. Le workflow gère le second checkout et le push, vous pouvez donc garder votre script inchangé pour les exécutions locales.
* Si votre `build_site()` écrit vers un `DEFAULT_DESTINATION` différent, vous pouvez toujours le remplacer en exécutant l'étape de construction Jekyll explicite montrée ci-dessus, qui écrit vers `_site/`. L'étape de déploiement synchronise depuis `_site/`.

### Dépôt de destination privé ?

* C'est possible. GitHub Pages ne sert que les dépôts publics (ou les branches publiques dans les organisations ayant Pages activé), mais si votre objectif est simplement de pousser des artefacts vers un dépôt privé pour une raison quelconque, la méthode ci-dessus fonctionne toujours. Si vous souhaitez vraiment un hébergement Pages, assurez-vous que le dépôt/la branche de destination est configuré(e) pour servir Pages (public si nécessaire) ou utilisez un autre hébergeur (par ex., Cloudflare Pages, Netlify) et déployez-y à la place.

C'est tout — vous construirez désormais sur les runners de GitHub et pousserez `_site/` vers un autre dépôt dans le cloud.