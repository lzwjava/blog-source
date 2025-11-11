---
audio: false
generated: true
lang: fr
layout: post
title: DeepSeek R1
translated: true
type: note
---

DeepSeek R1 adopte une approche novatrice de l'apprentissage par renforcement (RL) qui met fortement l'accent sur les **capacités de raisonnement** des grands modèles de langage (LLM). Leur technique diffère du Reinforcement Learning from Human Feedback (RLHF) traditionnel à plusieurs égards clés.

Voici une analyse des techniques utilisées par DeepSeek dans l'apprentissage par renforcement de R1 :

**1. Apprentissage par Renforcement Pur (RL) pour le Raisonnement Initial (DeepSeek-R1-Zero) :**

* **Pas de Supervised Fine-tuning (SFT) Initial sur des Instructions :** Contrairement à de nombreux LLM qui subissent d'abord un SFT sur des instructions rédigées par des humains, DeepSeek-R1-Zero a été entraîné avec du **RL pur** directement sur le modèle de base (DeepSeek-V3-Base).
* **Group Relative Policy Optimization (GRPO) :** Ils ont utilisé GRPO comme algorithme RL principal. GRPO est conçu pour être plus efficace que le Proximal Policy Optimization (PPO) en éliminant le besoin d'un réseau critique séparé. Il estime les récompenses de base en comparant un groupe de sorties générées, attribuant des scores relatifs basés sur leur qualité. Cela encourage le modèle à générer de meilleures réponses par rapport à ses propres tentatives précédentes.
* **Système de Récompense Basé sur des Règles :** Au lieu de s'appuyer uniquement sur les préférences humaines pour la phase RL initiale, DeepSeek-R1-Zero a utilisé un **système de récompense basé sur des règles**. Ce système s'est principalement concentré sur :
    * **Récompenses de Précision :** Récompenser le modèle pour avoir fourni des réponses correctes, en particulier dans les tâches avec des solutions vérifiables comme les problèmes de mathématiques (vérifier si la réponse finale est correcte).
    * **Récompenses de Format :** Récompenser le modèle pour avoir respecté un format de sortie spécifique, en particulier l'utilisation des balises `` pour encadrer son processus de raisonnement. Cela a encouragé l'émergence du raisonnement en chaîne (chain-of-thought).
* **Comportements de Raisonnement Émergents :** Cette approche de RL pur a permis à DeepSeek-R1-Zero de développer naturellement des compétences de raisonnement impressionnantes, y compris l'auto-vérification, la réflexion et la génération de longues explications en chaîne de pensée, sans démonstrations humaines explicites pour ces comportements.

**2. Entraînement Multi-Étapes pour Améliorer la Lisibilité et les Capacités Générales (DeepSeek-R1) :**

Pour remédier aux limitations de DeepSeek-R1-Zero (comme une mauvaise lisibilité et le mélange de langues), DeepSeek-R1 a employé un pipeline d'entraînement multi-étapes plus complet :

* **Fine-tuning sur des Données de Démarrage à Froid (Cold-Start) :** Avant la phase RL principale, le modèle de base a été affiné sur un petit jeu de données de haute qualité, contenant des exemples de raisonnement en chaîne de pensée longs, rédigés par des humains (ou générés et raffinés). Ces données de "démarrage à froid" ont aidé à guider le modèle vers la production d'étapes de raisonnement plus lisibles et cohérentes.
* **Apprentissage par Renforcement Orienté Raisonnement (Deuxième Étape RL) :** Le modèle a ensuite subi une deuxième phase de RL à grande échelle (similaire à DeepSeek-R1-Zero) mais avec une **récompense de cohérence linguistique** supplémentaire. Cette récompense pénalisait le modèle pour avoir mélangé les langues dans son processus de raisonnement.
* **Supervised Fine-tuning (SFT) :** Après le RL orienté raisonnement, le modèle a été encore affiné sur un jeu de données diversifié incluant à la fois des données de raisonnement (synthétisées en utilisant l'échantillonnage par rejet du modèle RL, jugées par DeepSeek-V3) et des données générales non liées au raisonnement (augmentées avec une chaîne de pensée). Cette étape SFT visait à améliorer l'utilité et l'innocuité du modèle tout en préservant ses solides capacités de raisonnement.
* **RL pour Tous les Scénarios (Troisième Étape RL) :** Une phase RL finale a été conduite en utilisant des prompts provenant d'un plus large éventail de scénarios pour affiner davantage les capacités globales du modèle et son alignement avec les comportements souhaités.

**Différences Clés par Rapport au RLHF Traditionnel :**

* **Dépendance Réduite envers les Données Extensives de Préférences Humaines :** Bien qu'une certaine évaluation humaine ait pu être impliquée dans le jugement de la qualité des données synthétisées, l'entraînement RL central dans DeepSeek-R1 a largement tiré parti des récompenses basées sur des règles, en particulier dans les étapes initiales. Cela réduit le coût et la complexité de la collecte de grandes quantités de comparaisons directes de préférences humaines.
* **Accent sur le Raisonnement Émergent :** L'approche de RL pur visait à inciter le modèle à *découvrir* lui-même des stratégies de raisonnement efficaces, plutôt que d'apprendre uniquement à partir d'exemples de raisonnement fournis par des humains.
* **Approche Multi-Étapes :** Le pipeline de DeepSeek implique une séquence soigneusement orchestrée de pré-entraînement, de fine-tuning ciblé et de multiples étapes RL avec différents signaux de récompense pour atteindre à la fois un raisonnement solide et des capacités linguistiques générales.

**Code pour Illustrer l'Apprentissage par Renforcement (Conceptuel et Simplifié) :**

Il est difficile de fournir un exemple de code exécutable direct qui réplique entièrement le processus d'entraînement RL de DeepSeek en raison de sa complexité et de son échelle. Cependant, l'extrait conceptuel suivant de type PyTorch illustre l'idée centrale de GRPO et d'une récompense basée sur des règles :

```python
import torch
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# Supposez que vous avez un modèle de langage pré-entraîné et un tokeniseur
model_name = "gpt2"  # Remplacer par un modèle de base plus approprié
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

def generate_responses(prompt, num_responses=4, max_length=128):
    input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = policy_model.generate(
        input_tokens.input_ids,
        max_length=max_length,
        num_return_sequences=num_responses,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return responses

def calculate_accuracy_reward(response):
    # Exemple simplifié pour un problème de math : "What is 2 + 2?"
    if "2 + 2" in response and "4" in response:
        return 1.0
    else:
        return 0.0

def calculate_format_reward(response):
    if "" in response:
        return 0.5
    else:
        return 0.0

def calculate_combined_reward(response):
    accuracy_reward = calculate_accuracy_reward(response)
    format_reward = calculate_format_reward(response)
    return accuracy_reward + format_reward

def train_step(prompt, num_samples=4):
    optimizer.zero_grad()
    responses = generate_responses(prompt, num_samples=num_samples)
    rewards = torch.tensor([calculate_combined_reward(resp) for resp in responses]).float().to(device)

    # Mise à jour de type GRPO simplifiée : Encourager les réponses avec une récompense plus élevée
    best_reward_index = torch.argmax(rewards)
    best_response = responses[best_reward_index]
    inputs = tokenizer(prompt + best_response, return_tensors="pt").to(device)
    outputs = policy_model(**inputs, labels=inputs.input_ids)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    return loss.item(), best_response, rewards.tolist()

# Boucle d'entraînement (très simplifiée)
num_episodes = 10
training_prompts = ["Solve: 2 + 2 = ?", "Explain the concept of gravity