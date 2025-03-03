---
audio: false
lang: hant
layout: post
title: 豆定義存儲例外
translated: true
---

根據你提供的錯誤，你在 IBM WebSphere 上運行的具有 OSGi 支持的 Java 應用程序在初始化 Spring Framework 應用程序上下文時遇到 `BeanDefinitionStoreException`。這個異常表示「無效的 bean 定義」，這通常源於 Spring 設置中的錯誤配置。以下是一個全面的指南來排查和修復問題。

---

## 了解問題
錯誤顯示：
- **異常**：`org.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition`
- **關鍵組件**：堆疊跡中提到 `PlaceholderConfigurerSupport`、`PropertySourcesPlaceholderConfigurer` 和 `AbstractApplicationContext`。
- **上下文**：失敗發生在 Spring 應用程序上下文的 `refresh` 過程中，由 `ContextLoader` 在 WebSphere 的 Web 應用程序環境中觸發。
- **根本原因**：可能與未解析的屬性占位符、無效的 bean 定義或 WebSphere/OSGi 環境中的部署特定問題有關。

這表明 Spring 由於配置錯誤無法正確定義或初始化一個或多個 bean。讓我們逐步解決這個問題。

---

## 逐步修復

### 1. 驗證屬性占位符
**為什麼**：堆疊跡突出顯示 `PlaceholderConfigurerSupport` 和 `PropertySourcesPlaceholderConfigurer`，它們處理屬性解析。如果 bean 定義使用占位符（例如 `${admin.email}`）且未定義，Spring 將失敗。

**如何修復**：
- **定位屬性文件**：確保你的 `application.properties` 或 `application.yml` 文件在類路徑中（例如 `src/main/resources`）。
- **檢查屬性**：打開文件並確認所有在 bean 定義中引用的占位符都已定義。例如：
  ```properties
  admin.email=admin@example.com
  ```
- **修正拼寫錯誤**：查找屬性名稱或文件路徑中的拼寫錯誤。
- **配置設置**：
  - **XML**：如果使用 XML，驗證 `<context:property-placeholder>` 標籤：
    ```xml
    <context:property-placeholder location="classpath:application.properties"/>
    ```
  - **Java 配置**：如果使用 `@Configuration`，確保 `PropertySourcesPlaceholderConfigurer` 已配置：
    ```java
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
    ```

### 2. 檢查 Bean 定義
**為什麼**：「無效的 bean 定義」消息指向 Spring 配置中 bean 定義的問題。

**如何修復**：
- **XML 配置**：
  - 打開你的 Spring XML 文件（例如 `applicationContext.xml`）並檢查：
    - Bean ID 和類名是正確的並存在於類路徑中。
    - 屬性是有效的並與 setter 方法或構造函數參數匹配。
    - 正確的 bean 示例：
      ```xml
      <bean id="myBean" class="com.example.MyClass">
          <property name="email" value="${admin.email}"/>
      </bean>
      ```
  - 使用 IDE 驗證 XML 語法和模式。
- **Java 配置**：
  - 檢查 `@Configuration` 類中的 `@Bean` 方法：
    ```java
    @Bean
    public MyClass myBean() {
        MyClass bean = new MyClass();
        bean.setEmail(env.getProperty("admin.email"));
        return bean;
    }
    ```
  - 確保返回類型和方法名有效。
- **組件掃描**：
  - 如果使用 `@Component`、`@Service` 等，確認基礎包已掃描：
    ```java
    @ComponentScan("com.example")
    ```

### 3. 解決循環依賴
**為什麼**：如果兩個 bean 相互依賴（例如 Bean A 需要 Bean B，Bean B 需要 Bean A），Spring 可能無法初始化它們。

**如何修復**：
- **使用 `@Lazy`**：
  - 使用 `@Lazy` 註釋一個依賴以延遲其初始化：
    ```java
    @Autowired
    @Lazy
    private BeanB beanB;
    ```
- **重構**：如果可能，重新設計你的 bean 以避免循環引用。

### 4. 檢查依賴和類路徑
**為什麼**：缺失或不兼容的庫可能導致 bean 定義中引用的類不可用。

**如何修復**：
- **Maven/Gradle**：
  - 確保所有必需的 Spring 依賴項在你的 `pom.xml`（Maven）或 `build.gradle`（Gradle）中。Maven 示例：
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - 運行 `mvn dependency:tree` 或 `gradle dependencies` 以檢查衝突。
- **類路徑**：確認所有類（例如 `com.example.MyClass`）已編譯並在部署的應用程序中可用。

### 5. 啟用調試日誌
**為什麼**：更詳細的日誌可以確定導致失敗的具體 bean 或屬性。

**如何修復**：
- 添加到 `application.properties`：
  ```properties
  logging.level.org.springframework=DEBUG
  ```
- 重新啟動應用程序並檢查日誌以獲取有關 bean 創建或屬性解析的具體錯誤。

### 6. 驗證 WebSphere/OSGi 配置
**為什麼**：堆疊跡顯示 WebSphere 和 OSGi 組件，這可能引入部署特定的問題。

**如何修復**：
- **束解析**：確保所有 OSGi 束已正確部署並其依賴項在 WebSphere 中解析。
- **類路徑**：驗證 WebSphere 的類加載器包括你的應用程序的 JAR 和屬性文件。
- **伺服器日誌**：檢查 WebSphere 日誌（例如 `SystemOut.log`）以獲取其他錯誤或警告。

### 7. 審查早期日誌
**為什麼**：日誌片段從 10:15:57 開始成功加載屬性，但錯誤發生在 16:56:57。早期問題可能觸發了失敗。

**如何修復**：
- 在日誌文件中向上滾動或檢查存檔日誌以獲取 `BeanDefinitionStoreException` 之前的警告或錯誤。

---

## 常見情況和解決方案
- **未解析的占位符**：
  - **問題**：bean 定義中的 `${admin.email}`，但在 `application.properties` 中。
  - **修復**：將 `admin.email=somevalue` 添加到文件中。
- **缺失類**：
  - **問題**：`<bean class="com.example.NonExistentClass">`
  - **修復**：更正類名或添加缺失的依賴項。
- **語法錯誤**：
  - **問題**：格式不正確的 XML 或 Java 配置。
  - **修復**：使用 IDE 或工具（例如 `xmllint`）驗證 XML。

---

## 最後步驟
1. **應用修復**：從屬性占位符和 bean 定義開始，因為根據堆疊跡它們是最有可能的罪魁禍首。
2. **本地測試**：重新部署並在開發環境中測試。
3. **部署到 WebSphere**：如果本地工作，重新部署到 WebSphere 並監控日誌。
4. **迭代**：如果錯誤持續，使用調試日誌縮小範圍以確定失敗的 bean 或屬性。

通過遵循這些步驟，你應該能夠解決 `BeanDefinitionStoreException` 並成功初始化 Spring 應用程序上下文。如果問題仍然存在，分享更具體的詳細信息（例如配置文件或完整日誌）以獲取進一步的幫助。