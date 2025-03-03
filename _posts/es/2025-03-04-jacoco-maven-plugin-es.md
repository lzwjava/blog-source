---
audio: false
generated: true
lang: es
layout: post
title: JaCoCo Plugin de Maven
translated: true
---

Aquí tienes una guía paso a paso sobre **cómo usar el plugin JaCoCo Maven** para medir la cobertura del código en un proyecto Java basado en Maven. JaCoCo (Java Code Coverage) es una herramienta que se integra con Maven para rastrear cuánto de tu código se ejerce con las pruebas, típicamente pruebas unitarias. Al agregar y configurar el plugin JaCoCo Maven en tu proyecto, puedes generar informes detallados de cobertura durante el proceso de construcción.

---

### **Pasos para usar el plugin JaCoCo Maven**

#### **1. Agregar el plugin JaCoCo Maven a tu `pom.xml`**
Para usar el plugin JaCoCo Maven, necesitas incluirlo en la sección `<build><plugins>` del archivo `pom.xml` de tu proyecto. A continuación, se muestra una configuración básica que configura el plugin:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- Usa la última versión disponible -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>verify</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`groupId`, `artifactId` y `version`**: Estos identifican el plugin JaCoCo Maven. Reemplaza `0.8.12` con la última versión disponible en [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin).
- **`<executions>`**: Esta sección configura cuándo y cómo se ejecuta el plugin durante el ciclo de vida de construcción de Maven:
  - **`<goal>prepare-agent</goal>`**: Prepara el agente JaCoCo para recopilar datos de cobertura durante la ejecución de las pruebas. Por defecto, se vincula a una fase temprana (como `initialize`) y no requiere una fase explícita a menos que se personalice.
  - **`<goal>report</goal>`**: Genera el informe de cobertura después de que las pruebas hayan sido ejecutadas. Aquí se vincula a la fase `verify`, que ocurre después de la fase `test`, asegurando que todos los datos de prueba estén disponibles.

#### **2. Asegúrate de que las pruebas estén configuradas**
El plugin JaCoCo funciona analizando la ejecución de las pruebas, típicamente pruebas unitarias ejecutadas por el plugin Maven Surefire. En la mayoría de los proyectos Maven, Surefire está incluido por defecto y ejecuta pruebas ubicadas en `src/test/java`. No se necesita configuración adicional a menos que tus pruebas sean no estándar. Verifica que:
- Tienes pruebas unitarias escritas (por ejemplo, usando JUnit o TestNG).
- El plugin Surefire está presente (se hereda del POM padre de Maven por defecto en la mayoría de los casos).

Si necesitas configurar explícitamente Surefire, podría verse así:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- Usa la última versión -->
</plugin>
```

El objetivo `prepare-agent` configura el agente JaCoCo modificando la propiedad `argLine`, que Surefire usa para ejecutar pruebas con el seguimiento de cobertura habilitado.

#### **3. Ejecutar la construcción de Maven**
Para generar el informe de cobertura, ejecuta el siguiente comando en el directorio de tu proyecto:

```bash
mvn verify
```

- **`mvn verify`**: Esto ejecuta todas las fases hasta `verify`, incluyendo `compile`, `test` y `verify`. El plugin JaCoCo:
  1. Preparará el agente antes de que las pruebas se ejecuten.
  2. Recopilará datos de cobertura durante la fase `test` (cuando Surefire ejecuta las pruebas).
  3. Generará el informe durante la fase `verify`.

Alternativamente, si solo quieres ejecutar pruebas sin proceder a `verify`, usa:

```bash
mvn test
```

Sin embargo, dado que el objetivo `report` está vinculado a `verify` en esta configuración, necesitarás ejecutar `mvn verify` para ver el informe. Si prefieres que el informe se genere durante `mvn test`, puedes cambiar la `<phase>` para la ejecución `report` a `test`, aunque `verify` es una convención común.

#### **4. Ver el informe de cobertura**
Después de ejecutar `mvn verify`, JaCoCo genera un informe HTML por defecto. Puedes encontrarlo en:

```
target/site/jacoco/index.html
```

- Abre este archivo en un navegador web para ver un desglose detallado de la cobertura del código, incluyendo porcentajes para paquetes, clases, métodos y líneas.
- El informe también incluye formatos XML y CSV en el mismo directorio (`jacoco.xml` y `jacoco.csv`), útiles para la integración con herramientas como sistemas CI.

---

### **Personalizaciones opcionales**
Para casos de uso más avanzados, puedes ajustar la configuración del plugin:

- **Excluir clases o paquetes**:
  Para excluir cierto código del análisis de cobertura (por ejemplo, código generado), agrega una sección `<configuration>`:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  Coloca esto dentro de la etiqueta `<plugin>`, arriba de `<executions>`.

- **Imponer umbrales de cobertura**:
  Para fallar la construcción si la cobertura cae por debajo de un umbral, agrega el objetivo `check`:

  ```xml
  <execution>
      <id>check</id>
      <phase>verify</phase>
      <goals>
          <goal>check</goal>
      </goals>
      <configuration>
          <rules>
              <rule>
                  <element>BUNDLE</element>
                  <limits>
                      <limit>
                          <counter>LINE</counter>
                          <value>COVEREDRATIO</value>
                          <minimum>0.80</minimum> <!-- 80% de cobertura de línea -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **Cambiar el directorio de salida del informe**:
  Para personalizar la ubicación del informe, agrega:

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **Resumen**
Para usar el plugin JaCoCo Maven:
1. Agrega el plugin a tu `pom.xml` con los objetivos `prepare-agent` y `report`.
2. Asegúrate de que tu proyecto tenga pruebas configuradas (típicamente a través de Surefire).
3. Ejecuta `mvn verify` para generar el informe de cobertura.
4. Verifica el informe en `target/site/jacoco/index.html`.

Esta configuración proporciona una manera sencilla de integrar la cobertura del código en tu proceso de construcción de Maven, ayudándote a evaluar la efectividad de tus pruebas. Para la última versión del plugin o configuraciones avanzadas, consulta la [documentación oficial de JaCoCo](https://www.jacoco.org/jacoco/trunk/doc/maven.html).