---
audio: false
generated: true
lang: fr
layout: post
title: Emplacement de la Configuration Checkstyle
translated: true
type: note
---

Pour résoudre les problèmes que vous rencontrez avec le `maven-checkstyle-plugin` lors de l'exécution de `mvn clean checkstyle:check`, où il ne trouve pas le fichier `checks.xml` et échoue à initialiser le module `SuppressWithNearbyTextFilter`, suivez ces étapes. Les problèmes proviennent de l'emplacement du fichier et d'une version incompatible de Checkstyle. Voici une solution complète :

---

### Étape 1 : Corriger l'emplacement du fichier `checks.xml`
L'erreur indique que le plugin ne peut pas trouver `checks.xml`. Comme il est situé à la racine de votre projet (et non dans `src/main/resources`, où le plugin le cherche généralement), vous devez lui indiquer explicitement où le trouver.

- **Action** : Mettez à jour la balise `<configLocation>` dans votre `pom.xml` pour pointer vers la racine du projet.

---

### Étape 2 : Résoudre l'erreur `SuppressWithNearbyTextFilter`
Le module `SuppressWithNearbyTextFilter` échoue à l'initialisation car la version de Checkstyle utilisée par le plugin est obsolète et ne prend pas en charge ce filtre. Vous devez mettre à niveau le plugin et spécifier une version compatible de Checkstyle.

- **Action** : Mettez à niveau le `maven-checkstyle-plugin` vers la version `3.3.1` et ajoutez une dépendance vers la version `10.17.0` de Checkstyle, qui prend en charge `SuppressWithNearbyTextFilter`.

---

### Configuration mise à jour du `pom.xml`
Modifiez la section `maven-checkstyle-plugin` dans votre `pom.xml` comme suit :

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.1</version> <!-- Mise à niveau vers la dernière version -->
    <configuration>
        <configLocation>${project.basedir}/checks.xml</configLocation> <!-- Pointe vers checks.xml à la racine du projet -->
    </configuration>
    <dependencies>
        <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>10.17.0</version> <!-- Prend en charge SuppressWithNearbyTextFilter -->
        </dependency>
    </dependencies>
    <executions>
        <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### Explication :
- **`<configLocation>${project.basedir}/checks.xml</configLocation>`** : Spécifie que `checks.xml` se trouve à la racine du projet (`${project.basedir}` est une propriété Maven pour le répertoire racine).
- **`version 3.3.1`** : Utilise une version plus récente du plugin pour une meilleure compatibilité.
- **Dépendance Checkstyle `10.17.0`** : Garantit que le plugin utilise une version de Checkstyle qui inclut `SuppressWithNearbyTextFilter`.

---

### Étape 3 : Vérifier la configuration de `checks.xml`
Assurez-vous que le module `SuppressWithNearbyTextFilter` dans votre `checks.xml` est correctement défini. Un exemple de configuration pourrait ressembler à ceci :

```xml
<module name="SuppressWithNearbyTextFilter">
    <property name="nearbyTextPattern" value="@SuppressWarnings"/>
</module>
```

- **Action** : Vérifiez `checks.xml` pour détecter les fautes de frappe ou les propriétés incorrectes. Référez-vous à la [documentation Checkstyle](https://checkstyle.org/filters/suppresswithnearbytextfilter.html) pour plus de détails.
- **Conseil de dépannage** : Si l'erreur persiste, supprimez temporairement le module `SuppressWithNearbyTextFilter` de `checks.xml` et exécutez `mvn checkstyle:check` pour voir si le problème est spécifique à ce filtre.

---

### Étape 4 : Tester la correction
- Exécutez la commande suivante pour tester :
  ```bash
  mvn clean checkstyle:check
  ```
- Si cela fonctionne, le plugin devrait trouver `checks.xml` et traiter tous les modules sans erreurs.
- Pour vous assurer que Checkstyle s'exécute pendant la compilation, utilisez :
  ```bash
  mvn compile
  ```

---

### Optionnel : Emplacement alternatif du fichier
Si vous préférez une configuration Maven plus standard :
- Déplacez `checks.xml` vers `src/main/resources/checks.xml`.
- Mettez à jour `<configLocation>` avec :
  ```xml
  <configLocation>classpath:checks.xml</configLocation>
  ```
- Cela respecte la convention Maven qui consiste à placer les ressources dans `src/main/resources`.

---

### Notes supplémentaires
- **Avertissement sans rapport** : Si vous voyez un avertissement concernant une balise `<blocked>` dans `/usr/share/maven/conf/settings.xml`, cela n'est pas lié à ce problème mais suggère un problème dans votre fichier de configuration Maven. Examinez-le séparément si nécessaire.
- **Vous rencontrez toujours des problèmes ?** Partagez les éléments suivants pour une aide supplémentaire :
  - Le contenu (ou un extrait) de `checks.xml`.
  - La sortie complète de `mvn clean checkstyle:check -X` (mode debug).

---

En appliquant ces modifications, le `maven-checkstyle-plugin` devrait correctement localiser `checks.xml` et prendre en charge le `SuppressWithNearbyTextFilter`, résolvant ainsi vos erreurs.

---

L'erreur que vous avez rencontrée précédemment indiquait que le `maven-checkstyle-plugin` ne pouvait pas trouver `checks.xml` dans le classpath et échouait ensuite en raison d'un problème avec le module `SuppressWithNearbyTextFilter`. D'après votre structure de projet mise à jour, il semble que `checks.xml` se trouve à la racine du projet (`~/Projects/blog-server/checks.xml`), et non dans `src/main/resources` comme supposé précédemment. Cela explique pourquoi le plugin ne pouvait pas le trouver lorsqu'il était configuré avec `<configLocation>classpath:checks.xml</configLocation>` ou `<configLocation>checks.xml</configLocation>`, car ces paramètres s'attendent à trouver le fichier dans le classpath (généralement `src/main/resources`).

Pour corriger cela et garantir que le `maven-checkstyle-plugin` s'exécute avec `mvn compile` en utilisant votre `checks.xml` personnalisé à la racine du projet, vous devez mettre à jour `<configLocation>` pour pointer vers le chemin absolu ou relatif du fichier. De plus, vous devez résoudre le problème `SuppressWithNearbyTextFilter` en garantissant la compatibilité avec la version de Checkstyle. Voici la solution étape par étape.

### Configuration mise à jour du `pom.xml`
Modifiez le `maven-checkstyle-plugin` dans votre `pom.xml` pour référencer `checks.xml` à la racine du projet et utiliser une version compatible de Checkstyle pour prendre en charge `SuppressWithNearbyTextFilter`.

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*.xml</include>
                <include>**/*.yaml</include>
            </includes>
        </resource>
    </resources>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.4.2</version>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M8</version>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.3.1</version> <!-- Dernière version pour une meilleure compatibilité -->
            <configuration>
                <configLocation>${project.basedir}/checks.xml</configLocation> <!-- Pointe vers checks.xml à la racine du projet -->
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version> <!-- Prend en charge SuppressWithNearbyTextFilter -->
                </dependency>
            </dependencies>
            <executions>
                <execution>
                    <id>checkstyle-check</id>
                    <phase>compile</phase>
                    <goals>
                        <goal>check</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### Explication des modifications
1. **`<configLocation>` mise à jour** :
   - Changé en `${project.basedir}/checks.xml` pour pointer vers `checks.xml` à la racine du projet (`~/Projects/blog-server/checks.xml`).
   - `${project.basedir}` résout le répertoire contenant `pom.xml`, garantissant que le plugin trouve le fichier indépendamment du classpath.

2. **Version du plugin mise à niveau** :
   - Mise à jour de `maven-checkstyle-plugin` vers `3.3.1` (dernière version en juin 2025) pour une meilleure compatibilité et correction de bogues.

3. **Dépendance Checkstyle ajoutée** :
   - Ajout de `<dependency>` pour Checkstyle `10.17.0`, qui inclut la prise en charge de `SuppressWithNearbyTextFilter`. La version par défaut de Checkstyle dans `maven-checkstyle-plugin:3.1.1` (`8.29`) ne prend pas en charge ce filtre, ce qui causait l'erreur précédente.

4. **Conservation de `<phase>compile</phase>`** :
   - Garantit que `checkstyle:check` s'exécute pendant `mvn compile`, comme demandé.

5. **Section Resources** :
   - Conservation de la section `<resources>` pour garantir le traitement des fichiers `src/main/resources` (comme `application.yaml`), bien que cela ne soit pas directement lié à `checks.xml` puisqu'il se trouve maintenant à la racine du projet.

### Vérifier le contenu de `checks.xml`
L'erreur concernant `SuppressWithNearbyTextFilter` suggère que votre `checks.xml` référence ce filtre. Assurez-vous qu'il est correctement configuré. Un exemple valide :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
    <module name="SuppressWithNearbyTextFilter">
        <!-- Exemple de propriétés, ajustez si nécessaire -->
        <property name="nearbyTextPattern" value="@SuppressWarnings"/>
    </module>
    <module name="TreeWalker">
        <!-- Autres vérifications -->
        <module name="ConstantName"/>
    </module>
</module>
```

- **Vérification** : Ouvrez `checks.xml` à `~/Projects/blog-server/checks.xml` et vérifiez que `SuppressWithNearbyTextFilter` est correctement orthographié et inclut les propriétés requises (voir [documentation Checkstyle](https://checkstyle.org/filters/suppresswithnearbytextfilter.html)).
- **Action** : Si vous n'êtes pas sûr, supprimez temporairement la section `<module name="SuppressWithNearbyTextFilter"/>` et testez pour isoler le problème.

### Tester la configuration
1. **Nettoyer le projet** :
   ```bash
   mvn clean
   ```
   Cela supprime le répertoire `target`, y compris `checkstyle-checker.xml` et `checkstyle-result.xml`, garantissant qu'aucun artefact obsolète n'interfère.

2. **Exécuter Checkstyle** :
   ```bash
   mvn checkstyle:check
   ```
   Cela teste la configuration Checkstyle indépendamment.

3. **Exécuter la compilation** :
   ```bash
   mvn compile
   ```
   Cela devrait exécuter Checkstyle (en raison de la liaison à la phase `compile`) puis compiler si aucune violation ne fait échouer la build.

### Déboguer si les problèmes persistent
Si vous rencontrez des erreurs :
1. **Vérifier le chemin du fichier** :
   - Confirmez que `checks.xml` existe à `~/Projects/blog-server/checks.xml`.
   - Vérifiez que le nom du fichier est exactement `checks.xml` (sensible à la casse, sans extension cachée).

2. **Exécuter avec les logs de débogage** :
   ```bash
   mvn clean checkstyle:check -X
   ```
   Recherchez les messages concernant le chargement de `checks.xml` ou l'initialisation de `SuppressWithNearbyTextFilter`. Partagez la sortie pertinente si l'erreur persiste.

3. **Tester avec un `checks.xml` minimal** :
   Remplacez temporairement `checks.xml` par une configuration minimale pour écarter les problèmes liés au contenu du fichier :
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE module PUBLIC
       "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
       "https://checkstyle.org/dtds/configuration_1_3.dtd">
   <module name="Checker">
       <module name="TreeWalker">
           <module name="ConstantName"/>
       </module>
   </module>
   ```
   Exécutez ensuite `mvn checkstyle:check`. Si cela fonctionne, le problème vient de `SuppressWithNearbyTextFilter` ou d'autres modules dans votre `checks.xml` original.

### Notes supplémentaires
- **Avertissement Settings.xml** : Votre sortie montre un avertissement concernant une balise `<blocked>` non reconnue dans `/usr/share/maven/conf/settings.xml`. Cela n'est pas lié au problème Checkstyle mais indique un problème potentiel avec votre configuration Maven. Vérifiez la ligne 164 de `/usr/share/maven/conf/settings.xml` et supprimez ou corrigez la balise `<blocked>`, car ce n'est pas un élément standard des paramètres Maven.
- **Emplacement alternatif du fichier** : Si vous préférez, vous pouvez déplacer `checks.xml` vers `src/main/resources/checks.xml` et revenir à `<configLocation>` avec `classpath:checks.xml`. Cela est plus conventionnel pour les projets Maven, car les ressources sont automatiquement incluses dans le classpath.
- **Échec en cas de violation** : Si les violations Checkstyle font échouer la build et que vous souhaitez autoriser la compilation à continuer, ajoutez `<failOnViolation>false</failOnViolation>` à la `<configuration>` du plugin :
  ```xml
  <configuration>
      <configLocation>${project.basedir}/checks.xml</configLocation>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

### Vérification
Après avoir appliqué les modifications :
1. Exécutez `mvn clean compile` et confirmez que :
   - Checkstyle s'exécute en utilisant `checks.xml` de la racine du projet.
   - Aucune erreur ne se produit liée à `checks.xml` ou `SuppressWithNearbyTextFilter`.
   - La compilation continue si Checkstyle réussit ou est configuré pour ne pas faire échouer la build.
2. Vérifiez `target/checkstyle-result.xml` pour les résultats de Checkstyle.

Si l'erreur persiste, veuillez partager :
- Le contenu (ou un extrait pertinent) de `checks.xml`.
- La sortie de débogage de `mvn clean checkstyle:check -X`.
- Toute règle Checkstyle spécifique que vous essayez d'appliquer avec `SuppressWithNearbyTextFilter`.