---
audio: false
generated: true
lang: hant
layout: post
title: Java 物件序列化
translated: true
type: note
---

我假設你指的是 "java.io.Serializable" — Java 中用於物件序列化的關鍵介面。以下是如何使用它的實用指南：

### 什麼是 Serializable？
`java.io.Serializable` 是一個標記介面（無需實作任何方法），它告訴 Java 運行時該類別可以被序列化 — 轉換為位元組流以儲存到檔案、透過網絡傳送或存入資料庫，並在之後反序列化回物件。

### 使用 Serializable 的基本步驟

1. **實作介面**
   在類別中加入 `implements Serializable`。這是最低要求。

   ```java
   import java.io.Serializable;

   public class Person implements Serializable {
       private String name;
       private int age;

       // 建構子
       public Person(String name, int age) {
           this.name = name;
           this.age = age;
       }

       // Getter 和 Setter
       public String getName() { return name; }
       public void setName(String name) { this.name = name; }
       public int getAge() { return age; }
       public void setAge(int age) { this.age = age; }

       @Override
       public String toString() {
           return "Person{name='" + name + "', age=" + age + "}";
       }
   }
   ```

2. **序列化 - 寫入物件**
   使用 `ObjectOutputStream` 將物件寫入檔案或流。

   ```java
   import java.io.FileOutputStream;
   import java.io.ObjectOutputStream;
   import java.io.IOException;

   public class SerializeExample {
       public static void main(String[] args) {
           Person person = new Person("Alice", 25);

           try (FileOutputStream fileOut = new FileOutputStream("person.ser");
                ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
               out.writeObject(person);
               System.out.println("Serialized data is saved in person.ser");
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   }
   ```

3. **反序列化 - 讀取物件**
   使用 `ObjectInputStream` 將物件讀回。

   ```java
   import java.io.FileInputStream;
   import java.io.ObjectInputStream;
   import java.io.IOException;

   public class DeserializeExample {
       public static void main(String[] args) {
           try (FileInputStream fileIn = new FileInputStream("person.ser");
                ObjectInputStream in = new ObjectInputStream(fileIn)) {
               Person person = (Person) in.readObject();
               System.out.println("Deserialized Person: " + person);
           } catch (IOException | ClassNotFoundException e) {
               e.printStackTrace();
           }
       }
   }
   ```

### 關鍵注意事項

- **serialVersionUID**：為確保反序列化時的相容性，請定義一個 `serialVersionUID`。如果不定義，Java 會自動生成一個，但該值可能因 JVM 或類別變更而不同。

   ```java
   private static final long serialVersionUID = 1L;
   ```

   將此加入你的 `Person` 類別。

- **Transient 欄位**：標記為 `transient` 的欄位將不會被序列化。
   ```java
   private transient String temporaryData;
   ```

- **非序列化欄位**：如果某個欄位的類別未實作 `Serializable`，你將會收到 `NotSerializableException`。解決方法是讓該類別實作 `Serializable`，或將該欄位標記為 `transient`。

- **繼承**：如果父類別實作了 `Serializable`，子類別也會是可序列化的。如果沒有，則父類別必須有一個無參數建構子，反序列化才能正常運作。

### 包含 transient 和 serialVersionUID 的範例
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password; // 不會被序列化
    private int id;

    public Employee(String name, String password, int id) {
        this.name = name;
        this.password = password;
        this.id = id;
    }

    @Override
    public String toString() {
        return "Employee{name='" + name + "', password='" + password + "', id=" + id + "}";
    }
}
```

### 測試
序列化並反序列化 `Employee`。你會注意到 `password` 在反序列化後為 `null`，因為它被標記為 `transient`。

### 常見應用場景
- 將物件狀態儲存到檔案（例如遊戲存檔）。
- 透過網絡傳送物件（例如在 RMI 或分散式系統中）。
- 快取物件。

### 注意事項
- **安全性**：序列化可能暴露私有欄位，若處理不當。對於敏感資料，可考慮自定義 `writeObject` 和 `readObject` 方法。
- **效能**：對於複雜物件，序列化可能較慢。
- **版本控制**：類別變更（例如新增欄位）可能破壞反序列化，除非妥善管理 `serialVersionUID`。

### 自定義序列化（可選）
若需要控制序列化過程，可實作以下方法：
```java
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    // 自定義邏輯
}

private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    // 自定義邏輯
}
```

如有任何部分需要進一步了解，請隨時告訴我！