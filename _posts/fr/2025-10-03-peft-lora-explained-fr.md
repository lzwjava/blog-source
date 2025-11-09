---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Explication Structurée de PEFT et LoRA
translated: true
type: note
---

### 1. L'échelle des modèles de langage modernes : le pré-entraînement et son importance
Le texte commence par souligner l'échelle immense des principaux LLM actuels : « Les principaux modèles de langage d'aujourd'hui contiennent plus de mille milliards de paramètres, pré-entraînés sur des dizaines de milliers de milliards de tokens. Les performances des modèles de base continuent de s'améliorer avec l'échelle, car ces milliers de milliards sont nécessaires pour apprendre et représenter tous les motifs présents dans les connaissances humaines écrites. »

#### Que sont les paramètres et les tokens ?
- **Les paramètres** sont les « poids » dans un réseau de neurones – des valeurs numériques que le modèle apprend pendant l'entraînement. Considérez-les comme la « mémoire » ou les « boutons de réglage » des connaissances du modèle. Un modèle à mille milliards de paramètres (par exemple, GPT-4 ou PaLM) possède environ 1 000 milliards de telles valeurs, ce qui équivaut approximativement au stockage de données de millions d'images haute résolution.
- **Les tokens** sont les unités de base du texte que le modèle traite (par exemple, des mots ou des sous-mots). Le pré-entraînement consiste à fournir au modèle **des dizaines de milliers de milliards** de ces tokens (par exemple, provenant de livres, de sites web et de dépôts de code) pour qu'il apprenne des motifs généraux comme la grammaire, les faits et le raisonnement.

#### Pourquoi l'échelle améliore-t-elle les performances ?
- Les LLM sont des architectures basées sur les transformateurs (introduites dans l'article de 2017 « Attention is All You Need »), qui excellent à capturer des motifs complexes grâce à des couches de mécanismes d'attention et de réseaux feed-forward.
- Les lois d'échelle empiriques (par exemple, de Kaplan et al. d'OpenAI, 2020) montrent que les performances (par exemple, la précision sur des tâches comme le question-réponse) s'améliorent de manière prévisible avec plus de paramètres, de données et de calcul. Doubler les paramètres donne souvent des gains logarithmiques dans les « capacités émergentes » (par exemple, le modèle devient soudainement bon en mathématiques ou en traduction).
- **Intuition** : La connaissance humaine est vaste et interconnectée. Pour la représenter entièrement (par exemple, la syntaxe de chaque langue, les faits historiques, les principes scientifiques), le modèle a besoin d'un « espace de paramètres » énorme pour encoder celles-ci sous forme de corrélations de bas niveau. Les modèles plus petits (par exemple, 1 milliard de paramètres) surapprennent les motifs superficiels et échouent sur des tâches nuancées, tandis que les modèles à l'échelle du billion généralisent mieux.
- **Compromis** : Cette échelle nécessite une puissance de calcul massive (par exemple, des milliers de GPU pendant des semaines) et de l'énergie, mais c'est la fondation pour les « modèles de base » comme les séries Llama ou GPT.

En bref, le pré-entraînement construit un « cerveau » polyvalent en forçant brutalement l'apprentissage des motifs à partir du corpus écrit de l'humanité. Le texte présente cela comme la ligne de base avant toute spécialisation.

### 2. Post-entraînement (Fine-Tuning) : Concentration plus étroite et défis d'efficacité
Le texte oppose le pré-entraînement au « post-entraînement », qui « implique des ensembles de données plus petits et se concentre généralement sur des domaines de connaissances et des gammes de comportement plus restreints. Il semble peu économique d'utiliser un térabit de poids pour représenter des mises à jour provenant d'un gigabit ou d'un mégabit de données d'entraînement. »

#### Qu'est-ce que le Post-entraînement/Fine-Tuning ?
- Après le pré-entraînement, le modèle de base est « fine-tuné » sur des ensembles de données plus petits et spécifiques à une tâche (par exemple, 1 à 10 millions d'exemples contre des milliers de milliards de tokens). Cela l'adapte à des applications comme les chatbots (par exemple, le suivi d'instructions), l'analyse de sentiments ou les questions-réponses médicales.
- Exemples : Fine-tuner GPT-3 sur des logs de support client pour créer un assistant utile, ou sur des textes juridiques pour la revue de contrats.
- **Pourquoi des ensembles de données plus petits ?** Le fine-tuning cible des « mises à jour » ou des « remplacements » de la connaissance de base – par exemple, enseigner la politesse ou le jargon spécifique à un domaine – sans réinventer la compréhension générale du langage.

#### L'intuition du gaspillage
- **Inadéquation entre la taille des données et celle du modèle** : Si le modèle de base a environ ~1 trillion de paramètres (échelle du térabit, puisqu'environ 1 bit par paramètre), mais que les données de fine-tuning sont minuscules (échelle du gigabit ou du mégabit), mettre à jour *tous* les paramètres revient à réécrire une encyclopédie entière pour une seule note de bas de page. La plupart des poids du modèle restent non pertinents pour la nouvelle tâche.
- **Problèmes du Fine-Tuning Complet (FullFT)** :
  - **Surcharge de calcul** : La mise à jour de tous les paramètres nécessite de recalculer les gradients (signaux d'erreur) pour l'ensemble du modèle à chaque étape d'entraînement. Cela multiplie les coûts mémoire et temporels par 10 à 100x.
  - **Oubli catastrophique** : Le FullFT peut dégrader les capacités générales du modèle (par exemple, un modèle fine-tuné pour les mathématiques oublie la poésie).
  - **Gonflement du stockage** : Les modèles fine-tunés sont aussi volumineux que le modèle de base (des billions de paramètres), ce qui rend le déploiement coûteux (par exemple, les coûts cloud augmentent avec la taille).
- **Analogie** : Imaginez accorder un orchestre massif pour une performance solo en réentraînant chaque musicien. C'est excessif alors que vous pourriez simplement coacher le soliste.

Cette inefficacité a motivé le **Parameter Efficient Fine-Tuning (PEFT)** : des méthodes pour mettre à jour seulement une infime fraction (par exemple, 0,1 à 1 %) des paramètres tout en atteignant 90 à 100 % des gains de performance du FullFT.

### 3. Parameter Efficient Fine-Tuning (PEFT) : L'idée générale
« Le PEFT... ajuste un grand réseau en mettant à jour un ensemble de paramètres beaucoup plus petit. »

- **Motivation principale** : Préserver les forces du modèle de base tout en injectant des mises à jour spécifiques à une tâche avec des changements minimaux. Cela réduit le calcul, la mémoire et le stockage – crucial pour démocratiser l'IA (par exemple, permettre à de petites équipes de fine-tuner des modèles comme Llama 2 sans supercalculateurs).
- **Techniques PEFT courantes** (au-delà de LoRA, mentionné plus tard) :
  - **Adaptateurs** : Insérer de petits modules « plug-in » (par exemple, des couches bottleneck) entre les couches de transformateurs, en n'entraînant que ceux-ci.
  - **Prompt Tuning** : Apprendre des prompts logiciels (par exemple, des tokens virtuels) ajoutés aux entrées, en mettant à jour seulement ~0,01 % des paramètres.
  - **Prefix Tuning** : Similaire, mais ajuste les préfixes pour les couches d'attention.
- **Pourquoi cela fonctionne** : Les mises à jour du fine-tuning sont souvent « de faible dimension » – elles se situent dans un sous-espace de l'espace complet des paramètres. Vous n'avez pas besoin de tout modifier ; quelques changements ciblés se propagent à travers le réseau.
- **Succès empirique** : Les méthodes PEFT égalent ou dépassent le FullFT sur des benchmarks comme GLUE (compréhension du langage naturel) avec 10 à 100 fois moins de calcul. Des bibliothèques comme PEFT de Hugging Face rendent cela plug-and-play.

Le PEFT change le paradigme de « tout entraîner » à « modifier de manière chirurgicale », s'alignant sur le thème de l'efficacité du texte.

### 4. Low-Rank Adaptation (LoRA) : La principale méthode PEFT
« La principale méthode PEFT est la Low-Rank Adaptation, ou LoRA. LoRA remplace chaque matrice de poids W du modèle original par une version modifiée W′ = W + γ B A, où B et A sont des matrices qui, ensemble, ont beaucoup moins de paramètres que W, et γ est un facteur d'échelle constant. En effet, LoRA crée une représentation en faible dimension des mises à jour apportées par le fine-tuning. »

#### Analyse mathématique
LoRA cible les matrices de poids **W** dans le transformateur (par exemple, dans les projections requête/clé/valeur pour l'attention ou les couches feed-forward). Ce sont généralement des matrices d × k (par exemple, 4096 × 4096, des millions de paramètres chacune).

- **La Formule** : Pendant le fine-tuning, au lieu de mettre à jour W directement, LoRA calcule les sorties comme :
  ```
  h = W x + γ (B A) x  (où x est l'entrée)
  ```
  - **W** : Poids originaux gelés (inchangés).
  - **A** : Une matrice de faible rang, initialisée aléatoirement (par exemple, r × k, où r << d, comme r=8-64).
  - **B** : Une autre matrice de faible rang (d × r), initialisée à zéro (ainsi la mise à jour initiale est nulle, évitant les perturbations).
  - **γ (gamma)** : Facteur d'échelle (par exemple, γ = α / r, où α est un hyperparamètre comme 16) pour contrôler l'amplitude de la mise à jour et stabiliser l'entraînement.
  - Poids mis à jour complet : **W' = W + γ B A**.

- **Pourquoi « Low-Rank » (Faible Rang) ?**
  - Les matrices peuvent être décomposées via la décomposition en valeurs singulières (SVD) : Toute matrice ≈ U Σ V^T, où le « rang » est le nombre de valeurs singulières significatives.
  - Les mises à jour du fine-tuning ΔW = W' - W sont souvent **de faible rang** (r << min(d,k)), ce qui signifie qu'elles capturent les changements dans un sous-espace compressé (par exemple, quelques directions comme « accentuer la sécurité » ou « se concentrer sur le code »).
  - **B A** approxime ΔW avec un rang r (paramètres : d*r + r*k contre d*k pour W complet). Pour r=8 dans un W de 4096×4096, LoRA utilise ~65k paramètres contre 16M – une réduction de 99,6 % !
  - **Intuition** : Les mises à jour sont comme des vecteurs dans un espace à haute dimension ; LoRA les projette sur une « autoroute » à faible dimension (rang r), ignorant le bruit dans le vaste espace des paramètres.

- **Comment fonctionne l'entraînement** :
  1. Passe avant : Calculer h en utilisant W + γ B A, mais n'entraîner que A et B (W gelé).
  2. Rétropropagation : Les gradients ne circulent que vers A/B, gardant la mémoire faible.
  3. Inférence : Soit fusionner (W' = W + B A) pour un modèle unique, soit garder séparé pour la modularité.
- **D'après l'article (Hu et al., 2021)** : LoRA a été introduit pour les modèles de vision et de langage mais a explosé dans le NLP. Il surpasse les adaptateurs sur des tâches comme la synthèse tout en utilisant moins de mémoire. Des variantes comme QLoRA quantifient davantage le modèle de base pour des empreintes encore plus petites.

En substance, LoRA « pirate » le modèle en ajoutant un « delta » léger (B A) qui représente le fine-tuning comme une transformation linéaire compacte.

### 5. Avantages de LoRA par rapport au Fine-Tuning Complet (FullFT)
Le texte énumère les avantages opérationnels, en soulignant l'aspect pratique au-delà de la simple efficacité brute. Je vais développer chacun d'eux.

#### a. Coût et vitesse du post-entraînement
- LoRA s'entraîne 100 à 1000 fois plus vite/moins cher car il ne met à jour que ~0,1 % des paramètres. Par exemple, fine-tuner Llama-7B sur un seul GPU A100 (FullFT nécessite 8+ GPU) prend des heures contre des jours.
- Une précision inférieure (par exemple, bfloat16) suffit, réduisant la consommation d'énergie.

#### b. Service multi-locataire
« Puisque LoRA entraîne un adaptateur (c'est-à-dire les matrices A et B) tout en gardant les poids originaux inchangés, un seul serveur d'inférence peut garder en mémoire de nombreux adaptateurs (différentes versions du modèle) et en échantillonner simultanément de manière groupée. Punica: Multi-Tenant LoRA Serving (Chen, Ye, et al, 2023) Les moteurs d'inférence modernes tels que vLLM et SGLang implémentent cette fonctionnalité. »

- **Ce que cela signifie** : La base W est partagée ; les adaptateurs sont minuscules (Mo contre Go pour les modèles complets). Un serveur charge un W + N adaptateurs (par exemple, pour le codage, l'écriture, la traduction).
- **Multi-locataire** : Servir plusieurs utilisateurs/modèles en parallèle sans recharger la base. Regrouper les requêtes entre les adaptateurs pour plus d'efficacité.
- **Impact dans le monde réel** : En production (par exemple, Hugging Face Spaces ou Azure ML), cela permet des « soupes de modèles » ou de changer de personnalité à la volée. Punica (2023) optimise la mémoire via la pagination ; vLLM/SGLang utilisent l'attention paginée pour un débit 10x supérieur.
- **Analogie** : Comme un seul moteur (W) avec des kits turbo interchangeables (adaptateurs) contre l'achat d'une nouvelle voiture par réglage.

#### c. Taille de l'infrastructure pour l'entraînement
« Lors du fine-tuning de l'ensemble du modèle, l'état de l'optimiseur doit être stocké avec les poids originaux, souvent à une précision plus élevée. En conséquence, le FullFT nécessite généralement un ordre de grandeur d'accélérateurs de plus que l'échantillonnage à partir du même modèle... Pour l'entraînement, en plus de stocker les poids, nous devons généralement stocker les gradients et les moments de l'optimiseur pour tous les poids ; de plus, ces variables sont souvent stockées dans une précision plus élevée (float32) que celle utilisée pour stocker les poids pour l'inférence (bfloat16 ou moins). Puisque LoRA entraîne beaucoup moins de poids et utilise beaucoup moins de mémoire, il peut être entraîné sur une infrastructure seulement légèrement plus grande que celle utilisée pour l'échantillonnage. »

- **Répartition de la mémoire d'entraînement** :
  - FullFT : Poids (1T params @ bfloat16 = ~2 To) + Gradients (identique) + États de l'optimiseur (par exemple, Adam : 2 moments par param @ float32 = ~8 To au total). Nécessite des centaines de GPU dans une « infrastructure » distribuée (par exemple, parallélisme de données/modèle).
  - LoRA : Seuls A/B (~0,1 % des paramètres) obtiennent des gradients/états (~2-10 Go supplémentaires). Entraînement sur 1-2 GPU, même infrastructure que pour l'inférence.
- **Détails sur la précision** : L'inférence utilise une faible précision (bfloat16/float16) pour la vitesse ; l'entraînement a besoin de float32 pour la stabilité des gradients. LoRA minimise cette surcharge.
- **Accessibilité** : Les amateurs/startups peuvent fine-tuner sur du matériel grand public (par exemple, RTX 4090), contre le FullFT qui nécessite des clusters d'entreprise. Efficacité : LoRA converge souvent plus vite en raison de moins de variables.

#### d. Facilité de chargement et de transfert
« Avec moins de poids à stocker, les adaptateurs LoRA sont rapides et faciles à configurer ou à transférer entre les machines. »

- Les adaptateurs sont des fichiers de <100 Mo (contre des centaines de Go pour les modèles complets), compressables et partageables (par exemple, via GitHub ou le torrent).
- Déploiement : Charger la base une fois, échanger les adaptateurs en quelques secondes. La fusion est optionnelle pour la permanence.
- **Cas particuliers** : Contrôle de version (par exemple, Git pour les adaptateurs), apprentissage fédéré (entraîner les adaptateurs sur l'appareil, envoyer seulement les deltas), ou réglage itératif (empiler plusieurs LoRA).

### Implications plus larges et limites
- **Pourquoi LoRA domine** : C'est simple, efficace et s'intègre parfaitement (par exemple, dans la bibliothèque PEFT). Utilisé dans des modèles comme les fine-tunes de Stable Diffusion ou Alpaca (Llama avec réglage d'instructions).
- **Limites** : Pas toujours aussi performant que le FullFT sur des tâches très spécifiques ; le choix du rang r est important (trop faible sous-apprend, trop élevé gaspille l'efficacité). Ne gère pas tous les types de mises à jour (par exemple, les changements architecturaux).
- **Tendances futures** : Des extensions comme DoRA (décompose davantage les poids) ou VeRA (basé sur des vecteurs, encore plus épars). À mesure que les modèles passent à l'échelle de 10T+ de paramètres, PEFT/LoRA devient essentiel pour la durabilité.

Ce texte encapsule un changement pivotal dans l'IA : du réentraînement complet gourmand en ressources aux mises à jour modulaires et élégantes. Si vous souhaitez des dérivations mathématiques, des exemples de code (par exemple, en PyTorch) ou des plongées dans des articles connexes, faites-le moi savoir !