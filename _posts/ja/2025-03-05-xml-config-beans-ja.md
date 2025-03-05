---
audio: false
generated: true
lang: ja
layout: post
title: XML設定ファイルのBeans
translated: true
---

あなたの質問に対する回答として、beans XMLがどのように動作するか、beanのプロパティやpropsとキーを含む方法、どのクラスがこれらのXMLファイルを使用し、どのように読み込まれるかについて、明確かつ体系的に説明します。この説明は、Springのようなコンテキストを前提としています。ここで「beans XML」は、beanを設定するための一般的な用語です。

### Beans XMLの動作

Springのようなフレームワークでは、**beans XMLファイル**は、*bean*と呼ばれるオブジェクトを定義し管理するための設定ファイルです。これらのbeanは、Springフレームワークによってインスタンス化、設定、管理されるJavaオブジェクトです。XMLファイルには以下が含まれます：

- **Beans**: 各beanは`<bean>`タグを使用して定義され、`id`（ユニークな識別子）と`class`（インスタンス化するJavaクラスの完全修飾名）を含みます。
- **Properties**: beanには、beanの動作を設定するために設定される値や参照が含まれます。プロパティは`<property>`タグを使用して定義されます。
- **PropsとKeys**: `<property>`タグ内で、`<props>`要素を使用してキーと値のペアのセットを定義できます。これは、beanが`java.util.Properties`オブジェクトや`Map`のような構造を期待する場合に便利です。`<props>`要素には、`key`属性と対応する値を持つ複数の`<prop>`タグが含まれます。

以下は、beans XMLファイルの例です：

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

この例では：
- IDが`myBean`のbeanが`com.example.MyBean`クラスから作成されます。
- beanには`someProperty`という名前のプロパティがあります。
- `<props>`要素はキーと値のペアのセット（`key1=value1`と`key2=value2`）を定義し、Springはこれを`Properties`オブジェクトに変換し、`myBean`にセッターメソッド`setSomeProperty(Properties props)`を通じて注入します。

「リソースを入れる」というフレーズは少し不明確ですが、XMLファイルがアプリケーションのクラスパスまたはファイルシステム内の*リソース*（ファイル）であることを指している可能性があります。または、XMLで定義されたbean（データソースなど）がアプリケーションで使用されるリソースを表しているかもしれません。今は、XMLファイル自体がアプリケーションによって読み込まれるリソースであると仮定します。

### これらのXMLファイルを使用するクラス

Springでは、beans XMLファイルを使用（つまり、読み込みおよび処理）する責任を持つクラスは、**`ApplicationContext`**です。より具体的には、`ApplicationContext`インターフェースの実装です。例えば：

- **`ClassPathXmlApplicationContext`**: XMLファイルをクラスパスから読み込みます。
- **`FileSystemXmlApplicationContext`**: XMLファイルをファイルシステムから読み込みます。

`ApplicationContext`は、アプリケーションに設定情報を提供するSpringの中央インターフェースです。XMLファイルを読み取り、解析し、beanの定義を使用してbeanを作成し管理します。bean自体（例：`com.example.MyBean`）は、XMLで定義されたプロパティを使用しますが、`ApplicationContext`はXMLファイルを直接処理してこれを実現します。

### どのように読み込まれるか

beans XMLファイルは、`ApplicationContext`の実装のインスタンスを作成し、XMLファイルの場所を指定することでアプリケーションに読み込まれます。以下にその手順を示します：

1. **XMLファイルの場所を指定**: `ApplicationContext`をインスタンス化する際に、XMLファイルの名前またはパスを提供します。例えば：
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   ここで、`"beans.xml"`はクラスパスにあると仮定されます（例：一般的なJavaプロジェクトの`src/main/resources`ディレクトリ）。

2. **リソースとしての読み込み**: `ApplicationContext`は、`ResourceLoader`を使用してXMLファイルを`Resource`として検索し読み込みます。この場合、`ClassPathXmlApplicationContext`はファイルをクラスパスから検索します。

3. **XMLの解析**: 内部的には、Springは`XmlBeanDefinitionReader`を使用してXMLファイルを解析します。このリーダーは`<bean>`タグ、プロパティ、`<props>`要素を解釈し、`BeanDefinition`オブジェクトを作成します。これらのオブジェクトは、各beanがどのように構築されるべきかを説明します。

4. **Beanの作成**: `ApplicationContext`（Springの`BeanFactory`を拡張）は、これらのbean定義を使用してbeanをインスタンス化し、プロパティを設定（`<props>`から`Properties`オブジェクトを注入することも含む）し、そのライフサイクルを管理します。

読み込まれた後、beanは以下のように`ApplicationContext`から取得できます：
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### 全体をまとめる

- **Beans XMLの動作**: XMLはbeanとそのプロパティ、キーと値のペアを含む`<props>`を定義します。SpringはこのXMLを解析してbeanを設定しインスタンス化します。
- **XMLを使用するクラス**: `ApplicationContext`（例：`ClassPathXmlApplicationContext`）は、XMLファイルを使用してアプリケーションを設定します。
- **読み込み方法**: XMLは、`ApplicationContext`のインスタンスを作成し、ファイルの場所を指定することでクラスパスまたはファイルシステムからリソースとして読み込まれます。

例えば、`beans.xml`がクラスパスにある場合、以下のように読み込みます：
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Springは残りを処理し、設定されたbeanをアプリケーションに利用可能にします。

このメカニズムは強力で柔軟であり、XMLで複雑な設定を定義し、Springが実行時にそれを実現することができます。