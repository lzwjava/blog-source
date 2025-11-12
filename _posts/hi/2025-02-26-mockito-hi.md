---
audio: false
generated: true
lang: hi
layout: post
title: जावा परीक्षणों में मोकिटो का उपयोग
translated: true
type: note
---

Java tests में Mockito का उपयोग करने के लिए, mock objects बनाने, methods को stub करने और interactions को verify करने के लिए इन steps का पालन करें:

### 1. **Dependencies जोड़ें**
अपने `pom.xml` (Maven) में Mockito और JUnit शामिल करें:
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

### 2. **Test Class सेट अप करें**
Mockito के extension के साथ JUnit 5 का उपयोग करें:
```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **Mocks बनाएँ और Dependencies Inject करें**
- उन dependencies के लिए `@Mock` का उपयोग करें जिन्हें आप mock बनाना चाहते हैं।
- test के अंतर्गत class में mocks inject करने के लिए `@InjectMocks` का उपयोग करें।

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService, UserRepository पर निर्भर करता है
```

### 4. **Method Calls को Stub करें**
Mock behavior को परिभाषित करने के लिए `when().thenReturn()` का उपयोग करें:
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

### 5. **Interactions Verify करें**
जांचें कि क्या एक mock method को अपेक्षा के अनुरूप called किया गया था:
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // Verify करें कि repository method को एक बार ID 1 के साथ called किया गया था
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **सामान्य उपयोग के मामले**

#### **Exceptions Stub करें**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("DB Error"));
    
    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **Argument Matchers**
Arguments को लचीले ढंग से match करने के लिए `any()`, `eq()`, आदि का उपयोग करें:
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **BDD (Behavior-Driven Development) Style**
पठनीयता के लिए `given().willReturn()` का उपयोग करें:
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
विस्तृत assertions करने के लिए arguments को capture करें:
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

### **मुख्य नोट्स**
- **Initialization**: `@ExtendWith(MockitoExtension.class)` (JUnit 5) या `@BeforeEach` में `MockitoAnnotations.openMocks(this)` का उपयोग करें।
- **Static Mocks**: static methods/constructors को mock करने के लिए `mockito-inline` dependency का उपयोग करें।
- **Spies**: वास्तविक objects (partial mocks) को wrap करने के लिए `@Spy` का उपयोग करें।

### **समस्या निवारण**
- **Null Mocks**: सुनिश्चित करें कि mocks initialized हैं (`@ExtendWith` या `openMocks()` का उपयोग करें)।
- **Stubbing Errors**: Test में methods के called होने से पहले उन्हें stub करें।

उन्नत उपयोग के लिए, [Mockito Documentation](https://site.mockito.org/) देखें।