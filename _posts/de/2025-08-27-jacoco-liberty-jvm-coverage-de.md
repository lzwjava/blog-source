---
audio: false
generated: true
image: false
lang: de
layout: post
title: JaCoCo für Liberty JVM Coverage
translated: true
type: note
---

Sie können es schaffen – hängen Sie JaCoCo an die **Liberty JVM** an, die Ihr EAR ausführt. Der Schlüssel ist: JaCoCo muss sich in derselben JVM wie Liberty befinden, nicht in Ihrem Python-Runner.

Hier sind zuverlässige Setups (wählen Sie eines aus).

---

## 1) Einfach & robust: Bei JVM-Exit in Datei schreiben

**Verwenden Sie dies, wenn:** Sie den Liberty-Server nach den Tests stoppen können.

1. **Stellen Sie das Agent-JAR bereit** (einmalig in Ihrem Build)

```xml
<!-- kopiert jacoco agent nach target/jacoco/jacocoagent.jar -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-dependency-plugin</artifactId>
  <version>3.6.1</version>
  <executions>
    <execution>
      <id>copy-jacoco-agent</id>
      <phase>prepare-package</phase>
      <goals><goal>copy</goal></goals>
      <configuration>
        <artifactItems>
          <artifactItem>
            <groupId>org.jacoco</groupId>
            <artifactId>org.jacoco.agent</artifactId>
            <version>0.8.12</version>
            <classifier>runtime</classifier>
            <destFileName>jacocoagent.jar</destFileName>
          </artifactItem>
        </artifactItems>
        <outputDirectory>${project.build.directory}/jacoco</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

2. **Fügen Sie eine Liberty JVM-Option hinzu** (Datei: `wlp/usr/servers/<serverName>/jvm.options`)

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=file,append=false,includes=com.myco.*,excludes=org.slf4j.*,destfile=${server.output.dir}/jacoco/jacoco-it.exec
```

* Legen Sie `jacocoagent.jar` in `wlp/usr/servers/<serverName>/jacoco/` ab (oder einen anderen lesbaren Pfad).
* Passen Sie `includes`/`excludes` an Ihre Pakete an.

3. **Ablauf**

* Starten Sie Liberty (`server start <serverName>`), deployen Sie das EAR.
* Führen Sie Ihre Python-`unittest` aus (sie rufen die Endpunkte auf).
* Stoppen Sie Liberty (`server stop <serverName>`).
  → Der Agent schreibt `${server.output.dir}/jacoco/jacoco-it.exec`.

4. **Bericht generieren**

* Wenn Ihr Projekt ein Multi-Modul-Projekt ist (EAR + EJB + WAR), verwenden Sie einen Aggregator-Pom und `report-aggregate`:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-aggregate</goal></goals>
      <configuration>
        <dataFile>${env.SERVER_OUTPUT_DIR}/jacoco/jacoco-it.exec</dataFile>
        <includes>
          <include>com/myco/**</include>
        </includes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

(Oder verwenden Sie `jacococli`:)

```bash
java -jar jacococli.jar report /path/to/jacoco-it.exec \
  --classfiles module1/target/classes --classfiles module2/target/classes \
  --sourcefiles module1/src/main/java --sourcefiles module2/src/main/java \
  --html target/jacoco-it-report
```

---

## 2) Live-Dump ohne Liberty zu stoppen (TCP-Server-Modus)

**Verwenden Sie dies, wenn:** Liberty weiterlaufen soll und Sie die Abdeckung bei Bedarf abrufen möchten.

1. `jvm.options`:

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=tcpserver,address=*,port=6300,append=false,includes=com.myco.*
```

2. Liberty starten, Python-Tests ausführen, dann **dumpen**:

```bash
# holt die Abdeckung per TCP und schreibt ein .exec lokal
java -jar jacococli.jar dump --address 127.0.0.1 --port 6300 --destfile jacoco-it.exec --reset
```

Generieren Sie nun den Bericht wie oben.
Tipp: `--reset` setzt die Zähler zurück, sodass Sie während eines langen Laufs mehrere Snapshots machen können.

---

## 3) Container / CI (Umgebungsvariablen-Stil)

* Wenn Sie Liberty in Docker/K8s ausführen, mounten Sie den Agenten und setzen Sie:

  * `jvm.options` wie oben, **oder**
  * `WLP_JAVA_OPTIONS` / `JAVA_TOOL_OPTIONS` Umgebungsvariable, die denselben `-javaagent=...` enthält.
* Für Cluster mit mehreren Liberty-JVMs geben Sie jedem einen eindeutigen TCP-Port oder Dateipfad und **führen Sie sie zusammen**:

```bash
java -jar jacococli.jar merge node1.exec node2.exec --destfile merged.exec
```

---

## Hinweise & Fallstricke

* **EAR-Layout ist für JaCoCo irrelevant**; es instrumentiert Bytecode im Speicher. Für die Berichterstellung werden nur die **ursprünglichen Klassendateien** aus Ihren Modulen (`target/classes`) und deren Quellen für die hübsche HTML-Ausgabe benötigt.
* Verwenden Sie **aktuelles JaCoCo (0.8.12+)** für Java 17/21 Kompatibilität (Liberty läuft oft auf OpenJ9/HotSpot – beides ist in Ordnung).
* Achten Sie auf `includes/excludes`, um Third-Party-Bibliotheken nicht zu zählen.
* Wenn die `.exec`-Datei leer ist, haben Sie wahrscheinlich:

  * den Agenten nicht angehängt,
  * Ihre Pakete herausgefiltert,
  * oder den Dump abgerufen, bevor Traffic den Code erreicht hat.

---

Wenn Sie das Modullayout Ihres EARs teilen (EJB/WAR-Module und Paketwurzeln), kann ich eine genaue `report-aggregate`-Konfiguration und ein kleines Skript einfügen, um: Liberty zu starten → Python-Tests auszuführen → Dump zu holen → HTML-Bericht in einem Durchgang zu erstellen.