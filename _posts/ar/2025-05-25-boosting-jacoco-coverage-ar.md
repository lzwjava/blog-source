---
audio: false
generated: true
image: false
lang: ar
layout: post
model: deepseek/deepseek-v3.2-exp
title: تعزيز تغطية جاكوكو في جافا سبرينغ
translated: true
type: note
---

إليك استراتيجية شاملة لزيادة تغطية JaCoCo في مشروع Java Spring الكبير الخاص بك الذي يحتوي على 30+ واجهة برمجة تطبيقات (API):

## 1. **تحسين التهيئة**

### تهيئة Maven
```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.11</version>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
        <execution>
            <id>check</id>
            <goals>
                <goal>check</goal>
            </goals>
            <configuration>
                <rules>
                    <rule>
                        <element>BUNDLE</element>
                        <limits>
                            <limit>
                                <counter>LINE</counter>
                                <value>COVEREDRATIO</value>
                                <minimum>0.80</minimum>
                            </limit>
                        </limits>
                    </rule>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>
```

### إعداد متعدد الوحدات (إذا كان مطبقاً)
```xml
<!-- في الـ parent pom -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.11</version>
</plugin>

<!-- في وحدة التجميع -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>report-aggregate</id>
            <phase>verify</phase>
            <goals>
                <goal>report-aggregate</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

## 2. **استراتيجية الاختبار حسب الطبقة**

### اختبارات الوحدة (الأولوية القصوى)
```java
// اختبارات طبقة الخدمة
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void shouldCreateUserSuccessfully() {
        // Given
        UserRequest request = new UserRequest("john", "john@email.com");
        User user = User.builder().name("john").email("john@email.com").build();
        when(userRepository.save(any(User.class))).thenReturn(user);
        
        // When
        UserResponse response = userService.createUser(request);
        
        // Then
        assertThat(response.getName()).isEqualTo("john");
        verify(userRepository).save(any(User.class));
    }
}

// اختبارات طبقة المستودع
@DataJpaTest
class UserRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void shouldFindByEmail() {
        // Given
        User user = User.builder().name("john").email("john@email.com").build();
        entityManager.persist(user);
        
        // When
        Optional<User> found = userRepository.findByEmail("john@email.com");
        
        // Then
        assertThat(found).isPresent();
        assertThat(found.get().getName()).isEqualTo("john");
    }
}
```

### اختبارات التكامل
```java
@SpringBootTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@TestPropertySource(locations = "classpath:application-test.properties")
class UserIntegrationTest {
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Test
    void shouldCreateUserViaApi() {
        // Given
        UserRequest request = new UserRequest("john", "john@email.com");
        
        // When
        ResponseEntity<UserResponse> response = restTemplate.postForEntity(
            "/api/users", 
            request, 
            UserResponse.class
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody().getName()).isEqualTo("john");
    }
}
```

### اختبارات المتحكم (Controller)
```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void shouldReturnUserById() throws Exception {
        // Given
        UserResponse userResponse = new UserResponse(1L, "john", "john@email.com");
        when(userService.getUserById(1L)).thenReturn(userResponse);
        
        // When & Then
        mockMvc.perform(get("/api/users/1"))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.name").value("john"));
    }
}
```

## 3. **تقنيات تحسين التغطية**

### بناة بيانات الاختبار
```java
public class UserTestBuilder {
    
    public static User.UserBuilder defaultUser() {
        return User.builder()
                  .id(1L)
                  .name("john")
                  .email("john@email.com")
                  .createdAt(LocalDateTime.now());
    }
}

// الاستخدام في الاختبارات
User user = UserTestBuilder.defaultUser().build();
```

### الاختبارات المعلمة
```java
@ParameterizedTest
@ValueSource(strings = {"valid@email.com", "test@domain.com", "user@example.org"})
void shouldValidateEmailFormat(String email) {
    UserRequest request = new UserRequest("test", email);
    assertThat(validator.isValid(request)).isTrue();
}
```

### اختبار الاستثناءات
```java
@Test
void shouldThrowUserNotFoundException() {
    // Given
    when(userRepository.findById(999L)).thenReturn(Optional.empty());
    
    // When & Then
    assertThatThrownBy(() -> userService.getUserById(999L))
        .isInstanceOf(UserNotFoundException.class)
        .hasMessage("User not found with id: 999");
}
```

## 4. **مناطق التغطية المنخفضة الشائعة التي يجب استهدافها**

### فئات التهيئة
```java
@Test
void shouldLoadConfigurationProperties() {
    // Given
    EnvironmentTestUtils.addEnvironment(
        context, 
        "app.security.jwt.secret=secret",
        "app.security.jwt.expiration=3600"
    );
    
    // When
    context.refresh();
    JwtProperties props = context.getBean(JwtProperties.class);
    
    // Then
    assertThat(props.getSecret()).isEqualTo("secret");
}
```

### معالجو الاستثناءات
```java
@Test
void shouldHandleValidationException() throws Exception {
    // Given
    MethodArgumentNotValidException exception = mock(MethodArgumentNotValidException.class);
    
    // When
    ResponseEntity<ErrorResponse> response = 
        exceptionHandler.handleValidationException(exception);
    
    // Then
    assertThat(response.getStatusCode()).isEqualTo(HttpStatus.BAD_REQUEST);
}
```

### أدوات التعيين والمحولات
```java
@Test
void shouldMapUserToUserResponse() {
    // Given
    User user = UserTestBuilder.defaultUser().build();
    
    // When
    UserResponse response = userMapper.toResponse(user);
    
    // Then
    assertThat(response.getId()).isEqualTo(1L);
    assertThat(response.getName()).isEqualTo("john");
}
```

## 5. **تقنيات متقدمة**

### تغطية الاختبار للمنطق الشرطي
```java
@Test
void shouldCoverAllUserStatusScenarios() {
    // اختبار حالة ACTIVE
    User activeUser = UserTestBuilder.defaultUser().status(UserStatus.ACTIVE).build();
    assertThat(activeUser.canLogin()).isTrue();
    
    // اختبار حالة INACTIVE
    User inactiveUser = UserTestBuilder.defaultUser().status(UserStatus.INACTIVE).build();
    assertThat(inactiveUser.canLogin()).isFalse();
    
    // اختبار حالة SUSPENDED
    User suspendedUser = UserTestBuilder.defaultUser().status(UserStatus.SUSPENDED).build();
    assertThat(suspendedUser.canLogin()).isFalse();
}
```

### اختبار التكامل مع Testcontainers
```java
@Testcontainers
@SpringBootTest
class UserRepositoryIT {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:13");
    
    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }
    
    @Test
    void shouldPersistUserWithDatabase() {
        // اختبار تكامل قاعدة البيانات الحقيقية
    }
}
```

## 6. **التكامل مع CI/CD**

### أمر Maven للتغطية
```bash
mvn clean verify jacoco:report
```

### فحص التغطية في خط الأنابيب
```yaml
# مثال على GitHub Actions
- name: Test and Coverage
  run: mvn clean verify jacoco:check
```

## 7. **مكاسب سريعة للتحسين الفوري**

1. **إضافة اختبارات وحدة مفقودة للـ getters/setters البسيطة**
2. **اختبار جميع سيناريوهات الاستثناء**
3. **تغطية جميع نقاط نهاية المتحكم (Controller)**
4. **اختبار منطق التحقق**
5. **إضافة اختبارات لفئات الأدوات المساعدة**

## 8. **المراقبة وإعداد التقارير**

### إنشاء التقارير
```bash
# إنشاء تقارير HTML
mvn jacoco:report

# إنشاء تقرير مجمع للوحدات المتعددة
mvn jacoco:report-aggregate
```

ابدأ بالتركيز على المنطق التجاري الحرج وواجهات برمجة التطبيقات (APIs) ذات التغطية الأقل. استخدم تقارير JaCoCo بتنسيق HTML لتحديد الأسطر والفروع غير المغطاة بدقة، ثم اكتب اختبارات مستهدفة لتلك المناطق المحددة.