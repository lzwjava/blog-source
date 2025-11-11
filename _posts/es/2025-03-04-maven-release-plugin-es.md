---
audio: false
generated: true
lang: es
layout: post
title: Plugin de Lanzamiento de Maven
translated: true
type: note
---

Aquí tienes una guía completa sobre cómo usar el **Maven Release Plugin** para gestionar y automatizar el proceso de lanzamiento de tu proyecto Maven.

---

### ¿Qué es el Maven Release Plugin?

El **Maven Release Plugin** es una herramienta que automatiza el proceso de lanzamiento de un proyecto Maven. Maneja tareas como:

- Actualizar los números de versión en el/los archivo(s) POM de tu proyecto.
- Confirmar los cambios en tu sistema de control de versiones (VCS), como Git.
- Crear una etiqueta (tag) para el lanzamiento en el VCS.
- Construir y desplegar los artefactos de la versión.
- Preparar el proyecto para el siguiente ciclo de desarrollo actualizando nuevamente los números de versión.

Los dos objetivos principales del plugin son:

- **`release:prepare`**: Prepara el proyecto para un lanzamiento actualizando las versiones, confirmando los cambios y etiquetando el lanzamiento en el VCS.
- **`release:perform`**: Construye y despliega la versión lanzada utilizando el código etiquetado del VCS.

---

### Guía Paso a Paso para Usar el Maven Release Plugin

#### 1. Añade el Maven Release Plugin a tu Archivo POM

Para usar el plugin, debes incluirlo en el `pom.xml` de tu proyecto. Añádelo en la sección `<build><plugins>` de la siguiente manera:

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

**Nota**: Consulta la [página oficial del Maven Release Plugin](https://maven.apache.org/maven-release/maven-release-plugin/) para obtener la última versión y reemplaza `2.5.3` en consecuencia.

#### 2. Configura la Sección SCM (Source Control Management)

El plugin interactúa con tu VCS (por ejemplo, Git) para confirmar cambios y crear etiquetas. Debes especificar los detalles de tu VCS en la sección `<scm>` de tu `pom.xml`. Para un repositorio Git alojado en GitHub, podría verse así:

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- Reemplaza `username` y `project` con tu nombre de usuario de GitHub y el nombre del repositorio reales.
- Ajusta las URLs si estás usando un servicio de alojamiento Git diferente (por ejemplo, GitLab, Bitbucket).
- Asegúrate de tener las credenciales necesarias configuradas (por ejemplo, claves SSH o un token de acceso personal) para poder enviar (push) cambios al repositorio.

#### 3. Prepara tu Proyecto para el Lanzamiento

Antes de ejecutar los comandos de lanzamiento, asegúrate de que tu proyecto esté listo:

- Todas las pruebas pasan (`mvn test`).
- No hay cambios sin confirmar en tu directorio de trabajo (ejecuta `git status` para verificar).
- Estás en la rama correcta (por ejemplo, `master` o `main`) para el lanzamiento.

#### 4. Ejecuta `release:prepare`

El objetivo `release:prepare` prepara tu proyecto para el lanzamiento. Ejecuta el siguiente comando en tu terminal:

```bash
mvn release:prepare
```

**Qué sucede durante `release:prepare`**:

- **Verifica cambios sin confirmar**: Asegura que tu directorio de trabajo esté limpio.
- **Solicita las versiones**: Pide la versión de lanzamiento y la siguiente versión de desarrollo.
  - Ejemplo: Si tu versión actual es `1.0-SNAPSHOT`, podría sugerir `1.0` para el lanzamiento y `1.1-SNAPSHOT` para la siguiente versión de desarrollo. Puedes aceptar los valores predeterminados o introducir versiones personalizadas (por ejemplo, `1.0.1` para un lanzamiento de parche).
- **Actualiza los archivos POM**: Cambia la versión a la versión de lanzamiento (por ejemplo, `1.0`), confirma el cambio y lo etiqueta en el VCS (por ejemplo, `project-1.0`).
- **Prepara para el siguiente ciclo**: Actualiza el POM a la siguiente versión de desarrollo (por ejemplo, `1.1-SNAPSHOT`) y la confirma.

**Ejecución de Prueba Opcional**: Para probar el proceso sin realizar cambios, usa:

```bash
mvn release:prepare -DdryRun=true
```

Esto simula los pasos de preparación sin confirmar o etiquetar.

#### 5. Ejecuta `release:perform`

Después de preparar el lanzamiento, constrúyelo y despliégalo con:

```bash
mvn release:perform
```

**Qué sucede durante `release:perform`**:

- Extrae (checkout) la versión etiquetada del VCS.
- Construye el proyecto.
- Despliega los artefactos al repositorio especificado en la sección `<distributionManagement>` de tu POM.

**Configura `<distributionManagement>`** (si se despliega a un repositorio remoto):

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

#### 6. Verifica el Lanzamiento

Después de `release:perform`, verifica el lanzamiento:

- Revisa tu gestor de repositorios para asegurarte de que los artefactos (por ejemplo, JARs, fuentes) estén desplegados.
- Prueba la versión lanzada en otro proyecto añadiéndola como dependencia en su POM.

---

### Configuración Adicional y Consejos

#### Manejo de Fallos

- **Limpieza**: Si el proceso de lanzamiento falla, usa:
  ```bash
  mvn release:clean
  ```
  para eliminar los archivos temporales creados por el plugin.
- **Reversión**: Para deshacer los cambios realizados por `release:prepare`:
  ```bash
  mvn release:rollback
  ```
  Ten precaución y verifica qué cambios se revierten.

#### Proyectos Multi-Módulo

Para proyectos multi-módulo, el plugin actualiza las versiones en todos los módulos de manera consistente por defecto. Asegúrate de que el POM padre incluya la configuración del plugin y del SCM.

#### Modo por Lotes para Automatización

Para ejecutar el lanzamiento de forma no interactiva (por ejemplo, en una canalización CI/CD), usa el flag `-B` y especifica las versiones:

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### Problemas Comunes y Soluciones

- **Errores de VCS**: Asegúrate de que los comandos de Git (por ejemplo, `git commit`, `git push`) funcionen manualmente. Verifica la autenticación (claves SSH, tokens).
- **Fallos de Construcción**: Verifica que la construcción tenga éxito localmente (`mvn clean install`) y que las dependencias se resuelvan correctamente.
- **Estrategia de Versiones**: Personaliza las versiones durante los prompts o mediante propiedades si los valores predeterminados no se adaptan a tus necesidades.

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
3. **Ejecución de prueba opcional**:
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **Limpieza o reversión si es necesario**:
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### Conclusión

El Maven Release Plugin simplifica el proceso de lanzamiento automatizando la gestión de versiones, las interacciones con el VCS y el despliegue. Al añadir el plugin a tu POM, configurar tu SCM y seguir los pasos de `release:prepare` y `release:perform`, puedes lanzar tus proyectos Maven de manera eficiente. Siempre prueba tu configuración con una ejecución de prueba y verifica los resultados para garantizar un proceso de lanzamiento fluido.