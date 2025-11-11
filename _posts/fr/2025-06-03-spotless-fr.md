---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de Spotless pour formater le code
translated: true
type: note
---

Il n'existe pas de commande `mvn checkstyle:format` dans le Maven Checkstyle Plugin. Ce plugin est principalement conçu pour vérifier le code par rapport à une configuration Checkstyle et rapporter les violations, et non pour formater automatiquement le code. Cependant, vous pouvez réaliser le formatage de code basé sur une configuration Checkstyle en utilisant d'autres outils comme Spotless ou le Maven Formatter Plugin, qui peuvent être configurés pour s'aligner sur vos règles Checkstyle.

Ci-dessous, je vais expliquer comment formater le code en fonction de votre configuration Checkstyle en utilisant le **Spotless Maven Plugin**, car c'est un choix populaire pour cet usage et il peut s'intégrer avec les règles Checkstyle.

### Solution : Utilisation de Spotless avec une Configuration Checkstyle

Le Spotless Maven Plugin peut formater le code Java selon un fichier de configuration Checkstyle (par exemple, `checkstyle.xml`). Voici comment le configurer :

#### 1. Ajouter Spotless à votre `pom.xml`
Ajoutez le plugin Spotless à votre `pom.xml` et configurez-le pour utiliser votre fichier de configuration Checkstyle.

```xml
<build>
  <plugins>
    <plugin>
      <groupId>com.diffplug.spotless</groupId>
      <artifactId>spotless-maven-plugin</artifactId>
      <version>2.43.0</version> <!-- Utilisez la dernière version -->
      <configuration>
        <java>
          <!-- Pointez vers votre fichier de configuration Checkstyle -->
          <googleJavaFormat>
            <version>1.22.0</version> <!-- Optionnel : Utilisez une version spécifique -->
            <style>GOOGLE</style> <!-- Ou AOSP, ou omettre pour la valeur par défaut -->
          </googleJavaFormat>
          <formatAnnotations>
            <!-- Utilisez la configuration Checkstyle pour le formatage -->
            <checkstyle>
              <file>${project.basedir}/checkstyle.xml</file> <!-- Chemin vers votre config Checkstyle -->
              <version>10.17.0</version> <!-- Correspond à votre version de Checkstyle -->
            </checkstyle>
          </formatAnnotations>
        </java>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>apply</goal> <!-- Formate automatiquement le code -->
          </goals>
          <phase>process-sources</phase> <!-- Optionnel : Liez à une phase -->
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### 2. Assurez-vous que votre Configuration Checkstyle Existe
Assurez-vous d'avoir un fichier `checkstyle.xml` dans votre projet (par exemple, dans le répertoire racine ou un sous-répertoire). Ce fichier définit les standards de codage (par exemple, indentation, espaces, etc.) que Spotless utilisera pour formater votre code. Si vous utilisez un standard comme Google Java Format, vous pouvez le référencer, ou utiliser une configuration Checkstyle personnalisée adaptée à votre projet.

Exemple d'extrait de `checkstyle.xml` pour des règles de formatage basiques :
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
    </module>
  </module>
</module>
```

#### 3. Exécutez Spotless pour Formater le Code
Pour formater votre code en fonction de la configuration Checkstyle, exécutez :
```bash
mvn spotless:apply
```

Cette commande formatera tous les fichiers Java de votre projet selon les règles définies dans votre configuration Checkstyle et tous les paramètres de formatage supplémentaires (par exemple, Google Java Format).

#### 4. Vérifiez le Formatage avec Checkstyle
Après le formatage, vous pouvez exécuter `mvn checkstyle:check` pour vérifier que le code formaté est conforme à vos règles Checkstyle. Si vous avez suivi le conseil précédent de définir `<failOnViolation>false</failOnViolation>`, cela rapportera toute violation restante sans arrêter la build.

### Alternative : Maven Formatter Plugin
Si vous préférez ne pas utiliser Spotless, vous pouvez utiliser le **Maven Formatter Plugin**, qui prend également en charge le formatage basé sur des règles mais est moins couramment utilisé avec des configurations Checkstyle directement. Voici une configuration basique :

```xml
<build>
  <plugins>
    <plugin>
      <groupId>net.revelc.code.formatter</groupId>
      <artifactId>formatter-maven-plugin</artifactId>
      <version>2.23.0</version> <!-- Utilisez la dernière version -->
      <configuration>
        <configFile>${project.basedir}/checkstyle.xml</configFile> <!-- Chemin vers la config Checkstyle -->
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>format</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

Exécutez le formatage avec :
```bash
mvn formatter:format
```

### Notes
- **Aucune Commande de Formatage Checkstyle Directe** : Le Checkstyle Maven Plugin ne fournit pas de goal `format`. Des outils comme Spotless ou le Formatter Plugin sont nécessaires pour appliquer le formatage basé sur les règles Checkstyle.
- **Compatibilité des Versions de Checkstyle** : Assurez-vous que la version de Checkstyle spécifiée dans Spotless (ou Formatter) correspond à la version utilisée dans votre plugin Checkstyle pour éviter les incompatibilités de règles.
- **Règles Checkstyle Personnalisées** : Votre `checkstyle.xml` doit inclure des règles liées au formatage (par exemple, `Indentation`, `WhitespaceAround`, etc.) pour que Spotless les applique correctement.
- **Projets Multi-Modules** : Dans un projet Maven multi-modules, vous pouvez placer la configuration Spotless/Formatter dans le `pom.xml` parent pour l'appliquer à tous les modules, ou la configurer par module selon les besoins.
- **Vérifiez Après le Formatage** : Exécutez toujours `mvn checkstyle:check` après le formatage pour confirmer la conformité, surtout si vous avez des règles non liées au formatage (par exemple, longueur de méthode, complexité) dans votre configuration Checkstyle.

Si vous n'avez pas de `checkstyle.xml` ou si vous avez besoin d'aide pour en créer un, faites-le moi savoir et je pourrai fournir un exemple ou vous guider davantage ! De plus, si vous préférez un outil différent ou avez des exigences de formatage spécifiques, veuillez les partager et j'adapterai la solution.