---
audio: false
generated: true
lang: fr
layout: post
title: Déclenchement des GitHub Actions
translated: true
type: note
---

Oui, une GitHub Action peut déclencher une autre GitHub Action, mais pas directement. Les workflows GitHub Actions sont généralement déclenchés par des événements spécifiques tels que des pushes, des pull requests ou des planifications, mais il existe plusieurs méthodes indirectes pour qu'un workflow en déclenche un autre. Voici les principales méthodes pour y parvenir :

---

### 1. Utilisation de l'événement `workflow_dispatch`
Vous pouvez déclencher un workflow de manière programmatique en utilisant l'événement `workflow_dispatch` via l'API GitHub. Cela permet à un workflow d'en initier un autre qui est configuré pour écouter cet événement.

- **Fonctionnement** : Le premier workflow effectue un appel d'API pour déclencher le second workflow.
- **Exemple** :
  ```yaml
  name: Déclencher un Autre Workflow
  on: [push]
  jobs:
    trigger:
      runs-on: ubuntu-latest
      steps:
        - name: Déclencher le Workflow
          run: |
            curl -X POST \
              -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
              -H "Accept: application/vnd.github.v3+json" \
              https://api.github.com/repos/<owner>/<repo>/actions/workflows/<workflow_id>/dispatches \
              -d '{"ref": "main"}'
  ```
  Remplacez `<owner>`, `<repo>`, et `<workflow_id>` par les détails de votre dépôt et l'ID du workflow cible. Le second workflow doit inclure `on: [workflow_dispatch]` dans sa configuration.

---

### 2. Utilisation des Événements Repository Dispatch
Un workflow peut envoyer un événement personnalisé en utilisant un repository dispatch, qu'un autre workflow peut écouter et sur lequel il peut se déclencher.

- **Fonctionnement** : Le premier workflow envoie un événement repository dispatch via l'API GitHub, et le second workflow répond à cet événement.
- **Exemple** :
  - Premier workflow (envoie l'événement) :
    ```yaml
    name: Envoyer un Événement Dispatch
    on: [push]
    jobs:
      send-dispatch:
        runs-on: ubuntu-latest
        steps:
          - name: Envoyer le Dispatch
            run: |
              curl -X POST \
                -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/<owner>/<repo>/dispatches \
                -d '{"event_type": "custom_event"}'
    ```
  - Second workflow (déclenché par l'événement) :
    ```yaml
    name: Déclenché par Dispatch
    on:
      repository_dispatch:
        types: [custom_event]
    jobs:
      respond:
        runs-on: ubuntu-latest
        steps:
          - name: Répondre à l'Événement
            run: echo "Déclenché par custom_event"
    ```

---

### 3. Déclenchement via des Événements Git
Un workflow peut en déclencher un autre en générant un événement Git, comme créer un commit ou ouvrir une pull request, auquel le second workflow est configuré pour répondre.

- **Fonctionnement** : Le premier workflow modifie le dépôt (par exemple en poussant un commit), déclenchant ainsi un second workflow configuré pour cet événement (par exemple `on: [push]`).
- **Exemple** :
  ```yaml
  name: Créer un Commit
  on: [push]
  jobs:
    create-commit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout
          uses: actions/checkout@v2
        - name: Créer un Fichier
          run: echo "Nouveau fichier" > newfile.txt
        - name: Commit et Push
          run: |
            git config user.name "GitHub Action"
            git config user.email "action@github.com"
            git add newfile.txt
            git commit -m "Ajouter un nouveau fichier"
            git push
  ```
  Cela pourrait déclencher un autre workflow configuré pour s'exécuter sur les événements `push`.

---

### Considérations Clés
- **Permissions** : Le token GitHub utilisé dans les appels API doit avoir des permissions suffisantes pour déclencher des workflows ou envoyer des événements dispatch.
- **Limites de Taux** : Soyez conscient des limites de taux de l'API GitHub, en particulier pour les workflows s'exécutant fréquemment.
- **Éviter les Boucles** : Empêchez les boucles infinies en ajoutant des conditions pour arrêter les workflows de se déclencher mutuellement sans fin.
- **Configuration** : Assurez-vous que le workflow cible est correctement configuré pour écouter l'événement souhaité.

---

### Conclusion
Bien que GitHub Actions n'offre pas de mécanisme direct pour qu'un workflow en appelle un autre, vous pouvez y parvenir indirectement en utilisant `workflow_dispatch`, les événements repository dispatch, ou des événements Git comme les commits ou les pull requests. Ces méthodes vous permettent d'enchaîner ou de déclencher des workflows efficacement en fonction de vos besoins.