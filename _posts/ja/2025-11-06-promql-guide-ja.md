---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: PromQLクエリ言語ガイド
translated: true
type: note
---

PromQL（Prometheus Query Language）は、Prometheusから時系列データをリアルタイムで選択および集計するための関数型クエリ言語です。インスタントクエリ（単一時点で評価）と範囲クエリ（時間範囲にわたって複数ステップで評価）をサポートしています。PromQL式は4つのデータ型のいずれかを返します：**インスタントベクトル**、**範囲ベクトル**、**スカラー**、または**文字列**。

---

## はじめに

PromQLによりユーザーは以下が可能です：
- **インスタントベクトルセレクター**を使用して時系列を選択
- **範囲ベクトルセレクター**を使用して時間範囲にわたるデータを取得
- **演算子**（算術、比較、論理、集計）を適用
- `rate()`、`sum()`、`avg()`などの**関数**を分析に使用
- **HTTP API**経由でデータをクエリ

式はPrometheus UIで評価されます：
- **Tableタブ**: インスタントクエリ
- **Graphタブ**: 範囲クエリ

---

## 時系列セレクター

時系列セレクターは、取得するメトリクスとラベルを定義します。

### インスタントベクトルセレクター

マッチする各時系列の最新サンプルを選択します。

**構文**:  
```
<metric_name>{<label_matchers>}
```

**例**:
- メトリクス`http_requests_total`を持つ全ての時系列:
  ```
  http_requests_total
  ```
- 特定のjobとgroup:
  ```
  http_requests_total{job="prometheus", group="canary"}
  ```
- 環境に対する正規表現マッチ、かつGETメソッドを除外:
  ```
  http_requests_total{environment=~"staging|testing|development", method!="GET"}
  ```
- `__name__`でのマッチ:
  ```
  {__name__=~"job:.*"}
  ```

**ラベルマッチャー**:
- `=` : 完全一致
- `!=` : 不一致
- `=~` : 正規表現マッチ（アンカー付き）
- `!~` : 正規表現不一致

> 注: `{job=~".+"}`は有効ですが、`{}`単体は無効です。

---

### 範囲ベクトルセレクター

時間にわたる一連のサンプルを選択します。

**構文**:  
```
<instant_selector>[<duration>]
```

**例**:
- `prometheus` jobの`http_requests_total`の過去5分間:
  ```
  http_requests_total{job="prometheus"}[5m]
  ```

> 範囲は**左開区間、右閉区間**です：開始時刻は含まず、終了時刻を含みます。

---

### オフセット修飾子

評価時間を前後にシフトします。

**構文**:  
```
<selector> offset <duration>
```

**例**:
- 5分前の`http_requests_total`の値:
  ```
  http_requests_total offset 5m
  ```
- 1週間前のレート:
  ```
  rate(http_requests_total[5m] offset 1w)
  ```
- 先読み（負のオフセット）:
  ```
  rate(http_requests_total[5m] offset -1w)
  ```

> セレクターの直後に記述する必要があります。

---

### `@`修飾子

特定のタイムスタンプで評価します。

**構文**:  
```
<selector> @ <timestamp>
```

**例**:
- Unixタイムスタンプ`1609746000`での値:
  ```
  http_requests_total @ 1609746000
  ```
- 特定時刻でのレート:
  ```
  rate(http_requests_total[5m] @ 1609746000)
  ```
- `start()`または`end()`の使用:
  ```
  http_requests_total @ start()
  rate(http_requests_total[5m] @ end())
  ```

> `offset`と組み合わせることができます。

---

## レートと集計

PromQLは**レート**と**集計**演算子をサポートし、時間または系列全体にわたるメトリクスを計算します。

### rate関数

1秒あたりの平均増加率を計算します。

**例**:
```
rate(http_requests_total[5m])
```

> **範囲ベクトル**に対して使用します。

---

### 集計演算子

時系列を結合するためにインスタントベクトルに適用します。

**例**:
- 全ての`http_requests_total`の合計:
  ```
  sum(http_requests_total)
  ```
- インスタンスごとの平均:
  ```
  avg by (instance)(http_requests_total)
  ```
- jobごとのカウント:
  ```
  count by (job)(http_requests_total)
  ```

> 集計にはマッチングする系列が必要です。`by`または`without`句を使用します。

---

## 演算子

PromQLはいくつかの演算子タイプをサポートします。

### 算術演算子

| 演算子 | 説明       | 例                          |
|--------|------------|------------------------------|
| `+`    | 加算       | `rate(a[5m]) + rate(b[5m])`  |
| `-`    | 減算       | `rate(a[5m]) - rate(b[5m])`  |
| `*`    | 乗算       | `http_requests_total * 60`   |
| `/`    | 除算       | `rate(a[5m]) / rate(b[5m])`  |
| `%`    | 剰余       | `http_requests_total % 100`  |

> 被演算子は互換性が必要です（同じ型と形状）。

---

### 比較演算子

2つのインスタントベクトルを比較します。

| 演算子 | 説明           | 例                              |
|--------|----------------|----------------------------------|
| `==`   | 等しい         | `rate(a[5m]) == rate(b[5m])`     |
| `!=`   | 等しくない     | `rate(a[5m]) != 0`               |
| `>`    | より大きい     | `http_requests_total > 100`      |
| `<`    | より小さい     | `http_requests_total < 10`       |
| `>=`   | 以上           | `rate(a[5m]) >= 2`               |
| `<=`   | 以下           | `http_requests_total <= 5`       |

> ブーリアンインスタントベクトルを返します。

---

### 論理演算子

ブーリアン式を結合します。

| 演算子  | 説明        | 例                                   |
|---------|-------------|---------------------------------------|
| `and`   | 論理AND     | `rate(a[5m]) > 1 and rate(b[5m]) > 1` |
| `or`    | 論理OR      | `rate(a[5m]) > 1 or rate(b[5m]) > 1`  |
| `unless`| 除外        | `rate(a[5m]) unless rate(b[5m]) > 0`  |

> 被演算子は同じカーディナリティのブーリアンベクトルである必要があります。

---

## 関数

PromQLには変換と分析のための組み込み関数が含まれています。

**一般的な関数**:
- `rate(v range-vector)` – 1秒あたりのレート
- `irate(v range-vector)` – 瞬間レート（最後の2点）
- `avg(v)` – 平均値
- `sum(v)` – 値の合計
- `count(v)` – 要素数
- `min(v)`, `max(v)` – 最小値/最大値
- `quantile(v instant-vector, q)` – パーセンタイル

**例**:
```
quantile by (job)(0.95, http_request_duration_seconds_bucket[5m])
```

> 完全なリストは[Prometheus Functions Documentation](https://prometheus.io/docs/prometheus/latest/querying/functions/)を参照してください。

---

## クエリのためのHTTP API

PromQLクエリはHTTP API経由で送信できます。

### インスタントクエリ

**エンドポイント**: `/api/v1/query`

**メソッド**: `GET`

**パラメータ**:
- `query`: PromQL式
- `time`: 評価タイムスタンプ（Unix秒、オプション）
- `timeout`: クエリタイムアウト（例: `30s`）

**例**:
```
GET /api/v1/query?query=http_requests_total{job="prometheus"}&time=1609746000
```

**レスポンス**: `status`、`data.result`（インスタントベクトルまたはスカラー）を含むJSON。

---

### 範囲クエリ

**エンドポイント**: `/api/v1/query_range`

**パラメータ**:
- `query`: PromQL式
- `start`: 開始時刻（Unix秒）
- `end`: 終了時刻（Unix秒）
- `step`: 解像度ステップ（例: `15s`）

**例**:
```
GET /api/v1/query_range?query=rate(http_requests_total[5m])&start=1609746000&end=1609746600&step=10s
```

**レスポンス**: 各ステップでの時系列データを含むJSON。

---

## 追加の注意点

- **リテラル**:
  - 文字列: `"hello"`, `'world'`, `` `raw` ``
  - 浮動小数点数: `3.14`, `-2.5e-3`, `1_000`, `0xFF`
  - 期間: `5m`, `1h30m`, `500ms`

- **コメント**: `#`で開始

- **陳腐化**: 系列は更新がないと5分（デフォルト）で陳腐化します。

- **サブクエリ**: 範囲にわたってインスタントクエリを実行:
  ```
  rate(http_requests_total[10m:5m])[5m]
  ```

---

このガイドは、初心者から中級ユーザー向けにPromQLの核心をカバーしています。高度な使用方法については、[Prometheus Querying Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)およびリンク先のページを参照してください。