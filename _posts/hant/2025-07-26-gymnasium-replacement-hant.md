---
audio: false
generated: true
lang: hant
layout: post
title: 健身室：強化學習的現代訓練場
translated: true
type: note
---

Gym 函式庫是一個由 OpenAI 最初開發的熱門 Python 強化學習工具包。強化學習是機器學習的一個子領域，智能體透過與環境互動來學習決策，以最大化獎勵。該函式庫提供標準化 API 和一系列基準環境（例如遊戲、機器人模擬和經典控制問題），用於開發、測試和比較強化學習演算法。這使得研究人員和開發者能夠更輕鬆地進行原型開發，而無需從頭構建環境。

主要功能包括：
- **環境**：預建任務，例如 CartPole（平衡桿）、Atari 遊戲或 MuJoCo 物理模擬。
- **API 簡潔性**：您可以使用 `gym.make("EnvironmentName")` 創建環境，然後使用 `reset()` 開始、`step(action)` 進行互動並獲取觀察結果/獎勵，以及 `render()` 進行視覺化。
- **可擴展性**：使用者可以透過繼承 Gym 的基礎類別來創建自訂環境。
- **整合性**：可與 Stable Baselines、RLlib 或 PyTorch/TensorFlow 等函式庫良好配合，以實現強化學習智能體。

然而，原始的 OpenAI Gym 已不再積極維護，並在 2021 年左右被棄用。建議使用 **Gymnasium**，這是 Farama Foundation 的直接分支和延續版本。Gymnasium 完全相容（您可以透過 `import gymnasium as gym` 導入），並增加了改進功能，例如更好的向量化環境以進行平行訓練、更嚴格的類型檢查以及持續更新。可透過 `pip install gymnasium` 安裝，並使用如 `pip install gymnasium[atari]` 的額外指令來安裝特定環境。

Python 基本使用範例：
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()  # 隨機動作（智能體會學習更好的動作）
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

如果您剛開始接觸強化學習，Gymnasium 是現今大多數專案的首選工具。

[OpenAI Gym GitHub](https://github.com/openai/gym)  
[Gymnasium 文件](https://gymnasium.farama.org/)  
[Gym 文件（舊版）](https://www.gymlibrary.dev/)