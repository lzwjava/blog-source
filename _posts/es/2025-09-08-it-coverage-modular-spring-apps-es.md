---
audio: false
date: 2025-09-08
generated: true
image: false
lang: es
layout: post
title: Cobertura de TI para Aplicaciones Modulares Spring
translated: true
type: note
---

### Evaluación General de Tu Configuración
Tu configuración actual es sólida para un proyecto pequeño multi-módulo como este, especialmente porque ya tienes el flujo central funcionando: adjuntar el agente JaCoCo a Jetty, ejecutar pruebas de integración externas de Python mediante el Exec Plugin, y generar un reporte en el módulo `PlaygroundWeb`. Esto captura la cobertura en tiempo de ejecución de los endpoints API probados por `unittest` de Python, que es exactamente lo que necesitas para la cobertura de pruebas de integración (IT) en una aplicación web Spring.

Puntos fuertes clave:
- **Modular y vinculado a fases**: Usar fases de Maven (`pre-integration-test` para inicio de Jetty, `integration-test` para pruebas de Python, `post-integration-test` para parada, `verify` para el reporte) garantiza fiabilidad y reproducibilidad.
- **Adjuntar el agente**: El argumento JVM (`-javaagent:...`) en Jetty instrumenta correctamente el runtime, capturando la cobertura en `jacoco.it.exec`.
- **Integración de pruebas externas**: El Exec Plugin maneja Python muy bien, y mantener las pruebas en la raíz del repositorio (`${project.parent.basedir}/tests`) las desacopla de los módulos Java.
- **Sin duplicación innecesaria**: Evitas ejecutar Jetty/Python en `PlaygroundUtils` (que no tiene controladores), lo cual es eficiente.

Desafíos que has identificado:
- **Cobertura para módulos de librerías como `PlaygroundUtils`**: Dado que el código de utils se ejecuta en la JVM de `PlaygroundWeb` (como una dependencia en el WAR), está instrumentado y aparece en el `jacoco.it.exec` de `PlaygroundWeb`. Pero tus reportes son específicos del módulo, por lo que la cobertura de `PlaygroundUtils` no es visible a menos que se agregue o incluya.
- **La naturaleza no autocontenida de JaCoCo**: A diferencia de Checkstyle/Spotless (que solo analizan artefactos fuente/estáticos), JaCoCo necesita datos de runtime (archivos `.exec`) de pruebas externas y la adjunción del agente. Esto lo hace frágil para configuraciones multi-módulo sin una coordinación cuidadosa.
- **Limitaciones del objetivo de agregación**: `jacoco:report-aggregate` espera archivos `.exec` por módulo (por ejemplo, de pruebas unitarias), pero tu cobertura es puramente de IT en un módulo. Forzar la agregación puede generar reportes vacíos para librerías como `PlaygroundUtils`.
- **Escalabilidad a 10+ módulos**: Duplicar las configuraciones de Jetty/Python en todos los módulos sería ineficiente (servidores/pruebas redundantes). Las soluciones alternativas poco elegantes, como copiar archivos `.exec` o ejecutar todo dos veces (como mencionaste), introducen sobrecarga de mantenimiento y aumentan el tiempo de construcción.

Tu recurso a reportes por módulo es pragmático, pero podemos optimizar para la inclusión de cobertura sin duplicación.

### Estrategia Recomendada
Enfócate en **generar un único reporte de cobertura de IT integral en el módulo que ejecuta la aplicación** (`PlaygroundWeb` en este caso), mientras **incluyes datos de cobertura para módulos dependientes** como `PlaygroundUtils`. Esto evita ejecutar las pruebas múltiples veces y aprovecha el hecho de que todo el código se ejecuta en una sola JVM.

¿Por qué esto sobre la agregación?
- La agregación (`report-aggregate`) es mejor para la cobertura de pruebas unitarias distribuidas entre módulos. Para la cobertura de IT desde un único runtime (tu caso), es excesiva y no encaja naturalmente.
- Un reporte unificado da una visión holística de la cobertura de la aplicación, que a menudo es más útil que los reportes aislados por módulo (por ejemplo, "80% en general, pero la capa de utils está al 60%").
- Para proyectos más grandes, esto escala tratando el "módulo de aplicación" (WAR/EAR) como el centro de cobertura, incorporando las dependencias.

#### Implementación Paso a Paso para Tu Proyecto de 2 Módulos
Comienza poco a poco: Aplica esto a tu configuración actual (1 módulo de aplicación + 1 librería). Pruébalo y luego expande.

1. **Mantén la Ejecución de IT Solo en `PlaygroundWeb`**:
   - No se necesitan cambios aquí. Jetty inicia el WAR (que incluye `PlaygroundUtils`), las pruebas de Python acceden a los endpoints, la cobertura se captura en `${project.build.directory}/jacoco.it.exec`.
   - Confirma que el código de utils se ejercita: Si tus pruebas de Python llaman a endpoints que usan clases de `PlaygroundUtils` (por ejemplo, `SystemUtils`), su cobertura estará en el archivo `.exec`.

2. **Mejora el Reporte de JaCoCo en `PlaygroundWeb` para Incluir `PlaygroundUtils`**:
   - Usa `<additionalClassesDirectories>` y `<additionalSourceDirectories>` de JaCoCo en el objetivo `report`. Esto le indica a JaCoCo que escanee las clases/fuentes de `PlaygroundUtils` contra el mismo archivo `.exec`.
   - Actualiza el POM de `PlaygroundWeb` (en la configuración de `jacoco-maven-plugin`):

     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <executions>
             <!-- Prepare-agent existente -->
             <execution>
                 <id>prepare-agent</id>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <!-- Reporte mejorado: Incluir el módulo utils -->
             <execution>
                 <id>report-it</id>
                 <phase>verify</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
                 <configuration>
                     <dataFile>${jacoco.it.exec}</dataFile>
                     <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
                     <!-- Añade esto para incluir la cobertura de PlaygroundUtils -->
                     <additionalClassesDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/target/classes</directory>
                     </additionalClassesDirectories>
                     <additionalSourceDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/src/main/java</directory>
                     </additionalSourceDirectories>
                 </configuration>
             </execution>
         </executions>
     </plugin>
     ```

   - Esto genera un reporte (en `PlaygroundWeb/target/site/jacoco-it`) que cubre ambos módulos. Verás desgloses por paquete/clase, incluyendo `org.lzw` de utils.

3. **Deshabilita/Elimina JaCoCo de `PlaygroundUtils`**:
   - Dado que no tiene IT propia, elimina cualquier configuración/propiedad de JaCoCo (por ejemplo, `<jacoco.it.exec>`, `<it.report.skip>`). No necesita generar su propio reporte; la cobertura se maneja aguas arriba.
   - Si tienes pruebas unitarias en utils, mantén un `prepare-agent` + `report` separado para la cobertura unitaria (`jacoco.exec` por defecto), pero aíslalo de la IT.

4. **Construye y Verifica**:
   - Ejecuta `mvn clean verify` desde el padre.
   - Jetty/Python se ejecutan solo una vez (en `PlaygroundWeb`).
   - Revisa `PlaygroundWeb/target/site/jacoco-it/index.html`: Debería mostrar la cobertura para las clases de ambos módulos.
   - Si la cobertura de utils es 0%, asegúrate de que tus pruebas de Python ejerciten esas clases (por ejemplo, añade una prueba que active `SystemUtils` a través de un endpoint).

5. **Opcional: Hacer Cumplir Umbrales de Cobertura**:
   - Añade una ejecución `check` en el plugin JaCoCo de `PlaygroundWeb` para fallar la construcción si la cobertura cae por debajo de un umbral (por ejemplo, 70% de cobertura de líneas en general).
     ```xml
     <execution>
         <id>check-it</id>
         <goals>
             <goal>check</goal>
         </goals>
         <configuration>
             <dataFile>${jacoco.it.exec}</dataFile>
             <rules>
                 <rule>
                     <element>BUNDLE</element>
                     <limits>
                         <limit>
                             <counter>LINE</counter>
                             <value>COVEREDRATIO</value>
                             <minimum>0.70</minimum>
                         </limit>
                     </limits>
                 </rule>
             </rules>
         </configuration>
     </execution>
     ```

#### Escalando a un Proyecto Más Grande (por ejemplo, 10 Módulos)
Para 10+ módulos (por ejemplo, múltiples librerías + 1-2 módulos de aplicación/WAR), extiende lo anterior para evitar complejidad:

- **Centralizar la IT en los Módulos de Aplicación**: Si tienes un WAR principal (como `PlaygroundWeb`), conviértelo en el "centro de cobertura". Añade `<additionalClassesDirectories>` y `<additionalSourceDirectories>` para todas las librerías dependientes (por ejemplo, mediante un bucle o listas de propiedades en el POM padre).
  - Ejemplo: Define rutas en las propiedades del padre:
    ```xml
    <properties>
        <lib1.classes>${project.basedir}/Lib1/target/classes</lib1.classes>
        <lib1.sources>${project.basedir}/Lib1/src/main/java</lib1.sources>
        <!-- Repetir para 10 librerías -->
    </properties>
    ```
  - En la configuración del reporte JaCoCo del WAR: Referéncialas dinámicamente.

- **Si Hay Múltiples Aplicaciones/WARs**: Crea módulos de IT dedicados (por ejemplo, `App1-IT`, `App2-IT`) que dependan del WAR, configuren Jetty/Exec/JaCoCo allí, e incluyan solo las clases/fuentes de las dependencias relevantes. Esto mantiene las construcciones modulares (por ejemplo, `mvn verify -pl App1-IT` para cobertura dirigida).

- **Evitar la Duplicación de IT por Módulo**: Nunca ejecutes Jetty/Python en módulos de librería—es ineficiente. Si una librería necesita IT aislada (raro), dale su propia mini-suite de servidor/pruebas.

- **Agregación para Reportes (Si es Necesaria)**: Si insistes en reportes separados por módulo:
  - Genera el `.exec` en el módulo de aplicación.
  - Usa `dependency:copy` de Maven o un script personalizado (vía Exec Plugin) en el `post-integration-test` del padre para copiar el `.exec` al `target/` de cada librería (por ejemplo, como `jacoco-it.exec`).
  - Luego, configura `report` en cada librería para usar ese archivo copiado.
  - Pero esto es más complejo—prefiere el reporte unificado a menos que los interesados exijan métricas por módulo.

- **Consejos de Herramientas para Escalar**:
  - **Perfiles de Maven**: Usa perfiles (por ejemplo, `-Pcoverage`) para activar/desactivar IT/reportes para construcciones de desarrollo más rápidas.
  - **Optimización en CI**: En CI (por ejemplo, GitHub Actions), almacena en caché las dependencias de Maven y ejecuta IT solo en cambios a pruebas/endpoints.
  - **Alternativas si JaCoCo se Vuelve Demasiado Complejo**: Considera SonarQube para análisis agregado (ingiere datos de JaCoCo entre módulos). O cambia a herramientas de runtime como OpenClover, pero JaCoCo está bien si te apegas al enfoque del centro.
  - **Probar las Pruebas**: Añade una prueba de smoke en Python para verificar el inicio del servidor (por ejemplo, consultar `http://localhost:8080/health`).

Esta estrategia minimiza las ejecuciones (un Jetty/Python por aplicación), maneja las dependencias de JaCoCo de forma limpia y escala sin explosión. Si compartes más detalles (por ejemplo, cómo se usa utils en los endpoints), puedo refinar los fragmentos de POM aún más.