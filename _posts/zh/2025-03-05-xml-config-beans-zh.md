---
audio: true
generated: true
lang: zh
layout: post
title: XML 配置文件 For Beans
translated: true
---

要回答关于如何使用 beans XML 的问题，包括 bean 属性、props 和 keys，哪个类使用这些 XML 文件以及它们是如何加载的，我们可以清晰且系统地进行分解。这个解释假设在 Spring 这样的上下文中，"beans XML" 是配置 beans 的常用术语。

### Beans XML 如何工作？

在像 Spring 这样的框架中，**beans XML 文件** 是用来定义和管理称为 *beans* 的对象的配置文件。这些 beans 通常是 Spring 框架实例化、配置和管理的 Java 对象。XML 文件指定：

- **Beans**：每个 bean 使用 `<bean>` 标签定义，包括一个 `id`（唯一标识符）和一个 `class`（要实例化的 Java 类的完全限定名）。
- **Properties**：beans 可以有属性，这些属性是设置到 bean 中的值或引用，用于配置其行为。属性使用 `<property>` 标签定义。
- **Props 和 Keys**：在 `<property>` 标签中，可以使用 `<props>` 元素来定义一组键值对。这在 bean 期望 `java.util.Properties` 对象或类似结构（如 `Map`）时非常有用。`<props>` 元素包含多个 `<prop>` 标签，每个标签都有一个 `key` 属性和相应的值。

以下是 beans XML 文件中如何显示的示例：

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

在这个示例中：
- 从类 `com.example.MyBean` 创建一个 ID 为 `myBean` 的 bean。
- 该 bean 有一个名为 `someProperty` 的属性。
- `<props>` 元素定义了一组键值对（`key1=value1` 和 `key2=value2`），Spring 将这些键值对转换为 `Properties` 对象并通过 setter 方法（如 `setSomeProperty(Properties props)`）注入到 `myBean` 中。

你的查询中提到的“它放入资源”这句话有点不明确，但它可能指的是 XML 文件是应用程序使用的*资源*（应用程序类路径或文件系统中的文件），或者它可能意味着 XML 中定义的 beans（如数据源）代表应用程序使用的资源。现在，我们假设它指的是 XML 文件本身作为应用程序加载的资源。

### 使用这些 XML 文件的类是什么？

在 Spring 中，负责使用（即加载和处理）beans XML 文件的类是 **`ApplicationContext`**。更具体地说，它是 `ApplicationContext` 接口的一个实现，例如：

- **`ClassPathXmlApplicationContext`**：从类路径加载 XML 文件。
- **`FileSystemXmlApplicationContext`**：从文件系统加载 XML 文件。

`ApplicationContext` 是 Spring 提供配置信息给应用程序的核心接口。它读取 beans XML 文件，解析它，并使用定义来创建和管理 beans。虽然 beans 本身（例如 `com.example.MyBean`）使用 XML 中定义的属性，但 `ApplicationContext` 是直接处理 XML 文件以实现这一点的类。

### 它将如何加载？

beans XML 文件通过创建 `ApplicationContext` 实现的实例并指定 XML 文件的位置来加载到应用程序中。以下是它的工作步骤：

1. **指定 XML 文件位置**：在实例化 `ApplicationContext` 时，提供 XML 文件的名称或路径。例如：
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   这里，`"beans.xml"` 假设在类路径中（例如在典型的 Java 项目中的 `src/main/resources` 目录中）。

2. **作为资源加载**：`ApplicationContext` 使用 `ResourceLoader` 来定位和加载 XML 文件作为 `Resource`。在这种情况下，`ClassPathXmlApplicationContext` 在类路径中查找文件。

3. **解析 XML**：在内部，Spring 使用 `XmlBeanDefinitionReader` 来解析 XML 文件。这个读取器解释 `<bean>` 标签、属性和 `<props>` 元素，创建描述每个 bean 应该如何构造的 `BeanDefinition` 对象。

4. **Bean 创建**：`ApplicationContext`（它扩展了 Spring 的 `BeanFactory`）使用这些 bean 定义来实例化 beans，设置它们的属性（包括从 `<props>` 注入 `Properties` 对象），并管理它们的生命周期。

加载后，可以从 `ApplicationContext` 中检索 beans，如下所示：
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### 总结

- **Beans XML 如何工作**：XML 定义 beans 和它们的属性，包括通过 `<props>` 定义的键值对。Spring 解析这个 XML 来配置和实例化 beans。
- **使用 XML 的类**：`ApplicationContext`（例如 `ClassPathXmlApplicationContext`）使用 XML 文件来设置应用程序。
- **如何加载**：当你创建一个 `ApplicationContext` 实例并指定文件的位置时，XML 文件作为资源从类路径或文件系统加载。

例如，如果你的 `beans.xml` 在类路径中，你可以用以下方式加载它：
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Spring 然后处理剩下的部分，使配置的 beans 可用于你的应用程序。

这种机制功能强大且灵活，允许你在 XML 中定义复杂的配置，Spring 在运行时将其生成。