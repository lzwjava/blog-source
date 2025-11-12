---
audio: false
generated: true
lang: ja
layout: post
title: インスタンス化例外
translated: true
type: note
---

`LazyDynaBean.java`の844行目で発生する`java.lang.InstantiationException`（エラーメッセージ「Error instantiating property of type」）を修正するには、以下の手順に従ってください。この例外は通常、Apache Commons BeanUtilsライブラリの`LazyDynaBean`がプロパティの型のインスタンスを作成しようとするが、型がインスタンス化できないために失敗した場合に発生します。これは、型が抽象クラス、インターフェース、またはpublicの引数なしコンストラクタがないことが原因である可能性が高いです。

### 問題の理解
`LazyDynaBean`はApache Commons BeanUtilsライブラリの動的Bean実装で、プロパティがアクセスされたときに遅延初期化するように設計されています。このエラーは、`LazyDynaBean.java`の844行目でコードがプロパティの型のインスタンスを作成しようとする（例：`Class.newInstance()`を使用）が、操作が失敗して`InstantiationException`がスローされることを示しています。一般的な原因は次のとおりです：
- プロパティの型が抽象クラスまたはインターフェースである（例：`java.util.ArrayList`ではなく`java.util.List`）
- 型が具象クラスであるが、`newInstance()`に必要なpublicの引数なしコンストラクタがない

### 問題を修正する手順

#### 1. 問題のあるプロパティを特定する
- **スタックトレースを確認する**：完全なスタックトレースまたはエラーログは、例外が発生したときに`LazyDynaBean`がインスタンス化しようとしているプロパティを示しているはずです。例えば、例外が`dynaBean.get("someProperty")`のような呼び出し中にスローされた場合、「someProperty」が原因です。
- **エラーメッセージを確認する**：完全なエラーメッセージが型を指定している場合（例：「Error instantiating property of type java.util.List」）、関連する型をメモします。

#### 2. プロパティの型を決定する
- **`DynaClass`の設定を検査する**：`LazyDynaBean`は、プロパティとその型を定義するために`DynaClass`（多くの場合`LazyDynaClass`）に依存しています。プロパティがどのように定義されているかを確認します：
  - 明示的に`LazyDynaClass`を作成した場合、`dynaClass.add("propertyName", PropertyType.class)`のようなプロパティが追加されるコードを探します。
  - `LazyDynaBean`が事前定義された`DynaClass`なしで作成された場合（例：`new LazyDynaBean()`）、プロパティは動的に追加され、型は最初に設定された値から推論されるか、問題のある型にデフォルト設定される可能性があります。
- **デバッグのヒント**：ロギングを追加するか、デバッガを使用して、問題のあるプロパティに対して`dynaClass.getDynaProperty("propertyName").getType()`によって返される型を出力します。

#### 3. プロパティの型がインスタンス化可能であることを確認する
- **具象クラスを使用する**：型が抽象クラスまたはインターフェースである場合（例：`List`、`Map`、またはカスタムインターフェース`MyInterface`）、publicの引数なしコンストラクタを持つ具象実装に置き換えます：
  - `List`の場合、`List.class`の代わりに`ArrayList.class`を使用します。
  - `Map`の場合、`Map.class`の代わりに`HashMap.class`を使用します。
  - カスタムインターフェースまたは抽象クラスの場合、具象サブクラスを選択します（例：`MyInterface`を実装する`MyConcreteClass`）。
- **例**：
  ```java
  LazyDynaClass dynaClass = new LazyDynaClass();
  dynaClass.add("myList", ArrayList.class); // 具象クラス
  LazyDynaBean dynaBean = new LazyDynaBean(dyna