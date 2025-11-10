---
audio: false
generated: true
lang: fr
layout: post
title: 'Gymnase : La Salle de Sport Moderne pour l''Apprentissage par Renforcement'
translated: true
type: note
---

La bibliothèque Gym fait référence à une boîte à outils Python populaire initialement développée par OpenAI pour l'apprentissage par renforcement (RL), un sous-domaine du machine learning où les agents apprennent à prendre des décisions en interagissant avec des environnements pour maximiser des récompenses. Elle fournit une API standardisée et une collection d'environnements de référence (comme des jeux, des simulations robotiques et des problèmes de contrôle classiques) pour développer, tester et comparer des algorithmes de RL. Cela facilite le prototypage pour les chercheurs et les développeurs sans avoir à construire des environnements à partir de zéro.

Principales fonctionnalités :
- **Environnements** : Tâches pré-construites telles que CartPole (équilibrer un mât), les jeux Atari, ou les simulations physiques MuJoCo.
- **Simplicité de l'API** : Vous créez un environnement avec `gym.make("NomEnvironnement")`, puis utilisez des méthodes comme `reset()` pour démarrer, `step(action)` pour interagir et obtenir des observations/récompenses, et `render()` pour visualiser.
- **Extensibilité** : Les utilisateurs peuvent créer des environnements personnalisés en sous-classant les classes de base de Gym.
- **Intégration** : Fonctionne bien avec des bibliothèques comme Stable Baselines, RLlib, ou PyTorch/TensorFlow pour implémenter des agents de RL.

Cependant, le OpenAI Gym original n'est plus activement maintenu et a été déprécié depuis environ 2021. Il est recommandé d'utiliser **Gymnasium**, qui est un fork direct et une continuation par la Farama Foundation. Gymnasium est entièrement compatible (vous pouvez l'importer avec `import gymnasium as gym`), ajoute des améliorations comme de meilleurs environnements vectorisés pour l'entraînement parallèle, une vérification de types plus stricte et des mises à jour continues. L'installation se fait via `pip install gymnasium`, avec des extras comme `pip install gymnasium[atari]` pour des environnements spécifiques.

Exemple d'utilisation basique en Python :
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()  # Action aléatoire (l'agent apprendrait de meilleures actions)
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

Si vous débutez en RL, Gymnasium est le choix recommandé aujourd'hui pour la plupart des projets.

[OpenAI Gym GitHub](https://github.com/openai/gym)  
[Documentation Gymnasium](https://gymnasium.farama.org/)  
[Documentation Gym (Legacy)](https://www.gymlibrary.dev/)