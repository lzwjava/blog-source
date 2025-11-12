---
audio: false
generated: true
lang: hant
layout: post
title: 使用FastJson
translated: true
type: note
---

FastJSON 是由阿里巴巴開發的高效能 JSON 處理函式庫，廣泛用於將 JSON 字串解析為 Java 物件、將 Java 物件序列化為 JSON，以及高效處理 JSON 資料。以下是基於其核心功能的使用指南。

### 步驟 1：將 FastJSON 加入專案
要使用 FastJSON，您需要將其加入專案中。若使用 Maven，請在 `pom.xml` 中加入以下依賴項：

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- 請使用可用的最新版本 -->
</dependency>
```

若使用 Gradle，請在 `build.gradle` 中加入：

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

請查閱 [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) 以獲取最新版本。

### 步驟 2：基本用法
以下是使用 FastJSON 進行序列化和反序列化等常見任務的方法。

#### 1. **將 Java 物件序列化為 JSON**
您可以使用 `JSON.toJSONString()` 將 Java 物件轉換為 JSON 字串。

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // 建立範例物件
        User user = new User("Alice", 25);
        
        // 序列化為 JSON 字串
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// 範例 User 類別
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter 和 Setter（FastJSON 需依賴這些方法正常運作）
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

#### 2. **將 JSON 反序列化為 Java 物件**
您可以使用 `JSON.parseObject()` 將 JSON 字串解析回 Java 物件。

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";
        
        // 反序列化為 User 物件
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**輸出：**
```
Name: Alice, Age: 25
```

#### 3. **將 JSON 解析為清單**
若 JSON 代表物件清單，請使用 `JSON.parseArray()`。

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

### 步驟 3：進階功能
FastJSON 提供額外的自訂選項：

#### 1. **自訂序列化**
您可以使用 `SerializerFeature` 選項控制欄位的序列化方式。

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);
        
        // 使用 PrettyFormat 獲得易讀的輸出
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
- `WriteNullListAsEmpty`：將空清單寫為 `[]` 而非 `null`。
- `WriteMapNullValue`：在輸出中包含值為 `null` 的欄位。

#### 2. **處理複雜物件**
對於嵌套物件，請確保內部類別具有正確的 getter/setter 方法。

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

### 步驟 4：注意事項與最佳實踐
- **安全性**：舊版 FastJSON 曾存在漏洞（例如遠端程式碼執行）。請務必使用最新版本，並避免啟用 `Feature.SupportAutoType`，除非必要。
- **效能**：FastJSON 針對速度進行了優化，但對於大型資料集，請在您的具體使用情境中進行測試。
- **文件**：更多詳細資訊請參閱官方 [FastJSON GitHub 頁面](https://github.com/alibaba/fastjson)。

如有特定使用情境或疑難排解需求，請隨時告知！