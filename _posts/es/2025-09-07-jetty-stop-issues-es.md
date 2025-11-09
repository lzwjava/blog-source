---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Corrección de Problemas de Detención de Jetty Bifurcado
translated: true
type: note
---

En realidad hiciste la mayoría de las cosas bien—el bloqueo casi siempre se debe a que **el objetivo de stop no puede alcanzar el Jetty bifurcado** (stopHost/port/key scope incorrectos) o porque **`run-forked` mantiene Maven adjunto** inesperadamente. Dos soluciones sólidas a continuación; elige una.

### Opción A — Patrón confiable: `jetty:start` (daemon) + `jetty:stop`

Esto evita `run-forked` por completo y es el más estable para ciclos de vida de pruebas de integración.

**Qué cambiar**

1. Fija la versión del plugin y usa `start` con `daemon=true` en `pre-integration-test`.
2. Mantén tus pruebas de integración de Python en `integration-test`.
3. Usa `stop` en `post-integration-test`.
4. Proporciona los *mismos* `stopHost/stopPort/stopKey` en **ambas** ejecuciones.

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <configuration>
    <httpConnector>
      <port>8080</port>
      <host>127.0.0.1</host>
    </httpConnector>
  </configuration>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>start</goal>
      </goals>
      <configuration>
        <daemon>true</daemon>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**Por qué esto soluciona el “bloqueo”**

* `daemon=true` hace que `start` devuelva el control a Maven inmediatamente, para que tus pruebas de integración puedan ejecutarse.
* Coincidir `stopHost/stopPort/stopKey` garantiza que el objetivo `stop` alcance el mismo Jetty.
* No hay dependencia del comportamiento del hilo monitor de `run-forked`.

---

### Opción B — Mantener `run-forked`, pero hacer que stop funcione realmente

Si prefieres `run-forked`, las dificultades comunes son:

* Los valores predeterminados de `stopHost` pueden diferir de cómo el proceso hijo se enlaza (IPv6 vs IPv4).
* `stopPort/stopKey` solo se configuran en la ejecución de inicio pero **no** se reflejan en la ejecución de stop.
* El proceso hijo no expone un manejador de stop si la configuración está mal ubicada.

**Ajusta la configuración así:**

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>run-forked</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>

        <httpConnector>
          <host>127.0.0.1</host>
          <port>8080</port>
        </httpConnector>

        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**Barreras de protección adicionales**

* Añade `-Djava.net.preferIPv4Stack=true` a los `jvmArgs` del proceso hijo si tu macOS/Java elige IPv6 y el objetivo stop usa IPv4:

  ```
  <jvmArgs>
    -Djava.net.preferIPv4Stack=true
    -javaagent:...
  </jvmArgs>
  ```
* Asegúrate de que nada más esté usando el puerto `8081`. Si es así, cambia tanto el inicio como el stop a otro puerto libre.
* Si tus pruebas de integración fallan o se cuelgan, `post-integration-test` puede no ejecutarse nunca; en ese caso, añade un plan de respaldo de terminación en la fase `verify` (ver más abajo).

---

### Red de seguridad opcional — terminar el proceso hijo si `stop` falla

Añade un pequeño ayudante para terminar forzosamente el Jetty bifurcado mediante el PID escrito en un archivo:

1. En la configuración de `run-forked`/`start`:

```
<pidFile>${project.build.directory}/jetty.pid</pidFile>
```

2. Después de `post-integration-test`, añade un `exec-maven-plugin` en `verify` que verifique el archivo pid y elimine el proceso si todavía está en ejecución.

---

### Un par de notas menores de tu registro

* `No Spring WebApplicationInitializer types detected` es normal si usas `web.xml` + DispatcherServlet; no está relacionado con el bloqueo de stop.
* Considera mover las pruebas de integración a **maven-failsafe-plugin** (se enlaza a `integration-test`/`verify`) y mantener las pruebas unitarias en surefire. Tu enfoque actual con `exec-maven-plugin` funciona, pero failsafe se integra mejor con el ciclo de vida de las pruebas de integración.

---

Si quieres, pega tu bloque de plugin de Jetty **completo** + cualquier mirror de `settings.xml` (para la ruta del repositorio local) y adaptaré el diff mínimo exacto para tu repositorio.