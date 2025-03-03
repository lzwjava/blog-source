---
audio: false
generated: true
lang: es
layout: post
title: Maven Release Plugin
translated: true
---

Aquí tienes una guía completa sobre cómo usar el **Maven Release Plugin** para gestionar y automatizar el proceso de lanzamiento de tu proyecto Maven.

---

### ¿Qué es el Maven Release Plugin?

El **Maven Release Plugin** es una herramienta que automatiza el proceso de lanzar un proyecto Maven. Maneja tareas como:

- Actualizar los números de versión en los archivos POM de tu proyecto.
- Cometer cambios en tu sistema de control de versiones (VCS), como Git.
- Crear una etiqueta para el lanzamiento en el VCS.
- Construir y desplegar los artefactos del lanzamiento.
- Preparar el proyecto para el siguiente ciclo de desarrollo actualizando los números de versión nuevamente.

Los dos objetivos principales del plugin son:

- **`release:prepare`**: Prepara el proyecto para un lanzamiento actualizando versiones, cometiendo cambios y etiquetando el lanzamiento en el VCS.
- **`release:perform`**: Construye y despliega la versión lanzada utilizando el código etiquetado del VCS.

---

### Guía Paso a Paso para Usar el Maven Release Plugin

#### 1. Agregar el Maven Release Plugin a tu Archivo POM

Para usar el plugin, debes incluirlo en el `pom.xml` de tu proyecto. Agregalo bajo la sección `<build><plugins>` de la siguiente manera:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- Usa la última versión estable -->
        </plugin>
    </plugins>
</build>
```

**Nota**: Verifica la [página oficial del Maven Release Plugin](https://maven.apache.org/maven-release/maven-release-plugin/) para obtener la última versión y reemplaza `2.5.3` en consecuencia.

#### 2. Configurar la Sección SCM (Source Control Management)

El plugin interactúa con tu VCS (por ejemplo, Git) para cometer cambios y crear etiquetas. Debes especificar los detalles de tu VCS en la sección `<scm>` de tu `pom.xml`. Para un repositorio Git alojado en GitHub, podría verse así:

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- Reemplaza `username` y `project` con tu nombre de usuario de GitHub y el nombre del repositorio.
- Ajusta las URLs si usas un servicio de alojamiento de Git diferente (por ejemplo, GitLab, Bitbucket).
- Asegúrate de tener las credenciales necesarias (por ejemplo, claves SSH o un token de acceso personal) configuradas para empujar cambios al repositorio.

#### 3. Preparar tu Proyecto para el Lanzamiento

Antes de ejecutar los comandos de lanzamiento, asegúrate de que tu proyecto esté listo:

- Todos los tests pasan (`mvn test`).
- No hay cambios sin cometer en tu directorio de trabajo (ejecuta `git status` para verificar).
- Estás en la rama correcta (por ejemplo, `master` o `main`) para el lanzamiento.

#### 4. Ejecutar `release:prepare`

El objetivo `release:prepare` prepara tu proyecto para el lanzamiento. Ejecuta el siguiente comando en tu terminal:

```bash
mvn release:prepare
```

**Qué sucede durante `release:prepare`**:

- **Verifica cambios sin cometer**: Asegura que tu directorio de trabajo esté limpio.
- **Solicita versiones**: Pregunta por la versión de lanzamiento y la siguiente versión de desarrollo.
  - Ejemplo: Si tu versión actual es `1.0-SNAPSHOT`, podría sugerir `1.0` para el lanzamiento y `1.1-SNAPSHOT` para la siguiente versión de desarrollo. Puedes aceptar los valores predeterminados o ingresar versiones personalizadas (por ejemplo, `1.0.1` para un lanzamiento de parche).
- **Actualiza archivos POM**: Cambia la versión a la versión de lanzamiento (por ejemplo, `1.0`), comete el cambio y lo etiqueta en el VCS (por ejemplo, `project-1.0`).
- **Prepara para el siguiente ciclo**: Actualiza el POM a la siguiente versión de desarrollo (por ejemplo, `1.1-SNAPSHOT`) y comete el cambio.

**Prueba de Simulación Opcional**: Para probar el proceso sin hacer cambios, usa:

```bash
mvn release:prepare -DdryRun=true
```

Esto simula los pasos de preparación sin cometer ni etiquetar.

#### 5. Ejecutar `release:perform`

Después de preparar el lanzamiento, constrúyelo y despliégalo con:

```bash
mvn release:perform
```

**Qué sucede durante `release:perform`**:

- Verifica la versión etiquetada desde el VCS.
- Construye el proyecto.
- Despliega los artefactos al repositorio especificado en la sección `<distributionManagement>` de tu POM.

**Configura `<distributionManagement>`** (si desplegas en un repositorio remoto):

```xml
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>http://my-repository-manager/releases</url>
    </repository>
    <snapshotRepository>
        <id>snapshots</id>
        <url>http://my-repository-manager/snapshots</url>
    </snapshotRepository>
</distributionManagement>
```

- Reemplaza las URLs con las direcciones de tu gestor de repositorios (por ejemplo, Nexus, Artifactory).
- Asegúrate de que las credenciales estén configuradas en tu archivo `~/.m2/settings.xml` bajo `<servers>` con `id`s coincidentes.

#### 6. Verificar el Lanzamiento

Después de `release:perform`, verifica el lanzamiento:

- Verifica tu gestor de repositorios para asegurarte de que los artefactos (por ejemplo, JARs, fuentes) están desplegados.
- Prueba la versión lanzada en otro proyecto agregándola como dependencia en su POM.

---

### Configuración Adicional y Consejos

#### Manejo de Fallos

- **Limpieza**: Si el proceso de lanzamiento falla, usa:
  ```bash
  mvn release:clean
  ```
  para eliminar los archivos temporales creados por el plugin.
- **Deshacer**: Para deshacer los cambios realizados por `release:prepare`:
  ```bash
  mvn release:rollback
  ```
  Ten cuidado y verifica qué cambios se revierten.

#### Proyectos Multi-Módulo

Para proyectos multi-módulo, el plugin actualiza las versiones de manera consistente en todos los módulos por defecto. Asegúrate de que el POM padre incluya el plugin y la configuración SCM.

#### Modo por Lotes para Automatización

Para ejecutar el lanzamiento de manera no interactiva (por ejemplo, en una pipeline CI/CD), usa la bandera `-B` y especifica las versiones:

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### Problemas Comunes y Soluciones

- **Errores de VCS**: Asegúrate de que los comandos de Git (por ejemplo, `git commit`, `git push`) funcionen manualmente. Verifica la autenticación (claves SSH, tokens).
- **Fallos de Construcción**: Verifica que la construcción tenga éxito localmente (`mvn clean install`) y que las dependencias se resuelvan correctamente.
- **Estrategia de Versión**: Personaliza las versiones durante las solicitudes o a través de propiedades si los valores predeterminados no se adaptan a tus necesidades.

---

### Resumen de Comandos

1. **Preparar el lanzamiento**:
   ```bash
   mvn release:prepare
   ```
2. **Realizar el lanzamiento**:
   ```bash
   mvn release:perform
   ```
3. **Prueba de Simulación Opcional**:
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **Limpieza o deshacer si es necesario**:
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### Conclusión

El Maven Release Plugin simplifica el proceso de lanzamiento automatizando la gestión de versiones, las interacciones con el VCS y el despliegue. Al agregar el plugin a tu POM, configurar tu SCM y seguir los pasos `release:prepare` y `release:perform`, puedes lanzar tus proyectos Maven de manera eficiente. Siempre prueba tu configuración con una prueba de simulación y verifica los resultados para asegurar un proceso de lanzamiento fluido.