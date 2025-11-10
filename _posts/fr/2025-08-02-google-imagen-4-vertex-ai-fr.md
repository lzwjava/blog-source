---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide d'Aperçu de Google Imagen 4
translated: true
type: note
---

Pour utiliser Google Imagen 4 Preview 0606, vous devez y accéder via la plateforme Vertex AI de Google, car il s'agit d'une offre d'aperçu d'IA générative conçue pour la génération d'images à partir de texte. Voici un guide étape par étape basé sur les informations disponibles :

### Comment utiliser Google Imagen 4 Preview 0606

1.  **Accéder à Vertex AI** :
    *   **Plateforme** : Imagen 4 Preview 0606 est disponible sur Vertex AI de Google Cloud. Vous aurez besoin d'un compte Google Cloud pour commencer.
    *   **Inscription** : Si vous n'avez pas de compte, inscrivez-vous sur [cloud.google.com](https://cloud.google.com) et configurez un projet. Assurez-vous que la facturation est activée, car il s'agit d'une offre d'aperçu pouvant engendrer des coûts (les détails de tarification sont disponibles dans la section Imagen de la page de tarification Vertex AI).[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)
    *   **Naviguer vers Vertex AI** : Une fois connecté, allez dans la section Vertex AI de la Google Cloud Console et localisez les outils d'IA générative.

2.  **Configurer l'environnement** :
    *   **Authentification** : Authentifiez votre compte en utilisant les identifiants Google Cloud. Vous pouvez générer un jeton d'accès en utilisant la commande :
        ```bash
        gcloud auth print-access-token
        ```
    *   **Projet et Localisation** : Définissez votre ID de projet Google Cloud et la localisation (par exemple, `us-central1`). Exemple :
        ```bash
        export GOOGLE_CLOUD_PROJECT=your-project-id
        export GOOGLE_CLLOUD_LOCATION=us-central1
        ```

3.  **Utiliser le modèle Imagen 4** :
    *   **Accès API** : Imagen 4 Preview 0606 est accessible via l'API Vertex AI. Utilisez le endpoint de modèle `imagen-4.0-generate-preview-06-06`. Vous pouvez interagir avec lui de manière programmatique en utilisant des outils comme cURL ou le Google Gen AI SDK pour Python.
    *   **Exemple de requête cURL** :
        ```bash
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://${GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/projects/${GOOGLE_CLOUD_PROJECT}/locations/${GOOGLE_CLOUD_LOCATION}/publishers/google/models/imagen-4.0-generate-preview-06-06:predict" \
        -d '{"instances": [{"prompt": "A cat reading a book"}], "parameters": {"sampleCount": 1}}'
        ```
        Cela renvoie une image encodée en base64.[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)
    *   **Exemple avec le SDK Python** :
        ```python
        from google import genai
        from google.genai.types import GenerateImagesConfig
        client = genai.Client()
        image = client.models.generate_images(
            model="imagen-4.0-generate-preview-06-06",
            prompt="A dog reading a newspaper",
            config=GenerateImagesConfig(image_size="2K")
        )
        image.generated_images[0].image.save("output-image.png")
        print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")
        ```
        Cela génère une image et l'enregistre sous forme de fichier PNG.[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

4.  **Créer des prompts efficaces** :
    *   **Structure du prompt** : Pour de meilleurs résultats, utilisez des prompts détaillés et spécifiques. Incluez le sujet, l'environnement, le style artistique (par exemple, photoréaliste, abstrait), l'ambiance et les éléments de composition (par exemple, l'angle de la caméra). Exemple : « Une illustration graphique vibrante d'une ville futuriste au coucher du soleil, style cyberpunk, avec des lumières néon et une perspective en contre-plongée dramatique. »
    *   **Conseils** :
        *   Soyez précis : Des prompts vagues peuvent conduire à des résultats imprévisibles.
        *   Évitez les entrées non-sensiques (par exemple, des émojis aléatoires), car elles peuvent produire des résultats incohérents.
        *   Spécifiez le texte si nécessaire, car Imagen 4 a une meilleure capacité de rendu typographique.[](https://deepmind.google/models/imagen/)[](https://replicate.com/blog/google-imagen-4)
    *   **Prompts négatifs** : Vous pouvez utiliser un prompt négatif pour exclure les éléments indésirables (par exemple, « no text » si vous ne voulez pas de texte dans l'image).[](https://docs.aimlapi.com/api-references/image-models/google/imagen-4-preview)

5.  **Explorer les variantes** :
    *   Imagen 4 Preview 0606 a des variantes comme **Fast** (jusqu'à 10x plus rapide, optimisé pour la génération en masse) et **Ultra** (meilleur alignement avec les prompts pour un usage professionnel). Vérifiez si elles sont disponibles dans votre interface Vertex AI et choisissez en fonction de vos besoins (par exemple, Fast pour le prototypage rapide, Ultra pour les sorties de haute qualité).[](https://fal.ai/models/fal-ai/imagen4/preview)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

6.  **Examiner la sortie et les fonctionnalités de sécurité** :
    *   **Formats de sortie** : Les images sont générées dans des formats standards comme PNG ou JPEG, jusqu'à une résolution de 2K.[](https://fal.ai/models/fal-ai/imagen4/preview)
    *   **Filigrane SynthID** : Toutes les images incluent un filigrane numérique invisible pour les identifier comme étant générées par une IA, garantissant la transparence.[](https://deepmind.google/models/imagen/)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
    *   **Restrictions de contenu** : Imagen 4 utilise un filtrage pour minimiser le contenu nuisible, mais il peut avoir des difficultés avec les compositions complexes, les petits visages ou les images parfaitement centrées. Consultez les directives d'utilisation de Google pour les restrictions de contenu.[](https://deepmind.google/models/imagen/)[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

7.  **Plateformes alternatives** :
    *   Imagen 4 est également disponible sur des plateformes tierces comme Replicate, fal.ai, ou AI/ML API, qui peuvent offrir des interfaces plus simples ou des environnements de sandbox pour les tests. Par exemple :
        *   **Replicate** : Exécutez Imagen 4 avec un prompt comme « Un paysage de montagne serein au coucher du soleil, style hyperréaliste. » Consultez la documentation de Replicate pour les clés API et l'utilisation.[](https://replicate.com/blog/google-imagen-4)[](https://replicate.com/google/imagen-4-fast)
        *   **fal.ai** : Utilisez leur API avec une requête comme :
            ```javascript
            const result = await fal.subscribe("fal-ai/imagen4/preview", {
                input: { prompt: "A serene mountain landscape at sunset, hyperrealistic style" }
            });
            console.log(result.images[0].url);
            ```
            La tarification varie (par exemple, 0,05 $/image pour Standard, 0,04 $ pour Fast, 0,06 $ pour Ultra).[](https://fal.ai/models/fal-ai/imagen4/preview)
    *   **Application Gemini ou Google Workspace** : Imagen 4 est intégré dans l'application Gemini, Google Slides, Docs et Vids pour une génération d'image directe dans les flux de travail. Par exemple, dans Google Docs, vous pouvez générer des images pour illustrer des documents.[](https://www.stablediffusion.blog/imagen4)

8.  **Tester et itérer** :
    *   Expérimentez avec les prompts dans un environnement de sandbox (par exemple, Google AI Studio pour des tests gratuits limités) avant de l'intégrer en production.[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
    *   Surveillez l'utilisation de l'API et les coûts via le tableau de bord de la plateforme, car les offres d'aperçu peuvent avoir un support limité ou des fonctionnalités changeantes.[](https://fal.ai/models/fal-ai/imagen4/preview)

### Notes supplémentaires
*   **Tarification** : Consultez la page de tarification Vertex AI pour les coûts d'Imagen 4 (par exemple, 0,04 $/image pour Standard, 0,06 $/image pour Ultra).[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)[](https://fal.ai/models/fal-ai/imagen4/preview)
*   **Limitations** : Imagen 4 peut avoir des difficultés avec les prompts vagues, les petits visages ou les compositions parfaitement centrées. Utilisez des prompts clairs et structurés pour de meilleurs résultats.[](https://deepmind.google/models/imagen/)
*   **Disponibilité** : En tant qu'offre d'aperçu, les fonctionnalités et le support peuvent changer. Consultez les descriptions des étapes de lancement de Google Cloud pour les mises à jour.[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

Pour une documentation détaillée, visitez la [page Vertex AI Imagen](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview) ou le [Google Developers Blog](https://developers.googleblog.com). Pour l'accès API, consultez [x.ai/api](https://x.ai/api) pour des conseils généraux sur l'API d'IA, bien que les détails spécifiques à Imagen 4 se trouvent sur Google Cloud.[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)

Si vous avez besoin d'aide pour une plateforme ou un cas d'utilisation spécifique, faites-le-moi savoir !