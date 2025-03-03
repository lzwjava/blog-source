---
audio: false
generated: true
lang: hant
layout: post
title: 使用 FastJson
translated: true
---

FastJSON 是阿里巴巴開發的一個高效能的 Java JSON 處理庫。它廣泛用於將 JSON 字串解析為 Java 對象、將 Java 對象序列化為 JSON，以及高效處理 JSON 數據。以下是根據其核心功能使用 FastJSON 的指南。

### 第 1 步：將 FastJSON 添加到您的項目中
要使用 FastJSON，您需要將其包含在您的項目中。如果您使用 Maven，請將以下依賴項添加到您的 `pom.xml`：

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- 使用可用的最新版本 -->
</dependency>
```

對於 Gradle，請將以下內容添加到您的 `build.gradle`：

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

請參考 [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) 以獲取最新版本。

### 第 2 步：基本使用
以下是如何使用 FastJSON 進行常見任務，例如序列化和反序列化。

#### 1. **將 Java 對象序列化為 JSON**
您可以使用 `JSON.toJSONString()` 將 Java 對象轉換為 JSON 字串。

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // 創建一個範例對象
        User user = new User("Alice", 25);

        // 序列化為 JSON 字串
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// 範例 User 類
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

**輸出：**
```json
{"age":25,"name":"Alice"}
```

#### 2. **將 JSON 反序列化為 Java 對象**
您可以使用 `JSON.parseObject()` 將 JSON 字串解析回 Java 對象。

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";

        // 反序列化為 User 對象
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**輸出：**
```
Name: Alice, Age: 25
```

#### 3. **將 JSON 解析為列表**
如果您的 JSON 表示對象列表，請使用 `JSON.parseArray()`。

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";

        // 反序列化為 List<User>
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**輸出：**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### 第 3 步：高級功能
FastJSON 提供額外的自定義選項：

#### 1. **自定義序列化**
您可以使用 `SerializerFeature` 選項控制字段的序列化方式。

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);

        // 使用 PrettyFormat 以便於閱讀的輸出
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**輸出：**
```json
{
	"age":25,
	"name":"Alice"
}
```

常見的 `SerializerFeature` 選項：
- `WriteNullListAsEmpty`：空列表寫為 `[]` 而不是 `null`。
- `WriteMapNullValue`：在輸出中包含值為 `null` 的字段。

#### 2. **處理複雜對象**
對於嵌套對象，請確保內部類別具有適當的 getter/setter。

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

**輸出：**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### 第 4 步：注意事項和最佳實踐
- **安全性**：FastJSON 的舊版本存在漏洞（例如遠程代碼執行）。始終使用最新版本，並且除非必要否則不要啟用 `Feature.SupportAutoType`。
- **性能**：FastJSON 針對速度進行了優化，但請針對您的特定用例進行測試，特別是大數據集。
- **文檔**：請參考官方 [FastJSON GitHub 頁面](https://github.com/alibaba/fastjson) 以獲取更多詳細信息。

如果您需要幫助處理特定用例或故障排除，請告訴我！