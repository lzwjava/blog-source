---
audio: false
generated: true
image: false
lang: es
layout: post
model: deepseek/deepseek-v3.2-exp
title: Aumentando la Cobertura de JaCoCo en Java Spring
translated: true
type: note
---

Aquí tienes una estrategia integral para aumentar la cobertura de JaCoCo en tu gran proyecto Java Spring con 30+ APIs:

## 1. **Optimización de la Configuración**

### Configuración de Maven
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

### Configuración Multi-módulo (si aplica)
```xml
<!-- En el pom padre -->
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.11</version>
</plugin>

<!-- En el módulo de agregación -->
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

## 2. **Estrategia de Pruebas por Capa**

### Pruebas Unitarias (Máxima Prioridad)
```java
// Pruebas de la Capa de Servicio
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

// Pruebas de la Capa de Repositorio
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

### Pruebas de Integración
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

### Pruebas de Controlador
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

## 3. **Técnicas de Mejora de Cobertura**

### Constructores de Datos de Prueba
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

// Uso en pruebas
User user = UserTestBuilder.defaultUser().build();
```

### Pruebas Parametrizadas
```java
@ParameterizedTest
@ValueSource(strings = {"valid@email.com", "test@domain.com", "user@example.org"})
void shouldValidateEmailFormat(String email) {
    UserRequest request = new UserRequest("test", email);
    assertThat(validator.isValid(request)).isTrue();
}
```

### Pruebas de Excepciones
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

## 4. **Áreas Comunes de Baja Cobertura a Objetivar**

### Clases de Configuración
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

### Manejadores de Excepciones
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

### Mappers y Convertidores
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

## 5. **Técnicas Avanzadas**

### Cobertura de Pruebas para Lógica Condicional
```java
@Test
void shouldCoverAllUserStatusScenarios() {
    // Probar estado ACTIVE
    User activeUser = UserTestBuilder.defaultUser().status(UserStatus.ACTIVE).build();
    assertThat(activeUser.canLogin()).isTrue();
    
    // Probar estado INACTIVE
    User inactiveUser = UserTestBuilder.defaultUser().status(UserStatus.INACTIVE).build();
    assertThat(inactiveUser.canLogin()).isFalse();
    
    // Probar estado SUSPENDED
    User suspendedUser = UserTestBuilder.defaultUser().status(UserStatus.SUSPENDED).build();
    assertThat(suspendedUser.canLogin()).isFalse();
}
```

### Prueba de Integración con Testcontainers
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
        // Prueba de integración con base de datos real
    }
}
```

## 6. **Integración con CI/CD**

### Comando Maven para Cobertura
```bash
mvn clean verify jacoco:report
```

### Verificación de Cobertura en Pipeline
```yaml
# Ejemplo de GitHub Actions
- name: Test and Coverage
  run: mvn clean verify jacoco:check
```

## 7. **Victorias Rápidas para Mejora Inmediata**

1. **Añadir pruebas unitarias faltantes para getters/setters simples**
2. **Probar todos los escenarios de excepción**
3. **Cubrir todos los endpoints del controlador**
4. **Probar la lógica de validación**
5. **Añadir pruebas para clases de utilidad**

## 8. **Monitoreo y Reportes**

### Generar Reportes
```bash
# Generar reportes HTML
mvn jacoco:report

# Generar reporte agregado para multi-módulo
mvn jacoco:report-aggregate
```

Comienza enfocándote en la lógica de negocio crítica y las APIs con la cobertura más baja. Usa los reportes HTML de JaCoCo para identificar exactamente qué líneas y ramas no están cubiertas, luego escribe pruebas dirigidas para esas áreas específicas.