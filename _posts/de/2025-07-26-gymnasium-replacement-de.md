---
audio: false
generated: true
lang: de
layout: post
title: 'Gymnasium: Die moderne Turnhalle für RL'
translated: true
type: note
---

Die Gym-Bibliothek bezieht sich auf ein beliebiges Python-Toolkit, das ursprünglich von OpenAI für Reinforcement Learning (RL) entwickelt wurde, ein Teilgebiet des maschinellen Lernens, bei dem Agenten lernen, Entscheidungen zu treffen, indem sie mit Umgebungen interagieren, um Belohnungen zu maximieren. Es bietet eine standardisierte API und eine Sammlung von Benchmark-Umgebungen (wie Spiele, Robotersimulationen und klassische Steuerungsprobleme), um RL-Algorithmen zu entwickeln, zu testen und zu vergleichen. Dies erleichtert es Forschern und Entwicklern, Prototypen zu erstellen, ohne Umgebungen von Grund auf zu bauen.

Wichtige Merkmale sind:
- **Umgebungen**: Vorgefertigte Aufgaben wie CartPole (Balancieren eines Stabs), Atari-Spiele oder MuJoCo-Physiksimulationen.
- **API-Einfachheit**: Man erstellt eine Umgebung mit `gym.make("Umgebungsname")` und verwendet dann Methoden wie `reset()` zum Starten, `step(Aktion)` zur Interaktion und zum Erhalten von Beobachtungen/Belohnungen und `render()` zur Visualisierung.
- **Erweiterbarkeit**: Benutzer können benutzerdefinierte Umgebungen erstellen, indem sie die Basisklassen von Gym unterklassifizieren.
- **Integration**: Funktioniert gut mit Bibliotheken wie Stable Baselines, RLlib oder PyTorch/TensorFlow zur Implementierung von RL-Agenten.

Allerdings wird das ursprüngliche OpenAI Gym nicht mehr aktiv gepflegt und ist seit etwa 2021 veraltet. Es wird empfohlen, **Gymnasium** zu verwenden, einen direkten Fork und die Fortführung durch die Farama Foundation. Gymnasium ist vollständig kompatibel (man kann es als `import gymnasium as gym` importieren), fügt Verbesserungen hinzu wie bessere vektorisierte Umgebungen für paralleles Training, strengere Typüberprüfung und laufende Updates. Die Installation erfolgt über `pip install gymnasium`, mit Extras wie `pip install gymnasium[atari]` für spezifische Umgebungen.

Beispiel für die grundlegende Verwendung in Python:
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()  # Zufällige Aktion (ein Agent würde bessere lernen)
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

Wenn Sie mit RL beginnen, ist Gymnasium heute die erste Wahl für die meisten Projekte.

[OpenAI Gym GitHub](https://github.com/openai/gym)  
[Gymnasium Dokumentation](https://gymnasium.farama.org/)  
[Gym Dokumentation (Legacy)](https://www.gymlibrary.dev/)