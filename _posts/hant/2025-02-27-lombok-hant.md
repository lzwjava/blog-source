---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 中使用 Lombok
translated: true
type: note
---

要在 Java 中使用 Lombok，您需要在專案中進行設定，以減少如 getter、setter 和建構函數等樣板程式碼，從而簡化程式碼。以下是逐步操作指南：

首先，您需要將 Lombok 添加為依賴項。如果您使用 Maven，請在 `pom.xml` 中包含以下內容：

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.32</version> <!-- 請檢查最新版本 -->
    <scope>provided</scope>
</dependency>
```

如果您使用 Gradle，請在 `build.gradle` 中添加以下內容：

```gradle
provided 'org.projectlombok:lombok:1.18.32'
// 同時添加以下內容以確保註解處理正常工作
annotationProcessor 'org.projectlombok:lombok:1.18.32'
```

接下來，如果您使用像 IntelliJ IDEA 或 Eclipse 這樣的 IDE，您需要啟用註解處理並安裝 Lombok 外掛：
- **IntelliJ**：前往 `File > Settings > Plugins`，搜尋 "Lombok"，安裝後重啟。然後確保在 `Settings > Build, Execution, Deployment > Compiler > Annotation Processors` 中勾選 `Enable annotation processing`。
- **Eclipse**：從官方網站 (projectlombok.org) 下載 Lombok JAR，使用 `java -jar lombok.jar` 運行，並按照安裝程式的指示指向您的 Eclipse 安裝目錄。

現在，您可以在 Java 程式碼中使用 Lombok 註解。以下是一個簡單範例：

```java
import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Person {
    private String name;
    private int age;
}
```

在此範例中：
- `@Getter` 和 `@Setter` 會自動為 `name` 和 `age` 生成 getter 和 setter 方法。
- `@NoArgsConstructor` 會創建一個無參數建構函數。
- `@AllArgsConstructor` 會創建一個包含所有欄位作為參數的建構函數。

當您編譯或運行此程式碼時，Lombok 會處理這些註解並為您添加樣板程式碼。您可以這樣測試：

```java
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        System.out.println(person.getName()); // 輸出：Alice
        person.setAge(31);
        System.out.println(person.getAge()); // 輸出：31
    }
}
```

一些您可能也會覺得有用的常用註解：
- `@Data`：這是 `@Getter`、`@Setter`、`@ToString`、`@EqualsAndHashCode` 以及為必要欄位（如 final 欄位）生成建構函數的快捷方式。
- `@Builder`：為物件創建提供建造者模式。
- `@Slf4j`：為您的類別添加一個記錄器（例如來自 SLF4J）。

例如，使用 `@Data` 和 `@Builder`：

```java
import lombok.Data;
import lombok.Builder;

@Data
@Builder
public class User {
    private String username;
    private String email;
}

// 使用方式
public class Main {
    public static void main(String[] args) {
        User user = User.builder()
                        .username("john_doe")
                        .email("john@example.com")
                        .build();
        System.out.println(user); // 輸出：User(username=john_doe, email=john@example.com)
    }
}
```

請注意：
- 請務必在 Maven Central 或官方網站上檢查 Lombok 的最新版本。
- 如果您在團隊中工作，請確保每個人都已在他們的 IDE 中設定好 Lombok，以避免因生成的程式碼在原始碼中不可見而導致混淆。