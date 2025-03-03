---
audio: false
generated: true
lang: ja
layout: post
title: オブジェクトシリアライズのJava
translated: true
---

私は「java.io.Serializable」を意味したのだと思います - Javaでオブジェクトシリアライズに使用される重要なインターフェースです。以下はその使用方法の実践的なガイドです：

### Serializableとは？
`java.io.Serializable`はメソッドを実装する必要のないマーカーインターフェースで、Javaランタイムにクラスがシリアライズ可能であることを伝えます - ファイルに保存、ネットワークを通じて送信、データベースに保存、または後でオブジェクトにデシリアライズされるためのバイトストリームに変換されます。

### Serializableの基本的な使用方法

1. **インターフェースの実装**
   クラスに`implements Serializable`を追加します。これが最低限の要件です。

   ```java
   import java.io.Serializable;

   public class Person implements Serializable {
       private String name;
       private int age;

       // コンストラクタ
       public Person(String name, int age) {
           this.name = name;
           this.age = age;
       }

       // ゲッターとセッター
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

2. **シリアライズ - オブジェクトの書き込み**
   `ObjectOutputStream`を使用してオブジェクトをファイルまたはストリームに書き込みます。

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
               System.out.println("シリアライズされたデータはperson.serに保存されました");
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   }
   ```

3. **デシリアライズ - オブジェクトの読み込み**
   `ObjectInputStream`を使用してオブジェクトを読み込みます。

   ```java
   import java.io.FileInputStream;
   import java.io.ObjectInputStream;
   import java.io.IOException;

   public class DeserializeExample {
       public static void main(String[] args) {
           try (FileInputStream fileIn = new FileInputStream("person.ser");
                ObjectInputStream in = new ObjectInputStream(fileIn)) {
               Person person = (Person) in.readObject();
               System.out.println("デシリアライズされたPerson: " + person);
           } catch (IOException | ClassNotFoundException e) {
               e.printStackTrace();
           }
       }
   }
   ```

### 重要なポイント

- **serialVersionUID**: デシリアライズ時の互換性を確保するために、`serialVersionUID`を定義します。定義しないとJavaが自動的に生成しますが、JVMやクラスの変更によって異なる可能性があります。

   ```java
   private static final long serialVersionUID = 1L;
   ```

   これを`Person`クラスに追加します。

- **一時的なフィールド**: `transient`でマークされたフィールドはシリアライズされません。
   ```java
   private transient String temporaryData;
   ```

- **シリアライズ不可のフィールド**: フィールドのクラスが`Serializable`を実装していない場合、`NotSerializableException`が発生します。そのクラスを`Serializable`にするか、フィールドを`transient`にマークします。

- **継承**: 親クラスが`Serializable`を実装している場合、サブクラスもシリアライズ可能です。そうでない場合、親クラスには引数のないコンストラクタが必要です。

### transientとserialVersionUIDの例
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password; // シリアライズされません
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

### テスト
`Employee`をシリアライズおよびデシリアライズします。`password`が`transient`であるため、デシリアライズ後に`null`になることに気づくでしょう。

### 一般的な使用例
- オブジェクトの状態をファイルに保存（例：ゲームのセーブ）。
- オブジェクトをネットワークを通じて送信（例：RMIまたは分散システム）。
- オブジェクトのキャッシュ。

### 陥穽
- **セキュリティ**: シリアライズは、適切に処理されないとプライベートフィールドを公開する可能性があります。感度の高いデータにはカスタムの`writeObject`と`readObject`メソッドを検討してください。
- **パフォーマンス**: シリアライズは複雑なオブジェクトでは遅くなることがあります。
- **バージョニング**: クラスの変更（例：フィールドの追加）は、`serialVersionUID`が管理されていない限りデシリアライズを破壊する可能性があります。

### カスタムシリアライズ（オプション）
シリアライズを制御する必要がある場合は、これらのメソッドを実装します：
```java
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    // カスタムロジック
}

private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    // カスタムロジック
}
```

もっと深く掘り下げたい部分があれば教えてください！