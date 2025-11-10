---
audio: false
generated: true
lang: fr
layout: post
title: 'Lunettes connectées de Meta : Fonctionnalités et API'
translated: true
type: note
---

Décortiquons l'offre de lunettes intelligentes de Meta, incluant Ray-Ban et Oakley, leur base d'utilisateurs et ce que leurs API offrent aux développeurs.

**Que sont les lunettes intelligentes Meta VR, Ray-Ban et Oakley ?**

Il est important de clarifier la terminologie. « Meta VR Glass » n'est pas un nom de produit spécifique largement utilisé par Meta. L'offre principale de réalité virtuelle et mixte de Meta est la gamme de casques **Meta Quest** (par exemple, le Meta Quest 3).

Lorsque les gens parlent de « lunettes Meta » dans un format plus général, semblable à des lunettes classiques, ils font généralement référence à :

*   **Les Lunettes Intelligentes Ray-Ban Meta :** Ce sont des lunettes intelligentes grand public développées en partenariat avec EssilorLuxottica (la société derrière Ray-Ban). Elles sont conçues pour ressembler à des lunettes de soleil Ray-Ban classiques et se concentrent sur des fonctionnalités comme :
    *   La capture photo et vidéo mains libres (avec une LED indicatrice visible pour le respect de la vie privée).
    *   Des haut-parleurs à conduction osseuse pour l'audio (musique, podcasts, appels).
    *   Des micros intégrés pour les appels et les commandes vocales (incluant « Hey Meta » pour Meta AI).
    *   Des capacités de diffusion en direct sur Facebook et Instagram.
    *   L'intégration avec Meta AI pour diverses tâches (par exemple, obtenir des informations, envoyer des messages, décrire l'environnement pour l'accessibilité).
    *   Aucun affichage intégré ou écran de réalité augmentée monté sur la tête (ce sont des « lunettes intelligentes », et non des lunettes de RA au sens typique du terme).

*   **Les Lunettes Intelligentes Oakley Meta (par exemple, Oakley Meta HSTN) :** Il s'agit d'une nouvelle gamme de « Lunettes IA Performance » développées en collaboration avec Oakley, qui fait également partie d'EssilorLuxottica. Elles partagent de nombreuses fonctionnalités avec les lunettes Ray-Ban Meta mais sont spécifiquement conçues pour les athlètes et la performance. Les aspects clés incluent :
    *   Une esthétique audacieuse et sportive typique d'Oakley.
    *   Une durabilité et une résistance à l'eau améliorées (IPX4).
    *   Une autonomie plus longue.
    *   Une caméra de plus haute résolution (vidéo 3K).
    *   L'intégration avec Meta AI, offrant des fonctionnalités adaptées aux athlètes (par exemple, demander les conditions de vent pour le golf).

**Combien d'utilisateurs ?**

En février 2025, les **Lunettes Intelligentes Ray-Ban Meta** se sont vendues à plus de **2 millions d'unités** depuis leur lancement en septembre 2023. EssilorLuxottica prévoit d'augmenter la capacité de production annuelle à 10 millions d'unités d'ici fin 2026, ce qui indique une forte demande et la conviction de Meta en l'avenir du produit.

Les **Lunettes Intelligentes Oakley Meta** sont une gamme de produits plus récente, les précommandes ayant commencé en juillet 2025. Par conséquent, les chiffres spécifiques d'utilisateurs pour les lunettes Oakley Meta ne sont pas encore disponibles, mais elles visent une présence significative sur le marché.

**Que fournissent leurs API aux développeurs ?**

Il est important de distinguer les API pour les casques VR/MR (comme le Meta Quest) et les lunettes intelligentes (comme les Ray-Ban Meta et Oakley Meta).

**Pour Meta Quest (casques VR/MR) :**

Meta fournit une plateforme de développement robuste pour son Meta Horizon OS (anciennement Quest OS), offrant diverses API et SDK pour créer des expériences immersives de réalité virtuelle et mixte. Les domaines clés pour les développeurs incluent :

*   **OpenXR :** Une norme pour créer des expériences XR haute performance, permettant aux développeurs de créer des applications VR/MR multiplateformes.
*   **Meta Horizon Worlds :** Des outils pour créer et façonner des expériences au sein de la plateforme de réalité virtuelle sociale de Meta.
*   **Applications Android :** Les développeurs peuvent rendre les applications Android existantes compatibles avec Meta Horizon OS et tirer parti de ses fonctionnalités spatiales uniques.
*   **Développement Web :** Concevoir et déployer des applications web 2D qui utilisent les capacités de multitâche du Quest.
*   **Meta Spatial SDK :** Conçu pour la réalité mixte, permettant aux développeurs de transformer des applications 2D avec des éléments spatiaux innovants.
*   **API de la caméra de transmission vidéo (Passthrough) :** Permet aux développeurs de fusionner de manière transparente les mondes virtuel et réel, créant des applications de réalité mixte.
*   **API d'interaction :** Pour le suivi des mains, la saisie via les manettes, la locomotion, et plus encore.
*   **API de commande vocale et de synthèse vocale (TTS) :** Pour intégrer le contrôle vocal et la sortie vocale dans les applications.
*   **API de compréhension de la scène :** Pour accéder et utiliser les données sur l'environnement physique de l'utilisateur (par exemple, maillage de la scène, ancres).
*   **API de fonctionnalités sociales :** Pour les classements, les défis, les notifications utilisateur, etc.

**Pour les Lunettes Intelligentes Ray-Ban Meta et Oakley Meta :**

Actuellement, il n'existe pas de SDK ou d'API officiel, complet et public, spécifiquement destiné aux développeurs tiers pour créer des applications personnalisées qui s'exécutent *directement sur* les lunettes intelligentes Ray-Ban Meta ou Oakley Meta.

Cependant, les développeurs ont fait preuve de créativité pour trouver des moyens d'interagir avec ces appareils :

*   **Intégration Meta AI :** Le principal moyen pour les développeurs d'interagir avec ces lunettes est via leur intégration avec **Meta AI**. Cela signifie que les développeurs peuvent potentiellement exploiter les capacités de Meta AI pour diverses tâches en utilisant les API existantes pour les grands modèles de langage (LLM) et autres services d'IA. Par exemple, certains projets communautaires ont démontré des intégrations « artisanales » utilisant Messenger comme pont pour envoyer des commandes ou recevoir des données des lunettes, puis en traitant ces données avec des services comme ChatGPT ou Google Gemini via leurs API respectives. Cela repose sur la capacité intégrée des lunettes à interagir avec Meta AI et à envoyer/recevoir des messages.
*   **Partage de contenu :** Les lunettes fonctionnent principalement comme un dispositif de capture et de partage. Les développeurs peuvent interagir avec l'**application Meta View** (l'application compagnon des lunettes) en fournissant des moyens de partager le contenu capturé avec les lunettes vers leurs plateformes, de la même manière que le contenu est partagé vers Instagram, Facebook, WhatsApp, etc.
*   **Fonctionnalités d'accessibilité :** Le Meta AI intégré fournit des fonctionnalités d'accessibilité comme la description de l'environnement ou la lecture de texte à voix haute. Bien que ce ne soit pas une API directe pour que les développeurs créent de nouvelles applications *sur* les lunettes, cela met en lumière le potentiel d'assistance pilotée par l'IA qui pourrait éventuellement être exposée via des outils de développement plus ouverts.

Bien que Meta ait exprimé sa vision à long terme pour un développement plus ouvert sur les futures lunettes intelligentes (potentiellement avec des afficheurs tête haute, comme le projet « Orion » qui fait l'objet de rumeurs), pour les lunettes intelligentes Ray-Ban Meta et Oakley Meta actuelles, l'accès des développeurs est principalement indirect, tirant parti de leur intégration avec Meta AI et des fonctionnalités de partage de contenu. La communauté explore activement des solutions de contournement et des intégrations non officielles en l'absence d'un SDK public dédié au développement d'applications sur l'appareil.