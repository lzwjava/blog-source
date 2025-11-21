---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4.1-fast
title: Perfiles de Maven para la Configuración de Entorno WAS
translated: true
type: note
---

Para IBM WebSphere Application Server (WAS tradicional, no Liberty), el empaquetado estándar es un archivo **EAR** (incluso para aplicaciones web simples, ya que WAS prefiere EAR sobre WAR independiente). La mejor práctica para manejar diferentes entornos — como desarrollo local (usuario de inicio de sesión fijo/codificado para pruebas) vs servidor/producción (SSO o dominio de seguridad adecuado) — es usar **perfiles de construcción Maven** en un único `pom.xml`. Esto evita mantener múltiples archivos POM separados (por ejemplo, `pom.xml` y `build_pom.xml`), lo cual es propenso a errores y no es idiomático en Maven.

### ¿Por qué Perfiles en lugar de Múltiples POMs?
- Una única fuente de verdad (POM único).
- Activación fácil: `mvn package -Plocal` o `mvn package -Pserver`.
- Los perfiles pueden filtrar recursos, sobrescribir archivos, cambiar la configuración de plugins o ajustar enlaces (por ejemplo, `ibm-web-bnd.xml`, `ibm-application-ext.xml` para autenticación específica de WAS).
- Comúnmente utilizados para diferencias entre dev/pruebas/prod, incluyendo configuraciones de autenticación.

### Estructura Recomendada
Utilice el Maven Resources Plugin con filtrado + directorios de recursos específicos del perfil para intercambiar archivos de configuración (por ejemplo, `web.xml`, archivos `properties`, configuración de seguridad de Spring, o enlaces WAS).

Ejemplo de estructura de directorios:
```
src/
├── main/
│   ├── resources/          (configuraciones comunes)
│   ├── webapp/
│   │   ├── WEB-INF/
│   │   │   ├── web.xml      (versión común o base)
│   │   │   └── ibm-web-bnd.xml (opcional, para enlaces JNDI/auth)
│   └── ...
├── local/                   (recursos específicos del perfil, copiados/filtrados solo para local)
│   └── webapp/
│       └── WEB-INF/
│           ├── web.xml      (versión local con form-login + usuario/rol codificado o sin seguridad)
│           └── ...
└── server/                  (específico del perfil para producción/SSO)
    └── webapp/
        └── WEB-INF/
            ├── web.xml      (versión servidor con <login-config><auth-method>CLIENT-CERT</auth-method> o SPNEGO para SSO)
            └── ...
```

### Ejemplo de Fragmento de pom.xml
```xml
<project ...>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-was-app</artifactId>
    <version>1.0.0</version>
    <packaging>ear</packaging>   <!-- O war si se despliega como WAR, pero EAR es preferido para WAS -->

    <properties>
        <maven.compiler.source>11</maven.compiler.source> <!-- o tu versión de Java -->
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Tus dependencias de la aplicación -->
        <!-- Para APIs de WAS en tiempo de compilación (scope provided) -->
        <dependency>
            <groupId>com.ibm.tools.target</groupId>
            <artifactId>was</artifactId>
            <version>9.0</version> <!-- Coincide con tu versión de WAS, ej. 8.5.5 o 9.0 -->
            <type>pom</type>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Construir EAR (ajustar para WAR si es necesario) -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- Tu configuración EAR, módulos, etc. -->
                </configuration>
            </plugin>

            <!-- Filtrado de recursos y sobrescrituras específicas del perfil -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <useDefaultDelimiters>true</useDefaultDelimiters>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Perfiles -->
    <profiles>
        <!-- Perfil local/dev: usuario fijo, form login o sin seguridad -->
        <profile>
            <id>local</id>
            <activation>
                <activeByDefault>true</activeByDefault> <!-- Por defecto para construcciones locales -->
            </activation>
            <build>
                <resources>
                    <!-- Recursos comunes -->
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <!-- Sobrescribir con archivos específicos locales -->
                    <resource>
                        <directory>src/local/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- Ejemplo de propiedades filtradas para usuario codificado local -->
                <app.login.user>devuser</app.login.user>
                <app.login.password>devpass</app.login.password>
            </properties>
        </profile>

        <!-- Perfil servidor/prod: SSO real (ej. SPNEGO, LTPA, o OpenIDConnect) -->
        <profile>
            <id>server</id>
            <build>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <resource>
                        <directory>src/server/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- Propiedades de producción, ej., habilitar flags SSO -->
                <app.auth.method>SSO</app.auth.method>
            </properties>
        </profile>
    </profiles>
</project>
```

### Puntos Clave para Diferencias de Autenticación
- **Local**: Usar FORM login con usuarios/roles simples en `web.xml` o un archivo properties, o deshabilitar la seguridad por completo (`<security-constraint>` eliminado).
- **Servidor**: Configurar SSO específico de WAS en `web.xml` (por ejemplo, `<auth-method>FORM</auth-method>` con SPNEGO, o usar la función OpenID Connect al estilo Liberty, pero para WAS tradicional a menudo LTPA + dominio de seguridad global). Los enlaces WAS (`ibm-web-bnd.xml`) también pueden ser sobrescritos por perfil para mapeos de usuario/rol.
- Si se usa Spring Security o similar, intercambiar `applicationContext-security.xml` o properties de la misma manera.
- Para usuario local codificado: Evitar credenciales reales codificadas; usar un usuario de prueba mapeado en un `users.properties` local o deshabilitar comprobaciones de autenticación mediante un flag.

### Comandos de Construcción
- Local (por defecto): `mvn clean package`
- Servidor/Prod: `mvn clean package -Pserver`

Esto produce EARs diferentes adaptados para cada entorno desde la **misma base de código**. Si realmente necesita nombres de artefactos separados (por ejemplo, `myapp-local.ear` vs `myapp.ear`), agregue `<finalName>${project.artifactId}-${profile}</finalName>` en las secciones `<build>` específicas del perfil.

[Guía de Perfiles de Maven](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)  
[Plugin Maven EAR](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Integración Maven de IBM WAS](https://www.ibm.com/docs/en/wasdtfe/9.7.0?topic=suye-configuring-dependency-pom-files-that-emulate-classpath-specific-websphere-runtime-environments)