---
audio: false
generated: true
lang: fr
layout: post
title: Analyse détaillée des plateformes d'IA pour l'intégration de clés d'API et
  les modèles de tarification
translated: true
type: note
---

### Points Clés
- Il semble probable que Portkey soit une plateforme adaptée pour utiliser vos propres clés API d'IA avec une interface unifiée, bien qu'elle ait un abonnement payant, ce qui pourrait ne pas correspondre à votre préférence pour une tarification à l'usage.
- Les recherches suggèrent qu'OpenRouter propose une utilisation payante par token sans abonnement, mais il ne permet pas de connecter vos propres clés API, ce qui pourrait ne pas répondre à vos besoins.
- Les éléments recueillis indiquent qu'il existe peu de plateformes qui correspondent parfaitement à vos critères : utilisation de vos propres clés API avec une tarification à l'usage basée sur la consommation de tokens et sans frais d'abonnement, ce qui pourrait nécessiter un compromis.

### Recommandation de Plateforme
Après avoir évalué vos besoins, Portkey ([Portkey AI](https://portkey.ai/)) semble être l'option la plus proche. Il vous permet de connecter vos propres clés API pour divers modèles d'IA, en fournissant une interface unifiée pour la gestion. Cependant, il fonctionne sur un modèle basé sur l'abonnement (par exemple, 49 $/mois pour le plan Pro), ce qui signifie que vous paieriez un forfait fixe pour utiliser la plateforme, en plus de payer directement les fournisseurs d'IA via vos clés pour l'utilisation des tokens. Cela pourrait ne pas correspondre entièrement à votre souhait d'éviter les frais d'abonnement comme 20 $/mois, mais il offre des fonctionnalités avancées comme l'observabilité et la gestion des prompts qui pourraient être utiles.

Si éviter les frais d'abonnement est crucial et que vous êtes prêt à renoncer à utiliser vos propres clés API, OpenRouter ([OpenRouter](https://openrouter.ai)) est une autre option. Il facture 0,0001 $ par token après un quota gratuit de 1000 tokens par mois, sans frais d'abonnement, mais vous utiliseriez leur API au lieu de vos propres clés, ce qui signifie que vous les payez directement pour l'utilisation des modèles.

### Détail Inattendu
Une découverte inattendue est que de nombreuses plateformes, comme OpenRouter, fournissent leur propre accès aux modèles d'IA, obligeant les utilisateurs à payer via la plateforme plutôt que d'utiliser des clés API personnelles, ce qui pourrait limiter votre contrôle sur les coûts et les données.

---

### Note d'Enquête : Analyse Détaillée des Plateformes d'IA pour l'Intégration de Clés API et les Modèles de Tarification

Cette analyse explore les plateformes qui permettent aux utilisateurs de connecter leurs propres clés API d'IA et qui offrent une tarification à l'usage basée sur la consommation de tokens, sans frais d'abonnement, comme alternative à des plateformes comme ChatBoxAI et OpenWebUI. La recherche, menée à 02h42 PDT le vendredi 14 mars 2025, vise à répondre aux besoins spécifiques de l'utilisateur tout en considérant les complexités de la tarification et de la fonctionnalité des plateformes.

#### Contexte et Exigences de l'Utilisateur
L'utilisateur dispose de plusieurs clés API pour diverses plateformes d'IA et recherche une plateforme qui :
- Permet de connecter ses propres clés API pour une interface unifiée.
- Offre une tarification à l'usage basée sur la consommation de tokens, évitant les frais d'abonnement comme 20 $/mois.
- Fournit une interface utilisateur (UI) meilleure que ChatBoxAI, qu'il a trouvée médiocre, et intègre potentiellement Mistral.

Compte tenu de ces exigences, l'analyse se concentre sur l'identification des plateformes répondant à ces critères, la compréhension de leurs modèles de tarification et l'évaluation de leur interface utilisateur et de leurs capacités d'intégration.

#### Évaluation des Plateformes

##### Contexte sur ChatBoxAI et OpenWebUI
- **ChatBoxAI** ([ChatBox AI](https://chatboxai.app/en)) est un client de bureau pour les modèles d'IA comme ChatGPT, Claude et d'autres, permettant aux utilisateurs de connecter leurs propres clés API. Il a un modèle d'abonnement pour son service d'IA, qui peut inclure des frais de 20 $/mois, et prend en charge Mistral via des intégrations, contrairement à ce que mentionne l'utilisateur sur l'absence d'intégration de Mistral. Son interface utilisateur est notée comme médiocre par l'utilisateur.
- **OpenWebUI** ([Open WebUI](https://openwebui.com/)) est une interface open source et auto-hébergée pour les modèles d'IA, prenant en charge divers exécutants LLM comme Ollama et les API compatibles OpenAI. Il permet aux utilisateurs de connecter leurs propres clés API et est gratuit, sans frais d'abonnement, correspondant au modèle à l'usage via les coûts des fournisseurs. Cependant, l'utilisateur cherche des alternatives à cela.

##### Plateformes Candidates
Plusieurs plateformes ont été évaluées, en se concentrant sur leur capacité à gérer les clés API fournies par l'utilisateur et leurs modèles de tarification. Les principales conclusions sont résumées ci-dessous :

| Plateforme   | Permet les Clés API Personnelles | Modèle de Tarification                     | Intégration Mistral | Notes sur l'UI                      |
|--------------|----------------------------------|--------------------------------------------|---------------------|-------------------------------------|
| Portkey      | Oui                              | Basé sur l'abonnement (ex: 49 $/mois)      | Oui                 | Web, réputée pour sa facilité d'utilisation |
| OpenRouter   | Non                              | Payant par token (0,0001 $/token après 1000 gratuits) | Oui | Web, interface simple               |
| Unify.ai     | Potentiellement (BYOM)           | Pas clair, probablement abonnement         | Oui                 | Axée sur les workflows, moins sur l'UI |
| LiteLLM      | Oui                              | Gratuit (open source)                      | Oui                 | Couche API, pas d'UI pour l'utilisateur |

- **Portkey** ([Portkey AI](https://portkey.ai/)) : Cette plateforme permet aux utilisateurs de connecter leurs propres clés API pour plus de 250 LLM, y compris Mistral, via sa AI Gateway. Elle fournit une interface unifiée avec des fonctionnalités comme l'observabilité, la gestion des prompts et les basculements de modèles. La tarification est basée sur l'abonnement, avec des plans comme un niveau Starter gratuit, un niveau Pro à 49 $/mois et des tarifs personnalisés pour les entreprises. Les utilisateurs paient Portkey pour l'accès à la plateforme et les fournisseurs directement via leurs clés pour l'utilisation des modèles, ce qui pourrait ne pas correspondre à l'évitement des frais d'abonnement. Les avis des utilisateurs mettent en avant sa facilité d'utilisation et ses fonctionnalités complètes, suggérant une UI potentiellement meilleure que le client de bureau ChatBoxAI.

- **OpenRouter** ([OpenRouter](https://openrouter.ai)) : Cette plateforme offre une API unifiée pour plusieurs LLM, avec une tarification par token (0,0001 $/token après 1000 tokens gratuits mensuels, sans frais d'abonnement). Cependant, elle ne permet pas aux utilisateurs de connecter leurs propres clés API ; à la place, les utilisateurs utilisent l'API d'OpenRouter, les payant directement pour l'utilisation des modèles. Elle prend en charge Mistral et a une interface web notée pour sa simplicité, offrant potentiellement une meilleure UI que ChatBoxAI. Cela correspond au modèle à l'usage mais ne répond pas à l'exigence d'utilisation de clés API personnelles.

- **Unify.ai** ([Unify: Build AI Your Way](https://unify.ai/)) : Cette plateforme se concentre sur la création de workflows d'IA et mentionne "Bring Your Own Model" (BYOM), suggérant un support potentiel pour les modèles fournis par l'utilisateur. Cependant, sa tarification et son interface utilisateur sont moins claires, et elle semble plus orientée développeurs, avec probablement des coûts basés sur l'abonnement. Elle prend en charge Mistral, mais son adéquation pour une interface utilisateur est incertaine, la rendant moins adaptée par rapport à Portkey ou OpenRouter.

- **LiteLLM** : Un proxy d'API d'IA open source qui permet aux utilisateurs de connecter leurs propres clés API et de les utiliser via une API unifiée. C'est gratuit, sans frais d'abonnement, et les utilisateurs paient les fournisseurs directement via leurs clés pour l'utilisation des tokens. Cependant, il n'a pas d'interface utilisateur, le rendant plus adapté aux développeurs l'intégrant dans des applications, et non pour une interaction directe de l'utilisateur comme ChatBoxAI ou OpenWebUI.

#### Analyse de l'Adéquation aux Exigences de l'Utilisateur
- **Utilisation de Clés API Personnelles** : Portkey et LiteLLM le permettent explicitement, tandis qu'OpenRouter ne le permet pas, obligeant les utilisateurs à utiliser son API. La fonctionnalité BYOM d'Unify.ai est ambiguë et moins axée sur l'utilisateur.
- **Tarification à l'Usage Basée sur la Consommation de Tokens** : OpenRouter correspond avec sa tarification par token, mais les utilisateurs n'utilisent pas leurs propres clés. Portkey a un modèle d'abonnement, ce qui contredit le souhait de l'utilisateur d'éviter des frais comme 20 $/mois. LiteLLM est gratuit, correspondant à l'absence d'abonnement, mais manque d'interface utilisateur. Aucune plateforme ne combine parfaitement toutes les exigences sans compromis.
- **Interface Utilisateur et Intégration Mistral** : Portkey et OpenRouter ont toutes deux des interfaces web, potentiellement meilleures que le client de bureau ChatBoxAI, et toutes deux prennent en charge Mistral. Les avis des utilisateurs suggèrent que l'UI de Portkey est conviviale, tandis que celle d'OpenRouter est simple. L'absence d'UI de LiteLLM le rend inadapté pour des besoins axés sur l'interface utilisateur.

#### Défis et Compromis
Le principal défi est l'apparente absence de plateformes permettant aux utilisateurs de connecter leurs propres clés API, de fournir une interface utilisateur unifiée et de facturer en fonction de l'utilisation des tokens sans frais d'abonnement. La plupart des plateformes facturent soit un abonnement (comme Portkey), soit n'autorisent pas les clés API personnelles (comme OpenRouter). Cela suggère un compromis :
- Accepter des frais d'abonnement pour les fonctionnalités de la plateforme (Portkey) tout en utilisant ses propres clés.
- Utiliser un modèle payant par token sans ses propres clés (OpenRouter), perdant potentiellement le contrôle des coûts via les clés personnelles.

#### Recommandation et Considérations
Compte tenu de l'insistance de l'utilisateur sur l'utilisation de ses propres clés API et l'évitement des frais d'abonnement, aucune correspondance parfaite n'a été trouvée. Cependant, **Portkey** est recommandé comme l'option la plus proche, permettant la connexion de clés API personnelles et offrant une interface unifiée avec une UI potentiellement meilleure que ChatBoxAI. Malgré les frais d'abonnement (par exemple, 49 $/mois pour Pro), il prend en charge des fonctionnalités avancées qui peuvent justifier le coût pour gérer plusieurs modèles d'IA. Les utilisateurs devraient évaluer si les fonctionnalités l'emportent sur le coût de l'abonnement, surtout par rapport au paiement direct des fournisseurs via les clés sans plateforme.

Pour ceux qui privilégient le paiement par token sans abonnement et sont prêts à renoncer à l'utilisation de clés personnelles, **OpenRouter** est une alternative, facturant 0,0001 $ par token après 1000 gratuits, avec une interface web simple et la prise en charge de Mistral. Cependant, cela signifie renoncer au contrôle des clés API, ce qui pourrait ne pas correspondre à la possession de multiples clés par l'utilisateur.

#### Conclusion
Cette analyse souligne la complexité de trouver une plateforme répondant à tous les critères de l'utilisateur. Portkey offre la meilleure adéquation pour utiliser des clés API personnelles avec une interface unifiée, bien qu'avec un coût d'abonnement. OpenRouter fournit un modèle payant par token sans abonnement mais ne prend pas en charge les clés personnelles. Les utilisateurs pourraient devoir décider en fonction de si les fonctionnalités de la plateforme ou la flexibilité des coûts sont plus critiques, explorant potentiellement des options open source comme l'auto-hébergement d'alternatives à OpenWebUI pour une utilisation gratuite avec des clés personnelles.

#### Citations Clés
- [Portkey AI control panel for production AI](https://portkey.ai/)
- [OpenRouter unified interface for LLMs](https://openrouter.ai)
- [ChatBox AI your AI copilot](https://chatboxai.app/en)
- [Open WebUI extensible self-hosted interface for AI](https://openwebui.com/)