---
audio: false
generated: true
lang: hant
layout: post
title: 蒙地卡羅樹搜尋
translated: true
type: note
---

讓我們深入探討**蒙特卡羅樹搜尋（MCTS）**——這是一種在決策問題中廣泛使用的強大演算法，尤其在遊戲和人工智慧領域。我將逐步拆解其原理，涵蓋其起源、核心概念、運作機制、實作方式、優缺點及應用場景，助你全面掌握這項技術。

---

### 什麼是蒙特卡羅樹搜尋？

蒙特卡羅樹搜尋是一種啟發式搜尋演算法，結合了樹搜尋的精確性與蒙特卡羅方法的隨機性。它特別適用於決策空間龐大複雜、無法窮舉所有可能性（如極小化極大演算法）的問題。MCTS 會逐步建立部分搜尋樹，並透過隨機模擬來引導探索方向，聚焦於具潛力的決策路徑。

- **起源**：MCTS 於 2000 年代中期崛起，Rémi Coulom（2006年）等人貢獻卓著。其聲名大噪是因應用於圍棋 AI（如 AlphaGo），徹底改變電腦處理龐大狀態空間遊戲的方式。
- **關鍵應用場景**：圍棋、象棋、撲克等遊戲，乃至現實中的規劃或優化問題。

---

### 核心概念

MCTS 運作於一棵**樹結構**上：
- **節點**代表遊戲狀態或決策點。
- **邊**代表觸發新狀態的動作或決策。
- **根節點**是當前決策的起始狀態。

此演算法透過統計方法平衡**探索**（嘗試新決策）與**利用**（聚焦已知優質決策）。它不需完美的評估函數，僅需具備模擬結果的能力。

---

### MCTS 的四階段流程

MCTS 在每次模擬循環中依序執行四個步驟：

#### 1. **選擇**
- 從根節點開始，遍歷樹結構至葉節點（未完全展開或終止狀態的節點）。
- 使用**選擇策略**挑選子節點，最常見的是**應用於樹的上置信區間（UCT）**公式：
  \\[
  UCT = \bar{X}_i + C \sqrt{\frac{\ln(N)}{n_i}}
  \\]
  - \\(\bar{X}_i\\)：節點的平均獎勵（勝率）。
  - \\(n_i\\)：節點的訪問次數。
  - \\(N\\)：父節點的訪問次數。
  - \\(C\\)：探索常數（通常設為 \\(\sqrt{2}\\) 或依問題調整）。
- UCT 平衡了利用（\\(\bar{X}_i\\)）與探索（\\(\sqrt{\frac{\ln(N)}{n_i}}\\) 項）。

#### 2. **展開**
- 若選擇的葉節點非終止狀態且存在未訪問的子節點，則展開該節點，新增一個或多個子節點（代表未嘗試的決策）。
- 通常每次迭代僅新增一個子節點以控制記憶體使用。

#### 3. **模擬（推演）**
- 從新展開的節點開始，執行**隨機模擬**至終止狀態（如勝/負/平手）。
- 模擬採用輕量策略（常為均勻隨機決策），因精確評估每個狀態的成本過高。
- 記錄模擬結果（如勝局為 +1、平局為 0、敗局為 -1）。

#### 4. **反向傳播**
- 將模擬結果反向更新至樹中所有經過的節點：
  - 增加訪問計數（\\(n_i\\)）。
  - 更新總獎勵（如勝局總數或平均勝率）。
- 此步驟強化樹結構對潛力路徑的認知。

重複以上步驟數千次後，根據訪問次數最多或平均獎勵最高的子節點，從根節點選出最佳決策。

---

### MCTS 運作範例

以簡易井字遊戲為例：
1. **根節點**：當前棋盤狀態（如 X 回合且棋盤部分填滿）。
2. **選擇**：UCT 根據過往模擬選擇潛力決策（如將 X 置於中央）。
3. **展開**：為未嘗試的決策新增子節點（如 O 在角落回應）。
4. **模擬**：執行隨機決策直至遊戲結束（如 X 獲勝）。
5. **反向傳播**：更新統計數據——中央決策獲得 +1 獎勵，訪問次數增加。

經過數千次迭代後，樹結構顯示中央落點勝率最高，因此被選為最終決策。

---

### 虛擬碼

以下是基礎 MCTS 實作：

```python
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.reward = 0

def mcts(root, iterations):
    for _ in range(iterations):
        node = selection(root)
        if not node.state.is_terminal():
            node = expansion(node)
        reward = simulation(node.state)
        backpropagation(node, reward)
    return best_child(root)

def selection(node):
    while node.children and not node.state.is_terminal():
        node = max(node.children, key=uct)
    return node

def expansion(node):
    untried_moves = node.state.get_untried_moves()
    if untried_moves:
        move = random.choice(untried_moves)
        new_state = node.state.apply_move(move)
        child = Node(new_state, parent=node)
        node.children.append(child)
        return child
    return node

def simulation(state):
    current = state.clone()
    while not current.is_terminal():
        move = random.choice(current.get_moves())
        current.apply_move(move)
    return current.get_result()

def backpropagation(node, reward):
    while node:
        node.visits += 1
        node.reward += reward
        node = node.parent

def uct(child):
    if child.visits == 0:
        return float('inf')  # 優先探索未訪問節點
    return (child.reward / child.visits) + 1.41 * math.sqrt(math.log(child.parent.visits) / child.visits)

def best_child(node):
    return max(node.children, key=lambda c: c.visits)  # 亦可使用 reward/visits
```

---

### MCTS 的優勢

1. **隨時可中止演算法**：隨時停止皆能根據當前統計數據給出合理決策。
2. **無需評估函數**：依賴模擬而非領域特定啟發式方法。
3. **可擴展性**：適用於龐大狀態空間（如圍棋的 \\(10^{170}\\) 種可能局面）。
4. **自適應性**：隨迭代次數增加，自然聚焦於潛力分支。

---

### MCTS 的劣勢

1. **計算密集**：需大量模擬以獲取優質結果，未經優化時可能耗時。
2. **探索深度不足**：若迭代次數有限，可能忽略深層策略。
3. **隨機性依賴**：粗糙的推演策略可能扭曲結果；模擬準確度影響品質。
4. **記憶體使用**：樹結構增長在記憶體受限環境中可能成為瓶頸。

---

### 強化與變體

為克服劣勢，MCTS 常透過以下方式強化：
- **推演啟發式**：融入領域知識（如井字遊戲中優先選擇中央位置）取代純隨機。
- **平行化**：並行執行多組模擬（根平行化或樹平行化）。
- **RAVE（快速行動價值評估）**：共享相似決策的統計數據以加速收斂。
- **與神經網絡整合**：如 AlphaGo 使用神經網絡引導選擇（策略網絡）與評估狀態（價值網絡）。

---

### 應用領域

1. **遊戲**：
   - 圍棋（AlphaGo 的突破性應用）。
   - 象棋（與神經網絡結合，如 Leela Chess Zero）。
   - 撲克（透過調整處理不完全資訊）。
2. **機器人學**：不確定環境中的路徑規劃。
3. **優化問題**：解決排程或資源分配等組合問題。
4. **即時策略**：動態不可預測情境中的決策制定。

---

### 實作實用建議

- **調整 \\(C\\) 常數**：根據問題微調 UCT 探索常數（\\(C = \sqrt{2}\\) 可作為起點）。
- **限制樹結構增長**：修剪節點或限制展開以管理記憶體。
- **優化推演過程**：使用輕量模擬或啟發式方法節省時間。
- **測試迭代次數**：嘗試 100、1,000 或 10,000 次迭代，權衡速度與品質。

---

### 總結

MCTS 是一種多功能且優雅的演算法，在傳統搜尋方法難以應對的領域中表現卓越。其精髓在於簡潔性——透過隨機模擬與漸進生長的樹結構指引——卻能擴展至解決 AI 領域中最棘手的問題。無論是開發遊戲 AI 或處理規劃任務，MCTS 皆提供了穩健的起點，尤其當與神經網絡等現代強化技術結合時。

如果你有興趣，我可以帶你深入特定實作（如井字遊戲），或進一步探討 UCT 調參、平行化 MCTS 等細節。你覺得如何？