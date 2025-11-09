---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Performance PC pour Black Myth Wukong
translated: true
type: note
---

### Black Myth: Wukong sur votre configuration PC

Votre configuration PC est une véritable bête — un i9-13900KF, une RTX 4070, 64 Go de RAM DDR5 et un stockage NVMe rapide signifient que vous allez pulvériser ce jeu en 4K avec les paramètres ultra et le ray tracing activé, en atteignant facilement plus de 60 FPS. Aucun goulot d'étranglement ici ; elle est bien au-dessus des spécifications recommandées (qui demandent une RTX 2060 et un i7-9700). Le coût total de la configuration (~14 000 CNY) est un bon rapport qualité-prix pour une machine haut de gamme comme celle-ci.

Black Myth: Wukong est un jeu de rôle d'action solo inspiré de *La Pérégrination vers l'Ouest*, où vous incarnez l'Élu (un guerrier singe) combattant des boss mythiques dans la Chine ancienne. Le combat est de type souls-like (esquive, parade, gestion de l'endurance) mais plus accessible, avec des combos fluides, des transformations et des améliorations de sorts. Comptez 30 à 40 heures pour l'histoire principale, plus l'exploration et le NG+.

#### Avez-vous besoin de Windows ? (Réponse courte : Non)
- **Steam sur Ubuntu 22.04** : Steam fonctionne nativement sous Linux. Si vous ne l'avez pas encore installé :
  1. Ouvrez un terminal et exécutez : `sudo apt update && sudo apt install steam`.
  2. Lancez Steam, connectez-vous et laissez-le télécharger les mises à jour.
- **Compatibilité du jeu** : Black Myth: Wukong n'a pas de version native Linux (il est uniquement sous Windows), mais il fonctionne *parfaitement* sous Linux via Proton (la couche de compatibilité de Valve intégrée à Steam). Il est classé **Platine** sur ProtonDB, ce qui signifie des performances "parfaites" sans bidouillage nécessaire. Les utilisateurs rapportent de meilleurs taux de rafraîchissement et une meilleure stabilité sous Linux que sous Windows dans certains cas, grâce aux versions optimisées de Proton.
- **Raccourcis potentiels** :
  - Il utilise le DRM Denuvo, qui pourrait interpréter les changements de version de Proton comme de "nouvelles installations" (limitant les activations). Tenez-vous en à une version de Proton pour éviter cela.
  - Des rares plantages au lancement ? Forcez l'utilisation de Proton Experimental dans Steam (clic droit sur le jeu > Propriétés > Compatibilité > cochez "Forcer l'utilisation d'un outil de compatibilité Steam Play spécifique" > sélectionnez Proton Experimental).
- **Test de performance** : Avant d'acheter, téléchargez l'outil de benchmark gratuit Black Myth: Wukong sur Steam — il fonctionne très bien sous Proton et vous permet de stress-tester votre configuration.
- Conclusion : Restez sur Ubuntu. Installer Windows en double amorçage est excessif, sauf si vous jouez à d'autres jeux multijoueurs lourds en anti-triche (celui-ci est solo, donc pas de problème).

Si vous *voulez vraiment* Windows pour une optimisation de pointe (par exemple, 5 à 10 % de performance en plus dans des cas marginaux), le double amorçage est facile, mais c'est inutile ici.

#### Comment l'obtenir et y jouer
1. **Acheter & Installer** :
   - Recherchez "Black Myth: Wukong" dans Steam (ID de l'application : 2358720). C'est ~60 USD / ~430 CNY, souvent en solde.
   - Taille d'installation : ~130 Go, donc votre SSD de 1 To est amplement suffisant (HDD pour le surplus si nécessaire).
   - Dans Steam : Clic droit sur le jeu > Propriétés > Compatibilité > Activer Steam Play pour tous les titres > Sélectionner Proton Experimental.

2. **Contrôles (Par défaut Clavier/Souris)** :
   - Utilisez votre souris/clavier existants — c'est réactif, mais une manette (Xbox/PS) est plus naturelle pour les combos.
   - **Mouvement** : ZQSD pour se déplacer, Espace pour esquiver/sauter, Maj pour sprinter.
   - **Combat** : Clic gauche (attaque légère), Clic droit (attaque lourde), R (parade — le timing est crucial !), Q/E (sorts), F (immobiliser les ennemis pour les coups de grâce).
   - **Endurance** : Les attaques/esquives vident une barre bleue — gérez-la comme dans Dark Souls.
   - **Améliorations** : Collectez de la Volonté (équivalent des âmes) pour améliorer les compétences aux autels. Concentrez-vous sur les bâtons, les transformations (par exemple, devenir un oiseau pour des attaques aériennes) et les reliques.
   - Remappez les touches dans Paramètres > Contrôles si nécessaire.

3. **Conseils rapides pour bien démarrer** :
   - **Début de partie** : Priorisez l'esquive plutôt que le blocage — la parade vient plus tard. Explorez pour trouver des pots cachés (ils donnent du butin).
   - **Boss** : Apprenez les patterns ; utilisez les piliers pour vous couvrir. Les Étincelles (améliorations) sont cachées — cherchez en hauteur et en bas.
   - **Performance** : Dans le jeu, réglez le préréglage sur Très Élevé, DLSS Qualité (votre 4070 excelle ici), et limitez les FPS à 60 pour une expérience fluide.
   - **Audio/Sous-titres** : La VO anglaise est correcte, mais le chinois avec les sous-titres capture mieux l'ambiance mythique.
   - Sauvegardez souvent aux Autels du Gardien (points de contrôle).

Si vous rencontrez des problèmes (par exemple, configuration de la manette), Lutris ou Heroic Launcher sont des alternatives, mais Steam Proton est le plus simple. Profitez des combats épiques — c'est l'un des meilleurs jeux de 2024 !

#### Références
- [Black Myth: Wukong sur Steam](https://store.steampowered.com/app/2358720/Black_Myth_Wukong/)
- [ProtonDB : Black Myth: Wukong](https://www.protondb.com/app/2358720)
- [Reddit : Wukong Benchmark sur Proton](https://www.reddit.com/r/linux_gaming/comments/1er0biq/black_myth_wukong_has_a_free_benchmark_and_it/)
- [SteamDB : Détails de l'application](https://steamdb.info/app/2358720/)