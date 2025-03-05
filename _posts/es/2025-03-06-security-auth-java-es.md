---
audio: false
generated: true
lang: es
layout: post
title: Autenticación y Autorización en Java
translated: true
---

Para usar el paquete `javax.security.auth` en Java, es necesario entender que forma parte del marco de trabajo Java Authentication and Authorization Service (JAAS). Este paquete proporciona clases e interfaces para autenticar usuarios (verificar quiénes son) y autorizarlos (determinar qué pueden hacer). A continuación se presenta una guía paso a paso para usar `javax.security.auth` en un escenario de autenticación básica, como autenticar a un usuario con un nombre de usuario y una contraseña.

---

### **Visión General de Conceptos Clave**
Antes de sumergirse en los pasos, aquí hay una breve explicación de los componentes principales en `javax.security.auth`:

- **Subject**: Representa una entidad (por ejemplo, un usuario o servicio) que está siendo autenticada. Puede tener múltiples identidades (Principals) y credenciales (por ejemplo, contraseñas o certificados).
- **Principal**: Una identidad o rol asociado con un Subject, como un nombre de usuario o membresía en un grupo.
- **Credential**: Información utilizada para autenticar a un Subject, como una contraseña o una clave criptográfica.
- **LoginModule**: Un componente enchufable que realiza la lógica de autenticación (por ejemplo, verificar un nombre de usuario y una contraseña contra una base de datos).
- **LoginContext**: La clase central que coordina el proceso de autenticación utilizando uno o más LoginModules.
- **CallbackHandler**: Una interfaz para interactuar con el usuario, como solicitar un nombre de usuario y una contraseña.

Con estos conceptos en mente, exploremos cómo usar el paquete.

---

### **Pasos para Usar `javax.security.auth`**

#### **1. Configurar JAAS**
El proceso de autenticación depende de una configuración que especifica qué `LoginModule`(s) usar. Esto se puede definir en un archivo de configuración o de manera programática.

Por ejemplo, cree un archivo llamado `jaas.config` con el siguiente contenido:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: El nombre de la aplicación o contexto, que referenciará en su código.
- **`com.example.MyLoginModule`**: El nombre completo de su `LoginModule` personalizado (lo implementará más adelante).
- **`required`**: Una bandera que indica que este módulo debe tener éxito para que la autenticación pase. Otras banderas incluyen `requisite`, `sufficient` y `optional`, que permiten lógica más compleja con múltiples módulos.

Establezca la propiedad del sistema para apuntar a este archivo:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

Alternativamente, puede establecer la configuración de manera programática, pero un archivo es más sencillo para la mayoría de los casos.

#### **2. Implementar un CallbackHandler**
Un `CallbackHandler` recopila la entrada del usuario, como un nombre de usuario y una contraseña. Aquí hay una implementación simple usando la consola:

```java
import javax.security.auth.callback.*;
import java.io.*;

public class MyCallbackHandler implements CallbackHandler {
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                NameCallback nc = (NameCallback) callback;
                System.out.print(nc.getPrompt());
                nc.setName(System.console().readLine());
            } else if (callback instanceof PasswordCallback) {
                PasswordCallback pc = (PasswordCallback) callback;
                System.out.print(pc.getPrompt());
                pc.setPassword(System.console().readPassword());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

- **NameCallback**: Solicita y recupera el nombre de usuario.
- **PasswordCallback**: Solicita y recupera la contraseña (almacenada como un `char[]` por seguridad).

#### **3. Implementar un LoginModule**
Un `LoginModule` define la lógica de autenticación. A continuación se presenta un ejemplo básico que verifica contra un nombre de usuario y una contraseña codificados en el programa (en la práctica, usaría una base de datos o un servicio externo):

```java
import javax.security.auth.*;
import javax.security.auth.callback.*;
import javax.security.auth.login.*;
import javax.security.auth.spi.*;
import java.security.Principal;
import java.util.*;

public class MyLoginModule implements LoginModule {
    private Subject subject;
    private CallbackHandler callbackHandler;
    private boolean succeeded = false;

    // Inicializar el módulo
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // Realizar autenticación
    public boolean login() throws LoginException {
        if (callbackHandler == null) {
            throw new LoginException("No callback handler provided");
        }

        try {
            NameCallback nameCallback = new NameCallback("Username: ");
            PasswordCallback passwordCallback = new PasswordCallback("Password: ", false);
            callbackHandler.handle(new Callback[]{nameCallback, passwordCallback});

            String username = nameCallback.getName();
            char[] password = passwordCallback.getPassword();

            // Verificación codificada en el programa (reemplazar con lógica real en la práctica)
            if ("myuser".equals(username) && "mypassword".equals(new String(password))) {
                succeeded = true;
                return true;
            } else {
                succeeded = false;
                throw new FailedLoginException("Authentication failed");
            }
        } catch (Exception e) {
            throw new LoginException("Login error: " + e.getMessage());
        }
    }

    // Confirmar la autenticación (agregar Principals al Subject)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // Abortar el proceso de autenticación
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Cerrar sesión del Subject
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// Implementación simple de Principal
class MyPrincipal implements Principal {
    private String name;

    public MyPrincipal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

- **login()**: Usa el `CallbackHandler` para obtener credenciales y verifica.
- **commit()**: Si la autenticación tiene éxito, agrega un `Principal` al `Subject`.
- **abort()** y **logout()**: Manejan la limpieza o cancelación.

#### **4. Autenticar Usando LoginContext**
Ahora, use `LoginContext` para realizar la autenticación en su aplicación principal:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // Asegúrese de que la configuración JAAS esté establecida
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // Crear LoginContext con el nombre de la configuración y CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // Realizar autenticación
            lc.login();

            // Obtener el Subject autenticado
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // Imprimir los Principals del Subject
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // Cerrar sesión cuando termine
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: Enlaza con la configuración `"MyApp"` y usa `MyCallbackHandler`.
- **`lc.login()`**: Dispara el proceso de autenticación.
- **`lc.getSubject()`**: Recupera el `Subject` autenticado.

#### **5. Realizar Acciones Autorizadas (Opcional)**
Una vez autenticado, puede usar el `Subject` para ejecutar código con sus privilegios usando `Subject.doAs()`:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // Realizar acciones privilegiadas aquí
        return null;
    }
});
```

Esto es útil para la autorización, donde las acciones se restringen en función de los `Principals` del `Subject`.

---

### **Juntando Todo**
1. **Configuración**: Defina `jaas.config` con su `LoginModule`.
2. **CallbackHandler**: Implemente `MyCallbackHandler` para recopilar la entrada del usuario.
3. **LoginModule**: Implemente `MyLoginModule` con su lógica de autenticación.
4. **Código Principal**: Use `LoginContext` para autenticar y recuperar un `Subject`.
5. **Autorización**: Use `Subject.doAs()` para acciones privilegiadas si es necesario.

Cuando ejecute la clase `Main`, hará:
- Solicitar un nombre de usuario y una contraseña.
- Autenticar usando `MyLoginModule`.
- Imprimir el `Subject` y sus `Principals` si tiene éxito.

---

### **Notas Adicionales**
- **Uso en el Mundo Real**: Reemplace las credenciales codificadas en `MyLoginModule` con verificaciones contra una base de datos, LDAP o otro servicio. Java proporciona módulos estándar como `Krb5LoginModule` (Kerberos) o `JndiLoginModule` (LDAP), pero pueden requerir configuración adicional.
- **Múltiples LoginModules**: La configuración puede especificar múltiples módulos con banderas (`required`, `sufficient`, etc.) para crear flujos de autenticación complejos.
- **Seguridad**: Use prácticas seguras, como evitar `String` para contraseñas (use `char[]`) e integrarse con marcos de trabajo de seguridad existentes.

Esta guía cubre los conceptos básicos del uso de `javax.security.auth` para autenticación y autorización en Java!