---
audio: false
generated: true
lang: ja
layout: post
title: 正確で安全な自然言語からSQLへのシステム構築
translated: true
type: note
---

### NL-to-SQLシステム構築における重要な焦点領域

自然言語からSQL（NL-to-SQL）への変換システムを構築するには、日常言語でのユーザークエリを実行可能なSQL文に翻訳する必要があり、多くの場合、LLM（GPTバリアントやHugging Faceの専門モデルなど）のようなAIモデルが使用されます。あなたのPostgreSQLスキーマと例示クエリに基づき、焦点を当てる主な領域は以下の通りです：

#### 1. **精度とスキーマの理解**
   - **スキーマ認識**：AIプロンプトには常に完全なデータベーススキーマ（テーブル、カラム、データ型、リレーションシップ）を提供してください。これによりモデルが正しいSQLを生成するのに役立ちます。あなたのケースでは、`first_name`、`created_at`、`date_of_birth`、`last_login`などのカラムを強調し、幻覚（例：存在しないフィールドの考案）を避けてください。
   - **曖昧さの処理**：自然言語は曖昧です—例えば、「around the day last month」は±1日を意味する可能性がありますが、プロンプトを通じてあいまいな用語（例：「recent week」を7日間と解釈）の解釈を明確にしてください。解釈を導くためにプロンプト内で例を使用してください。
   - **データ型と関数**：PostgreSQL固有の構文、例えば日付に`AGE()`を使用、大文字小文字を区別しない文字列に`ILIKE`を使用、適切なキャスト（例：あなたの例での`CAST(created_at AS DATE)`）に焦点を当ててください。SQL方言の違いについてモデルを訓練またはファインチューニングしてください。
   - **エッジケース**：複数のテーブルを含む結合、集約（例：COUNT、SUM）、または副問い合わせなどの複雑なクエリを処理してください。`password_hash`や`account_balance`などの機密性の高いフィールドを含むクエリについてテストしてください。

#### 2. **パフォーマンスと最適化**
   - 効率的なSQLを生成：モデルにインデックスの使用（例：`created_at`や`first_name`に対する）、結果の制限（デフォルトで`LIMIT`を追加）、フルテーブルスキャンの回避を促してください。
   - スケーラビリティ：大規模なデータセットの場合、クエリ最適化ツールを統合するか、生成されたSQLを実行計画に対して検証してください。

#### 3. **エラーハンドリングと検証**
   - 実行前に生成されたSQLを構文解析および検証してください（例：Pythonで`sqlparse`のようなSQLパーサライブラリを使用）。
   - フォールバック応答を提供：クエリが不明確な場合、無効なSQLを生成する代わりにユーザーに明確化を促してください。

#### 4. **セキュリティと安全性**
   - **SQLインジェクションの防止**：リスクは生成されたSQLを実行することから生じます。ユーザー入力を直接SQL文字列に連結しないでください。代わりに：
     - 実行時に**パラメータ化クエリ**またはプリペアドステートメントを使用してください（例：Pythonの`psycopg2`で：`cursor.execute("SELECT * FROM users WHERE first_name = %s", (name,))`）。
     - AIにプレースホルダー（例：`WHERE first_name ILIKE %s`）を含むSQLを生成し、値は別途バインドするように指示してください。
     - NL入力をサニタイズ：悪意のあるパターン（例：「DROP」や「;」などのSQLキーワードを検出する正規表現を使用）を除去するためにユーザークエリを前処理してください。
     - 読み取り専用に制限：AIをSELECTクエリのみの生成に制限し—DDL（例：CREATE/DROP）やDML（例：INSERT/UPDATE）をブロックしてください。「SELECT文のみを生成し、データを変更しないでください」のようなプロンプト指示を通じて行います。
   - **データアクセスの制御**：
     - **行レベルセキュリティ（RLS）**：PostgreSQLで、テーブルにRLSポリシーを有効にしてください（例：`ALTER TABLE users ENABLE ROW LEVEL SECURITY; CREATE POLICY user_policy ON users USING (role = current_user);`）。これにより、クエリがユーザーがアクセス権を持つ行のみを返すことが保証されます。
     - **ビューとロール**：制限されたビュー（例：`CREATE VIEW safe_users AS SELECT id, username, first_name FROM users;`）を作成し、データベースロールを通じてアクセスを許可してください。AIは基本テーブルではなくビューをクエリするべきです。
     - **APIレイヤー**：システムをAPI（例：FastAPIを使用）でラップし、ユーザーを認証しアクセス制御（例：ユーザーロールを決定するJWTトークン）を適用してください。
     - **サンドボックス実行**：クエリを読み取り専用レプリカデータベースまたはコンテナ化環境（例：Docker）で実行し、本番データから分離してください。
     - **監査ログ**：監視のためにすべての生成SQLと実行をログに記録してください。
   - **データプライバシー**：プロンプト内で機密カラム（例：`password_hash`、`email`）をブラックリスト登録することで、それらを公開するのを避けてください：「明示的に必要とされ許可されていない限り、password_hash、emailのような機密フィールドを選択しないでください。」
   - **レート制限とクォータ**：ユーザー/セッションごとのクエリを制限することで悪用を防いでください。

#### 5. **制御された変換のためのプロンプトエンジニアリング**
   - NL-to-SQLの品質は、AIへの指示方法に大きく依存します。以下の要素を含む構造化されたプロンプトを使用してください：
     - **システムプロンプトテンプレート**：
       ```
       You are an expert SQL generator for PostgreSQL. Given the schema below and a natural language query, generate a safe, accurate SELECT query. 

       Schema:
       [Insert full schema here, e.g., CREATE TABLE users (...)]

       Rules:
       - Only generate SELECT statements. No INSERT, UPDATE, DELETE, or DDL.
       - Use parameterized placeholders (e.g., %s) for user-provided values to prevent injection.
       - Handle dates with PostgreSQL functions like AGE(), CURRENT_DATE, INTERVAL.
       - For ambiguous terms (e.g., "around last month"), interpret as [specific rule, e.g., ±1 day from the same day last month].
       - Limit results to 100 rows unless specified.
       - If the query involves age, calculate as of the current year or specified year (e.g., EXTRACT(YEAR FROM AGE(CURRENT_DATE, date_of_birth)) = 20).
       - Do not select sensitive columns like password_hash, email.
       - If unclear, respond with "Clarify: [question]".

       User Query: [NL query]
       ```
     - **プロンプト内の例**：モデルを導くために、提供されたクエリと生成されたSQLのような2-3のショット例を含めてください。
     - **連鎖思考**：モデルに段階的に推論するように指示してください：「第一に、主要なフィルターを特定。第二に、カラムにマッピング。第三に、WHERE句を構築。」
     - **ファインチューニング**：カスタムモデルを使用する場合、SpiderやWikiSQLのようなデータセット、およびあなたのスキーマ固有の例で補強されたデータセットでファインチューニングしてください。
     - **テスト**：実行精度（エラーなく実行するか？）や意味的マッチ（期待される結果を返すか？）のような指標で評価してください。

#### あなたの例示クエリへの潜在的な改善
主要な質問ではありませんが、生成されたSQLには良い要素もありますが、より安全で/正確になる可能性があります：
- パラメータを使用：`WHERE first_name ILIKE %s`に変更し、'andy'をバインドしてください。
- 年齢「as of 2025」：特定の年末に固定するために`EXTRACT(YEAR FROM AGE('2025-12-31'::date, date_of_birth)) = 20`を使用してください。
- 安全性のために`ORDER BY last_login DESC LIMIT 10;`を追加してください。

これを安全に実装するには、バックエンドレイヤー（例：AI出力から直接SQLを実行しない）が必要です。LLMライブラリ（例：NL-to-SQLチェーンのためのLangChain）を使用したスクリプトから小規模に始めてください。

コード例や特定の部分（例：Python実装）のヘルプが必要な場合は、詳細を提供してください！

**参考文献**  
[PostgreSQL Documentation: Row-Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)  
[LangChain NL-to-SQL Tutorial](https://python.langchain.com/docs/tutorials/sql_qa/)  
[Preventing SQL Injection in Python](https://realpython.com/prevent-python-sql-injection/)