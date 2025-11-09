---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Lois d'échelle pour les modèles de langage neuronaux
translated: true
type: note
---

### Aperçu
L'article de 2020 « Scaling Laws for Neural Language Models » par Jared Kaplan et ses collègues d'OpenAI (incluant Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Mann, Prafulla Dhariwal, Andrew Radford, et Ilya Sutskever) explore comment la performance des grands modèles de langage neuronaux — mesurée par la perte d'entropie croisée — évolue en fonction des ressources clés d'entraînement. Grâce à des expériences approfondies sur des modèles basés sur des transformers, ils découvrent des relations de loi de puissance prévisibles qui sont valables sur de vastes plages de tailles de modèles, de jeux de données et de budgets de calcul (couvrant plus de sept ordres de grandeur). Ces « lois d'échelle » fournissent un cadre pour optimiser l'efficacité de l'entraînement et prédire les performances sans avoir recours à la méthode essai-erreur.

### Principales découvertes sur les lois d'échelle
L'idée centrale est que la perte \\( L \\) diminue selon une loi de puissance par rapport à trois variables :
- **Taille du modèle (\\( N \\), nombre de paramètres)** : \\( L(N) \propto N^{-\alpha} \\), où \\( \alpha \approx 0,076 \\) (pour la modélisation du langage). Les modèles plus grands apprennent plus vite initialement mais s'entraînent plus lentement dans l'ensemble.
- **Taille du jeu de données (\\( D \\), nombre de tokens)** : \\( L(D) \propto D^{-\beta} \\), avec \\( \beta \approx 0,103 \\). Plus de données réduit constamment la perte, mais les gains diminuent à mesure que \\( D \\) augmente.
- **Calcul (\\( C \\), opérations en virgule flottante)** : \\( L(C) \propto C^{-\gamma} \\), où \\( \gamma \approx 0,050 \\). Ceci combine les effets de \\( N \\) et \\( D \\), car \\( C \approx 6ND \\) pour un entraînement typique.

Ces lois sont empiriques mais remarquablement cohérentes entre les architectures (par exemple, la largeur par rapport à la profondeur a peu d'impact) et les tâches. D'autres observations incluent :
- **Efficacité de l'échantillonnage** : Les modèles plus grands sont beaucoup plus efficaces en termes de données — par exemple, un modèle 100 fois plus grand n'a besoin que d'environ 10 fois moins de données pour la même perte.
- **Sur-apprentissage** : Il est prévisible sur la base du ratio \\( N/D \\) ; il se produit lorsque \\( N \\) dépasse \\( D \\) d'un certain facteur, suivant \\( L_{\text{test}} - L_{\text{train}} \propto (N/D)^\kappa \\).
- **Allocation optimale** : Pour un budget de calcul fixe, la meilleure stratégie est d'entraîner des modèles *très grands* sur une quantité *modeste* de données, en s'arrêtant tôt (avant la convergence complète) pour éviter les rendements décroissants.

### Implications théoriques et pratiques
L'article suggère que ces lois découlent de propriétés fondamentales des réseaux neuronaux, comme des pertes minimales irréductibles dues au bruit ou une perplexité irréductible. Elles remettent en question l'intuition « plus de données est toujours meilleur », favorisant plutôt des modèles massifs pour extraire plus de performance d'un calcul limité. Cela a profondément influencé le développement moderne de l'IA, justifiant les investissements dans des géants comme GPT-3 en prédisant que l'augmentation de l'échelle produit de manière prévisible des avancées.

En bref, l'article plaide pour une voie « optimale en calcul » : prioriser la taille du modèle, utiliser juste assez de données de haute qualité et s'entraîner efficacement — ouvrant la voie à l'ère de l'échelle dans les LLM.

[Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)