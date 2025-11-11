---
audio: false
lang: ja
layout: post
title: BeanDefinitionStoreException
translated: true
type: note
---

提供されたエラーメッセージによると、IBM WebSphere上でOSGiサポート付きで動作するJavaアプリケーションが、Spring Frameworkアプリケーションコンテキストの初期化中に`BeanDefinitionStoreException`に遭遇しています。この例外は「無効なBean定義」を示しており、通常はSpring設定の設定ミスに起因します。以下に、問題のトラブルシューティングと修正のための包括的なガイドを示します。

---

## 問題の理解
エラーからわかること：
- **例外**: `org.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition`
- **主要コンポーネント**: スタックトレース内の`PlaceholderConfigurerSupport`、`PropertySourcesPlaceholderConfigurer`、`AbstractApplicationContext`への言及。
- **コンテキスト**: Webアプリケーション環境におけるWebSphere上の`ContextLoader`によってトリガーされる、Springアプリケーションコンテキストの`refresh`プロセス中に障害が発生。
- **根本原因**: 未解決のプロパティプレースホルダー、無効なBean定義、またはWebSphere/OSGi環境に特有のデプロイメント関連の問題が原因である可能性が高い。

これは、Springが設定エラーのために1つ以上のBeanを正しく定義または初期化できないことを示唆しています。段階的に解決していきましょう。

---

## ステップバイステップでの修正

### 1. プロパティプレースホルダーの確認
**理由**: スタックトレースは`PlaceholderConfigurerSupport`と`PropertySourcesPlaceholderConfigurer`を強調しており、これらはプロパティ解決を処理します。Bean定義が`${admin.email}`のようなプレースホルダーを使用していて、それが定義されていない場合、Springは失敗します。

**修正方法**:
- **プロパティファイルの場所を特定**: `application.properties`または`application.yml`ファイルがクラスパス内（例: `src/main/resources`）にあることを確認してください。
- **プロパティを確認**: ファイルを開き、Bean定義で参照されているすべてのプレースホルダーが定義されていることを確認してください。例:
  ```properties
  admin.email=admin@example.com
  ```
- **タイプミスを修正**: プロパティ名やファイルパス内のタイプミスを探してください。
- **設定のセットアップ**:
  - **XML**: XMLを使用している場合、`<context:property-placeholder>`タグを確認してください:
    ```xml
    <context:property-placeholder location="classpath:application.properties"/>
    ```
  - **Java Config**: `@Configuration`を使用している場合、`PropertySourcesPlaceholderConfigurer`が設定されていることを確認してください:
    ```java
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
    ```

### 2. Bean定義の検査
**理由**: 「Invalid bean definition」メッセージは、Spring設定内でのBeanの定義方法に問題があることを示しています。

**修正方法**:
- **XML設定**:
  - Spring XMLファイル（例: `applicationContext.xml`）を開き、以下を確認してください:
    - Bean IDとクラス名が正しく、クラスパス上に存在する。
    - プロパティが有効で、セッターメソッドまたはコンストラクタ引数と一致する。
    - 正しいBeanの例:
      ```xml
      <bean id="myBean" class="com.example.MyClass">
          <property name="email" value="${admin.email}"/>
      </bean>
      ```
  - IDEを使用してXML構文とスキーマを検証してください。
- **Java設定**:
  - `@Configuration`クラス内の`@Bean`メソッドを確認してください:
    ```java
    @Bean
    public MyClass myBean() {
        MyClass bean = new MyClass();
        bean.setEmail(env.getProperty("admin.email"));
        return bean;
    }
    ```
  - 戻り値の型とメソッド名が有効であることを確認してください。
- **コンポーネントスキャン**:
  - `@Component`、`@Service`などを使用している場合、ベースパッケージがスキャンされていることを確認してください:
    ```java
    @ComponentScan("com.example")
    ```

### 3. 循環依存関係の解決
**理由**: 2つのBeanが互いに依存している場合（例: Bean AがBean Bを必要とし、Bean BがBean Aを必要とする）、Springはそれらの初期化に失敗する可能性があります。

**修正方法**:
- **`@Lazy`の使用**:
  - 依存関係の1つに`@Lazy`を注釈して初期化を遅延させます:
    ```java
    @Autowired
    @Lazy
    private BeanB beanB;
    ```
- **リファクタリング**: 可能であれば、循環参照を避けるようにBeanを再設計します。

### 4. 依存関係とクラスパスの確認
**理由**: 不足している、または互換性のないライブラリにより、Bean定義で参照されているクラスが利用できなくなる可能性があります。

**修正方法**:
- **Maven/Gradle**:
  - 必要なすべてのSpring依存関係が`pom.xml`（Maven）または`build.gradle`（Gradle）にあることを確認してください。Mavenの例:
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - 競合を確認するために`mvn dependency:tree`または`gradle dependencies`を実行してください。
- **クラスパス**: すべてのクラス（例: `com.example.MyClass`）がコンパイルされ、デプロイされたアプリケーションで利用可能であることを確認してください。

### 5. デバッグログの有効化
**理由**: より詳細なログは、障害を引き起こしている正確なBeanやプロパティを特定するのに役立ちます。

**修正方法**:
- `application.properties`に追加:
  ```properties
  logging.level.org.springframework=DEBUG
  ```
- アプリケーションを再起動し、Beanの作成やプロパティ解決に関する特定のエラーのログを確認してください。

### 6. WebSphere/OSGi設定の検証
**理由**: スタックトレースはWebSphereとOSGiコンポーネントを示しており、デプロイメント固有の問題を引き起こす可能性があります。

**修正方法**:
- **バンドル解決**: すべてのOSGiバンドルが正しくデプロイされ、それらの依存関係がWebSphereで解決されていることを確認してください。
- **クラスパス**: WebSphereのクラスローダーにアプリケーションのJARとプロパティファイルが含まれていることを確認してください。
- **サーバーログ**: WebSphereログ（例: `SystemOut.log`）で追加のエラーや警告を確認してください。

### 7. 以前のログの確認
**理由**: ログの抜粋は10:15:57にプロパティの読み込み成功から始まっていますが、エラーは16:56:57に発生しています。以前の問題が障害を引き起こした可能性があります。

**修正方法**:
- ログファイルを上にスクロールするか、`BeanDefinitionStoreException`の前の警告やエラーについてアーカイブされたログを確認してください。

---

## 一般的なシナリオと解決策
- **未解決のプレースホルダー**:
  - **問題**: Bean定義内の`${admin.email}`が`application.properties`に定義されていない。
  - **修正**: ファイルに`admin.email=somevalue`を追加する。
- **クラスの欠落**:
  - **問題**: `<bean class="com.example.NonExistentClass">`
  - **修正**: クラス名を修正するか、不足している依存関係を追加する。
- **構文エラー**:
  - **問題**: 不正な形式のXMLまたはJava設定。
  - **修正**: IDEや`xmllint`などのツールで検証する。

---

## 最終ステップ
1. **修正を適用**: スタックトレースに基づいて最も可能性の高い原因であるプロパティプレースホルダーとBean定義から開始します。
2. **ローカルでテスト**: 開発環境で再デプロイしてテストします。
3. **WebSphereにデプロイ**: ローカルで動作する場合、WebSphereに再デプロイし、ログを監視します。
4. **反復**: エラーが解決しない場合、デバッグログを使用して障害が発生しているBeanやプロパティを特定します。

これらの手順に従うことで、`BeanDefinitionStoreException`を解決し、Springアプリケーションコンテキストを正常に初期化できるはずです。問題が解決しない場合は、さらなる支援のために（設定ファイルや完全なログなどの）より具体的な詳細を共有してください。