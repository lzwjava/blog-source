---
audio: false
generated: true
lang: ja
layout: post
title: ScalaのコレクションライブラリをJavaで使用する
translated: true
---

Javaで`scala.collection`パッケージを使用するには、ScalaとJavaの相互運用性を活用することができます。両方の言語はJVMバイトコードにコンパイルされるため、JavaコードからScalaクラスを呼び出すことができます。ただし、ScalaライブラリがJavaプロジェクトにアクセス可能である必要があります。以下にその手順を示します。

---

### **ステップ 1: JavaプロジェクトにScalaライブラリを追加する**

`scala.collection`パッケージはScala標準ライブラリの一部であるため、JavaプロジェクトのクラスパスにScalaライブラリを追加する必要があります。ビルドツールにScalaライブラリの依存関係を追加することで行います。

- **Maven**:
  `pom.xml`に以下を追加します：
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- 必要に応じてバージョンを変更 -->
  </dependency>
  ```

- **Gradle**:
  `build.gradle`に以下を追加します：
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

これにより、Scalaクラス、特に`scala.collection`に含まれるクラスがJavaコードで利用可能になります。

---

### **ステップ 2: Scalaコレクションクラスをインポートする**

Scalaライブラリがクラスパスにあると、Javaコードで`scala.collection`パッケージから特定のクラスをインポートできます。例えば、Scalaの不変の`List`を使用するには、以下のようにインポートします：

```java
import scala.collection.immutable.List;
```

他にもよく使用されるコレクションには以下があります：
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

Scalaのコレクションは不変と可変の両方のバリエーションがありますが、Javaのコレクションは通常可変であり、不変にするためにはラップする必要があります（例：`Collections.unmodifiableList`）。

---

### **ステップ 3: JavaでScalaコレクションを作成する**

Scalaコレクションは通常、コンパニオンオブジェクトを使用して作成されます。これらのオブジェクトは、Javaが直接サポートしないScalaの構文（例：`List(1, 2, 3)`）を使用します。Scalaの`apply`メソッドは、Javaから呼び出された場合、コレクションのような`List`に対して`Seq`を引数として期待します。

JavaとScalaのコレクションを橋渡しするために、Scalaが提供する変換ユーティリティを使用します。例えば、Scala 2.12以前では`scala.collection.JavaConverters`、Scala 2.13以降では`scala.jdk.CollectionConverters`を使用します。以下に、Javaの`List`からScalaの`List`を作成する方法を示します。

#### **例: Scala Listの作成**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // Java Listを作成
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // Java ListをScala Seqに変換
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // コンパニオンオブジェクトを使用してScala Listを作成
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // Scala Listを出力
        System.out.println(scalaList); // 出力: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: Javaの`List`をScalaの`Seq`（Scala 2.13では`mutable.Buffer`のサブタイプ）に変換します。
- **`List$.MODULE$`**: Scalaの`List`コンパニオンオブジェクトのシングルトンインスタンスにアクセスし、`apply`メソッドを呼び出します。
- **`apply(scalaSeq)`**: `Seq`から新しい不変のScala `List`を作成します。

---

### **ステップ 4: Scalaコレクションを使用する**

JavaでScalaコレクションを持つと、そのメソッドを使用できます。ただし、ScalaとJavaの違いに注意が必要です：
- **不変性**: 多くのScalaコレクション（例：`scala.collection.immutable.List`）は不変であり、メソッドは新しいコレクションを返すのではなく、元のコレクションを変更します。
- **型消去**: ScalaとJavaの両方で型消去が使用されるため、要素を取得する際にキャストが必要になることがあります。
- **関数型メソッド**: Scalaコレクションは`map`、`filter`などの関数型操作をサポートしており、Java 8+のラムダ式で使用できます。

#### **例: 要素へのアクセス**
```java
// 最初の要素を取得
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // 出力: Head: 1

// 先頭以外の要素（テール）を取得
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // 出力: Tail: List(2, 3)
```

#### **例: Scala Listのマッピング**
ラムダを使用して各要素を2倍にします：
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // 出力: Doubled: List(2, 4, 6)
```

ここでは、`Function1`は1つの引数を持つScalaインターフェースであり、Javaのラムダ構文と一致します。

---

### **重要な考慮事項**

- **型安全性**: Scalaコレクションはパラメータ化されていますが、型消去のためメソッドの戻り値が`Object`として表示されることがあります。必要に応じてキャストします（例：`(Integer) scalaList.head()`）。
- **パフォーマンス**: JavaとScalaの境界を越えることで若干のオーバーヘッドが発生しますが、通常は少ないです。
- **パラダイムのシフト**: Scalaコレクションは不変性と関数型プログラミングを強調しており、Javaの命令型スタイルとは異なります。例えば、不変の`List`には「追加」することはできず、新しいものを作成します（例：`:+`を使用して追加し、新しい`List`を返します）。
- **バージョンの互換性**: Scalaライブラリのバージョンが必要に応じて一致するようにしてください。Scala 2.13以降では`scala.jdk.CollectionConverters`を使用し、2.12以前では`scala.collection.JavaConverters`を使用します。

---

### **まとめ**

`scala.collection`パッケージをJavaで使用するには、以下の手順を実行します：
1. Scalaライブラリをプロジェクトのクラスパスに追加します（例：MavenまたはGradleを使用）。
2. 必要なScalaコレクションクラスをインポートします（例：`scala.collection.immutable.List`）。
3. コンパニオンオブジェクトを使用してScalaコレクションを作成し、`CollectionConverters`を使用してJavaコレクションをScala `Seq`に変換します。
4. 必要に応じてキャストとラムダを使用してコレクションを操作します。

このアプローチにより、Javaのエコシステム内でScalaの強力なコレクションライブラリを活用できます。例えば、不変データ構造や関数型操作を使用することができます。