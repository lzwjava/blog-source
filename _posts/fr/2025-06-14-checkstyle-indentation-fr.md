---
audio: false
generated: true
lang: fr
layout: post
title: Détection de l'indentation dans Checkstyle
translated: true
type: note
---

Je comprends que vous vous demandez pourquoi Checkstyle ne détecte pas l'indentation manquante avant l'instruction `System.out.println` dans votre méthode `logAfter`. Décomposons cela étape par étape pour identifier le problème et le résoudre.

### Pourquoi Checkstyle ne détecte-t-il pas le problème d'indentation ?
Checkstyle utilise des modules spécifiques pour appliquer les standards de codage, et pour l'indentation, il s'appuie sur le module `Indentation`. Si ce module n'est pas correctement configuré ou inclus dans votre configuration Checkstyle, il ne détectera pas les erreurs d'indentation comme celle dans votre code.

Voici votre code actuel :

```java
package org.lzwjava;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
    System.out.println("Method executed: " + joinPoint.getSignature());  // Pas d'indentation
    }
}
```

Selon les conventions Java standard, les instructions à l'intérieur d'une méthode (comme `System.out.println`) doivent être indentées par rapport à la déclaration de la méthode. Dans votre code, la ligne `System.out.println` n'a pas d'indentation, ce que Checkstyle devrait signaler comme une erreur s'il est correctement configuré. Voici les raisons les plus probables pour lesquelles cela n'est pas détecté :

1. **Le module `Indentation` n'est pas inclus** dans votre fichier de configuration Checkstyle (par exemple, `checks.xml`).
2. **Le module est inclus mais mal configuré**, il n'applique donc pas les règles d'indentation attendues.
3. **Votre configuration exclut certains fichiers ou packages**, empêchant la vérification de s'exécuter sur ce code.
4. **Il y a un problème avec la façon dont Checkstyle est exécuté** (par exemple, via Maven ou un IDE), qui remplace le comportement attendu.

Abordons ces possibilités pour résoudre le problème.

---

### Étape 1 : Vérifier le module `Indentation` dans votre configuration
Commencez par vérifier votre fichier de configuration Checkstyle (probablement `checks.xml`) pour voir si le module `Indentation` est inclus. Voici comment :

1. **Localisez votre fichier `checks.xml`**. Il se trouve généralement dans votre répertoire de projet (par exemple, `/home/lzw/Projects/blog-server/checks.xml` si vous utilisez une configuration similaire).
2. **Recherchez le module `Indentation`** dans la section `TreeWalker`. Il devrait ressembler à ceci :

   ```xml
   <module name="TreeWalker">
       <!-- Autres vérifications -->
       <module name="Indentation">
           <property name="basicOffset" value="4"/>  <!-- 4 espaces par niveau d'indentation -->
           <property name="lineWrappingIndentation" value="4"/>  <!-- Optionnel : pour les lignes multiples -->
       </module>
       <!-- Autres vérifications -->
   </module>
   ```

   - **Si vous ne voyez pas ce module**, c'est le problème — Checkstyle ne vérifie pas du tout l'indentation.
   - **S'il est présent**, vérifiez que `basicOffset` est défini sur une valeur raisonnable (par exemple, 4 espaces, ce qui est standard pour Java).

---

### Étape 2 : Ajouter ou corriger le module `Indentation`
Si le module est manquant ou mal configuré, voici comment le corriger :

#### S'il est manquant : Ajoutez le module `Indentation`
Ajoutez ce qui suit dans la section `TreeWalker` de votre `checks.xml` :

```xml
<module name="Indentation">
    <property name="basicOffset" value="4"/>  <!-- 4 espaces est typique -->
    <property name="lineWrappingIndentation" value="4"/>
</module>
```

#### S'il est présent : Vérifiez les paramètres
Assurez-vous que :
- `basicOffset` est défini sur le nombre d'espaces que vous attendez pour l'indentation (par exemple, 4).
- Aucune propriété ne désactive ou ne remplace la vérification d'une manière qui ignore votre code.

Sauvegardez le fichier après avoir apporté les modifications.

---

### Étape 3 : Vérifier les exclusions
Parfois, les configurations Checkstyle excluent certains fichiers ou packages. Dans votre `checks.xml`, recherchez :
- Un `SuppressionFilter` ou `SuppressionCommentFilter` qui pourrait ignorer le package `org.lzwjava` ou ce fichier spécifique.
- Tous les motifs qui excluent les fichiers `.java` ou des répertoires spécifiques.

Si vous trouvez une telle exclusion affectant votre code, supprimez-la ou ajustez-la pour que `DebugAspect.java` soit vérifié.

---

### Étape 4 : Tester la correction
Après avoir mis à jour votre configuration, exécutez à nouveau Checkstyle. Si vous utilisez Maven, par exemple :

```bash
mvn clean checkstyle:check
```

Vérifiez la sortie. Vous devriez voir une erreur comme :

```
[ERROR] DebugAspect.java:13: 'System.out.println' should be indented +4 spaces relative to its enclosing block.
```

Cela indiquerait que Checkstyle détecte maintenant l'indentation manquante. Pour référence, voici comment votre code *devrait* apparaître avec une indentation correcte :

```java
@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());  // Indentation de 4 espaces
    }
}
```

---

### Étape 5 : Dépannage si cela ne fonctionne toujours pas
Si Checkstyle ne signale toujours pas le problème :
- **Exécutez avec une sortie de débogage** : Utilisez une commande verbeuse pour voir ce que fait Checkstyle :
  ```bash
  mvn -X checkstyle:check
  ```
  Recherchez les messages concernant le module `Indentation` ou les fichiers ignorés.
- **Testez avec une configuration minimale** : Créez un `checks.xml` temporaire avec uniquement la vérification `Indentation` :
  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE module PUBLIC
      "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
      "https://checkstyle.org/dtds/configuration_1_3.dtd">
  <module name="Checker">
      <module name="TreeWalker">
          <module name="Indentation">
              <property name="basicOffset" value="4"/>
          </module>
      </module>
  </module>
  ```
  Pointez Checkstyle vers ce fichier et testez à nouveau pour isoler le problème.
- **Vérifiez votre configuration** : Si vous exécutez Checkstyle via un IDE (comme IntelliJ ou Eclipse), assurez-vous que l'IDE utilise le `checks.xml` mis à jour et non une ancienne configuration ou une configuration séparée.

---

### Conclusion
Checkstyle ne détecte pas l'indentation manquante car le module `Indentation` est probablement manquant ou mal configuré dans votre `checks.xml`. En ajoutant ou en corrigeant ce module et en vous assurant qu'aucune exclusion ne s'applique, Checkstyle devrait signaler le manque d'indentation avant `System.out.println`. Mettez à jour votre configuration comme indiqué, réexécutez Checkstyle, et vous devriez voir l'erreur signalée comme prévu. Faites-moi savoir si vous avez besoin d'aide pour les prochaines étapes !