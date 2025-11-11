---
audio: false
generated: true
lang: hant
layout: post
title: Bean 的 XML 配置檔案
translated: true
type: note
---

針對您關於 beans XML 運作原理的疑問，包括帶有 props 和 keys 的 bean 屬性、哪些類別會使用這些 XML 檔案，以及它們如何被載入，我們將清晰且有系統地進行解析。此說明假設使用 Spring 這類框架的情境，其中 "beans XML" 是配置 bean 的常用術語。

### Beans XML 的運作原理？

在 Spring 這類框架中，**beans XML 檔案**是一個用於定義和管理稱為 *bean* 的物件的配置檔案。這些 bean 通常是 Spring 框架實例化、配置和管理的 Java 物件。XML 檔案指定了：

- **Beans**：每個 bean 使用 `<bean>` 標籤定義，其中包括 `id`（唯一識別碼）和 `class`（要實例化的 Java 類別的完整限定名稱）。
- **Properties**：Bean 可以擁有屬性，這些是設定到 bean 中以配置其行為的值或參考。屬性使用 `<property>` 標籤定義。
- **Props 和 Keys**：在 `<property>` 標籤內，您可以使用 `<props>` 元素來定義一組鍵值對。當 bean 需要 `java.util.Properties` 物件或類似結構（如 `Map`）時，這非常有用。`<props>` 元素包含多個 `<prop>` 標籤，每個標籤都有一個 `key` 屬性和對應的值。

以下是在 beans XML 檔案中的範例：

```xml
<bean id="myBean" class="com.example.MyBean">
    <property name="someProperty">
        <props>
            <prop key="key1">value1</prop>
            <prop key="key2">value2</prop>
        </props>
    </property>
</bean>
```

在此範例中：
- 一個 ID 為 `myBean` 的 bean 由類別 `com.example.MyBean` 創建。
- 該 bean 有一個名為 `someProperty` 的屬性。
- `<props>` 元素定義了一組鍵值對（`key1=value1` 和 `key2=value2`），Spring 會將其轉換為 `Properties` 物件，並透過 setter 方法（例如 `setSomeProperty(Properties props)`）注入到 `myBean` 中。

您查詢中的 "it puts in resources" 說法有點不明確，但它可能指的是 XML 檔案作為應用程式使用的*資源*（位於應用程式的 classpath 或檔案系統中的檔案），或者可能意味著 XML 中定義的 bean（如資料來源）代表了應用程式使用的資源。目前，我們假設它是關於 XML 檔案本身作為應用程式載入的資源。

### 哪些類別會使用這些 XML 檔案？

在 Spring 中，負責使用（即載入和處理）beans XML 檔案的類別是 **`ApplicationContext`**。更精確地說，它是 `ApplicationContext` 介面的實現，例如：

- **`ClassPathXmlApplicationContext`**：從 classpath 載入 XML 檔案。
- **`FileSystemXmlApplicationContext`**：從檔案系統載入 XML 檔案。

`ApplicationContext` 是 Spring 用於向應用程式提供配置資訊的核心介面。它讀取 beans XML 檔案，進行解析，並使用其中的定義來創建和管理 bean。雖然 bean 本身（例如 `com.example.MyBean`）使用 XML 中定義的屬性，但 `ApplicationContext` 是直接處理 XML 檔案以實現此目的的類別。

### 它將如何被載入？

beans XML 檔案通過創建 `ApplicationContext` 實現的實例並指定 XML 檔案的位置來載入到應用程式中。以下是其逐步運作方式：

1. **指定 XML 檔案位置**：當您實例化 `ApplicationContext` 時，您需要提供 XML 檔案的名稱或路徑。例如：
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   這裡，`"beans.xml"` 被假定位於 classpath 中（例如，在典型的 Java 專案中位於 `src/main/resources` 目錄）。

2. **作為資源載入**：`ApplicationContext` 使用 `ResourceLoader` 來定位並將 XML 檔案作為 `Resource` 載入。在此情況下，`ClassPathXmlApplicationContext` 會在 classpath 中尋找該檔案。

3. **解析 XML**：Spring 內部使用 `XmlBeanDefinitionReader` 來解析 XML 檔案。該讀取器解釋 `<bean>` 標籤、屬性和 `<props>` 元素，創建描述每個 bean 應如何構建的 `BeanDefinition` 物件。

4. **Bean 創建**：`ApplicationContext`（它擴展了 Spring 的 `BeanFactory`）使用這些 bean 定義來實例化 bean、設定它們的屬性（包括從 `<props>` 注入 `Properties` 物件）並管理它們的生命週期。

載入後，您可以像這樣從 `ApplicationContext` 中檢索 bean：
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### 整體總結

- **Beans XML 的運作原理**：XML 定義了 bean 及其屬性，包括透過 `<props>` 設定的鍵值對。Spring 解析此 XML 以配置和實例化 bean。
- **使用 XML 的類別**：`ApplicationContext`（例如 `ClassPathXmlApplicationContext`）使用 XML 檔案來設定應用程式。
- **載入方式**：當您創建 `ApplicationContext` 實例並指定檔案位置時，XML 會從 classpath 或檔案系統作為資源載入。

例如，如果您的 `beans.xml` 位於 classpath 中，您將透過以下方式載入它：
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
然後 Spring 會處理其餘工作，使配置的 bean 可供您的應用程式使用。

這種機制強大且靈活，允許您在 XML 中定義複雜的配置，Spring 在運行時將其實現。