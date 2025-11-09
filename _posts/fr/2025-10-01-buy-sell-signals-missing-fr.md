---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Signaux d'achat et de vente manquants sur les graphiques annuels
translated: true
type: note
---

### Problème avec les signaux d'achat/vente sur le graphique en chandeliers dans l'application mobile Tiger Trade Global

Il semble que vous rencontriez un problème d'affichage où les signaux d'achat/vente (par exemple, les indicateurs techniques pour les signaux de trading comme les croisements RSI ou les signaux MACD, ou peut-être les marqueurs de flux de trades pour les volumes/exécutions d'achat/vente) apparaissent sur les graphiques en chandeliers en timeframe hebdomadaire ou mensuel mais disparaissent en vue annuelle. Dans l'application Tiger Trade (version 9.4.0.2 datant de septembre 2025), ce comportement peut être dû à des limitations de conception de l'application — les timeframes plus longs comme l'annuel ont moins de points de données (par exemple, agrégés en chandeliers mensuels), ce qui peut empêcher les indicateurs de calculer correctement, d'apparaître de manière désordonnée, ou d'être masqués complètement pour éviter des inexactitudes.

### Pourquoi cela se produit :
- **Granularité des données** : Sur les graphiques annuels, les chandeliers représentent des mois ou des années, donc les indicateurs techniques (par exemple, le RSI nécessitant ~14 points de données) peuvent ne pas déclencher de signaux en raison d'un nombre insuffisant de barres. Les timeframes plus courts (hebdomadaire/mensuel) ont plus de barres, permettant des signaux clairs.
- **Paramètres de l'application** : Dans les versions mobiles, les signaux d'achat/vente provenant du "flux de trades" (ticks de volume d'achat/vente en temps réel ou indicateurs) sont activés pour des périodes plus courtes dans les graphiques des pages de cotation pour éviter la surcharge. Des mises à jour comme la 9.2.4 ont ajouté les signaux de flux de trades, mais ils peuvent par défaut s'appliquer uniquement aux vues intraday/semaine/mois [1].
- **Raisons de performance/interface utilisateur** : L'affichage de signaux denses sur les vues annuelles pourrait ralentir l'application ou dérouter les utilisateurs, donc ils sont masqués conditionnellement.

### Comment résoudre ou contourner le problème :
1. **Changer de Timeframe comme vous l'avez fait** : Pour des signaux d'achat/vente fiables, restez sur les vues hebdomadaires ou mensuelles du graphique en chandeliers. Dans l'onglet graphique de la page de l'action, appuyez sur le sélecteur de timeframe (par exemple, "Semaine" ou "M" pour mois) pour basculer — les signaux devraient réapparaître.

2. **Vérifier les paramètres des indicateurs** :
   - Ouvrez la page de l'action > Onglet Graphique/Chandeliers.
   - Appuyez sur l'icône de modification/paramètres (⚙️ ou une clé à molette) sur le graphique.
   - Assurez-vous que vos indicateurs (par exemple, RSI, MACD) sont activés. Si les signaux se masquent toujours sur l'annuel, l'application peut les restreindre — essayez de les réajouter ou de vider le cache dans Profil > Paramètres > Vider le cache.

3. **Activer les signaux du flux de trades (le cas échéant)** :
   - Dans la dernière version 9.4.0.2, le flux de trades (indicateurs de volume d'achat/vente superposés sur les chandeliers) peut ne pas s'afficher sur l'annuel. Allez dans Profil > Paramètres > Paramètres des Cotations ou du Graphique pour activer/désactiver "Afficher le flux de trades" si disponible (les mises à jour récentes mettent l'accent sur cela pour les graphiques en timeframe [1]).
   - S'il s'agit de marqueurs de trades exécutés (points/lignes sur le graphique), l'application mobile ne les affiche généralement pas sur les graphiques ; vérifiez plutôt l'onglet "Positions" ou "Ordres" pour les achats/ventes exécutés.

4. **Mise à jour de l'application et conseils** :
   - Assurez-vous d'être en version 9.4.0.2 (vérifiez dans Profil > À propos dans l'application). Les versions antérieures peuvent avoir des bogues ; mettez à jour via l'app store.
   - Si les signaux disparaissent de manière persistante, redémarrez l'application ou déconnectez-vous/reconnectez-vous. Pour la version bureau de Tiger Trade, vous pouvez activer l'affichage complet des marqueurs via les Paramètres du graphique, mais la version mobile ne le permet pas [2] [3].
   - Pour les indicateurs personnalisés comme les flèches d'achat/vente, visitez support.tiger.com pour les FAQ mobiles — les applications ne prennent pas en charge les indicateurs auto-écrits sur mobile.

Si le problème persiste ou si vous avez besoin de signaux spécifiquement sur les graphiques annuels, contactez le support de Tiger Brokers via l'application (Profil > Aide) ou les forums, car il pourrait s'agir d'un bogue dans la version mobile globale. Pour des guides détaillés sur les indicateurs, regardez la vidéo "Adding Indicators to the K Chart" sur YouTube [4].

Citations :
[1] https://www.itiger.com/about/app/update
[2] https://support.tiger.com/english/frequently-asked-questions/questions-about-indicators
[3] https://support.tiger.com/english/windows/chart/chart-settings
[4] https://www.youtube.com/watch?v=5xgmRavEkFE