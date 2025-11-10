---
audio: false
generated: true
lang: fr
layout: post
title: Mise à Niveau de Guice pour Corriger l'Avertissement de Sécurité
translated: true
type: note
---

L'avertissement que vous voyez :

```
WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::staticFieldBase has been called by com.google.inject.internal.aop.HiddenClassDefiner (file:/opt/homebrew/Cellar/maven/3.9.10/libexec/lib/guice-5.1.0-classes.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.inject.internal.aop.HiddenClassDefiner
WARNING: sun.misc.Unsafe::staticFieldBase will be removed in a future release
```

Il s'agit d'un **avertissement provenant de la Java Virtual Machine (JVM)**, et non directement de votre code. Cela signifie qu'une bibliothèque que vous utilisez (dans ce cas, Guice, spécifiquement le `guice-5.1.0-classes.jar`) appelle en interne une méthode (`staticFieldBase`) de `sun.misc.Unsafe`.

`sun.misc.Unsafe` est une API interne de Java, destinée à des opérations de bas niveau au sein du JDK lui-même. Elle ne fait pas partie de l'API Java standard et son utilisation est déconseillée car elle peut entraîner un comportement instable ou indéfini, et elle est sujette à modification ou suppression dans les futures versions de Java. La JVM vous prévient que cette méthode spécifique est "terminally deprecated" (définitivement dépréciée) et sera supprimée, ce qui signifie qu'elle finira par provoquer la rupture de votre application si la bibliothèque continue de l'utiliser sans alternative.

**Comment "supprimer" cet avertissement :**

Vous ne pouvez pas directement le "supprimer" en modifiant votre code, car l'utilisation se trouve dans une bibliothèque tierce (Guice). Voici ce que vous pouvez faire, listé par ordre de préférence :

1.  **Mettre à niveau Guice (Recommandé) :**
    La meilleure et la plus durable des solutions est de passer à une version plus récente de Guice qui n'utilise plus `sun.misc.Unsafe` ou qui a migré vers les API Java standard comme `VarHandle` (introduit dans JDK 9) ou l'API Foreign Function & Memory (JEP 454, standard dans JDK 22).

    En regardant la version `guice-5.1.0-classes.jar`, il semble que vous utilisiez Guice 5.1.0. Vérifiez les versions officielles de Guice et leur documentation pour trouver des mises à jour qui traitent spécifiquement de l'utilisation de `sun.misc.Unsafe` sur les nouvelles versions de Java. Souvent, les mainteneurs des bibliothèques sont au courant de ces dépréciations et fournissent des versions mises à jour.

      * **Action :** Modifiez votre `pom.xml` pour utiliser une version plus récente de Guice. Vous devrez trouver la dernière version stable de Guice compatible avec votre version de Java (JDK 21 dans votre cas).

    ```xml
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>LATEST_GUICE_VERSION</version> </dependency>
    ```

    Vous devrez peut-être inclure `guice-assistedinject` ou d'autres modules Guice si votre projet les utilise.

2.  **Supprimer l'Avertissement (Solution Temporaire - Non Recommandée à Long Terme) :**
    Bien que vous ne devriez pas compter sur cela à long terme, vous pouvez supprimer l'avertissement au moment de l'exécution s'il est purement cosmétique et n'entrave pas la fonctionnalité de votre application *pour le moment*. Cela se fait via les arguments de ligne de commande de la JVM.

    Pour JDK 24 (votre cible actuelle est 21, mais c'est bon à savoir au fur et à mesure que Java évolue), le comportement par défaut est `warn`. Pour le supprimer, vous pouvez le définir explicitement sur `allow` :

    Vous pouvez ajouter ceci à votre configuration `exec-maven-plugin` :

    ```xml
    <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
            <executable>bash</executable>
            <arguments>
                <argument>-c</argument>
                <argument>java --add-opens java.base/sun.misc=ALL-UNNAMED --sun-misc-unsafe-memory-access=allow -cp ${project.build.directory}/classes com.lzw.solutions.uva.${problem}.Main &lt; src/main/resources/uva/${problem}/1.in</argument>
            </arguments>
        </configuration>
    </plugin>
    ```

    *Auto-correction :* L'avertissement principal concerne `sun.misc.Unsafe::staticFieldBase` étant "terminally deprecated", et non un accès réflexif illégal. Ainsi, `--add-opens java.base/sun.misc=ALL-UNNAMED` pourrait ne pas être nécessaire ici, sauf si vous receviez également des avertissements "Illegal reflective access". L'option plus directe pour l'avertissement "terminally deprecated" est `--sun-misc-unsafe-memory-access=allow`.

    **Cependant, ceci est une solution temporaire.** Ce drapeau indique simplement à la JVM d'autoriser l'utilisation des méthodes `sun.misc.Unsafe` sans imprimer l'avertissement. Il *ne résout pas* le problème sous-jacent, à savoir que `sun.misc.Unsafe` sera éventuellement supprimé, et votre application pourrait cesser de fonctionner dans les futures versions du JDK.

3.  **Signaler aux Mainteneurs de Guice (Déjà Suggéré par l'Avertissement) :**
    L'avertissement lui-même suggère "Please consider reporting this to the maintainers of class `com.google.inject.internal.aop.HiddenClassDefiner`." Bien que vous utilisiez une version spécifique, si vous pouvez confirmer que ce problème persiste dans les dernières versions de Guice (ce qui ne devrait normalement pas être le cas, car elles ont tendance à résoudre ces problèmes), le signaler serait bénéfique pour la communauté.

**En résumé, la meilleure marche à suivre est de mettre à niveau votre dépendance Guice.** L'API `sun.misc.Unsafe` est une cible mouvante, et les bibliothèques doivent s'adapter aux API plus récentes, plus sûres et officiellement prises en charge fournies par Java.