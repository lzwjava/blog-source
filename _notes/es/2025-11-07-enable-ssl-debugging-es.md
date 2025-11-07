---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Depuración de SSL TLS de Java
translated: true
---

### Habilitar la depuración SSL/TLS en Java

Para habilitar el registro detallado de las actividades relacionadas con SSL/TLS en Java (por ejemplo, handshakes, validación de certificados, intercambios de claves), se utiliza la propiedad del sistema JVM `-Djavax.net.debug`. Esto envía información de depuración a la consola (stdout/stderr) cuando se ejecuta tu aplicación Java.

#### Instrucciones paso a paso

1. **Elige el nivel de depuración**:
   - Usa `ssl` para detalles básicos del handshake SSL/TLS.
   - Usa `ssl:handshake` para mensajes detallados del handshake (incluye suites de cifrado y certificados).
   - Usa `all` para una depuración exhaustiva (incluye SSL más otros protocolos de red—úsalo con moderación ya que es muy verboso).
   - Recomendación común: Comienza con `ssl:handshake:verbose,keymanager:trustmanager` para obtener información específica de SSL.

2. **Establece la propiedad al ejecutar tu aplicación Java**:
   - **Ejecución por línea de comandos** (por ejemplo, mediante el comando `java`):
     ```
     java -Djavax.net.debug=ssl:handshake -jar tu-app.jar
     ```
     Reemplaza `tu-app.jar` con tu aplicación o clase real (por ejemplo, `com.example.Main`).

   - **En un IDE (por ejemplo, IntelliJ IDEA, Eclipse)**:
     - Ve a Configuraciones de Ejecución/Depuración.
     - Añade `-Djavax.net.debug=ssl:handshake` al campo **Opciones de la VM**.
     - Ejecuta o depura la configuración.

   - **En una herramienta de construcción (por ejemplo, Maven o Gradle)**:
     - **Maven** (en `pom.xml` dentro de `<build><plugins><plugin>` para surefire):
       ```xml
       <configuration>
         <argLine>-Djavax.net.debug=ssl:handshake</argLine>
       </configuration>
       ```
     - **Gradle** (en `build.gradle`):
       ```groovy
       test {
         jvmArgs '-Djavax.net.debug=ssl:handshake'
       }
       ```

3. **Captura los registros**:
   - La salida aparece en tu consola/terminal.
   - Redirige a un archivo para facilitar la revisión:
     ```
     java -Djavax.net.debug=ssl:handshake -jar tu-app.jar > ssl-debug.log 2>&1
     ```
   - Busca líneas que comiencen con `***` (por ejemplo, `*** ClientHello` para el inicio del handshake) o prefijos `javax.net.ssl`.

4. **Desactívalo**:
   - Simplemente elimina el flag `-D` cuando hayas terminado—no está establecido por defecto para evitar sobrecarga de rendimiento.

#### Ejemplo de fragmento de salida
Cuando está habilitado, verás algo como:
```
*** ServerHello, TLSv1.2
RandomCookie:  GMT: 1731000000 bytes = { ... }
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
Compression Method: 0
***
```

#### Consejos
- Esto funciona para Java 8+ (incluyendo 11, 17, 21). En versiones más recientes, también podrías habilitar `-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3` para registros específicos del protocolo.
- Un alto nivel de verbosidad puede ralentizar tu aplicación y saturar los registros—prueba en un entorno de desarrollo.
- Si usas un framework como Spring Boot, añádelo a `application.properties`: `debug=true` (para modo general) o mediante argumentos de la línea de comandos.

Para más detalles, consulta la documentación oficial de Oracle: [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names).