---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Empaquetado WAR vs EAR
translated: true
type: note
---

Aquí tienes una comparación práctica, sin tablas, del empaquetado Maven **WAR** vs **EAR** y cómo usarías cada uno en proyectos reales.

# Para qué sirve cada tipo de empaquetado

* **WAR (`packaging: war`)** – Una única aplicación web: servlets/Jakarta REST, JSP/JSF, Spring MVC/Boot (como WAR), etc. Se despliega en un contenedor de servlets (Tomcat/Jetty) o en la capa web de un servidor de aplicaciones completo.
* **EAR (`packaging: ear`)** – Un paquete de múltiples módulos desplegados juntos en un servidor de aplicaciones Java EE/Jakarta EE completo (WildFly/JBoss EAP, WebLogic, WebSphere). Típicamente contiene uno o más WARs, JARs EJB y librerías compartidas con una única unidad de despliegue.

# Cuándo elegir cada uno típicamente

* Elige **WAR** si tienes una sola aplicación web o aplicación Spring Boot y no necesitas EJBs o características de servidor multi-módulo.
* Elige **EAR** si debes desplegar varios módulos juntos (ej., EJBs + múltiples WARs + librerías compartidas), necesitas servicios del servidor de aplicaciones (XA, realms de seguridad centralizados, JMS, transacciones distribuidas) entre módulos, o tu organización exige el uso de EARs.

# Qué hay dentro del artefacto

* Contenido de un **WAR**: `/WEB-INF/classes`, `/WEB-INF/lib`, `web.xml` opcional (o anotaciones), recursos estáticos. Un classloader por WAR en la mayoría de servidores.
* Contenido de un **EAR**: `*.war`, `*.jar` (EJBs/utilidad), `META-INF/application.xml` (o anotaciones/configuración simplificada), y opcionalmente `lib/` para librerías compartidas entre módulos. Proporciona un classloader a nivel de EAR visible para todos los módulos.

# Consideraciones de dependencias y classloading

* **WAR**: Declara las APIs de servlet/Jakarta EE como `provided`; todo lo demás va en `/WEB-INF/lib`. El aislamiento es más simple; menos conflictos de versión.
* **EAR**: Coloca las librerías comunes en `lib/` del EAR (vía `maven-ear-plugin`), para que todos los módulos compartan una versión. Precaución con los conflictos entre las librerías de los módulos y las APIs proporcionadas por el servidor; alinea las versiones y usa `provided` donde sea apropiado.

# Plugins de Maven que usarás

* **Proyectos WAR**: `maven-war-plugin`
* **Agregador EAR**: `maven-ear-plugin`
* **Módulos EJB (si los hay)**: `maven-ejb-plugin`
* El padre/agregador a menudo usa `packaging: pom` para unir los módulos.

# Ejemplos mínimos

Aplicación web única (WAR):

```xml
<!-- pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-web</artifactId><version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <!-- Usa provided para las APIs del servidor -->
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <!-- Tus dependencias de aplicación -->
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <!-- Opcional: configurar webResources, warName, filtering -->
      </plugin>
    </plugins>
  </build>
</project>
```

EAR multi-módulo con un WAR y un EJB:

```xml
<!-- parent/pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-app</artifactId><version>1.0.0</version>
  <packaging>pom</packaging>
  <modules>
    <module>ejb-module</module>
    <module>web-module</module>
    <module>ear-assembly</module>
  </modules>
</project>
```

```xml
<!-- ejb-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ejb-module</artifactId>
  <packaging>ejb</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- web-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>web-module</artifactId>
  <packaging>war</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type> <!-- permite la inyección @EJB -->
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- ear-assembly/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ear-assembly</artifactId>
  <packaging>ear</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId><artifactId>web-module</artifactId><version>1.0.0</version>
      <type>war</type>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type>
    </dependency>
    <!-- Librerías para poner en EAR/lib compartidas por todos los módulos -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <defaultLibBundleDir>lib</defaultLibBundleDir>
          <modules>
            <webModule>
              <groupId>com.example</groupId>
              <artifactId>web-module</artifactId>
              <contextRoot>/myapp</contextRoot>
            </webModule>
            <ejbModule>
              <groupId>com.example</groupId>
              <artifactId>ejb-module</artifactId>
            </ejbModule>
          </modules>
          <!-- Opcional: generar application.xml, o proporcionar uno personalizado -->
          <generateApplicationXml>true</generateApplicationXml>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

Resultados de la construcción:

* `mvn -pl web-module -am clean package` → `web-module-1.0.0.war`
* `mvn -pl ear-assembly -am clean package` → `ear-assembly-1.0.0.ear` que contiene el WAR, el EJB y `lib/`.

# Diferencias operativas importantes

* **Objetivo de despliegue**

  * WAR: contenedor de servlets o capa web del servidor de aplicaciones.
  * EAR: servidor de aplicaciones completo; despliega todos los módulos atómicamente.
* **Transacciones y mensajería**

  * WAR por sí solo usa lo que el contenedor expone; las configuraciones complejas de XA/JMS a menudo residen en EJBs dentro de EARs.
* **Versionado y lanzamiento**

  * WAR: simple de recompilar y redesplegar una sola aplicación.
  * EAR: coordina versiones de muchos módulos; una unidad de despliegue para consistencia.
* **Tiempo de arranque y desarrollo local**

  * WAR: retroalimentación rápida, runtime más ligero.
  * EAR: más pesado; la integración IDE/servidor ayuda pero los ciclos son más lentos.
* **Nota sobre Spring Boot moderno**

  * Boot prefiere **JAR** ejecutable; WAR es compatible si lo despliegas en un contenedor externo.
  * Boot **no** está dirigido a EAR; si debes usar un servidor de aplicaciones, despliega Boot como WAR y evita EAR a menos que tu plataforma lo requiera.

# Errores comunes y consejos

* Usa `provided` para las APIs del servidor para evitar incluirlas en el paquete.
* Para EARs, coloca las librerías compartidas en `defaultLibBundleDir` para evitar copias duplicadas dentro de cada WAR/EJB.
* Alinea las versiones de Jakarta EE entre módulos; los desajustes causan errores de classloading.
* En WebLogic/WebSphere, ten en cuenta las políticas de classloader (parent-first vs parent-last); a veces necesitas descriptores específicos del proveedor.
* Si no necesitas EJBs/XA, un WAR simple (o Boot JAR) es más simple y usualmente más portable.

Si me dices tu servidor de aplicaciones (Tomcat vs WildFly/WebLogic/etc.) y si tienes EJBs o múltiples aplicaciones web, puedo esbozar los POMs y descriptores de despliegue exactos que necesitarás.