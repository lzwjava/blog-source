---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: PromQL 查詢語言指南
translated: true
type: note
---

PromQL（Prometheus 查詢語言）是一種功能性查詢語言，用於從 Prometheus 中即時選取和匯總時間序列資料。它支援即時查詢（在單一時間點評估）和範圍查詢（在時間範圍內的多個步驟中評估）。PromQL 表達式可返回四種資料類型之一：**即時向量**、**範圍向量**、**純量**或**字串**。

---

## 簡介

PromQL 讓使用者能夠：
- 使用**即時向量選擇器**選取時間序列。
- 使用**範圍向量選擇器**檢索一段時間範圍內的資料。
- 應用**運算子**（算術、比較、邏輯、匯總）。
- 使用函數如 `rate()`、`sum()`、`avg()` 進行分析。
- 透過 **HTTP API** 查詢資料。

表達式在 Prometheus UI 中評估：
- **表格頁籤**：即時查詢。
- **圖表頁籤**：範圍查詢。

---

## 時間序列選擇器

時間序列選擇器定義要檢索的指標和標籤。

### 即時向量選擇器

選取每個匹配時間序列的最新樣本。

**語法**：  
```
<指標名稱>{<標籤匹配器>}
```

**範例**：
- 所有指標為 `http_requests_total` 的時間序列：
  ```
  http_requests_total
  ```
- 特定 job 和 group：
  ```
  http_requests_total{job="prometheus", group="canary"}
  ```
- 環境正則匹配且排除 GET 方法：
  ```
  http_requests_total{environment=~"staging|testing|development", method!="GET"}
  ```
- 匹配 `__name__`：
  ```
  {__name__=~"job:.*"}
  ```

**標籤匹配器**：
- `=` ：完全匹配
- `!=` ：不相等
- `=~` ：正則匹配（錨定）
- `!~` ：非正則匹配

> 注意：`{job=~".+"}` 有效；單獨的 `{}` 無效。

---

### 範圍向量選擇器

選取一段時間內的樣本範圍。

**語法**：  
```
<即時選擇器>[<持續時間>]
```

**範例**：
- `prometheus` job 的 `http_requests_total` 最近 5 分鐘資料：
  ```
  http_requests_total{job="prometheus"}[5m]
  ```

> 範圍為**左開右閉**：排除開始時間，包含結束時間。

---

### 偏移修飾符

將評估時間向前或向後移動。

**語法**：  
```
<選擇器> offset <持續時間>
```

**範例**：
- 5 分鐘前的 `http_requests_total` 值：
  ```
  http_requests_total offset 5m
  ```
- 1 週前的速率：
  ```
  rate(http_requests_total[5m] offset 1w)
  ```
- 向前查看（負偏移）：
  ```
  rate(http_requests_total[5m] offset -1w)
  ```

> 必須緊接在選擇器之後。

---

### `@` 修飾符

在特定時間戳評估。

**語法**：  
```
<選擇器> @ <時間戳>
```

**範例**：
- Unix 時間戳 `1609746000` 的值：
  ```
  http_requests_total @ 1609746000
  ```
- 特定時間的速率：
  ```
  rate(http_requests_total[5m] @ 1609746000)
  ```
- 使用 `start()` 或 `end()`：
  ```
  http_requests_total @ start()
  rate(http_requests_total[5m] @ end())
  ```

> 可與 `offset` 結合使用。

---

## 速率與匯總

PromQL 支援**速率**和**匯總**運算子，用於計算隨時間或跨序列的指標。

### 速率函數

計算每秒平均增長速率。

**範例**：
```
rate(http_requests_total[5m])
```

> 用於**範圍向量**。

---

### 匯總運算子

應用於即時向量以合併時間序列。

**範例**：
- 所有 `http_requests_total` 的總和：
  ```
  sum(http_requests_total)
  ```
- 每個 instance 的平均值：
  ```
  avg by (instance)(http_requests_total)
  ```
- 每個 job 的計數：
  ```
  count by (job)(http_requests_total)
  ```

> 匯總需要匹配的序列；使用 `by` 或 `without` 子句。

---

## 運算子

PromQL 支援多種運算子類型。

### 算術運算子

| 運算子 | 描述         | 範例                          |
|--------|--------------|------------------------------|
| `+`    | 加法         | `rate(a[5m]) + rate(b[5m])`  |
| `-`    | 減法         | `rate(a[5m]) - rate(b[5m])`  |
| `*`    | 乘法         | `http_requests_total * 60`   |
| `/`    | 除法         | `rate(a[5m]) / rate(b[5m])`  |
| `%`    | 取模         | `http_requests_total % 100`  |

> 運算元必須相容（相同類型和形狀）。

---

### 比較運算子

比較兩個即時向量。

| 運算子 | 描述         | 範例                              |
|--------|--------------|----------------------------------|
| `==`   | 等於         | `rate(a[5m]) == rate(b[5m])`     |
| `!=`   | 不等於       | `rate(a[5m]) != 0`               |
| `>`    | 大於         | `http_requests_total > 100`      |
| `<`    | 小於         | `http_requests_total < 10`       |
| `>=`   | 大於或等於   | `rate(a[5m]) >= 2`               |
| `<=`   | 小於或等於   | `http_requests_total <= 5`       |

> 返回布林即時向量。

---

### 邏輯運算子

組合布林表達式。

| 運算子 | 描述         | 範例                                 |
|--------|--------------|-------------------------------------|
| `and`  | 邏輯 AND     | `rate(a[5m]) > 1 and rate(b[5m]) > 1` |
| `or`   | 邏輯 OR      | `rate(a[5m]) > 1 or rate(b[5m]) > 1`  |
| `unless` | 除外       | `rate(a[5m]) unless rate(b[5m]) > 0`  |

> 運算元必須是相同基數的布林向量。

---

## 函數

PromQL 包含內建函數用於轉換和分析。

**常用函數**：
- `rate(v range-vector)` – 每秒速率。
- `irate(v range-vector)` – 瞬時速率（最後兩個點）。
- `avg(v)` – 平均值。
- `sum(v)` – 值的總和。
- `count(v)` – 元素數量。
- `min(v)`, `max(v)` – 最小值/最大值。
- `quantile(v instant-vector, q)` – 百分位數。

**範例**：
```
quantile by (job)(0.95, http_request_duration_seconds_bucket[5m])
```

> 完整列表請參閱 [Prometheus 函數文件](https://prometheus.io/docs/prometheus/latest/querying/functions/)。

---

## 用於查詢的 HTTP API

PromQL 查詢可透過 HTTP API 發送。

### 即時查詢

**端點**：`/api/v1/query`

**方法**：`GET`

**參數**：
- `query`：PromQL 表達式
- `time`：評估時間戳（Unix 秒數，可選）
- `timeout`：查詢超時（例如 `30s`）

**範例**：
```
GET /api/v1/query?query=http_requests_total{job="prometheus"}&time=1609746000
```

**回應**：包含 `status`、`data.result`（即時向量或純量）的 JSON。

---

### 範圍查詢

**端點**：`/api/v1/query_range`

**參數**：
- `query`：PromQL 表達式
- `start`：開始時間（Unix 秒數）
- `end`：結束時間（Unix 秒數）
- `step`：解析度步長（例如 `15s`）

**範例**：
```
GET /api/v1/query_range?query=rate(http_requests_total[5m])&start=1609746000&end=1609746600&step=10s
```

**回應**：每個步長的時間序列資料 JSON。

---

## 補充說明

- **字面值**：
  - 字串：`"hello"`、`'world'`、`` `raw` ``
  - 浮點數：`3.14`、`-2.5e-3`、`1_000`、`0xFF`
  - 持續時間：`5m`、`1h30m`、`500ms`

- **註解**：以 `#` 開頭

- **陳舊性**：序列在 5 分鐘（預設）無更新後變為陳舊。

- **子查詢**：在範圍內執行即時查詢：
  ```
  rate(http_requests_total[10m:5m])[5m]
  ```

---

本指南涵蓋了 PromQL 從初學者到中階使用者的核心內容。進階用法請參閱 [Prometheus 查詢基礎](https://prometheus.io/docs/prometheus/latest/querying/basics/)及相關頁面。