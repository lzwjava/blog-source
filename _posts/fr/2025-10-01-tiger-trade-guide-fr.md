---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide d'Achat et de Vente de l'Application Tiger Trade
translated: true
type: note
---

### Comment afficher Acheter/Vendre dans l'application mobile Tiger Trade Global

L'application Tiger Trade (publiée par Tiger Brokers, également connue sous le nom de Tiger Trade : Invest Globally sur le Google Play ou similaire dans les boutiques d'applications régionales) permet de trader des actions américaines, des options, des ETF, des futures et plus encore. La dernière version en septembre 2025 est la 9.4.0.2, qui a introduit des améliorations pour TigerAI concernant l'analyse et les fonctions pour actionnaires montrant les tendances d'achat/vente [1].

Pour afficher les options d'achat/vente dans l'application (en supposant que vous parliez des pages de trading d'actions ou d'options) :

1.  **Ouvrez l'application et accédez à une action** :
    - Recherchez une action (par exemple, AAPL) dans l'onglet d'accueil ou Marchés.
    - Appuyez sur l'action pour ouvrir sa page de détails, qui comprend les onglets graphique, actualités et analyse.

2.  **Afficher les boutons Acheter/Vendre pour les actions** :
    - Sur la page de l'action, descendez jusqu'en bas ou appuyez sur l'icône "Trade".
    - Les boutons Acheter et Vendre apparaissent, vous permettant de saisir les détails de l'ordre (par exemple, quantité, type d'ordre comme marché ou limite).
    - Il n'y a pas de superposition persistante des boutons d'achat/vente sur le graphique dans l'application mobile (contrairement à la version desktop, qui a des paramètres de trading sur graphique configurables avec des boutons [2] [2]).

3.  **Afficher Acheter/Vendre pour les Options** :
    - Sur la page de l'action, appuyez sur l'onglet "Options" pour voir la chaîne d'options.
    - Faites défiler pour sélectionner les dates d'expiration. Chaque option montre les cours acheteur/vendeur avec des actions d'achat/vente implicites lorsqu'on appuie dessus (acheter pour ouvrir pour les calls/puts, ou vendre si vous êtes long sur une position [3] [4]).
    - Si aucune option n'affiche d'achat/vente (par exemple, la liste apparaît vide après avoir cliqué sur quelque chose), vous avez peut-être basculé vers le filtre "Mes Positions", qui n'affiche que les options que vous détenez. Revenez à "Toutes les Options" en haut de la chaîne [4].

### Concernant la fonctionnalité "Weekly Invest"
Il n'existe pas de fonctionnalité explicitement nommée "Weekly Invest" ou "AI Weekly Invest", mais cela fait probablement référence à **l'Auto-Invest** (aussi appelé Tiger Invest), un outil d'investissement régulier pour les actions américaines et les ETF :
- Il prend en charge les achats automatisés (pas les ventes) à intervalles fixes, comme chaque semaine, à partir de 2 USD (ou l'équivalent en HKD/autres devises) en utilisant des fractions d'actions [5] [5].
- Accès : Allez dans Portefeuille > Auto-Invest (ou recherchez dans les menus de l'application).
- Cela n'affecte pas la visibilité des boutons d'achat/vente sur les pages d'actions/options — le trading reste séparé. Si les boutons Acheter/Vendre ont disparu après une interaction avec l'Auto-Invest, redémarrez l'application ou déconnectez/reconnectez-vous, car il peut s'agir d'un bug d'interface dans la version 9.4.0.2.

Si les boutons sont toujours cachés après une aventure (par exemple, après avoir cliqué sur un filtre, activé/désactivé le graphique ou utilisé une fonctionnalité d'IA), vérifiez :
- Assurez-vous que votre compte est financé et éligible au trading (Tiger prend en charge les fractions d'actions et les options pour les utilisateurs éligibles [6]).
- Désactivez les superpositions TigerAI ou changez l'unité de temps du graphique si cela interfère visuellement.
- Pour les paramètres de l'application : Appuyez sur Profil > Paramètres > vérifiez les options d'affichage (il n'y a pas de bouton spécifique pour activer/désactiver l'affichage achat/vente dans la version mobile).

Pour une aide supplémentaire, visitez le centre d'aide Tiger Trade ou contactez le support. S'il s'agit de la version desktop Tiger Trade pour Windows/Mac, les boutons de trading sur le graphique peuvent être activés via Options > Paramètres du graphique > Trading [2].

Citations :
[1] https://apps.apple.com/nz/app/tiger-trade-buy-us-asx-shares/id1023600494
[2] https://support.tiger.com/english/windows/chart/chart-trading
[3] https://www.itiger.com/sg/help/detail/option-trading
[4] https://www.youtube.com/watch?v=5JKam5MP-nc
[5] https://www.itiger.com/nz/help/detail/15849694
[6] https://play.google.com/store/apps/details?id=com.tigerbrokers.stock&hl=en_US