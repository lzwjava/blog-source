---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的反射
translated: true
type: note
---

### 重點摘要
- 似乎 `java.lang.reflect` 在 Java 中用於反射機制，允許程式在運行時檢查和修改其結構。
- 研究表明，關鍵類別包括 `Class`、`Method`、`Field` 和 `Constructor`，用於檢查和操作類別組件。
- 證據顯示常見用途包括動態方法調用、存取私有欄位，以及創建通用框架。

### 什麼是 `java.lang.reflect`？
`java.lang.reflect` 是 Java 中的一個套件，它實現了反射功能，此特性允許程式在運行時檢查或修改自身的結構和行為。這意味著您可以動態地檢查類別、方法、欄位，甚至調用它們，而無需在編譯時預先知道這些資訊。

### 如何使用
要使用 `java.lang.reflect`，首先需要獲取一個 `Class` 物件，該物件代表您要檢查的類別。您可以通過三種方式實現：
- 如果您在編譯時知道類別，請使用 `MyClass.class`。
- 在物件實例上調用 `instance.getClass()`。
- 使用 `Class.forName("package.ClassName")` 進行動態載入，但這可能會拋出 `ClassNotFoundException`。

獲取 `Class` 物件後，您可以：
- 使用 `getMethods()` 獲取公共方法，或使用 `getDeclaredMethods()` 獲取所有方法（包括私有方法）。
- 使用 `getFields()` 存取公共欄位，或使用 `getDeclaredFields()` 存取所有欄位，並使用 `setAccessible(true)` 來存取私有欄位。
- 使用 `getConstructors()` 處理建構函數，並使用 `newInstance()` 創建實例。

例如，要調用私有方法：
- 獲取 `Method` 物件，使用 `setAccessible(true)` 設置為可存取，然後使用 `invoke()` 調用該方法。

### 意外細節
一個意想不到的方面是，反射可能通過繞過存取修飾符來影響安全性，因此在生產程式碼中應謹慎使用 `setAccessible(true)`。

---

### 調查筆記：使用 `java.lang.reflect` 的全面指南

本筆記基於對現有資源的廣泛分析，深入探討了 Java 中 `java.lang.reflect` 套件的功能、用法及其影響。反射是 Java 中的一項強大功能，允許程式在運行時檢查和修改其結構，對於動態編程場景尤其有價值。

#### Java 反射簡介

反射是 Java 編程語言中的一項功能，允許正在執行的程式檢查或「內省」自身，並操作內部屬性。這種能力在 Pascal、C 或 C++ 等語言中並不常見，使得 Java 的反射成為一種獨特而強大的工具。例如，它允許 Java 類別獲取其所有成員的名稱並顯示它們，這在 JavaBeans 等場景中非常有用，其中軟體組件可以通過建構工具使用反射來動態載入和檢查類別屬性 ([使用 Java 反射](https://www.oracle.com/technical-resources/articles/java/javareflection.html))。

`java.lang.reflect` 套件提供了實現反射所需的類別和接口，支援如調試器、解釋器、物件檢查器、類別瀏覽器等應用程式，以及物件序列化和 JavaBeans 等服務。該套件與 `java.lang.Class` 一起，便於根據目標物件的運行時類別或給定類別聲明的成員來存取公共成員，並在擁有必要的 `ReflectPermission` 權限時，可以抑制預設的反射存取控制 ([java.lang.reflect (Java Platform SE 8)](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html))。

#### 關鍵類別及其角色

`java.lang.reflect` 套件包含幾個關鍵類別，每個類別在反射中都有特定用途：

- **Class**：代表 Java 虛擬機（JVM）中的類別或接口。它是反射操作的入口點，提供了檢查運行時屬性（包括成員和類型資訊）的方法。對於每種類型的物件，JVM 都會實例化一個不可變的 `java.lang.Class` 實例，這對於創建新類別和物件至關重要 ([課程：類別 (The Java™ Tutorials > The Reflection API)](https://docs.oracle.com/javase/tutorial/reflect/class/index.html))。

- **Method**：代表類別的方法，允許動態調用和檢查。它提供了 `getName()`、`getParameterTypes()` 和 `invoke()` 等方法，使程式能夠在運行時調用方法，甚至在設置可存取性後調用私有方法 ([Java 反射指南 | Baeldung](https://www.baeldung.com/java-reflection))。

- **Field**：代表類別的欄位（成員變數），便於動態獲取或設置值。它包括 `getName()`、`getType()`、`get()` 和 `set()` 等方法，並能夠使用 `setAccessible(true)` 存取私有欄位 ([Java 反射範例教程 | DigitalOcean](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial))。

- **Constructor**：代表類別的建構函數，允許動態創建新實例。它提供了 `getParameterTypes()` 和 `newInstance()` 等方法，對於使用特定建構函數參數實例化物件非常有用 ([Java 中的反射 - GeeksforGeeks](https://www.geeksforgeeks.org/reflection-in-java/))。

- **AccessibleObject**：是 `Field`、`Method` 和 `Constructor` 的基礎類別，提供了 `setAccessible()` 方法來覆蓋存取控制檢查，這對於存取私有成員至關重要，但由於安全影響需要謹慎處理 ([java.lang.reflect (Java SE 19 & JDK 19 [build 1])](https://download.java.net/java/early_access/panama/docs/api/java.base/java/lang/reflect/package-summary.html))。

#### 實際用法與範例

要使用 `java.lang.reflect`，第一步是獲取一個 `Class` 物件，可以通過三種方式實現：

1. **使用 `.class` 語法**：直接引用類別，例如 `Class<?> cls1 = String.class`。
2. **使用 `getClass()` 方法**：在實例上調用，例如 `String str = "hello"; Class<?> cls2 = str.getClass()`。
3. **使用 `Class.forName()`**：通過名稱動態載入，例如 `Class<?> cls3 = Class.forName("java.lang.String")`，請注意這可能會拋出 `ClassNotFoundException` ([軌跡：反射 API (The Java™ Tutorials)](https://docs.oracle.com/javase/tutorial/reflect/index.html))。

獲取 `Class` 物件後，可以檢查各種類別屬性：

- `getName()` 返回完整限定名稱。
- `getSuperclass()` 檢索父類別。
- `getInterfaces()` 列出實現的接口。
- `isInterface()` 檢查是否為接口。
- `isPrimitive()` 判斷是否為基本類型。

##### 操作方法

可以使用以下方式檢索方法：
- `getMethods()` 用於所有公共方法，包括繼承的方法。
- `getDeclaredMethods()` 用於類別中聲明的所有方法，包括私有方法。

要調用方法，請使用 `Method` 物件的 `invoke()` 方法。例如，調用公共方法：
```java
Method method = cls.getMethod("toString");
String result = (String) method.invoke(str);
```
對於私有方法，首先設置可存取性：
```java
Method privateMethod = cls.getDeclaredMethod("privateMethod");
privateMethod.setAccessible(true);
privateMethod.invoke(obj);
```
這種方法對於動態方法調用非常有用，特別是在方法名稱在運行時確定的框架中 ([調用方法 (The Java™ Tutorials > The Reflection API > Members)](https://docs.oracle.com/javase/tutorial/reflect/member/methodInvocation.html))。

##### 操作欄位

欄位的存取方式類似：
- `getFields()` 用於公共欄位，包括繼承的欄位。
- `getDeclaredFields()` 用於所有聲明的欄位。

要獲取或設置欄位值：
```java
Field field = cls.getDeclaredField("x");
field.setAccessible(true);
int value = (int) field.get(obj);
field.set(obj, 10);
```
這在需要檢查所有物件欄位的調試或日誌記錄中特別有用 ([Java 反射（附範例）](https://www.programiz.com/java-programming/reflection))。

##### 操作建構函數

可以使用以下方式檢索建構函數：
- `getConstructors()` 用於公共建構函數。
- `getDeclaredConstructors()` 用於所有建構函數。

要創建實例：
```java
Constructor<?> constructor = cls.getConstructor(int.class, String.class);
Object obj = constructor.newInstance(10, "hello");
```
這對於動態物件創建至關重要，例如在依賴注入框架中 ([Java 反射 - javatpoint](https://www.javatpoint.com/java-reflection))。

#### 處理存取控制與安全性

預設情況下，反射會尊重存取修飾符（public、private、protected）。要存取私有成員，請在相應的物件（例如 `Field`、`Method`、`Constructor`）上使用 `setAccessible(true)`。然而，這可能通過繞過封裝來帶來安全風險，因此建議僅在必要時使用，並確保擁有適當的權限，例如 `ReflectPermission` ([java - 什麼是反射？為什麼它有用？ - Stack Overflow](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful))。

#### 使用案例與實際應用

反射常用於：
- **通用框架**：創建可與任何類別協作的函式庫，例如 Spring 或 Hibernate。
- **序列化/反序列化**：將物件轉換為流或從流轉換為物件，例如在 Java 的物件序列化中。
- **測試框架**：動態調用方法，如在 JUnit 中所見。
- **工具開發**：構建檢查類別結構的調試器、IDE 和類別瀏覽器。

例如，假設您有一個類別名稱列表，並希望創建實例並調用方法：
```java
List<String> classNames = Arrays.asList("com.example.ClassA", "com.example.ClassB");
for (String className : classNames) {
    Class<?> cls = Class.forName(className);
    Object obj = cls.newInstance();
    Method method = cls.getMethod("doSomething");
    method.invoke(obj);
}
```
這展示了動態類別載入和方法調用，是運行時適應性的強大功能 ([Java 反射 API 的增強功能](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html))。

另一個實際範例是通用日誌記錄機制：
```java
void printObjectFields(Object obj) {
    Class<?> cls = obj.getClass();
    Field[] fields = cls.getDeclaredFields();
    for (Field field : fields) {
        field.setAccessible(true);
        System.out.println(field.getName() + ": " + field.get(obj));
    }
}
```
這可用於調試，打印任何物件的所有欄位，展示了反射在檢查任務中的實用性 ([Java 中的反射 - GeeksforGeeks](https://www.geeksforgeeks.org/reflection-in-java/))。

#### 潛在陷阱與最佳實踐

儘管功能強大，反射有幾個需要注意的事項：

1. **效能**：反射操作（如 `Method.invoke()` 或 `Constructor.newInstance()`）通常比直接調用慢，因為涉及動態查找和檢查，正如 Java SE 8 中的效能增強所述 ([Java 反射 API 的增強功能](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html))。

2. **安全性**：允許任意存取私有成員可能損害封裝和安全性，因此應謹慎使用 `setAccessible(true)`，特別是在生產程式碼中，並隔離反射使用以最小化風險 ([java - 什麼是反射？為什麼它有用？ - Stack Overflow](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful))。

3. **類型安全**：反射通常涉及處理泛型 `Object` 類型，如果不當處理，會增加 `ClassCastException` 的風險，需要仔細的轉型和類型檢查 ([Java 反射範例教程 | DigitalOcean](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial))。

4. **異常處理**：許多反射方法可能拋出異常，如 `NoSuchMethodException`、`IllegalAccessException` 或 `InvocationTargetException`，需要穩健的異常處理以確保程式穩定性 ([軌跡：反射 API (The Java™ Tutorials)](https://docs.oracle.com/javase/tutorial/reflect/index.html))。

最佳實踐包括：
- 僅在必要時使用反射，在可能的情況下優先使用靜態類型。
- 最小化 `setAccessible(true)` 的使用以維護封裝。
- 通過適當的轉型和驗證確保類型安全。
- 優雅地處理異常以防止運行時失敗。

#### 反射方法的比較分析

為了組織各種存取類別組件的方法，請考慮以下比較關鍵反射操作的表格：

| 操作                  | 公共存取方法       | 所有存取方法          | 備註                                      |
|-----------------------|-------------------|----------------------|------------------------------------------|
| 獲取方法              | `getMethods()`    | `getDeclaredMethods()` | 公共方法包括繼承的，所有方法包括聲明的 |
| 獲取欄位              | `getFields()`     | `getDeclaredFields()`  | 公共欄位包括繼承的，所有欄位包括私有的 |
| 獲取建構函數          | `getConstructors()` | `getDeclaredConstructors()` | 僅公共建構函數，所有包括私有的 |
| 調用方法              | `invoke()` 後 `getMethod()` | `invoke()` 後 `getDeclaredMethod()` | 對於私有方法需要 `setAccessible(true)` |
| 存取欄位              | `get()`/`set()` 後 `getField()` | `get()`/`set()` 後 `getDeclaredField()` | 對於私有欄位需要 `setAccessible(true)` |

此表格突出了公共方法和所有存取方法之間的區別，對於理解反射的範圍和安全影響至關重要 ([java.lang.reflect.Method 類別在 Java 中 - GeeksforGeeks](https://www.geeksforgeeks.org/java-lang-reflect-method-class-in-java/))。

#### 結論

`java.lang.reflect` 套件是 Java 中動態編程的基石，提供了在運行時檢查和操作類別結構的強大能力。通過理解其關鍵類別、實際用法和最佳實踐，開發人員可以利用反射實現強大的應用，同時減輕其潛在的陷阱。本全面指南基於權威來源，確保了無論是新手還是有經驗的 Java 程式設計師都能獲得深入的理解。

**主要引用來源：**
- [使用 Java 反射介紹與範例](https://www.oracle.com/technical-resources/articles/java/javareflection.html)
- [Java 反射指南與詳細範例](https://www.baeldung.com/java-reflection)
- [Java 中的反射全面教程](https://www.geeksforgeeks.org/reflection-in-java/)
- [Java 反射範例教程（適合初學者）](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial)
- [Java 反射詳細指南與範例](https://www.javatpoint.com/java-reflection)
- [什麼是反射？為什麼它在 Java 中有用？](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)
- [java.lang.reflect.Method 類別在 Java 中詳細介紹](https://www.geeksforgeeks.org/java-lang-reflect-method-class-in-java/)
- [Java 反射與實際範例](https://www.programiz.com/java-programming/reflection)
- [java.lang.reflect 套件摘要 Java SE 8](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html)
- [java.lang.reflect 套件摘要 Java SE 19](https://download.java.net/java/early_access/panama/docs/api/java.base/java/lang/reflect/package-summary.html)
- [核心 Java 反射官方文檔](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/index.html)
- [軌跡：反射 API Java 教程](https://docs.oracle.com/javase/tutorial/reflect/index.html)
- [軌跡：反射 API Java 教程詳細版](https://docs.oracle.com/javase/tutorial/reflect/)
- [Java 反射 API 的增強功能](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html)
- [課程：類別 - 反射 API Java 教程](https://docs.oracle.com/javase/tutorial/reflect/class/index.html)
- [調用方法 - 反射 API Java 教程](https://docs.oracle.com/javase/tutorial/reflect/member/methodInvocation.html)