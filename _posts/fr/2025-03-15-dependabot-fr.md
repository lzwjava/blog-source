---
audio: false
generated: true
lang: fr
layout: post
title: Suppression de Dependabot
translated: true
type: note
---

Pour supprimer Dependabot de GitHub Actions, vous devez désactiver sa capacité à créer des pull requests qui déclenchent des workflows et, optionnellement, supprimer tous les workflows personnalisés spécifiquement liés à Dependabot. Voici les étapes pour y parvenir. Notez que je suppose que "dependant bot" dans votre requête fait référence à "Dependabot", un outil courant sur GitHub pour la gestion des dépendances.

---

### Étape 1 : Désactiver les mises à jour de version de Dependabot
Les mises à jour de version de Dependabot créent automatiquement des pull requests pour maintenir vos dépendances à jour. Ces pull requests peuvent déclencher des workflows GitHub Actions. Pour désactiver cette fonctionnalité :

- **Localiser le fichier de configuration** : Vérifiez dans votre dépôt la présence d'un fichier nommé `dependabot.yml` dans le répertoire `.github`.
- **Supprimer le fichier** : S'il existe, supprimez le fichier `dependabot.yml` et validez cette modification. Cela empêche Dependabot de créer des pull requests pour les mises à jour de version.
- **Vérifier** : Si aucun fichier `dependabot.yml` n'existe, les mises à jour de version sont déjà désactivées.

---

### Étape 2 : Désactiver les mises à jour de sécurité de Dependabot
Les mises à jour de sécurité de Dependabot génèrent des pull requests pour corriger les vulnérabilités dans vos dépendances, ce qui peut également déclencher des workflows GitHub Actions. Pour les désactiver :

- **Accéder aux paramètres du dépôt** : Dans votre dépôt GitHub, cliquez sur l'onglet **Settings**.
- **Naviguer vers les paramètres de sécurité** : Faites défiler jusqu'à **Security & analysis** (ou **Code security and analysis**, selon l'interface de votre GitHub).
- **Désactiver les mises à jour de sécurité** : Trouvez **Dependabot security updates** et cliquez sur **Disable**.

Cela empêche Dependabot de créer des pull requests pour les corrections de sécurité.

---

### Étape 3 : (Optionnel) Supprimer les workflows personnalisés liés à Dependabot
Si vous avez configuré des workflows GitHub Actions spécifiquement pour gérer les pull requests de Dependabot (par exemple, fusion automatique, étiquetage ou utilisation des métadonnées de Dependabot), vous pouvez les nettoyer :

- **Vérifier les fichiers de workflow** : Recherchez dans le répertoire `.github/workflows` les fichiers YAML.
- **Identifier la logique Dependabot** : Recherchez des conditions comme `if: github.event.pull_request.user.login == 'dependabot[bot]'` ou des actions telles que `dependabot/fetch-metadata`.
- **Supprimer ou modifier** : Supprimez ces workflows ou ajustez-les pour supprimer la logique spécifique à Dependabot, puis validez les modifications.

Cette étape est optionnelle car la désactivation de Dependabot dans les étapes 1 et 2 l'empêchera de créer de nouvelles pull requests, ce qui signifie que les workflows existants ne seront plus déclenchés par Dependabot. Cependant, supprimer ces workflows garantit un nettoyage complet.

---

### Notes supplémentaires
- **Pull Requests existantes** : La désactivation de Dependabot ne ferme pas les pull requests existantes qu'il a créées. Celles-ci peuvent toujours déclencher des workflows si elles sont mises à jour. Vous pouvez les fermer manuellement si nécessaire.
- **Alertes Dependabot** : Si vous souhaitez également arrêter les notifications de vulnérabilité (non directement liées à GitHub Actions), allez dans **Settings > Security & analysis** et désactivez **Dependabot alerts**. Ceci est optionnel et sans rapport avec les déclencheurs de workflow.

---

### Résultat
En complétant les étapes 1 et 2, Dependabot ne créera plus de pull requests dans votre dépôt, supprimant ainsi efficacement son influence sur GitHub Actions. Si vous avez personnalisé des workflows pour Dependabot, l'étape 3 garantit que toute l'automatisation associée est supprimée. Vos GitHub Actions ne s'exécuteront désormais qu'en fonction d'autres événements, sans être affectées par Dependabot.