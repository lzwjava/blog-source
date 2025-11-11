---
audio: false
generated: true
lang: es
layout: post
title: Autenticación SASL en Java
translated: true
type: note
---

Para usar el paquete `javax.security.sasl` en Java, necesitas aprovechar sus clases e interfaces para implementar mecanismos de Simple Authentication and Security Layer (SASL) para autenticación y, opcionalmente, seguridad de datos en aplicaciones cliente-servidor. Las clases principales involucradas son `Sasl`, `SaslClient` y `SaslServer`. A continuación se presenta una guía completa sobre cómo usar este paquete, incluyendo pasos y código de ejemplo para implementaciones tanto del cliente como del servidor.

---

### **Descripción General de javax.security.sasl**
El paquete `javax.security.sasl` proporciona un framework para la autenticación SASL, comúnmente utilizado en protocolos como LDAP, IMAP o aplicaciones personalizadas. Incluye:
- **`Sasl`**: Una clase de utilidad con métodos estáticos para crear instancias de `SaslClient` y `SaslServer`.
- **`SaslClient`**: Representa el lado del cliente en el proceso de autenticación SASL.
- **`SaslServer`**: Representa el lado del servidor en el proceso de autenticación SASL.
- **`CallbackHandler`**: Una interfaz que implementas para manejar callbacks de autenticación (por ejemplo, proporcionar nombres de usuario o contraseñas).

El proceso implica crear un `SaslClient` o `SaslServer`, suministrar un callback handler para gestionar los datos de autenticación y participar en un intercambio de desafío-respuesta hasta que la autenticación se complete.

---

### **Pasos para Usar javax.security.sasl**

#### **1. Determina Tu Rol (Cliente o Servidor)**
Decide si tu aplicación actúa como un cliente (autenticándose ante un servidor) o como un servidor (autenticando a un cliente). Esto determina si usarás `SaslClient` o `SaslServer`.

#### **2. Elige un Mecanismo SASL**
SASL admite varios mecanismos, tales como:
- `PLAIN`: Autenticación simple con nombre de usuario y contraseña (sin cifrado).
- `DIGEST-MD5`: Basado en contraseña con desafío-respuesta.
- `GSSAPI`: Autenticación basada en Kerberos.

Selecciona un mecanismo admitido tanto por el cliente como por el servidor. Para simplificar, esta guía utiliza el mecanismo `PLAIN` como ejemplo.

#### **3. Implementa un CallbackHandler**
Se requiere un `CallbackHandler` para proporcionar o verificar las credenciales de autenticación. Necesitarás implementar la interfaz `javax.security.auth.callback.CallbackHandler`.

- **Para un Cliente**: Proporciona credenciales como nombre de usuario y contraseña.
- **Para un Servidor**: Verifica las credenciales del cliente o proporciona datos de autenticación del lado del servidor.

Aquí hay un ejemplo de un `CallbackHandler` del lado del cliente para el mecanismo `PLAIN`:

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
                throw new UnsupportedCallbackException(callback, "Callback no soportado");
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
                // Recuperar la contraseña esperada para el nombre de usuario desde una base de datos
            } else if (callback instanceof PasswordCallback) {
                // Establecer la contraseña esperada para su verificación
                ((PasswordCallback) callback).setPassword("contraseñaEsperada".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. Implementación del Lado del Cliente**
Para autenticarse como cliente:

1. **Crea un SaslClient**:
   Usa `Sasl.createSaslClient` con el mecanismo, protocolo, nombre del servidor, propiedades y el callback handler.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // Opcional; null si es el mismo que el ID de autenticación
   String protocol = "ldap"; // ej., "ldap", "imap"
   String serverName = "miservidor.ejemplo.com";
   HashMap<String, Object> props = null; // Propiedades opcionales, ej., QoP
   CallbackHandler cbh = new ClientCallbackHandler("usuario", "contraseña");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **Maneja el Intercambio de Desafío-Respuesta**:
   - Verifica si hay una respuesta inicial (común en mecanismos donde el cliente inicia como `PLAIN`).
   - Envía respuestas al servidor y procesa los desafíos hasta que la autenticación se complete.

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // Enviar respuesta al servidor (específico del protocolo, ej., via socket o LDAP BindRequest)
   }

   // Recibir desafío del servidor (específico del protocolo)
   byte[] challenge = /* leer del servidor */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // Enviar respuesta al servidor
       if (sc.isComplete()) break;
       challenge = /* leer siguiente desafío del servidor */;
   }

   // La autenticación está completa; verificar el éxito por medios específicos del protocolo
   ```

   Para `PLAIN`, el cliente envía las credenciales en la respuesta inicial, y el servidor típicamente responde con éxito o fallo sin desafíos adicionales.

#### **5. Implementación del Lado del Servidor**
Para autenticar a un cliente como servidor:

1. **Crea un SaslServer**:
   Usa `Sasl.createSaslServer` con el mecanismo, protocolo, nombre del servidor, propiedades y el callback handler.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslServer;
   import java.util.HashMap;

   String mechanism = "PLAIN";
   String protocol = "ldap";
   String serverName = "miservidor.ejemplo.com";
   HashMap<String, Object> props = null;
   CallbackHandler cbh = new ServerCallbackHandler();

   SaslServer ss = Sasl.createSaslServer(mechanism, protocol, serverName, props, cbh);
   ```

2. **Maneja el Intercambio de Desafío-Respuesta**:
   - Procesa la respuesta inicial del cliente y genera desafíos hasta que la autenticación se complete.

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
       // Proceder con el usuario autorizado
   }
   ```

   Para `PLAIN`, el servidor verifica las credenciales en la respuesta inicial y completa la autenticación sin desafíos adicionales.

#### **6. Opcional: Usa Capas de Seguridad**
Si el mecanismo (ej., `DIGEST-MD5`) admite una capa de seguridad:
- Usa `sc.wrap()` y `sc.unwrap()` en el cliente, o `ss.wrap()` y `ss.unwrap()` en el servidor, para cifrar/descifrar mensajes después de la autenticación.
- `PLAIN` no admite capas de seguridad.

---

### **Puntos Clave**
- **Integración**: Integra el intercambio SASL en el protocolo de comunicación de tu aplicación (por ejemplo, solicitudes LDAP Bind, comandos IMAP AUTHENTICATE).
- **Manejo de Errores**: Envuelve el código en bloques try-catch para manejar `SaslException` y otros errores potenciales.
- **Propiedades**: Usa el mapa `props` para configurar opciones como la calidad de protección (`"javax.security.sasl.qop"`) si el mecanismo lo admite.

---

### **Ejemplo de Caso de Uso**
Para un cliente LDAP que se autentica con `PLAIN`:
1. Crea un `SaslClient` con el mecanismo `PLAIN`.
2. Envía una `BindRequest` de LDAP con el mecanismo y la respuesta inicial (`sc.evaluateChallenge(new byte[0])`).
3. Procesa la `BindResponse` del servidor para confirmar el éxito.

Para un protocolo personalizado, reemplaza los pasos específicos de LDAP con los comandos de autenticación de tu protocolo.

---

Siguiendo estos pasos, puedes usar efectivamente `javax.security.sasl` para implementar autenticación SASL en tu aplicación Java, adaptando el proceso a tu mecanismo y protocolo elegidos.