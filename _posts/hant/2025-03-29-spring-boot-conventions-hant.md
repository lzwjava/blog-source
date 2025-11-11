---
audio: false
generated: true
lang: hant
layout: post
title: Spring Boot Java 編碼規範
translated: true
type: note
---

## 1. 核心原則
- 遵循標準 Java 程式碼慣例
- 優先考慮可讀性與可維護性
- 在 Spring 生態系統中保持一致性
- 對齊核心 Java 最佳實踐

## 2. 程式碼格式化

### 通用準則
- 使用 IntelliJ IDEA 預設格式化設定
- 4 空格縮排（不使用 Tab 鍵）
- 最大行長度為 120 個字元
- 使用標準 Java 大括號風格

### 具體格式化規則
- 方法之間需留空行
- 不留行尾空白字元
- 使用 Unix 風格行結束符號（LF）

## 3. 命名慣例

### 類別命名
- 使用具描述性、有意義的名稱
- 使用 UpperCamelCase 命名法
- 範例：
  - `ConfigurationProperties`
  - `AutoConfigurationImportSelector`
  - `SpringApplication`

### 方法命名
- 使用 lowerCamelCase 命名法
- 使用動詞或動詞片語
- 範例：
  - `configure()`
  - `registerBeanDefinitions()`
  - `isEnabledByDefault()`

## 4. 註解實踐

### 註解排序
- 註解標準順序：
  1. 覆寫註解（`@Override`）
  2. 作用域註解（`@Component`、`@Service`）
  3. 依賴注入註解
  4. 交易註解
  5. 自訂專案註解

### 註解放置
```java
@Component
@Transactional
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

## 5. 依賴注入

### 優先注入方法
- 建構子注入
- 避免欄位注入
- 在建構子上使用 `@Autowired`

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

## 6. 日誌記錄
- 使用 SLF4J 進行日誌記錄
- 使用 `private static final Logger` 或 Lombok 的 `@Slf4j`

```java
@Slf4j
@Service
public class UserService {
    public void processUser(User user) {
        log.info("Processing user: {}", user.getUsername());
    }
}
```

## 7. 錯誤處理
- 使用特定例外類型
- 提供有意義的錯誤訊息
- 使用 `@ControllerAdvice` 進行全域例外處理

## 8. 配置設定
- 優先使用 `application.yml` 而非 `application.properties`
- 使用環境特定的配置設定
- 外部化配置數值

## 9. 測試
- 使用 JUnit 5
- 善用 Spring Boot Test 工具
- 遵循 Arrange-Act-Assert 模式

## 10. 補充資源
- [Spring Boot GitHub 編碼風格](https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.md)
- [Spring Framework 指南](https://github.com/spring-projects/spring-framework/wiki/Code-Style)