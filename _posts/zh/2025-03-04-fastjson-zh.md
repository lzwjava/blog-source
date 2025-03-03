---
audio: false
generated: true
lang: zh
layout: post
title: 使用FastJson
translated: true
---

FastJSON 是阿里巴巴开发的一个高性能的 Java JSON 处理库。它广泛用于将 JSON 字符串解析为 Java 对象、将 Java 对象序列化为 JSON，以及高效处理 JSON 数据。以下是基于其核心功能的使用指南。

### 第 1 步：将 FastJSON 添加到您的项目中
要使用 FastJSON，您需要在项目中包含它。如果您使用 Maven，请将以下依赖项添加到您的 `pom.xml`：

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- 使用最新可用版本 -->
</dependency>
```

对于 Gradle，请将以下内容添加到您的 `build.gradle`：

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

请访问 [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) 查找最新版本。

### 第 2 步：基本用法
以下是如何使用 FastJSON 进行常见任务，如序列化和反序列化。

#### 1. **将 Java 对象序列化为 JSON**
您可以使用 `JSON.toJSONString()` 将 Java 对象转换为 JSON 字符串。

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // 创建一个示例对象
        User user = new User("Alice", 25);

        // 序列化为 JSON 字符串
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// 示例 User 类
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters 和 setters（FastJSON 正常工作所需）
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**输出：**
```json
{"age":25,"name":"Alice"}
```

#### 2. **将 JSON 反序列化为 Java 对象**
您可以使用 `JSON.parseObject()` 将 JSON 字符串解析回 Java 对象。

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";

        // 反序列化为 User 对象
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**输出：**
```
Name: Alice, Age: 25
```

#### 3. **将 JSON 解析为列表**
如果您的 JSON 表示对象列表，请使用 `JSON.parseArray()`。

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";

        // 反序列化为 List<User>
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**输出：**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### 第 3 步：高级功能
FastJSON 提供了额外的自定义选项：

#### 1. **自定义序列化**
您可以使用 `SerializerFeature` 选项控制字段的序列化方式。

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);

        // 使用 PrettyFormat 以便于阅读的输出
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**输出：**
```json
{
	"age":25,
	"name":"Alice"
}
```

常见的 `SerializerFeature` 选项：
- `WriteNullListAsEmpty`：空列表写为 `[]` 而不是 `null`。
- `WriteMapNullValue`：在输出中包含值为 `null` 的字段。

#### 2. **处理复杂对象**
对于嵌套对象，请确保内部类有适当的 getter/setter。

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        Address address = new Address("123 Main St", "NY");
        User user = new User("Alice", 25, address);

        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);

        User parsedUser = JSON.parseObject(jsonString, User.class);
        System.out.println(parsedUser.getAddress().getCity());
    }
}

class User {
    private String name;
    private int age;
    private Address address;

    public User(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public Address getAddress() { return address; }
    public void setAddress(Address address) { this.address = address; }
}

class Address {
    private String street;
    private String city;

    public Address(String street, String city) {
        this.street = street;
        this.city = city;
    }

    public String getStreet() { return street; }
    public void setStreet(String street) { this.street = street; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
}
```

**输出：**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### 第 4 步：注意事项和最佳实践
- **安全性**：FastJSON 的旧版本存在漏洞（例如远程代码执行）。始终使用最新版本，并除非必要否则不要启用 `Feature.SupportAutoType`。
- **性能**：FastJSON 优化了速度，但请根据您的具体用例对大数据集进行测试。
- **文档**：请参考官方 [FastJSON GitHub 页面](https://github.com/alibaba/fastjson) 以获取更多详细信息。

如果您需要帮助处理特定用例或故障排除，请告诉我！