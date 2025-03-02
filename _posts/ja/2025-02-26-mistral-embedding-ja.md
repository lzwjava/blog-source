---
audio: false
generated: true
lang: ja
layout: post
title: Mistral AIの埋め込み
translated: true
---

Mistral AIの埋め込みAPIを利用して、テキストの意味を捉えた数値表現（埋め込み）を生成することで、埋め込み例を提供することができます。これらの埋め込みは、類似性検出、クラスタリング、分類、検索などのタスクに役立ちます。以下に、Mistral AIの埋め込みエンドポイントを使用して、文のセットの埋め込みを生成し、その類似度を計算する方法を示します。この例は、提供されたコードの構造に基づいていますが、埋め込みに特化しています。以下のドキュメントに従っています: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### 前提条件

例を実行する前に、以下を確認してください:
1. **APIキー**: 有効なMistral AI APIキーを`MISTRAL_API_KEY`環境変数に保存してください。
2. **依存関係**: 必要なPythonパッケージをインストールしてください。以下のコマンドでインストールできます:
   ```bash
   pip install requests numpy
   ```

### 例コード

以下は、3つの文の埋め込みを生成し、そのペアごとの類似度を計算する完全なPythonスクリプトです:

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    Mistral AI埋め込みAPIを呼び出して、テキストのリストの埋め込みを生成します。

    引数:
        texts (list): 埋め込み対象の文字列のリスト。
        model (str): 使用する埋め込みモデル（デフォルト: "mistral-embed"）。

    戻り値:
        list: 埋め込みベクトルのリスト、またはリクエストが失敗した場合はNone。
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("エラー: MISTRAL_API_KEY環境変数が設定されていません。")
        return None

    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "input": texts
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and "data" in response_json:
            embeddings = [item["embedding"] for item in response_json["data"]]
            return embeddings
        else:
            print(f"Mistral Embeddings APIエラー: 無効な応答形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral Embeddings APIエラー: {e}")
        if e.response:
            print(f"応答ステータスコード: {e.response.status_code}")
            print(f"応答コンテンツ: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    2つの埋め込みの類似度をドット積を使用して計算します。

    引数:
        emb1 (list): 第1埋め込みベクトル。
        emb2 (list): 第2埋め込みベクトル。

    戻り値:
        float: 類似度スコア（ドット積、正規化されたベクトルのコサイン類似度に相当）。
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # 埋め込み対象の例テキスト
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]

    # 埋め込みを生成
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # 埋め込み次元を表示
        print(f"埋め込み次元: {len(embeddings[0])}")

        # ペアごとの類似度を計算
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])

        # 結果を表示
        print(f"\n類似度結果:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nText 1とText 2の類似度: {sim_12:.4f}")
        print(f"Text 1とText 3の類似度: {sim_13:.4f}")
        print(f"Text 2とText 3の類似度: {sim_23:.4f}")
```

### 実行方法

1. **APIキーを設定**:
   ```bash
   export MISTRAL_API_KEY="your_api_key_here"
   ```

2. **保存と実行**:
   スクリプトを保存（例: `embedding_example.py`）し、実行します:
   ```bash
   python embedding_example.py
   ```

### 期待される出力

API呼び出しが成功すると、以下のような出力が表示されます（正確な値は返された埋め込みによって異なります）：

```
埋め込み次元: 1024

類似度結果:
Text 1: 'I love programming in Python.'
Text 2: 'Python is a great programming language.'
Text 3: 'The weather is sunny today.'

Text 1とText 2の類似度: 0.9200
Text 1とText 3の類似度: 0.6500
Text 2とText 3の類似度: 0.6700
```

### 説明

- **APIエンドポイント**: `call_mistral_embeddings_api`関数は、テキストのリストと`"mistral-embed"`モデルを渡して、`https://api.mistral.ai/v1/embeddings`にPOSTリクエストを送信します。APIは、`"data"`キーの下に埋め込みを含むJSON応答を返します。

- **埋め込み**: 各埋め込みは1024次元のベクトル（Mistralのドキュメントに従います）で、入力テキストの意味的内容を表します。埋め込みは1のノルムに正規化されています。

- **類似度計算**: 埋め込みが正規化されているため、2つの埋め込みのドット積（`np.dot`）はそのコサイン類似度に等しいです。高い値はより高い意味的類似度を示します:
  - **Text 1とText 2**: 両方ともPythonでのプログラミングについてなので、類似度は高いです（例: ~0.92）。
  - **Text 1とText 3**: 1つはプログラミング、もう1つは天気についてなので、類似度は低いです（例: ~0.65）。
  - **Text 2とText 3**: 同様に、異なるトピックのため類似度は低いです。

### 追加の使用例

Mistral AIの埋め込みは、類似度検出を超えて適用できます:
- **クラスタリング**: 類似するテキストをグループ化するために、K-meansなどのアルゴリズムを使用します（`scikit-learn`が必要です）。
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
  print(kmeans.labels_)
  ```
- **検索**: クエリを埋め込みし、最も類似するテキストを見つけます:
  ```python
  query = "Tell me about Python."
  query_emb = call_mistral_embeddings_api([query])[0]
  similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
  most_similar = texts[np.argmax(similarities)]
  print(f"最も類似するテキスト: '{most_similar}'")
  ```
- **分類**: 埋め込みを機械学習モデルの特徴として使用します。

### 注意点

- **モデル**: `"mistral-embed"`モデルは埋め込みに最適化されています。更新や追加モデルについては、[ドキュメント](https://docs.mistral.ai/capabilities/embeddings/)を参照してください。
- **バッチ処理**: APIは一度の呼び出しで複数のテキストを処理し、効率を向上させます。
- **高度なアプリケーション**: 大規模な類似度検索には、FaissやMilvusなどのベクトルデータベースと統合します。

この例は、Mistral AI埋め込みの実践的な導入を提供し、提供されたチャット完了コードの構造に適応することで、エンドポイントとデータ形式を変更することができます。