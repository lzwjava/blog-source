---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: パラメータを使用したDB2ストアドプロシージャの呼び出し
translated: true
type: note
---

### 前提条件とコンテキスト
お問い合わせは、IBMデータベースシステム（IBM DB2（Linux/Unix/Windows、z/OS、iSeries）など）における*ストアドプロシージャ*（おそらく「store procedure」のタイプミス）の呼び出しに関するものと思われます。ストアドプロシージャは、入力パラメータを受け取り、操作を実行し、出力や結果を返すことができる、データベースに保存された実行可能なスクリプトです。正確な構文は、プログラミング言語とIBM環境（SQL、COBOL、RPG、JDBC経由のJavaなど）によって異なります。ここでは、リレーショナルデータベースで標準的である、DB2におけるSQLベースのCALLステートメントの最も一般的なケースに焦点を当てます。

もし異なるIBMプラットフォーム（IBM i CLコマンド、MQ、Watson Queryなど）を使用している場合は、詳細を提供していただければ、より適切なアドバイスを提供できます。

### DB2ストアドプロシージャ呼び出しでパラメータを渡す方法
DB2におけるストアドプロシージャは、SQLの`CALL`ステートメントを使用して呼び出します。パラメータは、プロシージャの定義（入力用のIN、出力用のOUT、両方用のINOUTなど）に一致する、括弧内のカンマ区切りリストで渡されます。

#### ステップバイステップガイド
1.  **プロシージャのシグネチャを定義または把握する**: プロシージャ名とパラメータを確実に把握してください。例えば、プロシージャは以下のように定義されているかもしれません：
    ```sql
    CREATE PROCEDURE update_employee (IN emp_id INT, IN new_salary DECIMAL(10,2), OUT status_msg VARCHAR(100))
    ```
    - ここで、`emp_id`は入力（IN）、`new_salary`は入力、`status_msg`は出力（OUT）です。

2.  **CALLステートメントを使用する**: SQL環境（DB2コマンドラインプロセッサ、またはJavaなどのプログラムに埋め込まれた場合）で、以下のようにプロシージャを呼び出します：
    ```sql
    CALL update_employee(12345, 75000.00, ?);
    ```
    - `?`はOUTパラメータのプレースホルダーです。プログラムによる呼び出しでは、出力を結果セットやホスト変数で処理します。
    - 入力はリテラルまたは変数として渡され、出力はプレースホルダーまたはバインドされた変数を介してキャプチャされます。

3.  **パラメータタイプの取り扱い**:
    - **INパラメータ**: 値を直接渡します（例：数値、引用符で囲んだ文字列）。
    - **OUT/INOUTパラメータ**: CALL内で`?`を使用し、コード内でそれらをバインドして実行後に値を取得します。
    - 順序と型を正確に一致させてください。不一致はエラー（例：無効なパラメータに対するSQLCODE -440）の原因となります。

4.  **コード例**:
    - **DB2 CLP（コマンドライン）経由**: 直接SQLを実行。
        ```sql
        CALL my_proc('input_value', ?);
        ```
        OUTパラメータは`FETCH FIRST FROM`で取得するか、スクリプト内で処理します。
    - **JDBC（Java）経由**:
        ```java
        CallableStatement stmt = conn.prepareCall("{CALL update_employee(?, ?, ?)}");
        stmt.setInt(1, 12345);          // INパラメータ
        stmt.setBigDecimal(2, new java.math.BigDecimal("75000.00")); // INパラメータ
        stmt.registerOutParameter(3, Types.VARCHAR); // OUTパラメータ
        stmt.execute();
        String status = stmt.getString(3); // OUTパラメータを取得
        ```
    - **IBM i上のRPG経由**: パラメータ型に一致する変数宣言と共に`CALLP`を使用。
        ```rpg
        D PROC_PARAM    S                   LIKE(PARAM_TYPE)
        PROC_PARAM = 'value';
        CALLP MY_PROC(PROC_PARAM);
        ```
    - **エラーハンドリング**: 呼び出し後にSQLSTATEまたはSQLCODEを確認。例：'00000'は成功を意味します。

#### 主なヒントと根拠
-   **DB2ドキュメントからの根拠**: IBMの公式DB2 SQLリファレンス（LUW v11.5やz/OS用など）によると、`CALL`ステートメントはオプションのパラメータリストで定義されています。例えば、構文は`CALL procedure-name [(parameter [, parameter] ...)]`です。これはリレーショナルデータベースの業界標準に一致し、一貫性のためにDB2の各種バリアントでサポートされています（IBM Knowledge Centerを参照）。
-   **バリエーション**: IBM i (AS400) では、RPGプログラムに対して、`CALL PGM(MYPROC) PARM('value')`のようなCL（コマンド言語）呼び出しを使用する場合があります。メインフレームCOBOLでは、ホスト変数と共に`EXEC SQL CALL...`を埋め込みます。
-   **テスト**: 呼び出し前に`db2 describe routine procedure_name`を使用してパラメータを検査します。
-   **制限事項**: 多数のパラメータセットには配列や結果セットが必要な場合があり、複雑な型には特定の取り扱いが必要です。

もしこれがあなたの環境に合わない場合（IBM Watsonや他のツールなど）、正確な手順を得るためにプラットフォームや言語などの詳細なコンテキストを共有してください。