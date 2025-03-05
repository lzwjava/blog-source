---
audio: false
generated: true
lang: es
layout: post
title: Autenticación SASL en Java
translated: true
---

Para usar el paquete `javax.security.sasl` en Java, necesitas aprovechar sus clases e interfaces para implementar mecanismos de Simple Authentication and Security Layer (SASL) para la autenticación y, opcionalmente, la seguridad de datos en aplicaciones cliente-servidor. Las clases principales involucradas son `Sasl`, `SaslClient` y `SaslServer`. A continuación se presenta una guía completa sobre cómo usar este paquete, incluyendo pasos y código de ejemplo tanto para la implementación del cliente como del servidor.

---

### **Descripción general de javax.security.sasl**
El paquete `javax.security.sasl` proporciona un marco para la autenticación SASL, comúnmente utilizado en protocolos como LDAP, IMAP o aplicaciones personalizadas. Incluye:
- **`Sasl`**: Una clase utilitaria con métodos estáticos para crear instancias de `SaslClient` y `SaslServer`.
- **`SaslClient`**: Representa el lado del cliente del proceso de autenticación SASL.
- **`SaslServer`**: Representa el lado del servidor del proceso de autenticación SASL.
- **`CallbackHandler`**: Una interfaz que implementas para manejar las devoluciones de llamada de autenticación (por ejemplo, proporcionar nombres de usuario o contraseñas).

El proceso implica crear un `SaslClient` o `SaslServer`, proporcionar un manejador de devoluciones de llamada para gestionar los datos de autenticación y participar en un intercambio de desafío-respuesta hasta que la autenticación esté completa.

---

### **Pasos para usar javax.security.sasl**

#### **1. Determinar tu rol (Cliente o Servidor)**
Decide si tu aplicación actúa como cliente (autenticándose en un servidor) o como servidor (autenticando a un cliente). Esto determina si usarás `SaslClient` o `SaslServer`.

#### **2. Elegir un mecanismo SASL**
SASL soporta varios mecanismos, como:
- `PLAIN`: Autenticación simple de nombre de usuario/contraseña (sin cifrado).
- `DIGEST-MD5`: Basado en contraseña con desafío-respuesta.
- `GSSAPI`: Autenticación basada en Kerberos.

Selecciona un mecanismo soportado tanto por el cliente como por el servidor. Para simplificar, esta guía usa el mecanismo `PLAIN` como ejemplo.

#### **3. Implementar un CallbackHandler**
Un `CallbackHandler` es necesario para proporcionar o verificar las credenciales de autenticación. Necesitarás implementar la interfaz `javax.security.auth.callback.CallbackHandler`.

- **Para un Cliente**: Proporcionar credenciales como nombre de usuario y contraseña.
- **Para un Servidor**: Verificar las credenciales del cliente o proporcionar datos de autenticación del lado del servidor.

Aquí tienes un ejemplo de un `CallbackHandler` del lado del cliente para el mecanismo `PLAIN`:

```java
import javax.security.auth.callback.*;
import java.io.IOException;

public class ClientCallbackHandler implements CallbackHandler {
    private final String username;
    private final String password;

    public ClientCallbackHandler(String username, String password) {
        this.username = username;
        this.password = password;
    }

    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                ((NameCallback) callback).setName(username);
            } else if (callback instanceof PasswordCallback) {
                ((PasswordCallback) callback).setPassword(password.toCharArray());
            } else {
                throw new UnsupportedCallbackException(callback, "Devolución de llamada no soportada");
            }
        }
    }
}
```

Para el servidor, podrías verificar las credenciales contra una base de datos:

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // Obtener la contraseña esperada para el nombre de usuario de una base de datos
            } else if (callback instanceof PasswordCallback) {
                // Establecer la contraseña esperada para la verificación
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. Implementación del lado del cliente**
Para autenticarse como cliente:

1. **Crear un SaslClient**:
   Usa `Sasl.createSaslClient` con el mecanismo, protocolo, nombre del servidor, propiedades y manejador de devoluciones de llamada.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // Opcional; null si es el mismo que el ID de autenticación
   String protocol = "ldap"; // p. ej., "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // Propiedades opcionales, p. ej., QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **Manejar el intercambio de desafío-respuesta**:
   - Verificar una respuesta inicial (común en mecanismos de cliente primero como `PLAIN`).
   - Enviar respuestas al servidor y procesar desafíos hasta que la autenticación se complete.

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // Enviar respuesta al servidor (específico del protocolo, p. ej., a través de socket o LDAP BindRequest)
   }

   // Leer desafío del servidor (específico del protocolo)
   byte[] challenge = /* leer del servidor */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // Enviar respuesta al servidor
       if (sc.isComplete()) break;
       challenge = /* leer siguiente desafío del servidor */;
   }

   // La autenticación está completa; verificar el éxito mediante medios específicos del protocolo
   ```

   Para `PLAIN`, el cliente envía las credenciales en la respuesta inicial y el servidor generalmente responde con éxito o fracaso sin desafíos adicionales.

#### **5. Implementación del lado del servidor**
Para autenticar a un cliente como servidor:

1. **Crear un SaslServer**:
   Usa `Sasl.createSaslServer` con el mecanismo, protocolo, nombre del servidor, propiedades y manejador de devoluciones de llamada.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslServer;
   import java.util.HashMap;

   String mechanism = "PLAIN";
   String protocol = "ldap";
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null;
   CallbackHandler cbh = new ServerCallbackHandler();

   SaslServer ss = Sasl.createSaslServer(mechanism, protocol, serverName, props, cbh);
   ```

2. **Manejar el intercambio de desafío-respuesta**:
   - Procesar la respuesta inicial del cliente y generar desafíos hasta que la autenticación se complete.

   ```java
   byte[] response = /* leer respuesta inicial del cliente */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // Enviar desafío al cliente (específico del protocolo)

   while (!ss.isComplete()) {
       response = /* leer siguiente respuesta del cliente */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // Autenticación completa
           break;
       }
       // Enviar desafío al cliente
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // Proseguir con el usuario autorizado
   }
   ```

   Para `PLAIN`, el servidor verifica las credenciales en la respuesta inicial y completa la autenticación sin desafíos adicionales.

#### **6. Opcional: Usar capas de seguridad**
Si el mecanismo (p. ej., `DIGEST-MD5`) soporta una capa de seguridad:
- Usa `sc.wrap()` y `sc.unwrap()` en el cliente, o `ss.wrap()` y `ss.unwrap()` en el servidor, para cifrar/descifrar mensajes después de la autenticación.
- `PLAIN` no soporta capas de seguridad.

---

### **Puntos clave**
- **Integración**: Incrustar el intercambio SASL en el protocolo de comunicación de tu aplicación (p. ej., solicitudes LDAP Bind, comandos IMAP AUTHENTICATE).
- **Manejo de errores**: Envolver el código en bloques try-catch para manejar `SaslException` y otros posibles errores.
- **Propiedades**: Usar el mapa `props` para configurar opciones como la calidad de protección (`"javax.security.sasl.qop"`) si es soportada por el mecanismo.

---

### **Caso de uso de ejemplo**
Para un cliente LDAP que se autentica con `PLAIN`:
1. Crear un `SaslClient` con el mecanismo `PLAIN`.
2. Enviar una solicitud LDAP `BindRequest` con el mecanismo y la respuesta inicial (`sc.evaluateChallenge(new byte[0])`).
3. Procesar la respuesta `BindResponse` del servidor para confirmar el éxito.

Para un protocolo personalizado, reemplaza los pasos específicos de LDAP con los comandos de autenticación de tu protocolo.

---

Siguiendo estos pasos, puedes usar `javax.security.sasl` de manera efectiva para implementar la autenticación SASL en tu aplicación Java, adaptando el proceso a tu mecanismo y protocolo seleccionados.