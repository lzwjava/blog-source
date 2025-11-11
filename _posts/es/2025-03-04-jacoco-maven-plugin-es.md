---
audio: false
generated: true
lang: es
layout: post
title: Plugin Maven de JaCoCo
translated: true
type: note
---

Aquí tienes una guía paso a paso sobre **cómo usar el plugin Maven de JaCoCo** para medir la cobertura de código en un proyecto Java basado en Maven. JaCoCo (Java Code Coverage) es una herramienta que se integra con Maven para rastrear cuánto de tu código es ejercitado por las pruebas, típicamente unit tests. Al agregar y configurar el plugin Maven de JaCoCo en tu proyecto, puedes generar informes detallados de cobertura durante el proceso de build.

---

### **Pasos para Usar el Plugin Maven de JaCoCo**

#### **1. Agrega el Plugin Maven de JaCoCo a tu `pom.xml`**
Para usar el plugin Maven de JaCoCo, necesitas incluirlo en la sección `<build><plugins>` del archivo `pom.xml` de tu proyecto. A continuación se muestra una configuración básica que prepara el plugin:

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

- **`groupId`, `artifactId` y `version`**: Estos identifican el plugin Maven de JaCoCo. Reemplaza `0.8.12` con la última versión disponible en [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin).
- **`<executions>`**: Esta sección configura cuándo y cómo se ejecuta el plugin durante el ciclo de vida de build de Maven:
  - **`<goal>prepare-agent</goal>`**: Prepara el agente de JaCoCo para recopilar datos de cobertura durante la ejecución de las pruebas. Por defecto, se vincula a una fase temprana (como `initialize`) y no requiere una fase explícita a menos que se personalice.
  - **`<goal>report</goal>`**: Genera el informe de cobertura después de que se han ejecutado las pruebas. Está vinculado a la fase `verify` aquí, que ocurre después de la fase `test`, asegurando que todos los datos de prueba estén disponibles.

#### **2. Asegúrate de que las Pruebas Estén Configuradas**
El plugin de JaCoCo funciona analizando la ejecución de las pruebas, típicamente las pruebas unitarias ejecutadas por el Maven Surefire Plugin. En la mayoría de los proyectos Maven, Surefire se incluye por defecto y ejecuta las pruebas ubicadas en `src/test/java`. No se necesita configuración adicional a menos que tus pruebas no sean estándar. Verifica que:
- Tengas pruebas unitarias escritas (por ejemplo, usando JUnit o TestNG).
- El plugin Surefire esté presente (se hereda del POM padre por defecto de Maven en la mayoría de los casos).

Si necesitas configurar Surefire explícitamente, podría verse así:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- Usa la última versión -->
</plugin>
```

El goal `prepare-agent` configura el agente de JaCoCo modificando la propiedad `argLine`, que Surefire usa para ejecutar las pruebas con el seguimiento de cobertura habilitado.

#### **3. Ejecuta el Build de Maven**
Para generar el informe de cobertura, ejecuta el siguiente comando en el directorio de tu proyecto:

```bash
mvn verify
```

- **`mvn verify`**: Esto ejecuta todas las fases hasta `verify`, incluyendo `compile`, `test` y `verify`. El plugin de JaCoCo:
  1.  Preparará el agente antes de que se ejecuten las pruebas.
  2.  Recopilará datos de cobertura durante la fase `test` (cuando Surefire ejecuta las pruebas).
  3.  Generará el informe durante la fase `verify`.

Alternativamente, si solo quieres ejecutar las pruebas sin proceder a `verify`, usa:

```bash
mvn test
```

Sin embargo, dado que el goal `report` está vinculado a `verify` en esta configuración, necesitarás ejecutar `mvn verify` para ver el informe. Si prefieres que el informe se genere durante `mvn test`, puedes cambiar la `<phase>` para la ejecución del `report` a `test`, aunque `verify` es una convención común.

#### **4. Visualiza el Informe de Cobertura**
Después de ejecutar `mvn verify`, JaCoCo genera un informe HTML por defecto. Puedes encontrarlo en:

```
target/site/jacoco/index.html
```

- Abre este archivo en un navegador web para ver un desglose detallado de la cobertura de código, incluyendo porcentajes para paquetes, clases, métodos y líneas.
- El informe también incluye formatos XML y CSV en el mismo directorio (`jacoco.xml` y `jacoco.csv`), útiles para la integración con herramientas como sistemas de CI.

---

### **Personalizaciones Opcionales**
Para casos de uso más avanzados, puedes ajustar la configuración del plugin:

- **Excluir Clases o Paquetes**:
  Para excluir cierto código del análisis de cobertura (por ejemplo, código generado), agrega una sección `<configuration>`:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  Coloca esto dentro de la etiqueta `<plugin>`, encima de `<executions>`.

- **Forzar Umbrales de Cobertura**:
  Para hacer fallar el build si la cobertura cae por debajo de un umbral, agrega el goal `check`:

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

- **Cambiar el Directorio de Salida del Informe**:
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
Para usar el plugin Maven de JaCoCo:
1. Agrega el plugin a tu `pom.xml` con los goals `prepare-agent` y `report`.
2. Asegúrate de que tu proyecto tenga pruebas configuradas (típicamente via Surefire).
3. Ejecuta `mvn verify` para generar el informe de cobertura.
4. Revisa el informe en `target/site/jacoco/index.html`.

Esta configuración proporciona una manera directa de integrar la cobertura de código en tu proceso de build de Maven, ayudándote a evaluar la efectividad de tus pruebas. Para la última versión del plugin o configuraciones avanzadas, consulta la [documentación oficial de JaCoCo](https://www.jacoco.org/jacoco/trunk/doc/maven.html).