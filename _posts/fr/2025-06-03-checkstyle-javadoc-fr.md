---
audio: false
generated: true
lang: fr
layout: post
title: Désactiver les vérifications Javadoc dans Checkstyle
translated: true
type: note
---

Pour configurer Checkstyle afin d'ignorer toutes les vérifications liées à Javadoc et de les traiter comme des non-violations, vous devez modifier votre fichier de configuration Checkstyle (généralement `checkstyle.xml`) pour désactiver ou supprimer les modules liés à Javadoc. Voici comment procéder :

### Option 1 : Désactiver les vérifications liées à Javadoc
Checkstyle possède plusieurs modules liés à Javadoc, tels que `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle` et `JavadocPackage`. Pour les désactiver, assurez-vous que ces modules sont soit supprimés, soit commentés dans votre fichier de configuration. Par exemple :

```xml
<module name="Checker">
    <!-- Autres modules -->
    <!-- Commenter ou supprimer les vérifications liées à Javadoc -->
    <!--
    <module name="JavadocMethod"/>
    <module name="JavadocType"/>
    <module name="JavadocVariable"/>
    <module name="JavadocStyle"/>
    <module name="JavadocPackage"/>
    -->
</module>
```

Si ces modules ne sont pas présents dans votre configuration, Checkstyle n'appliquera pas les vérifications Javadoc.

### Option 2 : Supprimer les vérifications Javadoc à l'aide de filtres de suppression
Vous pouvez utiliser le `SuppressionFilter` de Checkstyle pour supprimer toutes les vérifications liées à Javadoc dans votre base de code. Ajoutez une règle de suppression dans un fichier de suppressions séparé (par exemple, `suppressions.xml`) et référencez-le dans votre configuration Checkstyle.

1. **Créez un fichier de suppressions** (par exemple, `suppressions.xml`) :
   ```xml
   <!DOCTYPE suppressions PUBLIC
       "-//Checkstyle//DTD Suppression DTD 1.0//EN"
       "https://checkstyle.org/dtds/suppressions_1_0.dtd">
   <suppressions>
       <!-- Supprimer toutes les vérifications liées à Javadoc -->
       <suppress checks="Javadoc.*" files=".*"/>
   </suppressions>
   ```

   Le motif `checks="Javadoc.*"` correspond à toutes les vérifications commençant par "Javadoc" (par exemple, `JavadocMethod`, `JavadocType`, etc.), et `files=".*"` applique la suppression à tous les fichiers.

2. **Référencez le fichier de suppressions dans votre configuration Checkstyle** :
   ```xml
   <module name="Checker">
       <module name="SuppressionFilter">
           <property name="file" value="suppressions.xml"/>
       </module>
       <!-- Autres modules -->
   </module>
   ```

### Option 3 : Utiliser les annotations `@SuppressWarnings`
Si vous souhaitez supprimer les vérifications Javadoc pour des classes ou méthodes spécifiques, vous pouvez utiliser l'annotation `@SuppressWarnings("checkstyle:javadoc")` dans votre code Java. Par exemple :

```java
@SuppressWarnings("checkstyle:javadoc")
public class MyClass {
    // Le code sans Javadoc ne déclenchera pas de violations
}
```

Cette approche est utile pour une suppression ciblée mais nécessite d'ajouter des annotations dans le code, ce qui peut ne pas être idéal pour désactiver globalement les vérifications Javadoc.

### Notes
- **Vérifiez votre configuration** : Après avoir modifié la configuration, exécutez Checkstyle pour vous assurer que les violations liées à Javadoc ne sont plus signalées. Par exemple, utilisez la commande :
  ```bash
  java -jar checkstyle.jar -c checkstyle.xml VosFichiersSource
  ```
- **Modules Javadoc courants** : Assurez-vous de traiter tous les modules pertinents, y compris `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle`, `JavadocPackage`, `MissingJavadocMethod`, `MissingJavadocType` et `InvalidJavadocPosition`.
- **Version de Checkstyle** : Les noms exacts des modules et la syntaxe de suppression peuvent varier légèrement selon votre version de Checkstyle. Les exemples ci-dessus sont compatibles avec Checkstyle 8.x et versions ultérieures.
- **Suppression globale** : L'approche par `SuppressionFilter` (Option 2) est généralement la manière la plus propre de désactiver toutes les vérifications Javadoc sans modifier extensivement la configuration centrale.

Si vous utilisez un outil de build spécifique comme Maven ou Gradle, faites-le-moi savoir et je pourrai fournir des conseils supplémentaires sur l'intégration de la configuration Checkstyle mise à jour !