---
audio: false
generated: true
lang: es
layout: post
title: Usando FastJson
translated: true
---

FastJSON es una biblioteca de procesamiento de JSON de alto rendimiento para Java, desarrollada por Alibaba. Se utiliza ampliamente para analizar cadenas JSON en objetos Java, serializar objetos Java en JSON y manejar datos JSON de manera eficiente. A continuación, se presenta una guía sobre cómo usar FastJSON basada en sus características principales.

### Paso 1: Agregar FastJSON a su Proyecto
Para usar FastJSON, debe incluirlo en su proyecto. Si usa Maven, agregue la siguiente dependencia a su `pom.xml`:

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- Use la versión más reciente disponible -->
</dependency>
```

Para Gradle, agregue esto a su `build.gradle`:

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

Consulte el [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) para obtener la última versión.

### Paso 2: Uso Básico
Aquí se muestra cómo usar FastJSON para tareas comunes como la serialización y la deserialización.

#### 1. **Serializar Objetos Java en JSON**
Puede convertir un objeto Java en una cadena JSON usando `JSON.toJSONString()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // Crear un objeto de ejemplo
        User user = new User("Alice", 25);

        // Serializar en cadena JSON
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// Clase de ejemplo User
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters y setters (requeridos para que FastJSON funcione correctamente)
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

#### 2. **Deserializar JSON en Objetos Java**
Puede analizar una cadena JSON de nuevo en un objeto Java usando `JSON.parseObject()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";

        // Deserializar en objeto User
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
Si su JSON representa una lista de objetos, use `JSON.parseArray()`.

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";

        // Deserializar en List<User>
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

### Paso 3: Características Avanzadas
FastJSON ofrece opciones adicionales de personalización:

#### 1. **Personalizar la Serialización**
Puede controlar cómo se serializan los campos usando opciones `SerializerFeature`.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);

        // Usar PrettyFormat para salida legible
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

#### 2. **Manejar Objetos Complejos**
Para objetos anidados, asegúrese de que las clases internas tengan getters/setters adecuados.

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

### Paso 4: Notas y Mejores Prácticas
- **Seguridad**: FastJSON ha tenido vulnerabilidades en versiones anteriores (por ejemplo, ejecución de código remoto). Siempre use la última versión y evite habilitar `Feature.SupportAutoType` a menos que sea necesario.
- **Rendimiento**: FastJSON está optimizado para la velocidad, pero pruébelo con su caso de uso específico para conjuntos de datos grandes.
- **Documentación**: Consulte la página oficial de [FastJSON GitHub](https://github.com/alibaba/fastjson) para obtener más detalles.

¡Hágame saber si necesita ayuda con un caso de uso específico o con la solución de problemas!