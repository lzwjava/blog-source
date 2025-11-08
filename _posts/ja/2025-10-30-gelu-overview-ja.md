---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GELU活性化関数の概要
translated: true
type: note
---

### GELUとは？

Gaussian Error Linear Unit（GELU）は、ニューラルネットワークで使用される滑らかな活性化関数であり、特にBERTやGPTシリーズなどのTransformerベースのモデルで利用されます。2016年に研究者Dan HendrycksとKevin Gimpelによって導入され、線形変換の利点とガウス（正規）分布に着想を得た確率的重み付けを組み合わせています。ReLU（負の入力に対してゼロを出力する）のような単純な活性化関数とは異なり、GELUは負の値に対しても小さな勾配の流れを許容し、勾配消失のような問題を軽減し収束を改善することで、深いネットワークにおける性能向上をもたらします。

#### 数学的定義
GELUの核心となる式は以下の通りです：

\\[
\text{GELU}(x) = x \cdot \Phi(x)
\\]

ここで、\\(\Phi(x)\\)は標準正規分布の累積分布関数（CDF）です：

\\[
\Phi(x) = \frac{1}{2} \left[ 1 + \erf\left( \frac{x}{\sqrt{2}} \right) \right]
\\]

ここで、\\(\erf\\)は誤差関数であり、ガウス分布がステップ関数をどの程度よく近似するかを測定します。これによりGELUは確率的性質を持ちます：負の入力をReLUほど厳しく「ドロップ」せず、正の入力はそのまま保持します。

計算効率のために、シグモイドベースの近似式がよく使用されます：

\\[
\text{GELU}(x) \approx x \cdot \sigma(1.702x)
\\]

ここで、\\(\sigma\\)はシグモイド関数です。

#### GELUを使用する理由
- **滑らかさ**： どこでも微分可能であり、最適化を助けます。
- **非単調性**： 負の値をわずかに抑制しますが、ゼロにはせず、情報を保持します。
- **実証的な利点**： 自然言語処理などのタスクにおいてReLUやELUを上回り、大規模モデルではより高速な学習と高い精度を実現します。
- **欠点**： erfやシグモイドの計算により、ReLUよりも計算コストがわずかに高くなります。

実際には、PyTorchやTensorFlowなどのライブラリには組み込みのGELU実装（例: `torch.nn.GELU()`）があります。

#### 参考文献
- [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415)
- [GELU Explained](https://www.baeldung.com/cs/gelu-activation-function)
- [GELU Activation](https://medium.com/@shauryagoel/gelu-gaussian-error-linear-unit-4ec59fb2e47c)