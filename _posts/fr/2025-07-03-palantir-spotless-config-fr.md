---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de Palantir Java Format avec Spotless
translated: true
type: note
---

Pour configurer le **Palantir Java Format** avec le **Spotless Maven Plugin** dans un fichier `pom.xml`, vous devez configurer le plugin pour utiliser `palantirJavaFormat` et spécifier les options de formatage telles que l'espacement des tabulations, l'indentation, l'ordre des imports et autres paramètres. Voici un guide détaillé sur la façon de configurer ces paramètres et les options disponibles basées sur le plugin Spotless et le Palantir Java Format.

### Ajout du Spotless Maven Plugin avec Palantir Java Format

Incluez le Spotless Maven Plugin dans votre `pom.xml` et configurez-le pour utiliser `palantirJavaFormat`. Voici une configuration de base avec des paramètres courants pour l'espacement des tabulations, l'indentation, l'ordre des imports et d'autres options :

```xml
<plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
    <version>2.43.0</version> <!-- Utilisez la dernière version -->
    <configuration>
        <java>
            <!-- Spécifier les fichiers à formater (optionnel, par défaut tous les fichiers .java) -->
            <includes>
                <include>src/main/java/**/*.java</include>
                <include>src/test/java/**/*.java</include>
            </includes>
            <!-- Palantir Java Format -->
            <palantirJavaFormat>
                <version>2.53.0</version> <!-- Spécifiez la version souhaitée -->
                <style>GOOGLE</style> <!-- Options : GOOGLE, AOSP ou PALANTIR -->
                <formatJavadoc>true</formatJavadoc> <!-- Optionnel : Formater le Javadoc -->
            </palantirJavaFormat>
            <!-- Paramètres d'indentation -->
            <indent>
                <tabs>true</tabs> <!-- Utiliser les tabulations au lieu des espaces -->
                <spacesPerTab>4</spacesPerTab> <!-- Nombre d'espaces par tabulation -->
            </indent>
            <!-- Configuration de l'ordre des imports -->
            <importOrder>
                <order>java,javax,org,com,\\#</order> <!-- Ordre personnalisé des imports -->
            </importOrder>
            <!-- Supprimer les imports inutilisés -->
            <removeUnusedImports/>
            <!-- Autres paramètres optionnels -->
            <trimTrailingWhitespace/>
            <endWithNewline/>
            <toggleOffOn/> <!-- Activer les balises spotless:off et spotless:on -->
        </java>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>apply</goal> <!-- Formater automatiquement le code -->
            </goals>
            <phase>validate</phase> <!-- Exécuter pendant la phase de validation -->
        </execution>
    </executions>
</plugin>
```

### Explication des Options de Configuration

Voici une analyse des principales options de configuration pour la section `<java>` dans Spotless avec `palantirJavaFormat`, en se concentrant sur l'espacement des tabulations, l'indentation, l'ordre des imports et d'autres paramètres pertinents :

#### 1. **Palantir Java Format (`<palantirJavaFormat>`)**

- **`<version>`** : Spécifie la version de `palantir-java-format` à utiliser. Vérifiez la dernière version sur [Maven Repository](https://mvnrepository.com/artifact/com.palantir.java-format/palantir-java-format) ou [GitHub](https://github.com/palantir/palantir-java-format/releases). Exemple : `<version>2.53.0</version>`.
- **`<style>`** : Définit le style de formatage. Les options sont :
  - `GOOGLE` : Utilise le Google Java Style (indentation de 2 espaces, limite de ligne à 100 caractères).
  - `AOSP` : Utilise le style Android Open Source Project (indentation de 4 espaces, limite de ligne à 100 caractères).
  - `PALANTIR` : Utilise le style de Palantir (indentation de 4 espaces, limite de ligne à 120 caractères, formatage adapté aux lambdas).
- **`<formatJavadoc>`** : Booléen pour activer/désactiver le formatage du Javadoc (nécessite Palantir Java Format version ≥ 2.39.0). Exemple : `<formatJavadoc>true</formatJavadoc>`.
- **Custom Group Artifact** : Rarement nécessaire, mais vous pouvez spécifier un group et un artifact personnalisés pour le formateur. Exemple : `<groupArtifact>com.palantir.java-format:palantir-java-format</groupArtifact>`.

#### 2. **Indentation (`<indent>`)**

- **`<tabs>`** : Booléen pour utiliser les tabulations (`true`) ou les espaces (`false`) pour l'indentation. Exemple : `<tabs>true</tabs>`.
- **`<spacesPerTab>`** : Nombre d'espaces par tabulation (utilisé lorsque `<tabs>` est `false` ou pour l'indentation mixte). Les valeurs courantes sont `2` ou `4`. Exemple : `<spacesPerTab>4</spacesPerTab>`.
  - **Remarque** : Le style de Palantir Java Format (par exemple, `GOOGLE`, `AOSP`, `PALANTIR`) peut influencer le comportement de l'indentation. Par exemple, `GOOGLE` utilise par défaut 2 espaces, tandis que `AOSP` et `PALANTIR` utilisent 4 espaces. Les paramètres `<indent>` dans Spotless peuvent remplacer ou compléter ces valeurs par défaut, mais assurez la cohérence pour éviter les conflits.

#### 3. **Ordre des Imports (`<importOrder>`)**

- **`<order>`** : Spécifie l'ordre des groupes d'imports, séparés par des virgules. Utilisez `\\#` pour les imports statiques et une chaîne vide (`""`) pour les imports non spécifiés. Exemple : `<order>java,javax,org,com,\\#</order>` trie les imports commençant par `java`, puis `javax`, etc., avec les imports statiques en dernier.
- **`<file>`** : Alternativement, spécifiez un fichier contenant l'ordre des imports. Exemple : `<file>${project.basedir}/eclipse.importorder</file>`. Le format du fichier correspond à la configuration de l'ordre des imports d'Eclipse (par exemple, `java|javax|org|com|\\#`).
  - Exemple de contenu du fichier :
    ```
    #sort
    java
    javax
    org
    com
    \#
    ```

#### 4. **Autres Paramètres Utiles**

- **`<removeUnusedImports>`** : Supprime les imports inutilisés. Optionnellement, spécifiez le moteur :
  - Par défaut : Utilise `google-java-format` pour la suppression.
  - Alternative : `<engine>cleanthat-javaparser-unnecessaryimport</engine>` pour la compatibilité JDK8+ avec les nouvelles fonctionnalités Java (par exemple, Java 17).
- **`<trimTrailingWhitespace>`** : Supprime les espaces blancs de fin de ligne. Exemple : `<trimTrailingWhitespace/>`.
- **`<endWithNewline>`** : Garantit que les fichiers se terminent par une nouvelle ligne. Exemple : `<endWithNewline/>`.
- **`<toggleOffOn>`** : Active les commentaires `// spotless:off` et `// spotless:on` pour exclure des sections de code du formatage. Exemple : `<toggleOffOn/>`.
- **`<licenseHeader>`** : Ajoute un en-tête de licence aux fichiers. Exemple :
  ```xml
  <licenseHeader>
      <content>/* (C) $YEAR */</content>
  </licenseHeader>
  ```
  Vous pouvez également utiliser un fichier : `<file>${project.basedir}/license.txt</file>`.
- **`<formatAnnotations>`** : Garantit que les annotations de type sont sur la même ligne que les champs qu'elles décrivent. Exemple : `<formatAnnotations/>`.
- **`<ratchetFrom>`** : Limite le formatage aux fichiers modifiés par rapport à une branche Git (par exemple, `origin/main`). Exemple : `<ratchetFrom>origin/main</ratchetFrom>`.

#### 5. **Formatage Spécifique au POM (`<pom>`)**

Pour formater le fichier `pom.xml` lui-même, utilisez la section `<pom>` avec `sortPom` :
```xml
<pom>
    <sortPom>
        <nrOfIndentSpace>2</nrOfIndentSpace> <!-- Indentation pour le POM -->
        <predefinedSortOrder>recommended_2008_06</predefinedSortOrder> <!-- Ordre standard du POM -->
        <sortDependencies>groupId,artifactId</sortDependencies> <!-- Trier les dépendances -->
        <sortPlugins>groupId,artifactId</sortPlugins> <!-- Trier les plugins -->
        <endWithNewline>true</endWithNewline>
    </sortPom>
</pom>
```
- **Options pour `sortPom`** :
  - `<nrOfIndentSpace>` : Nombre d'espaces pour l'indentation (par exemple, `2` ou `4`).
  - `<predefinedSortOrder>` : Options comme `recommended_2008_06` ou `custom_1` pour l'ordre des éléments.
  - `<sortDependencies>` : Trier par `groupId`, `artifactId` ou d'autres critères.
  - `<sortPlugins>` : Trier les plugins de manière similaire.
  - `<endWithNewline>` : Garantir que le POM se termine par une nouvelle ligne.
  - `<expandEmptyElements>` : Développer les balises XML vides (par exemple, `<tag></tag>` vs `<tag/>`).

### Exécution de Spotless

- **Vérifier le formatage** : `mvn spotless:check` – Valide le code par rapport aux règles configurées, échouant la build si des violations sont trouvées.
- **Appliquer le formatage** : `mvn spotless:apply` – Formate automatiquement le code pour se conformer aux règles.

### Notes et Bonnes Pratiques

- **Cohérence avec l'IDE** : Pour aligner IntelliJ ou Eclipse avec Spotless, installez le plugin IntelliJ `palantir-java-format` ou utilisez un fichier de formateur Eclipse. Pour IntelliJ, importez un fichier de style compatible (par exemple, `intellij-java-google-style.xml` pour le style Google) ou configurez manuellement pour correspondre aux paramètres Palantir.
- **Compatibilité des Versions** : Assurez-vous que la version de `palantir-java-format` supporte votre version de Java. Pour Java 17+, utilisez une version récente (par exemple, 2.53.0). Certaines fonctionnalités comme le pattern matching peuvent avoir un support limité.
- **Formatage Personnalisé** : Pour une personnalisation avancée, utilisez un fichier XML de formateur Eclipse avec `<eclipse>` au lieu de `<palantirJavaFormat>` :
  ```xml
  <eclipse>
      <file>${project.basedir}/custom-style.xml</file>
  </eclipse>
  ```
  Exemple de `custom-style.xml` :
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <profiles version="21">
      <profile kind="CodeFormatterProfile" name="custom" version="21">
          <setting id="org.eclipse.jdt.core.formatter.tabulation.char" value="space"/>
          <setting id="org.eclipse.jdt.core.formatter.indentation.size" value="4"/>
          <setting id="org.eclipse.jdt.core.formatter.tabulation.size" value="4"/>
      </profile>
  </profiles>
  ```
- **Limitations** : Palantir Java Format est moins configurable que le formateur d'Eclipse mais est conçu pour la cohérence et les fonctionnalités Java modernes (par exemple, les lambdas). Il peut ne pas gérer tous les cas particuliers (par exemple, les lambdas profondément imbriquées).

### Résumé des Options Disponibles

| **Option**                  | **Description**                                                                 | **Exemples de Valeurs**                        |
|-----------------------------|---------------------------------------------------------------------------------|------------------------------------------------|
| `<palantirJavaFormat>`      | Configure Palantir Java Format.                                                | `<version>2.53.0</version>`, `<style>PALANTIR</style>` |
| `<indent>`                  | Définit le style d'indentation (tabulations ou espaces) et la taille.          | `<tabs>true</tabs>`, `<spacesPerTab>4</spacesPerTab>` |
| `<importOrder>`             | Définit l'ordre des groupes d'imports ou utilise un fichier.                   | `<order>java,javax,org,com,\\#</order>`        |
| `<removeUnusedImports>`     | Supprime les imports inutilisés, avec un moteur optionnel.                     | `<engine>cleanthat-javaparser-unnecessaryimport</engine>` |
| `<trimTrailingWhitespace>`  | Supprime les espaces blancs de fin de ligne.                                   | `<trimTrailingWhitespace/>`                    |
| `<endWithNewline>`         | Garantit que les fichiers se terminent par une nouvelle ligne.                | `<endWithNewline/>`                           |
| `<toggleOffOn>`            | Active les balises `spotless:off`/`spotless:on`.                              | `<toggleOffOn/>`                              |
| `<licenseHeader>`          | Ajoute un en-tête de licence.                                                 | `<content>/* (C) $YEAR */</content>`           |
| `<formatAnnotations>`       | Formate les annotations pour qu'elles soient sur la même ligne que les champs. | `<formatAnnotations/>`                         |
| `<sortPom>`                | Formate `pom.xml` avec tri et indentation.                                    | `<nrOfIndentSpace>2</nrOfIndentSpace>`        |

### Sources

- Documentation du Spotless Maven Plugin : [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)
- Palantir Java Format : [GitHub](https://github.com/palantir/palantir-java-format)
- Stack Overflow et exemples communautaires pour la configuration de Spotless

Cette configuration garantit un formatage de code cohérent avec Palantir Java Format, adapté à vos préférences pour l'espacement des tabulations, l'indentation et l'ordre des imports. Faites-moi savoir si vous avez besoin de précisions supplémentaires ou d'options complémentaires !