---
audio: false
generated: true
image: false
lang: ja
layout: post
model: deepseek/deepseek-v3.2-exp
title: Java SpringにおけるJaCoCoカバレッジ向上
translated: true
type: note
---

30以上のAPIを持つ大規模なJava SpringプロジェクトでJaCoCoカバレッジを向上させるための包括的な戦略：

## 1. **設定の最適化**

### Maven設定
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

### マルチモジュール設定（該当する場合）
```xml
<!-- 親pomで -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.11</version>
</plugin>

<!-- 集約モジュールで -->
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

## 2. **レイヤー別テスト戦略**

### ユニットテスト（最優先）
```java
// サービスレイヤーテスト
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void shouldCreateUserSuccessfully() {
        // 前提条件
        UserRequest request = new UserRequest("john", "john@email.com");
        User user = User.builder().name("john").email("john@email.com").build();
        when(userRepository.save(any(User.class))).thenReturn(user);
        
        // 実行
        UserResponse response = userService.createUser(request);
        
        // 検証
        assertThat(response.getName()).isEqualTo("john");
        verify(userRepository).save(any(User.class));
    }
}

// リポジトリレイヤーテスト
@DataJpaTest
class UserRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void shouldFindByEmail() {
        // 前提条件
        User user = User.builder().name("john").email("john@email.com").build();
        entityManager.persist(user);
        
        // 実行
        Optional<User> found = userRepository.findByEmail("john@email.com");
        
        // 検証
        assertThat(found).isPresent();
        assertThat(found.get().getName()).isEqualTo("john");
    }
}
```

### 統合テスト
```java
@SpringBootTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@TestPropertySource(locations = "classpath:application-test.properties")
class UserIntegrationTest {
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Test
    void shouldCreateUserViaApi() {
        // 前提条件
        UserRequest request = new UserRequest("john", "john@email.com");
        
        // 実行
        ResponseEntity<UserResponse> response = restTemplate.postForEntity(
            "/api/users", 
            request, 
            UserResponse.class
        );
        
        // 検証
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody().getName()).isEqualTo("john");
    }
}
```

### コントローラーテスト
```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void shouldReturnUserById() throws Exception {
        // 前提条件
        UserResponse userResponse = new UserResponse(1L, "john", "john@email.com");
        when(userService.getUserById(1L)).thenReturn(userResponse);
        
        // 実行 & 検証
        mockMvc.perform(get("/api/users/1"))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.name").value("john"));
    }
}
```

## 3. **カバレッジ向上テクニック**

### テストデータビルダー
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

// テストでの使用例
User user = UserTestBuilder.defaultUser().build();
```

### パラメータ化テスト
```java
@ParameterizedTest
@ValueSource(strings = {"valid@email.com", "test@domain.com", "user@example.org"})
void shouldValidateEmailFormat(String email) {
    UserRequest request = new UserRequest("test", email);
    assertThat(validator.isValid(request)).isTrue();
}
```

### 例外テスト
```java
@Test
void shouldThrowUserNotFoundException() {
    // 前提条件
    when(userRepository.findById(999L)).thenReturn(Optional.empty());
    
    // 実行 & 検証
    assertThatThrownBy(() -> userService.getUserById(999L))
        .isInstanceOf(UserNotFoundException.class)
        .hasMessage("User not found with id: 999");
}
```

## 4. **カバレッジが低くなりがちな対象領域**

### 設定クラス
```java
@Test
void shouldLoadConfigurationProperties() {
    // 前提条件
    EnvironmentTestUtils.addEnvironment(
        context, 
        "app.security.jwt.secret=secret",
        "app.security.jwt.expiration=3600"
    );
    
    // 実行
    context.refresh();
    JwtProperties props = context.getBean(JwtProperties.class);
    
    // 検証
    assertThat(props.getSecret()).isEqualTo("secret");
}
```

### 例外ハンドラー
```java
@Test
void shouldHandleValidationException() throws Exception {
    // 前提条件
    MethodArgumentNotValidException exception = mock(MethodArgumentNotValidException.class);
    
    // 実行
    ResponseEntity<ErrorResponse> response = 
        exceptionHandler.handleValidationException(exception);
    
    // 検証
    assertThat(response.getStatusCode()).isEqualTo(HttpStatus.BAD_REQUEST);
}
```

### マッパーとコンバーター
```java
@Test
void shouldMapUserToUserResponse() {
    // 前提条件
    User user = UserTestBuilder.defaultUser().build();
    
    // 実行
    UserResponse response = userMapper.toResponse(user);
    
    // 検証
    assertThat(response.getId()).isEqualTo(1L);
    assertThat(response.getName()).isEqualTo("john");
}
```

## 5. **高度なテクニック**

### 条件分岐ロジックのテストカバレッジ
```java
@Test
void shouldCoverAllUserStatusScenarios() {
    // ACTIVEステータスのテスト
    User activeUser = UserTestBuilder.defaultUser().status(UserStatus.ACTIVE).build();
    assertThat(activeUser.canLogin()).isTrue();
    
    // INACTIVEステータスのテスト
    User inactiveUser = UserTestBuilder.defaultUser().status(UserStatus.INACTIVE).build();
    assertThat(inactiveUser.canLogin()).isFalse();
    
    // SUSPENDEDステータスのテスト
    User suspendedUser = UserTestBuilder.defaultUser().status(UserStatus.SUSPENDED).build();
    assertThat(suspendedUser.canLogin()).isFalse();
}
```

### Testcontainersを使用した統合テスト
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
        // 実際のデータベースを使用した統合テスト
    }
}
```

## 6. **CI/CD統合**

### カバレッジ用Mavenコマンド
```bash
mvn clean verify jacoco:report
```

### パイプラインでのカバレッジチェック
```yaml
# GitHub Actionsの例
- name: Test and Coverage
  run: mvn clean verify jacoco:check
```

## 7. **即時改善のためのクイックウィン**

1. **単純なgetter/setterの不足テストを追加**
2. **すべての例外シナリオをテスト**
3. **すべてのコントローラーエンドポイントをカバー**
4. **バリデーションロジックをテスト**
5. **ユーティリティクラスのテストを追加**

## 8. **モニタリングとレポート**

### レポート生成
```bash
# HTMLレポートを生成
mvn jacoco:report

# マルチモジュールの集約レポートを生成
mvn jacoco:report-aggregate
```

まずは最も重要なビジネスロジックとカバレッジが最も低いAPIに焦点を当ててください。JaCoCoのHTMLレポートを使用して、カバレッジされていない行やブランチを正確に特定し、それらの特定の領域に対してターゲットを絞ったテストを作成してください。