---
audio: false
generated: true
lang: ja
layout: post
title: BeanのXML設定ファイル
translated: true
type: note
---

あなたの「beans XMLの動作方法、propsとkeysを使用したbeanプロパティ、これらのXMLファイルを使用するクラス、および読み込み方法」に関する質問に対処するため、明確かつ体系的に説明します。この説明は、Springのようなコンテキストを想定しています。ここでは「beans XML」がbeanを設定するための一般的な用語です。

### Beans XMLの動作方法

Springのようなフレームワークでは、**beans XMLファイル**は*bean*と呼ばれるオブジェクトを定義および管理するために使用される設定ファイルです。これらのbeanは通常、Springフレームワークがインスタンス化、設定、および管理するJavaオブジェクトです。XMLファイルは以下を指定します：

- **Beans**: 各beanは`<bean>`タグを使用して定義され、`id`（一意の識別子）と`class`（インスタンス化するJavaクラスの完全修飾名）が含まれます。
- **プロパティ**: Beanはプロパティを持つことができます。これらは、beanの動作を設定するためにbeanに設定される値または参照です。プロパティは`<property>`タグを使用して定義されます。
- **PropsとKeys**: `<property>`タグ内で、`<props>`要素を使用して一連のキーと値のペアを定義できます。これは、beanが`java.util.Properties`オブジェクトまたは`Map`のような類似の構造を期待する場合に便利です。`<props>`要素は複数の`<prop>`タグを含み、各タグには`key`属性と対応する値があります。

以下は、beans XMLファイルでの表示例です：

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
- `<props>`要素は一連のキーと値のペア（`key1=value1`および`key2=value2`）を定義し、Springはこれを`Properties`オブジェクトに変換し、`setSomeProperty(Properties props)`のようなセッターメソッドを介して`myBean`に注入します。

あなたのクエリにある「it puts in resources」というフレーズは少し不明確ですが、おそらく、アプリケーションが使用する*リソース*（アプリケーションのクラスパスまたはファイルシステム内のファイル）としてのXMLファイルを指しているか、またはXMLで定義されたbean（データソースなど）がアプリケーションで使用されるリソースを表している可能性があります。ここでは、XMLファイル自体がアプリケーションによってロードされるリソースであると仮定します。

### これらのXMLファイルを使用するクラスは何ですか？

Springでは、beans XMLファイルを使用する（つまり、ロードおよび処理する）責任を持つクラスは**`ApplicationContext`**です。より正確には、`ApplicationContext`インターフェースの実装です。例えば：

- **`ClassPathXmlApplicationContext`**: クラスパスからXMLファイルをロードします。
- **`FileSystemXmlApplicationContext`**: ファイルシステムからXMLファイルをロードします。

`ApplicationContext`は、アプリケーションに設定情報を提供するSpringの中心的なインターフェースです。これはbeans XMLファイルを読み取り、解析し、定義を使用してbeanを作成および管理します。bean自体（例：`com.example.MyBean`）はXMLで定義されたプロパティを使用しますが、`ApplicationContext`はこれを実現するためにXMLファイルを直接処理するクラスです。

### どのようにロードされますか？

beans XMLファイルは、`ApplicationContext`実装のインスタンスを作成し、XMLファイルの場所を指定することでアプリケーションにロードされます。以下はその仕組みをステップバイステップで説明します：

1. **XMLファイルの場所を指定**: `ApplicationContext`をインスタンス化するときに、XMLファイルの名前またはパスを提供します。例：
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   ここで、`"beans.xml"`はクラスパス内（例：典型的なJavaプロジェクトの`src/main/resources`ディレクトリ）にあると想定されます。

2. **リソースとしてのロード**: `ApplicationContext`は`ResourceLoader`を使用してXMLファイルを`Resource`として特定し、ロードします。この場合、`ClassPathXmlApplicationContext`はクラスパス内のファイルを探します。

3. **XMLの解析**: 内部的に、Springは`XmlBeanDefinitionReader`を使用してXMLファイルを解析します。このリーダーは`<bean>`タグ、プロパティ、および`<props>`要素を解釈し、各beanの構築方法を記述する`BeanDefinition`オブジェクトを作成します。

4. **Beanの作成**: `ApplicationContext`（Springの`BeanFactory`を拡張）はこれらのbean定義を使用してbeanをインスタンス化し、それらのプロパティを設定し（`<props>`からの`Properties`オブジェクトの注入を含む）、それらのライフサイクルを管理します。

一度ロードされると、以下のように`ApplicationContext`からbeanを取得できます：
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### 全体のまとめ

- **Beans XMLの動作方法**: XMLはbeanとそれらのプロパティ（`<props>`を介したキーと値のペアを含む）を定義します。SpringはこのXMLを解析してbeanを設定およびインスタンス化します。
- **XMLを使用するクラス**: `ApplicationContext`（例：`ClassPathXmlApplicationContext`）は、アプリケーションを設定するためにXMLファイルを使用します。
- **ロード方法**: XMLは、ファイルの場所を指定して`ApplicationContext`インスタンスを作成するときに、クラスパスまたはファイルシステムからリソースとしてロードされます。

例えば、`beans.xml`がクラスパスにある場合、以下でロードします：
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Springはその後残りを処理し、設定されたbeanをアプリケーションで利用可能にします。

このメカニズムは強力で柔軟性があり、Springが実行時に実現する複雑な設定をXMLで定義することができます。