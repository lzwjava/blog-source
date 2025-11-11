---
audio: false
generated: true
lang: ja
layout: post
title: 強化学習の例
translated: true
type: note
---

以下に、強化学習（RL）の簡単な概念例と、単純なシナリオを用いた基本的なPythonコード例を示します。RLは、エージェントが環境と対話しながら報酬を最大化することを学習するものなので、例とコードはそれを反映しています。

### 強化学習の簡単な例

1. **歩き方を学ぶ子供**  
   - **エージェント**: 子供  
   - **環境**: 床や部屋  
   - **アクション**: 一歩踏み出す、這う、じっとする  
   - **報酬**: 前に進む (+1)、転ぶ (-1)  
   - **学習**: 子供は試行錯誤を通じて、バランスの取れた歩行が前進につながることを学ぶ

2. **物をつかむように訓練するロボットアーム**  
   - **エージェント**: ロボットアーム  
   - **環境**: 物が置かれたテーブル  
   - **アクション**: 上下左右に動く、把持する  
   - **報酬**: 物をうまくつかむ (+10)、落とす (-5)  
   - **学習**: アームは把持の成功率を最大化するように動きを調整する

3. **グリッドワールドゲーム**  
   - **エージェント**: グリッド内のキャラクター  
   - **環境**: ゴールと障害物がある3x3グリッド  
   - **アクション**: 上下左右に移動  
   - **報酬**: ゴールに到達 (+10)、壁にぶつかる (-1)  
   - **学習**: キャラクターはゴールへの最短経路を学ぶ

---

### 簡単なPythonコード例: グリッドワールドでのQ学習

ここでは、人気のあるRLアルゴリズムであるQ学習の基本的な実装を示します。これは、エージェントが左右に移動してゴールに到達する1次元の「世界」です。エージェントは報酬に基づいてQテーブルを更新することで学習します。

```python
import numpy as np
import random

# 環境設定: 5つの位置 (0から4) を持つ1次元世界、ゴールは位置4
state_space = 5  # 位置: [0, 1, 2, 3, 4]
action_space = 2  # アクション: 0 = 左に移動, 1 = 右に移動
goal = 4

# Qテーブルをゼロで初期化 (状態数 x アクション数)
q_table = np.zeros((state_space, action_space))

# ハイパーパラメータ
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
min_exploration_rate = 0.01
episodes = 1000

# 報酬関数
def get_reward(state):
    if state == goal:
        return 10  # ゴール到達で大きな報酬
    return -1  # 各ステップに対する小さなペナルティ

# ステップ関数: エージェントを移動させ、新しい状態を取得
def step(state, action):
    if action == 0:  # 左に移動
        new_state = max(0, state - 1)
    else:  # 右に移動
        new_state = min(state_space - 1, state + 1)
    reward = get_reward(new_state)
    done = (new_state == goal)
    return new_state, reward, done

# 訓練ループ
for episode in range(episodes):
    state = 0  # 位置0から開始
    done = False
    
    while not done:
        # 探索と活用
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, action_space - 1)  # 探索
        else:
            action = np.argmax(q_table[state])  # 活用
        
        # アクションを実行し、結果を観測
        new_state, reward, done = step(state, action)
        
        # Q学習の式を用いてQテーブルを更新
        old_value = q_table[state, action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state, action] = new_value
        
        # 新しい状態に移動
        state = new_state
    
    # 探索率を減衰
    exploration_rate = max(min_exploration_rate, exploration_rate * exploration_decay)

# 学習したポリシーをテスト
state = 0
steps = 0
print("学習したポリシーをテスト:")
while state != goal:
    action = np.argmax(q_table[state])
    state, reward, done = step(state, action)
    steps += 1
    print(f"ステップ {steps}: 状態 {state} に移動, アクション: {'左' if action == 0 else '右'}")
print(f"{steps} ステップでゴールに到達!")

# Qテーブルを表示
print("\n学習したQテーブル:")
print(q_table)
```

---

### コードの説明

1. **環境**: 5つの位置 (0から4) を持つ1次元の線。ゴールは位置4。
2. **アクション**: エージェントは左 (0) または右 (1) に移動できる。
3. **報酬**: ゴール到達で+10、各ステップで-1 (効率を促すため)。
4. **Qテーブル**: 各状態-アクションペアに対する期待される将来の報酬を格納するテーブル。
5. **Q学習**: エージェントは次の式を使用してQテーブルを更新する:  
   `Q(s, a) = (1 - α) * Q(s, a) + α * (報酬 + γ * max(Q(s', a')))`、ここで:
   - `α` = 学習率
   - `γ` = 割引率
   - `s` = 現在の状態, `a` = アクション, `s'` = 次の状態

6. **探索と活用**: エージェントは時々ランダムなアクションを選択し (探索)、時々Qテーブルを使用する (活用)。これは `exploration_rate` によって制御される。

---

### 出力例
```
学習したポリシーをテスト:
ステップ 1: 状態 1 に移動, アクション: 右
ステップ 2: 状態 2 に移動, アクション: 右
ステップ 3: 状態 3 に移動, アクション: 右
ステップ 4: 状態 4 に移動, アクション: 右
4 ステップでゴールに到達!

学習したQテーブル:
[[-2.5   2.3]
 [-1.8   4.5]
 [-1.2   6.8]
 [-0.5   9. ]
 [ 0.    0. ]]
```

エージェントは、どの開始位置からでも効率的にゴールに到達するために常に右に移動することを学びます。Qテーブルは、ゴールに近づくにつれて「右に移動」アクションに対する値が高くなることを示しています。

これは非常に基本的な例ですが、RLの本質を捉えています。より複雑なシナリオ (例: 2Dグリッドやゲーム) では、状態空間とアクション空間をそれに応じて拡張します。