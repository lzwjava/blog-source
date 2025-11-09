---
audio: false
date: 2025-09-10
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Überspringen des Angular Builds in Maven
translated: true
type: note
---

Kurze Antwort: ja – Sie können den Angular/npm-Build überspringen, aber nicht mit einem eingebauten Flag wie `--skip-web`. Verwenden Sie einen der folgenden Ansätze.

### 1) Web-Modul in einem Multi-Module-Build ausschließen

Wenn Ihre Angular-App ihr eigenes Maven-Modul ist (z. B. `web`), schließen Sie es einfach im Reactor aus:

```
mvn -pl '!web' -am clean package
```

Oder bauen Sie nur das Backend-Modul:

```
mvn -pl :backend -am clean package
```

(`-am` baut alle benötigten Abhängigkeiten; die Syntax `!web` schließt dieses Modul aus.)

### 2) Eine "Skip Frontend"-Property hinzufügen (funktioniert mit frontend-maven-plugin oder exec)

Schützen Sie die npm-Goals mit einer Property und schalten Sie sie von der Kommandozeile aus um.

**POM (Web-Modul oder Parent):**

```xml
<properties>
  <skip.frontend>false</skip.frontend>
</properties>

<build>
  <plugins>
    <!-- Beispiel: com.github.eirslett:frontend-maven-plugin -->
    <plugin>
      <groupId>com.github.eirslett</groupId>
      <artifactId>frontend-maven-plugin</artifactId>
      <version>...Ihre Version...</version>
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

    <!-- Wenn Sie exec-maven-plugin verwenden, um npm aufzurufen -->
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>...Ihre Version...</version>
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

### 3) Maven-Profile verwenden

Binden Sie den Frontend-Build nur in einem "with-frontend"-Profil und machen Sie ein "skip-frontend"-Profil in der Entwicklung zur Standardeinstellung.

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
        <!-- dieselbe Plugin-Konfiguration wie oben, ohne skip -->
      </plugins>
    </build>
  </profile>
</profiles>
```

**CLI:**

* Normal (überspringen): `mvn -Dskip.frontend clean package`
* Release (UI bauen): `mvn -Pwith-frontend clean package`

---

## Tipps zur Beschleunigung, wenn Sie die UI *doch* bauen

* Stellen Sie sicher, dass der persistente Cache von Angular aktiviert ist (Angular CLI cached standardmäßig; bewahren Sie `node_modules` und `.angular/cache` im CI-Cache auf).
* Führen Sie `ng build` nur für Releases aus; in der Entwicklung serven Sie die UI separat (`npm start`) und lassen Spring vorgebaute statische Assets serven (z. B. legen Sie `dist/` unter `src/main/resources/static` für gepackte Builds ab).
* Erwägen Sie, das Repo aufzuteilen, damit die Angular-App überhaupt kein Maven-Modul ist; bauen Sie sie nur, wenn sich Frontend-Dateien ändern.
* Wenn Sie eine aktuelle Angular-Version verwenden, nutzen Sie den standardmäßigen esbuild/Vite-Builder und lassen Sie Source Maps in CI-Release-Builds deaktiviert.

---

### Fazit

Verwenden Sie `-pl '!web'`, um das Web-Modul auszuschließen, **oder** fügen Sie eine `skip.frontend`-Property hinzu und konfigurieren Sie Ihre Plugin-Executions so, dass sie diese berücksichtigt. Es gibt kein standardmäßiges `mvn package --skip-web`, aber die beiden oben genannten Muster sind zuverlässig und gebräuchlich.