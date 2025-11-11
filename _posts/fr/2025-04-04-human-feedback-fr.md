---
audio: false
generated: true
lang: fr
layout: post
title: Apprentissage par Renforcement à l’Aide de Retours Humains (RLHF) Expliqué
translated: true
type: note
---

**L'apprentissage par renforcement à partir de retours humains (RLHF)** est une technique d'apprentissage automatique utilisée pour affiner les modèles d'IA, en particulier les grands modèles de langage (LLM), afin de mieux les aligner sur les préférences et les instructions humaines. Au lieu de s'appuyer uniquement sur des fonctions de récompense prédéfinies, le RLHF intègre des retours directs provenant d'humains pour guider le processus d'apprentissage.

**Pourquoi le RLHF est-il important ?**

* **Tâches subjectives :** Le RLHF excelle dans les tâches où le résultat souhaité est difficile à définir avec des règles explicites ou des récompenses numériques, comme la génération de texte créatif, la conversation naturelle ou la production de contenu utile et inoffensif.
* **Nuance et alignement :** Il aide les modèles d'IA à comprendre et à respecter les préférences humaines subtiles, les considérations éthiques et les styles d'interaction souhaités.
* **Performance améliorée :** Les modèles entraînés avec le RLHF démontrent souvent une performance et une satisfaction des utilisateurs nettement supérieures à celles des modèles entraînés uniquement par apprentissage par renforcement traditionnel ou par apprentissage supervisé.

**Fonctionnement du RLHF (généralement en trois étapes) :**

1.  **Pré-entraînement et réglage fin supervisé (SFT) :**
    * Un modèle de langage de base est d'abord pré-entraîné sur un jeu de données massif de texte et de code pour apprendre la compréhension et la génération du langage en général.
    * Ce modèle pré-entraîné est ensuite souvent affiné en utilisant l'apprentissage supervisé sur un jeu de données plus petit de démonstrations de haute qualité du comportement souhaité (par exemple, des humains écrivant des réponses idéales à des invites). Cette étape aide le modèle à comprendre le format et le style des sorties attendues.

2.  **Entraînement du modèle de récompense :**
    * C'est une étape cruciale du RLHF. Un **modèle de récompense** distinct est entraîné pour prédire les préférences humaines.
    * Des annotateurs humains se voient présenter différentes sorties du modèle SFT (ou d'une version ultérieure) pour la même invite. Ils classent ou évaluent ces sorties sur la base de divers critères (par exemple, l'utilité, la cohérence, la sécurité).
    * Ces données de préférence (par exemple, "la sortie A est meilleure que la sortie B") sont utilisées pour entraîner le modèle de récompense. Le modèle de récompense apprend à attribuer un score de récompense scalaire à toute sortie de modèle donnée, reflétant la préférence qu'un humain lui accorderait.

3.  **Réglage fin par apprentissage par renforcement :**
    * Le modèle de langage original (initialisé à partir du modèle SFT) est ensuite affiné en utilisant l'apprentissage par renforcement.
    * Le modèle de récompense entraîné à l'étape précédente sert de fonction de récompense de l'environnement.
    * L'agent d'apprentissage par renforcement (le modèle de langage) génère des réponses aux invites, et le modèle de récompense évalue ces réponses.
    * L'algorithme d'apprentissage par renforcement (souvent Proximal Policy Optimization - PPO) met à jour la politique du modèle de langage (sa façon de générer du texte) pour maximiser les récompenses prédites par le modèle de récompense. Cela encourage le modèle de langage à générer des sorties plus alignées sur les préférences humaines.
    * Pour empêcher que le réglage fin par apprentissage par renforcement ne s'écarte trop du comportement du modèle SFT (ce qui pourrait conduire à des résultats indésirables), un terme de régularisation (par exemple, une pénalité de divergence KL) est souvent inclus dans l'objectif de l'apprentissage par renforcement.

**Comment faire du RLHF (étapes simplifiées) :**

1.  **Collecter des données de préférence humaine :**
    * Concevez des invites ou des tâches pertinentes pour le comportement d'IA souhaité.
    * Générez plusieurs réponses à ces invites en utilisant votre modèle actuel.
    * Recrutez des annotateurs humains pour comparer ces réponses et indiquer leurs préférences (par exemple, les classer, choisir la meilleure, ou les noter).
    * Stockez ces données sous forme de paires (invite, réponse préférée, réponse moins préférée) ou dans des formats similaires.

2.  **Entraîner un modèle de récompense :**
    * Choisissez une architecture de modèle adaptée pour votre modèle de récompense (souvent un modèle basé sur un transformateur similaire au modèle de langage).
    * Entraînez le modèle de récompense sur les données de préférence humaine collectées. L'objectif est que le modèle de récompense attribue des scores plus élevés aux réponses que les humains ont préférées. Une fonction de perte courante utilisée est basée sur la maximisation de la marge entre les scores des réponses préférées et moins préférées.

3.  **Affiner le modèle de langage avec l'apprentissage par renforcement :**
    * Initialisez votre modèle de langage avec les poids de l'étape SFT (si vous en avez effectué une).
    * Utilisez un algorithme d'apprentissage par renforcement (comme PPO).
    * Pour chaque étape d'entraînement :
        * Échantillonnez une invite.
        * Demandez au modèle de langage de générer une réponse.
        * Utilisez le modèle de récompense entraîné pour obtenir un score de récompense pour la réponse générée.
        * Mettez à jour les paramètres du modèle de langage sur la base du signal de récompense pour encourager les actions (génération de tokens) qui conduisent à des récompenses plus élevées.
        * Incluez un terme de régularisation (par exemple, la divergence KL) pour maintenir la politique mise à jour proche de la politique SFT.

**Exemple de code (conceptuel et simplifié utilisant PyTorch) :**

Il s'agit d'un exemple conceptuel très simplifié pour illustrer les idées principales. Une implémentation complète du RLHF est nettement plus complexe et implique des bibliothèques comme Hugging Face Transformers, Accelerate et des bibliothèques d'apprentissage par renforcement.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# Supposez que vous avez collecté des données de préférence humaine :
# Liste de tuples : (invite, réponse_préférée, réponse_moins_préférée)
donnees_preference = [
    ("Écris une courte histoire sur un chat.", "Moustache le chat vivait dans un cottage douillet...", "Une histoire de chat. Fin."),
    ("Résume cet article :", "L'article discute de...", "Résumé de l'article."),
    # ... plus de données
]

# 1. Charger le modèle de langage pré-entraîné et le tokenizer
nom_modele = "gpt2"  # Ou un autre modèle pré-entraîné approprié
modele_politique = AutoModelForCausalLM.from_pretrained(nom_modele)
tokenizer = AutoTokenizer.from_pretrained(nom_modele)
device = "cuda" if torch.cuda.is_available() else "cpu"
modele_politique.to(device)

# 2. Définir un modèle de récompense simple
class ModeleRecompense(nn.Module):
    def __init__(self, modele_base):
        super().__init__()
        self.modele_base = modele_base.transformer  # Utiliser les couches du transformateur
        self.tete_v = nn.Linear(modele_base.config.n_embd, 1)

    def forward(self, input_ids, masque_attention):
        sorties = self.modele_base(input_ids=input_ids, attention_mask=masque_attention)
        etats_caches_final = sorties.last_hidden_state
        recompense = self.tete_v(etats_caches_final[:, -1])  # Obtenir la récompense du dernier token
        return recompense

modele_recompense = ModeleRecompense(modele_politique)
modele_recompense.to(device)
optimiseur_recompense = optim.AdamW(modele_recompense.parameters(), lr=1e-5)
criteres_recompense = nn.MarginRankingLoss(margin=1.0) # Encourager une récompense plus élevée pour la réponse préférée

# Entraîner le modèle de récompense
nb_epochs_recompense = 3
for epoch in range(nb_epochs_recompense):
    for invite, preferee, moins_preferee in donnees_preference:
        tokens_preferee = tokenizer(invite + preferee, return_tensors="pt", truncation=True, max_length=128).to(device)
        tokens_moins_preferee = tokenizer(invite + moins_preferee, return_tensors="pt", truncation=True, max_length=128).to(device)

        recompense_preferee = modele_recompense(**tokens_preferee)
        recompense_moins_preferee = modele_recompense(**tokens_moins_preferee)

        labels = torch.ones(recompense_preferee.size(0)).to(device) # On veut preferee > moins_preferee
        perte = criteres_recompense(recompense_preferee, recompense_moins_preferee, labels)

        optimiseur_recompense.zero_grad()
        perte.backward()
        optimiseur_recompense.step()
    print(f"Époque Récompense {epoch+1}, Perte : {perte.item()}")

# 3. Réglage fin par Apprentissage par Renforcement (Conceptuel - PPO est complexe)
optimiseur_politique = optim.AdamW(modele_politique.parameters(), lr=5e-6)

nb_episodes_rl = 5
for episode in range(nb_episodes_rl):
    for invite in [data[0] for data in donnees_preference]: # Échantillonner des invites
        tokens_entree = tokenizer(invite, return_tensors="pt").to(device)
        sequences_sortie = modele_politique.generate(
            tokens_entree.input_ids,
            max_length=60,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        reponse_generee = tokenizer.decode(sequences_sortie[0], skip_special_tokens=True)

        tokens_reponse = tokenizer(invite + reponse_generee, return_tensors="pt", truncation=True, max_length=128).to(device)
        recompense = modele_recompense(**tokens_reponse)

        # Mise à jour de la politique (Simplifiée) - En réalité, PPO utilise des méthodes plus sophistiquées
        perte = -recompense.mean() # Essayer de maximiser la récompense
        optimiseur_politique.zero_grad()
        perte.backward()
        optimiseur_politique.step()

    print(f"Épisode RL {episode+1}, Récompense : {recompense.item()}, Réponse : {reponse_generee}")

print("Entraînement RLHF terminé !")
```

**Principaux défis du RLHF :**

* **Collecte de données :** Obtenir des données de préférence humaine de haute qualité et diversifiées peut être coûteux et long.
* **Subjectivité et biais :** Les préférences humaines peuvent être subjectives et contenir des biais, qui peuvent être appris par le modèle de récompense.
* **Détournement de récompense :** L'agent d'apprentissage par renforcement pourrait trouver des moyens d'exploiter le modèle de récompense qui ne sont pas alignés sur les véritables préférences humaines.
* **Évolutivité :** Mettre le RLHF à l'échelle pour de très grands modèles et jeux de données nécessite des ressources computationnelles importantes et une ingénierie minutieuse.
* **Instabilité :** L'entraînement des modèles RLHF peut être instable et nécessiter un réglage minutieux des hyperparamètres.

Malgré ces défis, le RLHF s'est avéré être une technique puissante pour aligner les modèles d'IA sur les valeurs humaines et est un composant clé dans le développement de modèles de langage de pointe comme ChatGPT et d'autres.