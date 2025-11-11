---
audio: false
generated: true
image: false
lang: hi
layout: post
model: deepseek/deepseek-v3.2-exp
title: जावा स्प्रिंग में जैकोको कवरेज बढ़ाना
translated: true
type: note
---

यहाँ आपके बड़े Java Spring प्रोजेक्ट में 30+ APIs के साथ JaCoCo कवरेज बढ़ाने की एक व्यापक रणनीति है:

## 1. **कॉन्फ़िगरेशन ऑप्टिमाइज़ेशन**

### Maven कॉन्फ़िगरेशन
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

### मल्टी-मॉड्यूल सेटअप (यदि लागू हो)
```xml
<!-- parent pom में -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.11</version>
</plugin>

<!-- aggregation module में -->
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

## 2. **लेयर के अनुसार टेस्ट स्ट्रैटेजी**

### यूनिट टेस्ट (सर्वोच्च प्राथमिकता)
```java
// Service Layer Tests
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

// Repository Layer Tests
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

### इंटीग्रेशन टेस्ट
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

### कंट्रोलर टेस्ट
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

## 3. **कवरेज सुधार तकनीकें**

### टेस्ट डेटा बिल्डर्स
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

// Usage in tests
User user = UserTestBuilder.defaultUser().build();
```

### पैरामीटराइज्ड टेस्ट
```java
@ParameterizedTest
@ValueSource(strings = {"valid@email.com", "test@domain.com", "user@example.org"})
void shouldValidateEmailFormat(String email) {
    UserRequest request = new UserRequest("test", email);
    assertThat(validator.isValid(request)).isTrue();
}
```

### एक्सेप्शन टेस्टिंग
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

## 4. **कम कवरेज वाले सामान्य क्षेत्र जिन पर ध्यान देना है**

### कॉन्फ़िगरेशन क्लासेस
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

### एक्सेप्शन हैंडलर्स
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

### मैपर्स और कन्वर्टर्स
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

## 5. **एडवांस्ड तकनीकें**

### कंडीशनल लॉजिक के लिए टेस्ट कवरेज
```java
@Test
void shouldCoverAllUserStatusScenarios() {
    // Test ACTIVE status
    User activeUser = UserTestBuilder.defaultUser().status(UserStatus.ACTIVE).build();
    assertThat(activeUser.canLogin()).isTrue();
    
    // Test INACTIVE status
    User inactiveUser = UserTestBuilder.defaultUser().status(UserStatus.INACTIVE).build();
    assertThat(inactiveUser.canLogin()).isFalse();
    
    // Test SUSPENDED status
    User suspendedUser = UserTestBuilder.defaultUser().status(UserStatus.SUSPENDED).build();
    assertThat(suspendedUser.canLogin()).isFalse();
}
```

### Testcontainers के साथ इंटीग्रेशन टेस्ट
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
        // Real database integration test
    }
}
```

## 6. **CI/CD इंटीग्रेशन**

### कवरेज के लिए Maven कमांड
```bash
mvn clean verify jacoco:report
```

### पाइपलाइन में कवरेज चेक
```yaml
# GitHub Actions example
- name: Test and Coverage
  run: mvn clean verify jacoco:check
```

## 7. **तत्काल सुधार के लिए त्वरित जीत**

1. **सरल getters/setters के लिए गायब यूनिट टेस्ट जोड़ें**
2. **सभी एक्सेप्शन परिदृश्यों का परीक्षण करें**
3. **सभी कंट्रोलर एंडपॉइंट्स को कवर करें**
4. **वैलिडेशन लॉजिक का परीक्षण करें**
5. **यूटिलिटी क्लासेस के लिए टेस्ट जोड़ें**

## 8. **मॉनिटरिंग और रिपोर्टिंग**

### रिपोर्ट जनरेट करें
```bash
# HTML रिपोर्ट जनरेट करें
mvn jacoco:report

# मल्टी-मॉड्यूल के लिए एकत्रित रिपोर्ट जनरेट करें
mvn jacoco:report-aggregate
```

सबसे कम कवरेज वाले महत्वपूर्ण बिजनेस लॉजिक और APIs पर ध्यान केंद्रित करके शुरुआत करें। JaCoCo HTML रिपोर्ट्स का उपयोग यह पहचानने के लिए करें कि कौन सी लाइनें और ब्रांचेस कवर नहीं हैं, फिर उन विशिष्ट क्षेत्रों के लिए लक्षित टेस्ट लिखें।