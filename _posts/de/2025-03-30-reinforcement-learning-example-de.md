---
audio: false
generated: true
lang: de
layout: post
title: Beispiel für Bestärkendes Lernen
translated: true
type: note
---

Nachfolgend finden Sie einige einfache konzeptionelle Beispiele für Reinforcement Learning (RL), gefolgt von einem einfachen Python-Code-Beispiel mit einem einfachen Szenario. Beim RL lernt ein Agent durch Interaktion mit einer Umgebung, eine Belohnung zu maximieren. Die Beispiele und der Code spiegeln dies wider.

### Einfache Beispiele für Reinforcement Learning

1.  **Ein Kind lernt das Laufen**
    -   **Agent**: Das Kind.
    -   **Umgebung**: Der Boden oder das Zimmer.
    -   **Aktion**: Einen Schritt machen, krabbeln oder still stehen.
    -   **Belohnung**: Vorwärtsbewegung (+1), Hinfallen (-1).
    -   **Lernen**: Das Kind lernt durch Versuch und Irrtum, dass ausbalancierte Schritte zum Fortschritt führen.

2.  **Training eines Roboterarms zum Aufheben von Objekten**
    -   **Agent**: Der Roboterarm.
    -   **Umgebung**: Ein Tisch mit Objekten.
    -   **Aktion**: Hoch, runter, links, rechts bewegen oder greifen.
    -   **Belohnung**: Erfolgreiches Aufheben eines Objekts (+10), Fallenlassen (-5).
    -   **Lernen**: Der Arm passt seine Bewegungen an, um erfolgreiche Greifvorgänge zu maximieren.

3.  **Grid-World-Spiel**
    -   **Agent**: Ein Charakter in einem Raster.
    -   **Umgebung**: Ein 3x3-Raster mit einem Ziel und Hindernissen.
    -   **Aktion**: Hoch, runter, links oder rechts bewegen.
    -   **Belohnung**: Das Ziel erreichen (+10), gegen eine Wand laufen (-1).
    -   **Lernen**: Der Charakter lernt den kürzesten Weg zum Ziel.

---

### Einfaches Python-Code-Beispiel: Q-Learning in einer Grid World

Hier ist eine einfache Implementierung von Q-Learning, einem beliebten RL-Algorithmus, in einer einfachen 1D-"Welt", in der sich ein Agent nach links oder rechts bewegt, um ein Ziel zu erreichen. Der Agent lernt, indem er eine Q-Tabelle basierend auf Belohnungen aktualisiert.

```python
import numpy as np
import random

# Umgebungsaufbau: 1D-Welt mit 5 Positionen (0 bis 4), Ziel bei Position 4
state_space = 5  # Positionen: [0, 1, 2, 3, 4]
action_space = 2  # Aktionen: 0 = links bewegen, 1 = rechts bewegen
goal = 4

# Initialisiere Q-Tabelle mit Nullen (Zustände x Aktionen)
q_table = np.zeros((state_space, action_space))

# Hyperparameter
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
min_exploration_rate = 0.01
episodes = 1000

# Belohnungsfunktion
def get_reward(state):
    if state == goal:
        return 10  # Große Belohnung für das Erreichen des Ziels
    return -1  # Kleine Strafe für jeden Schritt

# Schritt-Funktion: Bewege den Agenten und erhalte neuen Zustand
def step(state, action):
    if action == 0:  # Links bewegen
        new_state = max(0, state - 1)
    else:  # Rechts bewegen
        new_state = min(state_space - 1, state + 1)
    reward = get_reward(new_state)
    done = (new_state == goal)
    return new_state, reward, done

# Trainingsschleife
for episode in range(episodes):
    state = 0  # Starte bei Position 0
    done = False
    
    while not done:
        # Exploration vs. Exploitation
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, action_space - 1)  # Explore
        else:
            action = np.argmax(q_table[state])  # Exploit
        
        # Führe Aktion aus und beobachte Ergebnis
        new_state, reward, done = step(state, action)
        
        # Aktualisiere Q-Tabelle mit der Q-Learning-Formel
        old_value = q_table[state, action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state, action] = new_value
        
        # Wechsle zum neuen Zustand
        state = new_state
    
    # Reduziere Explorationsrate
    exploration_rate = max(min_exploration_rate, exploration_rate * exploration_decay)

# Teste die gelernte Policy
state = 0
steps = 0
print("Testing the learned policy:")
while state != goal:
    action = np.argmax(q_table[state])
    state, reward, done = step(state, action)
    steps += 1
    print(f"Step {steps}: Moved to state {state}, Action: {'Left' if action == 0 else 'Right'}")
print(f"Reached goal in {steps} steps!")

# Gib die Q-Tabelle aus
print("\nLearned Q-table:")
print(q_table)
```

---

### Erklärung des Codes

1.  **Umgebung**: Eine 1D-Linie mit 5 Positionen (0 bis 4). Das Ziel ist bei Position 4.
2.  **Aktionen**: Der Agent kann sich nach links (0) oder rechts (1) bewegen.
3.  **Belohnungen**: +10 für das Erreichen des Ziels, -1 für jeden Schritt (um Effizienz zu fördern).
4.  **Q-Tabelle**: Eine Tabelle, die die erwarteten zukünftigen Belohnungen für jedes Zustands-Aktions-Paar speichert.
5.  **Q-Learning**: Der Agent aktualisiert die Q-Tabelle mit der Formel:  
    `Q(s, a) = (1 - α) * Q(s, a) + α * (Belohnung + γ * max(Q(s', a')))`, wobei:
    -   `α` = Lernrate
    -   `γ` = Diskontfaktor
    -   `s` = aktueller Zustand, `a` = Aktion, `s'` = nächster Zustand
6.  **Exploration vs. Exploitation**: Der Agent wählt manchmal zufällige Aktionen (Exploration) und manchmal verwendet er die Q-Tabelle (Exploitation), gesteuert durch die `exploration_rate`.

---

### Beispielhafte Ausgabe

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

Der Agent lernt, sich von jeder Startposition aus immer nach rechts zu bewegen, um das Ziel effizient zu erreichen. Die Q-Tabelle zeigt höhere Werte für "rechts bewegen"-Aktionen an, je näher man dem Ziel kommt.

Dies ist ein sehr einfaches Beispiel, aber es erfasst die Essenz von RL. Für komplexere Szenarien (z. B. 2D-Raster oder Spiele) würden Sie den Zustands- und Aktionsraum entsprechend erweitern!