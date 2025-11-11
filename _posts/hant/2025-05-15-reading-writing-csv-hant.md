---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 讀寫CSV檔案
translated: true
type: note
---

### Python 的 `csv` 模組簡介

`csv` 模組是 Python 標準函式庫的一部分，用於讀取和寫入 CSV（逗號分隔值）檔案。它能有效解析行和列。使用時，首先導入模組：`import csv`。您將使用檔案物件，通常以讀取模式（`'r'`）或寫入模式（`'w'`）開啟。

關鍵組件：
- **Reader**：從檔案解析 CSV 資料（例如 `csv.reader()` 用於基於行的存取）。
- **Writer**：將資料輸出到 CSV 檔案（例如 `csv.writer()`）。
- CSV 檔案被視為行的序列，其中每一行是一個字串列表（列）。

為了安全性和便利性，請始終使用 `with` 語句處理檔案，以確保正確關閉。

### 基本讀取 CSV 檔案

讀取 CSV：
```python
import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # 每個 'row' 是一個列的列表
```
- 這會逐行讀取檔案。您可以透過索引存取特定列（例如 `row[0]` 用於第一列）。
- 對於標頭，請單獨讀取第一行：`headers = next(reader)`。

### 比較兩個 CSV 檔案：行與列

要比較兩個 CSV（例如 `file1.csv` 和 `file2.csv`），將它們載入到結構中，例如列表的列表（行），然後進行比較。假設：兩個 CSV 具有相同的結構（相同數量的列/行）。比較可以檢查完全匹配、差異或特定邏輯（例如，基於關鍵列進行匹配）。

#### 範例 1：比較行（整行）
使用字典儲存行（如果它們有唯一的 ID 列）或列表進行直接比較。

```python
import csv

def compare_rows(file1, file2, key_column=0):
    # 將 file1 讀入字典（使用 key_column 作為鍵，整行作為值）
    data1 = {}
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        headers1 = next(reader1, None)  # 跳過標頭（如果存在）
        for row in reader1:
            data1[row[key_column]] = row  # 例如，以第一列為鍵

    # 類似地讀取 file2
    data2 = {}
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        headers2 = next(reader2, None)
        for row in reader2:
            data2[row[key_column]] = row

    # 比較
    common_keys = set(data1.keys()) & set(data2.keys())
    differing_rows = []
    for key in common_keys:
        if data1[key] != data2[key]:
            differing_rows.append((key, data1[key], data2[key]))
    
    return differing_rows  # 列表，包含 (key, row_from_file1, row_from_file2)

# 使用方式
differences = compare_rows('file1.csv', 'file2.csv', key_column=0)  # 以第 0 列為鍵
print("差異行：", differences)
```

- **運作方式**：將 CSV 轉換為以某列（例如 ID）為鍵的字典。直接比較匹配的行。調整 `key_column` 以指定鍵列。
- **變化**：對於無鍵的逐行比較，請同時迭代兩個讀取器（如果順序/長度相同）。

#### 範例 2：比較列
比較整個檔案中的特定列（例如，檢查兩個檔案中的第 1 列值是否相同）。

```python
import csv

def compare_columns(file1, file2, col_index=0):
    # 將列資料提取為列表
    col1 = []
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        next(reader1, None)  # 跳過標頭（如果需要）
        for row in reader1:
            if len(row) > col_index:
                col1.append(row[col_index])

    col2 = []
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        next(reader2, None)
        for row in reader2:
            if len(row) > col_index:
                col2.append(row[col_index])

    # 比較列
    are_equal = col1 == col2
    differences = []
    for i, (val1, val2) in enumerate(zip(col1, col2)):
        if val1 != val2:
            differences.append((i, val1, val2))
    
    return are_equal, differences  # 布林值表示是否匹配，列表包含 (row_index, val1, val2)

# 使用方式
equal, diffs = compare_columns('file1.csv', 'file2.csv', col_index=1)  # 比較第 1 列
print("列是否相等？", equal)
print("差異（行索引, 值1, 值2）：", diffs)
```

- **運作方式**：將指定列提取到列表中，然後進行元素級比較。假設 CSV 具有相同的行數；如有需要，請處理不匹配的情況。
- **變化**：對於更高級的列操作，使用 `pandas`（例如 `df1['column'] == df2['column']`），但對於純標準函式庫，請堅持使用 `csv`。

#### 提示與邊緣案例
- **標頭**：如果 CSV 有標頭，請使用 `next(reader)` 跳過它們。
- **資料類型**：CSV 以字串形式讀取；如果需要，請轉換為 int/float（例如 `int(row[0])`）。
- **大型檔案**：對於大型 CSV，使用 DictReader 進行鍵控存取：`csv.DictReader(file)` 返回 OrderedDict 形式行。
- **分隔符**：如果不是逗號分隔，請在 reader/writer 中使用 `delimiter=';'`。
- **錯誤**：使用 try-except 包裝以處理檔案問題；驗證列長度以避免索引錯誤。
- **替代方案**：對於複雜比較，考慮使用像 `pandas` 這樣的函式庫（對於資料框使用 `df1.equals(df2)`）。

有關完整文件，請查閱 Python 的[官方 csv 模組指南](https://docs.python.org/3/library/csv.html)。如果您有特定的 CSV 檔案或比較邏輯，請提供更多詳細資訊以獲取量身定制的程式碼！