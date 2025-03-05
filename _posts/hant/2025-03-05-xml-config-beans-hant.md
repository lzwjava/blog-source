---
audio: true
generated: true
lang: hant
layout: post
title: XML 配置檔案 For Beans
translated: true
---

關於如何使用 beans XML，包括 bean 屬性、 props 和 keys，以及哪個類別使用這些 XML 文件以及它們如何加載，讓我們清晰且系統地分解這些問題。這個解釋假設在 Spring 這樣的框架中，"beans XML" 是配置 beans 的常見術語。

### Beans XML 如何運作？

在像 Spring 這樣的框架中，**beans XML 文件** 是一個用來定義和管理稱為 *beans* 的物件的配置文件。這些 beans 通常是 Spring 框架實例化、配置和管理的 Java 物件。XML 文件指定：

- **Beans**：每個 bean 使用 `<bean>` 標籤定義，包括一個 `id`（唯一識別碼）和一個 `class`（要實例化的 Java 類的完全限定名稱）。
- **屬性**：Beans 可以有屬性，這些屬性是設置到 bean 中的值或引用，用來配置其行為。屬性使用 `<property>` 標籤定義。
- **Props 和 Keys**：在 `<property>` 標籤中，可以使用 `<props>` 元素來定義一組鍵值對。這在 bean 期望 `java.util.Properties` 物件或類似結構（如 `Map`）時非常有用。`<props>` 元素包含多個 `<prop>` 標籤，每個標籤都有一個 `key` 屬性和相應的值。

以下是 beans XML 文件中的一個範例：

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

在這個範例中：
- 從類 `com.example.MyBean` 創建一個 ID 為 `myBean` 的 bean。
- 該 bean 有一個名為 `someProperty` 的屬性。
- `<props>` 元素定義了一組鍵值對（`key1=value1` 和 `key2=value2`），Spring 將這些轉換為 `Properties` 物件並通過設置方法（如 `setSomeProperty(Properties props)`）注入到 `myBean` 中。

你的查詢中提到的「它把資源放進去」這個短語有點不明確，但它可能指的是 XML 文件是應用程序使用的 *資源*（應用程序的類路徑或文件系統中的文件），或者它可能指的是 XML 中定義的 beans（如數據源）代表應用程序使用的資源。目前，讓我們假設它指的是 XML 文件本身作為應用程序加載的資源。

### 使用這些 XML 文件的類別是什麼？

在 Spring 中，負責使用（即加載和處理）beans XML 文件的類別是 **`ApplicationContext`**。更具體地說，它是 `ApplicationContext` 接口的實現，例如：

- **`ClassPathXmlApplicationContext`**：從類路徑加載 XML 文件。
- **`FileSystemXmlApplicationContext`**：從文件系統加載 XML 文件。

`ApplicationContext` 是 Spring 提供配置信息給應用程序的中央接口。它讀取 beans XML 文件，解析它，並使用定義來創建和管理 beans。雖然 beans 本身（例如 `com.example.MyBean`）使用 XML 中定義的屬性，但 `ApplicationContext` 是直接處理 XML 文件以實現這一點的類別。

### 它將如何加載？

beans XML 文件通過創建 `ApplicationContext` 實現的實例並指定 XML 文件的位置來加載到應用程序中。以下是步驟：

1. **指定 XML 文件位置**：當你實例化 `ApplicationContext` 時，提供 XML 文件的名稱或路徑。例如：
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   這裡，`"beans.xml"` 假設在類路徑中（例如在典型的 Java 專案中的 `src/main/resources` 目錄中）。

2. **加載作為資源**：`ApplicationContext` 使用 `ResourceLoader` 來定位和加載 XML 文件作為 `Resource`。在這種情況下，`ClassPathXmlApplicationContext` 在類路徑中查找文件。

3. **解析 XML**：在內部，Spring 使用 `XmlBeanDefinitionReader` 來解析 XML 文件。這個讀取器解釋 `<bean>` 標籤、屬性和 `<props>` 元素，創建描述每個 bean 如何構建的 `BeanDefinition` 物件。

4. **Bean 創建**：`ApplicationContext`（它擴展了 Spring 的 `BeanFactory`）使用這些 bean 定義來實例化 beans，設置它們的屬性（包括從 `<props>` 注入 `Properties` 物件），並管理它們的生命週期。

加載後，可以從 `ApplicationContext` 中檢索 beans，例如：
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### 總結

- **Beans XML 如何運作**：XML 定義 beans 和它們的屬性，包括通過 `<props>` 的鍵值對。Spring 解析這個 XML 來配置和實例化 beans。
- **使用 XML 的類別**：`ApplicationContext`（例如 `ClassPathXmlApplicationContext`）使用 XML 文件來設置應用程序。
- **如何加載**：當你創建 `ApplicationContext` 實例並指定文件位置時，XML 文件從類路徑或文件系統加載作為資源。

例如，如果你的 `beans.xml` 在類路徑中，可以這樣加載：
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Spring 會處理其餘部分，使配置的 beans 可用於你的應用程序。

這種機制強大且靈活，允許你在 XML 中定義複雜配置，Spring 在運行時將其實現。