---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Performances et efficacité de DeepSeek OCR
translated: true
type: note
---

### DeepSeek OCR est-il bon ?

DeepSeek OCR est un modèle vision-langage (VLM) de 3 milliards de paramètres nouvellement publié par DeepSeek AI, lancé le 20 octobre 2025, spécifiquement optimisé pour la reconnaissance optique de caractères (OCR) et le traitement de documents structurés. Sur la base des premières évaluations et benchmarks, il démontre de solides performances :

- **Efficacité de compression** : Il utilise la « compression de contexte optique » pour réduire les données visuelles en beaucoup moins de tokens (par exemple, 100 tokens visuels au lieu de 1 000+ tokens de texte pour le même contenu), atteignant une précision de décodage d'environ 97 % à des taux de compression de 10x et des résultats quasi sans perte jusqu'à 20x. Cela le rend très efficace pour traiter de grands documents sans perdre les détails essentiels.

- **Débit** : Sur un seul GPU, il peut traiter plus de 200 000 pages par jour, ce qui représente un bond significatif pour les applications réelles comme la numérisation d'archives ou l'automatisation de l'extraction de formulaires.

- **Performances sur les benchmarks** : Il surpasse les autres modèles OCR open-source (par exemple, dans les tâches de compréhension de documents) et égale ou approche les leaders closed-source comme GPT-4V en précision pour les sorties structurées. Les premiers tests soulignent son avantage dans le traitement des mises en page complexes, des tableaux et du texte multilingue.

Cela dit, il est très récent, donc l'adoption réelle ne fait que commencer. Il existe des rapports de difficultés de configuration pour des exécutions locales (par exemple, sur Apple Silicon ou des configurations NVIDIA nécessitant des ajustements), mais une fois en fonctionnement, les utilisateurs le décrivent comme « plutôt bon » pour un usage expérimental. Globalement, si vous recherchez une solution OCR efficace et précise pour les documents, c'est un choix solide — surtout en tant qu'option open-source. Pour l'OCR d'images générales (par exemple, les mèmes ou l'écriture manuscrite), il pourrait encore nécessiter un fine-tuning par rapport à des outils spécialisés comme Tesseract.

### Qu'est-ce qu'un Vision Token ?

Dans les modèles d'IA, en particulier les modèles vision-langage (VLM) multimodaux comme ceux d'OpenAI, DeepSeek ou LLaVA, un **vision token** est une représentation numérique compacte d'un petit morceau de données visuelles. Voici une explication :

- **Fonctionnement** : Les images ne sont pas fournies directement aux modèles de langage (qui traitent le texte). Au lieu de cela, l'image est divisée en patchs de taille fixe (par exemple, 14x14 pixels). Chaque patch est intégré dans un vecteur — un « token » — similaire à la façon dont les mots deviennent des tokens en texte. Ces vision tokens capturent des caractéristiques comme les bords, les couleurs ou les textures, permettant au modèle de « comprendre » et de raisonner sur l'image aux côtés des tokens de texte.

- **Importance** : Cette tokenisation permet un traitement efficace. Par exemple, une image 512x512 pourrait générer des centaines de vision tokens, mais des techniques avancées (comme dans DeepSeek OCR) les compressent davantage pour réduire les coûts de calcul tout en préservant la précision. C'est essentiel pour des tâches comme le sous-titrage d'images, les questions-réponses visuelles ou l'OCR, où le modèle mélange les informations visuelles et textuelles.

- **Exemple** : Dans GPT-4V, une photo téléchargée devient environ 85 vision tokens (redimensionnée et découpée en patchs), que le modèle traite comme des mots d'invite pour générer des réponses.

Les vision tokens comblent le fossé entre les pixels et le langage, permettant à l'IA de « voir » d'une manière qui est réalisable sur le plan computationnel.

**Références**  
[DeepSeek Just Released a 3B OCR Model](https://www.marktechpost.com/2025/10/20/deepseek-just-released-a-3b-ocr-model-a-3b-vlm-designed-for-high-performance-ocr-and-structured-document-conversion/)  
[DeepSeek-OCR Isn't About OCR, It's About Token Compression](https://medium.com/@olimiemma/deepseek-ocr-isnt-about-ocr-it-s-about-token-compression-db1747602e29)  
[DeepSeek's New OCR Model Can Process Over 2 Lakh Pages Daily](https://analyticsindiamag.com/ai-news-updates/deepseeks-new-ocr-model-can-process-over-2-lakh-pages-daily-on-a-single-gpu/)  
[Token: AI & ML Definition](https://www.ultralytics.com/glossary/token)  
[Revolutionizing AI Vision: Visual Perception Tokens](https://kitemetric.com/blogs/revolutionizing-ai-vision-introducing-visual-perception-tokens)