---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einrichtung von Maven WAR- und EAR-Modulen
translated: true
type: note
---

### Maven Multi-Module-Projekt Setup für WAR zu EAR

In Maven verwenden Sie eine Multi-Module-Projektstruktur, um ein Modul ein WAR (z.B. eine Webanwendung) erstellen zu lassen und ein anderes Modul dieses in ein EAR (Enterprise Archive) zu verpacken. Das EAR-Modul hängt über das `maven-ear-plugin` vom WAR-Modul ab. Dies stellt sicher, dass das WAR während des Builds in das EAR eingebunden wird.

#### Schritt 1: Erstellen der Parent POM
Die Parent POM definiert die Module und verwaltet gemeinsame Konfigurationen. Setzen Sie das Packaging auf `pom`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>web-module</module>  <!-- Dieses zuerst bauen -->
        <module>ear-module</module>
    </modules>

    <!-- Optional: Gemeinsame Abhängigkeiten und Plugin-Versionen -->
    <dependencyManagement>
        <dependencies>
            <!-- Versionen für Kind-Module hier definieren -->
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <!-- Plugin-Versionen verwalten -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-ear-plugin</artifactId>
                    <version>3.3.0</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### Schritt 2: Konfigurieren des WAR-Moduls
Dieses Modul baut die Webanwendung als WAR. Setzen Sie das Packaging auf `war`. Hier ist keine spezielle EAR-Konfiguration nötig – es muss nur zuerst gebaut werden.

Verzeichnisstruktur: `web-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>web-module</artifactId>
    <packaging>war</packaging>

    <dependencies>
        <!-- Fügen Sie Ihre Web-Abhängigkeiten hinzu, z.B. servlet-api -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Schritt 3: Konfigurieren des EAR-Moduls
Dieses Modul packt das EAR. Setzen Sie das Packaging auf `ear` und verwenden Sie das `maven-ear-plugin`, um auf das WAR-Modul zu verweisen. Das Plugin wird das WAR-Artefakt abrufen und in das EAR einbinden.

Verzeichnisstruktur: `ear-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>ear-module</artifactId>
    <packaging>ear</packaging>

    <dependencies>
        <!-- Vom WAR-Modul abhängen, um es in den Build einzubeziehen -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>web-module</artifactId>
            <version>${project.version}</version>
            <type>war</type>
        </dependency>
        <!-- Optional: EJB- oder andere Module hinzufügen, falls nötig -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- EAR-Version (z.B. für Java EE) -->
                    <version>8</version>
                    
                    <!-- Verzeichnis für Bibliotheken im EAR -->
                    <defaultLibBundleDir>lib</defaultLibBundleDir>
                    
                    <!-- Skinny WARs (Abhängigkeiten ausschließen, die bereits in EAR-Libs sind) -->
                    <skinnyWars>true</skinnyWars>
                    
                    <!-- Einzubindende Module definieren -->
                    <modules>
                        <webModule>
                            <groupId>com.example</groupId>
                            <artifactId>web-module</artifactId>
                            <bundleDir>/</bundleDir>  <!-- Wurzel des EAR -->
                            <contextRoot>/mywebapp</contextRoot>  <!-- Deployment-Kontext -->
                        </webModule>
                        <!-- Weitere <ejbModule> oder <jarModule> bei Bedarf hinzufügen -->
                    </modules>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Schritt 4: Das Projekt bauen
- Führen Sie den Befehl aus dem **Elternverzeichnis** aus: `mvn clean install`
  - Dies baut die Module in der Reihenfolge (zuerst WAR, dann EAR).
- Das EAR befindet sich in `ear-module/target/ear-module-1.0-SNAPSHOT.ear`.
- Um nur das EAR zu bauen (vorausgesetzt, das WAR ist bereits gebaut): `cd ear-module && mvn clean package`.

#### Wichtige Hinweise
- **Build-Reihenfolge**: Listen Sie das WAR-Modul im `<modules>`-Abschnitt der Parent-POM vor dem EAR-Modul auf, um sicherzustellen, dass Maven das WAR zuerst baut.
- **Abhängigkeiten**: Die `<dependency>` des EAR-Moduls auf das WAR stellt sicher, dass es während des Packagings aufgelöst wird.
- **Anpassung**: Passen Sie den `<contextRoot>` für den URL-Pfad der Webanwendung an. Fügen Sie bei Bedarf weitere Module (z.B. EJB JARs) in `<modules>` hinzu.
- **Fehlerbehebung**: Wenn das WAR nicht eingebunden wird, prüfen Sie, ob die Artefakt-Koordinaten exakt übereinstimmen. Verwenden Sie `mvn dependency:tree` im EAR-Modul zur Überprüfung.

Weitere Details finden Sie in der offiziellen Dokumentation des Maven EAR Plugins.

[Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Maven Multi-Module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Multi-module_Projects)