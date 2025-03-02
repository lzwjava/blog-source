---
audio: false
generated: true
lang: zh
layout: post
title: 使用Mockito进行Java测试
translated: true
---

要在 Java 测试中使用 Mockito，请按照以下步骤创建模拟对象、存根方法并验证交互：

### 1. **添加依赖**
在 `pom.xml`（Maven）中包含 Mockito 和 JUnit：
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

### 2. **设置测试类**
使用 JUnit 5 与 Mockito 的扩展：
```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **创建模拟对象并注入依赖**
- 使用 `@Mock` 来模拟你想要模拟的依赖。
- 使用 `@InjectMocks` 将模拟对象注入到被测试的类中。

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService 依赖于 UserRepository
```

### 4. **存根方法调用**
使用 `when().thenReturn()` 来定义模拟行为：
```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // 存根仓库的方法
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);

    assertEquals("Alice", result.getName());
}
```

### 5. **验证交互**
检查模拟方法是否按预期调用：
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // 验证仓库方法被调用一次，ID 为 1
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **常见用例**

#### **存根异常**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("DB Error"));

    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **参数匹配器**
使用 `any()`, `eq()` 等来灵活匹配参数：
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **BDD（行为驱动开发）风格**
使用 `given().willReturn()` 以提高可读性：
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

#### **参数捕获器**
捕获参数以执行详细断言：
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

### **关键注意事项**
- **初始化**：使用 `@ExtendWith(MockitoExtension.class)`（JUnit 5）或在 `@BeforeEach` 中使用 `MockitoAnnotations.openMocks(this)`。
- **静态模拟**：使用 `mockito-inline` 依赖来模拟静态方法/构造函数。
- **间谍**：使用 `@Spy` 来包装真实对象（部分模拟）。

### **故障排除**
- **空模拟**：确保模拟对象已初始化（使用 `@ExtendWith` 或 `openMocks()`）。
- **存根错误**：在测试中调用方法之前存根方法。

对于高级用法，请参考 [Mockito 文档](https://site.mockito.org/)。