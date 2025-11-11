---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca JWT de Java
translated: true
type: note
---

Para utilizar la biblioteca `com.nimbusds.jwt` en Java y extraer información como la fecha de expiración, la fecha de emisión y otras reclamaciones (claims) de un JSON Web Token (JWT), sigue los pasos que se detallan a continuación. Esta solución asume que estás trabajando con un JWT firmado, que es el tipo más común, y se centra en proporcionar un enfoque claro y práctico para lograr tu objetivo.

---

## Prerrequisitos

Primero, asegúrate de tener la biblioteca Nimbus JOSE + JWT agregada a tu proyecto. Si estás usando Maven, incluye la siguiente dependencia en tu `pom.xml`:

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- Reemplaza con la última versión -->
</dependency>
```

Puedes consultar la última versión en [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt).

---

## Pasos para Extraer la Fecha de Expiración, Fecha de Emisión y Otras Reclamaciones

Así es como puedes analizar (parsear) un JWT y recuperar la fecha de expiración, la fecha de emisión y reclamaciones adicionales utilizando la biblioteca `com.nimbusds.jwt`:

1.  **Analizar la Cadena JWT**: Usa el método `SignedJWT.parse()` para convertir la cadena JWT en un objeto `SignedJWT`.
2.  **Obtener el Conjunto de Reclamaciones**: Accede a las reclamaciones (pares clave-valor) del JWT usando `getJWTClaimsSet()`.
3.  **Extraer Reclamaciones Específicas**:
    - Usa `getExpirationTime()` para la fecha de expiración (reclamación `exp`).
    - Usa `getIssueTime()` para la fecha de emisión (reclamación `iat`).
    - Usa `getSubject()`, `getClaim()` u otros métodos para reclamaciones adicionales.
4.  **Manejar Errores**: Envuelve la lógica de análisis en un bloque try-catch para gestionar posibles problemas de análisis.

---

## Código de Ejemplo

A continuación se muestra un ejemplo completo en Java que demuestra cómo extraer la fecha de expiración, la fecha de emisión y una reclamación adicional (por ejemplo, el sujeto) de un JWT:

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // Reemplaza esto con tu cadena JWT real
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // Paso 1: Analizar la cadena JWT
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // Paso 2: Obtener el conjunto de reclamaciones
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // Paso 3: Extraer fechas de expiración y emisión
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // Ejemplo de otra reclamación

            // Paso 4: Mostrar los resultados
            if (expirationDate != null) {
                System.out.println("Fecha de expiración: " + expirationDate);
            } else {
                System.out.println("No hay fecha de expiración establecida.");
            }

            if (issuedDate != null) {
                System.out.println("Fecha de emisión: " + issuedDate);
            } else {
                System.out.println("No hay fecha de emisión establecida.");
            }

            if (subject != null) {
                System.out.println("Sujeto: " + subject);
            } else {
                System.out.println("No hay sujeto establecido.");
            }

        } catch (ParseException e) {
            System.out.println("JWT inválido: " + e.getMessage());
        }
    }
}
```

---

## Explicación del Código

### 1. **Importaciones**
- `SignedJWT`: Representa un JWT firmado y proporciona métodos para analizarlo y procesarlo.
- `JWTClaimsSet`: Contiene las reclamaciones del payload del JWT.
- `ParseException`: Se lanza si la cadena JWT está mal formada o no se puede analizar.
- `Date`: Se utiliza para representar los tiempos de expiración y emisión.

### 2. **Análisis del JWT**
- El método `SignedJWT.parse(jwtString)` toma una cadena JWT (por ejemplo, `header.payload.signature`) y devuelve un objeto `SignedJWT`. Si el JWT es inválido, lanza una `ParseException`.

### 3. **Acceso a las Reclamaciones**
- `signedJWT.getJWTClaimsSet()` recupera el conjunto de reclamaciones, que contiene todas las reclamaciones del payload del JWT.

### 4. **Extracción de Reclamaciones Específicas**
- **`getExpirationTime()`**: Devuelve la reclamación `exp` como un objeto `Date` (o `null` si no está presente). Representa cuándo expira el token.
- **`getIssueTime()`**: Devuelve la reclamación `iat` como un objeto `Date` (o `null` si no está presente). Indica cuándo se emitió el token.
- **`getSubject()`**: Devuelve la reclamación `sub` como un `String` (o `null` si no está presente), un ejemplo de otra reclamación estándar. También puedes usar `getClaim("clave")` para recuperar reclamaciones personalizadas como un `Object`.

### 5. **Manejo de Errores**
- El bloque try-catch asegura que si el JWT está mal formado o es inválido, el programa maneje el error de forma controlada imprimiendo un mensaje de error.

---

## Notas

- **JWTs Firmados vs. No Firmados**: Este ejemplo utiliza `SignedJWT` para tokens firmados. Si tienes un JWT no firmado, usa `PlainJWT.parse(jwtString)` en su lugar. Para un enfoque más genérico, puedes usar `JWTParser.parse(jwtString)` y luego verificar el tipo (`SignedJWT`, `PlainJWT`, etc.) usando instanceof.
- **Verificación de Firma**: Este código no verifica la firma del JWT. En un entorno de producción, debes verificar la firma usando `signedJWT.verify(verifier)` con una clave apropiada para garantizar la autenticidad del token.
- **Comprobaciones de Nulo**: Siempre verifica si es `null` al recuperar reclamaciones, ya que son opcionales y pueden no estar presentes en cada JWT.
- **Reclamaciones Personalizadas**: Para acceder a reclamaciones no estándar, usa `claimsSet.getClaim("nombreDeLaReclamacion")`, que devuelve un `Object` que puedes convertir (cast) al tipo apropiado (por ejemplo, `String`, `Integer`).

---

## Salida de Ejemplo

Para la cadena JWT de ejemplo anterior:
```
Fecha de expiración: Wed Jan 17 19:52:02 UTC 2018
Fecha de emisión: Wed Jan 17 19:50:22 UTC 2018
Sujeto: 1234567890
```

---

Este enfoque proporciona una forma simple y efectiva de extraer la fecha de expiración, la fecha de emisión y otras reclamaciones de un JWT utilizando la biblioteca `com.nimbusds.jwt`. ¡Reemplaza la `jwtString` con tu propio token y adapta el código a tus necesidades específicas!