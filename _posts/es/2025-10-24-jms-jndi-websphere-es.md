---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: APIs JMS y JNDI para WebSphere
translated: true
type: note
---

### Paquetes y APIs necesarios para JMS en Java

Para utilizar el fragmento de código JMS que referenciaste (para buscar y conectar con una Fábrica de Conexiones JMS en IBM WebSphere Application Server), necesitarás importar los paquetes Java relevantes. Estas son APIs estándar del ecosistema Java EE/Jakarta EE:

- **JNDI (Java Naming and Directory Interface)**: Para la búsqueda `InitialContext`.
  - Paquete: `javax.naming` (o `jakarta.naming` en versiones más recientes de Jakarta EE).
  - Clase clave: `InitialContext` – Este es el punto de partida para las operaciones JNDI. Proporciona un contexto para buscar recursos (como fábricas JMS o colas) por sus nombres JNDI (ej., `"jms/MyConnectionFactory"`). En un contenedor como WAS, se conecta automáticamente al servicio de nombres del servidor.

- **API JMS (Java Message Service)**: Para crear conexiones, sesiones, emisores/receptores y mensajes.
  - Paquete: `javax.jms` (JMS 1.1/2.0) o `jakarta.jms` (Jakarta JMS 3.0+ en EE moderno).
  - Interfaces clave: `QueueConnectionFactory`, `QueueConnection`, `QueueSession`, `QueueSender`, `Queue`, `TextMessage`, etc.

Ejemplo de importaciones al inicio de tu clase Java:
```java
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueConnection;
import javax.jms.QueueSession;
import javax.jms.Queue;
import javax.jms.QueueSender;
import javax.jms.TextMessage;
import javax.jms.JMSException;
```

**¿Qué es `InitialContext`?**  
Es una clase en la API JNDI que actúa como punto de entrada a un servicio de nombres. En tu código:  
```java
InitialContext ctx = new InitialContext();  // Crea un contexto predeterminado vinculado al entorno JNDI del servidor de aplicaciones
QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");  // Busca la fábrica preconfigurada por su nombre JNDI
```  
No se necesitan propiedades en el constructor para aplicaciones que se ejecutan *dentro* de WAS, ya que el contenedor inyecta el entorno (ej., mediante `java.naming.factory.initial`). Si ejecutas un cliente independiente *fuera* de WAS, pasarías una `Hashtable` con propiedades como la URL del proveedor.

### Dependencias de Maven (pom.xml)

Si tu aplicación Java está **desplegada y ejecutándose dentro de WAS** (ej., como una aplicación web, EJB o enterprise bean):  
- **No se necesitan dependencias adicionales**. WAS proporciona las APIs JMS y JNDI listas para usar como parte de su runtime Java EE. Solo compila contra ellas (están en el classpath durante la compilación/despliegue).  
- En `pom.xml`, puedes declararlas explícitamente con `<scope>provided</scope>` para evitar incluirlas en tu WAR/EAR (lo mantiene ligero):  
  ```xml
  <dependencies>
      <dependency>
          <groupId>javax.jms</groupId>  <!-- O jakarta.jms para versiones más recientes -->
          <artifactId>javax.jms-api</artifactId>
          <version>2.0.1</version>  <!-- JMS 2.0, compatible con WAS 8.5+ -->
          <scope>provided</scope>
      </dependency>
      <dependency>
          <groupId>javax.naming</groupId>
          <artifactId>javax.naming-api</artifactId>
          <version>1.0</version>  <!-- JNDI 1.0, estándar -->
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

Si tu aplicación es un **cliente independiente** (ejecutándose fuera de WAS, ej., un cliente ligero que se conecta al servidor):  
- Necesitarás las librerías **WebSphere Application Client** para soporte completo de JMS sobre IIOP. Descarga el paquete cliente "IBM WebSphere Application Server traditional" desde IBM, luego agrégalo a tu classpath.  
- En `pom.xml`, incluye:  
  ```xml
  <dependency>
      <groupId>com.ibm.ws</groupId>
      <artifactId>was-jms-client</artifactId>  <!-- Aproximado; utiliza el repositorio Maven de IBM si está disponible -->
      <version>9.0.5</version>  <!-- Coincide con tu versión de WAS -->
  </dependency>
  ```  
  O utiliza los JARs completos del cliente ligero (ej., `com.ibm.ws.orb_8.5.5.jar`, `com.ibm.ws.jndi_*.jar`). Consulta la documentación de IBM para la configuración exacta.

Para la migración a Jakarta EE (post-2020), cambia a los paquetes `jakarta.*`, pero WAS 9.x todavía usa `javax.*` por defecto—habilita Jakarta mediante feature packs si es necesario.

[Documentación de la API JMS de IBM WebSphere](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-jms-api)  
[Tutorial de JNDI para Java EE](https://docs.oracle.com/javase/tutorial/jndi/)