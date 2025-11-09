---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'Transformateurs : Origines, Conception et Avenir'
translated: true
type: note
---

### Résumé de « How I Learned to Stop Worrying and Love the Transformer » par Ashish Vaswani

Cette conférence de 45 minutes, donnée le 7 novembre 2023 dans le cadre de la série CS25 Transformers United de Stanford, est une plongée réflexive dans les origines, la conception, l'évolution et l'avenir de l'architecture Transformer. En tant que co-auteur du papier fondateur de 2017 « Attention Is All You Need », Vaswani partage des anecdotes personnelles de son passage chez Google Brain, démystifie des décisions clés et offre des visions optimistes mais réalistes pour la prochaine phase de l'IA. Elle est structurée autour du contexte historique, des innovations fondamentales, des avancées post-Transformer et d'idées prospectives—parfaite pour comprendre pourquoi les Transformers sont devenus la colonne vertébrale de l'IA moderne.

#### Contexte historique et l'étincelle des Transformers
Vaswani commence par un hommage à la Conférence de Dartmouth de 1956, où les pionniers de l'IA rêvaient d'une machine unifiée imitant l'intelligence humaine à travers la vision, le langage, et plus—utilisant des systèmes basés sur des règles et anticipant des victoires rapides. Soixante-dix ans plus tard : malgré les hivers de l'IA, nous y revenons avec les Transformers alimentant des modèles multimodaux. Il oppose cela au TAL des années 2000, qui était un patchwork désordonné de pipelines pour des tâches comme la traduction automatique (par exemple, les alignements de mots, l'extraction de phrases, le re-score neuronal). En 2013, le domaine était fragmenté en silos comme l'analyse de sentiments ou le dialogue, avec des progrès alimentés par le financement plutôt que par une théorie unifiée.

Le point de basculement ? Les représentations distribuées (par exemple, « king - man + woman ≈ queen » de word2vec) et les modèles seq2seq (2014–2015), qui ont regroupé des tâches diverses dans des frameworks encodeur-décodeur. Mais les réseaux récurrents comme les LSTMs étaient un calvaire : le traitement séquentiel tuait le parallélisme, les états cachés créaient un goulot d'étranglement pour l'information, et les dépendances à longue distance étaient faibles. Les convolutions (par exemple, ByteNet, ConvS2S) ont aidé pour la vitesse mais ont buté sur les connexions distantes.

**Anecdote interne :** En travaillant sur Google Neural Machine Translation (GNMT) en 2016, l'équipe de Vaswani a abandonné les pipelines pour des LSTMs purs, atteignant l'état de l'art avec des données massives. Pourtant, les LSTMs semblaient « frustrants »—lents sur les GPU, difficiles à mettre à l'échelle. Le « déclic » fut le désir d'un parallélisme total : encoder les entrées et décoder les sorties sans la corvée étape par étape. Les premiers rêves non-autorégressifs (tout générer d'un coup, puis raffiner) ont échoué parce que les modèles ne pouvaient pas apprendre l'ordre sans un guidage gauche-droite, qui élimine naturellement les chemins improbables.

#### Choix de conception fondamentaux : Construire le Transformer original
Les Transformers ont abandonné la récurrence et les convolutions pour de l'attention pure, permettant des conversations directes de token à token via la similarité de contenu—comme extraire des patches d'image similaires dans les tâches de vision (par exemple, le débruitage non-local means). L'auto-attention est invariante par permutation mais adaptée au parallélisme, avec une complexité O(n² d) qui est un atout pour les GPU lorsque les séquences ne sont pas infinies.

Blocs de construction clés :
- **Attention Scaled Dot-Product :** Projections Q, K, V des entrées ; scores sous forme de softmax(QK^T / √d_k) pondéré sur V. Mis à l'échelle pour éviter les gradients disparaissants (en supposant une variance unitaire). Masquage causal pour les décodeurs empêche de regarder vers l'avant. Choisi plutôt que l'attention additive pour la vitesse des multiplications matricielles.
- **Attention Multi-Head :** Une seule tête moyenne trop (par exemple, brouille les rôles dans « le chat a léché la main »). Les têtes divisent les dimensions en sous-espaces—comme des machines de Turing multi-bandes—pour des sous-espaces focalisés (par exemple, une tête se verrouille sur une probabilité de 1 pour des spécificités). Aucun calcul supplémentaire, sélectivité de type convolution.
- **Encodage Positionnel :** Les sinusoïdes injectent l'ordre, visant les positions relatives (décomposables par distance). N'ont pas tout à fait appris les relations initialement, mais ont fonctionné.
- **Empliage et Stabilisation :** Emplis encodeur-décodeur avec des résiduels et de la normalisation de couche (pre-norm plus tard pour les réseaux plus profonds). Les feed-forwards étendent/contractent comme les ResNets. Encodeur : auto-attention ; Décodeur : auto-attention masquée + attention croisée.

Il a écrasé les benchmarks WMT avec 8x moins de flops que les ensembles de LSTMs, a généralisé pour le parsing, et a laissé entrevoir un potentiel multimodal. Interprétabilité ? Les têtes se sont spécialisées (certaines à longue portée, d'autres locales de type conv), mais Vaswani plaisante en disant que c'est « lire dans les feuilles de thé »—prometteur mais flou.

#### Évolution : Corrections et Victoires de la Mise à l'Échelle
Les Transformers ont « collé » parce qu'ils sont simples, mais des ajustements les ont amplifiés :
- **Positions 2.0 :** Les sinusoïdes échouaient sur les relations ; les embeddings relatifs (biais par paire) ont boosté la traduction/la musique. ALiBi (biais de distance appris) extrapole les longueurs ; RoPE (rotations mélangeant absolu/relatif) est maintenant roi—économise la mémoire, saisit bien les relations.
- **Contextes Longs :** Malédiction quadratique ? Fenêtres locales, motifs clairsemés (strided/global), hachage (Reformer), récupération (Memorizing Transformer), astuces low-rank. Flash Attention évite les écritures en mémoire pour la vitesse ; Multi-Query réduit les têtes KV pour l'inférence. Les gros modèles diluent de toute façon le coût de l'attention.
- **Autres Améliorations :** Le pre-norm stabilise ; le décodage spéculatif (brouillon rapide, vérification lente) imite la vitesse non-autorégressive en production.

**Pépite interne :** Bidouiller une attention relative efficace était de la « gymnastique matricielle », mais la physique du matériel (par exemple, les produits scalaires pour les accélérateurs) a guidé les choix.

#### Directions Futures : Au-Delà de la Mise à l'Échelle
Vaswani est optimiste : Les géants auto-supervisés permettent des agents in-context, faisant écho à la machine unifiée de Dartmouth. Les lois de l'échelle règnent, mais il faut surveiller les résurgences des RNN ou de meilleures architectures. Priorités :
- **Agents Multimodaux :** Prompt-programmer par milliers ; les outils comme ponts (internaliser les simples, collaborer sur les complexes).
- **Données & Infra :** Gains de 2x grâce à de meilleures données ; FP8/INT8 pour la bande passante, entraînement à l'échelle InfiniBand.
- **Intelligence Adaptative :** Petits modèles + planificateurs/représentations de données égalent les gros ; few-shot à l'inférence ; signalisation de l'incertitude ; construction de compétences (par exemple, bots Minecraft).
- **Magie Full-Stack :** Boucles de rétroaction pour les workflows (par exemple, l'analyse de données comme minage de « dark knowledge »).
- **Émergents :** Le grokking dans les jouets jusqu'aux mystères de GPT-4—étudier le petit pour comprendre le grand.
- **Systèmes :** La bande passante mémoire est le goulot d'étranglement ; récupération pour tout.

Il taquine sa startup avec le co-auteur Noam Shazeer : Automatiser les workflows à partir de l'analyse de données, full-stack pour la magie de la rétroaction. Des outils jusqu'à ce qu'il n'y ait plus que « des Transformers partout », en tirant parti de l'intelligence logicielle.

#### Points Forts du Q&R
Dans la discussion post-conférence :
- Obstacles non-autorégressifs : Nécessite un « ordonnancement oracle » pour l'indépendance ; les espaces latents aident mais la multi-modalité pose problème.
- Le Monde à partir du Texte : Les LLMs + RLHF extraient des planificateurs pour la robotique ; mélanger les données d'entraînement suscite une créativité « nouvelle ».
- Modularité : Le MoE induit des experts ; la coordination multi-agent (objectifs, mises à jour, vérifications) est clé.
- Conseil : Poursuivre la boucle fermée humain-IA ; le domaine est grand ouvert pour des surprises.

Intemporel—des vibrations historiques, de la profondeur technique, de l'inspiration sans battage médiatique. Si vous êtes dans l'IA, c'est un incontournable pour comprendre pourquoi les Transformers ont gagné.

[How I Learned to Stop Worrying and Love the Transformer (YouTube)](https://www.youtube.com/watch?v=1GbDTTK3aR4)