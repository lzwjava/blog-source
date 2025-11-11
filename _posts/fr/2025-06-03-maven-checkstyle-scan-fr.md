---
audio: false
generated: true
lang: fr
layout: post
title: 'Maven Checkstyle : Poursuivre l''analyse'
translated: true
type: note
---

Pour que `mvn checkstyle:check` continue d'analyser tous les modules sans échouer prématurément en cas de violations, vous devez configurer le plugin Maven Checkstyle pour désactiver l'option `failOnViolation`. Par défaut, `failOnViolation` est défini sur `true`, ce qui arrête la construction dès que des violations sont détectées. Le définir sur `false` permet à l'analyse de se terminer pour tous les modules, en rapportant toutes les violations sans interrompre la construction.

### Solution
Mettez à jour votre `pom.xml` pour configurer le plugin Checkstyle comme suit :

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-checkstyle-plugin</artifactId>
      <version>3.3.1</version> <!-- Utilisez la dernière version -->
      <configuration>
        <failOnViolation>false</failOnViolation>
        <logViolationsToConsole>true</logViolationsToConsole> <!-- Optionnel : enregistre les violations dans la console -->
      </configuration>
      <executions>
        <execution>
          <id>checkstyle</id>
          <phase>validate</phase> <!-- Ou votre phase préférée -->
          <goals>
            <goal>check</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

### Explication
- **`<failOnViolation>false</failOnViolation>`** : Ce paramètre empêche la construction d'échouer lorsque des violations Checkstyle sont détectées, permettant à l'analyse de continuer pour tous les modules.
- **`<logViolationsToConsole>true</logViolationsToConsole>`** : (Optionnel) Garantit que les violations sont imprimées dans la console pour plus de visibilité, même si la construction n'échoue pas.
- **Phase d'exécution** : Le `<phase>validate</phase>` lie la vérification Checkstyle à la phase `validate` du cycle de vie Maven. Ajustez la phase (par exemple, `compile`, `verify`) si vous souhaitez qu'elle s'exécute à une étape différente.

### Exécution de la Commande
Exécutez à nouveau la commande :
```bash
mvn checkstyle:check
```
Avec `failOnViolation` défini sur `false`, Maven analysera tous les modules, rapportera toutes les violations et terminera la construction sans s'arrêter prématurément.

### Notes
- Assurez-vous d'utiliser une version récente du `maven-checkstyle-plugin` (par exemple, 3.3.1 comme indiqué). Vérifiez la dernière version sur Maven Central si nécessaire.
- Si vous travaillez sur un projet multi-modules, cette configuration s'applique à tous les modules, sauf si elle est surchargée dans un `pom.xml` enfant.
- Pour générer un rapport des violations, envisagez d'exécuter `mvn checkstyle:checkstyle` à la place, qui produit un rapport HTML sans faire échouer la construction par défaut.

Si vous avez des exigences spécifiques (par exemple, des règles Checkstyle personnalisées ou une configuration différente), faites-le-moi savoir et je pourrai adapter la solution davantage !