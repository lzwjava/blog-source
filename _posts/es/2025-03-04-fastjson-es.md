---
audio: false
generated: true
lang: es
layout: post
title: Uso de FastJson
translated: true
type: note
---

FastJSON es una librería de procesamiento JSON de alto rendimiento para Java, desarrollada por Alibaba. Es ampliamente utilizada para analizar cadenas JSON en objetos Java, serializar objetos Java en JSON y manejar datos JSON de manera eficiente. A continuación se presenta una guía sobre cómo usar FastJSON basada en sus características principales.

### Paso 1: Agregar FastJSON a tu proyecto
Para usar FastJSON, necesitas incluirlo en tu proyecto. Si estás usando Maven, agrega la siguiente dependencia a tu `pom.xml`:

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- Usa la última versión disponible -->
</dependency>
```

Para Gradle, agrega esto a tu `build.gradle`:

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

Consulta el [Repositorio Central de Maven](https://mvnrepository.com/artifact/com.alibaba/fastjson) para obtener la última versión.

### Paso 2: Uso básico
Aquí se explica cómo usar FastJSON para tareas comunes como serialización y deserialización.

#### 1. **Serializar objetos Java a JSON**
Puedes convertir un objeto Java a una cadena JSON usando `JSON.toJSONString()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // Crear un objeto de ejemplo
        User user = new User("Alice", 25);
        
        // Serializar a cadena JSON
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// Clase User de ejemplo
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters y setters (necesarios para que FastJSON funcione correctamente)
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**Salida:**
```json
{"age":25,"name":"Alice"}
```

#### 2. **Deserializar JSON a objetos Java**
Puedes analizar una cadena JSON de vuelta a un objeto Java usando `JSON.parseObject()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";
        
        // Deserializar a objeto User
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**Salida:**
```
Name: Alice, Age: 25
```

#### 3. **Analizar JSON en una Lista**
Si tu JSON representa una lista de objetos, usa `JSON.parseArray()`.

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";
        
        // Deserializar a List<User>
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**Salida:**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### Paso 3: Características avanzadas
FastJSON ofrece opciones de personalización adicionales:

#### 1. **Personalizar la serialización**
Puedes controlar cómo se serializan los campos usando opciones de `SerializerFeature`.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);
        
        // Usar PrettyFormat para una salida legible
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**Salida:**
```json
{
	"age":25,
	"name":"Alice"
}
```

Opciones comunes de `SerializerFeature`:
- `WriteNullListAsEmpty`: Las listas vacías se escriben como `[]` en lugar de `null`.
- `WriteMapNullValue`: Incluir campos con valores `null` en la salida.

#### 2. **Manejo de objetos complejos**
Para objetos anidados, asegúrate de que las clases internas tengan los getters/setters apropiados.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        Address address = new Address("123 Main St", "NY");
        User user = new User("Alice", 25, address);
        
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);

        User parsedUser = JSON.parseObject(jsonString, User.class);
        System.out.println(parsedUser.getAddress().getCity());
    }
}

class User {
    private String name;
    private int age;
    private Address address;

    public User(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public Address getAddress() { return address; }
    public void setAddress(Address address) { this.address = address; }
}

class Address {
    private String street;
    private String city;

    public Address(String street, String city) {
        this.street = street;
        this.city = city;
    }

    public String getStreet() { return street; }
    public void setStreet(String street) { this.street = street; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
}
```

**Salida:**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### Paso 4: Notas y mejores prácticas
- **Seguridad**: FastJSON ha tenido vulnerabilidades en versiones antiguas (por ejemplo, ejecución remota de código). Usa siempre la última versión y evita habilitar `Feature.SupportAutoType` a menos que sea necesario.
- **Rendimiento**: FastJSON está optimizado para velocidad, pero pruébalo con tu caso de uso específico para conjuntos de datos grandes.
- **Documentación**: Consulta la [página oficial de FastJSON en GitHub](https://github.com/alibaba/fastjson) para más detalles.

¡Avísame si necesitas ayuda con un caso de uso específico o para resolver problemas!