---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Exclure les packages com.ibm dans JaCoCo
translated: true
type: note
---

Pour exclure les packages **`com.ibm`** (ou tout autre package) de la couverture JaCoCo dans un environnement **WebSphere Liberty Profile**, vous pouvez configurer les exclusions dans votre fichier **`pom.xml`**. Cela se fait généralement dans la configuration du **plugin Maven JaCoCo**.

---

### **Comment exclure les packages `com.ibm` dans `pom.xml`**

Vous pouvez utiliser la balise `<excludes>` dans la configuration du plugin JaCoCo pour spécifier les classes ou packages à exclure du rapport de couverture.

#### **Exemple de configuration :**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version> <!-- Utilisez la dernière version -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>test</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                    <configuration>
                        <outputDirectory>${project.reporting.outputDirectory}/jacoco</outputDirectory>
                        <excludes>
                            <!-- Exclure tous les packages com.ibm -->
                            <exclude>com/ibm/**</exclude>
                        </excludes>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

---

### **Explication :**
- **`<excludes>`** : Cette section spécifie les classes ou packages à exclure du rapport de couverture.
- **`<exclude>com/ibm/**</exclude>`** : Ceci exclut toutes les classes sous le package `com.ibm` et ses sous-packages.

---

### **Notes supplémentaires :**
- Si vous souhaitez exclure plusieurs packages, ajoutez d'autres entrées `<exclude>` :
  ```xml
  <excludes>
      <exclude>com/ibm/**</exclude>
      <exclude>org/apache/**</exclude>
  </excludes>
  ```
- Si vous utilisez **JaCoCo avec WebSphere Liberty**, assurez-vous que l'agent JaCoCo est correctement configuré dans votre fichier `server.env` ou `jvm.options`, et que les exclusions dans le `pom.xml` correspondent à vos besoins.

---

### **Bonnes pratiques :**
- Vérifiez toujours les exclusions en générant un rapport de couverture et en contrôlant que les packages exclus n'y figurent pas.
- Si vous devez exclure des packages au runtime (par exemple, dans les arguments de l'agent JaCoCo), vous pouvez utiliser le paramètre `excludes` dans les arguments de l'agent :
  ```plaintext
  -javaagent:/chemin/vers/jacocoagent.jar=destfile=/chemin/vers/jacoco.exec,excludes=com.ibm.*
  ```