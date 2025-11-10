---
audio: false
generated: true
image: false
lang: fr
layout: post
title: 'Outils d''IA locaux : Obstacles à l''adoption'
translated: true
type: note
---

### Pourquoi peu de gens utilisent Ollama pour exécuter des modèles d'IA locaux (et des interfaces comme Open-WebUI pour discuter)

Ollama est un outil open-source populaire pour exécuter de grands modèles de langage (LLM) localement sur votre machine, permettant une utilisation de l'IA axée sur la confidentialité ou hors ligne. Open-WebUI est une interface web auto-hébergée qui s'associe à Ollama (ou à des backends similaires) pour offrir une expérience de discussion similaire à ChatGPT. Bien que ces outils aient gagné en traction auprès des passionnés de technologie et des développeurs, leur adoption reste limitée pour le grand public. Sur la base de discussions, d'avis et d'analyses d'utilisateurs, voici les principales raisons pour lesquelles peu de gens les utilisent largement :

- **Exigences matérielles élevées** : Exécuter des LLM performants localement demande une puissance de calcul importante, telle qu'un GPU puissant avec au moins 16 Go de VRAM (par exemple, la série NVIDIA RTX) et 32 Go+ de RAM système. La plupart des utilisateurs quotidiens ont des ordinateurs portables ou de bureau standard qui ne peuvent pas gérer les grands modèles sans ralentissements sévères ou plantages. Par exemple, les modèles quantifiés (comprimés pour une utilisation locale) nécessitent toujours des mises à niveau matérielles coûteuses, et sans elles, les performances sont inutilisables pour quoi que ce soit au-delà des tâches de base. Cela les rend inaccessibles pour les non-joueurs ou les utilisateurs occasionnels.

- **Performances plus lentes et moins fiables** : Les modèles locaux sont souvent quantifiés (réduits en précision) pour tenir sur du matériel grand public, ce qui conduit à des résultats inférieurs par rapport aux services cloud comme ChatGPT ou Grok. Ils peuvent être lents (10 à 30 secondes par réponse contre des réponses cloud quasi instantanées), sujets aux erreurs, aux hallucinations, aux sorties répétitives et à un faible suivi des instructions. Des tâches comme le codage, les mathématiques ou le traitement de longs documents échouent fréquemment, car les modèles locaux (par exemple, les versions à 32B paramètres) sont beaucoup plus petits et moins capables que les modèles cloud massifs (des centaines de milliards de paramètres).

- **Complexité de configuration et technique** : Bien que l'installation de base d'Ollama soit simple, l'optimiser pour de bons résultats implique de modifier des paramètres comme les fenêtres de contexte (la valeur par défaut est souvent trop faible à 2k-4k tokens, ce qui fait "oublier" le prompt au modèle), la mise en œuvre d'extensions comme le RAG (Retrieval-Augmented Generation) pour une meilleure précision, ou la gestion des niveaux de quantification. Open-WebUI ajoute une autre couche, nécessitant souvent Docker, la configuration des ports et le dépannage. Il manque des guides complets et adaptés aux débutants, ce qui entraîne de la frustration. De nombreux utilisateurs signalent rencontrer des bugs, des problèmes de mémoire ou avoir besoin de compétences en ligne de commande, ce qui dissuade les personnes non techniques.

- **Commodité des alternatives cloud** : Des services comme OpenAI, Google Gemini ou Grok sont prêts à l'emploi — aucun téléchargement, aucun souci matériel, et toujours disponibles avec une vitesse et une intelligence supérieures. Pour discuter ou pour la productivité, pourquoi se préoccuper d'une configuration locale lorsque les options cloud sont gratuites ou peu coûteuses (par exemple, 0,005 $ pour 100k tokens) et gèrent mieux les requêtes complexes ? Les outils locaux excellent pour la confidentialité ou l'utilisation hors ligne, mais la plupart des gens privilégient la facilité par rapport à ces avantages.

- **Sur-enthousiasme et déception** : Les médias sociaux et YouTube présentent souvent les modèles locaux comme des "tueurs de ChatGPT", mais les tests en conditions réelles montrent d'importants écarts de qualité. Par exemple, les modèles locaux ont du mal avec des benchmarks simples (par exemple, compter les lettres dans un mot) que les modèles cloud réussissent parfaitement. Cela conduit les utilisateurs à essayer Ollama, à être déçus et à revenir en arrière. Open-WebUI aide avec une interface plus agréable, mais ne corrige pas les limitations sous-jacentes des modèles.

- **Cas d'utilisation limités pour la plupart des gens** : Les configurations locales sont excellentes pour les développeurs qui conçoivent des agents, pour les tâches sensibles à la confidentialité (par exemple, traiter des données confidentielles) ou pour les scénarios hors ligne. Cependant, pour discuter quotidiennement, faire des recherches ou s'amuser, elles sont excessives et sous-performent. Des problèmes comme la prise en charge de modèles obsolètes dans Ollama ou une mauvaise intégration d'outils limitent encore plus leur attrait.

En résumé, bien qu'Ollama et Open-WebUI responsabilisent les utilisateurs avancés, les barrières matérielles, de performance et d'effort les rendent niche. À mesure que le matériel s'améliore et que les modèles deviennent plus efficaces, l'adoption pourrait croître, mais pour l'instant, les services cloud dominent par leur simplicité et leur puissance.

### Références
- [Why Are All Local AI Models So Bad? No One Talks About This!](https://www.reddit.com/r/ollama/comments/1idqxto/why_are_all_local_ai_models_so_bad_no_one_talks/)
- [Why I Stopped Using Ollama and Local Models (And Switched Back to OpenAI)](https://medium.com/@Shamimw/why-i-stopped-using-ollama-and-local-models-and-switched-back-to-openai-2d125f303e1c)
- [Just Wanted to Run a Large AI Model, But It Turned Out Not So Simple](https://medium.com/@rifewang/just-wanted-to-run-a-large-ai-model-but-it-turned-out-not-so-simple-a6701823c4e4)
- [DT4 - AI - Ollama for local LLM - Recommendations?](https://discourse.devontechnologies.com/t/dt4-ai-ollama-for-local-llm-recommendations/82597)
- [Local AI on M-Chip Macbooks?](https://forum.level1techs.com/t/local-ai-on-m-chip-macbooks/220407)
- [Does anyone have a video or written article that would get one up to ...](https://news.ycombinator.com/item?id=40977760)
- [How to get CrewAI to properly use Ollama models](https://community.crewai.com/t/how-to-get-crewai-to-properly-use-ollama-models/5117)