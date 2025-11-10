---
audio: false
generated: true
lang: es
layout: post
title: Actualización de Guice para Corregir Advertencia de Seguridad
translated: true
type: note
---

La advertencia que estás viendo:

```
WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::staticFieldBase has been called by com.google.inject.internal.aop.HiddenClassDefiner (file:/opt/homebrew/Cellar/maven/3.9.10/libexec/lib/guice-5.1.0-classes.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.inject.internal.aop.HiddenClassDefiner
WARNING: sun.misc.Unsafe::staticFieldBase will be removed in a future release
```

Esta es una **advertencia de la Java Virtual Machine (JVM)**, no directamente de tu código. Significa que una librería que estás usando (en este caso, Guice, específicamente el `guice-5.1.0-classes.jar`) está llamando internamente a un método (`staticFieldBase`) de `sun.misc.Unsafe`.

`sun.misc.Unsafe` es una API interna de Java, destinada a operaciones de bajo nivel dentro del propio JDK. No es parte de la API estándar de Java y se desaconseja su uso porque puede llevar a un comportamiento inestable o indefinido y está sujeto a cambios o eliminación en futuras versiones de Java. La JVM te está advirtiendo que este método en particular está "terminalmente obsoleto" y será eliminado, lo que significa que eventualmente hará que tu aplicación falle si la librería continúa usándolo sin una alternativa.

**Cómo "eliminar" esta advertencia:**

No puedes "eliminarla" directamente cambiando tu código, ya que el uso está dentro de una librería de terceros (Guice). Esto es lo que puedes hacer, listado en orden de preferencia:

1.  **Actualizar Guice (Más Recomendado):**
    La mejor y más sostenible solución es actualizar a una versión más nueva de Guice que ya no use `sun.misc.Unsafe` o que haya migrado a las APIs estándar de Java como `VarHandle` (introducido en JDK 9) o la Foreign Function & Memory API (JEP 454, estándar en JDK 22).

    Mirando la versión `guice-5.1.0-classes.jar`, parece que estás usando Guice 5.1.0. Revisa los lanzamientos oficiales de Guice y su documentación en busca de actualizaciones que aborden específicamente el uso de `sun.misc.Unsafe` en versiones más nuevas de Java. A menudo, los mantenedores de las librerías están al tanto de estas obsolescencias y proporcionan versiones actualizadas.

      * **Acción:** Modifica tu `pom.xml` para usar una versión más nueva de Guice. Necesitarás encontrar la última versión estable de Guice que sea compatible con tu versión de Java (JDK 21 en tu caso).

    ```xml
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>LATEST_GUICE_VERSION</version> </dependency>
    ```

    Es posible que necesites incluir `guice-assistedinject` u otros módulos de Guice si tu proyecto los usa.

2.  **Suprimir la Advertencia (Solución Temporal - No Recomendada a Largo Plazo):**
    Aunque no deberías depender de esto a largo plazo, puedes suprimir la advertencia en tiempo de ejecución si es puramente cosmética y no obstaculiza la funcionalidad de tu aplicación *por ahora*. Esto se hace mediante argumentos de línea de comandos de la JVM.

    Para JDK 24 (tu objetivo actual es 21, pero es bueno saberlo a medida que Java progresa), el valor por defecto es `warn`. Para suprimirla, puedes establecerlo explícitamente en `allow`:

    Puedes agregar esto a tu configuración de `exec-maven-plugin`:

    ```xml
    <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
            <executable>bash</executable>
            <arguments>
                <argument>-c</argument>
                <argument>java --add-opens java.base/sun.misc=ALL-UNNAMED --sun-misc-unsafe-memory-access=allow -cp ${project.build.directory}/classes com.lzw.solutions.uva.${problem}.Main &lt; src/main/resources/uva/${problem}/1.in</argument>
            </arguments>
        </configuration>
    </plugin>
    ```

    *Auto-corrección:* La advertencia principal es sobre `sun.misc.Unsafe::staticFieldBase` estando "terminalmente obsoleto", no sobre acceso reflectivo ilegal. Por lo tanto, `--add-opens java.base/sun.misc=ALL-UNNAMED` podría no ser necesario aquí a menos que también estuvieras recibiendo advertencias de "Illegal reflective access". La bandera más directa para la advertencia de "terminalmente obsoleto" es `--sun-misc-unsafe-memory-access=allow`.

    **Sin embargo, esto es una solución temporal.** Esta bandera simplemente le dice a la JVM que permita el uso de los métodos de `sun.misc.Unsafe` sin imprimir la advertencia. *No resuelve* el problema subyacente de que `sun.misc.Unsafe` eventualmente será eliminado, y tu aplicación podría fallar en futuras versiones del JDK.

3.  **Reportar a los Mantenedores de Guice (Ya Sugerido por la Advertencia):**
    La propia advertencia sugiere "Please consider reporting this to the maintainers of class `com.google.inject.internal.aop.HiddenClassDefiner`." Aunque estás usando una versión específica, si puedes confirmar que este problema persiste en las últimas versiones de Guice (lo cual probablemente no debería, ya que suelen abordar estos problemas), reportarlo sería beneficioso para la comunidad.

**En resumen, el mejor curso de acción es actualizar tu dependencia de Guice.** La API `sun.misc.Unsafe` es un objetivo en movimiento, y las librerías necesitan adaptarse a las APIs más nuevas, seguras y oficialmente soportadas proporcionadas por Java.