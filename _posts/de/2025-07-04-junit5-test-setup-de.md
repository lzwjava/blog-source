---
audio: false
generated: true
lang: de
layout: post
title: JUnit 5 dateibasierte Testkonfiguration
translated: true
type: note
---

Hier ist eine vereinfachte Einrichtung, die **ausschließlich JUnit 5** (ohne Mockito) zum Testen deiner Algorithmus-Lösungen mit Eingabedateien (`1.in`) verwendet:

---

### 1. Aktualisiere `pom.xml` (Nur JUnit)
```xml
<dependencies>
    <!-- JUnit 5 -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.9.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.9.2</version>
        <scope>test</scope>
    </dependency>
</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M7</version>
        </plugin>
    </plugins>
</build>
```

---

### 2. Verzeichnisstruktur
```
src/
├── main/
│   ├── java/com/algorithm/solutions/codeforces/CF123A.java  # Beispiel-Lösung
│   └── resources/codeforces/1.in                           # Eingabedatei
└── test/
    ├── java/com/algorithm/solutions/codeforces/CF123ATest.java  # Testklasse
    └── resources/codeforces/1.expected                         # Erwartete Ausgabe (optional)
```

---

### 3. Beispiel-Testklasse (`CF123ATest.java`)
```java
package com.algorithm.solutions.codeforces;

import org.junit.jupiter.api.Test;
import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

class CF123ATest {

    @Test
    void testWithInputFile() throws IOException {
        // Leite stdin von src/test/resources um
        InputStream originalIn = System.in;
        FileInputStream fileIn = new FileInputStream("src/test/resources/codeforces/1.in");
        System.setIn(fileIn);

        // Leite stdout um, um Ausgabe zu erfassen
        PrintStream originalOut = System.out;
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // Führe die Lösung aus
        CF123A.main(new String[0]);

        // Stelle Streams wieder her
        System.setIn(originalIn);
        System.setOut(originalOut);

        // Überprüfe die Ausgabe (optionaler Vergleich mit 1.expected)
        String output = outContent.toString().trim();
        assertTrue(output.endsWith("42"));  // Beispiel-Assertion
    }
}
```

---

### 4. Hauptmerkmale:
1. **Eingabeumleitung**
   - Liest `1.in` aus `src/test/resources` als `System.in`.
   - Verwendet `ByteArrayOutputStream`, um `System.out` zu erfassen.

2. **Ausgabeverifizierung**
   - Assertion gegen erwartete Ausgabe (oder Überprüfung von Schlüsselmustern).

3. **Saubere Ressourcenbehandlung**
   - Stellt ursprüngliche `System.in`/`System.out` nach dem Test wieder her.

---

### 5. Tests ausführen
```bash
mvn test
```
Oder über die IDE (IntelliJ/Eclipse/VSCode).

---

### 6. Alternative: Parametrisierte Tests (Mehrere Eingaben)
```java
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

@ParameterizedTest
@CsvFileSource(resources = "/codeforces/test_cases.csv", numLinesToSkip = 1)
void testMultipleCases(String input, String expected) {
    System.setIn(new ByteArrayInputStream(input.getBytes()));
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    System.setOut(new PrintStream(out));

    CF123A.main(new String[0]);

    assertEquals(expected, out.toString().trim());
}
```
Erstelle `src/test/resources/codeforces/test_cases.csv`:
```csv
input,expected
1 2 3,6
4 5 6,15
```

---

Dies bietet dir einen **schlanken Testaufbau** mit:
- Keinen Mockito-Abhängigkeiten
- Eingabe-/Ausgabeumleitung
- IDE-/Maven-Kompatibilität
- Unterstützung für dateibasiertes Testen

Lass mich wissen, wenn du dies für ein bestimmtes Problem anpassen möchtest!