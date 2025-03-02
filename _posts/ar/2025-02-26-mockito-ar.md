---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Mockito في اختبارات Java
translated: true
---

لاستخدام Mockito في اختبارات Java، اتبع هذه الخطوات لإنشاء كائنات وهمية، استبدال طرق، وتأكيد التفاعلات:

### 1. **إضافة الاعتماديات**
أضف Mockito و JUnit إلى ملف `pom.xml` (Maven):
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

### 2. **إعداد فئة الاختبار**
استخدم JUnit 5 مع امتداد Mockito:
```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **إنشاء كائنات وهمية وإدخال الاعتماديات**
- استخدم `@Mock` للاعتماديات التي تريد استبدالها.
- استخدم `@InjectMocks` لإدخال الكائنات الوهمية إلى فئة الاختبار.

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService يعتمد على UserRepository
```

### 4. **استبدال استدعاءات الطرق**
استخدم `when().thenReturn()` لتحديد سلوك الكائن الوهمي:
```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // استبدل طريقة المستودع
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);

    assertEquals("Alice", result.getName());
}
```

### 5. **تأكيد التفاعلات**
تحقق من أن طريقة الكائن الوهمي تم استدعاؤها كما هو متوقع:
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // تحقق من أن طريقة المستودع تم استدعاؤها مرة واحدة مع معرف 1
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **حالات استخدام شائعة**

#### **استبدال الاستثناءات**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("DB Error"));

    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **مطابقة المعلمات**
استخدم `any()`, `eq()`, إلخ. لمطابقة المعلمات بشكل مرن:
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **BDD (Behavior-Driven Development) Style**
استخدم `given().willReturn()` لمزيد من القراءة:
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

#### **مقبض المعلمات**
أسر المعلمات لإجراء تأكيدات تفصيلية:
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

### **ملاحظات رئيسية**
- **التنشيط**: استخدم `@ExtendWith(MockitoExtension.class)` (JUnit 5) أو `MockitoAnnotations.openMocks(this)` في `@BeforeEach`.
- **الكائنات الوهمية الثابتة**: استخدم اعتمادية `mockito-inline` لاستبدال الطرق الثابتة/المباني.
- **الجواسيس**: استخدم `@Spy` لتغليف الكائنات الحقيقية (استبدال جزئي).

### **إصلاح الأخطاء**
- **الكائنات الوهمية الفارغة**: تأكد من أن الكائنات الوهمية تم تنشيطها (استخدم `@ExtendWith` أو `openMocks()`).
- **أخطاء الاستبدال**: استبدل الطرق قبل استدعائها في الاختبار.

للمستخدم المتقدم، راجع [توثيق Mockito](https://site.mockito.org/).