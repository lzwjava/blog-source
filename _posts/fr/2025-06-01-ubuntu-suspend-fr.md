---
audio: false
generated: true
lang: fr
layout: post
title: Guide de mise en veille d'Ubuntu
translated: true
type: note
---

Sous Ubuntu, vous pouvez mettre votre système en veille ou en hibernation en utilisant plusieurs méthodes :

## Méthodes graphiques :
- **Coin supérieur droit** : Cliquez sur l'icône d'alimentation/paramètres dans le panneau supérieur, puis sélectionnez « Suspendre » (veille) ou « Hiberner » si disponible
- **Menu Activités** : Appuyez sur la touche Super, tapez « power » ou « suspend », et sélectionnez les options d'alimentation

## Méthodes en ligne de commande :
```bash
# Pour suspendre (veille)
systemctl suspend

# Pour hiberner
systemctl hibernate

# Pour le mode veille hybride (combinaison des deux)
systemctl hybrid-sleep
```

## Raccourcis clavier :
- De nombreux systèmes Ubuntu utilisent par défaut **Fn + Touche Veille** ou **Ctrl + Alt + Fin**
- Vous pouvez les personnaliser dans Paramètres > Clavier > Raccourcis

## Notes importantes :
- **Veille/Suspendre** : Maintient la RAM sous tension, réveil rapide mais utilise un peu de batterie
- **Hibernation** : Sauvegarde tout sur le disque et éteint le système, réveil plus lent mais aucune consommation d'énergie
- L'hibernation pourrait ne pas être activée par défaut sur les versions récentes d'Ubuntu en raison de problèmes potentiels avec certains matériels

Si l'hibernation ne fonctionne pas, vous devrez peut-être d'abord l'activer en configurant l'espace swap et en modifiant les paramètres système. La veille/suspension devrait fonctionner immédiatement sur la plupart des systèmes.