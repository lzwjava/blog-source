---
audio: false
date: 2025-09-10
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Corrección de Advertencias de Codificación de la Plataforma Maven
translated: true
type: note
---

Esa advertencia de Maven significa que el proceso de compilación de tu proyecto depende de la **codificación predeterminada de la plataforma** (por ejemplo, GBK en un sistema Windows en chino). Si otros desarrolladores o servidores de CI utilizan una codificación diferente (como UTF-8 en Linux), los recursos de texto (código fuente Java, properties, XML, etc.) podrían leerse o compilarse incorrectamente.

Aquí te mostramos cómo solucionarlo:

---

### 1. Establece la Codificación de Origen en `pom.xml`

En la sección `<properties>` de tu proyecto, declara explícitamente la codificación:

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <maven.compiler.encoding>UTF-8</maven.compiler.encoding>
</properties>
```

Esto asegura que Maven compile las fuentes y genere los informes de manera consistente en UTF-8, independientemente del valor predeterminado de tu SO.

---

### 2. Configura el Plugin del Compilador (si aún no está hecho)

Algunas configuraciones antiguas de Maven requieren especificar la codificación en el plugin del compilador:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---

### 3. Verifica las Codificaciones de los Archivos

* Asegúrate de que tus archivos `.java`, `.properties`, `.yml`, etc., estén guardados en UTF-8, no en GBK.
* En IntelliJ IDEA o VS Code, establece **File Encoding = UTF-8** en la configuración del proyecto.
* Para Git, puedes imponer una codificación consistente con `.gitattributes` si es necesario.

---

### 4. Ejecuta Maven con Codificación Explícita (Opcional)

También puedes anular la codificación al ejecutar Maven:

```bash
mvn clean install -Dfile.encoding=UTF-8
```

Pero la mejor práctica es solucionarlo dentro del `pom.xml`, para que sea consistente para todos.

---

✅ Después de estos cambios, la advertencia sobre la "codificación dependiente de la plataforma GBK" debería desaparecer, y tu proyecto Spring + Maven será seguro en cuanto a codificación en todas las máquinas.

¿Quieres que también te muestre cómo **convertir archivos fuente existentes de GBK a UTF-8** de forma segura (para que tu repositorio esté limpio y consistente)?