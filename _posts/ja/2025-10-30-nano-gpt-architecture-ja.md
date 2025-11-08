---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ナノGPTモデルアーキテクチャ概要
translated: true
type: note
---

### NanoGPT モデルアーキテクチャ概要

NanoGPTは、PyTorchでGPT-2に似たデコーダー専用のトランスフォーマーモデルを実装しています。アーキテクチャは`model.py`ファイルで定義され、ハイパーパラメータを設定する設定可能な`GPTConfig`を使用します。デフォルト設定（例: "gpt2"バリアント）では以下を使用します:

- **トランスフォーマーブロック数**: 12 (`n_layer = 12`)
- **埋め込み次元（レイヤーサイズ）**: 768 (`n_embd = 768`)
- **アテンションヘッド数**: 12 (`n_head = 12`)
- **MLP中間層サイズ**: 3072 (`n_embd * 4`、拡張係数は4)

各トランスフォーマーブロック（クラス`Block`）は、残差接続とレイヤー正規化を備えた標準的なデコーダーブロックです。以下を含みます:
- **LayerNorm 1** (`ln1`): セルフアテンションの前に適用
- **マルチヘッドセルフアテンション** (`attn`): 先読みを防ぐための因果的（マスクされた）アテンション
- アテンション後の残差加算
- **LayerNorm 2** (`ln2`): MLPの前に適用
- **MLP** (`mlp`): シンプルなフィードフォワードネットワーク
- MLP後の残差加算

全体モデル（クラス`GPT`）は、トークンと位置埋め込みの後にこれらの12ブロックを積み重ね、最終的なLayerNorm（`ln_f`）と語彙サイズへの線形投影が続きます。

#### MLP構造
MLP（`Block`内のクラス`MLP`）は2層のフィードフォワードネットワークです:
- 第一線形層 (`c_fc`): `n_embd` (768) から中間サイズ (3072) へ投影
- GELU活性化: 第一投影後に要素ごとに適用
- 第二線形層 (`c_proj`): 3072から`n_embd` (768) へ戻す投影

これは前述の「fc -> gelu -> projection」パターンに従います。

#### フォワードパスの流れ
フォワードパスは残差スタイルで、事前正規化（サブレイヤーの前のLayerNorm）です。以下に高レベルの内訳を示します:

1. **メインフォワード (GPT.forward)**:
   - トークン埋め込み: 入力トークン（形状`[B, T]`）→ 埋め込み（形状`[B, T, n_embd]`）
   - 位置埋め込み: トークン埋め込みに加算
   - `n_layer` (12) 個のトランスフォーマーブロックのスタックを通して渡す: 各々に対して`x = block(x)`
   - 最終LayerNorm: `x = self.ln_f(x)`
   - 線形投影: `logits = self.lm_head(x)` → 出力形状`[B, T, vocab_size]`
   
   スニペット（簡略化）:
   ```python
   def forward(self, idx, targets=None):
       # ... 埋め込み + 位置
       for block in self.blocks:
           x = block(x)
       x = self.ln_head(x)
       logits = self.head(x)
       # ... ターゲットがある場合の損失
       return logits
   ```

2. **トランスフォーマーブロック内のフォワード (Block.forward)**:
   - 入力`x`に`ln1`を適用
   - セルフアテンション: `x = x + attn(ln1(x))`（残差）
   - 結果に`ln2`を適用
   - MLP: `x = x + mlp(ln2(x))`（残差）
   
   スニペット（簡略化）:
   ```python
   def forward(self, x):
       x = x + self.attn(self.ln1(x))
       x = x + self.mlp(self.ln2(x))
       return x
   ```

3. **セルフアテンション内のフォワード (MultiheadAttention.forward)**:
   - LayerNorm入力 → Q, K, V投影を計算（線形層`c_attn`）
   - ヘッドに分割、因果マスクを適用、スケールドドットプロダクトアテンション
   - ヘッドを連結、`c_proj`で投影して戻す
   - 残差加算（ただしブロック内では外部で加算）
   
   キーポイント: 因果マスクにより将来のトークンが無視される。出力形状は`[B, T, n_embd]`として保持。
   
   スニペット（コアアテンション計算、簡略化）:
   ```python
   def forward(self, x):
       B, T, C = x.shape
       qkv = self.c_attn(x).split(self.n_embd, dim=2)  # Q,K,V
       # ... ヘッドに変形、マスク、attn = q @ k.transpose / sqrt
       # attn = attn.masked_fill(mask == 0, -1e9)
       # y = attn @ v
       # ... 連結と投影
       return self.c_proj(y.reshape(B, T, C))
   ```

4. **MLP内のフォワード (MLP.forward)**:
   - 第一投影: `x = self.c_fc(x)` → 中間サイズへ
   - GELU: `x = F.gelu(x)`
   - 第二投影: `x = self.c_proj(x)` → `n_embd`へ戻す
   
   スニペット:
   ```python
   def forward(self, x):
       x = self.c_fc(x)
       x = F.gelu(x)
       x = self.c_proj(x)
       return x
   ```

この設定はGPT-2のアーキテクチャに密接に従っており、デフォルト設定では約124Mパラメータを持ちます。正確なコードについては、リポジトリを確認してください。

[model.pyソース](https://github.com/karpathy/nanoGPT/blob/master/model.py)