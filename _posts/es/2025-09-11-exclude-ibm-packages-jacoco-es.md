---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Excluir Paquetes com.ibm en JaCoCo
translated: true
type: note
---

Para excluir paquetes **`com.ibm`** (o cualquier otro paquete) de la cobertura de JaCoCo en un entorno de **WebSphere Liberty Profile**, puedes configurar las exclusiones en tu archivo **`pom.xml`**. Esto se realiza típicamente en la configuración del **plugin de Maven para JaCoCo**.

---

### **Cómo excluir paquetes `com.ibm` en `pom.xml`**

Puedes usar la etiqueta `<excludes>` en la configuración del plugin de JaCoCo para especificar qué clases o paquetes deben excluirse del reporte de cobertura.

#### **Configuración de Ejemplo:**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version> <!-- Usa la versión más reciente -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>test</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                    <configuration>
                        <outputDirectory>${project.reporting.outputDirectory}/jacoco</outputDirectory>
                        <excludes>
                            <!-- Excluir todos los paquetes com.ibm -->
                            <exclude>com/ibm/**</exclude>
                        </excludes>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

---

### **Explicación:**
- **`<excludes>`**: Esta sección especifica qué clases o paquetes deben excluirse del reporte de cobertura.
- **`<exclude>com/ibm/**</exclude>`**: Esto excluye todas las clases bajo el paquete `com.ibm` y sus subpaquetes.

---

### **Notas Adicionales:**
- Si deseas excluir múltiples paquetes, añade más entradas `<exclude>`:
  ```xml
  <excludes>
      <exclude>com/ibm/**</exclude>
      <exclude>org/apache/**</exclude>
  </excludes>
  ```
- Si estás usando **JaCoCo con WebSphere Liberty**, asegúrate de que el agente de JaCoCo esté configurado correctamente en tu archivo `server.env` o `jvm.options`, y que las exclusiones en el `pom.xml` se alineen con tus requisitos.

---

### **Mejor Práctica:**
- Siempre verifica las exclusiones ejecutando un reporte de cobertura y comprobando que los paquetes excluidos no estén incluidos en los resultados.
- Si necesitas excluir paquetes en tiempo de ejecución (por ejemplo, en los argumentos del agente JaCoCo), puedes usar el parámetro `excludes` en los argumentos del agente:
  ```plaintext
  -javaagent:/path/to/jacocoagent.jar=destfile=/path/to/jacoco.exec,excludes=com.ibm.*
  ```