---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot例外処理
translated: true
type: note
---

Spring Bootやより広範なSpring Frameworkを扱う際、開発者は設定の問題、実行時エラー、APIの不適切な使用などが原因で例外に遭遇することがよくあります。以下は、遭遇する可能性のある一般的な例外と、その典型的な原因と解決策のリストです。これらの例外は明確にするためにカテゴリ別にグループ化されています。

---

### **1. 設定関連の例外**

- **`org.springframework.beans.factory.BeanCreationException`**:
  - **原因**: 依存関係の欠落、設定ミス、インスタンス化エラーなどによりBeanの作成に失敗しました。
  - **例**: `@Component`、`@Service`の欠落、または`@Autowired`された依存関係が見つからない。
  - **解決策**: Bean定義を確認し、依存関係が利用可能であることを保証し、アノテーションを検証してください。

- **`org.springframework.beans.factory.NoSuchBeanDefinitionException`**:
  - **原因**: Springがアプリケーションコンテキスト内に要求された型または名前のBeanを見つけられません。
  - **例**: 定義されていない、またはスキャンされていないBeanを`@Autowired`しようとする。
  - **解決策**: Beanがアノテーション（例: `@Component`）で修飾されており、コンポーネントスキャンのパス内にあることを確認してください。

- **`org.springframework.context.ApplicationContextException`**:
  - **原因**: Springアプリケーションコンテキストの初期化における一般的な失敗。
  - **例**: `application.properties`内の無効な設定、または`@Configuration`クラス内の構文エラー。
  - **解決策**: 根本原因（例: 無効なプロパティや欠落したリソース）についてスタックトレースを確認してください。

- **`org.springframework.beans.factory.UnsatisfiedDependencyException`**:
  - **原因**: Beanが必要とする依存関係を満たすことができません。
  - **例**: 循環依存関係またはインターフェースに対する実装の欠落。
  - **解決策**: 循環依存関係を解消する（例: `@Lazy`を使用）か、欠落している依存関係を提供してください。

---

### **2. WebおよびREST関連の例外**

- **`org.springframework.web.bind.MissingServletRequestParameterException`**:
  - **原因**: HTTPリクエストに必須のリクエストパラメータが欠落しています。
  - **例**: `@RequestParam("id")`が指定されているが、クライアントが`id`を送信しなかった。
  - **解決策**: パラメータをオプションにする（`required = false`）か、クライアントがそれを含めることを保証してください。

- **`org.springframework.http.converter.HttpMessageNotReadableException`**:
  - **原因**: リクエストボディをデシリアライズできません（例: 不正な形式のJSON）。
  - **例**: 無効なJSONを`@RequestBody`エンドポイントに送信する。
  - **解決策**: リクエストペイロードを検証し、対象のオブジェクト構造と一致することを保証してください。

- **`org.springframework.web.method.annotation.MethodArgumentTypeMismatchException`**:
  - **原因**: メソッド引数を期待される型に変換できません。
  - **例**: `int`を期待するパラメータに`"abc"`のような文字列を渡す。
  - **解決策**: 入力を検証するか、カスタムコンバーターを使用してください。

- **`org.springframework.web.servlet.NoHandlerFoundException`**:
  - **原因**: リクエストされたURLに対するコントローラーマッピングが存在しません。
  - **例**: `@RequestMapping`のタイプミスやコントローラーの欠落。
  - **解決策**: エンドポイントのマッピングを確認し、コントローラーがスキャンされていることを保証してください。

---

### **3. データアクセス (Spring Data/JPA/Hibernate) 関連の例外**

- **`org.springframework.dao.DataIntegrityViolationException`**:
  - **原因**: データベース操作が制約（例: 一意キーや外部キー）に違反しました。
  - **例**: 重複した主キー値の挿入。
  - **解決策**: データの一意性を確認するか、例外を適切に処理してください。

- **`org.springframework.orm.jpa.JpaSystemException`**:
  - **原因**: JPA関連の一般的な実行時エラー。多くの場合、Hibernate例外をラップしています。
  - **例**: 制約違反や接続の問題。
  - **解決策**: 詳細についてネストされた例外（例: `SQLException`）を調査してください。

- **`org.hibernate.LazyInitializationException`**:
  - **原因**: アクティブなセッションの外でレイジーロードされたエンティティにアクセスしようとしました。
  - **例**: トランザクション終了後に`@OneToMany`リレーションシップにアクセスする。
  - **解決策**: イーガーフェッチを使用する、クエリ内でフェッチする（例: `JOIN FETCH`）、またはオープンなセッションを保証してください。

- **`org.springframework.dao.InvalidDataAccessApiUsageException`**:
  - **原因**: Spring DataまたはJDBC APIの誤った使用。
  - **例**: 値を期待するクエリにnullパラメータを渡す。
  - **解決策**: クエリパラメータとAPIの使用法を検証してください。

---

### **4. セキュリティ関連の例外**

- **`org.springframework.security.access.AccessDeniedException`**:
  - **原因**: 認証されたユーザーがリソースに対する権限を持っていません。
  - **例**: 必要なロールなしで保護されたエンドポイントにアクセスする。
  - **解決策**: `@PreAuthorize`やセキュリティ設定を確認し、ロール/権限を調整してください。

- **`org.springframework.security.authentication.BadCredentialsException`**:
  - **原因**: ユーザー名またはパスワードが間違っているため、認証に失敗しました。
  - **例**: ログインフォームでユーザーが誤った資格情報を入力する。
  - **解決策**: 資格情報が正しいことを保証する。ユーザーフィードバックのためのエラーハンドリングをカスタマイズする。

- **`org.springframework.security.authentication.DisabledException`**:
  - **原因**: ユーザーアカウントが無効化されています。
  - **例**: `UserDetails`の実装が`isEnabled() == false`を返す。
  - **解決策**: アカウントを有効にするか、ユーザーステータスを更新してください。

---

### **5. その他の実行時例外**

- **`java.lang.IllegalStateException`**:
  - **原因**: Springが実行中に無効な状態に遭遇しました。
  - **例**: 完全に初期化されていないBeanのメソッドを呼び出す。
  - **解決策**: ライフサイクルメソッドやBeanの初期化順序を確認してください。

- **`org.springframework.transaction.TransactionException`**:
  - **原因**: トランザクション管理中の問題が発生しました。
  - **例**: 未処理の例外によるトランザクションのロールバック。
  - **解決策**: 適切な`@Transactional`の使用を保証し、トランザクション内で例外を処理してください。

- **`java.lang.NullPointerException`**:
  - **原因**: nullオブジェクト参照にアクセスしようとしました。
  - **例**: 設定ミスにより`@Autowired`された依存関係が注入されなかった。
  - **解決策**: nullチェックを追加するか、依存関係が欠落している理由をデバッグしてください。

---

### **6. Spring Boot固有の例外**

- **`org.springframework.boot.context.embedded.EmbeddedServletContainerException`** (旧バージョン) または **`org.springframework.boot.web.server.WebServerException`** (新バージョン):
  - **原因**: 組み込みWebサーバー（例: Tomcat, Jetty）の起動に失敗しました。
  - **例**: ポートが既に使用中（例: `8080`）。
  - **解決策**: `application.properties`でポートを変更する（`server.port=8081`）か、使用中のポートを解放してください。

- **`org.springframework.boot.autoconfigure.jdbc.DataSourceProperties$DataSourceBeanCreationException`**:
  - **原因**: データソースの設定に失敗しました。
  - **例**: `spring.datasource.url/username/password`の欠落または誤り。
  - **解決策**: `application.properties`または`application.yml`内のデータソースプロパティを検証してください。

- **`org.springframework.boot.SpringApplication - Application run failed`**:
  - **原因**: Spring Boot起動中の一般的な失敗。
  - **例**: 設定ミス、Beanの欠落、依存関係の競合。
  - **解決策**: 根本原因について完全なスタックトレースを確認してください。

---

### **例外を処理するためのベストプラクティス**

1. **グローバル例外処理**:
   - `@ControllerAdvice`と`@ExceptionHandler`を使用して、アプリケーション全体で一貫して例外をキャッチし処理します。
   - 例:
     ```java
     @ControllerAdvice
     public class GlobalExceptionHandler {
         @ExceptionHandler(DataIntegrityViolationException.class)
         public ResponseEntity<String> handleDataIntegrityViolation() {
             return ResponseEntity.status(HttpStatus.CONFLICT).body("データ整合性違反が発生しました。");
         }
     }
     ```

2. **ロギング**:
   - SLF4J/Logbackなどのフレームワークを使用して例外をログに記録し、デバッグを支援します。

3. **カスタム例外**:
   - アプリケーション固有の例外を定義し、適切なHTTPステータスにマッピングします。

4. **検証**:
   - `@Valid`とBean Validation（例: `@NotNull`）を使用して、エラーを早期に検出し、実行時例外を回避します。

5. **デバッグ**:
   - `application.properties`で詳細なロギング（`logging.level.org.springframework=DEBUG`）を有効にして問題を追跡します。

---

### **まとめ**

これらの例外は、Spring BootやSpring Frameworkを使用する際に遭遇する最も一般的なものの一部です。それらの原因と解決策を理解することは、開発とデバッグを大幅に高速化することができます。特定の例外に直面してより深く掘り下げる必要がある場合は、詳細を共有してください。それに合わせて説明を提供します！