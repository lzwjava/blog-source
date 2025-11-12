---
audio: false
generated: true
lang: hant
layout: post
title: 強化學習範例
translated: true
type: note
---

以下提供幾個強化學習（RL）的簡單概念範例，以及一個使用簡單情境的基本 Python 程式碼範例。強化學習涉及智能體透過與環境互動來學習最大化獎勵，因此這些範例和程式碼將體現這一點。

### 強化學習的簡單範例

1. **孩童學習走路**  
   - **智能體**：孩童。  
   - **環境**：地板或房間。  
   - **動作**：邁出一步、爬行或靜止不動。  
   - **獎勵**：向前移動 (+1)、跌倒 (-1)。  
   - **學習過程**：孩童透過嘗試錯誤學習到保持平衡的步伐能帶來進步。

2. **訓練機械手臂抓取物件**  
   - **智能體**：機械手臂。  
   - **環境**：擺放物件的桌子。  
   - **動作**：向上、向下、向左、向右移動或抓取。  
   - **獎勵**：成功抓取物件 (+10)、掉落物件 (-5)。  
   - **學習過程**：機械手臂調整其動作以最大化成功抓取的次數。

3. **網格世界遊戲**  
   - **智能體**：網格中的角色。  
   - **環境**：包含目標與障礙物的 3x3 網格。  
   - **動作**：向上、向下、向左或向右移動。  
   - **獎勵**：抵達目標 (+10)、撞到牆壁 (-1)。  
   - **學習過程**：角色學習前往目標的最短路徑。

---

### 簡單 Python 程式碼範例：網格世界中的 Q-Learning

以下是一個 Q-Learning（一種流行的 RL 演算法）的基本實現，在一個簡單的一維「世界」中，智能體透過左右移動來抵達目標。智能體透過根據獎勵更新 Q-table 來學習。

```python
import numpy as np
import random

# 環境設定：一維世界，包含 5 個位置 (0 到 4)，目標位於位置 4
state_space = 5  # 位置：[0, 1, 2, 3, 4]
action_space = 2  # 動作：0 = 向左移動，1 = 向右移動
goal = 4

# 初始化 Q-table 為零（狀態 x 動作）
q_table = np.zeros((state_space, action_space))

# 超參數
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
min_exploration_rate = 0.01
episodes = 1000

# 獎勵函數
def get_reward(state):
    if state == goal:
        return 10  # 抵達目標獲得高獎勵
    return -1  # 每一步的小懲罰

# 步驟函數：移動智能體並取得新狀態
def step(state, action):
    if action == 0:  # 向左移動
        new_state = max(0, state - 1)
    else:  # 向右移動
        new_state = min(state_space - 1, state + 1)
    reward = get_reward(new_state)
    done = (new_state == goal)
    return new_state, reward, done

# 訓練循環
for episode in range(episodes):
    state = 0  # 從位置 0 開始
    done = False
    
    while not done:
        # 探索與利用
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, action_space - 1)  # 探索
        else:
            action = np.argmax(q_table[state])  # 利用
        
        # 執行動作並觀察結果
        new_state, reward, done = step(state, action)
        
        # 使用 Q-learning 公式更新 Q-table
        old_value = q_table[state, action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state, action] = new_value
        
        # 移動到新狀態
        state = new_state
    
    # 衰減探索率
    exploration_rate = max(min_exploration_rate, exploration_rate * exploration_decay)

# 測試學習到的策略
state = 0
steps = 0
print("測試學習到的策略：")
while state != goal:
    action = np.argmax(q_table[state])
    state, reward, done = step(state, action)
    steps += 1
    print(f"步驟 {steps}：移動到狀態 {state}，動作：{'向左' if action == 0 else '向右'}")
print(f"在 {steps} 步內抵達目標！")

# 印出 Q-table
print("\n學習到的 Q-table：")
print(q_table)
```

---

### 程式碼解說

1. **環境**：一條包含 5 個位置 (0 到 4) 的一維線段。目標位於位置 4。
2. **動作**：智能體可以向左 (0) 或向右 (1) 移動。
3. **獎勵**：抵達目標獲得 +10，每一步獲得 -1（以鼓勵效率）。
4. **Q-Table**：一個儲存每個狀態-動作對預期未來獎勵的表格。
5. **Q-Learning**：智能體使用以下公式更新 Q-table：  
   `Q(s, a) = (1 - α) * Q(s, a) + α * (reward + γ * max(Q(s', a')))`，其中：
   - `α` = 學習率
   - `γ` = 折扣因子
   - `s` = 當前狀態，`a` = 動作，`s'` = 下一個狀態

6. **探索與利用**：智能體有時選擇隨機動作（探索），有時使用 Q-table（利用），由 `exploration_rate` 控制。

---

### 範例輸出
```
測試學習到的策略：
步驟 1：移動到狀態 1，動作：向右
步驟 2：移動到狀態 2，動作：向右
步驟 3：移動到狀態 3，動作：向右
步驟 4：移動到狀態 4，動作：向右
在 4 步內抵達目標！

學習到的 Q-table：
[[-2.5   2.3]
 [-1.8   4.5]
 [-1.2   6.8]
 [-0.5   9. ]
 [ 0.    0. ]]
```

智能體學習到從任何起始位置始終向右移動以有效率地抵達目標。Q-table 顯示隨著接近目標，「向右移動」動作的值更高。

這是一個非常基礎的範例，但捕捉了強化學習的精髓。對於更複雜的情境（例如二維網格或遊戲），您需要相應地擴展狀態和動作空間！