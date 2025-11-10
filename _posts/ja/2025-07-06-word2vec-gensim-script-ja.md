---
audio: false
generated: true
lang: ja
layout: post
title: Gensimを使ったWord2Vecスクリプト
translated: true
type: note
---

Word2VecのPythonスクリプトを提供するにあたり、「Word2Vecに関するスクリプト」という要求が幅広い解釈ができるため、いくつか仮定を置く必要があります。以下に2つの一般的なシナリオを提供します：

1.  **`gensim`を使用したトレーニングと基本的な使用法のシンプルなスクリプト:** これがPythonでWord2Vecを使用する最も一般的で実用的な方法です。
2.  **スクラッチからの非常に基本的な概念実証的な実装:** これはコアアルゴリズムを理解するためにはより適していますが、複雑さと最適化の点で実世界での使用には実用的ではありません。

ご要頂いた内容を考慮し、多くの方が使用する`gensim`アプローチを優先します。

-----

### `gensim`を使用したWord2VecのPythonスクリプト

このスクリプトは以下を実演します：

  * サンプルテキストデータの準備
  * Word2Vecモデルのトレーニング
  * 最も類似した単語の検索
  * 単語の類推の実行
  * モデルの保存と読み込み

**前提条件:**

`gensim`ライブラリをインストールする必要があります：

```bash
pip install gensim
```

**Pythonスクリプト (`word2vec_gensim_example.py`):**

```python
import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging

# トレーニングの進捗を確認するためにロギングを設定
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# --- 1. サンプルテキストデータの準備 ---
# 実際のシナリオでは、ファイルからテキストデータを読み込みます。
# ここでは、シンプルな文のリストを使用します。
raw_sentences = [
    "I love natural language processing.",
    "Word embeddings are a fascinating topic.",
    "Machine learning revolutionizes many industries.",
    "Deep learning is a subset of machine learning.",
    "Natural language processing uses various techniques.",
    "Computers understand human language better with word vectors.",
    "The quick brown fox jumps over the lazy dog.",
    "Dog and cat are common pets.",
    "King is to Queen as Man is to Woman."
]

# 文を前処理：トークン化し小文字に変換
# gensimのsimple_preprocessがこれに便利です
tokenized_sentences = [simple_preprocess(sentence) for sentence in raw_sentences]

print("\n--- トークン化された文 ---")
for sentence in tokenized_sentences:
    print(sentence)

# --- 2. Word2Vecモデルのトレーニング ---
# パラメータの説明:
#   vector_size: 単語ベクトルの次元数
#   window: 文内における現在の単語と予測される単語間の最大距離
#   min_count: 合計頻度がこの値より低いすべての単語を無視します
#   sg: トレーニングアルゴリズム: 0はCBOW、1はSkip-gram。Skip-gramは一般にレアワードに対してより優れています
#   workers: モデルのトレーニングに使用するワーカースレッド数（=より高速なトレーニング）
#   epochs: コーパスに対する反復回数（エポック数）
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,      # 例: 100次元のベクトル
    window=5,             # 前後5単語のコンテキストウィンドウ
    min_count=1,          # すべての単語を含める（この小さな例では）
    sg=1,                 # Skip-gramを使用 (sg=1)
    workers=4,            # トレーニングに4つのCPUコアを使用
    epochs=10             # 10エポックトレーニング
)

print("\n--- モデルのトレーニング完了 ---")

# --- 3. モデルの探索 ---

# 特定の単語のベクトルを取得
try:
    word_vector = model.wv['machine']
    print(f"\n'machine'のベクトル（最初の10次元）: {word_vector[:10]}")
    print(f"'machine'のベクトルの形状: {word_vector.shape}")
except KeyError:
    print("\n'machine'は語彙に見つかりませんでした。")

# 最も類似した単語を検索
print("\n--- 'machine'に最も類似した単語 ---")
try:
    similar_words = model.wv.most_similar('machine')
    for word, similarity in similar_words:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'machine'は語彙に見つかりませんでした。")

print("\n--- 'dog'に最も類似した単語 ---")
try:
    similar_words_dog = model.wv.most_similar('dog')
    for word, similarity in similar_words_dog:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'dog'は語彙に見つかりませんでした。")


# 単語の類推を実行（例: King - Man + Woman = Queen）
# これは非常に小さなデータセットでは完全には動作しないかもしれませんが、概念を実演します。
print("\n--- 単語の類推 (King - Man + Woman = ?) ---")
try:
    result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    if result:
        print(f"King - Man + Woman は次に類似: {result[0][0]} (類似度: {result[0][1]:.4f})")
    else:
        print("類推の結果がありません。語彙が小さすぎる可能性があります。")
except KeyError as e:
    print(f"類推に必要な単語の1つ以上が語彙に見つかりません: {e}")
except Exception as e:
    print(f"類推中にエラーが発生しました: {e}")

# 2つの単語間の類似度をチェック
print("\n--- 'machine'と'learning'の間の類似度 ---")
try:
    similarity = model.wv.similarity('machine', 'learning')
    print(f"類似度: {similarity:.4f}")
except KeyError:
    print("1つまたは両方の単語が語彙に見つかりません。")

print("\n--- 'dog'と'cat'の間の類似度 ---")
try:
    similarity_pets = model.wv.similarity('dog', 'cat')
    print(f"類似度: {similarity_pets:.4f}")
except KeyError:
    print("1つまたは両方の単語が語彙に見つかりません。")

print("\n--- 'dog'と'computer'の間の類似度 ---")
try:
    similarity_diff = model.wv.similarity('dog', 'computer')
    print(f"類似度: {similarity_diff:.4f}")
except KeyError:
    print("1つまたは両方の単語が語彙に見つかりません。")

# --- 4. モデルの保存と読み込み ---
model_path = "word2vec_model.bin"
model.save(model_path)
print(f"\nモデルを {model_path} に保存しました")

# モデルを読み戻す
loaded_model = Word2Vec.load(model_path)
print(f"モデルを {model_path} から読み込みました")

# 読み込まれたモデルを検証
print("\n--- 読み込まれたモデルの検証（読み込まれたモデルを使用した'machine'に最も類似した単語） ---")
try:
    similar_words_loaded = loaded_model.wv.most_similar('machine')
    for word, similarity in similar_words_loaded:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n読み込まれたモデルの語彙に'machine'が見つかりませんでした。")

print("\nスクリプトの実行が完了しました。")
```

**スクリプトの実行方法:**

1.  上記のコードをPythonファイル（例: `word2vec_gensim_example.py`）として保存します。
2.  ターミナルまたはコマンドプロンプトを開きます。
3.  ファイルを保存したディレクトリに移動します。
4.  次のコマンドを使用してスクリプトを実行します: `python word2vec_gensim_example.py`

-----

### Word2Vecの主要な概念 (`gensim`実装)

  * **`gensim.models.Word2Vec`**: トレーニングのためのメインクラス
  * **`sentences`**: イテラブルのイテラブル。外側のイテラブルはコーパス、内側のイテラブルは（トークン化された文の）単語のリストです
  * **`vector_size`**: 単語ベクトルの次元数。より高い次元はより多くのニュアンスを捉えることができますが、より多くのデータと計算を必要とします
  * **`window`**: 文内における現在の単語とその周囲の単語間の最大距離
  * **`min_count`**: `min_count`回数よりも少なく出現する単語は無視されます。これは意味のある埋め込みを持たない可能性がある非常にレアな単語をフィルタリングするのに役立ちます
  * **`sg` (Skip-gram vs. CBOW)**:
      * `sg=0` (CBOW - Continuous Bag of Words): コンテキストに基づいて現在の単語を予測します。トレーニングが高速です
      * `sg=1` (Skip-gram): 現在の単語を与えられた周囲の単語を予測します。一般にレアワードに対してより優れたパフォーマンスを発揮します
  * **`workers`**: トレーニングに使用するCPUコアの数。プロセスを高速化します
  * **`epochs`**: アルゴリズムがデータセット全体を反復処理する回数。より多くのエポックはより高品質な埋め込みにつながる可能性がありますが、より長く時間がかかります
  * **`model.wv`**: トレーニングされた単語埋め込みと`most_similar`、`similarity`などのメソッドを含む「単語ベクトル」オブジェクト（`KeyedVectors`）。`model.wv['word']`のようにベクトルに直接アクセスすることもできます

-----

この`gensim`スクリプトは、Word2Vecを扱うための強固な基盤を提供します。実際のアプリケーションでは、通常、はるかに大きなコーパス（例：Wikipedia、Common Crawl）を使用し、最適なパフォーマンスを得るためにハイパーパラメータを調整します。