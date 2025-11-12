---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Mockito في اختبارات جافا
translated: true
type: note
---

لاستخدام Mockito في اختبارات Java، اتبع هذه الخطوات لإنشاء كائنات وهمية، وتحديد سلوك الأساليب، والتحقق من التفاعلات:

### 1. **إضافة التبعيات**
قم بتضمين Mockito و JUnit في ملف `pom.xml` الخاص بك (Maven):
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

### 3. **إنشاء كائنات وهمية وحقن التبعيات**
- استخدم `@Mock` للتبعيات التي تريد محاكاتها.
- استخدم `@InjectMocks` لحقن الكائنات الوهمية في الفئة قيد الاختبار.

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService تعتمد على UserRepository
```

### 4. **تحديد سلوك استدعاءات الأساليب (Stubbing)**
استخدم `when().thenReturn()` لتحديد سلوك الكائن الوهمي:
```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // تحديد سلوك أسلوب المستودع
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);
    
    assertEquals("Alice", result.getName());
}
```

### 5. **التحقق من التفاعلات**
تحقق مما إذا كان أسلوب الكائن الوهمي قد تم استدعاؤه كما هو متوقع:
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // تحقق من أن أسلوب المستودع تم استدعاؤه مرة واحدة بالمعرف 1
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **حالات الاستخدام الشائعة**

#### **تحديد سلوك لرمي استثناءات**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("خطأ في قاعدة البيانات"));
    
    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **مطابقة الوسائط (Argument Matchers)**
استخدم `any()`, `eq()`، إلخ لمطابقة الوسائط بمرونة:
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **أسلوب BDD (التطوير القائم على السلوك)**
استخدم `given().willReturn()` لتحسين قابلية القراءة:
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

#### **الاقتناص الوسائط (Argument Captor)**
اقتنص الوسائط لإجراء تحقق تفصيلي:
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
- **التهيئة**: استخدم `@ExtendWith(MockitoExtension.class)` (JUnit 5) أو `MockitoAnnotations.openMocks(this)` في `@BeforeEach`.
- **الكائنات الوهمية الساكنة**: استخدم تبعية `mockito-inline لمحاكاة الأساليب/المنشئات الساكنة.
- **الكائنات المراقبة (Spies)**: استخدم `@Spy` لتحويل الكائنات الحقيقية إلى كائنات وهمية جزئية.

### **استكشاف الأخطاء وإصلاحها**
- **كائنات وهمية فارغة (Null)**: تأكد من تهيئة الكائنات الوهمية (استخدم `@ExtendWith` أو `openMocks()`).
- **أخطاء في تحديد السلوك (Stubbing)**: حدد سلوك الأساليب قبل استدعائها في الاختبار.

للحصول على استخدامات متقدمة، راجع [توثيق Mockito](https://site.mockito.org/).