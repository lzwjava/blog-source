---
audio: false
generated: true
lang: ja
layout: post
title: JavaテストにおけるMockitoの活用
translated: true
type: note
---

JavaテストでMockitoを使用するには、以下の手順に従ってモックオブジェクトの作成、メソッドのスタブ化、相互作用の検証を行います：

### 1. **依存関係の追加**
`pom.xml`（Maven）にMockitoとJUnitを追加：

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

### 2. **テストクラスの設定**
JUnit 5とMockitoの拡張機能を使用：

```java
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {
    // ...
}
```

### 3. **モックの作成と依存関係の注入**
- モック化したい依存関係には`@Mock`を使用
- テスト対象クラスにモックを注入するには`@InjectMocks`を使用

```java
@Mock
private UserRepository userRepository;

@InjectMocks
private UserService userService; // UserServiceはUserRepositoryに依存
```

### 4. **メソッド呼び出しのスタブ化**
`when().thenReturn()`を使用してモックの動作を定義：

```java
@Test
void getUserById_ReturnsUser_WhenUserExists() {
    User mockUser = new User(1L, "Alice");
    // リポジトリメソッドのスタブ化
    when(userRepository.findById(1L)).thenReturn(mockUser);

    User result = userService.getUserById(1L);
    
    assertEquals("Alice", result.getName());
}
```

### 5. **相互作用の検証**
モックメソッドが期待通りに呼び出されたか確認：

```java
@Test
void getUserById_CallsRepository() {
    userService.getUserById(1L);
    // リポジトリメソッドがID 1で1回呼び出されたことを検証
    verify(userRepository, times(1)).findById(1L);
}
```

---

### **一般的な使用例**

#### **例外のスタブ化**
```java
@Test
void getUserById_ThrowsException_WhenRepositoryFails() {
    when(userRepository.findById(anyLong())).thenThrow(new RuntimeException("DB Error"));
    
    assertThrows(RuntimeException.class, () -> userService.getUserById(1L));
}
```

#### **引数マッチャー**
`any()`, `eq()`などを使用して柔軟に引数をマッチング：

```java
when(userRepository.findById(anyLong())).thenReturn(new User(1L, "Bob"));
```

#### **BDD（振る舞駆動開発）スタイル**
可読性のために`given().willReturn()`を使用：

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

#### **引数キャプチャー**
引数をキャプチャして詳細なアサーションを実行：

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

### **重要な注意点**
- **初期化**: `@ExtendWith(MockitoExtension.class)`（JUnit 5）または`@BeforeEach`内で`MockitoAnnotations.openMocks(this)`を使用
- **静的メソッドのモック**: 静的メソッド/コンストラクタのモック化には`mockito-inline`依存関係を使用
- **スパイ**: 実際のオブジェクトをラップするには`@Spy`を使用（部分的なモック）

### **トラブルシューティング**
- **Nullモック**: モックが初期化されていることを確認（`@ExtendWith`または`openMocks()`を使用）
- **スタブ化エラー**: テストでメソッドが呼び出される前にスタブ化する

高度な使用方法については、[Mockitoドキュメント](https://site.mockito.org/)を参照してください。