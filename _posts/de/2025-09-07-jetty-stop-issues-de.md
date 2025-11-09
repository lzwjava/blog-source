---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Behebung von Problemen beim Stoppen einer Forked Jetty
translated: true
type: note
---

Du hast eigentlich die meisten Dinge richtig gemacht – das Hängen liegt fast immer daran, dass **das Stop-Ziel den geforkten Jetty nicht erreichen kann** (falscher stopHost/Port/Key-Bereich) oder daran, dass **`run-forked` Maven unerwartet attached hält**. Zwei solide Lösungen unten; wähle eine.

### Option A — Zuverlässiges Muster: `jetty:start` (Daemon) + `jetty:stop`

Dies umgeht `run-forked` vollständig und ist das stabilste für IT-Lifecycles.

**Was zu ändern ist**

1.  Pinnen der Plugin-Version und Verwenden von `start` mit `daemon=true` in `pre-integration-test`.
2.  Behalte deine Python-ITs in `integration-test`.
3.  Verwende `stop` in `post-integration-test`.
4.  Stelle *dieselben* `stopHost/stopPort/stopKey` in **beiden** Executions bereit.

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <configuration>
    <httpConnector>
      <port>8080</port>
      <host>127.0.0.1</host>
    </httpConnector>
  </configuration>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>start</goal>
      </goals>
      <configuration>
        <daemon>true</daemon>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**Warum dies das "Hängen" behebt**

*   `daemon=true` sorgt dafür, dass `start` die Kontrolle sofort an Maven zurückgibt, sodass deine ITs laufen können.
*   Übereinstimmende `stopHost/stopPort/stopKey` garantieren, dass der `stop`-Mojo denselben Jetty erreicht.
*   Keine Abhängigkeit vom Monitor-Thread-Verhalten von `run-forked`.

---

### Option B — Behalte `run-forked`, aber sorge dafür, dass stop tatsächlich funktioniert

Wenn du `run-forked` bevorzugst, sind die häufigen Fallstricke:

*   `stopHost`-Standardwerte können sich davon unterscheiden, wie das Child sich bindet (IPv6 vs. IPv4).
*   `stopPort/stopKey` werden nur in der Start-Execution gesetzt, aber **nicht** in der Stop-Execution gespiegelt.
*   Child stellt keinen Stop-Handler bereit, wenn die Konfiguration falsch platziert ist.

**Konfiguration straffer gestalten:**

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>run-forked</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>

        <httpConnector>
          <host>127.0.0.1</host>
          <port>8080</port>
        </httpConnector>

        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**Zusätzliche Sicherungen**

*   Füge `-Djava.net.preferIPv4Stack=true` zu den Child-`jvmArgs` hinzu, wenn dein macOS/Java IPv6 wählt und das Stop-Goal IPv4 verwendet:

    ```
    <jvmArgs>
      -Djava.net.preferIPv4Stack=true
      -javaagent:...
    </jvmArgs>
    ```
*   Stelle sicher, dass nichts anderes auf `8081` läuft. Wenn doch, ändere sowohl Start als auch Stop auf einen anderen freien Port.
*   Wenn deine ITs abstürzen oder hängen, wird `post-integration-test` möglicherweise nie ausgeführt; füge in diesem Fall einen Kill-Fallback in der `verify`-Phase hinzu (siehe unten).

---

### Optionale Absicherung — Child killen, wenn `stop` fehlschlägt

Füge einen kleinen Helfer hinzu, der den geforkten Jetty gewaltsam über eine in eine Datei geschriebene PID beendet:

1.  In der `run-forked`/`start`-Konfiguration:

```
<pidFile>${project.build.directory}/jetty.pid</pidFile>
```

2.  Nach `post-integration-test`, füge einen `exec-maven-plugin` in `verify` hinzu, der die PID-Datei prüft und den Prozess killt, falls er noch läuft.

---

### Ein paar kleinere Anmerkungen von deinem Log

*   `No Spring WebApplicationInitializer types detected` ist normal, wenn du `web.xml` + DispatcherServlet verwendest; steht nicht im Zusammenhang mit dem Stop-Hängen.
*   Erwäge, ITs zum **maven-failsafe-plugin** zu verschieben (bindet an `integration-test`/`verify`) und behalte Unit-Tests bei surefire. Dein aktueller `exec-maven-plugin`-Ansatz funktioniert, aber failsafe integriert sich besser in den IT-Lifecycle.

---

Wenn du möchtest, poste deinen **vollständigen** Jetty-Plugin-Block + alle `settings.xml` Mirrors (für den lokalen Repo-Pfad) und ich passe den exakten minimalen Diff für dein Repo an.