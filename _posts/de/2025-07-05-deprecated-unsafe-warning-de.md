---
audio: false
generated: true
lang: de
layout: post
title: Aktualisiere Guice, um die Warnung zu unsicherem Code zu beheben
translated: true
type: note
---

Die Warnung, die du siehst:

```
WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::staticFieldBase has been called by com.google.inject.internal.aop.HiddenClassDefiner (file:/opt/homebrew/Cellar/maven/3.9.10/libexec/lib/guice-5.1.0-classes.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.inject.internal.aop.HiddenClassDefiner
WARNING: sun.misc.Unsafe::staticFieldBase will be removed in a future release
```

Dies ist eine **Warnung von der Java Virtual Machine (JVM)**, nicht direkt von deinem Code. Sie bedeutet, dass eine von dir verwendete Bibliothek (in diesem Fall Guice, speziell die `guice-5.1.0-classes.jar`) intern eine Methode (`staticFieldBase`) aus `sun.misc.Unsafe` aufruft.

`sun.misc.Unsafe` ist eine interne API in Java, die für Low-Level-Operationen innerhalb der JDK selbst gedacht ist. Sie ist nicht Teil der standardmäßigen Java-API und ihre Verwendung wird nicht empfohlen, da sie zu instabilem oder undefiniertem Verhalten führen kann und in zukünftigen Java-Versionen geändert oder entfernt werden kann. Die JVM warnt dich, dass diese spezielle Methode als "endgültig veraltet" markiert ist und entfernt wird. Das bedeutet, sie wird letztendlich dazu führen, dass deine Anwendung abstürzt, wenn die Bibliothek sie weiterhin ohne Alternative verwendet.

**Wie du diese Warnung "entfernst":**

Du kannst sie nicht direkt durch Ändern deines Codes "entfernen", da die Verwendung innerhalb einer Drittanbieter-Bibliothek (Guice) liegt. Hier sind deine Optionen, nach Priorität geordnet:

1.  **Guice aktualisieren (Am meisten empfohlen):**
    Die beste und nachhaltigste Lösung ist, auf eine neuere Version von Guice zu aktualisieren, die `sun.misc.Unsafe` nicht mehr verwendet oder auf die standardmäßigen Java-APIs wie `VarHandle` (eingeführt in JDK 9) oder die Foreign Function & Memory API (JEP 454, Standard in JDK 22) migriert ist.

    Wenn man sich die Version `guice-5.1.0-classes.jar` ansieht, scheinst du Guice 5.1.0 zu verwenden. Überprüfe die offiziellen Guice-Releases und deren Dokumentation auf Updates, die speziell die Verwendung von `sun.misc.Unsafe` in neueren Java-Versionen behandeln. Oft sind die Bibliotheksbetreuer sich dieser Veraltungen bewusst und bieten aktualisierte Versionen an.

      * **Aktion:** Ändere deine `pom.xml`, um eine neuere Guice-Version zu verwenden. Du musst die neueste stabile Version von Guice finden, die mit deiner Java-Version (in deinem Fall JDK 21) kompatibel ist.

    ```xml
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>LATEST_GUICE_VERSION</version> </dependency>
    ```

    Möglicherweise musst du `guice-assistedinject` oder andere Guice-Module einbinden, falls dein Projekt sie verwendet.

2.  **Die Warnung unterdrücken (Vorübergehende Problemumgehung - Langfristig nicht empfohlen):**
    Auch wenn du dich langfristig nicht darauf verlassen solltest, kannst du die Warnung zur Laufzeit unterdrücken, wenn sie rein kosmetisch ist und die Funktionalität deiner Anwendung *vorerst* nicht beeinträchtigt. Dies geschieht über JVM-Kommandozeilenargumente.

    Für JDK 24 (dein aktuelles Ziel ist 21, aber das ist gut zu wissen, da Java fortschreitet) ist der Standard `warn`. Um sie zu unterdrücken, kannst du ihn explizit auf `allow` setzen:

    Du kannst dies zu deiner `exec-maven-plugin`-Konfiguration hinzufügen:

    ```xml
    <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
            <executable>bash</executable>
            <arguments>
                <argument>-c</argument>
                <argument>java --add-opens java.base/sun.misc=ALL-UNNAMED --sun-misc-unsafe-memory-access=allow -cp ${project.build.directory}/classes com.lzw.solutions.uva.${problem}.Main &lt; src/main/resources/uva/${problem}/1.in</argument>
            </arguments>
        </configuration>
    </plugin>
    ```

    *Selbstkorrektur:* Die Hauptwarnung betrifft, dass `sun.misc.Unsafe::staticFieldBase` als "endgültig veraltet" markiert ist, nicht illegalen reflektierenden Zugriff. Daher ist `--add-opens java.base/sun.misc=ALL-UNNAMED` hier möglicherweise nicht notwendig, es sei denn, du erhieltest auch "Illegal reflective access"-Warnungen. Das direktere Flag für die "terminally deprecated"-Warnung ist `--sun-misc-unsafe-memory-access=allow`.

    **Dies ist jedoch eine vorübergehende Lösung.** Dieses Flag weist die JVM lediglich an, die Verwendung der `sun.misc.Unsafe`-Methoden ohne Ausgabe der Warnung zu erlauben. Es löst *nicht* das zugrundeliegende Problem, dass `sun.misc.Unsafe` letztendlich entfernt wird und deine Anwendung in zukünftigen JDK-Versionen möglicherweise nicht mehr funktioniert.

3.  **An die Guice-Betreuer melden (Bereits von der Warnung vorgeschlagen):**
    Die Warnung selbst schlägt vor: "Please consider reporting this to the maintainers of class `com.google.inject.internal.aop.HiddenClassDefiner`." Auch wenn du eine bestimmte Version verwendest, wäre es für die Community vorteilhaft, wenn du das Problem meldest, sofern es in den neuesten Guice-Versionen (in denen es eigentlich behoben sein sollte) weiterhin besteht.

**Zusammenfassend ist die beste Vorgehensweise, deine Guice-Abhängigkeit zu aktualisieren.** Die `sun.misc.Unsafe`-API ist ein sich ständig änderndes Ziel, und Bibliotheken müssen sich an die neueren, sichereren und offiziell unterstützten APIs anpassen, die von Java bereitgestellt werden.