---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Options de clients Web légers pour LLM locaux
translated: true
type: note
---

Si vous recherchez des clients web légers et open source pour exécuter des LLMs localement — avec moins de dépendances qu'Open WebUI — voici quelques alternatives intéressantes :

**1. Lobe Chat**
- Léger et extensible, Lobe Chat prend en charge à la fois les LLMs locaux et distants. Il offre un système de plugins et une interface utilisateur épurée, et peut être exécuté via Docker ou directement sur votre machine. Il est reconnu pour sa facilité de configuration et ses bonnes performances avec Ollama et d'autres backends.

**2. LM Studio**
- LM Studio est une application de bureau qui prend en charge les modèles GGUF (comme Mistral, Phi 3 et Gemma) et fournit une interface simple et conviviale. Il est idéal pour une inférence locale rapide et ne nécessite pas de configuration complexe ni de nombreuses dépendances.

**3. text-generation-webui (Oobabooga)**
- Une interface web riche en fonctionnalités, basée sur Gradio, qui prend en charge plusieurs backends (transformers, GPTQ, AWQ, EXL2, llama.cpp). Elle est hautement personnalisable et très utilisée, bien que sa configuration soit légèrement plus complexe que celle de LM Studio.

**4. AnythingLLM**
- Une interface de chat polyvalente et auto-hébergée qui fonctionne bien pour les modèles locaux et cloud. Elle est conçue pour un usage général et est disponible en tant qu'application de bureau, ce qui la rend flexible et relativement légère.

**5. Jan**
- Jan est une interface de chat multiplateforme, fonctionnant hors ligne, avec une personnalisation par glisser-déposer et des modèles pré-construits. Elle est optimisée pour les performances et prend en charge plusieurs APIs LLM, ce qui en fait un bon choix pour les utilisateurs soucieux de la confidentialité.

**6. Ollama UI**
- Conçue spécifiquement pour Ollama, cette interface est minimale et facile à déployer, ce qui en fait un bon choix si vous utilisez déjà Ollama pour le déploiement de modèles.

**7. Open-LLM-WebUI**
- Une interface web simple et open source pour exécuter des LLMs compacts localement. Elle est conçue pour être facile à utiliser et nécessite une configuration minimale, ce qui en fait une bonne alternative pour ceux qui recherchent une solution simple.

**Tableau récapitulatif :**

| Client                | Caractéristiques principales                          | Complexité de configuration | Idéal pour                |
|-----------------------|-------------------------------------------------------|-----------------------------|---------------------------|
| Lobe Chat             | Plugins, support Docker, interface épurée             | Faible                      | Usage général, Ollama     |
| LM Studio             | App de bureau, support GGUF, interface simple         | Très faible                 | Inférence locale rapide   |
| text-generation-webui | Multi-backends, hautement personnalisable             | Moyenne                     | Utilisateurs avancés      |
| AnythingLLM           | App de bureau, flexible, usage général                | Faible                      | Hybride local/cloud       |
| Jan                   | Hors ligne, glisser-déposer, modèles                  | Faible                      | Confidentialité, personnalisation |
| Ollama UI             | Minimaliste, axé sur Ollama                           | Très faible                 | Utilisateurs d'Ollama     |
| Open-LLM-WebUI        | Simple, léger                                         | Faible                      | LLMs compacts             |

Si vous voulez l'option la plus légère, **LM Studio** ou **Ollama UI** sont d'excellents points de départ. Pour plus de fonctionnalités et de flexibilité, **Lobe Chat** ou **text-generation-webui** sont des choix solides.

Souhaitez-vous plus de détails sur la configuration ou des cas d'utilisation spécifiques pour l'un de ces outils ?