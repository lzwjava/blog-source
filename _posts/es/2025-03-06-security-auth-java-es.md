---
audio: false
generated: true
lang: es
layout: post
title: Autenticación y Autorización en Java
translated: true
type: note
---

Para utilizar el paquete `javax.security.auth` en Java, es necesario entender que forma parte del framework Java Authentication and Authorization Service (JAAS). Este paquete proporciona clases e interfaces para autenticar usuarios (verificar quiénes son) y autorizarlos (determinar qué pueden hacer). A continuación se presenta una guía paso a paso para usar `javax.security.auth` en un escenario de autenticación básico, como autenticar a un usuario con un nombre de usuario y contraseña.

---

### **Descripción General de Conceptos Clave**
Antes de profundizar en los pasos, aquí hay una breve explicación de los componentes principales en `javax.security.auth`:

- **Subject**: Representa una entidad (por ejemplo, un usuario o servicio) que se está autenticando. Puede tener múltiples identidades (Principals) y credenciales (por ejemplo, contraseñas o certificados).
- **Principal**: Una identidad o rol asociado a un Subject, como un nombre de usuario o membresía a un grupo.
- **Credential**: Información utilizada para autenticar un Subject, como una contraseña o una clave criptográfica.
- **LoginModule**: Un componente conectable que ejecuta la lógica de autenticación (por ejemplo, verificar un nombre de usuario y contraseña contra una base de datos).
- **LoginContext**: La clase central que coordina el proceso de autenticación utilizando uno o más LoginModules.
- **CallbackHandler**: Una interfaz para interactuar con el usuario, como solicitar un nombre de usuario y contraseña.

Teniendo en cuenta estos conceptos, exploremos cómo usar el paquete.

---

### **Pasos para Usar `javax.security.auth`**

#### **1. Configurar una Configuración JAAS**
El proceso de autenticación depende de una configuración que especifica qué `LoginModule`(s) usar. Esto se puede definir en un archivo de configuración o mediante programación.

Por ejemplo, crea un archivo llamado `jaas.config` con el siguiente contenido:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: El nombre de la aplicación o contexto, al que harás referencia en tu código.
- **`com.example.MyLoginModule`**: El nombre completo de tu `LoginModule` personalizado (lo implementarás más adelante).
- **`required`**: Un indicador que señala que este módulo debe tener éxito para que la autenticación sea exitosa. Otros indicadores incluyen `requisite`, `sufficient` y `optional`, que permiten lógicas más complejas con múltiples módulos.

Establece la propiedad del sistema para que apunte a este archivo:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

Alternativamente, puedes establecer la configuración mediante programación, pero un archivo es más simple para la mayoría de los casos.

#### **2. Implementar un CallbackHandler**
Un `CallbackHandler` recopila información del usuario, como un nombre de usuario y contraseña. Aquí hay una implementación simple usando la consola:

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
Un `LoginModule` define la lógica de autenticación. A continuación se muestra un ejemplo básico que verifica contra un nombre de usuario y contraseña codificados (en la práctica, usarías una base de datos o un servicio externo):

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

    // Realizar la autenticación
    public boolean login() throws LoginException {
        if (callbackHandler == null) {
            throw new LoginException("No callback handler provided");
        }

        try {
            NameCallback nameCallback = new NameCallback("Usuario: ");
            PasswordCallback passwordCallback = new PasswordCallback("Contraseña: ", false);
            callbackHandler.handle(new Callback[]{nameCallback, passwordCallback});

            String username = nameCallback.getName();
            char[] password = passwordCallback.getPassword();

            // Verificación codificada (reemplazar con lógica real en la práctica)
            if ("myuser".equals(username) && "mypassword".equals(new String(password))) {
                succeeded = true;
                return true;
            } else {
                succeeded = false;
                throw new FailedLoginException("Fallo de autenticación");
            }
        } catch (Exception e) {
            throw new LoginException("Error de inicio de sesión: " + e.getMessage());
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

    // Cerrar la sesión del Subject
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

- **login()**: Utiliza el `CallbackHandler` para obtener las credenciales y las verifica.
- **commit()**: Si la autenticación tiene éxito, agrega un `Principal` al `Subject`.
- **abort()** y **logout()**: Manejan la limpieza o cancelación.

#### **4. Autenticar Usando LoginContext**
Ahora, usa `LoginContext` para realizar la autenticación en tu aplicación principal:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // Asegurar que la configuración JAAS esté establecida
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // Crear LoginContext con el nombre de configuración y el CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // Realizar la autenticación
            lc.login();

            // Obtener el Subject autenticado
            Subject subject = lc.getSubject();
            System.out.println("Subject autenticado: " + subject);

            // Imprimir los Principals del Subject
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // Cerrar sesión cuando termine
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Fallo de autenticación: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: Se vincula a la configuración `"MyApp"` y utiliza `MyCallbackHandler`.
- **`lc.login()`**: Activa el proceso de autenticación.
- **`lc.getSubject()`**: Recupera el `Subject` autenticado.

#### **5. Realizar Acciones Autorizadas (Opcional)**
Una vez autenticado, puedes usar el `Subject` para ejecutar código con sus privilegios usando `Subject.doAs()`:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Ejecutando como: " + Subject.getSubject(java.security.AccessController.getContext()));
        // Realizar acciones privilegiadas aquí
        return null;
    }
});
```

Esto es útil para la autorización, donde las acciones están restringidas en función de los `Principals` del `Subject`.

---

### **Integrando Todo**
1. **Configuración**: Define `jaas.config` con tu `LoginModule`.
2. **CallbackHandler**: Implementa `MyCallbackHandler` para recopilar la entrada del usuario.
3. **LoginModule**: Implementa `MyLoginModule` con tu lógica de autenticación.
4. **Código Principal**: Usa `LoginContext` para autenticar y recuperar un `Subject`.
5. **Autorización**: Usa `Subject.doAs()` para acciones privilegiadas si es necesario.

Cuando ejecutes la clase `Main`, hará lo siguiente:
- Solicitará un nombre de usuario y contraseña.
- Autenticará usando `MyLoginModule`.
- Imprimirá el `Subject` y sus `Principals` si es exitoso.

---

### **Notas Adicionales**
- **Uso en el Mundo Real**: Reemplaza las credenciales codificadas en `MyLoginModule` con verificaciones contra una base de datos, LDAP u otro servicio. Java proporciona módulos estándar como `Krb5LoginModule` (Kerberos) o `JndiLoginModule` (LDAP), pero pueden requerir configuración adicional.
- **Múltiples LoginModules**: La configuración puede especificar múltiples módulos con indicadores (`required`, `sufficient`, etc.) para crear flujos de autenticación complejos.
- **Seguridad**: Utiliza prácticas seguras, como evitar `String` para contraseñas (usa `char[]`) e integrar con frameworks de seguridad existentes.

¡Esta guía cubre los conceptos básicos del uso de `javax.security.auth` para autenticación y autorización en Java!