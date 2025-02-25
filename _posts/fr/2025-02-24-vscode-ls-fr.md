---
audio: false
lang: fr
layout: post
title: Serveur de Langage Java dans Visual Studio Code
translated: true
---

Salut ! Le paramètre `java.jdt.ls.java.home` dans Visual Studio Code (VSCode) est une option de configuration spécifique utilisée par le Java Language Server (faisant partie de l'extension "Language Support for Java(TM) by Red Hat", incluse dans le Java Extension Pack). Décomposons cela :

---

### Ce que cela signifie
- **JDT** : Signifie "Java Development Tools", initialement partie de l'IDE Eclipse. Le Java Language Server dans VSCode est basé sur le JDT d'Eclipse, qui fournit des fonctionnalités comme l'auto-complétion, le débogage et la compilation.
- **LS** : Signifie "Language Server", un processus en arrière-plan qui alimente le support Java de VSCode (par exemple, IntelliSense, vérification des erreurs).
- **`java.jdt.ls.java.home`** : Ce paramètre indique au Java Language Server quel Java Development Kit (JDK) utiliser pour ses opérations. Il est distinct du paramètre plus général `java.home`, bien qu'ils soient liés.

En résumé, `java.jdt.ls.java.home` spécifie le chemin du JDK que le Java Language Server utilise pour :
- Analyser votre code Java.
- Fournir des fonctionnalités de langage (par exemple, l'auto-complétion, aller à la définition).
- Compiler et exécuter le code dans certains cas (bien que la compilation dépende souvent d'autres paramètres ou d'outils de construction).

---

### Différences avec `java.home`
- **`java.home`** : Un paramètre général de VSCode qui pointe vers le JDK pour toutes les extensions et tâches liées à Java dans VSCode. Il est utilisé sauf s'il est remplacé par des paramètres plus spécifiques.
- **`java.jdt.ls.java.home`** : Un paramètre plus spécifique qui remplace `java.home` uniquement pour le Java Language Server. Si ce paramètre n'est pas défini, le Language Server revient à `java.home`.

Ainsi, si vous définissez `java.jdt.ls.java.home`, il prend le pas sur les opérations du Language Server, vous permettant d'utiliser un JDK différent pour les fonctionnalités de langage que, par exemple, les tâches d'exécution ou de débogage.

---

### Comment le configurer
Étant donné que vous êtes sur Windows et utilisez VSCode 1.96.4 avec le Java Extension Pack, voici comment le définir :

1. **Ouvrir les Paramètres :**
   - Appuyez sur `Ctrl + ,` pour l'interface des Paramètres, ou utilisez `Ctrl + Shift + P` et tapez **"Open Settings (JSON)"** pour éditer `settings.json`.

2. **Définir le Chemin :**
   - **Dans l'interface des Paramètres :**
     - Recherchez **"java.jdt.ls.java.home"**.
     - Entrez le chemin complet vers votre JDK (par exemple, `C:\Program Files\Java\jdk-17.0.1`).
   - **Dans settings.json :**
     - Ajoutez cette ligne (remplacez par le chemin de votre JDK) :
       ```json
       "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       ```
     - Exemple de `settings.json` :
       ```json
       {
           "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       }
       ```

3. **Vérifier le Chemin du JDK :**
   - Assurez-vous que le chemin pointe vers un dossier JDK contenant un répertoire `bin` avec `javac.exe` et `java.exe`.

4. **Recharger VSCode :**
   - Rechargez la fenêtre (`Ctrl + Shift + P` > "Reload Window") ou redémarrez VSCode pour appliquer le changement.

---

### Quand l'utiliser
Vous définiriez généralement `java.jdt.ls.java.home` si :
- Vous avez plusieurs JDK installés et souhaitez que le Language Server utilise un JDK spécifique (par exemple, JDK 17) tandis que d'autres tâches Java (comme l'exécution du code) pourraient utiliser un autre JDK via `java.home`.
- Vous résolvez des problèmes du Language Server (par exemple, il ne détecte pas le bon JDK automatiquement).
- Votre projet a des exigences spécifiques en matière de version de JDK pour les fonctionnalités de langage.

Si vous ne le définissez pas, le Language Server utilisera le JDK de `java.home` (ou la variable d'environnement système `JAVA_HOME` en dernier recours).

---

### Exemple Pratique
Supposons que vous avez JDK 8 et JDK 17 installés :
- Définissez `"java.home": "C:\\Program Files\\Java\\jdk1.8.0_291"` pour une utilisation générale.
- Définissez `"java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"` pour vous assurer que le Language Server utilise JDK 17 pour le support de la syntaxe Java moderne.

Ainsi, vous pouvez déboguer/exécuter avec JDK 8 mais obtenir un support de langage pour les fonctionnalités de JDK 17.

---

Cela clarifie-t-il les choses ? Si vous vous demandez comment cela s'intègre dans votre configuration ou si vous avez besoin d'aide pour l'ajuster davantage, faites-le moi savoir ! 😊