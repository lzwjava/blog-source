---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Débordement Graphique Circulaire dans le Portail GreptimeDB
translated: true
type: post
---

J'ai soumis un problème GitHub, https://github.com/GreptimeTeam/docs/issues/1455, intitulé "GreptimeDB Portal: Large Purple Circular Graphic Exceeds the Viewport Boundaries on Smaller Screens."

![gt_1](https://github.com/user-attachments/assets/d191f9c7-a8c6-4ba6-96c5-9388f69bef30)

Ce problème affecte considérablement l'expérience utilisateur. Il rend l'ensemble de la page d'accueil ou de l'écran facilement déplaçable et difficile à contrôler, en particulier dans la zone inférieure. Le problème devient visible après avoir fait défiler la page d'accueil pendant un certain temps.

ChatGPT :

Le principal problème de la réactivité mobile du portail GreptimeDB est que le grand graphique circulaire violet dépasse les limites de la fenêtre d'affichage sur les écrans plus petits. Ce problème survient en raison des facteurs suivants :

1. **Positionnement fixe sans ajustements réactifs** : La forme violette est probablement positionnée à l'aide de valeurs fixes ou absolues qui ne s'adaptent pas aux différentes tailles d'écran. Sans considérations de conception réactive, ces éléments peuvent déborder de la fenêtre d'affichage sur les appareils mobiles.

2. **Absence de requêtes média** : Les requêtes média sont essentielles pour appliquer différents styles en fonction des dimensions de l'écran. L'absence de requêtes média signifie que les mêmes styles sont appliqués à tous les appareils, entraînant des problèmes de mise en page sur les écrans plus petits.

3. **Méta-balise de vue manquante** : L'absence d'une méta-balise de vue peut entraîner un mauvais dimensionnement sur les appareils mobiles. L'inclusion de `<meta name="viewport" content="width=device-width, initial-scale=1.0">` dans la section `<head>` assure que la page s'adapte à différentes tailles d'écran.

**Recommandations pour résoudre le problème :**

- **Mettre en œuvre un positionnement réactif** : Utilisez des unités relatives (par exemple, des pourcentages) et des techniques de conception réactive pour vous assurer que la forme violette s'adapte correctement à différentes tailles d'écran.

- **Appliquer des requêtes média** : Intégrez des requêtes média CSS pour ajuster la taille et la position de la forme violette en fonction des dimensions de l'écran de l'appareil. Cette approche permet un style personnalisé qui améliore l'expérience de visualisation mobile.

- **Ajouter une méta-balise de vue** : Assurez-vous d'inclure la méta-balise de vue dans la section `<head>` HTML pour faciliter un dimensionnement et un rendu appropriés sur les appareils mobiles.

En abordant ces aspects, le portail GreptimeDB peut obtenir une apparence plus polie et conviviale sur les navigateurs mobiles.

## Mise à jour

Il a été corrigé par l'équipe GreptimeDB.