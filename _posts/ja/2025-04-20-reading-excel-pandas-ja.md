---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: PandasでのExcelファイル読み込み
translated: true
type: note
---

### 前提条件
PythonでExcelファイルを読み込むには、`pandas`ライブラリとExcelエンジンが必要です。pandasがインストールされていない場合はインストールしてください：
```
pip install pandas
```
新しいExcel形式（.xlsx）の場合、`openpyxl`をインストールします：
```
pip install openpyxl
```
.xlsファイルの場合は、`xlrd`を使用します：
```
pip install xlrd
```

### 基本的な使い方
PandasはExcelデータをDataFrameに読み込むための`pd.read_excel()`関数を提供します。

1. pandasをインポート：
   ```python
   import pandas as pd
   ```

2. Excelファイルを読み込み（ファイルパスを指定）：
   ```python
   df = pd.read_excel('path/to/your/file.xlsx')
   ```
   - デフォルトでは最初のシートを読み込みます
   - 結果はExcelデータを含むDataFrameになります

3. データの確認：
   ```python
   print(df.head())  # 最初の5行を表示
   print(df.info())  # 列とデータ型の要約
   ```

### 高度なオプション
- **シートの指定**：`sheet_name`パラメータを使用（デフォルトは0で最初のシート）：
  ```python
  df = pd.read_excel('file.xlsx', sheet_name='Sheet2')  # 名前で指定
  df = pd.read_excel('file.xlsx', sheet_name=1)        # インデックスで指定（0から開始）
  ```
- **複数シートの読み込み**：リストまたは`None`を渡して全てのシートを辞書として読み込み：
  ```python
  all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # シート名をキーとしたDataFrameの辞書
  ```
- **データ範囲の指定**：列には`usecols`（例：列AからCには`'A:C'`）、初期行のスキップには`skiprows`を使用：
  ```python
  df = pd.read_excel('file.xlsx', usecols='A,C,E', skiprows=2)
  ```
- **ヘッダーの処理**：ヘッダーが0行目にない場合は`header`で指定：
  ```python
  df = pd.read_excel('file.xlsx', header=1)  # ヘッダーは1行目（0から開始するインデックス）
  ```
- **インデックスの設定**：`index_col`で列をインデックスとして設定：
  ```python
  df = pd.read_excel('file.xlsx', index_col='Column Name')
  ```

### 例
「Data」という名前のシートに売上データを含むExcelファイル`sales.xlsx`があるとします。

```python
import pandas as pd

# 特定のシートを読み込み
df = pd.read_excel('sales.xlsx', sheet_name='Data')

# DataFrameを表示
print(df)

# 必要に応じてCSVとして保存
df.to_csv('sales.csv', index=False)
```

詳細については、[pandasのread_excelドキュメント](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)を参照してください。エラーが発生した場合は、Excelファイルの形式を確認し、必要なパッケージがインストールされていることを確認してください。