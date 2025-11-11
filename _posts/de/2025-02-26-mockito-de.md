---
audio: false
generated: true
lang: de
layout: post
title: Mockito in Java-Tests verwenden
translated: true
type: note
---

Um Mockito in Java-Tests zu verwenden, folge diesen Schritten, um Mock-Objekte zu erstellen, Methoden zu stubben und Interaktionen zu verifizieren:

### 1. **Abhängigkeiten hinzufügen**
Füge Mockito und JUnit in deine `pom.xml` (Maven) ein:
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

### 2. **Testklasse einrichten**
Verwende JUnit 5 mit Mockitos Extension:
```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **Mocks erstellen und Abhängigkeiten injizieren**
- Verwende `@Mock` für Abhängigkeiten, die du mocken möchtest.
- Verwende `@InjectMocks`, um Mocks in die zu testende Klasse zu injizieren.

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserService hängt von UserRepository ab
```

### 4. **Methodenaufrufe stubben**
Verwende `when().thenReturn()`, um das Mock-Verhalten zu definieren:
```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // Stubbe die Methode des Repositories
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);
    
    assertEquals("Alice", result.getName());
}
```

### 5. **Interaktionen verifizieren**
Prüfe, ob eine Mock-Methode wie erwartet aufgerufen wurde:
```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // Verifiziere, dass die Repository-Methode einmal mit ID 1 aufgerufen wurde
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **Häufige Anwendungsfälle**

#### **Exceptions stubben**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("DB Error"));
    
    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **Argument Matchers**
Verwende `any()`, `eq()`, etc., um Argumente flexibel zu matchen:
```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **BDD (Behavior-Driven Development) Stil**
Verwende `given().willReturn()` für bessere Lesbarkeit:
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
Fange Argumente ab, um detaillierte Assertions durchzuführen:
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

### **Wichtige Hinweise**
- **Initialisierung**: Verwende `@ExtendWith(MockitoExtension.class)` (JUnit 5) oder `MockitoAnnotations.openMocks(this)` in `@BeforeEach`.
- **Statische Mocks**: Verwende die `mockito-inline` Abhängigkeit, um statische Methoden/Konstruktoren zu mocken.
- **Spies**: Verwende `@Spy`, um echte Objekte zu wrappen (partielle Mocks).

### **Fehlerbehebung**
- **Null Mocks**: Stelle sicher, dass Mocks initialisiert sind (verwende `@ExtendWith` oder `openMocks()`).
- **Stubbing-Fehler**: Stubbe Methoden, bevor sie im Test aufgerufen werden.

Für erweiterte Verwendung, siehe die [Mockito Dokumentation](https://site.mockito.org/).