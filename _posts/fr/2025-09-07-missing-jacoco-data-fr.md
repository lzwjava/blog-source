---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Résolution de l'absence du fichier de données d'exécution JaCoCo
translated: true
type: note
---

Pour générer le fichier de données d'exécution JaCoCo, souvent appelé **fichier '.exec'**, vous devez exécuter vos tests avec l'agent JaCoCo attaché. Le message de journal "Skipping JaCoCo execution due to missing execution data file" indique que l'objectif `report` a été exécuté sans que l'objectif `prepare-agent` n'ait été préalablement exécuté avec succès.

-----

### Étape 1 : Configurer le Plugin Maven JaCoCo

Assurez-vous d'abord que votre fichier `pom.xml` contient une configuration correcte du plugin Maven JaCoCo. Il devrait ressembler à ceci :

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.12</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

L'objectif **`prepare-agent`** est crucial car il configure l'agent d'exécution JaCoCo. Cet agent instrumente votre code pendant l'exécution des tests pour collecter les données de couverture.

-----

### Étape 2 : Exécuter les Tests

Après avoir configuré le plugin, exécutez votre build Maven. La commande typique pour exécuter les tests et générer le rapport est :

`mvn clean install`

Lorsque vous exécutez cette commande, Maven exécute d'abord l'objectif `prepare-agent`, qui attache l'agent JaCoCo à la JVM. Ensuite, lorsque la phase `test` s'exécute, l'agent enregistre les données de couverture de code et les sauvegarde dans un fichier, généralement situé à l'emplacement **`target/jacoco.exec`**. L'objectif `report` est ensuite exécuté ; il lit ce fichier `.exec` et génère les rapports HTML ou XML finaux.

Si vous rencontrez toujours des problèmes, vérifiez les points suivants :

  * **Structure du projet** : Assurez-vous que vos tests se trouvent dans le répertoire Maven standard `src/test/java`.
  * **Échecs des tests** : Si vos tests échouent, la construction peut s'arrêter avant que le fichier `.exec` ne puisse être généré. Résolvez d'abord tous les échecs de tests.
  * **Incompatibilité de version** : Assurez-vous que la version du plugin JaCoCo est compatible avec vos versions de Maven et Java.