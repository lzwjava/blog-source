---
audio: false
generated: true
lang: ja
layout: post
title: JavaにおけるScalaコレクションライブラリの活用
translated: true
type: note
---

Javaで`scala.collection`パッケージを使用するには、ScalaとJavaの相互運用性を活用できます。両言語はJVMバイトコードにコンパイルされるため、ScalaライブラリがJavaプロジェクトでアクセス可能であれば、Javaコードは`scala.collection`パッケージ内のクラスを呼び出すことができます。以下に、説明と例を交えたステップバイステップガイドを示します。

---

### **ステップ1: JavaプロジェクトにScalaライブラリを含める**
`scala.collection`パッケージはScala標準ライブラリの一部であるため、JavaプロジェクトのクラスパスにScalaライブラリを含める必要があります。ビルドツールにScalaライブラリの依存関係を追加することで実現できます：

- **Maven**:
  `pom.xml`に以下を追加：
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- 必要に応じてバージョンを変更 -->
  </dependency>
  ```

- **Gradle**:
  `build.gradle`に以下を追加：
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

これにより、`scala.collection`内のクラスを含むScalaクラスがJavaコードで利用可能になります。

---

### **ステップ2: Scalaコレクションクラスのインポート**
Scalaライブラリがクラスパスに含まれたら、Javaコードで`scala.collection`パッケージから特定のクラスをインポートできます。例えば、Scalaの不変`List`を使用するには：

```java
import scala.collection.immutable.List;
```

その他のよく使われるコレクション：
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

Scalaコレクションは可変版と不変版の両方があることに注意してください（Javaのコレクションは通常、`Collections.unmodifiableList`でラップしない限り可変です）。

---

### **ステップ3: JavaでのScalaコレクションの作成**
Scalaコレクションは通常、コンパニオンオブジェクトを使用して作成されます（例：`apply`メソッド）。ただし、JavaはScalaの構文（例：`List(1, 2, 3)`）を直接サポートしていないため、これらのメソッドを明示的に操作する必要があります。さらに、`List`のようなScalaコレクションの`apply`メソッドは、Javaから呼び出す場合、Scalaのvarargsのコンパイル方法により`Seq`を引数として期待します。

JavaとScalaコレクションを橋渡しするには、`scala.collection.JavaConverters`（Scala 2.12以前）または`scala.jdk.CollectionConverters`（Scala 2.13以降）などの変換ユーティリティを使用します。以下はJavaの`List`からScalaの`List`を作成する方法です：

#### **例: Scala Listの作成**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // Java Listの作成
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

- **`CollectionConverters.asScala`**: Javaの`List`をScalaの`Seq`（具体的にはScala 2.13では`mutable.Buffer`、`Seq`のサブタイプ）に変換します。
- **`List$.MODULE$`**: Scalaの`List`コンパニオンオブジェクトのシングルトンインスタンスにアクセスし、その`apply`メソッドを呼び出せるようにします。
- **`apply(scalaSeq)`**: `Seq`から新しい不変のScala `List`を作成します。

---

### **ステップ4: Scalaコレクションの使用**
JavaでScalaコレクションを取得したら、そのメソッドを使用できます。ただし、ScalaとJavaの違いに注意してください：
- **不変性**: 多くのScalaコレクション（例：`scala.collection.immutable.List`）は不変であり、メソッドは元のコレクションを変更するのではなく新しいコレクションを返します。
- **型消去**: ScalaとJavaの両方で型消去が使用されるため、要素を取得する際に結果をキャストする必要がある場合があります。
- **関数型メソッド**: Scalaコレクションは`map`、`filter`などの関数型操作をサポートしており、Java 8以降のラムダ式で使用できます。

#### **例: 要素へのアクセス**
```java
// 最初の要素を取得
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // 出力: Head: 1

// 先頭以外の要素を取得（tail）
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // 出力: Tail: List(2, 3)
```

#### **例: Scala Listのマッピング**
ラムダ式を使用して各要素を2倍にする：
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // 出力: Doubled: List(2, 4, 6)
```

ここで、`Function1`は1つの引数を持つ関数を表すScalaインターフェースであり、Javaのラムダ構文と互換性があります。

---

### **主な考慮事項**
- **型安全性**: Scalaコレクションはパラメータ化されていますが、メソッドの戻り値の型は型消去によりJavaでは`Object`として現れる場合があります。必要に応じてキャストしてください（例：`(Integer) scalaList.head()`）。
- **パフォーマンス**: Java-Scala間の境界を越える操作には多少のオーバーヘッドが発生しますが、通常は軽微です。
- **パラダイムの違い**: Scalaコレクションは不変性と関数型プログラミングを重視しており、Javaの手続き型スタイルとは異なる場合があります。例えば、不変な`List`に要素を「追加」することはできません—代わりに新しい`List`を作成します（例：`:+`を使用して追加し、新しい`List`を返す）。
- **バージョン互換性**: Scalaライブラリのバージョンが要件に合っていることを確認してください。Scala 2.13以降では`scala.jdk.CollectionConverters`を、2.12以前では`scala.collection.JavaConverters`を使用します。

---

### **まとめ**
Javaで`scala.collection`パッケージを使用するには：
1. プロジェクトのクラスパスにScalaライブラリを追加します（MavenやGradle経由）。
2. 目的のScalaコレクションクラスをインポートします（例：`scala.collection.immutable.List`）。
3. コンパニオンオブジェクト（例：`List$.MODULE$.apply`）を使用してScalaコレクションを作成し、`CollectionConverters`でJavaコレクションをScalaの`Seq`に変換します。
4. 必要に応じてキャストやラムダ式を使用して、Scalaのメソッドでコレクションを操作します。

このアプローチにより、Javaのエコシステム内で作業しながら、Scalaの強力なコレクションライブラリ（不変データ構造や関数型操作など）を活用できます。