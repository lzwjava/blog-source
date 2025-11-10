---
audio: false
generated: true
lang: fr
layout: post
title: Longueurs de contexte des modèles Mistral AI 2025
translated: true
type: note
---

En juin 2025, Mistral AI a publié plusieurs modèles avec différentes longueurs de contexte. Voici un résumé de certains modèles clés et leurs fenêtres de contexte :

*   **Magistral Small (magistral-small-2506) :** Ce modèle open-weight a une fenêtre de contexte de 128k, bien que les performances puissent se dégrader au-delà de 40k, donc une longueur maximale recommandée est de 40k tokens.
*   **Magistral Medium (magistral-medium-2506) :** Ce modèle de raisonnement disponible uniquement via API a également une fenêtre de contexte recommandée de 40k.
*   **Mistral Small 3.1 (mistral-small-2503) / Mistral Small 3.2 (mistral-small-2506) :** Ces modèles disposent d'une fenêtre de contexte allant jusqu'à 128 000 tokens.
*   **Codestral (codestral-2501) :** Ce modèle axé sur le code offre une fenêtre de contexte significative de 256 000 tokens.
*   **Mistral Large 2 (mistral-large-2407 / mistral-large-2411) :** Le grand modèle phare de Mistral a une fenêtre de contexte de 128k.
*   **Mistral NeMo (open-mistral-nemo-2407) :** Ce modèle 12B, développé en collaboration avec NVIDIA, propose une grande fenêtre de contexte allant jusqu'à 128 000 tokens.
*   **Mistral Medium 3 (mistral-medium-2505) :** Ce modèle multimodal prend également en charge une fenêtre de contexte de 128k.

Il est important de noter que bien que certains modèles annoncent des fenêtres de contexte très importantes (par exemple, 128k), les performances pratiques peuvent être optimisées pour une plage légèrement plus petite (par exemple, 40k pour les modèles Magistral).