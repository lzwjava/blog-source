---
audio: false
generated: true
lang: hi
layout: post
title: रीइन्फोर्समेंट लर्निंग उदाहरण
translated: true
type: note
---

नीचे, मैं रीइन्फोर्समेंट लर्निंग (RL) के कुछ सरल अवधारणात्मक उदाहरण प्रस्तुत करूंगा, जिसके बाद एक सरल परिदृश्य का उपयोग करते हुए एक बुनियादी पायथन कोड उदाहरण दिया जाएगा। RL में एक एजेंट पर्यावरण के साथ बातचीत करके एक पुरस्कार को अधिकतम करना सीखता है, इसलिए उदाहरण और कोड इसी को दर्शाएंगे।

### रीइन्फोर्समेंट लर्निंग के सरल उदाहरण

1.  **चलना सीखता हुआ बच्चा**
    - **एजेंट**: बच्चा।
    - **पर्यावरण**: फर्श या कमरा।
    - **क्रिया**: एक कदम उठाना, रेंगना, या स्थिर खड़े रहना।
    - **पुरस्कार**: आगे बढ़ना (+1), गिरना (-1)।
    - **सीख**: बच्चा प्रयास और त्रुटि के माध्यम से सीखता है कि संतुलित कदम उठाने से प्रगति होती है।

2.  **वस्तुओं को उठाने के लिए एक रोबोट भुजा को प्रशिक्षित करना**
    - **एजेंट**: रोबोट भुजा।
    - **पर्यावरण**: वस्तुओं वाली एक मेज।
    - **क्रिया**: ऊपर, नीचे, बाएं, दाएं हिलना या पकड़ना।
    - **पुरस्कार**: सफलतापूर्वक एक वस्तु उठाना (+10), उसे गिरा देना (-5)।
    - **सीख**: भुजा सफलतापूर्वक पकड़ने को अधिकतम करने के लिए अपनी हरकतों को समायोजित करती है।

3.  **ग्रिड वर्ल्ड गेम**
    - **एजेंट**: एक ग्रिड में एक चरित्र।
    - **पर्यावरण**: एक लक्ष्य और बाधाओं वाला 3x3 ग्रिड।
    - **क्रिया**: ऊपर, नीचे, बाएं, या दाएं हिलना।
    - **पुरस्कार**: लक्ष्य तक पहुंचना (+10), दीवार से टकराना (-1)।
    - **सीख**: चरित्र लक्ष्य तक पहुंचने का सबसे छोटा रास्ता सीखता है।

---

### सरल पायथन कोड उदाहरण: एक ग्रिड वर्ल्ड में Q-लर्निंग

यहां Q-लर्निंग, एक लोकप्रिय RL एल्गोरिदम, का एक बुनियादी कार्यान्वयन है, जो एक सरल 1D "दुनिया" में है जहां एक एजेंट एक लक्ष्य तक पहुंचने के लिए बाएं या दाएं चलता है। एजेंट पुरस्कारों के आधार पर Q-टेबल को अपडेट करके सीखता है।

```python
import numpy as np
import random

# Environment setup: 1D world with 5 positions (0 to 4), goal at position 4
state_space = 5  # Positions: [0, 1, 2, 3, 4]
action_space = 2  # Actions: 0 = move left, 1 = move right
goal = 4

# Initialize Q-table with zeros (states x actions)
q_table = np.zeros((state_space, action_space))

# Hyperparameters
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
min_exploration_rate = 0.01
episodes = 1000

# Reward function
def get_reward(state):
    if state == goal:
        return 10  # Big reward for reaching the goal
    return -1  # Small penalty for each step

# Step function: Move agent and get new state
def step(state, action):
    if action == 0:  # Move left
        new_state = max(0, state - 1)
    else:  # Move right
        new_state = min(state_space - 1, state + 1)
    reward = get_reward(new_state)
    done = (new_state == goal)
    return new_state, reward, done

# Training loop
for episode in range(episodes):
    state = 0  # Start at position 0
    done = False
    
    while not done:
        # Exploration vs Exploitation
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, action_space - 1)  # Explore
        else:
            action = np.argmax(q_table[state])  # Exploit
        
        # Take action and observe result
        new_state, reward, done = step(state, action)
        
        # Update Q-table using the Q-learning formula
        old_value = q_table[state, action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state, action] = new_value
        
        # Move to new state
        state = new_state
    
    # Decay exploration rate
    exploration_rate = max(min_exploration_rate, exploration_rate * exploration_decay)

# Test the learned policy
state = 0
steps = 0
print("Testing the learned policy:")
while state != goal:
    action = np.argmax(q_table[state])
    state, reward, done = step(state, action)
    steps += 1
    print(f"Step {steps}: Moved to state {state}, Action: {'Left' if action == 0 else 'Right'}")
print(f"Reached goal in {steps} steps!")

# Print the Q-table
print("\nLearned Q-table:")
print(q_table)
```

---

### कोड की व्याख्या

1.  **पर्यावरण**: 5 स्थितियों (0 से 4) वाली एक 1D लाइन। लक्ष्य स्थिति 4 पर है।
2.  **क्रियाएं**: एजेंट बाएं (0) या दाएं (1) चल सकता है।
3.  **पुरस्कार**: लक्ष्य तक पहुंचने के लिए +10, प्रत्येक कदम के लिए -1 (दक्षता को प्रोत्साहित करने के लिए)।
4.  **Q-टेबल**: एक तालिका जो प्रत्येक स्थिति-क्रिया जोड़ी के लिए अपेक्षित भविष्य के पुरस्कारों को संग्रहीत करती है।
5.  **Q-लर्निंग**: एजेंट सूत्र का उपयोग करके Q-टेबल को अपडेट करता है:  
    `Q(s, a) = (1 - α) * Q(s, a) + α * (reward + γ * max(Q(s', a')))`, जहां:
    - `α` = लर्निंग रेट
    - `γ` = डिस्काउंट फैक्टर
    - `s` = वर्तमान स्थिति, `a` = क्रिया, `s'` = अगली स्थिति

6.  **एक्सप्लोरेशन बनाम एक्सप्लॉइटेशन**: एजेंट कभी-कभी यादृच्छिक क्रियाएं चुनता है (एक्सप्लोरेशन) और कभी-कभी Q-टेबल का उपयोग करता है (एक्सप्लॉइटेशन), जिसे `exploration_rate` द्वारा नियंत्रित किया जाता है।

---

### नमूना आउटपुट

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

एजेंट किसी भी शुरुआती स्थिति से लक्ष्य तक कुशलतापूर्वक पहुंचने के लिए हमेशा दाएं चलना सीख जाता है। Q-टेबल लक्ष्य के करीब पहुंचने पर "दाएं चलें" क्रियाओं के लिए उच्च मान दिखाती है।

यह एक बहुत ही बुनियादी उदाहरण है, लेकिन यह RL का सार पकड़ता है। अधिक जटिल परिदृश्यों (जैसे, 2D ग्रिड या गेम) के लिए, आप राज्य और क्रिया स्थानों को तदनुसार विस्तारित करेंगे!