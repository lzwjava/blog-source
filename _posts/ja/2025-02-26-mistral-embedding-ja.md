---
audio: false
generated: true
lang: ja
layout: post
title: ミストラルAIエンベッディングス
translated: true
type: note
---

Mistral AIを使用して埋め込みの例を提供するには、Mistral AIのEmbeddings APIを活用して、意味的な意味を捉えたテキストの数値表現（埋め込み）を生成できます。これらの埋め込みは、類似性検出、クラスタリング、分類、検索などのタスクに有用です。以下では、Mistral AIの埋め込みエンドポイントを使用して、一連の文の埋め込みを生成し、それらの類似性を計算する方法を実演します。この例は、提供されたコードの構造に基づいていますが、埋め込みに特化して適応させたものです。詳細はドキュメントを参照してください: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/)。

### 前提条件

この例を実行する前に、以下を確認してください：
1.  **APIキー**: 有効なMistral AI APIキーが `MISTRAL_API_KEY` 環境変数に設定されていること。
2.  **依存関係**: 必要なPythonパッケージがインストールされていること。以下のコマンドでインストールできます：
    ```bash
    pip install requests numpy
    ```

### コード例

以下は、3つの文の埋め込みを生成し、それらのペアワイズ類似性を計算する完全なPythonスクリプトです：

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    Mistral AI埋め込みAPIを呼び出し、テキストのリストの埋め込みを生成します。

    Args:
        texts (list): 埋め込みを行う文字列のリスト。
        model (str): 使用する埋め込みモデル（デフォルト: "mistral-embed"）。

    Returns:
        list: 埋め込みベクトルのリスト。リクエストが失敗した場合はNone。
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
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
            print(f"Mistral Embeddings API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral Embeddings API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    ドット積を使用して2つの埋め込み間の類似性を計算します。

    Args:
        emb1 (list): 最初の埋め込みベクトル。
        emb2 (list): 2番目の埋め込みベクトル。

    Returns:
        float: 類似性スコア（ドット積、正規化ベクトルの場合はコサイン類似度と等価）。
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # 埋め込みを行う例文
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]

    # 埋め込みを生成
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # 埋め込みの次元数を表示
        print(f"Embedding dimension: {len(embeddings[0])}")

        # ペアワイズ類似性を計算
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])

        # 結果を表示
        print(f"\nSimilarity Results:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nSimilarity between Text 1 and Text 2: {sim_12:.4f}")
        print(f"Similarity between Text 1 and Text 3: {sim_13:.4f}")
        print(f"Similarity between Text 2 and Text 3: {sim_23:.4f}")
```

### 実行方法

1.  **APIキーの設定**:
    ```bash
    export MISTRAL_API_KEY="your_api_key_here"
    ```

2.  **保存と実行**:
    スクリプトを保存し（例: `embedding_example.py`）、実行します：
    ```bash
    python embedding_example.py
    ```

### 期待される出力

API呼び出しが成功した場合、以下のような出力が表示されます（正確な値は返される埋め込みに依存します）：
```
Embedding dimension: 1024

Similarity Results:
Text 1: 'I love programming in Python.'
Text 2: 'Python is a great programming language.'
Text 3: 'The weather is sunny today.'

Similarity between Text 1 and Text 2: 0.9200
Similarity between Text 1 and Text 3: 0.6500
Similarity between Text 2 and Text 3: 0.6700
```

### 説明

-   **APIエンドポイント**: `call_mistral_embeddings_api` 関数は、テキストのリストと `"mistral-embed"` モデルを渡して、`https://api.mistral.ai/v1/embeddings` にPOSTリクエストを送信します。APIは `"data"` キーの下に埋め込みを含むJSONレスポンスを返します。

-   **埋め込み**: 各埋め込みは、入力テキストの意味的コンテンツを表す1024次元のベクトルです（Mistralのドキュメントによる）。埋め込みはノルム1に正規化されています。

-   **類似性計算**: 埋め込みが正規化されているため、2つの埋め込み間のドット積（`np.dot`）はそれらのコサイン類似度と等しくなります。高い値はより大きな意味的類似性を示します：
    -   **Text 1 と Text 2**: 両方ともPythonでのプログラミングに関する内容なので、類似性は高くなります（例: ~0.92）。
    -   **Text 1 と Text 3**: 一方はプログラミング、もう一方は天気についてなので、類似性は低くなります（例: ~0.65）。
    -   **Text 2 と Text 3**: 同様のパターンで、トピックが異なるため類似性は低くなります。

### その他のユースケース

Mistral AIからの埋め込みは、類似性検出以外にも応用できます：
-   **クラスタリング**: K-meansなどのアルゴリズムを使用して類似したテキストをグループ化します（`scikit-learn` が必要）。
    ```python
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
    print(kmeans.labels_)
    ```
-   **検索**: クエリを埋め込み、最も類似したテキストを見つけます：
    ```python
    query = "Tell me about Python."
    query_emb = call_mistral_embeddings_api([query])[0]
    similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
    most_similar = texts[np.argmax(similarities)]
    print(f"Most similar text: '{most_similar}'")
    ```
-   **分類**: 機械学習モデルの特徴量として埋め込みを使用します。

### 注意点

-   **モデル**: `"mistral-embed"` モデルは埋め込み用に最適化されています。更新や追加モデルについては[ドキュメント](https://docs.mistral.ai/capabilities/embeddings/)を確認してください。
-   **バッチ処理**: APIは複数のテキストを1回の呼び出しで処理するため、効率が向上します。
-   **高度なアプリケーション**: 大規模な類似性検索には、FaissやMilvusなどのベクトルデータベースとの統合を検討してください。

この例は、Mistral AI埋め込みを使用するための実践的な入門を提供し、エンドポイントとデータ形式を変更することで、提供されたチャット補完コードの構造に適応可能です。