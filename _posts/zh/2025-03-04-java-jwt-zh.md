---
audio: false
generated: true
lang: zh
layout: post
title: Java JWT 库
translated: true
---

要在 Java 中使用 `com.nimbusds.jwt` 库从 JSON Web Token (JWT) 中提取信息，如过期日期、签发日期和其他声明，请按照下面的步骤进行操作。这个解决方案假设你在处理的是签名 JWT，这是最常见的类型，并且重点在于提供一个清晰、实用的方法来实现你的目标。

---

## 前提条件

首先，确保你已经将 Nimbus JOSE + JWT 库添加到你的项目中。如果你使用的是 Maven，请在 `pom.xml` 中包含以下依赖项：

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- 替换为最新版本 -->
</dependency>
```

你可以在 [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt) 上查看最新版本。

---

## 提取过期日期、签发日期和其他声明的步骤

以下是如何使用 `com.nimbusds.jwt` 库解析 JWT 并检索过期日期、签发日期和其他声明的方法：

1. **解析 JWT 字符串**：使用 `SignedJWT.parse()` 方法将 JWT 字符串转换为 `SignedJWT` 对象。
2. **获取声明集**：使用 `getJWTClaimsSet()` 从 JWT 中访问声明（键值对）。
3. **提取特定声明**：
   - 使用 `getExpirationTime()` 获取过期日期（`exp` 声明）。
   - 使用 `getIssueTime()` 获取签发日期（`iat` 声明）。
   - 使用 `getSubject()`、`getClaim()` 或其他方法获取其他声明。
4. **处理错误**：将解析逻辑包装在 try-catch 块中以管理潜在的解析问题。

---

## 示例代码

以下是一个完整的 Java 示例，演示如何从 JWT 中提取过期日期、签发日期和其他声明（例如主题）：

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // 替换为你的实际 JWT 字符串
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // 步骤 1：解析 JWT 字符串
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // 步骤 2：获取声明集
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // 步骤 3：提取过期和签发日期
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // 另一个声明的示例

            // 步骤 4：显示结果
            if (expirationDate != null) {
                System.out.println("过期日期: " + expirationDate);
            } else {
                System.out.println("未设置过期日期。");
            }

            if (issuedDate != null) {
                System.out.println("签发日期: " + issuedDate);
            } else {
                System.out.println("未设置签发日期。");
            }

            if (subject != null) {
                System.out.println("主题: " + subject);
            } else {
                System.out.println("未设置主题。");
            }

        } catch (ParseException e) {
            System.out.println("无效的 JWT: " + e.getMessage());
        }
    }
}
```

---

## 代码解释

### 1. **导入**
- `SignedJWT`：表示一个签名 JWT 并提供解析和处理方法。
- `JWTClaimsSet`：包含 JWT 负载中的声明。
- `ParseException`：如果 JWT 字符串格式不正确或无法解析，则抛出。
- `Date`：用于表示过期和签发时间。

### 2. **解析 JWT**
- `SignedJWT.parse(jwtString)` 方法接受一个 JWT 字符串（例如 `header.payload.signature`）并返回一个 `SignedJWT` 对象。如果 JWT 无效，则抛出 `ParseException`。

### 3. **访问声明**
- `signedJWT.getJWTClaimsSet()` 检索声明集，其中包含 JWT 负载中的所有声明。

### 4. **提取特定声明**
- **`getExpirationTime()`**：以 `Date` 对象返回 `exp` 声明（如果不存在则为 `null`）。这表示令牌过期的时间。
- **`getIssueTime()`**：以 `Date` 对象返回 `iat` 声明（如果不存在则为 `null`）。这表示令牌签发的时间。
- **`getSubject()`**：以 `String` 返回 `sub` 声明（如果不存在则为 `null`），这是另一个标准声明的示例。你也可以使用 `getClaim("key")` 以 `Object` 形式检索自定义声明。

### 5. **错误处理**
- try-catch 块确保如果 JWT 格式不正确或无效，程序能够优雅地处理错误并打印错误消息。

---

## 注意事项

- **签名 vs. 无签名 JWT**：这个示例使用 `SignedJWT` 处理签名令牌。如果你有无签名 JWT，请使用 `PlainJWT.parse(jwtString)`。对于更通用的方法，你可以使用 `JWTParser.parse(jwtString)`，然后使用 `instanceof` 检查类型（`SignedJWT`、`PlainJWT` 等）。
- **签名验证**：这个代码不验证 JWT 的签名。在生产环境中，你应该使用 `signedJWT.verify(verifier)` 和适当的密钥来验证令牌的真实性。
- **空检查**：在检索声明时始终检查 `null`，因为它们是可选的，可能不在每个 JWT 中存在。
- **自定义声明**：要访问非标准声明，使用 `claimsSet.getClaim("claimName")`，它以 `Object` 形式返回，你可以将其转换为适当的类型（例如 `String`、`Integer`）。

---

## 示例输出

对于上述示例 JWT 字符串：
```
过期日期: 2018年1月17日 19:52:02 UTC
签发日期: 2018年1月17日 19:50:22 UTC
主题: 1234567890
```

---

这个方法提供了一种简单有效的方法，使用 `com.nimbusds.jwt` 库从 JWT 中提取过期日期、签发日期和其他声明。将 `jwtString` 替换为你自己的令牌，并根据你的具体需求调整代码！