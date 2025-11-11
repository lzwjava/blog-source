---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 測試中使用 Mockito
translated: true
type: note
---

要在 Java 測試中使用 Mockito，請按照以下步驟建立模擬物件、設定方法存根及驗證互動：

### 1. **添加依賴項**
在 `pom.xml` (Maven) 中加入 Mockito 和 JUnit：
```xml
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-core</artifactId>
    <version>5.3.1</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.9.2</version>
    <scope>test</scope>
</dependency>
```

### 2. **設定測試類別**
使用 JUnit 5 搭配 Mockito 擴充功能：
```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **建立模擬物件並注入依賴**
- 使用 `@Mock` 標記需要模擬的依賴項
- 使用 `@InjectMocks` 將模擬物件注入待測試類別

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService 依賴 UserRepository
```

### 4. **設定方法存根**
使用 `when().thenReturn()` 定義模擬行為：
```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // 設定儲存庫方法存根
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);
    
    assertEquals("Alice", result.getName());
}
```

### 5. **驗證互動**
檢查模擬方法是否按預期呼叫：
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // 驗證儲存庫方法是否以 ID 1 呼叫一次
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **常見使用情境**

#### **設定異常存根**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("DB Error"));
    
    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **參數匹配器**
使用 `any()`, `eq()` 等靈活匹配參數：
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **BDD（行為驅動開發）風格**
使用 `given().willReturn()` 提升可讀性：
```java
import static org.mockito.BDDMockito.*;

@Test
void bddStyleExample() {
    given(userRepository.findById(1L)).willReturn(new User(1L, "Alice"));
    
    User result = userService.getUserById(1L);
    
    then(userRepository).should().findById(1L);
    assertEquals("Alice", result.getName());
}
```

#### **參數捕捉器**
捕捉參數以進行詳細斷言：
```java
@Test
void saveUser_CapturesArgument() {
    ArgumentCaptor<User> userCaptor = ArgumentCaptor.forClass(User.class);
    
    userService.saveUser("Charlie");
    
    verify(userRepository).save(userCaptor.capture());
    assertEquals("Charlie", userCaptor.getValue().getName());
}
```

---

### **重要注意事項**
- **初始化**：使用 `@ExtendWith(MockitoExtension.class)` (JUnit 5) 或在 `@BeforeEach` 中使用 `MockitoAnnotations.openMocks(this)`
- **靜態模擬**：使用 `mockito-inline` 依賴項來模擬靜態方法/建構子
- **間諜物件**：使用 `@Spy` 包裝真實物件（部分模擬）

### **疑難排解**
- **空模擬物件**：確保模擬物件已初始化（使用 `@ExtendWith` 或 `openMocks()`）
- **存根錯誤**：在測試呼叫方法前先設定存根

進階用法請參考 [Mockito 官方文件](https://site.mockito.org/)。