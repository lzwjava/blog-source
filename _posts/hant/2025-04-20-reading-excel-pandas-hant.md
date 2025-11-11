---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用 Pandas 讀取 Excel 檔案
translated: true
type: note
---

### 前置準備
要在 Python 中讀取 Excel 檔案，你需要 `pandas` 函式庫和一個 Excel 引擎。如果尚未安裝 pandas，請執行：
```
pip install pandas
```
對於現代 Excel 格式 (.xlsx)，請安裝 `openpyxl`：
```
pip install openpyxl
```
對於 .xls 檔案，請使用 `xlrd`：
```
pip install xlrd
```

### 基本用法
Pandas 提供 `pd.read_excel()` 函數將 Excel 資料載入至 DataFrame。

1. 匯入 pandas：
   ```python
   import pandas as pd
   ```

2. 讀取 Excel 檔案（指定檔案路徑）：
   ```python
   df = pd.read_excel('path/to/your/file.xlsx')
   ```
   - 預設會載入第一個工作表。
   - 結果將是一個包含 Excel 資料的 DataFrame。

3. 檢視資料：
   ```python
   print(df.head())  # 檢視前 5 列資料
   print(df.info())  # 顯示欄位摘要與資料型態
   ```

### 進階選項
- **指定工作表**：使用 `sheet_name` 參數（預設值 0 表示第一個工作表）：
  ```python
  df = pd.read_excel('file.xlsx', sheet_name='Sheet2')  # 依名稱指定
  df = pd.read_excel('file.xlsx', sheet_name=1)        # 依索引指定（從 0 開始）
  ```
- **讀取多個工作表**：傳入清單或 `None` 即可載入所有工作表為字典格式：
  ```python
  all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # 以工作表名稱為鍵的 DataFrame 字典
  ```
- **指定資料範圍**：使用 `usecols` 指定欄位（例如 `'A:C'` 表示 A 到 C 欄），並用 `skiprows` 跳過起始列：
  ```python
  df = pd.read_excel('file.xlsx', usecols='A,C,E', skiprows=2)
  ```
- **處理標頭列**：若標頭不在第 0 列，請透過 `header` 參數指定：
  ```python
  df = pd.read_excel('file.xlsx', header=1)  # 標頭位於第 1 列（索引從 0 開始）
  ```
- **設定索引**：使用 `index_col` 將特定欄位設為索引：
  ```python
  df = pd.read_excel('file.xlsx', index_col='Column Name')
  ```

### 範例
假設你有一個名為 `sales.xlsx` 的 Excel 檔案，其中包含名為 "Data" 的工作表，內有銷售資料。

```python
import pandas as pd

# 讀取特定工作表
df = pd.read_excel('sales.xlsx', sheet_name='Data')

# 顯示 DataFrame
print(df)

# 如有需要可儲存為 CSV
df.to_csv('sales.csv', index=False)
```

更多詳細資訊，請參閱 [pandas 官方文件中關於 read_excel 的說明](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)。若遇到錯誤，請檢查 Excel 檔案格式並確認已安裝所需套件。