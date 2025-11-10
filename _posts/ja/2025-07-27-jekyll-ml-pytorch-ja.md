---
audio: false
generated: true
image: false
lang: ja
layout: post
title: JekyllブログをPyTorchで強化
translated: true
type: note
---

### PyTorchを使用してJekyllブログをML/AIで改善する

Jekyllブログ（静的サイトジェネレーター）を運用している場合、レコメンデーションや分類のようなML/AI機能を統合するには工夫が必要です。Jekyllは静的なHTMLをビルドするため、動的要素（例：リアルタイムレコメンデーション）はクライアントサイドのJavaScript、またはJekyllプラグインやスクリプトを通じたビルドプロセス中の事前計算が必要になる可能性があります。LLM APIを避け、PyTorchを使用した独自のニューラルネットワークに焦点を当てたいとのこと—素晴らしい方針です。これにより全てがローカルで実行され、カスタマイズも可能になります。以下では、PyTorch実装に焦点を当てた実用的なアイデアを概説します。これらは、NumPy（データ処理用）のような基本的なライブラリにアクセスでき、高度なNLPライブラリ（Hugging Faceなど）がセットアップに含まれていなくても（必要に応じてローカルに追加は可能）、単純なトークン化または手動でテキスト前処理を扱えることを前提としています。

おそらく、Jekyllのビルドプロセス中（MakefileフックやGitHub Actions経由でデプロイする場合）に実行されるPythonスクリプト（例：`scripts/`ディレクトリ内）を作成することになるでしょう。例えば、`_posts/`内のMarkdown投稿を処理し、JSONデータを生成し、Liquidテンプレートを介してサイトに注入します。

#### 1. PyTorch分類器を使用した記事の分類
単純なニューラルネットワーク分類器をトレーニングして、投稿を自動的に分類します（例：「ML」、「Notes」、「Latex」などのトピックへ）。これは教師あり学習です：トレーニングデータとして投稿の一部に手動でラベルを付ける必要があります。ラベルがない場合は、教師なしクラスタリングから始めてください（後述）。

**手順:**
- **データ準備:** `_posts/`内のMarkdownファイルを解析します。テキストコンテンツを抽出します（frontmatterはスキップ）。データセットを作成：（テキスト, ラベル）のペアのリスト。最初は約50〜100のラベル付き例でCSVまたはリストを使用。
- **前処理:** テキストをトークン化（単純なスペース/空白文字での分割）、語彙を構築、数値インデックスに変換。ワンホットエンコーディングまたは基本的な埋め込みを使用。
- **モデル:** 多クラス分類のためのPyTorchにおける基本的なフィードフォワードニューラルネットワーク。
- **トレーニング:** ローカルマシンでトレーニング。クロスエントロピー損失とAdamオプティマイザを使用。
- **統合:** ビルド中にスクリプトを実行して全ての投稿を分類し、`categories.json`ファイルを生成し、Jekyllでページにタグ付けしたりカテゴリインデックスを作成するために使用。

**PyTorchコードスニペットの例（`scripts/categorize_posts.py`のようなスクリプト内）:**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os
from collections import Counter

# ステップ1: データの読み込みと前処理（簡略化）
def load_posts(posts_dir='_posts'):
    texts = []
    labels = []  # 手動ラベルを仮定: 0=ML, 1=Notes, など
    for file in os.listdir(posts_dir):
        if file.endswith('.md'):
            with open(os.path.join(posts_dir, file), 'r') as f:
                content = f.read().split('---')[2].strip()  # frontmatterをスキップ
                texts.append(content)
                # プレースホルダー: 辞書またはCSVからラベルを読み込み
                labels.append(0)  # 実際のラベルで置き換え
    return texts, labels

texts, labels = load_posts()
# 語彙の構築（上位1000語）
all_words = ' '.join(texts).lower().split()
vocab = {word: idx for idx, word in enumerate(Counter(all_words).most_common(1000))}
vocab_size = len(vocab)

# テキストをベクトルに変換（bag-of-words）
def text_to_vec(text):
    vec = np.zeros(vocab_size)
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

X = np.array([text_to_vec(t) for t in texts])
y = torch.tensor(labels, dtype=torch.long)

# ステップ2: モデル定義
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Classifier(vocab_size, num_classes=3)  # num_classesを調整

# ステップ3: トレーニング
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()
X_tensor = torch.tensor(X, dtype=torch.float32)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# ステップ4: 新しい投稿に対する推論
def classify_post(text):
    vec = torch.tensor(text_to_vec(text), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        pred = model(vec).argmax(1).item()
    return pred  # カテゴリ名にマッピングして戻す

# モデルを保存: torch.save(model.state_dict(), 'classifier.pth')
# ビルドスクリプト内: 全ての投稿を分類しJSONに書き出し
```

**改善点:** 精度を向上させるには、単語埋め込み（PyTorchで単純なEmbeddingレイヤーをトレーニング）を使用するか、レイヤーを追加します。ラベルがない場合は、クラスタリング（例：埋め込みに対するKMeans—次のセクションを参照）に切り替えてください。このスクリプトをMakefileで実行: `jekyll build && python scripts/categorize_posts.py`。

#### 2. PyTorch埋め込みを使用したレコメンデーションシステム
読者に類似記事を推薦します（例：「こちらもおすすめ…」）。コンテンツベースのレコメンデーションを使用：各投稿の埋め込みを学習し、類似度（コサイン距離）を計算。ユーザーデータは不要—投稿コンテンツのみ。

**手順:**
- **データ:** 上記と同じ—投稿からテキストを抽出。
- **モデル:** PyTorchでオートエンコーダーをトレーニングし、テキストを低次元埋め込み（例：64次元ベクトル）に圧縮。
- **トレーニング:** 再構成損失を最小化して意味のある表現を学習。
- **レコメンデーション:** 特定の投稿に対して、埋め込み空間内で最近傍を検索。
- **統合:** ビルド中に埋め込みを事前計算し、JSONに保存。サイト上でJSを使用してレコメンデーションを表示（または静的リストにはLiquidを使用）。

**PyTorchコードスニペットの例（`scripts/recommend_posts.py`内）:**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# 上記からload_postsとtext_to_vecを再利用

texts, _ = load_posts()  # ラベルは無視
X = np.array([text_to_vec(t) for t in texts])
X_tensor = torch.tensor(X, dtype=torch.float32)

# オートエンコーダーモデル
class Autoencoder(nn.Module):
    def __init__(self, input_size, embedding_size=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Linear(256, embedding_size)
        )
        self.decoder = nn.Sequential(
            nn.Linear(embedding_size, 256),
            nn.ReLU(),
            nn.Linear(256, input_size)
        )
    
    def forward(self, x):
        emb = self.encoder(x)
        return self.decoder(emb)

model = Autoencoder(vocab_size)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(200):
    optimizer.zero_grad()
    reconstructed = model(X_tensor)
    loss = loss_fn(reconstructed, X_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# 埋め込みを取得
with torch.no_grad():
    embeddings = model.encoder(X_tensor).numpy()

# 推薦: 投稿iに対して、上位3つの類似記事を検索
similarities = cosine_similarity(embeddings)
for i in range(len(texts)):
    rec_indices = similarities[i].argsort()[-4:-1][::-1]  # 自分を除く上位3つ
    print(f'Recs for post {i}: {rec_indices}')

# Jekyll用に埋め込みをJSONに保存
import json
with open('embeddings.json', 'w') as f:
    json.dump({'embeddings': embeddings.tolist(), 'posts': [f'post_{i}' for i in range(len(texts))]}, f)
```

**改善点:** より良い埋め込みには変分オートエンコーダーを使用。ユーザービュー（分析経由）がある場合は、PyTorchでの行列分解モデルを用いた協調フィルタリングを追加。クライアントサイド：JSONをJSで読み込み、パーソナライゼーションのためにオンザフライで類似度を計算。

#### 3. PyTorchを使用したその他のアイデア
- **自動タグ付けのための教師なしクラスタリング:** ラベル付けが面倒な場合、埋め込み（上記オートエンコーダーから）＋KMeansクラスタリングを使用して投稿をトピックごとにグループ化。埋め込みはPyTorch、クラスタリングはNumPy/SciPy。
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=5)
  clusters = kmeans.fit_predict(embeddings)
  # クラスターに基づいてタグを割り当て
  ```
  統合：スクリプト経由でfrontmatterにタグを生成。

- **セマンティック検索の強化:** クエリと投稿を同様に埋め込み、検索バーにコサイン類似度を使用。投稿埋め込みを事前計算；クエリ埋め込みにはJSを使用（ただしPyTorchはPythonなので、ONNX.js経由のJS推論用にモデルをONNXにエクスポートするか、検索を静的のままに）。

- **投稿要約:** ペア（全文, 手動要約）データでseq2seqモデル（PyTorchのRNN/LSTM）をトレーニング。大規模データセットなしでは困難ですが、自身の投稿から小規模で開始。抜粋生成に使用。

**一般的なヒント:**
- **スケーラビリティ:** 小規模ブログの場合、CPUでトレーニング；PyTorchは問題なく処理。`torch.save`でモデルを保存し、推論用に読み込み。
- **ビルド統合:** Makefileに追加: `train: python scripts/train_models.py` その後 `build: jekyll build && python scripts/generate_features.py`。
- **制限事項:** 高度なNLP（例：トランスフォーマー）なしでは結果は基本的—`torchtext`の追加または手動のGloVe埋め込みをローカルで検討。自身の`ml/`や`notes/`ディレクトリでテスト。
- **デプロイメント:** GitHub Pagesの場合、CIでスクリプトを実行。動的機能については、軽量なFlaskバックエンドの追加を検討しますが、それは静的Jekyllから外れます。

詳細（例：投稿数、トピック）を共有いただければ、これらをさらに改良できます！