---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Analyse de la Stack Technique du Blog de Yin Wang
translated: true
type: note
---

Le site web (https://www.yinwang.org/, intitulé "当然我在扯淡") semble être un blog personnalisé. D'après le code source HTML fourni :

- **Framework** : Il est principalement construit avec **Vue.js** (probablement la version 3), comme en témoignent les attributs spécifiques à Vue comme `data-v-app`, `data-v-[hash]` pour le CSS scopé, et les références aux composants (par exemple, `HomeView`, `PostView`, `router-link-active` pour la gestion de la navigation par Vue Router).
- **Outil de build** : **Vite** est utilisé pour le bundling et le développement, comme le montre le favicon (`/vite.svg`), les scripts préchargés avec des noms de fichiers hashés (par exemple, `/assets/index-DS_1rR7p.js`), et la structure globale des assets typique de la sortie de Vite.
- **Stylisation** : **Tailwind CSS** pour les classes utilitaires (par exemple, `bg-gray-50 dark:bg-gray-900`, `flex items-center`, préfixes responsives comme `sm:px-4`).
- **Autres remarques** : Aucun indicateur de rendu côté serveur (par exemple, pas de traces de Nuxt.js), c'est donc probablement un site statique ou une SPA rendue côté client. Le contenu (articles, tags, pagination) suggère une configuration personnalisée simple pour un blog personnel, utilisant possiblement Markdown pour le contenu des articles.

Il **n'est pas entièrement écrit manuellement** — le HTML est généré automatiquement pendant le processus de build à partir des composants et templates Vue. La logique principale (routing, composants) est codée en JS/TS, mais la sortie finale est constituée de fichiers statiques optimisés. Aucune preuve d'un générateur de site statique complet comme Hugo ou Jekyll ; il s'agit davantage d'un projet Vue + Vite léger.

[当然我在扯淡](https://www.yinwang.org/)