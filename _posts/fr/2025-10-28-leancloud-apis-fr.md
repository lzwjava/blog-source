---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: API LeanCloud non nommées Uluru
translated: true
type: note
---

Non, LeanCloud n’appelle pas son API publique « Uluru API ». Leurs API officielles sont désignées sous le nom d’API REST LeanCloud (pour le stockage de données, les requêtes, etc.), d’API REST Cloud Engine (pour les fonctions et hooks côté serveur), et d’autres endpoints spécifiques à des services similaires, comme ceux pour les notifications push ou le stockage de fichiers. Celles-ci sont largement documentées sur leur site pour développeurs (docs.leancloud.cn) sans aucune référence à « Uluru ».

Cependant, « Uluru » semble bien être un nom de code interne ou ancien associé au développement de leur produit ou SDK. Ceci est basé sur un package npm archivé appelé **uluru-js-sdk** (version 0.1.0, publiée il y a environ 12 ans sous le compte de l’éditeur « avos »). AVOS Cloud était le nom d’origine de LeanCloud avant le changement de marque, et ce package est décrit comme un « SDK JavaScript pour PAAS » (Platform as a Service), ce qui correspond aux services backend de LeanCloud. Il prenait en charge à la fois les environnements navigateur et Node.js pour des fonctionnalités principales comme les opérations sur les données – en adéquation avec les premières offres de LeanCloud – mais n’a jamais été promu publiquement comme le SDK principal. Les SDK actuels sont estampillés « LeanCloud SDK » (par exemple pour Java, Python, JavaScript, etc.) et sont disponibles sur GitHub sous leancloud/.

S’il s’agit d’une référence à quelque chose de plus récent ou spécifique (par exemple, un outil privé/interne), cela n’est pas documenté publiquement. Pour les détails officiels sur les API, consultez la [Documentation LeanCloud](https://docs.leancloud.cn/en/).