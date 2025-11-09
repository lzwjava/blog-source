---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-oss-120b
title: Résoudre les erreurs de requête trop volumineuse 413
translated: true
type: note
---

## Signification de l'erreur

- **413 Request Too Large** est un code d'état HTTP indiquant que le serveur a refusé de traiter la requête car la charge utile dépasse la taille autorisée. Dans le contexte du service d'inférence d'OpenAI, la « charge utile » correspond au nombre total de tokens (entrée + sortie) envoyés dans une seule requête. [1]

- **Limite de Tokens‑par‑minute (TPM)** : Le modèle `openai/gpt‑oss‑120b` est configuré avec un maximum de **8 000 TPM** pour le niveau de service à la demande. La requête que vous avez envoyée contenait **13 701 tokens**, ce qui représente **5 701 tokens au‑dessus de la limite**. [1]

- **Pourquoi cela se produit** :
  1. **Prompt volumineux** – le texte d'entrée (incluant les instructions système, les messages de l'utilisateur et toute donnée annexe) peut être très long.
  2. **Paramètre `max_tokens` élevé** – si la requête demande au modèle de générer une longue réponse, le nombre estimé de tokens de sortie s'ajoute à celui des tokens d'entrée.
  3. **Appels successifs rapides** – si de nombreuses requêtes sont effectuées en rafale, le cumul des tokens dans la minute en cours peut dépasser le quota TPM, même si chaque requête individuelle est sous la limite.

## Comment la résoudre

| Option | Action à entreprendre | Effet |
|--------|------------|--------|
| **Réduire le prompt** | Supprimer le texte inutile, utiliser des instructions concises ou compresser les données (par exemple, en résumant de gros blocs avant envoi). | Réduit le nombre de tokens en entrée. |
| **Réduire `max_tokens`** | Demander une réponse plus courte (par exemple, définir `max_tokens` sur 500 au lieu de 2000). | Diminue le nombre estimé de tokens en sortie. |
| **Diviser la requête** | Scinder un document volumineux en plusieurs segments plus petits et appeler le modèle séquentiellement, puis assembler les résultats ensuite. | Garde chaque appel sous la limite TPM. |
| **Changer de niveau de service** | Passer à un niveau de capacité supérieure (par exemple, le Niveau Développeur) où la limite TPM est plus élevée ou illimitée. | Permet des charges utiles plus importantes par requête sans erreur. |
| **Limiter les appels** | Ajouter un court délai entre les requêtes ou mettre en place un contrôle de débit pour maintenir le total de tokens par minute ≤ 8 000. | Empêche le dépassement TPM cumulatif. |

## Vérifications rapides avant d'envoyer une requête

1. **Compter les tokens** – utiliser l'outil tokenizer d'OpenAI (ou `tiktoken`) pour estimer le total de tokens (prompt + max tokens).
2. **Rester ≤ 8 000 TPM** pour le niveau à la demande.
3. **Si proche de la limite**, envisager l'une des mesures d'atténuation ci-dessus.

En veillant à ce que la requête reste dans le quota de 8 000 tokens par minute, l'erreur 413 « Request Too Large » sera évitée. [1]

Citations :
[1] https://www.reddit.com/r/OpenAI/comments/1nbtl2p/wow_weve_been_burning_money_for_6_months/