---
audio: false
generated: true
lang: ja
layout: post
title: Java SQLステートメントの種類比較
translated: true
type: note
---

Javaの`java.sql`パッケージでは、`Statement`、`PreparedStatement`、`CallableStatement`はSQLクエリを実行するためのインターフェースですが、それぞれ異なる目的と特徴を持っています。以下に簡潔な比較を示します：

1. **Statement**：
   - **目的**：パラメータのない静的なSQLクエリの実行に使用
   - **動作方法**：完全なSQLクエリを文字列として`executeQuery()`または`executeUpdate()`メソッドに渡す
   - **主な特徴**：
     - シンプルな1回限りのクエリに適している
     - パラメータバインディングがないため、値を手動でSQL文字列に連結する必要があり、SQLインジェクションのリスクがある
     - 繰り返し実行するクエリには非効率的（毎回SQLを再解析する）
   - **例**：
     ```java
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = 1");
     ```

2. **PreparedStatement**：
   - **目的**：パラメータ化された入力を持つプリコンパイル済みSQLクエリの実行に使用
   - **動作方法**：プレースホルダー（`?`）を含むクエリを定義し、`setInt()`、`setString()`などのメソッドでパラメータ値を設定
   - **主な特徴**：
     - SQLロジックとデータを分離することでSQLインジェクションを防止
     - 繰り返し実行するクエリに効率的（SQLは1回コンパイルされ再利用される）
     - 動的なパラメータバインディングをサポートし、より安全で柔軟
   - **例**：
     ```java
     PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
     pstmt.setInt(1, 1);
     ResultSet rs = pstmt.executeQuery();
     ```

3. **CallableStatement**：
   - **目的**：データベースのストアドプロシージャを実行するために使用
   - **動作方法**：`PreparedStatement`を拡張し、入力（`IN`）、出力（`OUT`）、入力出力（`IN OUT`）パラメータを扱うストアドプロシージャ呼び出しをサポート
   - **主な特徴**：
     - データベースのストアドプロシージャ専用に設計
     - `registerOutParameter()`などのメソッドを使用した出力パラメータの登録を可能にする
     - ストアドプロシージャのロジックに対する複雑なパラメータ処理をサポート
   - **例**：
     ```java
     CallableStatement cstmt = conn.prepareCall("{call getUserName(?, ?)}");
     cstmt.setInt(1, 1);
     cstmt.registerOutParameter(2, Types.VARCHAR);
     cstmt.execute();
     String username = cstmt.getString(2);
     ```

**主な違い**：
| 機能                   | Statement                          | PreparedStatement                  | CallableStatement                 |
|------------------------|------------------------------------|------------------------------------|------------------------------------|
| **目的**               | 静的なSQLクエリ                   | パラメータ化されたSQLクエリ       | ストアドプロシージャの実行        |
| **SQLインジェクション** | 脆弱（手動連結）                  | 安全（パラメータバインディング）  | 安全（パラメータバインディング）  |
| **パフォーマンス**      | 非効率（プリコンパイルなし）      | 効率的（プリコンパイル済み）      | ストアドプロシージャに効率的      |
| **使用ケース**          | シンプルで1回限りのクエリ         | 繰り返し実行またはパラメータ化クエリ | パラメータを持つストアドプロシージャ |
| **パラメータサポート**  | なし                              | 入力パラメータのみ                | 入力、出力、IN/OUTパラメータ      |

**使用する場面**：
- `Statement`は、セキュリティやパフォーマンスが重要でない、シンプルで繰り返し実行しないクエリに使用
- `PreparedStatement`は、パラメータ化されたクエリ、繰り返し実行、またはSQLインジェクション防止が必要な場合に使用
- `CallableStatement`は、入力/出力パラメータを持つデータベースのストアドプロシージャを呼び出す場合に使用

この説明は、私の知識更新時点での標準的なJava SQL APIの動作に基づいています。さらに詳細や例が必要な場合は、お知らせください！