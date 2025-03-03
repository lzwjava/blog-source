---
audio: false
generated: true
lang: fr
layout: post
title: JaCoCo Maven Plugin
translated: true
---

Voici un guide étape par étape sur **comment utiliser le plugin JaCoCo Maven** pour mesurer la couverture de code dans un projet Java basé sur Maven. JaCoCo (Java Code Coverage) est un outil qui s'intègre à Maven pour suivre quelle partie de votre code est exercée par les tests, généralement des tests unitaires. En ajoutant et en configurant le plugin JaCoCo Maven dans votre projet, vous pouvez générer des rapports de couverture détaillés pendant le processus de construction.

---

### **Étapes pour utiliser le plugin JaCoCo Maven**

#### **1. Ajouter le plugin JaCoCo Maven à votre `pom.xml`**
Pour utiliser le plugin JaCoCo Maven, vous devez l'inclure dans la section `<build><plugins>` de votre fichier `pom.xml` du projet. Voici une configuration de base qui configure le plugin :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- Utilisez la dernière version disponible -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>verify</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`groupId`, `artifactId` et `version`** : Ces éléments identifient le plugin JaCoCo Maven. Remplacez `0.8.12` par la dernière version disponible sur [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin).
- **`<executions>`** : Cette section configure quand et comment le plugin s'exécute pendant le cycle de vie de construction de Maven :
  - **`<goal>prepare-agent</goal>`** : Prépare l'agent JaCoCo pour collecter les données de couverture pendant l'exécution des tests. Par défaut, il est lié à une phase précoce (comme `initialize`) et ne nécessite pas de phase explicite sauf si personnalisé.
  - **`<goal>report</goal>`** : Génère le rapport de couverture après que les tests ont été exécutés. Il est lié à la phase `verify` ici, qui se produit après la phase `test`, garantissant que toutes les données de test sont disponibles.

#### **2. Assurez-vous que les tests sont configurés**
Le plugin JaCoCo fonctionne en analysant l'exécution des tests, généralement des tests unitaires exécutés par le plugin Maven Surefire. Dans la plupart des projets Maven, Surefire est inclus par défaut et exécute les tests situés dans `src/test/java`. Aucune configuration supplémentaire n'est nécessaire sauf si vos tests sont non standard. Vérifiez que :
- Vous avez des tests unitaires écrits (par exemple, en utilisant JUnit ou TestNG).
- Le plugin Surefire est présent (il est hérité du POM parent Maven par défaut dans la plupart des cas).

Si vous devez configurer explicitement Surefire, cela pourrait ressembler à ceci :

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- Utilisez la dernière version -->
</plugin>
```

Le but `prepare-agent` configure l'agent JaCoCo en modifiant la propriété `argLine`, que Surefire utilise pour exécuter les tests avec le suivi de couverture activé.

#### **3. Exécuter la construction Maven**
Pour générer le rapport de couverture, exécutez la commande suivante dans le répertoire de votre projet :

```bash
mvn verify
```

- **`mvn verify`** : Cela exécute toutes les phases jusqu'à `verify`, y compris `compile`, `test` et `verify`. Le plugin JaCoCo fera :
  1. Préparer l'agent avant l'exécution des tests.
  2. Collecter les données de couverture pendant la phase `test` (lorsque Surefire exécute les tests).
  3. Générer le rapport pendant la phase `verify`.

Alternativement, si vous souhaitez uniquement exécuter les tests sans passer à `verify`, utilisez :

```bash
mvn test
```

Cependant, puisque le but `report` est lié à `verify` dans cette configuration, vous devrez exécuter `mvn verify` pour voir le rapport. Si vous préférez que le rapport soit généré pendant `mvn test`, vous pouvez changer la `<phase>` pour l'exécution `report` à `test`, bien que `verify` soit une convention courante.

#### **4. Voir le rapport de couverture**
Après avoir exécuté `mvn verify`, JaCoCo génère un rapport HTML par défaut. Vous pouvez le trouver à :

```
target/site/jacoco/index.html
```

- Ouvrez ce fichier dans un navigateur web pour voir un décompte détaillé de la couverture de code, y compris les pourcentages pour les packages, les classes, les méthodes et les lignes.
- Le rapport inclut également des formats XML et CSV dans le même répertoire (`jacoco.xml` et `jacoco.csv`), utiles pour l'intégration avec des outils comme les systèmes CI.

---

### **Personnalisations optionnelles**
Pour des cas d'utilisation plus avancés, vous pouvez ajuster la configuration du plugin :

- **Exclure des classes ou des packages** :
  Pour exclure certains codes de l'analyse de couverture (par exemple, le code généré), ajoutez une section `<configuration>` :

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  Placez ceci à l'intérieur de la balise `<plugin>`, au-dessus de `<executions>`.

- **Imposer des seuils de couverture** :
  Pour échouer la construction si la couverture tombe en dessous d'un seuil, ajoutez le but `check` :

  ```xml
  <execution>
      <id>check</id>
      <phase>verify</phase>
      <goals>
          <goal>check</goal>
      </goals>
      <configuration>
          <rules>
              <rule>
                  <element>BUNDLE</element>
                  <limits>
                      <limit>
                          <counter>LINE</counter>
                          <value>COVEREDRATIO</value>
                          <minimum>0.80</minimum> <!-- 80% de couverture de ligne -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **Changer le répertoire de sortie du rapport** :
  Pour personnaliser l'emplacement du rapport, ajoutez :

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **Résumé**
Pour utiliser le plugin JaCoCo Maven :
1. Ajoutez le plugin à votre `pom.xml` avec les buts `prepare-agent` et `report`.
2. Assurez-vous que votre projet a des tests configurés (généralement via Surefire).
3. Exécutez `mvn verify` pour générer le rapport de couverture.
4. Vérifiez le rapport à `target/site/jacoco/index.html`.

Cette configuration fournit une méthode simple pour intégrer la couverture de code dans votre processus de construction Maven, vous aidant à évaluer l'efficacité de vos tests. Pour la dernière version du plugin ou des configurations avancées, consultez la [documentation officielle JaCoCo](https://www.jacoco.org/jacoco/trunk/doc/maven.html).