---
audio: false
generated: true
lang: fr
layout: post
title: Exemple d'apprentissage par renforcement
translated: true
type: note
---

Ci-dessous, je vais présenter quelques exemples conceptuels simples d'Apprentissage par Renforcement (RL) suivis d'un exemple de code Python de base utilisant un scénario simple. Le RL implique qu'un agent apprend à maximiser une récompense en interagissant avec un environnement, donc les exemples et le code refléteront cela.

### Exemples Simples d'Apprentissage par Renforcement

1.  **Un enfant qui apprend à marcher**
    - **Agent** : L'enfant.
    - **Environnement** : Le sol ou la pièce.
    - **Action** : Faire un pas, ramper ou rester immobile.
    - **Récompense** : Avancer (+1), tomber (-1).
    - **Apprentissage** : L'enfant apprend par essais et erreurs que faire des pas équilibrés permet d'avancer.

2.  **Entraîner un bras robotisé à saisir des objets**
    - **Agent** : Le bras robotisé.
    - **Environnement** : Une table avec des objets.
    - **Action** : Se déplacer vers le haut, le bas, la gauche, la droite, ou saisir.
    - **Récompense** : Saisir un objet avec succès (+10), le faire tomber (-5).
    - **Apprentissage** : Le bras ajuste ses mouvements pour maximiser les saisies réussies.

3.  **Jeu de Grille (Grid World)**
    - **Agent** : Un personnage dans une grille.
    - **Environnement** : Une grille 3x3 avec un objectif et des obstacles.
    - **Action** : Se déplacer vers le haut, le bas, la gauche ou la droite.
    - **Récompense** : Atteindre l'objectif (+10), heurter un mur (-1).
    - **Apprentissage** : Le personnage apprend le chemin le plus court vers l'objectif.

---

### Exemple de Code Python Simple : Q-Learning dans un Monde en Grille

Voici une implémentation de base du Q-Learning, un algorithme populaire de RL, dans un "monde" 1D où un agent se déplace à gauche ou à droite pour atteindre un objectif. L'agent apprend en mettant à jour une table Q en fonction des récompenses.

```python
import numpy as np
import random

# Configuration de l'environnement : monde 1D avec 5 positions (0 à 4), objectif à la position 4
state_space = 5  # Positions : [0, 1, 2, 3, 4]
action_space = 2  # Actions : 0 = aller à gauche, 1 = aller à droite
goal = 4

# Initialiser la table Q avec des zéros (états x actions)
q_table = np.zeros((state_space, action_space))

# Hyperparamètres
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
min_exploration_rate = 0.01
episodes = 1000

# Fonction de récompense
def get_reward(state):
    if state == goal:
        return 10  # Grande récompense pour avoir atteint l'objectif
    return -1  # Petite pénalité pour chaque étape

# Fonction step : Déplacer l'agent et obtenir le nouvel état
def step(state, action):
    if action == 0:  # Aller à gauche
        new_state = max(0, state - 1)
    else:  # Aller à droite
        new_state = min(state_space - 1, state + 1)
    reward = get_reward(new_state)
    done = (new_state == goal)
    return new_state, reward, done

# Boucle d'entraînement
for episode in range(episodes):
    state = 0  # Commencer à la position 0
    done = False
    
    while not done:
        # Exploration vs Exploitation
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, action_space - 1)  # Explorer
        else:
            action = np.argmax(q_table[state])  # Exploiter
        
        # Prendre une action et observer le résultat
        new_state, reward, done = step(state, action)
        
        # Mettre à jour la table Q en utilisant la formule du Q-learning
        old_value = q_table[state, action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state, action] = new_value
        
        # Passer au nouvel état
        state = new_state
    
    # Réduire le taux d'exploration
    exploration_rate = max(min_exploration_rate, exploration_rate * exploration_decay)

# Tester la politique apprise
state = 0
steps = 0
print("Testing the learned policy:")
while state != goal:
    action = np.argmax(q_table[state])
    state, reward, done = step(state, action)
    steps += 1
    print(f"Step {steps}: Moved to state {state}, Action: {'Left' if action == 0 else 'Right'}")
print(f"Reached goal in {steps} steps!")

# Afficher la table Q
print("\nLearned Q-table:")
print(q_table)
```

---

### Explication du Code

1.  **Environnement** : Une ligne 1D avec 5 positions (0 à 4). L'objectif est à la position 4.
2.  **Actions** : L'agent peut se déplacer à gauche (0) ou à droite (1).
3.  **Récompenses** : +10 pour atteindre l'objectif, -1 pour chaque étape (pour encourager l'efficacité).
4.  **Table Q** : Une table stockant les récompenses futures attendues pour chaque paire état-action.
5.  **Q-Learning** : L'agent met à jour la table Q en utilisant la formule :  
    `Q(s, a) = (1 - α) * Q(s, a) + α * (récompense + γ * max(Q(s', a')))`, où :
    - `α` = taux d'apprentissage (learning rate)
    - `γ` = facteur d'actualisation (discount factor)
    - `s` = état actuel, `a` = action, `s'` = état suivant
6.  **Exploration vs Exploitation** : L'agent choisit parfois des actions aléatoires (exploration) et utilise parfois la table Q (exploitation), contrôlé par `exploration_rate`.

---

### Exemple de Sortie

```
Testing the learned policy:
Step 1: Moved to state 1, Action: Right
Step 2: Moved to state 2, Action: Right
Step 3: Moved to state 3, Action: Right
Step 4: Moved to state 4, Action: Right
Reached goal in 4 steps!

Learned Q-table:
[[-2.5   2.3]
 [-1.8   4.5]
 [-1.2   6.8]
 [-0.5   9. ]
 [ 0.    0. ]]
```

L'agent apprend à toujours se déplacer vers la droite à partir de n'importe quelle position de départ pour atteindre l'objectif efficacement. La table Q montre des valeurs plus élevées pour les actions "se déplacer à droite" à mesure que l'on s'approche de l'objectif.

Il s'agit d'un exemple très basique, mais il capture l'essence du RL. Pour des scénarios plus complexes (par exemple, des grilles 2D ou des jeux), vous devriez étendre les espaces d'états et d'actions en conséquence !