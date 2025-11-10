---
audio: false
generated: true
lang: es
layout: post
title: Detección de Sangría en Checkstyle
translated: true
type: note
---

Entiendo que te preguntes por qué Checkstyle no detecta la falta de sangría antes de la sentencia `System.out.println` en tu método `logAfter`. Analicemos esto paso a paso para identificar el problema y solucionarlo.

### ¿Por qué Checkstyle no detecta el problema de sangría?
Checkstyle utiliza módulos específicos para hacer cumplir los estándares de codificación, y para la sangría, depende del módulo `Indentation`. Si este módulo no está configurado correctamente o no está incluido en tu configuración de Checkstyle, no detectará errores de sangría como el de tu código.

Aquí está tu código actual:

```java
package org.lzwjava;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
    System.out.println("Method executed: " + joinPoint.getSignature());  // Sin sangría
    }
}
```

Según las convenciones estándar de Java, las sentencias dentro de un método (como `System.out.println`) deben tener sangría respecto a la declaración del método. En tu código, la línea `System.out.println` no tiene sangría, lo que Checkstyle debería marcar como un error si está configurado correctamente. Estas son las razones más probables por las que no se detecta:

1. **El módulo `Indentation` no está incluido** en tu archivo de configuración de Checkstyle (por ejemplo, `checks.xml`).
2. **El módulo está incluido pero mal configurado**, por lo que no aplica las reglas de sangría esperadas.
3. **Tu configuración excluye ciertos archivos o paquetes**, impidiendo que la verificación se ejecute sobre este código.
4. **Hay un problema con cómo se ejecuta Checkstyle** (por ejemplo, a través de Maven o un IDE), que anula el comportamiento esperado.

Abordemos estas posibilidades para que funcione.

---

### Paso 1: Verificar el módulo `Indentation` en tu configuración
Primero, revisa tu archivo de configuración de Checkstyle (probablemente `checks.xml`) para ver si el módulo `Indentation` está incluido. Así es cómo:

1. **Localiza tu archivo `checks.xml`**. Normalmente está en el directorio de tu proyecto (por ejemplo, `/home/lzw/Projects/blog-server/checks.xml` si estás usando una configuración similar).
2. **Busca el módulo `Indentation`** dentro de la sección `TreeWalker`. Debería verse así:

   ```xml
   <module name="TreeWalker">
       <!-- Otras comprobaciones -->
       <module name="Indentation">
           <property name="basicOffset" value="4"/>  <!-- 4 espacios por nivel de sangría -->
           <property name="lineWrappingIndentation" value="4"/>  <!-- Opcional: para líneas partidas -->
       </module>
       <!-- Otras comprobaciones -->
   </module>
   ```

   - **Si no ves este módulo**, ese es el problema: Checkstyle no está verificando la sangría en absoluto.
   - **Si está ahí**, verifica que `basicOffset` tenga un valor razonable (por ejemplo, 4 espacios, que es el estándar para Java).

---

### Paso 2: Añadir o corregir el módulo `Indentation`
Si el módulo falta o no está configurado correctamente, así es cómo solucionarlo:

#### Si falta: Añade el módulo `Indentation`
Añade lo siguiente dentro de la sección `TreeWalker` de tu `checks.xml`:

```xml
<module name="Indentation">
    <property name="basicOffset" value="4"/>  <!-- 4 espacios es lo típico -->
    <property name="lineWrappingIndentation" value="4"/>
</module>
```

#### Si está presente: Verifica la configuración
Asegúrate de que:
- `basicOffset` esté configurado con el número de espacios que esperas para la sangría (por ejemplo, 4).
- No haya propiedades que deshabiliten o anulen la verificación de manera que se omita tu código.

Guarda el archivo después de hacer los cambios.

---

### Paso 3: Comprobar si hay exclusiones
A veces, las configuraciones de Checkstyle excluyen ciertos archivos o paquetes. En tu `checks.xml`, busca:
- Un `SuppressionFilter` o `SuppressionCommentFilter` que pueda estar omitiendo el paquete `org.lzwjava` o este archivo específico.
- Cualquier patrón que excluya archivos `.java` o directorios específicos.

Si encuentras una exclusión que afecte a tu código, elimínala o ajústala para que `DebugAspect.java` sea verificado.

---

### Paso 4: Probar la solución
Después de actualizar tu configuración, ejecuta Checkstyle nuevamente. Si estás usando Maven, por ejemplo:

```bash
mvn clean checkstyle:check
```

Revisa la salida. Deberías ver un error como:

```
[ERROR] DebugAspect.java:13: 'System.out.println' debe tener una sangría de +4 espacios respecto a su bloque contenedor.
```

Esto indicaría que Checkstyle ahora detecta la falta de sangría. Como referencia, así es como *debería* verse tu código con la sangría correcta:

```java
@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());  // Sangría de 4 espacios
    }
}
```

---

### Paso 5: Resolución de problemas si aún no funciona
Si Checkstyle aún no marca el problema:
- **Ejecutar con Salida de Depuración**: Usa un comando detallado para ver qué está haciendo Checkstyle:
  ```bash
  mvn -X checkstyle:check
  ```
  Busca mensajes sobre el módulo `Indentation` o archivos omitidos.
- **Probar con una Configuración Mínima**: Crea un `checks.xml` temporal con solo la verificación `Indentation`:
  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE module PUBLIC
      "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
      "https://checkstyle.org/dtds/configuration_1_3.dtd">
  <module name="Checker">
      <module name="TreeWalker">
          <module name="Indentation">
              <property name="basicOffset" value="4"/>
          </module>
      </module>
  </module>
  ```
  Dirige Checkstyle a este archivo y prueba de nuevo para aislar el problema.
- **Revisa tu Configuración**: Si estás ejecutando Checkstyle a través de un IDE (como IntelliJ o Eclipse), asegúrate de que el IDE esté usando el `checks.xml` actualizado y no una configuración antigua o separada.

---

### Conclusión
Checkstyle no detecta la falta de sangría porque es probable que el módulo `Indentation` falte o esté mal configurado en tu `checks.xml`. Al añadir o corregir este módulo y asegurarte de que no se apliquen exclusiones, Checkstyle debería marcar la falta de sangría antes de `System.out.println`. Actualiza tu configuración como se muestra, vuelve a ejecutar Checkstyle y deberías ver el error reportado como se espera. ¡Avísame si necesitas ayuda con los siguientes pasos!