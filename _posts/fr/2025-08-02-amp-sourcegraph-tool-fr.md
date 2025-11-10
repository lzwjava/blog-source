---
audio: false
generated: true
image: false
lang: fr
layout: post
title: 'Amp : Outil de Codage IA Avancé'
translated: true
type: note
---

Amp de Sourcegraph est un outil de codage agentique conçu pour maximiser les capacités des modèles d'IA avancés pour les développeurs. Voici ce qui le rend spécial :

- **Utilisation illimitée des tokens** : Contrairement aux autres outils de codage IA qui limitent l'utilisation des tokens, Amp utilise les meilleurs modèles (comme Claude Sonnet 4) sans restrictions, permettant une génération de code de haute qualité et l'exécution de tâches complexes. Cela le rend rentable pour un travail de développement sérieux.[](https://ampcode.com/manual)[](https://www.stackhawk.com/blog/secure-code-with-amp-by-sourcegraph/)

- **Intégration transparente** : Amp fonctionne comme une extension VS Code (compatible avec les forks comme Cursor, Windsurf et VSCodium) et un outil CLI, s'intégrant aux workflows existants sans nécessiter une nouvelle interface utilisateur. Il prend en charge les serveurs proxy et les certificats personnalisés pour les environnements d'entreprise.[](https://ampcode.com/manual)[](https://www.npmjs.com/package/%40sourcegraph/amp)

- **Collaboration multijoueur** : Amp permet le partage de threads et propose des tableaux de classement, permettant aux équipes de collaborer, de réutiliser des workflows efficaces et de suivre l'adoption. Cela favorise le travail d'équipe et améliore la productivité.[](https://sourcegraph.com/amp)[](https://ampcode.com/manual)

- **Gestion du contexte** : Amp sélectionne intelligemment les extraits de code pertinents pour le contexte, évitant une utilisation gonflée des tokens tout en s'assurant que l'IA dispose de suffisamment d'informations pour générer un code précis. C'est un différenciateur clé par rapport à des outils comme l'ancien produit de Sourcegraph, Cody, qui récupérait des bases de code entières.[](https://zoltanbourne.substack.com/p/early-preview-of-amp-the-new-ai-coding)[](https://www.reddit.com/r/cursor/comments/1kpin6e/tried_amp_sourcegraphs_new_ai_coding_agent_heres/)

- **Fonctionnalités de sécurité** : Amp inclut une liste d'autorisation de commandes pour contrôler les commandes CLI que l'IA peut exécuter, stockée dans les paramètres du projet, et une occultation automatique des secrets pour empêcher l'exposition de données sensibles. Il prend également en charge les politiques de non-rétention pour les utilisateurs enterprise.[](https://zoltanbourne.substack.com/p/early-preview-of-amp-the-new-ai-coding)[](https://ampcode.com/security)

- **Automatisation puissante** : Amp gère le raisonnement autonome, l'édition de code complète et les tâches complexes, rapportant écrire 70 à 80 % du code pour certains utilisateurs. Des fonctionnalités comme la mise à jour des "To-Do's" fournissent un suivi en direct de la progression, améliorant l'expérience utilisateur.[](https://ainativedev.io/news/sourcegraphs-amp-dropped)[](https://medium.com/%40jonathanaraney/1-month-with-amp-vs-1-year-with-cursor-15572fca36ee)

- **Orientation entreprise** : Amp Enterprise propose l'authentification unique, des remises sur volume et des paiements par facture pour les gros achats, le rendant adapté aux organisations. Il est conçu pour évoluer avec le développement accéléré par l'IA tout en s'intégrant à des outils de sécurité comme StackHawk pour les tests de vulnérabilité.[](https://sourcegraph.com/pricing)[](https://www.stackhawk.com/blog/secure-code-with-amp-by-sourcegraph/)

- **Éloges de la communauté** : Les développeurs soulignent la vitesse, la précision et la capacité d'Amp à accomplir des tâches efficacement, surpassant souvent les concurrents comme Cursor ou Claude Code. Les utilisateurs apprécient son accent sur des résultats de qualité et une expérience utilisateur réfléchie, comme la fonctionnalité "To-Do's".[](https://sourcegraph.com/amp)[](https://ampcode.com/)

Cependant, certains utilisateurs notent que sa tarification basée sur les crédits peut être coûteuse, les coûts étant liés à l'utilisation des LLM et à des outils supplémentaires comme la recherche web. Par exemple, un utilisateur a rapporté avoir dépensé 4 $ pour 2 000 lignes de code.[](https://www.reddit.com/r/ClaudeAI/comments/1ll0kow/sourcegraph_cody_discontinued_replaced_by_cody/)

Amp est disponible sur ampcode.com avec 10 $ de crédits gratuits à l'inscription (plus 30 $ supplémentaires pour les utilisateurs Enterprise Starter). Pour les détails de tarification, visitez https://x.ai/grok ou contactez amp-billing-help@sourcegraph.com.[](https://ampcode.com/manual)[](https://sourcegraph.com/blog/changes-to-cody-free-pro-and-enterprise-starter-plans)