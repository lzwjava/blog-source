---
audio: false
lang: hant
layout: post
title: BeanDefinitionStoreException
translated: true
type: note
---

根據您提供的錯誤資訊，您的 Java 應用程式在支援 OSGi 的 IBM WebSphere 上運行時，於 Spring Framework 應用程式上下文初始化期間遇到了 `BeanDefinitionStoreException`。此異常表示「無效的 bean 定義」，通常源於 Spring 設定中的配置錯誤。以下是一份完整的疑難排解與修復指南。

---

## 問題理解
錯誤顯示：
- **異常**：`org.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition`
- **關鍵元件**：堆疊追蹤中提及 `PlaceholderConfigurerSupport`、`PropertySourcesPlaceholderConfigurer` 和 `AbstractApplicationContext`。
- **上下文**：失敗發生在 Spring 應用程式上下文的 `refresh` 過程中，由 Web 應用程式環境中的 `ContextLoader` 在 WebSphere 上觸發。
- **根本原因**：可能與未解析的屬性佔位符、無效的 bean 定義，或 WebSphere/OSGi 環境中的部署特定問題有關。

這表明 Spring 因配置錯誤而無法正確定義或初始化一個或多個 bean。讓我們逐步解決此問題。

---

## 逐步修復

### 1. 驗證屬性佔位符
**原因**：堆疊追蹤突顯了 `PlaceholderConfigurerSupport` 和 `PropertySourcesPlaceholderConfigurer`，它們負責處理屬性解析。如果 bean 定義使用了如 `${admin.email}` 的佔位符但未定義，Spring 將會失敗。

**修復方法**：
- **定位屬性檔案**：確保您的 `application.properties` 或 `application.yml` 檔案位於 classpath 中（例如 `src/main/resources`）。
- **檢查屬性**：開啟檔案並確認所有在 bean 定義中引用的佔位符均已定義。例如：
  ```properties
  admin.email=admin@example.com
  ```
- **修正拼寫錯誤**：檢查屬性名稱或檔案路徑中的拼寫錯誤。
- **配置設定**：
  - **XML**：如果使用 XML，請驗證 `<context:property-placeholder>` 標籤：
    ```xml
    <context:property-placeholder location="classpath:application.properties"/>
    ```
  - **Java 配置**：如果使用 `@Configuration`，請確保配置了 `PropertySourcesPlaceholderConfigurer`：
    ```java
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
    ```

### 2. 檢查 Bean 定義
**原因**：「無效的 bean 定義」訊息指向 Spring 配置中 bean 定義方式的問題。

**修復方法**：
- **XML 配置**：
  - 開啟您的 Spring XML 檔案（例如 `applicationContext.xml`）並檢查：
    - Bean ID 和類別名稱正確且存在於 classpath 中。
    - 屬性有效且符合 setter 方法或建構函式參數。
    - 正確 bean 的範例：
      ```xml
      <bean id="myBean" class="com.example.MyClass">
          <property name="email" value="${admin.email}"/>
      </bean>
      ```
  - 使用 IDE 驗證 XML 語法和結構描述。
- **Java 配置**：
  - 檢查 `@Configuration` 類別中的 `@Bean` 方法：
    ```java
    @Bean
    public MyClass myBean() {
        MyClass bean = new MyClass();
        bean.setEmail(env.getProperty("admin.email"));
        return bean;
    }
    ```
  - 確保返回型別和方法名稱有效。
- **元件掃描**：
  - 如果使用 `@Component`、`@Service` 等，請確認基礎套件已被掃描：
    ```java
    @ComponentScan("com.example")
    ```

### 3. 解決循環依賴
**原因**：如果兩個 bean 相互依賴（例如 Bean A 需要 Bean B，而 Bean B 需要 Bean A），Spring 可能無法初始化它們。

**修復方法**：
- **使用 `@Lazy`**：
  - 使用 `@Lazy` 註解延遲其中一個依賴的初始化：
    ```java
    @Autowired
    @Lazy
    private BeanB beanB;
    ```
- **重構**：如果可能，重新設計您的 bean 以避免循環引用。

### 4. 檢查依賴項和 Classpath
**原因**：缺少或不相容的函式庫可能導致 bean 定義中引用的類別不可用。

**修復方法**：
- **Maven/Gradle**：
  - 確保所有必需的 Spring 依賴項都在您的 `pom.xml`（Maven）或 `build.gradle`（Gradle）中。Maven 範例：
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - 執行 `mvn dependency:tree` 或 `gradle dependencies` 以檢查衝突。
- **Classpath**：確認所有類別（例如 `com.example.MyClass`）已編譯並在部署的應用程式中可用。

### 5. 啟用除錯日誌記錄
**原因**：更詳細的日誌可以精確定位導致失敗的具體 bean 或屬性。

**修復方法**：
- 新增至 `application.properties`：
  ```properties
  logging.level.org.springframework=DEBUG
  ```
- 重新啟動應用程式並檢視日誌中有關 bean 建立或屬性解析的具體錯誤。

### 6. 驗證 WebSphere/OSGi 配置
**原因**：堆疊追蹤顯示了 WebSphere 和 OSGi 元件，這可能引入部署特定的問題。

**修復方法**：
- **套件解析**：確保所有 OSGi 套件已正確部署，且其依賴項在 WebSphere 中已解析。
- **Classpath**：驗證 WebSphere 的類別載入器包含您的應用程式的 JAR 和屬性檔案。
- **伺服器日誌**：檢查 WebSphere 日誌（例如 `SystemOut.log`）以獲取其他錯誤或警告。

### 7. 檢視先前的日誌
**原因**：日誌片段從 10:15:57 的成功屬性載入開始，但錯誤發生在 16:56:57。較早的問題可能觸發了失敗。

**修復方法**：
- 在日誌檔案中向上滾動或檢查歸檔日誌，尋找在 `BeanDefinitionStoreException` 之前的警告或錯誤。

---

## 常見情境與解決方案
- **未解析的佔位符**：
  - **問題**：bean 定義中的 `${admin.email}` 未在 `application.properties` 中定義。
  - **修復**：在檔案中新增 `admin.email=somevalue`。
- **缺少類別**：
  - **問題**：`<bean class="com.example.NonExistentClass">`
  - **修復**：更正類別名稱或新增缺少的依賴項。
- **語法錯誤**：
  - **問題**：格式錯誤的 XML 或 Java 配置。
  - **修復**：使用 IDE 或如 `xmllint` 的工具進行驗證（針對 XML）。

---

## 最終步驟
1. **應用修復**：從屬性佔位符和 bean 定義開始，因為根據堆疊追蹤，它們是最可能的原因。
2. **本地測試**：重新部署並在開發環境中測試。
3. **部署至 WebSphere**：如果在本地運行正常，則重新部署至 WebSphere 並監控日誌。
4. **迭代**：如果錯誤仍然存在，使用除錯日誌來縮小失敗的 bean 或屬性範圍。

透過遵循這些步驟，您應該能解決 `BeanDefinitionStoreException` 並使您的 Spring 應用程式上下文成功初始化。如果問題仍然存在，請分享更多具體細節（例如配置檔案或完整日誌）以獲得進一步協助。