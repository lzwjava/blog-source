---
audio: false
generated: true
lang: fr
layout: post
title: Paramètres de concurrence des GitHub Actions
translated: true
type: note
---

Votre configuration actuelle de workflow GitHub Actions a déjà `cancel-in-progress: false`, ce qui signifie qu'elle *ne devrait pas* annuler les jobs en cours d'exécution pour le groupe de concurrence `gh-pages`. Si les jobs sont toujours annulés, il pourrait y avoir un autre problème ou une mauvaise configuration causant ce comportement. Voici les étapes pour vérifier et résoudre le problème :

### 1. **Vérifier les Paramètres de Concurrence**
Votre configuration semble correcte pour empêcher l'annulation des jobs :

```yaml
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
```

- **Ce que cela fait** : La clé `concurrency` avec `cancel-in-progress: false` garantit que de multiples exécutions de workflow pour le même groupe `gh-pages` peuvent s'exécuter simultanément sans s'annuler mutuellement.
- **Où la placer** : Assurez-vous que ce bloc `concurrency` est défini **au niveau du workflow** (au niveau supérieur du fichier YAML, pas à l'intérieur d'un job ou d'une étape). Par exemple :

```yaml
name: Déployer sur GitHub Pages
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      # Vos étapes ici
```

Si le bloc `concurrency` est mal placé (par exemple, à l'intérieur d'un job), il ne fonctionnera pas comme prévu. Déplacez-le au niveau supérieur si nécessaire.

### 2. **Vérifier les Paramètres de Concurrence Conflictuels**
- **Workflows multiples** : Si vous avez plusieurs workflows (par exemple, des fichiers YAML distincts) qui interagissent avec la branche `gh-pages`, assurez-vous que *tous* les workflows concernés ont `cancel-in-progress: false`. Un seul workflow avec `cancel-in-progress: true` (ou sans `concurrency`) pourrait annuler les jobs d'autres workflows.
- **Paramètres du dépôt** : Vérifiez si des paramètres au niveau du dépôt ou des GitHub Actions tierces forcent des annulations. Par exemple, certaines intégrations CI/CD ou actions personnalisées pourraient remplacer le comportement de concurrence.

### 3. **Vérifier les Déclencheurs du Workflow**
Les jobs peuvent sembler être "annulés" si les déclencheurs sont mal configurés ou s'il y a des conditions de course. Vérifiez la section `on` de votre workflow :
- Assurez-vous que le workflow est déclenché uniquement quand c'est prévu (par exemple, `on: push: branches: [ main ]` ou `on: pull_request`).
- Si plusieurs déclencheurs sont définis (par exemple, `push` et `pull_request`), ils pourraient créer des exécutions qui se chevauchent. Utilisez des noms `concurrency.group` uniques pour différents déclencheurs si nécessaire, comme :

```yaml
concurrency:
  group: 'gh-pages-${{ github.event_name }}'
  cancel-in-progress: false
```

Cela crée des groupes de concurrence distincts pour les événements `push` et `pull_request`, les empêchant d'interférer.

### 4. **Consulter les Journaux de GitHub Actions**
- Allez dans l'onglet **Actions** de votre dépôt GitHub et examinez les journaux des jobs annulés.
- Recherchez des messages indiquant pourquoi le job a été annulé (par exemple, "Canceled due to concurrency" ou d'autres raisons comme des timeouts, une annulation manuelle ou des échecs).
- Si les journaux mentionnent la concurrence, vérifiez à nouveau que *tous* les workflows touchant la branche `gh-pages` ont `cancel-in-progress: false`.

### 5. **Gérer les Annulations Manuelles**
Si quelqu'un annule manuellement une exécution de workflow via l'interface GitHub, cela arrêtera tous les jobs de cette exécution, indépendamment de `cancel-in-progress: false`. Assurez-vous que votre équipe sait ne pas annuler manuellement les exécutions sauf si c'est nécessaire.

### 6. **Prendre en Compte les Dépendances du Workflow**
Si les jobs sont annulés à cause de dépendances ou d'échecs dans des étapes précédentes :
- Vérifiez la présence de mots-clés `needs` dans votre workflow. Si un job échoue, les jobs dépendants peuvent être ignorés ou annulés.
- Utilisez `if: always()` pour garantir que les jobs suivants s'exécutent même si les précédents échouent :

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Étapes de build
  deploy:
    needs: build
    if: always()
    runs-on: ubuntu-latest
    steps:
      # Étapes de déploiement
```

### 7. **Tester avec un Workflow Minimal**
Si le problème persiste, créez un workflow de test minimal pour isoler le problème :

```yaml
name: Test de Concurrence
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  test-job:
    runs-on: ubuntu-latest
    steps:
      - name: Sleep pour simuler un long job
        run: sleep 60
      - name: Afficher un message
        run: echo "Job terminé !"
```

Poussez plusieurs commits pour déclencher des exécutions concurrentes et vérifiez si les jobs se terminent sans annulation.

### 8. **Vérifier le Statut de GitHub Actions**
Rarement, GitHub Actions peut avoir des problèmes à l'échelle de la plateforme. Consultez la [page GitHub Status](https://www.githubstatus.com/) ou les publications récentes sur X concernant les pannes de GitHub Actions.

### 9. **Conseils de Débogage**
- Ajoutez une étape pour enregistrer l'ID d'exécution du workflow et le groupe de concurrence pour le débogage :

```yaml
steps:
  - name: Enregistrer les détails de l'exécution
    run: echo "ID d'exécution : ${{ github.run_id }}, Groupe de concurrence : ${{ github.workflow }}-${{ github.event_name }}"
```

- Utilisez l'API GitHub Actions pour inspecter les workflows en cours d'exécution de manière programmatique si nécessaire (nécessite une configuration avancée).

### Si Cela Ne Fonctionne Toujours Pas
Si les jobs sont toujours annulés :
- Partagez le fichier YAML complet du workflow et une capture d'écran ou une description du message d'annulation provenant des journaux de GitHub Actions.
- Faites-moi savoir si vous utilisez des actions spécifiques (par exemple, `actions/checkout`, `peaceiris/actions-gh-pages`) ou si vous avez plusieurs workflows interagissant avec `gh-pages`.

Cela aidera à identifier le problème exact. Faites-moi savoir comment je peux vous aider davantage !