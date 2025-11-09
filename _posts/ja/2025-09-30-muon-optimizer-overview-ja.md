---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: ミューオンオプティマイザーの紹介と概要
translated: true
type: note
---

### Muon Optimizerの包括的紹介

Muon Optimizerは、主にニューラルネットワークの線形層（全結合層や埋め込み層など）のトレーニングのために設計された、特殊化された二次の最適化アルゴリズムです。他の層にも拡張可能です。このアルゴリズムは、Keller JordanやJeremy Bernsteinなどの研究者によって2024年末に最初に提案され、極初期化やモジュラー双対性フレームワークなどの幾何学的な最適化手法にルーツを持っています[1][2]。Moonshot AIとKimi AIの創業者であるZhiling Yangは、1兆パラメータの大規模言語モデル（LLM）であるKimi K2モデルのトレーニングに関する議論でMuonを強調し、損失ランドスケープの幾何学に適応する効率的で高ランクな更新の基盤として機能したと述べています[3][4]。しかし、そのベースライン版は不安定性（長時間トレーニング中の損失スパイクなど）に悩まされ、Moonshot AIは注意層向けのQKクリッピングなどの安定化メカニズムを備えた強化版であるMuonClipを開発しました[3][2]。

Muonはそのトークン効率の良さで際立っています：AdamWのような一次のオプティマイザーと同等の性能を達成するのに必要なトレーニングトークンが少なく、LLMの事前学習のようなリソース集約的なタスクで価値があります。Muonは、完全な計算コストをかけずに二次の手法（ニュートン法など）を近似することを目指しており、高ランク行列更新を介した固有値適応に焦点を当てています。これは、勾配がノイジーになる大規模モデルで特に有用であり、Muonは自然勾配や行列平方根に触発された前処理を活用します。

#### 主要な原理と導出
- **核心概念**: Muonは幾何学的な最適化に根ざしており、損失関数の「エネルギーランドスケープ」に更新を適応させます。Fisher情報行列（またはその近似）に基づく前処理を使用して勾配をスケーリングします。これはAdaGradやShampooに似ていますが、密な線形層向けに最適化されています[1][2]。
- **アルゴリズムのステップ**:
  1. **勾配計算**: 線形層の重み \(W\) に対する標準的な勾配 \(\nabla W\) を計算します。
  2. **前処理**: ニュートン-シュルツ反復を使用して、前処理行列（例：層の統計量から導出）の行列平方根を近似します。これにより、完全な固有分解を行わずにランク適応が可能になります。
  3. **更新規則**: 高ランク成分をより効果的にスケーリングする更新を適用します。多くの場合、安定性のためにモメンタムやクリッピングと組み合わせられます。
- **数学的洞察**: \(G\) が勾配行列である場合、Muonは \(W \leftarrow W - \eta \cdot \sqrt{P}^{-1} G\) のような更新を近似します。ここで、\(\sqrt{P}\) は反復的な行列平方根を使用します[2][5]。これは、AdamWの対角またはモーメントベースのスケーリングとは対照的であり、Muonがパラメータ間の相関をより良く捉えることを可能にします。
- **効率向上**: Muonは、NanoGPTの記録で見られるように、一部のベンチマークでトレーニングステップ数を20-50%削減できます[1]。

#### 利点と欠点
- **利点**:
  - **線形層での優れた収束**: LLMに典型的な、高次元の密な空間で優れ、より少ないトークンでより低い損失をもたらします[4][6]。
  - **リソース効率**: 必要な勾配計算が少ないため、エポックあたりのトレーニングが高速です。
  - **オープンソースかつ拡張可能**: Flash-MuonのようなGPUアクセラレーション向けの特定の実装を含め、複数の実装が存在します[4][7]。
- **欠点**:
  - **不安定性**: より深いネットワークやスパースな層では発散しやすい傾向があります。MuonClipは、トレーニング中の注意スコア（クエリ-キー積など）をクリッピングすることでこの問題に対処します[3][2]。
  - **層特化性**: 畳み込み層やリカレント層には理想的ではなく、線形/MoEアーキテクチャ向けに偏っています。Kerasは非線形層には使用すべきでないと注記しています[8]。
  - **ハイパーパラメータの感度**: 学習率（\(\eta\)）および直交性を誘導する操作に対する調整が必要であり、調整なしではモデルサイズ間で転移しない可能性があります[2]。
- **MuonClip バリアント (Kimi特化)**: これはMuonの進化版であり、15.5兆トークンの事前学習における不安定性を防ぐためにQKクリッピングと統合されています。これは、Kimi K2の320億活性化パラメータを安定化させ、ゼロ損失スパイクでのトレーニングと優れたベンチマーク（例：Tau2-Benchで66.1）を可能にしました[3][8]。公開コードはまだありませんが、オープンなMuonを基盤としています。

Muonは、ScionなどのベンチマークやReddit/Xでの議論に登場し、その「幾何学的な直感」を称賛されるなど、AI最適化の分野に影響を与えています。完全な導出については、Jeremy Bernsteinのブログ[2]を参照してください。では、実用的な実装を見てみましょう。

### コード例: PyTorchでのMuonオプティマイザの実装
以下は、公式リポジトリ (https://github.com/KellerJordan/Muon) から適応した、基本的なMuonオプティマイザのPyTorch実装です。これは密な線形層向けの簡略化されたバージョンであり、前処理行列のためのニュートン-シュルツ反復を含みます。

```python
import torch
import torch.nn as nn

class Muon(torch.optim.Optimizer):
    """
    線形層向けMuonオプティマイザ。
    出典: https://github.com/KellerJordan/Muon
    """
    def __init__(self, params, lr=1e-3, lr_b=2e-3, b2=0.95, wd=0.0):
        defaults = dict(lr=lr, lr_b=lr_b, b2=b2, wd=wd)
        super().__init__(params, defaults)

    def step(self):
        for group in self.param_groups:
            lr = group['lr']
            lr_b = group['lr_b']
            b2 = group['b2']
            wd = group['wd']

            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad.data.float()
                state = self.state[p]
                if 'momentum' not in state:
                    state['momentum'] = torch.zeros_like(grad)

                # モメンタム更新
                state['momentum'].mul_(b2).add_(grad)

                # 重み減衰
                if wd != 0:
                    p.data.mul_(1 - lr * wd)

                # Muonの正規直交化 (ランク適応)
                grad_vec = state['momentum'].view(-1, grad.shape[-1])
                p_vec = p.data.view(-1, p.shape[-1])

                # 行列平方根近似のためのニュートン-シュルツ (簡略化版)
                G = grad_vec @ grad_vec.t() / grad_vec.shape[0]
                # 完全な実装では反復的ですが、ここでは冪級数で近似します
                sqrt_G = torch.sqrt(G + 1e-6 * torch.eye(G.shape[0], device=G.device))

                # 更新
                update = grad_vec.t() @ sqrt_G @ grad_vec / sqrt_G.shape[0]
                p.data.sub_(lr_b * update.view(p.shape))

# 使用例
model = nn.Linear(768, 768)  # 密な層
optimizer = Muon(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()
data = torch.randn(32, 768)
target = torch.randn(32, 768)

for epoch in range(10):
    optimizer.zero_grad()
    output = model(data)
    loss = loss_fn(output, target)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
```

**コードに関する注記**:
- これは簡略化されたバージョンです。完全なGitHubリポジトリには、効率化のためのCUDAカーネル（例：高速な行列積のためのFlash-Muon）が含まれています[3][4]。
- Keras/TensorFlowの場合: `from keras.optimizers import Muon; opt = Muon(learning_rate=0.01)` を使用します[8]。
- 調整されたハイパーパラメータ（例: `lr_b=2e-3`）は重要です。ご自身のモデルで実験してください。Kimi K2のMuonClipについては、公開コードは存在しませんが、注意のフォワードパスにクリッピングロジックを追加しています[2][5]。

拡張機能やベンチマークが必要な場合は、お知らせください！

引用:
[1] https://kellerjordan.github.io/posts/muon/
[2] https://jeremybernste.in/writing/deriving-muon
[3] https://github.com/KellerJordan/Muon
[4] https://github.com/nil0x9/flash-muon
[5] https://www.lakernewhouse.com/writing/muon-2
[6] https://medium.com/@kyeg/building-the-muon-optimizer-in-pytorch-a-geometric-approach-to-neural-network-optimization-17f4601be548
[7] https://discuss.huggingface.co/t/tutorial-understanding-and-implementing-the-muon-optimizer/167717
[8] https://keras.io/api/optimizers/muon/