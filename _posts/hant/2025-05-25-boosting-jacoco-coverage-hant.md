---
audio: false
generated: true
image: false
lang: hant
layout: post
model: deepseek/deepseek-v3.2-exp
title: 提升Java Spring中的JaCoCo覆蓋率
translated: true
type: note
---

以下是在擁有30多個API的大型Java Spring專案中提升JaCoCo覆蓋率的全面策略：

## 1. **配置優化**

### Maven配置
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

### 多模組設置（如適用）
```xml
<!-- 在父pom中 -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.11</version>
</plugin>

<!-- 在聚合模組中 -->
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

## 2. **分層測試策略**

### 單元測試（最高優先級）
```java
// 服務層測試
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void shouldCreateUserSuccessfully() {
        // 給定條件
        UserRequest request = new UserRequest("john", "john@email.com");
        User user = User.builder().name("john").email("john@email.com").build();
        when(userRepository.save(any(User.class))).thenReturn(user);
        
        // 執行操作
        UserResponse response = userService.createUser(request);
        
        // 驗證結果
        assertThat(response.getName()).isEqualTo("john");
        verify(userRepository).save(any(User.class));
    }
}

// 儲存庫層測試
@DataJpaTest
class UserRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void shouldFindByEmail() {
        // 給定條件
        User user = User.builder().name("john").email("john@email.com").build();
        entityManager.persist(user);
        
        // 執行操作
        Optional<User> found = userRepository.findByEmail("john@email.com");
        
        // 驗證結果
        assertThat(found).isPresent();
        assertThat(found.get().getName()).isEqualTo("john");
    }
}
```

### 整合測試
```java
@SpringBootTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@TestPropertySource(locations = "classpath:application-test.properties")
class UserIntegrationTest {
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Test
    void shouldCreateUserViaApi() {
        // 給定條件
        UserRequest request = new UserRequest("john", "john@email.com");
        
        // 執行操作
        ResponseEntity<UserResponse> response = restTemplate.postForEntity(
            "/api/users", 
            request, 
            UserResponse.class
        );
        
        // 驗證結果
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody().getName()).isEqualTo("john");
    }
}
```

### 控制器測試
```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void shouldReturnUserById() throws Exception {
        // 給定條件
        UserResponse userResponse = new UserResponse(1L, "john", "john@email.com");
        when(userService.getUserById(1L)).thenReturn(userResponse);
        
        // 執行操作 & 驗證結果
        mockMvc.perform(get("/api/users/1"))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.name").value("john"));
    }
}
```

## 3. **覆蓋率提升技巧**

### 測試數據構建器
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

// 在測試中的使用
User user = UserTestBuilder.defaultUser().build();
```

### 參數化測試
```java
@ParameterizedTest
@ValueSource(strings = {"valid@email.com", "test@domain.com", "user@example.org"})
void shouldValidateEmailFormat(String email) {
    UserRequest request = new UserRequest("test", email);
    assertThat(validator.isValid(request)).isTrue();
}
```

### 異常測試
```java
@Test
void shouldThrowUserNotFoundException() {
    // 給定條件
    when(userRepository.findById(999L)).thenReturn(Optional.empty());
    
    // 執行操作 & 驗證結果
    assertThatThrownBy(() -> userService.getUserById(999L))
        .isInstanceOf(UserNotFoundException.class)
        .hasMessage("User not found with id: 999");
}
```

## 4. **常見低覆蓋率區域目標**

### 配置類
```java
@Test
void shouldLoadConfigurationProperties() {
    // 給定條件
    EnvironmentTestUtils.addEnvironment(
        context, 
        "app.security.jwt.secret=secret",
        "app.security.jwt.expiration=3600"
    );
    
    // 執行操作
    context.refresh();
    JwtProperties props = context.getBean(JwtProperties.class);
    
    // 驗證結果
    assertThat(props.getSecret()).isEqualTo("secret");
}
```

### 異常處理器
```java
@Test
void shouldHandleValidationException() throws Exception {
    // 給定條件
    MethodArgumentNotValidException exception = mock(MethodArgumentNotValidException.class);
    
    // 執行操作
    ResponseEntity<ErrorResponse> response = 
        exceptionHandler.handleValidationException(exception);
    
    // 驗證結果
    assertThat(response.getStatusCode()).isEqualTo(HttpStatus.BAD_REQUEST);
}
```

### 映射器和轉換器
```java
@Test
void shouldMapUserToUserResponse() {
    // 給定條件
    User user = UserTestBuilder.defaultUser().build();
    
    // 執行操作
    UserResponse response = userMapper.toResponse(user);
    
    // 驗證結果
    assertThat(response.getId()).isEqualTo(1L);
    assertThat(response.getName()).isEqualTo("john");
}
```

## 5. **進階技巧**

### 條件邏輯的測試覆蓋
```java
@Test
void shouldCoverAllUserStatusScenarios() {
    // 測試 ACTIVE 狀態
    User activeUser = UserTestBuilder.defaultUser().status(UserStatus.ACTIVE).build();
    assertThat(activeUser.canLogin()).isTrue();
    
    // 測試 INACTIVE 狀態
    User inactiveUser = UserTestBuilder.defaultUser().status(UserStatus.INACTIVE).build();
    assertThat(inactiveUser.canLogin()).isFalse();
    
    // 測試 SUSPENDED 狀態
    User suspendedUser = UserTestBuilder.defaultUser().status(UserStatus.SUSPENDED).build();
    assertThat(suspendedUser.canLogin()).isFalse();
}
```

### 使用Testcontainers的整合測試
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
        // 真實數據庫整合測試
    }
}
```

## 6. **CI/CD整合**

### 覆蓋率Maven命令
```bash
mvn clean verify jacoco:report
```

### 流水線中的覆蓋率檢查
```yaml
# GitHub Actions示例
- name: Test and Coverage
  run: mvn clean verify jacoco:check
```

## 7. **快速見效的改進方法**

1. **為簡單的getter/setter添加缺失的單元測試**
2. **測試所有異常場景**
3. **覆蓋所有控制器端點**
4. **測試驗證邏輯**
5. **為工具類添加測試**

## 8. **監控和報告**

### 生成報告
```bash
# 生成HTML報告
mvn jacoco:report

# 為多模組生成聚合報告
mvn jacoco:report-aggregate
```

首先專注於關鍵業務邏輯和覆蓋率最低的API。使用JaCoCo HTML報告來精確識別哪些行和分支未被覆蓋，然後為這些特定區域編寫有針對性的測試。