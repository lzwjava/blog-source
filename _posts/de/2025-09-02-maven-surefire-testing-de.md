---
audio: false
generated: true
image: false
lang: de
layout: post
title: Maven Surefire Plugin Einheitstest Handbuch
translated: true
type: note
---

Das **Maven Surefire Plugin** ist das Plugin, das Ihre Unit-Tests während der **test**-Phase des Maven-Build-Lebenszyklus ausführt. Es ist eines der am häufigsten verwendeten Maven-Plugins, da nahezu jedes Projekt automatisiertes Testing benötigt, das in den Build integriert ist.

---

## Was es ist

* **Name**: `maven-surefire-plugin`
* **Zweck**: Führt Tests aus, die mit Frameworks wie JUnit (3, 4, 5), TestNG, etc. geschrieben wurden.
* **Phase**: Ist an die `test`-Phase des Standard-Lebenszyklus von Maven gebunden.
* **Ausgabe**: Erzeugt Testberichte (standardmäßig in `target/surefire-reports`).

---

## Wie es funktioniert

1. Wenn Sie `mvn test` oder `mvn package` ausführen, ruft Maven das Surefire-Plugin auf.
2. Es scannt Ihr `src/test/java`-Verzeichnis nach Testklassen.
3. Standardmäßig sucht es nach Dateien, die Namenskonventionen entsprechen wie:

   * `*Test.java`
   * `Test*.java`
   * `*Tests.java`
   * `*TestCase.java`
4. Führt sie in einem isolierten Classloader aus.
5. Schreibt die Ergebnisse nach `target/surefire-reports` (Klartext, XML und manchmal HTML über Reporting-Plugins).

---

## Grundlegende Verwendung

Sie können es in Ihrer `pom.xml` konfigurieren:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version> <!-- use latest stable -->
    </plugin>
  </plugins>
</build>
```

Danach führen Sie einfach aus:

```bash
mvn test
```

---

## Häufige Konfigurationen

* **Include-/Exclude-Patterns**:

```xml
<configuration>
  <includes>
    <include>**/*MyTest.java</include>
  </includes>
  <excludes>
    <exclude>**/IntegrationTest.java</exclude>
  </excludes>
</configuration>
```

* **Systemeigenschaften**:

```xml
<configuration>
  <systemPropertyVariables>
    <env>dev</env>
  </systemPropertyVariables>
</configuration>
```

* **Parallele Testausführung**:

```xml
<configuration>
  <forkCount>2</forkCount>
  <reuseForks>true</reuseForks>
  <parallel>classes</parallel>
</configuration>
```

Dies führt Tests in mehreren JVM-Forks oder Threads aus.

---

## Wann man es verwendet

* Immer dann, wenn Sie **Unit-Testing** in Ihren Maven-Lebenszyklus integrieren möchten.
* Um **Unit-Tests (Surefire)** von **Integrationstests (Failsafe-Plugin)** zu trennen:

  * Surefire → Unit-Tests (`mvn test`)
  * Failsafe → Integrationstests (`mvn verify`)

---

✅ **Kurz gesagt**: `maven-surefire-plugin` ist Ihr Standard-Plugin für die Ausführung von Unit-Tests in Maven-Projekten. Sie konfigurieren es in der `pom.xml`, führen es mit `mvn test` aus und überprüfen die Berichte in `target/surefire-reports`.

---

Möchten Sie, dass ich auch den **Unterschied zwischen Surefire und Failsafe** erkläre (da sie oft verwechselt werden)?