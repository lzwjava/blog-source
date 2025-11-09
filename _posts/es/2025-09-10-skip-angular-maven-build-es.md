---
audio: false
date: 2025-09-10
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Omitir la Compilación de Angular en Maven
translated: true
type: note
---

Respuesta corta: sí—puedes omitir la compilación de Angular/npm, pero no con una bandera incorporada como `--skip-web`. Utiliza uno de estos enfoques.

### 1) Excluir el módulo web en una compilación multi-módulo

Si tu aplicación Angular es su propio módulo Maven (por ejemplo, `web`), simplemente exclúyelo en el reactor:

```
mvn -pl '!web' -am clean package
```

O compila solo el módulo del backend:

```
mvn -pl :backend -am clean package
```

(`-am` compila cualquier dependencia necesaria; la sintaxis `!web` excluye ese módulo).

### 2) Agregar una propiedad “skip frontend” (funciona con frontend-maven-plugin o exec)

Protege los objetivos de npm con una propiedad y cámbiala desde la línea de comandos.

**POM (módulo web o padre):**

```xml
<properties>
  <skip.frontend>false</skip.frontend>
</properties>

<build>
  <plugins>
    <!-- Ejemplo: com.github.eirslett:frontend-maven-plugin -->
    <plugin>
      <groupId>com.github.eirslett</groupId>
      <artifactId>frontend-maven-plugin</artifactId>
      <version>...tu versión...</version>
      <configuration>
        <skip>${skip.frontend}</skip>
      </configuration>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals>
            <goal>npm</goal>
          </goals>
          <configuration>
            <arguments>run build</arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>

    <!-- Si usas exec-maven-plugin para llamar a npm -->
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>...tu versión...</version>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals><goal>exec</goal></goals>
          <configuration>
            <skip>${skip.frontend}</skip>
            <executable>npm</executable>
            <arguments>
              <argument>run</argument>
              <argument>build</argument>
            </arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

**CLI:**

```
mvn -Dskip.frontend=true clean package
```

### 3) Usar perfiles de Maven

Vincula la compilación del frontend solo en un perfil “with-frontend” y haz que un perfil “skip-frontend” sea el predeterminado en desarrollo.

**POM:**

```xml
<profiles>
  <profile>
    <id>with-frontend</id>
    <activation>
      <property>
        <name>!skip.frontend</name>
      </property>
    </activation>
    <build>
      <plugins>
        <!-- misma configuración del plugin que arriba, sin skip -->
      </plugins>
    </build>
  </profile>
</profiles>
```

**CLI:**

* Normal (omitir): `mvn -Dskip.frontend clean package`
* Release (compilar UI): `mvn -Pwith-frontend clean package`

---

## Consejos de velocidad si *sí* compilas la UI

* Asegúrate de que la caché persistente de Angular esté activada (Angular CLI almacena en caché por defecto; mantén `node_modules` y `.angular/cache` en caché en CI).
* Solo ejecuta `ng build` para release; en desarrollo, sirve la UI por separado (`npm start`) y haz que Spring sirva recursos estáticos precompilados (por ejemplo, coloca `dist/` bajo `src/main/resources/static` para compilaciones empaquetadas).
* Considera dividir el repositorio para que la aplicación Angular no sea un módulo Maven en absoluto; compílala solo cuando los archivos del frontend cambien.
* Si estás en una versión reciente de Angular, usa el builder predeterminado esbuild/Vite y mantén los source maps deshabilitados en las compilaciones de release en CI.

---

### Conclusión

Usa `-pl '!web'` para excluir el módulo web, **o** agrega una propiedad `skip.frontend` y configura las ejecuciones de tu plugin para que la respeten. No existe un estándar `mvn package --skip-web`, pero los dos patrones anteriores son confiables y comunes.