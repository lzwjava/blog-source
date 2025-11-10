---
audio: false
generated: true
lang: ja
layout: post
title: ジムナジウム：強化学習のためのモダンジム
translated: true
type: note
---

Gymライブラリは、強化学習（RL）のための人気のあるPythonツールキットを指します。これは元々OpenAIによって開発され、エージェントが環境と相互作用して報酬を最大化するための意思決定を学ぶ機械学習の一分野である強化学習において、標準化されたAPIとベンチマーク環境のコレクション（ゲーム、ロボティクスシミュレーション、古典的な制御問題など）を提供します。これにより、研究者や開発者は環境を一から構築することなく、RLアルゴリズムの開発、テスト、比較を容易に行うことができます。

主な機能:
- **環境**: CartPole（棒のバランス維持）、Atariゲーム、MuJoCo物理シミュレーションなどの事前構築済みタスク
- **APIの簡潔さ**: `gym.make("環境名")`で環境を作成し、`reset()`で開始、`step(アクション)`で相互作用と観測/報酬の取得、`render()`で可視化を行うメソッドを使用
- **拡張性**: ユーザーはGymの基底クラスをサブクラス化してカスタム環境を作成可能
- **統合性**: Stable Baselines、RLlib、PyTorch/TensorFlowなどのライブラリと連携してRLエージェントを実装

しかし、元のOpenAI Gymは現在積極的にメンテナンスされておらず、2021年頃から非推奨となっています。代わりに**Gymnasium**の使用が推奨されています。これはFarama Foundationによる直接的なフォークおよび継続版で、完全な互換性（`import gymnasium as gym`としてインポート可能）を持ち、並列トレーニングのための改良されたベクトル化環境、厳格な型チェック、継続的なアップデートなどの改善が加えられています。インストールは`pip install gymnasium`で行い、特定の環境には`pip install gymnasium[atari]`のような追加オプションを使用します。

Pythonでの基本的な使用例:
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()  # ランダムなアクション（エージェントはより良いものを学習する）
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

RLを始める場合、現在ではほとんどのプロジェクトでGymnasiumが第一選択肢となります。

[OpenAI Gym GitHub](https://github.com/openai/gym)  
[Gymnasium Documentation](https://gymnasium.farama.org/)  
[Gym Documentation (Legacy)](https://www.gymlibrary.dev/)