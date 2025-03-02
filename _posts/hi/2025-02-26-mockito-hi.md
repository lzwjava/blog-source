---
audio: false
generated: true
lang: hi
layout: post
title: Mockito को Java Tests में उपयोग करना
translated: true
---

Mockito को Java tests में उपयोग करने के लिए, निम्न कदमों का पालन करें ताकि मॉक ऑब्जेक्ट बनाएं, मेथड्स को स्टब करें और इंटरैक्शंस को वरिफाई करें:

### 1. **Dependencies को Add करें**
`pom.xml` (Maven) में Mockito और JUnit को शामिल करें:
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

### 2. **Test Class Setup करें**
JUnit 5 के साथ Mockito के एक्सटेंशन का उपयोग करें:
```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **Mocks बनाएं और Dependencies Inject करें**
- `@Mock` को dependencies के लिए उपयोग करें जो आप मॉक करना चाहते हैं।
- `@InjectMocks` को मॉक्स को test class में inject करने के लिए उपयोग करें।

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService UserRepository पर निर्भर करता है
```

### 4. **Method Calls को Stub करें**
`when().thenReturn()` का उपयोग करके मॉक व्यवहार को परिभाषित करें:
```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // Repository के method को stub करें
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);

    assertEquals("Alice", result.getName());
}
```

### 5. **Interactions को Verify करें**
एक मॉक मेथड को अपेक्षित रूप से कॉल किया गया था, यह जांचें:
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // Repository method को ID 1 के साथ एक बार कॉल किया गया था, यह वरिफाई करें
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **Common Use Cases**

#### **Exceptions को Stub करें**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("DB Error"));

    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **Argument Matchers**
`any()`, `eq()`, आदि का उपयोग करके arguments को फ्लेक्सिबल रूप से मैच करें:
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **BDD (Behavior-Driven Development) Style**
पढ़ने के लिए `given().willReturn()` का उपयोग करें:
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

#### **Argument Captor**
arguments को कैप्चर करें ताकि विस्तृत assertions कर सकें:
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

### **Key Notes**
- **Initialization**: `@ExtendWith(MockitoExtension.class)` (JUnit 5) या `@BeforeEach` में `MockitoAnnotations.openMocks(this)` का उपयोग करें.
- **Static Mocks**: static methods/constructors को मॉक करने के लिए `mockito-inline` dependency का उपयोग करें.
- **Spies**: `@Spy` का उपयोग करके वास्तविक ऑब्जेक्ट्स को wrap करें (partial mocks).

### **Troubleshooting**
- **Null Mocks**: Ensure mocks are initialized (use `@ExtendWith` or `openMocks()`).
- **Stubbing Errors**: Stub methods before they’re called in the test.

For advanced usage, refer to the [Mockito Documentation](https://site.mockito.org/).