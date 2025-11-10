---
audio: false
generated: true
lang: fr
layout: post
title: Spotless contre Checkstyle en Java
translated: true
type: note
---

Vous pouvez utiliser le **Spotless Maven Plugin** et le **Checkstyle Maven Plugin** ensemble dans un projet Java, car ils ont des objectifs complémentaires. Cependant, le fait que vous ayez *besoin* des deux dépend des exigences de votre projet. Ci-dessous, j'expliquerai comment ils peuvent fonctionner ensemble, leurs différences, et quand vous pourriez choisir l'un plutôt que l'autre.

### Différences Clés Entre Spotless et Checkstyle

| **Aspect**            | **Spotless**                                                                 | **Checkstyle**                                                              |
|-----------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Objectif**          | Formate automatiquement le code pour imposer un style cohérent et corrige les problèmes. | Analyse statiquement le code pour imposer des standards de codage et détecter les violations. |
| **Action**            | Modifie le code (ex : corrige l'indentation, l'ordre des imports, supprime les imports inutilisés). | Signale les violations sans modifier le code ; fait échouer la build si les vérifications échouent. |
| **Configuration**     | Configure des formateurs comme `palantir-java-format`, `google-java-format`, etc. | Utilise un ensemble de règles (ex : vérifications Google ou Sun) pour définir les standards de codage. |
| **Résultat**          | Fichiers source formatés (avec `mvn spotless:apply`).                        | Rapports (XML, HTML ou console) listant les violations de style.            |
| **Cas d'Usage**       | Garantit que le code est formaté de manière cohérente avant les commits ou les builds. | Impose des standards de codage et détecte des problèmes comme la complexité ou les mauvaises pratiques. |

### Utiliser Spotless et Checkstyle Ensemble

Vous pouvez combiner Spotless et Checkstyle pour obtenir à la fois un **formatage automatique** et une **application du style**. Voici comment ils se complètent :

1. **Spotless pour le Formatage** :
   - Spotless applique des règles de formatage (ex : indentation, ordre des imports) en utilisant des outils comme `palantir-java-format`.
   - Il garantit que le code est formaté de manière cohérente, réduisant l'effort manuel.
   - Exemple : Corrige une indentation de 2 espaces vs 4 espaces, trie les imports et supprime les imports inutilisés.

2. **Checkstyle pour la Validation** :
   - Checkstyle impose des standards de codage au-delà du formatage, tels que la longueur des méthodes, les conventions de nommage ou la complexité.
   - Il détecte des problèmes que les formateurs pourraient ne pas traiter, comme l'absence de Javadoc ou des méthodes trop complexes.
   - Exemple : Signale une méthode avec trop de paramètres ou impose la présence de Javadoc sur les méthodes publiques.

3. **Workflow** :
   - Exécutez d'abord Spotless (`mvn spotless:apply`) pour formater le code.
   - Puis exécutez Checkstyle (`mvn checkstyle:check`) pour vérifier la conformité avec des règles supplémentaires.
   - Cela garantit que le code est à la fois formaté et respecte des directives de style plus larges.

### Exemple de Configuration dans le `pom.xml`

Voici comment configurer les deux plugins dans votre `pom.xml` :

```xml
<build>
    <plugins>
        <!-- Spotless Plugin pour le Formatage -->
        <plugin>
            <groupId>com.diffplug.spotless</groupId>
            <artifactId>spotless-maven-plugin</artifactId>
            <version>2.43.0</version>
            <configuration>
                <java>
                    <includes>
                        <include>src/main/java/**/*.java</include>
                        <include>src/test/java/**/*.java</include>
                    </includes>
                    <palantirJavaFormat>
                        <version>2.53.0</version>
                        <style>GOOGLE</style> <!-- Utiliser le style Google -->
                    </palantirJavaFormat>
                    <indent>
                        <spacesPerTab>2</spacesPerTab> <!-- Indentation de 2 espaces -->
                    </indent>
                    <importOrder>
                        <order>java,javax,org,com,\\#</order>
                    </importOrder>
                    <removeUnusedImports/>
                    <trimTrailingWhitespace/>
                    <endWithNewline/>
                </java>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>apply</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
        </plugin>

        <!-- Checkstyle Plugin pour la Validation -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
                <configLocation>google_checks.xml</configLocation> <!-- Utiliser le style Google ou un XML personnalisé -->
                <includeTestSourceDirectory>true</includeTestSourceDirectory>
                <failOnViolation>true</failOnViolation> <!-- Faire échouer la build en cas de violation -->
                <consoleOutput>true</consoleOutput> <!-- Afficher les violations dans la console -->
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>check</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
            <dependencies>
                <!-- Spécifier la version de Checkstyle -->
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version>
                </dependency>
            </dependencies>
        </plugin>
    </plugins>
</build>
```

### Notes Importantes de Configuration

1. **Règles de Style Partagées** :
   - Pour éviter les conflits, alignez les configurations de Spotless et Checkstyle. Par exemple, utilisez `palantirJavaFormat` avec `style>GOOGLE` dans Spotless et `google_checks.xml` dans Checkstyle.
   - Téléchargez `google_checks.xml` depuis [le GitHub de Checkstyle](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) ou créez un ensemble de règles personnalisé.

2. **Ordre d'Exécution** :
   - Exécutez Spotless avant Checkstyle dans la phase `validate` pour garantir que le code est formaté avant la validation.
   - Exemple : `mvn spotless:apply checkstyle:check`.

3. **Règles Checkstyle Personnalisées** :
   - Personnalisez `google_checks.xml` ou créez le vôtre (ex : `my_checks.xml`) pour imposer des règles spécifiques, telles que :
     ```xml
     <module name="Indentation">
         <property name="basicOffset" value="2"/>
         <property name="lineWrappingIndentation" value="4"/>
     </module>
     <module name="ImportOrder">
         <property name="groups" value="java,javax,org,com"/>
         <property name="ordered" value="true"/>
         <property name="separated" value="true"/>
     </module>
     ```

4. **Éviter la Redondance** :
   - Si Spotless gère le formatage (ex : indentation, ordre des imports), désactivez les règles Checkstyle qui se chevauchent pour éviter les vérifications en double. Par exemple, désactivez le module `Indentation` de Checkstyle si Spotless impose l'indentation :
     ```xml
     <module name="Indentation">
         <property name="severity" value="ignore"/>
     </module>
     ```

### Quand Utiliser l'un ou l'autre, ou les Deux

- **Utiliser Spotless Seul** :
  - Si vous n'avez besoin que d'un formatage de code cohérent (ex : indentation, ordre des imports, espaces).
  - Idéal pour les équipes qui souhaitent un formatage automatisé sans application stricte du style.
  - Exemple : Petits projets ou équipes utilisant le formatage basé sur l'IDE.

- **Utiliser Checkstyle Seul** :
  - Si vous devez imposer des standards de codage (ex : conventions de nommage, Javadoc, complexité des méthodes) sans modifier le code.
  - Convient aux projets où les développeurs formatent manuellement le code mais ont besoin de validation.

- **Utiliser les Deux** :
  - Pour une qualité de code robuste : Spotless formate le code automatiquement, et Checkstyle détecte des problèmes supplémentaires (ex : Javadoc manquant, méthodes complexes).
  - Courant dans les grandes équipes ou les projets avec des standards de codage stricts.
  - Exemple : Projets d'entreprise ou dépôts open source exigeant un style cohérent et des vérifications de qualité.

### Considérations Pratiques

- **Performance** : L'exécution des deux plugins augmente le temps de build. Utilisez `spotless:check` (au lieu de `apply`) et `checkstyle:check` dans les pipelines d'intégration continue pour valider sans modifier le code.
- **Intégration IDE** :
  - Spotless : Utilisez les tâches Spotless Gradle/Maven ou les plugins IDE (ex : `palantir-java-format` pour IntelliJ).
  - Checkstyle : Utilisez le plugin Checkstyle-IDEA pour IntelliJ ou le plugin Eclipse Checkstyle, configuré avec le même `google_checks.xml`.
- **CI/CD** : Configurez les deux plugins dans votre pipeline d'intégration continue (ex : Jenkins, GitHub Actions) pour imposer le formatage et les vérifications de style sur les pull requests.
  ```yaml
  # Exemple de workflow GitHub Actions
  name: CI
  on: [pull_request]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Set up JDK 17
          uses: actions/setup-java@v3
          with: { java-version: '17' }
        - name: Run Spotless and Checkstyle
          run: mvn spotless:check checkstyle:check
  ```

### Conflits Potentiels et Solutions

- **Règles Qui Se Chevauchent** : Si Spotless formate le code différemment des règles de Checkstyle (ex : indentation de 2 espaces vs 4 espaces), les builds peuvent échouer. Solution : Alignez les configurations (ex : utilisez le style `GOOGLE` pour les deux).
- **Échecs de Build** : Le paramètre `failOnViolation` de Checkstyle peut faire échouer les builds si Spotless n'a pas été exécuté. Solution : Assurez-vous que Spotless s'exécute en premier ou utilisez `spotless:check` pour valider le formatage.
- **Adoption par l'Équipe** : Les développeurs peuvent résister au formatage automatique. Solution : Utilisez `spotless:check` en CI et formez l'équipe à l'intégration IDE.

### Sources

- Documentation Spotless : [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)
- Plugin Maven Checkstyle : [Site Maven](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
- Discussions communautaires sur Stack Overflow et les issues GitHub

### Conclusion

Utiliser Spotless et Checkstyle ensemble est une combinaison puissante pour maintenir la qualité du code : Spotless garantit un formatage cohérent, tandis que Checkstyle impose des standards de codage plus larges. Configurez-les pour qu'ils soient alignés (ex : mêmes règles d'indentation et d'ordre des imports) et exécutez-les séquentiellement dans votre processus de build. Si votre projet n'a besoin que de formatage, Spotless seul peut suffire ; si vous avez besoin d'une validation stricte, envisagez d'ajouter Checkstyle. Faites-moi savoir si vous avez besoin d'aide pour des configurations spécifiques ou d'un exemple de fichier `google_checks.xml` !