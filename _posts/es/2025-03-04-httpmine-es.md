---
audio: false
generated: true
lang: es
layout: post
title: Usando httpmine
translated: true
type: note
---

Supongo que te referías a "httpmime.jar" en lugar de "httpmine.jar", ya que "httpmime" es una librería bien conocida de Apache HttpComponents utilizada para manejar entidades MIME multipart en peticiones HTTP (por ejemplo, para subir archivos). Si me he equivocado, ¡por favor acláralo! Aquí te explico cómo usar `httpmime.jar` en un proyecto Java:

---

### ¿Qué es `httpmime.jar`?
El `httpmime.jar` es parte del proyecto Apache HttpComponents. Extiende la funcionalidad de `httpclient.jar` proporcionando soporte para peticiones multipart/form-data, que se usan comúnmente para subir archivos o enviar datos complejos a través de HTTP.

Para usarlo, también necesitarás sus dependencias, como `httpclient.jar` y `httpcore.jar`, ya que `httpmime` se construye sobre estas librerías.

---

### Pasos para Usar `httpmime.jar` en Tu Proyecto Java

#### 1. **Descargar el Archivo JAR**
- Visita la [página de descargas de Apache HttpComponents](https://hc.apache.org/downloads.cgi) o el Maven Repository para `httpmime` (por ejemplo, [versión 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)).
- Descarga el archivo `httpmime-<version>.jar` (por ejemplo, `httpmime-4.5.14.jar`).
- También necesitarás:
  - `httpclient-<version>.jar` (por ejemplo, `httpclient-4.5.14.jar`)
  - `httpcore-<version>.jar` (por ejemplo, `httpcore-4.4.16.jar`)
- Asegúrate de que las versiones sean compatibles (consulta las [dependencias del proyecto](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)).

Alternativamente, si usas Maven o Gradle, omite la descarga manual y añádelo mediante tu herramienta de build (ver paso 2).

#### 2. **Añadir el JAR a Tu Proyecto**
- **Método Manual (Sin Herramientas de Build):**
  - Coloca los archivos JAR descargados `httpmime.jar`, `httpclient.jar` y `httpcore.jar` en una carpeta (por ejemplo, `lib/` en el directorio de tu proyecto).
  - Si usas un IDE como Eclipse o IntelliJ:
    - **Eclipse**: Botón derecho en tu proyecto > Properties > Java Build Path > Libraries > Add External JARs > Selecciona los JARs > Apply.
    - **IntelliJ**: File > Project Structure > Modules > Dependencies > "+" > JARs or directories > Selecciona los JARs > OK.
  - Si ejecutas desde la línea de comandos, incluye los JARs en tu classpath:
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" TuClase.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." TuClase
    ```

- **Usando Maven (Recomendado):**
  Añade esto a tu `pom.xml`:
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- Usa la última versión -->
  </dependency>
  ```
  Maven descargará automáticamente `httpclient` y `httpcore` como dependencias transitivas.

- **Usando Gradle:**
  Añade esto a tu `build.gradle`:
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **Escribir Código para Usar `httpmime`**
Aquí tienes un ejemplo de cómo usar `httpmime` para subir un archivo mediante una petición HTTP POST multipart:

```java
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.HttpResponse;
import java.io.File;

public class FileUploadExample {
    public static void main(String[] args) throws Exception {
        // Crear un cliente HTTP
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // Definir la URL a la que enviar la petición
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // Construir la entidad multipart
        File file = new File("ruta/a/tu/archivo.txt"); // Reemplaza con la ruta de tu archivo
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // Añadir el archivo
        builder.addTextBody("description", "Este es un archivo de prueba"); // Añadir campo de texto (opcional)

        // Establecer la entidad en la petición POST
        httpPost.setEntity(builder.build());

        // Ejecutar la petición
        HttpResponse response = httpClient.execute(httpPost);

        // Imprimir el estado de la respuesta
        System.out.println("Código de Respuesta: " + response.getStatusLine().getStatusCode());

        // Limpiar recursos
        httpClient.close();
    }
}
```

#### 4. **Clases Clave y Uso**
- **`MultipartEntityBuilder`**: Se usa para construir la entidad multipart. Puedes añadir archivos (`addPart`), texto (`addTextBody`) o datos binarios (`addBinaryBody`).
- **`FileBody`**: Representa un archivo para subir.
- **`CloseableHttpClient`**: El cliente HTTP de `httpclient.jar` para ejecutar la petición.

#### 5. **Ejecutar Tu Programa**
- Si usas un IDE, simplemente ejecuta el programa.
- Si usas la línea de comandos, compila y ejecuta con el classpath como se mostró arriba.

#### 6. **Solución de Problemas**
- **ClassNotFoundException**: Asegúrate de que todos los JARs requeridos (`httpmime`, `httpclient`, `httpcore`) estén en tu classpath.
- **Version Mismatch**: Usa versiones compatibles de los JARs (por ejemplo, `httpmime-4.5.14` con `httpclient-4.5.14` y `httpcore-4.4.16`).
- **Proyectos Android**: Android tiene su propio paquete `org.apache.http`, que puede generar conflictos. Excluye la versión integrada o usa un JAR reempaquetado (por ejemplo, via JarJar).

---

### Ejemplo de Caso de Uso
Si estás subiendo un archivo a un servidor (como una API REST), `httpmime` simplifica la creación de la petición `multipart/form-data`, que es un estándar para la subida de archivos.

¡Avísame si necesitas alguna aclaración o ayuda con un escenario específico!