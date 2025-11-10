---
audio: false
generated: true
lang: fr
layout: post
title: Configuration des tests basés sur les fichiers avec JUnit 5
translated: true
type: note
---

Voici une configuration simplifiée utilisant **uniquement JUnit 5** (sans Mockito) pour tester vos solutions algorithmiques avec des fichiers d'entrée (`1.in`) :

---

### 1. Mettre à jour `pom.xml` (JUnit uniquement)
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

### 2. Structure des répertoires
```
src/
├── main/
│   ├── java/com/algorithm/solutions/codeforces/CF123A.java  # Exemple de solution
│   └── resources/codeforces/1.in                           # Fichier d'entrée
└── test/
    ├── java/com/algorithm/solutions/codeforces/CF123ATest.java  # Classe de test
    └── resources/codeforces/1.expected                         # Sortie attendue (optionnel)
```

---

### 3. Exemple de classe de test (`CF123ATest.java`)
```java
package com.algorithm.solutions.codeforces;

import org.junit.jupiter.api.Test;
import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

class CF123ATest {

    @Test
    void testWithInputFile() throws IOException {
        // Rediriger stdin depuis src/test/resources
        InputStream originalIn = System.in;
        FileInputStream fileIn = new FileInputStream("src/test/resources/codeforces/1.in");
        System.setIn(fileIn);

        // Rediriger stdout pour capturer la sortie
        PrintStream originalOut = System.out;
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // Exécuter la solution
        CF123A.main(new String[0]);

        // Restaurer les flux
        System.setIn(originalIn);
        System.setOut(originalOut);

        // Vérifier la sortie (comparaison optionnelle avec 1.expected)
        String output = outContent.toString().trim();
        assertTrue(output.endsWith("42"));  // Exemple d'assertion
    }
}
```

---

### 4. Fonctionnalités clés :
1. **Redirection d'entrée**  
   - Lit `1.in` depuis `src/test/resources` comme `System.in`.
   - Utilise `ByteArrayOutputStream` pour capturer `System.out`.

2. **Vérification de sortie**  
   - Assertion par rapport à la sortie attendue (ou vérification de motifs clés).

3. **Gestion propre des ressources**  
   - Restaure les `System.in`/`System.out` originaux après le test.

---

### 5. Exécuter les tests
```bash
mvn test
```
Ou via l'IDE (IntelliJ/Eclipse/VSCode).

---

### 6. Alternative : Tests paramétrés (entrées multiples)
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
Créer `src/test/resources/codeforces/test_cases.csv` :
```csv
input,expected
1 2 3,6
4 5 6,15
```

---

Cette configuration vous offre une **installation de test légère** avec :
- Aucune dépendance Mockito
- Redirection d'entrée/sortie
- Compatibilité IDE/Maven
- Prise en charge des tests basés sur des fichiers

Faites-moi savoir si vous souhaitez adapter cela pour un problème spécifique !