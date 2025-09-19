---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Nettoyer les éléments de démarrage dans macOS
translated: true
---

Pour gérer les applications et les processus qui se lancent automatiquement lorsque vous vous connectez à macOS (y compris macOS 15.2 et versions ultérieures), vous pouvez ajuster vos éléments de démarrage. Voici comment procéder :

### 1. **Utilisation des Paramètres Système (ou Préférences Système)**

   - **Étape 1 :** Cliquez sur le menu Apple () dans le coin supérieur gauche de votre écran et sélectionnez **Paramètres Système** (ou **Préférences Système** sur les versions antérieures de macOS).
   - **Étape 2 :** Allez dans **Général**, puis **Éléments de connexion**.
   - **Étape 3 :** Une liste des applications et services qui se lancent au démarrage s'affichera. Pour supprimer un élément, sélectionnez-le et cliquez sur le bouton **moins (–)** sous la liste.
   - **Étape 4 :** Répétez cette opération pour tous les éléments que vous souhaitez supprimer.

### 2. **Ajustement des Paramètres Spécifiques aux Applications**

   - De nombreuses applications incluent leurs propres paramètres pour contrôler leur comportement au démarrage. Consultez les préférences ou les paramètres de l'application pour désactiver le lancement automatique.

### 3. **Gestion des Agents et Démon de Lancement (Avancé)**

   - Les processus en arrière-plan peuvent être gérés par des Agents de Lancement ou des Démon de Lancement. Ces fichiers se trouvent généralement dans les répertoires suivants :
     - `~/Library/LaunchAgents` (pour les agents spécifiques à l'utilisateur)
     - `/Library/LaunchAgents` (pour les agents à l'échelle du système)
     - `/Library/LaunchDaemons` (pour les démons à l'échelle du système)
   - **Attention :** La modification de ces fichiers peut affecter la stabilité du système. Procédez avec prudence.

### Conseils :

- **Redémarrez votre Mac :** Après avoir apporté des modifications, redémarrez votre Mac pour vérifier que les éléments de démarrage ne se lancent plus.