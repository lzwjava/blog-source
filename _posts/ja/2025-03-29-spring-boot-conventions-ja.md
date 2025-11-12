---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot Java コーディング規約
translated: true
type: note
---

## 1. 基本原則
- 標準の Java コード規約に従う
- 可読性と保守性を優先する
- Spring エコシステム全体での一貫性
- コア Java のベストプラクティスに沿う

## 2. コードフォーマット

### 一般的なガイドライン
- IntelliJ IDEA のデフォルトフォーマットを使用する
- 4スペースのインデント（タブは使用しない）
- 最大行長は120文字
- 標準的な Java のブレーススタイルを使用する

### 具体的なフォーマットルール
- メソッド間には空白行を入れる
- 末尾の空白文字は削除する
- Unix スタイルの行末（LF）を使用する

## 3. 命名規則

### クラス命名
- 説明的で意味のある名前を使用する
- アッパーキャメルケースを使用する
- 例：
  - `ConfigurationProperties`
  - `AutoConfigurationImportSelector`
  - `SpringApplication`

### メソッド命名
- ローワーキャメルケースを使用する
- 動詞または動詞句を使用する
- 例：
  - `configure()`
  - `registerBeanDefinitions()`
  - `isEnabledByDefault()`

## 4. アノテーションの実践

### アノテーションの順序
- アノテーションの標準的な順序：
  1. オーバーライドアノテーション（`@Override`）
  2. スコープアノテーション（`@Component`、`@Service`）
  3. 依存性注入アノテーション
  4. トランザクションアノテーション
  5. カスタムプロジェクトアノテーション

### アノテーションの配置
```java
@Component
@Transactional
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

## 5. 依存性注入

### 推奨される注入方法
- コンストラクタインジェクション
- フィールドインジェクションは避ける
- コンストラクタに `@Autowired` を使用する

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

## 6. ロギング
- ロギングには SLF4J を使用する
- `private static final Logger` または Lombok の `@Slf4j` を使用する

```java
@Slf4j
@Service
public class UserService {
    public void processUser(User user) {
        log.info("Processing user: {}", user.getUsername());
    }
}
```

## 7. エラーハンドリング
- 具体的な例外を使用する
- 意味のあるエラーメッセージを提供する
- グローバルな例外処理には `@ControllerAdvice` を使用する

## 8. 設定
- `application.properties` よりも `application.yml` を使用する
- プロファイル固有の設定を使用する
- 設定値は外部化する

## 9. テスト
- JUnit 5 を使用する
- Spring Boot Test ユーティリティを活用する
- Arrange-Act-Assert パターンに従う

## 10. 追加リソース
- [Spring Boot GitHub コーディングスタイル](https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.md)
- [Spring Framework ガイドライン](https://github.com/spring-projects/spring-framework/wiki/Code-Style)