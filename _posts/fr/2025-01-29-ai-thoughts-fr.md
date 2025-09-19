---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Flux de travail IA, éditeurs de code et perturbation des plateformes
translated: true
---

### Table des matières

1. [Réflexions sur l'IA](#réflexions-sur-lia)  
   - L'IA manque d'intelligence ou de profondeur réelle  
   - Le machine learning est du calcul appliqué avancé  
   - Les LLM ont du mal avec les formats de fichiers structurés  
   - L'open source élimine le secret technologique  
   - Les outils basés sur le texte seront les premiers perturbés par l'IA  

2. [Nouvelles plateformes alimentées par des flux de travail IA](#nouvelles-plateformes-alimentées-par-des-flux-de-travail-ia)  
   - Les flux de travail IA automatisent la génération de contenu multilingue  
   - Les utilisateurs soumettent des invites pour la conversion de formats  
   - Les plateformes permettent l'amélioration et la synthétisation du contenu  
   - Flux de travail IA personnalisables via des paramètres de mots-clés  
   - L'IA gère la transformation du contenu de bout en bout  

3. [La prochaine orientation des éditeurs de code IA](#la-prochaine-orientation-des-éditeurs-de-code-ia)  
   - L'intégration cloud est cruciale pour les flux CI/CD  
   - Les tests A/B améliorent le contenu généré par l'IA  
   - Le RLHF s'étend aux retours de déploiement réel  
   - Les retours humains améliorent les sorties imparfaites de l'IA  
   - L'optimisation des invites est préférable à la correction des sorties  

---

## Réflexions sur l'IA  

*Dernière mise à jour en août 2025*  

- Satya Nadella a mentionné le paradoxe de Jevons. Cela vaut la peine d'être étudié.  

- Yin Wang : Il n'y a pas « d'intelligence » dans l'intelligence artificielle, pas de « neural » dans les réseaux de neurones, pas d'« apprentissage » dans le machine learning, et pas de « profondeur » dans l'apprentissage profond. Ce qui fonctionne vraiment dans ce domaine s'appelle le « calcul ». Je préfère donc appeler ce domaine « calcul différentiable », et le processus de construction de modèles « programmation différentiable ».  

- Yin Wang : Le machine learning est une théorie vraiment utile, voire belle, car ce n'est que du calcul revisité ! C'est la théorie ancienne et grande de Newton et Leibniz, sous une forme plus simple, élégante et puissante. Le machine learning consiste essentiellement à utiliser le calcul pour dériver et ajuster certaines fonctions, et l'apprentissage profond est l'ajustement de fonctions plus complexes.  

- Actuellement, les grands modèles de langage ne peuvent pas filtrer par langage de fichier comme YAML ou Python. Une grande partie des informations dans le monde réel est pourtant organisée ainsi. Cela signifie que nous pourrions entraîner des LLMs avec des fichiers.  

- Pour l'entraînement des LLMs, nous pourrions développer un système trouvant des correspondances exactes. Peut-être combiner l'algorithme de recherche KMP (Knuth-Morris-Pratt) avec l'architecture des transformers pour améliorer les capacités de recherche.  

- Il n'y a pas de secrets technologiques. L'open source révélera tous les secrets jalousement gardés.  

- L'IA affectera de nombreux outils, y compris indirectement. Certains disent qu'ils n'auront plus besoin de Figma pour dessiner des prototypes, mais qu'ils iront directement au code. Postman subira le même sort ; les gens utiliseront directement Python ou d'autres scripts pour appeler ou tester des API.  

- Une raison pour laquelle nous n'utiliserons pas Postman ou Figma à l'ère de l'IA est que leurs fonctionnalités ne peuvent pas être générées par du texte. Ils n'ont pas non plus de raccourci comme commande + K pour remplacer des composants.  

- Les interfaces utilisateur deviennent un obstacle à l'ère de l'IA. Pourquoi améliorer Postman pour tester des applications avec l'IA quand nous pouvons directement utiliser la bibliothèque requests de Python ou d'autres langages, qui seront eux-mêmes alimentés par l'IA ?  

- Pourquoi améliorer Figma pour créer des interfaces avec l'IA quand la génération d'interfaces par code, renforcée par l'IA, offre une approche plus directe et potentiellement plus puissante ?  

- Les LLM changeront d'abord les applications liées au texte, comme Google, les moteurs de recherche, les éditeurs de texte, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo et Feedly.  

- En revanche, les LLM ne révolutionneront pas des technologies comme Git, Linux, ffmpeg, les téléphones, le matériel, les navigateurs, les systèmes d'exploitation ou les appels vocaux et vidéo. Ces technologies sont centrées sur le code, qui n'est pas facilement généré par l'IA, contrairement aux outils de test d'API comme Postman.  

- Les technologies comportant beaucoup de code sont difficiles à révolutionner par l'IA, comme OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC, Qt, LLVM/Clang et GNOME. Si l'IA pouvait aider à concevoir ces technologies, elles ne seraient pas remplacées. L'IA devrait aider à créer de meilleures technologies, mais cela nécessitera plus de puissance de calcul pour générer une quantité équivalente de code.  

- Les LLM peuvent agir de deux manières : en modifiant le contenu ou les données d'une plateforme (ex. : traduction dans TikTok), ou en remplaçant directement des logiciels (ex. : Postman ou Google Search).  

- Les outils audio IA peuvent aussi agir de deux manières : en modifiant le contenu (ex. : génération de livres audio pour Audible) ou en remplaçant des logiciels (ex. : les applis de chant, car l'IA permet désormais de chanter facilement).  

- Pour mesurer l'impact de l'IA, on peut évaluer quelle quantité de données ou de code peut être générée ou améliorée par l'IA, partiellement ou entièrement. L'IA peut aussi aider à inventer de nouveaux logiciels.  

- Il existe trois types de produits : les produits d'IA générative, ceux utilisant leurs API, et les autres.  

- Une idée : utiliser l'IA pour accumuler en temps réel des informations, actualités ou tendances de plateformes comme Reddit, GitHub Trending, Twitter Trending, Quora et Zhihu. Les utilisateurs pourraient personnaliser leur flux avec des invites.  

- Il existe cinq types de données clés : texte, image, audio, vidéo et code.  

- D'autres types importants incluent les données numériques, géospatiales, biométriques, de capteurs, transactionnelles, métadonnées, séries temporelles, structurées, non structurées, semi-structurées, de santé, environnementales, de logs, réseau et comportementales.  

- Google reste meilleur pour l'indexation des sites, surtout pour télécharger un logiciel ou un document depuis un site spécifique. Cela fonctionne comme une recherche par domaine. Les LLM n'ont pas nécessairement les derniers liens de téléchargement.  

- Google reste utile pour la recherche d'images, tandis que les LLM excellent en génération de texte. Les gens préfèrent souvent des images réelles pour vérifier des détails matériels, dimensions, formes ou apparences.  

- Les chatbots IA sont populaires car le texte est plus difficile à traiter que les images. Mais la génération d'images IA a un potentiel inexploité : demander différents angles, zooms sur des visages ou des circuits. Comme les gens travaillent surtout avec du texte, les outils d'image IA ont une grande marge de progression.  

- L'IA excelle à expliquer des concepts et faciliter la compréhension. Les utilisateurs peuvent poser des questions sur n'importe quel détail, ce qui est probablement son utilité la plus significative.  

- J'ai utilisé l'IA pour apprendre les LLM. Le moment où elle m'a aidé à comprendre K, Q et V était merveilleux.  

- Depuis l'arrivée des LLM, je préfère Ubuntu car les nombreuses applications colorées de macOS m'intéressent moins. Je préfère tout faire via le terminal et le texte.  

- L'IA peut être évaluée par sa capacité à mettre à jour un fichier pom.xml ou requirements.txt, à actualiser des bibliothèques et à effectuer des vérifications. Ce processus peut être complexe.  

- À l'ère de l'IA, les langages performants et robustes gagneront en popularité, tandis que la syntaxe importera moins. Les LLM aideront à générer du code, réduisant la gêne tant que le programme s'exécute bien.  

- Les gens ont tendance à tout lire depuis les chatbots IA car c'est facile à apprendre, les réponses sont cohérentes et de haute qualité.  

- Mais l'information ne se limite pas au texte. Vous pouvez lire la plupart des textes via les chatbots, mais vous perdez le site original, sa mise en page, ses images et son design.  

- Les sites très interactifs (ex. : jeux web, Google Docs, Google Sheets, Zoom, Slack) ne seront pas fortement impactés par l'IA. Ils sont centrés sur le code, pas seulement sur le texte.  

- Il est facile de faire des fautes de frappe ou de mal formuler des invites pour les chatbots. C'est pourquoi une banque numérique ou un réseau social entièrement piloté par l'IA avec une simple boîte de chat ne fonctionne souvent pas. Les boutons, la navigation et les mises en page traditionnelles sont plus pratiques.  

- [Comment je vis bien à l'ère de l'IA et de la blockchain](./ai-blockchain-fr)  

---  

## Nouvelles plateformes alimentées par des flux de travail IA  

*08.01.2025*  

- Les flux de travail sont des systèmes où les LLM et outils sont orchestrés via des chemins de code prédéfinis.[^1]  

- Imaginez une nouvelle plateforme comme TikTok, Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit ou YouTube, entièrement alimentée par la traduction IA.  

- Chaque publication ou réponse est sauvegardée dans une seule langue. La plateforme traduira automatiquement le contenu dans 20 langues, selon la préférence de l'utilisateur.  

- Outre la traduction, d'autres fonctionnalités IA (synthétisation, génération audio/vidéo) joueront un rôle clé. L'utilisateur fournit le contexte, la plateforme s'occupe du reste.  

- Les utilisateurs peuvent uploader du texte, images, audio ou vidéo, et la plateforme les convertira automatiquement dans d'autres formats.  

- Les plateformes peuvent générer automatiquement des résumés, avec différents types disponibles en plusieurs langues.  

- Sur n'importe quel contenu, l'IA peut aider à générer, améliorer, corriger, synthétiser, étendre, convertir ou imaginer de nouvelles formes.  

- Les utilisateurs peuvent personnaliser la plateforme avec des mots-clés comme « anglais » ou « drôle » pour ajuster le style des flux IA.  

---  

[^1]: Building Effective Agents, [Anthropic](https://www.anthropic.com/research/building-effective-agents)  

---  

## La prochaine orientation des éditeurs de code IA  

*08.01.2025*  

Récemment, j'ajoutais un pipeline `xelatex` à GitHub Actions.  

J'ai rencontré un problème avec le package `fontawesome5`. La solution suggérée par 4o-mini (installer TeX Live 2021 avec `tlmgr install fontawesome5`) n'a pas fonctionné. Cependant, 4o a proposé une meilleure approche : passer à TeX Live 2023 et utiliser `tlmgr`. Bien que cela n'ait pas tout résolu, cela a amélioré la situation.  

J'ai utilisé ChatGPT pour comprendre le problème. Pour plus de détails, voir [Ce que ChatGPT O1 peut faire que 4o-mini ne peut pas](./o1-fr).  

Je n'ai pas utilisé d'éditeurs comme Cursor ou Windsurf ici, bien que je les aie testés sur un autre projet. Leur limite est de ne capturer que les sorties locales, restreignant leur utilité dans les environnements cloud.  

Dans des flux comme GitHub Actions ou Jenkins, les éditeurs doivent mieux s'intégrer au cloud et aux processus CI/CD.  

Cette intégration s'applique aussi aux outils de création de contenu (texte, images, audio, vidéo). Ils devraient être couplés à des systèmes de tests A/B. Les outils IA génèrent du contenu, et les tests A/B fournissent des retours, comme dans le Reinforcement Learning from Human Feedback (RLHF), où les modèles s'améliorent grâce aux retours réels.  

Étendre le RLHF au-delà des sorties de modèles, vers les environnements de test et déploiement réels, semble une direction prometteuse pour les éditeurs et outils de création IA.  

Les tests peuvent être instantanés ou longs, automatisés ou assistés par des humains. Si automatisés (ex. : tests A/B pour un outil IA), le processus inclut toujours des retours humains, mais de manière automatisée. Par exemple, l'ordinateur peut vérifier les résultats quotidiennement pour améliorer le processus.  

Si des humains interviennent, leurs retours sont souvent vagues. Par exemple, pour des images ou vidéos générées, les humains peuvent dire que ce n'est « pas assez drôle » ou qu'un détail doit être amélioré. La perfection dépend du goût individuel, et les retours humains restent essentiels.  

En théorie, toutes les règles définies par l'homme peuvent être écrites sous forme d'invites. Il y a des invites utilisateur et système. Mieux vaut améliorer les invites que corriger les sorties à chaque fois.