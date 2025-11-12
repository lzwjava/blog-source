---
audio: false
generated: true
lang: es
layout: post
title: Cómo Funcionan Las Propiedades En Spring Boot
translated: true
type: note
---

Exploremos cómo funcionan las propiedades en Spring Boot, incluyendo cómo usar archivos YAML o `.properties`, cómo sobrescribirlos con argumentos de línea de comandos como `-D`, las diversas formas de inicializar propiedades y cómo probarlas efectivamente.

---

### **Cómo funcionan las propiedades en Spring Boot**
Spring Boot proporciona un sistema flexible para gestionar la configuración de la aplicación a través de propiedades, que son pares clave-valor. Estas propiedades pueden definirse en múltiples fuentes, y Spring Boot las resuelve basándose en un orden de precedencia específico. Esto te permite personalizar tu aplicación para diferentes entornos o escenarios de despliegue. Las propiedades se cargan en el **Entorno de Spring (Spring Environment)**, haciéndolas accesibles en toda tu aplicación.

Las principales fuentes de propiedades incluyen:
- Archivos de configuración (por ejemplo, `application.properties` o `application.yml`)
- Argumentos de línea de comandos (por ejemplo, `--server.port=8081`)
- Propiedades del sistema (por ejemplo, `-Dserver.port=8081`)
- Variables de entorno
- Código Java (por ejemplo, mediante `@Value` o `@ConfigurationProperties`)

---

### **Uso de archivos YAML o Properties**
Spring Boot admite dos formatos principales para archivos de configuración, ambos ubicados típicamente en `src/main/resources`:

#### **1. Archivos `.properties`**
Este es un formato simple y plano de clave-valor:
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

#### **2. Archivos `.yml` o `.yaml`**
Este es un formato estructurado y jerárquico que usa indentación:
```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
```

**Puntos clave:**
- Usa `.properties` para configuraciones simples y `.yml` para configuraciones anidadas o complejas.
- Se pueden usar archivos específicos de perfil (por ejemplo, `application-dev.yml`) para configuraciones específicas del entorno.
- Ejemplo: Establecer `server.port=8080` cambia el puerto en el que se ejecuta tu aplicación Spring Boot.

---

### **Uso de argumentos de línea de comandos para sobrescribir propiedades**
Puedes sobrescribir propiedades definidas en archivos de configuración usando argumentos de línea de comandos de dos maneras:

#### **1. Usando `--` para Propiedades de Spring Boot**
Pasa propiedades directamente al ejecutar la aplicación:
```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/testdb
```
Estos tienen precedencia sobre los archivos de configuración.

#### **2. Usando `-D` para Propiedades del Sistema**
Establece propiedades del sistema con `-D`, que Spring Boot también reconoce:
```bash
java -Dserver.port=8081 -Dspring.datasource.url=jdbc:mysql://localhost:3306/testdb -jar myapp.jar
```
Las propiedades del sistema también sobrescriben los valores de los archivos de configuración.

---

### **Diferentes formas de inicializar propiedades**
Spring Boot ofrece varios métodos para definir o inicializar propiedades más allá de archivos y argumentos de línea de comandos:

#### **1. Variables de entorno**
Las propiedades se pueden establecer mediante variables de entorno. Por ejemplo:
- Establece `SERVER_PORT=8081` en tu entorno, y Spring Boot lo mapea a `server.port`.
- **Convención de nomenclatura:** Convierte los nombres de las propiedades a mayúsculas y reemplaza los puntos (`.`) con guiones bajos (`_`), por ejemplo, `spring.datasource.url` se convierte en `SPRING_DATASOURCE_URL`.

#### **2. Código Java**
Puedes inicializar propiedades mediante programación:
- **Usando `@Value`**: Inyecta una propiedad específica en un campo.
  ```java
  @Value("${server.port}")
  private int port;
  ```
- **Usando `@ConfigurationProperties`**: Vincula un grupo de propiedades a un objeto Java.
  ```java
  @Component
  @ConfigurationProperties(prefix = "app")
  public class AppProperties {
      private String name;
      // getters y setters
  }
  ```
  Esto vincula propiedades como `app.name` al campo `name`.

#### **3. Valores predeterminados**
Proporciona valores de respaldo si una propiedad no está definida:
- En `@Value`: `@Value("${server.port:8080}")` usa `8080` si `server.port` no está establecido.
- En archivos de configuración: Establece valores predeterminados en `application.properties` o YAML.

---

### **Precedencia de propiedades**
Spring Boot resuelve propiedades de múltiples fuentes en este orden (la precedencia más alta sobrescribe a la más baja):
1. Argumentos de línea de comandos (`--property=value`)
2. Propiedades del sistema (`-Dproperty=value`)
3. Variables de entorno
4. Archivos de configuración (`application.properties` o `application.yml`)
5. Valores predeterminados en el código

**Ejemplo:** Si `server.port=8080` está en `application.properties` pero ejecutas `java -jar myapp.jar --server.port=8081`, el puerto será `8081`.

---

### **Cómo probar propiedades**
Probar propiedades asegura que tu aplicación se comporte como se espera. Aquí hay enfoques comunes:

#### **1. Usando `@TestPropertySource`**
Sobrescribe propiedades en pruebas unitarias:
```java
@SpringBootTest
@TestPropertySource(properties = {"server.port=9090"})
public class MyTest {
    // Código de prueba
}
```

#### **2. Usando `application-test.properties`**
Coloca un archivo específico para pruebas en `src/test/resources`:
```properties
server.port=9090
```
Spring Boot carga este archivo automáticamente durante las pruebas.

#### **3. Sobrescrituras mediante programación**
Establece propiedades en la configuración de la prueba:
```java
@SpringBootTest
public class MyTest {
    @BeforeEach
    public void setup() {
        System.setProperty("server.port", "9090");
    }
}
```

#### **4. Usando `@ActiveProfiles`**
Activa propiedades específicas de un perfil:
- Define `application-test.yml` con configuraciones de prueba.
- Usa:
  ```java
  @SpringBootTest
  @ActiveProfiles("test")
  public class MyTest {
      // Código de prueba
  }
  ```

---

### **Resumen**
- **Archivos de configuración**: Usa `application.properties` o `application.yml` para configuraciones predeterminadas.
- **Argumentos de línea de comandos**: Sobrescribe con `--property=value` o `-Dproperty=value`.
- **Métodos de inicialización**: Aprovecha las variables de entorno, el código Java (`@Value`, `@ConfigurationProperties`) o los valores predeterminados.
- **Pruebas**: Usa `@TestPropertySource`, archivos específicos para pruebas, sobrescrituras mediante programación o perfiles.

Esto cubre los aspectos esenciales del trabajo con propiedades en Spring Boot. ¡Avísame si quieres más detalles!