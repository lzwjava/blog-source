---
audio: false
generated: true
lang: hant
layout: post
title: Java 語言特性
translated: true
type: note
---

以下是對**最常用 Java 語言功能**的詳細擴充說明，旨在讓您深入理解每個概念。我將解釋每個功能是什麼、為何重要、如何在實際編程中應用，並包含實用範例來說明其用法。本回答建立在基礎概念之上，並透過額外背景、細微差別和應用場景增添更多深度。

---

## 1. **類別 (Classes)**
- **定義**：類別是 Java 的基本建構塊，作為創建物件的模板或藍圖。它封裝了定義物件屬性和行為的資料（欄位）與行為（方法）。
- **重要性**：類別是 Java 物件導向編程（OOP）範式的基石。它們促進封裝（捆綁資料和方法）、抽象（隱藏實現細節）和模組化，使程式碼可重複使用且易於維護。
- **應用方式**：類別用於模擬程式中的實體，例如 `Person`、`Vehicle` 或 `BankAccount`。它們可以包含構造函數、帶有存取修飾符（`public`、`private`）的欄位，以及用於操作物件狀態的方法。
- **深入探討**：
  - 類別可以嵌套（內部類別）或抽象（不能直接實例化）。
  - 它們支援繼承，允許一個類別擴展另一個類別並繼承其屬性和方法。
- **範例**：
  ```java
  public class Student {
      private String name;  // 實例欄位
      private int age;
      
      // 構造函數
      public Student(String name, int age) {
          this.name = name;
          this.age = age;
      }
      
      // 方法
      public void displayInfo() {
          System.out.println("Name: " + name + ", Age: " + age);
      }
  }
  ```
- **實際應用**：`Student` 類別可以是學校管理系統的一部分，具有計算成績或追蹤出勤的方法。

---

## 2. **物件 (Objects)**
- **定義**：物件是類別的實例，使用 `new` 關鍵字創建。它代表類別藍圖的具體實現，擁有自己的狀態。
- **重要性**：物件使類別變得生動，允許具有獨特資料的多個實例。它們透過代表現實世界實體來實現複雜系統的建模。
- **應用方式**：物件透過其方法和欄位進行實例化和操作。例如，`Student student1 = new Student("Alice", 20);` 創建一個 `Student` 物件。
- **深入探討**：
  - 物件儲存在堆記憶體中，對它們的引用儲存在變數中。
  - Java 對物件使用傳引用，意味著對物件狀態的更改會在所有引用中反映。
- **範例**：
  ```java
  Student student1 = new Student("Alice", 20);
  student1.displayInfo();  // 輸出：Name: Alice, Age: 20
  ```
- **實際應用**：在電子商務系統中，像 `Order` 或 `Product` 這樣的物件代表個別購買或銷售項目。

---

## 3. **方法 (Methods)**
- **定義**：方法是類別中的程式碼塊，定義物件的行為。它們可以接受參數、返回值或執行操作。
- **重要性**：方法封裝邏輯、減少冗餘並提高程式碼可讀性。它們是與物件狀態互動的主要方式。
- **應用方式**：方法在物件上或靜態地在類別上調用。每個 Java 應用程式都從 `public static void main(String[] args)` 方法開始。
- **深入探討**：
  - 方法可以重載（相同名稱，不同參數）或覆寫（在子類別中重新定義）。
  - 它們可以是 `static`（類別層級）或基於實例（物件層級）。
- **範例**：
  ```java
  public class MathUtils {
      public int add(int a, int b) {
          return a + b;
      }
      
      public double add(double a, double b) {  // 方法重載
          return a + b;
      }
  }
  // 用法
  MathUtils utils = new MathUtils();
  System.out.println(utils.add(5, 3));      // 輸出：8
  System.out.println(utils.add(5.5, 3.2));  // 輸出：8.7
  ```
- **實際應用**：`BankAccount` 類別中的 `withdraw` 方法可以更新帳戶餘額並記錄交易。

---

## 4. **變數 (Variables)**
- **定義**：變數儲存資料值，必須以特定類型（例如 `int`、`String`、`double`）宣告。
- **重要性**：變數是程式資料的記憶體佔位符，實現狀態管理和計算。
- **應用方式**：Java 有幾種變數類型：
  - **局部變數**：在方法內部宣告，作用域限於該方法。
  - **實例變數**：在類別中宣告，與每個物件綁定。
  - **靜態變數**：使用 `static` 宣告，在類別的所有實例間共享。
- **深入探討**：
  - 變數有預設值（例如 `int` 為 `0`，物件為 `null`）如果未初始化（僅適用於實例/靜態變數）。
  - Java 強制執行強類型，防止不相容的賦值而不進行顯式轉換。
- **範例**：
  ```java
  public class Counter {
      static int totalCount = 0;  // 靜態變數
      int instanceCount;          // 實例變數
      
      public void increment() {
          int localCount = 1;     // 局部變數
          instanceCount += localCount;
          totalCount += localCount;
      }
  }
  ```
- **實際應用**：追蹤登入用戶數量（靜態）與個別會話時間（實例）。

---

## 5. **控制流程語句 (Control Flow Statements)**
- **定義**：控制流程語句決定程式的執行路徑，包括條件語句（`if`、`else`、`switch`）和循環（`for`、`while`、`do-while`）。
- **重要性**：它們實現決策和重複，對於實施複雜邏輯至關重要。
- **應用方式**：
  - **條件語句**：基於布林條件執行程式碼。
  - **循環**：遍歷資料或重複操作直到條件滿足。
- **深入探討**：
  - `switch` 語句支援 `String`（自 Java 7 起）和枚舉，除了基本類型。
  - 循環可以嵌套，`break`/`continue` 關鍵字修改其行為。
- **範例**：
  ```java
  int score = 85;
  if (score >= 90) {
      System.out.println("A");
  } else if (score >= 80) {
      System.out.println("B");
  } else {
      System.out.println("C");
  }
  
  for (int i = 0; i < 3; i++) {
      System.out.println("Loop iteration: " + i);
  }
  ```
- **實際應用**：處理訂單列表（`for` 循環）並根據總金額應用折扣（`if`）。

---

## 6. **介面 (Interfaces)**
- **定義**：介面是一個合約，指定實現類別必須定義的方法。它支援抽象和多繼承。
- **重要性**：介面實現鬆散耦合和多態，允許不同類別共享共同的 API。
- **應用方式**：類別使用 `implements` 關鍵字實現介面。自 Java 8 起，介面可以包含帶有實現的默認和靜態方法。
- **深入探討**：
  - 默認方法允許介面向後兼容的演進。
  - 函數式介面（帶有一個抽象方法）是 lambda 表達式的關鍵。
- **範例**：
  ```java
  public interface Vehicle {
      void start();
      default void stop() {  // 默認方法
          System.out.println("Vehicle stopped");
      }
  }
  
  public class Bike implements Vehicle {
      public void start() {
          System.out.println("Bike started");
      }
  }
  // 用法
  Bike bike = new Bike();
  bike.start();  // 輸出：Bike started
  bike.stop();   // 輸出：Vehicle stopped
  ```
- **實際應用**：支付網關系統中 `CreditCard` 和 `PayPal` 類別的 `Payment` 介面。

---

## 7. **異常處理 (Exception Handling)**
- **定義**：異常處理使用 `try`、`catch`、`finally`、`throw` 和 `throws` 來管理運行時錯誤。
- **重要性**：它通過防止崩潰並允許從錯誤（如文件未找到或除以零）中恢復來確保穩健性。
- **應用方式**：風險程式碼放在 `try` 塊中，特定異常在 `catch` 塊中捕獲，`finally` 執行清理程式碼。
- **深入探討**：
  - 異常是源自 `Throwable`（`Error` 或 `Exception`）的物件。
  - 可以通過擴展 `Exception` 創建自定義異常。
- **範例**：
  ```java
  try {
      int[] arr = new int[2];
      arr[5] = 10;  // ArrayIndexOutOfBoundsException
  } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Index out of bounds: " + e.getMessage());
  } finally {
      System.out.println("Cleanup done");
  }
  ```
- **實際應用**：在 Web 應用程式中處理網絡超時。

---

## 8. **泛型 (Generics)**
- **定義**：泛型允許通過將類別、介面和方法參數化為類型來實現類型安全、可重複使用的程式碼。
- **重要性**：它們在編譯時捕獲類型錯誤，減少運行時錯誤並消除轉換的需要。
- **應用方式**：常用於集合（例如 `List<String>`）和自定義泛型類別/方法。
- **深入探討**：
  - 萬用字元（`? extends T`、`? super T`）處理類型變異。
  - 類型擦除在運行時移除泛型類型信息以實現向後兼容。
- **範例**：
  ```java
  public class Box<T> {
      private T content;
      public void set(T content) { this.content = content; }
      public T get() { return content; }
  }
  // 用法
  Box<Integer> intBox = new Box<>();
  intBox.set(42);
  System.out.println(intBox.get());  // 輸出：42
  ```
- **實際應用**：用於鍵值存儲的泛型 `Cache<K, V>` 類別。

---

## 9. **Lambda 表達式 (Lambda Expressions)**
- **定義**：Lambda 表達式（Java 8+）是匿名函數的簡潔表示，通常與函數式介面一起使用。
- **重要性**：它們簡化了事件處理、集合處理和函數式編程的程式碼。
- **應用方式**：與 `Runnable`、`Comparator` 或帶有單個抽象方法的自定義介面配對使用。
- **深入探討**：
  - 語法：`(parameters) -> expression` 或 `(parameters) -> { statements; }`。
  - 它們啟用 Streams API 進行函數式風格的資料處理。
- **範例**：
  ```java
  List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
  names.forEach(name -> System.out.println(name.toUpperCase()));
  ```
- **實際應用**：使用 `Collections.sort(products, (p1, p2) -> p1.getPrice() - p2.getPrice())` 按價格對產品列表進行排序。

---

## 10. **註解 (Annotations)**
- **定義**：註解是應用於程式碼元素的元資料標籤（例如 `@Override`、`@Deprecated`），在編譯時或運行時處理。
- **重要性**：它們向編譯器、框架或工具提供指令，增強自動化並減少樣板程式碼。
- **應用方式**：用於配置（例如 JPA 中的 `@Entity`）、文檔或強制執行規則。
- **深入探討**：
  - 可以使用 `@interface` 定義自定義註解。
  - 保留策略（`SOURCE`、`CLASS`、`RUNTIME`）決定其生命週期。
- **範例**：
  ```java
  public class MyClass {
      @Override
      public String toString() {
          return "Custom string";
      }
      
      @Deprecated
      public void oldMethod() {
          System.out.println("Old way");
      }
  }
  ```
- **實際應用**：Spring 中的 `@Autowired` 用於自動注入依賴項。

---

## 其他核心功能

為了加深您的理解，以下是更多廣泛使用的 Java 功能及其詳細說明：

### 11. **陣列 (Arrays)**
- **定義**：陣列是固定大小、有序的相同類型元素集合。
- **重要性**：它們提供了一種簡單、高效的方式來存儲和存取多個值。
- **應用方式**：宣告為 `type[] name = new type[size];` 或直接初始化。
- **範例**：
  ```java
  int[] numbers = {1, 2, 3, 4};
  System.out.println(numbers[2]);  // 輸出：3
  ```
- **實際應用**：存儲一週的溫度列表。

### 12. **枚舉 (Enums)**
- **定義**：枚舉定義一組固定的命名常量，通常帶有關聯值或方法。
- **重要性**：它們比原始常量提高了類型安全性和可讀性。
- **應用方式**：用於預定義類別，如日期、狀態或狀態碼。
- **範例**：
  ```java
  public enum Status {
      PENDING("In progress"), APPROVED("Done"), REJECTED("Failed");
      private String desc;
      Status(String desc) { this.desc = desc; }
      public String getDesc() { return desc; }
  }
  // 用法
  System.out.println(Status.APPROVED.getDesc());  // 輸出：Done
  ```
- **實際應用**：在電子商務系統中代表訂單狀態。

### 13. **串流 (Streams) (Java 8+)**
- **定義**：串流提供了一種函數式方法來處理集合，支援 `filter`、`map` 和 `reduce` 等操作。
- **重要性**：它們簡化了資料操作，支援並行處理並提高了程式碼表達力。
- **應用方式**：使用 `.stream()` 從集合創建，並與操作鏈接。
- **範例**：
  ```java
  List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);
  int sum = nums.stream()
                .filter(n -> n % 2 == 0)
                .mapToInt(n -> n * 2)
                .sum();
  System.out.println(sum);  // 輸出：12 (2*2 + 4*2)
  ```
- **實際應用**：按地區匯總銷售資料。

### 14. **構造函數 (Constructors)**
- **定義**：構造函數是在創建物件時調用的特殊方法，用於初始化其狀態。
- **重要性**：它們確保物件以有效資料開始並減少初始化錯誤。
- **應用方式**：以與類別相同的名稱定義，可選帶參數。
- **範例**：
  ```java
  public class Book {
      String title;
      public Book(String title) {
          this.title = title;
      }
  }
  ```
- **實際應用**：使用用戶名和密碼初始化 `User` 物件。

### 15. **繼承 (Inheritance)**
- **定義**：繼承允許一個類別（子類別）使用 `extends` 繼承另一個類別（父類別）的欄位和方法。
- **重要性**：它促進程式碼重用並在類別之間建立層次關係。
- **應用方式**：用於創建通用類別的專門版本。
- **範例**：
  ```java
  public class Animal {
      void eat() { System.out.println("Eating"); }
  }
  public class Dog extends Animal {
      void bark() { System.out.println("Barking"); }
  }
  // 用法
  Dog dog = new Dog();
  dog.eat();  // 輸出：Eating
  dog.bark(); // 輸出：Barking
  ```
- **實際應用**：`SavingsAccount` 類別繼承自 `BankAccount`。

---

## 結論
這些功能——類別、物件、方法、變數、控制流程、介面、異常處理、泛型、lambda 表達式、註解等——是 Java 編程的骨幹。它們使您能夠為多樣化的應用編寫穩健、可擴展且易於維護的程式碼。要加深您的掌握：
- **實驗**：編寫結合這些功能的小型程式。
- **探索**：閱讀 Java API 文檔（例如 `java.util`、`java.lang`）。
- **應用**：建構如計算器、圖書館系統或 Web 應用等項目，以觀察這些功能的實際應用。

如果您想深入了解任何特定功能，請告訴我！