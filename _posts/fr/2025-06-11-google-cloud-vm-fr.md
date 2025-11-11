---
audio: false
generated: true
lang: fr
layout: post
title: Instance Google Cloud la plus économique
translated: true
type: note
---

Lorsque vous recherchez une machine virtuelle (VM) rentable sur Google Cloud, il y a plusieurs options et considérations à garder à l'esprit pour respecter votre budget d'environ 5 $ par mois. Voici quelques étapes et conseils pour vous aider à trouver l'option de VM la moins chère :

1. **VM à cœurs partagés** : Google Cloud propose des VM à cœurs partagés, qui sont les options les plus économiques. Ces VM partagent la puissance du CPU avec d'autres clients, ce qui peut entraîner des performances moins robustes mais les rend nettement moins chères. Cela peut être un bon point de départ pour un serveur simple avec de faibles besoins en ressources.

2. **VM préemptibles** : Envisagez d'utiliser des VM préemptibles, qui offrent des remises substantielles par rapport aux VM standard. Ces VM peuvent être arrêtées par Google Cloud si leurs ressources sont nécessaires ailleurs, elles conviennent donc mieux aux charges de travail tolérantes aux pannes. Les VM préemptibles peuvent offrir des remises allant jusqu'à 80 % par rapport aux prix standard.

3. **VM Tau** : Les VM Tau de Google Cloud sont conçues pour les charges de travail de scale-out et offrent jusqu'à 42 % de performance-prix en plus par rapport aux VM à usage général. Elles peuvent être plus rentables pour certains types de charges de travail.

4. **Types de machine personnalisés** : Vous pouvez créer des types de machine personnalisés adaptés à vos besoins spécifiques, ce qui peut aider à réduire les coûts en ne payant que pour les ressources dont vous avez besoin. Cette flexibilité vous permet d'ajuster avec précision le CPU et la mémoire pour correspondre aux exigences de votre charge de travail.

5. **Remises d'utilisation soutenue** : Google Cloud applique automatiquement des remises d'utilisation soutenue pour les VM qui fonctionnent pendant une partie significative du mois de facturation. La remise augmente avec l'utilisation et peut atteindre jusqu'à 30 % de réduction sur le prix standard.

6. **Niveau gratuit** : Google Cloud propose un niveau gratuit qui inclut une petite quantité de ressources de calcul chaque mois. Cela peut être suffisant pour des applications très légères et peut aider à réduire davantage les coûts.

7. **Calculateur de coûts** : Utilisez le Google Cloud Pricing Calculator pour estimer les coûts de différentes configurations et trouver la configuration la plus rentable pour vos besoins.

8. **VM Spot** : Les VM Spot offrent une tarification dynamique avec des remises de 60 à 91 % sur le prix on-demand pour la plupart des types de machine. Elles peuvent être une option très rentable si votre charge de travail peut tolérer des interruptions.

Pour un serveur simple avec de faibles besoins en ressources, commencer par une VM à cœurs partagés ou préemptible pourrait être la meilleure approche. Vous pouvez ensuite surveiller les performances et ajuster la configuration si nécessaire pour équilibrer coût et performance.