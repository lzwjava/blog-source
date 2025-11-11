---
audio: false
generated: true
lang: fr
layout: post
title: Planification Cron des GitHub Actions
translated: true
type: note
---

Oui, un workflow GitHub peut être configuré pour s'exécuter une fois par jour en utilisant une planification cron dans GitHub Actions.

### Explication

GitHub Actions vous permet d'automatiser des tâches dans votre dépôt via des workflows, qui sont définis dans des fichiers YAML situés dans le répertoire `.github/workflows`. Une façon de déclencher un workflow est d'utiliser l'événement `schedule`, qui utilise une syntaxe similaire à cron pour spécifier quand le workflow doit s'exécuter. La syntaxe cron dans GitHub Actions suit le format POSIX standard, composé de cinq champs : minute, heure, jour du mois, mois et jour de la semaine.

Pour exécuter un workflow une fois par jour, vous pouvez utiliser une expression cron telle que `0 0 * * *`, ce qui se traduit par "chaque jour à 00:00 UTC". Voici la décomposition :
- **Minute (0)** : à 0 minute de l'heure
- **Heure (0)** : 00:00 (minuit) UTC
- **Jour du mois (*)** : Tous les jours du mois
- **Mois (*)** : Tous les mois
- **Jour de la semaine (*)** : Tous les jours de la semaine

### Exemple de Configuration

Voici un exemple de configuration de workflow GitHub Actions qui s'exécute une fois par jour :

```yaml
name: Daily Workflow
on:
  schedule:
    - cron: '0 0 * * *'
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Print message
        run: echo "This runs once a day!"
```

Ce workflow s'exécutera à minuit UTC chaque jour.

### Points Clés à Considérer

- **Fuseau Horaire** : La planification fonctionne en UTC, ajustez donc l'expression cron si vous avez besoin qu'elle s'exécute à une heure spécifique dans votre fuseau horaire local.
- **Branche par Défaut** : Par défaut, les workflows planifiés s'exécutent sur la branche par défaut du dépôt (par exemple, `main` ou `master`) sauf indication contraire.
- **Fiabilité** : Bien que GitHub Actions vise à exécuter les workflows à l'heure spécifiée, de légers retards peuvent survenir en raison de la charge de l'infrastructure, bien que cela soit rare.
- **Limites d'Utilisation** : Pour les comptes GitHub gratuits, il existe des limites sur l'utilisation d'Actions (par exemple, des minutes par mois), mais une seule exécution quotidienne est typiquement bien dans ces contraintes.

### Conclusion

Avec une expression cron correctement configurée dans le fichier de workflow, GitHub Actions peut effectivement exécuter un workflow une fois par jour. Ainsi, la réponse à votre question est **oui**.