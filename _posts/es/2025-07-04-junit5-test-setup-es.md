---
audio: false
generated: true
lang: es
layout: post
title: Configuración de Pruebas Basadas en Archivos con JUnit 5
translated: true
type: note
---

Aquí tienes una configuración simplificada que utiliza **solo JUnit 5** (sin Mockito) para probar tus soluciones de algoritmos con archivos de entrada (`1.in`):

---

### 1. Actualizar `pom.xml` (Solo JUnit)
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

### 2. Estructura de Directorios
```
src/
├── main/
│   ├── java/com/algorithm/solutions/codeforces/CF123A.java  # Ejemplo de solución
│   └── resources/codeforces/1.in                           # Archivo de entrada
└── test/
    ├── java/com/algorithm/solutions/codeforces/CF123ATest.java  # Clase de prueba
    └── resources/codeforces/1.expected                         # Salida esperada (opcional)
```

---

### 3. Clase de Prueba de Ejemplo (`CF123ATest.java`)
```java
package com.algorithm.solutions.codeforces;

import org.junit.jupiter.api.Test;
import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

class CF123ATest {

    @Test
    void testWithInputFile() throws IOException {
        // Redirigir stdin desde src/test/resources
        InputStream originalIn = System.in;
        FileInputStream fileIn = new FileInputStream("src/test/resources/codeforces/1.in");
        System.setIn(fileIn);

        // Redirigir stdout para capturar la salida
        PrintStream originalOut = System.out;
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // Ejecutar la solución
        CF123A.main(new String[0]);

        // Restaurar streams
        System.setIn(originalIn);
        System.setOut(originalOut);

        // Verificar la salida (opcionalmente comparar con 1.expected)
        String output = outContent.toString().trim();
        assertTrue(output.endsWith("42"));  // Ejemplo de aserción
    }
}
```

---

### 4. Características Clave:
1. **Redirección de Entrada**  
   - Lee `1.in` desde `src/test/resources` como `System.in`.
   - Utiliza `ByteArrayOutputStream` para capturar `System.out`.

2. **Verificación de Salida**  
   - Realiza aserciones contra la salida esperada (o verifica patrones clave).

3. **Manejo Limpio de Recursos**  
   - Restaura el `System.in`/`System.out` original después de la prueba.

---

### 5. Ejecutar Pruebas
```bash
mvn test
```
O mediante el IDE (IntelliJ/Eclipse/VSCode).

---

### 6. Alternativa: Pruebas Parametrizadas (Múltiples Entradas)
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
Crear `src/test/resources/codeforces/test_cases.csv`:
```csv
input,expected
1 2 3,6
4 5 6,15
```

---

Esto te proporciona una **configuración de pruebas ligera** con:
- Sin dependencias de Mockito
- Redirección de entrada/salida
- Compatibilidad con IDE/Maven
- Soporte para pruebas basadas en archivos

¡Avísame si necesitas adaptar esto para un problema específico!