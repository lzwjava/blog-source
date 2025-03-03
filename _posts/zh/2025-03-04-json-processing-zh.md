---
audio: false
generated: true
lang: zh
layout: post
title: JSON 处理在 Java 中
translated: true
---

要在Java项目中使用`com.fasterxml.jackson`包进行JSON处理，可以利用Jackson库，它广泛用于将Java对象转换为JSON和反之。以下是一个逐步指南，假设你正在使用基于Maven的项目。本指南重点介绍`jackson-databind`模块，它提供了高级功能用于JSON数据绑定。

---

### 1. 将Jackson依赖项添加到项目中
要使用`com.fasterxml.jackson`包，需要在项目中包含Jackson库。如果你使用Maven，将以下依赖项添加到`pom.xml`文件中：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- 替换为最新版本 -->
</dependency>
```

- **注意**：检查[Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind)以获取最新版本，因为它可能比2.12.5新。
- `jackson-databind`模块依赖于`jackson-core`和`jackson-annotations`，因此除非你有特定需求，否则不需要单独添加它们。

添加依赖项后，运行`mvn install`或在IDE中刷新项目以下载库。

---

### 2. 创建`ObjectMapper`实例
`com.fasterxml.jackson.databind`包中的`ObjectMapper`类是进行JSON操作的主要工具。它是线程安全的，并且实例化资源密集型，因此最好创建一个单一的可重用实例：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

将其放在你将执行JSON操作的类中。

---

### 3. 将Java对象转换为JSON（序列化）
要将Java对象转换为JSON字符串，使用`writeValueAsString`方法。以下是一个示例：

#### 定义一个Java类
创建一个包含你想要序列化的字段的类。确保它有getter和setter，因为Jackson默认使用这些来访问私有字段：

```java
public class MyClass {
    private String field1;
    private int field2;

    public MyClass(String field1, int field2) {
        this.field1 = field1;
        this.field2 = field2;
    }

    public String getField1() {
        return field1;
    }

    public void setField1(String field1) {
        this.field1 = field1;
    }

    public int getField2() {
        return field2;
    }

    public void setField2(int field2) {
        this.field2 = field2;
    }
}
```

#### 序列化为JSON
使用`ObjectMapper`将对象转换为JSON：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        MyClass obj = new MyClass("value1", 123);
        String json = mapper.writeValueAsString(obj);
        System.out.println(json);
    }
}
```

**输出**：
```json
{"field1":"value1","field2":123}
```

---

### 4. 将JSON转换为Java对象（反序列化）
要将JSON字符串转换回Java对象，使用`readValue`方法：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // 打印 "value1"
    }
}
```

- **错误处理**：`readValue`方法在JSON格式不正确或不匹配类结构时会抛出`JsonProcessingException`（一个检查异常）。使用try-catch块处理它，或者在方法签名中声明它：

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. 使用注解自定义JSON处理
Jackson提供了注解来自定义字段的序列化或反序列化方式。从`com.fasterxml.jackson.annotation`中将这些注解添加到你的类中：

#### 重命名字段
使用`@JsonProperty`将Java字段映射到不同的JSON字段名称：

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // 构造函数、getter、setter
}
```

**输出**：
```json
{"name":"value1","field2":123}
```

#### 忽略字段
使用`@JsonIgnore`在序列化时排除字段：

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // 构造函数、getter、setter
}
```

**输出**：
```json
{"field1":"value1"}
```

#### 格式化日期
使用`@JsonFormat`指定日期的序列化方式：

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // 构造函数、getter、setter
}
```

**输出**（示例）：
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. 处理高级场景
以下是一些你可能会发现有用的额外功能：

#### 美化打印JSON
为了可读的JSON输出，使用`writerWithDefaultPrettyPrinter`：

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**输出**：
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### 忽略未知属性
如果JSON包含不在你的Java类中的字段，配置`ObjectMapper`忽略它们：

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### 处理文件
从文件读取或写入文件：

```java
// 写入文件
mapper.writeValue(new File("output.json"), obj);

// 从文件读取
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### 处理列表或泛型
对于集合，使用`TypeReference`保留泛型类型信息：

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. 使用`JsonNode`进行动态JSON操作
如果你不想将JSON映射到特定类，使用`JsonNode`进行基于树的方法：

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // 返回 "value1"
```

你也可以动态构建JSON：

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### 总结
要使用`com.fasterxml.jackson`包：
1. 将`jackson-databind`依赖项添加到`pom.xml`。
2. 创建一个单一的`ObjectMapper`实例以重用。
3. 使用`writeValueAsString`将Java对象转换为JSON，使用`readValue`将JSON转换为Java对象。
4. 使用注解（如`@JsonProperty`、`@JsonIgnore`和`@JsonFormat`）自定义行为。
5. 处理异常（例如`JsonProcessingException`）并配置`ObjectMapper`以满足特定需求（例如忽略未知属性）。
6. 探索高级功能，如美化打印、文件I/O或`JsonNode`进行动态JSON处理。

通过这些步骤，你可以在Java应用程序中有效地使用Jackson库处理JSON。