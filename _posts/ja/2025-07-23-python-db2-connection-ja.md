---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: PythonからIBM DB2への接続
translated: true
type: note
---

### 概要
IBM DB2はリレーショナルデータベース管理システムであり、Pythonでは`ibm_db`パッケージ（低レベルインターフェースを提供）と、`ibm_db`の上に構築されより簡単でPythonらしい使用法を実現するDB-API 2.0準拠のラッパーである`ibm_db_dbi`を使用して対話できます。`ibm_db`はより直接的で強力ですが深い知識を必要とし、一方`ibm_db_dbi`はPythonの`sqlite3`モジュールを模倣しており、標準的なデータベース操作をより簡単に行えます。両方ともIBM DB2 Pythonドライバーの一部です。

### インストール
以下のpipコマンドでパッケージをインストールします：
```
pip install ibm_db
pip install ibm_db_dbi
```
注意：これらにはDB2クライアントライブラリが必要です。Windows/Linuxでは、IBMのサイトからIBM Data Server Driver Packageをダウンロードしてインストールしてください。macOSでは追加の設定が必要な場合があります。DB2サーバーが（例：ホスト上で実行され、資格情報を持つ状態で）アクセス可能であることを確認してください。

### ibm_dbの使用
`ibm_db`は、接続、ステートメントの実行、結果の処理のための関数を提供します。DB-APIに非準拠ですが、より多くの制御が可能です。

#### 基本的な接続とクエリ
```python
import ibm_db

# 接続文字列形式: DATABASE=<db_name>;HOSTNAME=<host>;PORT=<port>;PROTOCOL=TCPIP;UID=<user>;PWD=<password>;
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# 接続
conn = ibm_db.connect(conn_str, "", "")

# クエリの実行
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM MYTABLE")

# 結果の取得（一度に1行）
row = ibm_db.fetch_assoc(stmt)
while row:
    print(row)  # 辞書を返す
    row = ibm_db.fetch_assoc(stmt)

# 閉じる
ibm_db.close(conn)
```
- **主な関数**: `connect()`、単純なクエリ用の`exec_immediate()`、インジェクション防止のためのパラメータ化クエリ用の`prepare()`および`execute()`
- **プリペアドステートメント**: `prepare()`でクエリをコンパイルし、パラメータを指定して`execute()`を実行

#### エラーハンドリング
```python
try:
    conn = ibm_db.connect(conn_str, "", "")
except Exception as e:
    print(f"接続失敗: {str(e)}")
```

### ibm_db_dbiの使用
`ibm_db_dbi`はDB-API 2.0を実装しており、`sqlite3`や`psycopg2`などのモジュールと互換性があります。

#### 基本的な接続とクエリ
```python
import ibm_db_dbi

# ibm_dbと同様の接続文字列
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# 接続
conn = ibm_db_dbi.connect(conn_str)

# カーソルの作成
cursor = conn.cursor()

# クエリの実行
cursor.execute("SELECT * FROM MYTABLE")

# 結果の取得
rows = cursor.fetchall()  # タプルのリストを返す
for row in rows:
    print(row)

# 閉じる
cursor.close()
conn.close()
```
- **パラメータ化クエリ**: `cursor.execute("SELECT * FROM MYTABLE WHERE ID = ?", (id_value,))` – ? プレースホルダーを使用
- **トランザクション**: `conn.commit()` または `conn.rollback()`。デフォルトでは自動コミットはオフ

### 主な違いと使い分け

| 特徴              | ibm_db                          | ibm_db_dbi                      |
|-------------------|---------------------------------|---------------------------------|
| 準拠性            | DB-API非準拠（低レベル）        | DB-API 2.0準拠                 |
| 使いやすさ        | より多くのコードが必要、直接アクセス | よりシンプル、Pythonライクな構文 |
| パフォーマンス    | 複雑な操作で潜在的に高速         | ラッパーによるオーバーヘッド     |
| 機能性            | 完全なDB2機能                   | DB-APIインターフェース経由の機能サブセット |
| 使用ケース        | 生の制御を必要とするカスタムアプリ | 標準的なCRUD操作               |

他のDB-APIドライバーに慣れている場合は`ibm_db_dbi`を、ストアドプロシージャやバルク操作などの高度なDB2固有の機能が必要な場合は`ibm_db`に切り替えてください。

### ベストプラクティス
- リソースリークを避けるため、例外を常に処理し、`try-finally`ブロックまたは`with`ブロック内で接続を閉じてください。
- 大きな結果セットの場合、メモリ使用量を制限するために`fetchall()`の代わりに`fetchmany(size)`を使用してください。
- DB2のバージョン互換性を確認してください。これらのパッケージはDB2 LUW、z/OS、iSeriesをサポートしています。
- SSL接続やCLPPlus統合などの高度なトピックについては、IBMのドキュメントを参照してください。

より多くの例については、[IBM db2 Python driver repo](https://github.com/ibmdb/python-ibmdb)を参照してください。問題が発生した場合は、DB2インスタンスが実行中であり、資格情報が正しいことを確認してください。