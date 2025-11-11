---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおけるオブジェクトシリアライゼーション
translated: true
type: note
---

「java.io.Serializable」を指していると思います - Javaにおけるオブジェクトシリアライゼーションのための重要なインターフェースです。以下はその実践的な使用方法です：

### Serializableとは？
`java.io.Serializable`はマーカーインターフェース（実装するメソッドなし）で、クラスがシリアライズ可能であることをJavaランタイムに伝えます。シリアライゼーションとは、オブジェクトをバイトストリームに変換してファイルに保存したり、ネットワーク経由で送信したり、データベースに格納したりし、後でデシリアライズしてオブジェクトに戻すプロセスです。

### Serializableを使用する基本的な手順

1. **インターフェースの実装**
   クラスに`implements Serializable`を追加します。これが最低要件です。

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

2. **シリアライゼーション - オブジェクトの書き込み**
   `ObjectOutputStream`を使用してオブジェクトをファイルやストリームに書き込みます。

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

3. **デシリアライゼーション - オブジェクトの読み込み**
   `ObjectInputStream`を使用してオブジェクトを読み戻します。

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

### 覚えておくべき重要なポイント

- **serialVersionUID**: デシリアライゼーション中の互換性を確保するために、`serialVersionUID`を定義します。定義しない場合、Javaは自動的に生成しますが、JVM間やクラスの変更によって異なる場合があります。

   ```java
   private static final long serialVersionUID = 1L;
   ```

   これを`Person`クラスに追加します。

- **transientフィールド**: `transient`でマークされたフィールドはシリアライズされません。
   ```java
   private transient String temporaryData;
   ```

- **非シリアライズ可能フィールド**: フィールドのクラスが`Serializable`を実装していない場合、`NotSerializableException`が発生します。そのクラスを`Serializable`にするか、フィールドを`transient`でマークしてください。

- **継承**: スーパークラスが`Serializable`を実装している場合、サブクラスもシリアライズ可能です。実装していない場合、デシリアライゼーションを機能させるにはスーパークラスに引数なしコンストラクタが必要です。

### transientとserialVersionUIDの使用例
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
`Employee`をシリアライズおよびデシリアライズします。`password`は`transient`のため、デシリアライズ後は`null`になります。

### 一般的な使用例
- オブジェクト状態のファイル保存（例：ゲームのセーブデータ）
- ネットワーク経由でのオブジェクト送信（例：RMIや分散システム）
- オブジェクトのキャッシュ

### 落とし穴
- **セキュリティ**: シリアライゼーションは注意して扱わないとプライベートフィールドを公開する可能性があります。機密データにはカスタムの`writeObject`および`readObject`メソッドを検討してください。
- **パフォーマンス**: 複雑なオブジェクトの場合、シリアライゼーションは遅くなる可能性があります。
- **バージョニング**: クラスの変更（例：フィールドの追加）は、`serialVersionUID`が管理されていない限り、デシリアライゼーションを破壊する可能性があります。

### カスタムシリアライゼーション（オプション）
シリアライゼーションを制御する必要がある場合は、これらのメソッドを実装します：
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

どの部分についてより深く知りたいか教えてください！