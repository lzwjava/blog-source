---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Approvisionnement de données textuelles pour l'entraînement des LLM
translated: true
type: note
---

### Comment obtenir de grandes quantités de données textuelles pour entraîner des modèles de langage

L'entraînement de grands modèles de langage (LLM) nécessite des quantités massives de données textuelles diverses et de haute qualité – souvent des billions de tokens provenant de livres, de sites web, de code, et plus encore. Les principaux défis sont l'échelle (téraoctets à pétaoctets), la qualité (filtrer le bruit, les doublons et le contenu à faible valeur) et la légalité (respecter les droits d'auteur, utiliser des données du domaine public ou sous licence). Voici un guide étape par étape pour les sourcer :

1.  **Commencez par les moissonnages web publics** : Ils constituent l'épine dorsale de la plupart des entraînements de LLM. Ils capturent des instantanés de l'internet.
    - Filtrez pour obtenir du texte propre en utilisant des outils comme CC-Net ou Dedup (bibliothèques Python via Hugging Face).
    - Traitez par lots pour gérer la taille – utilisez le stockage cloud (par exemple, AWS S3) pour les téléchargements.

2.  **Utilisez des ensembles de données organisés** : Collections pré-filtrées de groupes de recherche. Téléchargez via des API ou des liens directs.
    - Concentrez-vous sur des sous-ensembles multilingues et spécifiques à un domaine (par exemple, le code, la science) pour correspondre à vos besoins.
    - Des outils comme la bibliothèque Hugging Face Datasets facilitent le chargement : `from datasets import load_dataset`.

3.  **Complétez avec des sources spécifiques à un domaine** :
    - Livres : Project Gutenberg (domaine public).
    - Wikipédia : Archives linguistiques.
    - Code : Archives GitHub (via BigCode).
    - Générez des données synthétiques : Utilisez des modèles existants (par exemple, via l'API OpenAI) pour créer des chaînes de raisonnement, mais nettoyez-les pour éviter la contamination.

4.  **Conseils juridiques et éthiques** :
    - Tenez-vous aux licences libres (par exemple, CC-BY, MIT).
    - Dédupliquez (outils comme MinHash) et supprimez les PII (informations personnelles).
    - Pour un entraînement personnalisé, commencez petit (par exemple, affinez sur 1-10 Go) avant de passer à l'échelle.
    - Coûts de calcul : Prévoyez des centaines d'heures de GPU même pour un entraînement modeste ; utilisez Colab ou RunPod pour les tests.

5.  **Pipeline de traitement** :
    - Téléchargement → Nettoyage (supprimer le HTML, les non-textes) → Tokenisation (par exemple, avec TikToken) → Entraînement.
    - Bibliothèques : Pandas pour l'échantillonnage, spaCy/NLTK pour le prétraitement.

Les ensembles de données publics sont gratuits et massifs – idéaux pour les amateurs ou les chercheurs. Pour la production, les entreprises sous-traitent souvent des données propriétaires.

### Sources de données d'entraînement pour des modèles spécifiques

Les modèles propriétaires comme ceux d'OpenAI, Anthropic et DeepSeek gardent leurs recettes exactes secrètes pour des raisons de compétitivité, mais ils ont partagé des détails de haut niveau via des articles, des blogs et des fuites. Les modèles open-source (par exemple, Llama, Mistral) sont plus transparents, publiant souvent les plans des ensembles de données.

-   **Modèles GPT d'OpenAI (par exemple, GPT-4o)** :
    Ils s'entraînent sur un mélange de données internet publiquement disponibles (moissonnages web filtrés), de livres, d'articles et de code. Les premiers GPT utilisaient largement Common Crawl ; les suivants mettent l'accent sur des sources de haute qualité en STEM/code. Total : Des billions de tokens, avec une forte déduplication. Ils intègrent également des données sous licence et des interactions utilisateur (avec possibilité de désinscription). Aucune publication publique complète, mais c'est "l'intégralité d'internet" dans l'essence – aspirée, filtrée et augmentée.

-   **Modèles d'Anthropic (par exemple, Claude 3.5)** :
    L'accent est mis sur des données sûres et utiles : texte web public, livres et exemples synthétiques générés pour l'alignement (par exemple, Constitutional AI). Ils utilisent les conversations des utilisateurs avec Claude (possibilité de désinscription) et des ensembles de données de RLHF comme HH-RLHF. L'accent est mis sur des sources diverses et non toxiques ; certaines controverses concernent les transcriptions YouTube aspirées. Échelle totale : Des billions similaires, mais plus organisés pour l'éthique.

-   **Modèles DeepSeek (par exemple, DeepSeek-V3, R1)** :
    Modèles chinois "ouverts" utilisant des pages web brutes, des livres électroniques et des dépôts de code. V3 pré-entraîné sur 14,8 T de tokens sans données synthétiques délibérées, mais R1 ajoute 600 000 échantillons de raisonnement synthétiques via un échantillonnage par rejet (générés par des modèles antérieurs). Sources : Moissonnages web + docs techniques ; mélange propriétaire, mais transparent dans les articles.

-   **Modèles Open-Source (par exemple, Llama 3, BLOOM, GPT-J)** :
    Ceux-ci utilisent explicitement des ensembles de données publics comme The Pile (mélange multilingue de 800 Go), C4 (Colossal Clean Crawled Corpus, 750 Go de web anglais) ou OSCAR (Common Crawl multilingue). BLOOM a utilisé ROOTS (1,6 To, 46 langues). Ils évitent les données propriétaires, en se concentrant sur la reproductibilité – vérifiez les fiches de modèles sur Hugging Face pour les détails exacts.

En bref : Tous reposent sur des données à l'échelle du web, mais les propriétaires ajoutent du filtrage/des licences/des synthétiques pour la qualité. L'open-source s'appuie sur les collections publiques organisées par la communauté.

### Liens de téléchargement pour les grands ensembles de données textuelles publics

Voici les meilleures sources gratuites et téléchargeables (tailles approximatives ; vérifiez les mises à jour). Commencez par des sous-ensembles si le stockage est limité.

-   **Common Crawl** : Instantanés web mensuels (pétaoctets au total). Filtrez avec les index CC-MAIN. [Archives Common Crawl](https://commoncrawl.org/get-started)
-   **The Pile** : 800 Go de texte anglais diversifié (livres, code, arXiv, etc.). [EleutherAI The Pile sur Hugging Face](https://huggingface.co/datasets/EleutherAI/pile)
-   **C4 (Colossal Clean Crawled Corpus)** : 750 Go de web anglais nettoyé (utilisé pour T5/GPT). [TensorFlow Datasets C4](https://www.tensorflow.org/datasets/catalog/c4)
-   **OSCAR (Open Super-large Crawled Aggregated coRpus)** : Web multilingue (22 langues, ~10 To). [OSCAR sur Hugging Face](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201)
-   **Wikipedia Dumps** : Extraits de texte complets (Anglais : ~20 Go). [Téléchargements Wikimedia](https://dumps.wikimedia.org/enwiki/latest/)
-   **BooksCorpus/OpenWebText** : 11 Go de livres + 40 Go de Reddit/web (ère GPT-2). [OpenWebText sur GitHub](https://github.com/jcpeterson/openwebtext)
-   **RedPajama** : 1 T+ de tokens, répliqué à partir des articles de Llama. [TogetherAI RedPajama sur HF](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)
-   **LLMDataHub** : Liste organisée de 100+ ensembles de données (chat, code, etc.). [GitHub LLMDataHub](https://github.com/Zjh-819/LLMDataHub)

Pour plus, parcourez le hub Hugging Face Datasets : [Hugging Face Datasets](https://huggingface.co/datasets). Vérifiez toujours les licences !

**Références**
[Comment ChatGPT et nos modèles de base sont développés](https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-language-models-are-developed)
[Ce que GPT-oss révèle sur les données d'entraînement d'OpenAI](https://www.lesswrong.com/posts/iY9584TRhqrzawhZg/what-gpt-oss-leaks-about-openai-s-training-data)
[Anthropic utilisera les conversations de Claude comme données d'entraînement](https://www.wired.com/story/anthropic-using-claude-chats-for-training-how-to-opt-out/)
[Ensemble de données HH-RLHF d'Anthropic](https://huggingface.co/datasets/Anthropic/hh-rlhf)
[Qu'est-ce qui est entré dans l'entraînement de DeepSeek-R1 ?](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1)
[Le guide complet des modèles DeepSeek](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
[LLMDataHub : Ensembles de données impressionnants pour l'entraînement des LLM](https://github.com/Zjh-819/LLMDataHub)
[Ensembles de données d'entraînement open-source pour les LLM](https://kili-technology.com/large-language-models-llms/9-open-sourced-datasets-for-training-large-language-models)
[Données d'entraînement LLM : Les 8 principales sources de données publiques](https://oxylabs.io/blog/llm-training-data)