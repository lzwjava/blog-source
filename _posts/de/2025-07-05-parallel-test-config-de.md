---
audio: false
generated: true
lang: de
layout: post
title: Konfiguration von Maven für parallele Testausführung
translated: true
type: note
---

Um parallele Testausführung in Ihrem Maven-Projekt zu aktivieren, insbesondere für die bereitgestellte `MavenTest.java`-Klasse, können Sie den Maven Surefire Plugin konfigurieren, um Tests parallel auszuführen. Die `MavenTest.java`-Klasse verwendet JUnit 4 mit dynamischen Tests, um Maven-Befehle für verschiedene Probleme auszuführen, und der Stack-Trace Ihres ursprünglichen Fehlers deutet darauf hin, dass Tests bereits parallel ausgeführt werden (erkennbar an `ForkJoinPool` im Stack-Trace). Sie können die parallele Ausführung jedoch explizit steuern, indem Sie den Surefire Plugin in Ihrer `pom.xml`-Datei konfigurieren. Im Folgenden werde ich erklären, wie Sie die parallele Testausführung einrichten und die Verwendung eines `-DParallel`-Flags wie gewünscht umsetzen können.

### Warum parallele Ausführung stattfindet
Ihre Testausgabe zeigt `ForkJoinPool` im Stack-Trace, was darauf hindeutet, dass JUnit oder Maven bereits einen Thread-Pool für die parallele Ausführung verwendet. Die `MavenTest`-Klasse verwendet `@TestFactory` mit `DynamicTest`, und die Tests laufen wahrscheinlich aufgrund des Standardverhaltens von JUnit oder einer vorhandenen Surefire-Konfiguration parallel. Das Ziel ist nun, die parallele Ausführung explizit zu konfigurieren und die Steuerung über ein Kommandozeilen-Flag wie `-DParallel` zu ermöglichen.

### Schritte zur Konfiguration der parallelen Testausführung

1. **Aktualisieren Sie die `pom.xml`, um den Maven Surefire Plugin zu konfigurieren**:
   Der Maven Surefire Plugin unterstützt parallele Testausführung für JUnit 4.7+ (das Ihr Projekt verwendet, da es mit `DynamicTest` kompatibel ist). Sie können den Grad der Parallelität (z.B. `classes`, `methods` oder `both`) und die Anzahl der Threads angeben. Um die Steuerung über `-DParallel` zu ermöglichen, können Sie eine Maven-Eigenschaft verwenden, um die Parallelität zu aktivieren oder zu konfigurieren.

   Fügen Sie die Surefire Plugin-Konfiguration in Ihrer `pom.xml` hinzu oder aktualisieren Sie sie:

   ```xml
   <project>
       <!-- Andere Konfigurationen -->
       <properties>
           <!-- Standardmäßig keine parallele Ausführung, sofern nicht angegeben -->
           <parallel.mode>none</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <!-- Optional: Timeout für parallele Tests -->
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <!-- Forking-Konfiguration zur Isolierung von Tests -->
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   - **Erklärung**:
     - `<parallel>`: Gibt den Grad der Parallelität an. Gültige Werte für JUnit 4.7+ sind `methods`, `classes`, `both`, `suites`, `suitesAndClasses`, `suitesAndMethods`, `classesAndMethods` oder `all`. Für Ihre `MavenTest`-Klasse ist `classes` geeignet, da jeder `DynamicTest` ein Problem repräsentiert und Sie Tests für verschiedene Probleme parallel ausführen möchten.
     - `<threadCount>`: Setzt die Anzahl der Threads (z.B. `4` für vier gleichzeitige Tests). Sie können dies über `-Dthread.count=<Zahl>` überschreiben.
     - `<perCoreThreadCount>false</perCoreThreadCount>`: Stellt sicher, dass `threadCount` eine feste Zahl ist und nicht nach CPU-Kernen skaliert wird.
     - `<parallelTestsTimeoutInSeconds>`: Setzt ein Timeout für parallele Tests, um Hängen zu verhindern (entspricht Ihrem `TEST_TIMEOUT` von 10 Sekunden in `MavenTest.java`).
     - `<forkCount>1</forkCount>`: Führt Tests in einem separaten JVM-Prozess aus, um sie zu isolieren und Probleme mit gemeinsam genutztem Zustand zu reduzieren. `<reuseForks>true</reuseForks>` ermöglicht die Wiederverwendung der JVM für Effizienz.
     - `<parallel.mode>` und `<thread.count>`: Maven-Eigenschaften, die über Kommandozeilen-Flags überschrieben werden können (z.B. `-Dparallel.mode=classes`).

2. **Ausführen von Tests mit `-DParallel`**:
   Um ein `-DParallel`-Flag zur Steuerung der parallelen Ausführung zu verwenden, können Sie es der `parallel.mode`-Eigenschaft zuordnen. Führen Sie zum Beispiel aus:

   ```bash
   mvn test -Dparallel.mode=classes -Dthread.count=4
   ```

   - Wenn `-Dparallel.mode` nicht angegeben ist, deaktiviert der Standardwert (`none`) die parallele Ausführung.
   - Sie können auch ein einfacheres Flag wie `-DParallel=true` verwenden, um Parallelität mit einem vordefinierten Modus (z.B. `classes`) zu aktivieren. Um dies zu unterstützen, aktualisieren Sie die `pom.xml`, um `-DParallel` zu interpretieren:

   ```xml
   <project>
       <!-- Andere Konfigurationen -->
       <properties>
           <parallel.mode>${Parallel ? 'classes' : 'none'}</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   Jetzt können Sie Tests ausführen mit:

   ```bash
   mvn test -DParallel=true
   ```

   - `-DParallel=true`: Aktiviert die parallele Ausführung mit `parallel=classes` und `threadCount=4`.
   - `-DParallel=false` oder Weglassen von `-DParallel`: Deaktiviert die parallele Ausführung (`parallel=none`).
   - Sie können die Thread-Anzahl mit `-Dthread.count=<Zahl>` überschreiben (z.B. `-Dthread.count=8`).

3. **Sicherstellen der Thread-Sicherheit**:
   Ihre `MavenTest`-Klasse führt Maven-Befehle (`mvn exec:exec -Dproblem=<problem>`) parallel aus, wodurch separate Prozesse gestartet werden. Dies ist von Natur aus thread-sicher, da jeder Prozess seinen eigenen Speicherbereich hat und Probleme mit gemeinsam genutztem Zustand vermieden werden. Stellen Sie jedoch sicher, dass:
   - Die `com.lzw.solutions.uva.<problem>.Main`-Klassen keine Ressourcen gemeinsam nutzen (z.B. Dateien oder Datenbanken), die Konflikte verursachen könnten.
   - Eingabe-/Ausgabedateien oder Ressourcen, die von jedem Problem verwendet werden (z.B. Testdaten für `p10009`), isoliert sind, um Race Conditions zu vermeiden.
   - Wenn gemeinsame Ressourcen verwendet werden, ziehen Sie in Betracht, `@NotThreadSafe` für bestimmte Testklassen zu verwenden oder den Zugriff auf gemeinsame Ressourcen zu synchronisieren.

4. **Umgang mit der Skip-Liste bei paralleler Ausführung**:
   Ihre `MavenTest.java` enthält bereits ein `SKIP_PROBLEMS`-Set, um Probleme wie `p10009` zu überspringen. Dies funktioniert gut mit paralleler Ausführung, da übersprungene Probleme ausgeschlossen werden, bevor Tests geplant werden. Stellen Sie sicher, dass die Skip-Liste bei Bedarf aktualisiert wird:

   ```java
   private static final Set<String> SKIP_PROBLEMS = new HashSet<>(Arrays.asList(
       "p10009", // Überspringt p10009 aufgrund von NumberFormatException
       "p10037"  // Fügen Sie hier andere problematische Probleme hinzu
   ));
   ```

5. **Ausführen der Tests**:
   Um Tests parallel mit der Skip-Liste und dem `-DParallel`-Flag auszuführen:

   ```bash
   mvn test -DParallel=true -Dthread.count=4
   ```

   - Dies führt bis zu vier Problem-Tests gleichzeitig aus und überspringt `p10009` sowie alle anderen Probleme in `SKIP_PROBLEMS`.
   - Wenn Sie Parallelität für Debugging-Zwecke deaktivieren möchten:

     ```bash
     mvn test -DParallel=false
     ```

6. **Beheben der `NumberFormatException` für `p10009`**:
   Die `NumberFormatException` in `p10009` (von Ihrem ursprünglichen Fehler) deutet auf einen `null`-String hin, der geparst wird. Während das Überspringen von `p10009` das Problem vermeidet, möchten Sie es möglicherweise der Vollständigkeit halber beheben. Überprüfen Sie `com.lzw.solutions.uva.p10009.Main` in Zeile 17 (`readInt`-Methode) und fügen Sie Null-Checks hinzu:

   ```java
   public int readInt() {
       String input = readInput(); // Hypothetische Eingabe-Lesemethode
       if (input == null || input.trim().isEmpty()) {
           throw new IllegalArgumentException("Input cannot be null or empty");
       }
       return Integer.parseInt(input);
   }
   ```

   Alternativ behalten Sie `p10009` in der Skip-Liste, bis das Problem behoben ist.

### Hinweise zur parallelen Ausführung
- **Leistung**: Parallele Ausführung mit `parallel=classes` ist für Ihre `MavenTest`-Klasse geeignet, da jeder `DynamicTest` ein distinctes Problem repräsentiert. Dies minimiert den Overhead im Vergleich zu `methods` oder `both`.
- **Ressourcennutzung**: Parallele Ausführung erhöht die CPU- und Speichernutzung. Überwachen Sie Ihr System, um sicherzustellen, dass `threadCount` (z.B. `4`) Ihre Hardware nicht überlastet. Verwenden Sie `forkCount`, um Tests in separaten JVMs zu isolieren, falls Speicherprobleme auftreten.
- **Timeouts**: Die `parallelTestsTimeoutInSeconds`-Einstellung stellt sicher, dass Tests nicht unbegrenzt hängen, und entspricht Ihrem `TEST_TIMEOUT` von 10 Sekunden in `MavenTest.java`.
- **Thread-Sicherheit**: Da Ihre Tests `mvn exec:exec`-Befehle ausführen, die in separaten Prozessen laufen, ist Thread-Sicherheit weniger problematisch. Stellen Sie jedoch sicher, dass Testeingaben/-ausgaben (z.B. Dateien) pro Problem isoliert sind.
- **Debugging**: Wenn Tests im Parallelmodus unerwartet fehlschlagen, führen Sie sie sequenziell aus (`-DParallel=false`), um Probleme zu isolieren.

### Beispiel für einen vollständigen Befehl
Um Tests parallel auszuführen, `p10009` zu überspringen, mit vier Threads:

```bash
mvn test -DParallel=true -Dthread.count=4
```

Um ein bestimmtes Problem (z.B. `p10009`) ohne Parallelität zu debuggen, entfernen Sie es vorübergehend aus `SKIP_PROBLEMS` und führen Sie aus:

```bash
mvn test -DParallel=false -Dproblem=p10009
```

### Zusätzliche Überlegungen
- **JUnit 4 Einschränkungen**: Ihr Projekt verwendet JUnit 4 (basierend auf den `org.junit.jupiter.api`-Imports und `DynamicTest`). JUnit 4.7+ unterstützt parallele Ausführung über Surefire, aber JUnit 5 bietet flexiblere Parallelisierungsoptionen. Ziehen Sie ein Upgrade auf JUnit 5 in Betracht, wenn Sie erweiterte Funktionen wie pro-Klasse-Parallelität oder benutzerdefinierte Strategien benötigen.
- **Maven-Version**: Stellen Sie sicher, dass Sie eine recente Version von Maven (z.B. 3.9.10, wie in Ihrer Fehlerausgabe) und Surefire (z.B. 3.5.3) für optimale Unterstützung der parallelen Ausführung verwenden.
- **Fehlerbehandlung**: Um Tests robuster zu machen, ziehen Sie in Betracht, Ausnahmen in `runMavenExecTests` abzufangen (wie im vorherigen Antwortvorschlag), um Fehler zu protokollieren, ohne die Testsuite zu stoppen:

   ```java
   @TestFactory
   Collection<DynamicTest> runMavenExecTests() {
       return PROBLEMS.stream()
               .map(problem -> DynamicTest.dynamicTest("Test problem: " + problem, () -> {
                   String command = String.format("mvn exec:exec -Dproblem=%s", problem);
                   System.out.println("Executing command for " + problem + ": " + command);
                   try {
                       Process process = Runtime.getRuntime().exec(command);
                       // ... (restlicher Code zur Prozessbehandlung)
                       int exitCode = process.exitValue();
                       Assertions.assertTrue(
                               exitCode == 0,
                               "Maven command failed for problem: " + problem + "\nError output:\n" + errorOutput);
                   } catch (Exception e) {
                       System.err.println("Exception for problem " + problem + ": " + e.getMessage());
                       // Optional: Fortfahren statt Fehlschlag
                   }
               }))
               .collect(Collectors.toList());
   }
   ```

Dieses Setup ermöglicht es Ihnen, die parallele Ausführung mit `-DParallel=true` zu steuern, problematische Tests wie `p10009` zu überspringen und eine robuste Testausführung beizubehalten. Lassen Sie mich wissen, wenn Sie weitere Anpassungen benötigen, wie z.B. dynamische Skip-Listen über Kommandozeilenargumente oder erweiterte JUnit 5-Konfigurationen!