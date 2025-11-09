---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Désactivation des citations de recherche web de LibreChat
translated: true
type: note
---

## Désactivation des citations dans le mode recherche web de LibreChat

La fonction de recherche web de LibreChat (alimentée par des fournisseurs comme Serper.dev ou SearxNG, combinée à des scrapeurs comme Firecrawl) inclut automatiquement des citations dans les réponses pour créditer les sources et améliorer la transparence. D'après la documentation officielle et les discussions communautaires, il n'existe pas de bouton intégré accessible à l'utilisateur pour désactiver spécifiquement les citations de la recherche web au niveau individuel. Cependant, vous pouvez y parvenir ou vous en approcher via des modifications de configuration, principalement pour les administrateurs ou les auto-hébergeurs. Voici comment :

### 1. **Configuration au niveau administrateur (Approche recommandée)**
   Si vous exécutez votre propre instance de LibreChat (auto-hébergée), modifiez les fichiers de configuration pour limiter ou supprimer le rendu des citations. Les citations sont gérées via l'interface et les composants de recherche.

   - **Modifier `librechat.yaml` pour les paramètres de l'Interface** :
     LibreChat utilise un fichier YAML pour les paramètres globaux. Cherchez la section `interface`, qui contrôle la visibilité des citations (s'inspirant des contrôles de citations de fichiers, qui peuvent s'étendre au rendu de l'interface de recherche web).
     - Définissez `fileCitations` sur `false` pour désactiver globalement les autorisations de citations. Bien que ce soit explicitement pour les recherches de fichiers, cela peut influencer le rendu de l'interface de recherche web dans certaines configurations.
       ```yaml
       interface:
         fileCitations: false  # Désactive l'affichage des citations pour les recherches en général
       ```
     - Pour la recherche web spécifiquement, dans la section `webSearch`, vous pouvez désactiver ou personnaliser les fournisseurs pour éviter les liens sources détaillés :
       ```yaml
       webSearch:
         enabled: true  # Garder activé, mais ajuster les fournisseurs
         serper:  # Ou votre fournisseur
           enabled: true
           # Pas de drapeau 'citations' direct, mais omettre les clés API pour les scrapeurs comme Firecrawl réduit les extraits/citations détaillés
         firecrawl:
           enabled: false  # Désactive le scraping de contenu, qui génère souvent des citations
       ```
     - Redémarrez votre instance LibreChat après les modifications. Source pour la configuration de l'interface : [LibreChat Interface Object Structure](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface)[1].

   - **Variables d'environnement (Fichier .env)** :
     Dans votre fichier `.env`, désactivez les modes debug ou journalisation qui pourraient imposer des citations, ou définissez la recherche web sur un fournisseur minimal.
     - Exemple :
       ```
       DEBUG_PLUGINS=false  # Réduit la sortie verbeuse, y compris les citations
       SERPER_API_KEY=your_key  # Utiliser un fournisseur de recherche basique sans scraping pour moins de citations
       FIRECRAWL_API_KEY=  # Laisser vide pour désactiver le scraper (pas d'extraits de page/citations)
       ```
     - Cela fait passer les réponses à des résultats de recherche résumés uniquement, sans citations intégrées. Configuration complète : [LibreChat .env Configuration](https://www.librechat.ai/docs/configuration/dotenv)[2].

   - **Personnalisation du fournisseur de recherche web** :
     Passez à un fournisseur comme SearxNG, qui peut être configuré côté serveur pour omettre les liens sources.
     - Définissez `SEARXNG_INSTANCE_URL=your_minimal_searxng_url` dans `.env`.
     - Dans votre instance SearxNG, modifiez ses paramètres pour supprimer les métadonnées des résultats (par exemple, via `settings.yml` dans SearxNG : désactivez `reveal_version: false` et personnalisez les modèles pour supprimer les liens).
     - Documentation : [Web Search Configuration](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search)[3].

### 2. **Solutions de contournement au niveau utilisateur (Sans accès administrateur)**
   Si vous utilisez un LibreChat hébergé (par exemple, une instance publique), les options sont limitées car les citations sont souvent imposées pour la précision :
   - **Ingénierie de prompt** : Donnez des instructions explicites à l'IA dans vos messages, par exemple, "Recherche sur le web mais n'inclut pas de citations ou de sources dans ta réponse." Cela fonctionne de manière inconstante car l'outil de recherche peut toujours les ajouter, mais de nombreux modèles se conformeront partiellement.
   - **Désactiver complètement la recherche web** : Si les citations sont le principal problème, désactivez la recherche web par conversation :
     - Dans l'interface de chat, évitez de cliquer sur le bouton "Web Search".
     - Pour les agents : Lors de la création/édition d'un agent, supprimez la capacité `web_search` dans la configuration de l'agent (via l'interface Agents). Source : [Agents Documentation](https://www.librechat.ai/docs/features/agents)[4].
     - Demandez aux administrateurs d'ajouter un bouton ; les discussions communautaires suggèrent cela comme une demande de fonctionnalité (par exemple, [GitHub Discussion on Web Search Toggle](https://github.com/danny-avila/LibreChat/discussions/7738)[5]).

### 3. **Limitations et Notes**
   - Les citations sont un élément central de la recherche web pour garantir une utilisation éthique de l'IA et une traçabilité, donc les désactiver complètement pourrait nécessiter des modifications de code personnalisées (par exemple, modifier les composants frontend comme `WebSearchResults.jsx` dans le repo GitHub pour masquer les éléments de citation).
   - Aucun drapeau direct "désactiver les citations" n'existe dans les versions actuelles (à partir d'octobre 2025). Vérifiez les mises à jour dans la [Web Search Feature Docs](https://www.librechat.ai/docs/features/web_search)[6], car les fonctionnalités évoluent.
   - Si vous êtes en auto-hébergement, testez les modifications dans un environnement de développement — désactiver les scrapeurs pourrait réduire la qualité des réponses.
   - Les retours de la communauté (par exemple, Reddit) notent des bugs occasionnels avec les fonctionnalités de recherche, mais rien de spécifique aux citations : [Reddit Thread on LibreChat Issues](https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/)[7].

Pour un support officiel, rejoignez le Discord LibreChat ou ouvrez un issue GitHub avec les détails de votre configuration. Si cela ne résout pas le problème, fournissez plus de contexte sur votre version de LibreChat ou votre méthode d'hébergement !

Citations :
[1] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface
[2] https://www.librechat.ai/docs/configuration/dotenv
[3] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search
[4] https://www.librechat.ai/docs/features/agents
[5] https://github.com/danny-avila/LibreChat/discussions/7738
[6] https://www.librechat.ai/docs/features/web_search
[7] https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/