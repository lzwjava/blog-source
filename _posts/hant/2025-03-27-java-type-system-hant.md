---
audio: false
generated: true
lang: hant
layout: post
title: Java 的類型系統
translated: true
type: note
---

好的，讓我們深入探討 Java 的型別系統！本教程將涵蓋基本概念，助你入門。

**什麼是型別系統？**

在程式設計中，型別系統定義了可以使用的值的種類以及如何操作它們。它有助於確保程式是型別安全的，這意味著操作是在正確的資料型別上執行的，從而防止意外錯誤並提高程式碼的可靠性。

Java 擁有**強型別和靜態型別系統**。

* **強型別：** Java 是強型別的，這意味著變數的型別在編譯時和執行時都會被嚴格執行。你通常無法在不進行明確轉換（強制轉型）的情況下對不相容的型別執行操作。這有助於在開發過程早期發現錯誤。
* **靜態型別：** Java 是靜態型別的，這意味著變數的型別在程式執行前就已宣告（或在某些使用 `var` 的情況下推斷出來）。編譯器會在執行前檢查這些型別的相容性。

**Java 型別系統的主要組成部分：**

Java 的型別系統大致分為兩個主要類別：

1.  **基本型別：** 這些是 Java 中最基本的資料型別。它們直接在記憶體中表示單一值。
2.  **參考型別：** 這些型別代表物件，也就是類別或介面的實例。參考變數儲存物件在記憶體中的位址（參考）。

讓我們詳細探討每一類。

**1. 基本型別：**

Java 有八種基本資料型別：

| 型別      | 大小 (位元) | 描述                                       | 範圍                                                                 | 範例                  |
| --------- | ----------- | ------------------------------------------ | -------------------------------------------------------------------- | --------------------- |
| `byte`    | 8           | 有號整數                                   | -128 到 127                                                          | `byte age = 30;`      |
| `short`   | 16          | 有號整數                                   | -32,768 到 32,767                                                    | `short count = 1000;` |
| `int`     | 32          | 有號整數                                   | -2,147,483,648 到 2,147,483,647                                    | `int score = 95;`     |
| `long`    | 64          | 有號整數                                   | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807            | `long population = 1000000000L;` (注意 'L' 後綴) |
| `float`   | 32          | 單精度浮點數 (IEEE 754)                    | 大約 ±3.40282347E+38F                                                | `float price = 19.99F;` (注意 'F' 後綴) |
| `double`  | 64          | 雙精度浮點數 (IEEE 754)                    | 大約 ±1.79769313486231570E+308                                       | `double pi = 3.14159;` |
| `char`    | 16          | 單一 Unicode 字元                          | '\u0000' (0) 到 '\uffff' (65,535)                                  | `char initial = 'J';` |
| `boolean` | 視情況而定  | 代表邏輯值                                 | `true` 或 `false`                                                    | `boolean isVisible = true;` |

**關於基本型別的要點：**

* 它們直接儲存在記憶體中。
* 它們有預定義的大小和範圍。
* 它們不是物件，也沒有與之關聯的方法（儘管包裝類別如 `Integer`、`Double` 等提供了物件的表示形式）。
* 如果未明確初始化，基本型別欄位會被賦予預設值（例如，`int` 預設為 0，`boolean` 預設為 `false`）。

**2. 參考型別：**

參考型別代表物件，也就是類別或介面的實例。參考型別的變數持有物件在堆積中的記憶體位址（參考）。

**常見的參考型別：**

* **類別：** 類別是建立物件的藍圖。它們定義了該型別物件的資料（欄位/屬性）和行為（方法）。
    ```java
    class Dog {
        String name;
        int age;

        public void bark() {
            System.out.println("Woof!");
        }
    }

    public class Main {
        public static void main(String[] args) {
            Dog myDog = new Dog(); // 'Dog' 是參考型別
            myDog.name = "Buddy";
            myDog.age = 3;
            myDog.bark();
        }
    }
    ```
* **介面：** 介面定義了類別可以實作的方法契約。它們代表一組行為。
    ```java
    interface Animal {
        void makeSound();
    }

    class Cat implements Animal {
        public void makeSound() {
            System.out.println("Meow!");
        }
    }

    public class Main {
        public static void main(String[] args) {
            Animal myCat = new Cat(); // 'Animal' 是參考型別
            myCat.makeSound();
        }
    }
    ```
* **陣列：** 陣列是相同型別元素的集合。陣列的型別由其元素的型別決定。
    ```java
    int[] numbers = new int[5]; // 'int[]' 是參考型別
    numbers[0] = 10;

    String[] names = {"Alice", "Bob", "Charlie"}; // 'String[]' 是參考型別
    ```
* **列舉：** 列舉代表一組固定的命名常數。
    ```java
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }

    public class Main {
        public static void main(String[] args) {
            Day today = Day.MONDAY; // 'Day' 是參考型別
            System.out.println("Today is " + today);
        }
    }
    ```
* **包裝類別：** 對於每種基本型別，Java 都提供了一個對應的包裝類別（例如，`Integer` 對應 `int`，`Double` 對應 `double`）。這些類別讓你可以將基本型別值視為物件。
    ```java
    Integer num = 10; // 'Integer' 是參考型別
    Double piValue = 3.14; // 'Double' 是參考型別
    ```

**關於參考型別的要點：**

* 它們儲存對堆積中物件的參考（記憶體位址）。
* 它們可以是 `null`，意味著該參考不指向任何物件。
* 它們有關聯的方法和欄位（由其類別或介面定義）。
* 未初始化的參考型別欄位的預設值是 `null`。

**3. 使用 `var` 進行型別推斷（Java 10 及更高版本）：**

Java 10 引入了 `var` 關鍵字，允許進行區域變數型別推斷。編譯器可以根據初始化運算式推斷型別，而無需明確宣告型別。

```java
var message = "Hello"; // 編譯器推斷 'message' 為 String 型別
var count = 100;      // 編譯器推斷 'count' 為 int 型別
var prices = new double[]{10.5, 20.3}; // 編譯器推斷 'prices' 為 double[] 型別
```

**關於 `var` 的重要注意事項：**

* `var` 只能用於方法、建構函式或初始化器內的區域變數。
* 使用 `var` 時必須提供初始化器，因為編譯器需要它來推斷型別。
* `var` 不會改變 Java 的靜態型別。型別仍然在編譯時確定。

**4. 泛型：**

泛型允許你參數化型別。這意味著你可以定義能夠處理不同型別的類別、介面和方法，同時提供編譯時型別安全。

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>(); // String 的 List
        names.add("Alice");
        names.add("Bob");

        // names.add(123); // 這會導致編譯時錯誤

        List<Integer> numbers = new ArrayList<>(); // Integer 的 List
        numbers.add(10);
        numbers.add(20);
    }
}
```

這裡，`<String>` 和 `<Integer>` 是型別參數。泛型通過在編譯時強制執行型別約束，有助於在執行時防止 `ClassCastException`。

**5. 型別檢查：**

Java 在兩個主要階段執行型別檢查：

* **編譯時型別檢查：** Java 編譯器在程式碼執行前檢查型別錯誤。如果有任何型別不匹配（例如，嘗試在沒有明確強制轉型的情況下將 `String` 賦值給 `int` 變數），編譯器將報告錯誤並阻止程式被編譯。
* **執行時型別檢查：** 有些型別檢查是在程式執行期間進行的。例如，當你將一個參考型別強制轉型為另一種型別時，JVM 會檢查該物件是否實際上是目標型別的實例。如果不是，則會拋出 `ClassCastException`。

**6. 型別轉換（強制轉型）：**

有時你需要將值從一種型別轉換為另一種型別。Java 支援兩種強制轉型：

* **隱式強制轉型（擴展轉換）：** 當你將較小基本型別的值賦值給較大基本型別的變數時，會自動發生。不會發生資料遺失。
    ```java
    int myInt = 10;
    long myLong = myInt; // 從 int 到 long 的隱式強制轉型
    double myDouble = myLong; // 從 long 到 double 的隱式強制轉型
    ```
* **顯式強制轉型（縮窄轉換）：** 當你將較大基本型別的值賦值給較小基本型別的變數時，必須使用強制轉型運算子 `(targetType)` 手動完成。可能會發生資料遺失。
    ```java
    double myDouble = 10.99;
    int myInt = (int) myDouble; // 從 double 到 int 的顯式強制轉型 (myInt 將是 10)
    ```
* **參考型別強制轉型：** 你也可以在參考型別之間進行強制轉型，但這更複雜，涉及繼承和介面。
    * **向上轉型：** 將子類別的物件強制轉型為其父類別型別。這總是允許隱式進行。
    * **向下轉型：** 將父類別型別的物件強制轉型為其子類別型別。這需要顯式強制轉型，並且如果該物件實際上不是子類別的實例，則可能在執行時導致 `ClassCastException`。

**參考型別強制轉型範例：**

```java
class Animal {}
class Dog extends Animal {
    public void bark() {
        System.out.println("Woof!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myAnimal = new Dog(); // 向上轉型 (隱式)

        // Dog myDog = myAnimal; // 編譯時錯誤: 無法從 Animal 隱式轉換為 Dog
        Dog myDog = (Dog) myAnimal; // 向下轉型 (顯式)
        myDog.bark(); // 這會正常運作

        Animal anotherAnimal = new Animal();
        // Dog anotherDog = (Dog) anotherAnimal; // 這會在執行時拋出 ClassCastException
    }
}
```

**結論：**

理解 Java 的型別系統對於編寫正確且穩健的程式碼至關重要。通過了解基本型別和參考型別之間的區別、泛型的工作原理以及型別檢查和強制轉型的規則，你可以避免常見的程式設計錯誤並建構更可靠的應用程式。

本教程提供了基礎理解。隨著你繼續學習 Java，你將會遇到更多與型別相關的高級概念，例如繼承、多型以及更複雜的泛型場景。持續練習和實驗不同的型別，以鞏固你的理解！