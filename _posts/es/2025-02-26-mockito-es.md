---
audio: false
generated: true
lang: es
layout: post
title: Uso de Mockito en Pruebas de Java
translated: true
type: note
---

Para usar Mockito en pruebas de Java, sigue estos pasos para crear objetos mock, stub de métodos y verificar interacciones:

### 1. **Agregar Dependencias**
Incluye Mockito y JUnit en tu `pom.xml` (Maven):
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

### 2. **Configurar la Clase de Prueba**
Usa JUnit 5 con la extensión de Mockito:
```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **Crear Mocks e Inyectar Dependencias**
- Usa `@Mock` para las dependencias que quieras simular.
- Usa `@InjectMocks` para inyectar los mocks en la clase bajo prueba.

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService depende de UserRepository
```

### 4. **Hacer Stub de Llamadas a Métodos**
Usa `when().thenReturn()` para definir el comportamiento del mock:
```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // Hacer stub del método del repositorio
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);
    
    assertEquals("Alice", result.getName());
}
```

### 5. **Verificar Interacciones**
Comprueba si un método mock fue llamado como se esperaba:
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // Verifica que el método del repositorio fue llamado una vez con el ID 1
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **Casos de Uso Comunes**

#### **Stub de Excepciones**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("Error de BD"));
    
    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **Comparadores de Argumentos**
Usa `any()`, `eq()`, etc., para comparar argumentos de forma flexible:
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **Estilo BDD (Behavior-Driven Development)**
Usa `given().willReturn()` para mejorar la legibilidad:
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
Captura argumentos para realizar aserciones detalladas:
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

### **Notas Clave**
- **Inicialización**: Usa `@ExtendWith(MockitoExtension.class)` (JUnit 5) o `MockitoAnnotations.openMocks(this)` en `@BeforeEach`.
- **Mocks Estáticos**: Usa la dependencia `mockito-inline` para simular métodos/constructores estáticos.
- **Spies**: Usa `@Spy` para envolver objetos reales (mocks parciales).

### **Solución de Problemas**
- **Mocks Nulos**: Asegúrate de que los mocks estén inicializados (usa `@ExtendWith` o `openMocks()`).
- **Errores de Stubbing**: Haz stub de los métodos antes de que sean llamados en la prueba.

Para uso avanzado, consulta la [Documentación de Mockito](https://site.mockito.org/).