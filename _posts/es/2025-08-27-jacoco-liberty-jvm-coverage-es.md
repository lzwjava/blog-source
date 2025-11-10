---
audio: false
generated: true
image: false
lang: es
layout: post
title: JaCoCo para Cobertura JVM de Liberty
translated: true
type: note
---

Puedes hacerlo—conecta JaCoCo a la **JVM de Liberty** que ejecuta tu EAR. La clave es: JaCoCo debe estar dentro de la misma JVM que Liberty, no en tu ejecutor de Python.

Aquí tienes configuraciones confiables (elige una).

---

## 1) Simple y robusto: escribir a archivo al salir de la JVM

**Cuándo usarlo:** puedes detener el servidor Liberty después de las pruebas.

1.  **Hacer disponible el jar del agente** (una vez en tu build)

```xml
<!-- copiar el agente jacoco en target/jacoco/jacocoagent.jar -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-dependency-plugin</artifactId>
  <version>3.6.1</version>
  <executions>
    <execution>
      <id>copy-jacoco-agent</id>
      <phase>prepare-package</phase>
      <goals><goal>copy</goal></goals>
      <configuration>
        <artifactItems>
          <artifactItem>
            <groupId>org.jacoco</groupId>
            <artifactId>org.jacoco.agent</artifactId>
            <version>0.8.12</version>
            <classifier>runtime</classifier>
            <destFileName>jacocoagent.jar</destFileName>
          </artifactItem>
        </artifactItems>
        <outputDirectory>${project.build.directory}/jacoco</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

2.  **Agregar una opción JVM de Liberty** (archivo: `wlp/usr/servers/<serverName>/jvm.options`)

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=file,append=false,includes=com.myco.*,excludes=org.slf4j.*,destfile=${server.output.dir}/jacoco/jacoco-it.exec
```

*   Coloca `jacocoagent.jar` en `wlp/usr/servers/<serverName>/jacoco/` (o cualquier ruta legible).
*   Ajusta `includes`/`excludes` a tus paquetes.

3.  **Flujo de ejecución**

*   Inicia Liberty (`server start <serverName>`), despliega el EAR.
*   Ejecuta tus `unittest` de Python (ellos acceden a los endpoints).
*   Detén Liberty (`server stop <serverName>`).
  → El agente escribe `${server.output.dir}/jacoco/jacoco-it.exec`.

4.  **Generar el reporte**

*   Si tu proyecto es multi-módulo (EAR + EJB + WAR), usa un pom agregador y `report-aggregate`:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-aggregate</goal></goals>
      <configuration>
        <dataFile>${env.SERVER_OUTPUT_DIR}/jacoco/jacoco-it.exec</dataFile>
        <includes>
          <include>com/myco/**</include>
        </includes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

(O usa `jacococli`:)

```bash
java -jar jacococli.jar report /path/to/jacoco-it.exec \
  --classfiles module1/target/classes --classfiles module2/target/classes \
  --sourcefiles module1/src/main/java --sourcefiles module2/src/main/java \
  --html target/jacoco-it-report
```

---

## 2) Volcado en vivo sin detener Liberty (modo servidor TCP)

**Cuándo usarlo:** quieres mantener Liberty ejecutándose y obtener la cobertura bajo demanda.

1.  `jvm.options`:

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=tcpserver,address=*,port=6300,append=false,includes=com.myco.*
```

2.  Ejecuta Liberty, ejecuta las pruebas de Python, luego **volcado**:

```bash
# obtiene la cobertura via TCP y escribe un .exec localmente
java -jar jacococli.jar dump --address 127.0.0.1 --port 6300 --destfile jacoco-it.exec --reset
```

Ahora genera el reporte como arriba.
Consejo: `--reset` borra los contadores para que puedas tomar múltiples instantáneas durante una ejecución larga.

---

## 3) Contenedores / CI (estilo variable de entorno)

*   Si ejecutas Liberty en Docker/K8s, monta el agente y configura:

  *   `jvm.options` como arriba, **o**
  *   Variable de entorno `WLP_JAVA_OPTIONS` / `JAVA_TOOL_OPTIONS` conteniendo el mismo `-javaagent=...`.
*   Para clústeres con múltiples JVMs de Liberty, asigna a cada una un puerto TCP o ruta de archivo distinta, luego **combina**:

```bash
java -jar jacococli.jar merge node1.exec node2.exec --destfile merged.exec
```

---

## Notas y problemas comunes

*   El ** diseño del EAR no importa** para JaCoCo; instrumenta el bytecode en memoria. Para los reportes solo necesita los **archivos de clase originales** de tus módulos (`target/classes`) y sus fuentes para el HTML formateado.
*   Usa **JaCoCo reciente (0.8.12+)** para compatibilidad con Java 17/21 (Liberty a menudo se ejecuta en OpenJ9/HotSpot—ambos funcionan bien).
*   Vigila `includes/excludes` para evitar contar librerías de terceros.
*   Si el `.exec` está vacío, probablemente:

  *   olvidaste adjuntar el agente,
  *   filtraste tus paquetes,
  *   o hiciste el volcado antes de que el tráfico llegara al código.

---

Si compartes el diseño de módulos de tu EAR (módulos EJB/WAR y raíces de paquetes), puedo proporcionar una configuración exacta de `report-aggregate` y un pequeño script para: iniciar Liberty → ejecutar pruebas de Python → obtener el volcado → construir el reporte HTML de una vez.