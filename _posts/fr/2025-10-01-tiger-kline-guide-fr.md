---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide des indicateurs de K-Line de l'application Tiger Trade
translated: true
type: note
---

Dans l'application mobile Tiger Trade Global (dernière version 9.4.0.2 en septembre 2025), le graphique en K-ligne (chandeliers) sur les pages des actions affiche les données de prix, mais il n'intègre pas de marqueurs de trade ou d'indicateurs d'achat/vente pour les ordres exécutés (contrairement à la version desktop, où vous pouvez activer l'affichage des ordres via Paramètres du graphique > Trading). Cependant, vous pouvez ajouter des indicateurs techniques personnalisables au graphique en K-ligne qui analysent les tendances de prix et génèrent des signaux d'achat/vente, tels que les moyennes mobiles, le RSI (Relative Strength Index), le MACD ou les Bandes de Bollinger. Ceux-ci peuvent représenter visuellement des signaux haussiers/baissiers sur le graphique (par exemple, des croisements indiquant des points d'achat/vente).

Si des signaux d'achat/vente ont disparu après des clics accidentels (par exemple, en désactivant des indicateurs), vous devrez peut-être les réactiver ou les rajouter.

### Étapes pour Afficher/Ajouter des Indicateurs d'Achat/Vente sur le Graphique en K-Ligne :
1. **Ouvrez l'Application et Sélectionnez une Action** :
   - Recherchez une action (par exemple, AAPL) et appuyez dessus pour ouvrir la page de détails.

2. **Accédez au Graphique** :
   - Le graphique en K-ligne se trouve dans l'onglet "Chart" ou "K-Line" (vue par défaut sur la page de l'action).
   - Appuyez sur la zone du graphique pour faire apparaître la barre d'outils ou le menu (généralement en haut ou en bas).

3. **Ajoutez des Indicateurs** :
   - Recherchez une icône en forme de clé, d'engrenage ou "Edit" (⚙️) sur le graphique.
   - Appuyez dessus pour ouvrir les paramètres. Dans la liste des indicateurs, sélectionnez parmi les outils de signal d'achat/vente courants comme :
     - **Moyennes Mobiles (MA)** : Simple/EMA – Achetez lorsque la MA rapide croise au-dessus de la MA lente ; vendez sur les baisses.
     - **RSI** : Oscille entre 0-100 ; achetez en dessous de 30 (survendu), vendez au-dessus de 70 (suracheté).
     - **MACD** : Achetez lorsque les barres de l'histogramme deviennent positives ; vendez sur négatif.
     - **Bandes de Bollinger** : Achetez lorsque le prix touche la bande inférieure ; vendez à la bande supérieure.
   - Activez 1 à 3 indicateurs à la fois pour plus de clarté. Les signaux apparaissent sous forme de lignes, de flèches ou de superpositions sur les K-lignes.
   - Confirmez et appliquez les modifications pour les afficher.

4. **Personnalisez ou Désactivez** :
   - Pour supprimer/réactiver, retournez dans les paramètres des indicateurs et désélectionnez ou resélectionnez-les.
   - La dernière mise à jour 9.4.0.2 inclut des suppléments d'indicateurs de K-ligne pour une meilleure visualisation des signaux [1][2][3].

Si cela ne correspond pas à votre expérience (par exemple, pas d'icône d'édition ou indicateurs ne fonctionnant pas), assurez-vous que l'application est à jour, car les versions antérieures peuvent manquer certaines fonctionnalités. Pour en savoir plus sur la lecture des K-lignes et l'utilisation des indicateurs pour le timing d'achat/vente, reportez-vous aux tutoriels de Tiger Academy (par exemple, "10. Use technical indicators to determine the best buy and sell prices") [3][2]. Si vous utilisez plutôt l'application desktop Tiger Trade, les paramètres du graphique permettent d'activer les marqueurs d'ordre (ancres avec des lignes pour les niveaux d'achat/vente) sous Options > Paramètres du graphique > Trading > Afficher les ordres [4].

Pour des exemples visuels, recherchez "Adding Indicators to the K Chart" sur YouTube ou les forums de Tiger Brokers. Si le problème persiste, contactez le support de l'application via Profil > Aide.

Citations :
[1] https://www.youtube.com/watch?v=5xgmRavEkFE
[2] https://www.itiger.com/about/app/update
[3] https://www.itiger.com/sg/learn/detail/lnfogp3rckf7pksfpbd
[4] https://support.tiger.com/english/windows/chart/chart-settings