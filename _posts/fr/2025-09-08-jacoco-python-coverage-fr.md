---
audio: false
date: 2025-09-08
generated: true
image: false
lang: fr
layout: post
title: Stratégie de Couverture JaCoCo pour les Tests Python
translated: true
type: note
---

# Analyse et stratégie pour la couverture JaCoCo avec des tests d'intégration Python

## Analyse de la situation actuelle

Vous avez configuré un projet Maven multi-module avec :
- POM parent (`PlaygroundLib`)
- Module `PlaygroundUtils` (JAR avec des classes utilitaires)
- Module `PlaygroundWeb` (WAR avec des contrôleurs Spring MVC)

Votre objectif est d'utiliser `unittest` de Python pour tester les points de terminaison d'API et générer des rapports de couverture pour le code Java. Le défi est que les tests Python existent en dehors du projet Java, et vous devez exécuter Jetty pour servir l'application pendant les tests.

## Problèmes avec l'approche actuelle

1. **Problème d'exécutions multiples** : Vous exécutez `PlaygroundWeb` plusieurs fois pour générer des rapports de couverture séparés pour différents modules, ce qui est inefficace.

2. **Problème d'évolutivité** : Cette approche ne s'adaptera pas bien avec plus de modules. Pour un projet avec 10 modules, vous auriez besoin de 10 exécutions séparées.

3. **Fragmentation de la couverture** : Les rapports par module rendent plus difficile l'obtention d'une vue holistique de la couverture sur l'ensemble de l'application.

## Stratégie recommandée

### 1. Approche de collecte de couverture consolidée

Au lieu d'exécuter l'application plusieurs fois, je recommande :

1. **Exécuter l'application web une seule fois** avec l'agent JaCoCo attaché
2. **Exécuter tous les tests d'intégration Python** contre cette instance unique
3. **Générer un rapport de couverture consolidé** qui inclut tous les modules

Cette approche est plus efficace et fournit une vue unifiée de la couverture sur l'ensemble de votre application.

### 2. Étapes de mise en œuvre

#### Modifications du POM parent (`PlaygroundLib`)

Ajoutez un profil pour les tests d'intégration avec JaCoCo :

```xml
<profiles>
    <profile>
        <id>integration-test</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>merge</id>
                            <phase>post-integration-test</phase>
                            <goals>
                                <goal>merge</goal>
                            </goals>
                            <configuration>
                                <fileSets>
                                    <fileSet>
                                        <directory>${project.basedir}</directory>
                                        <includes>
                                            <include>*/target/jacoco-it.exec</include>
                                        </includes>
                                    </fileSet>
                                </fileSets>
                                <destFile>${project.build.directory}/jacoco-merged.exec</destFile>
                            </configuration>
                        </execution>
                        <execution>
                            <id>report-merged</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                            <configuration>
                                <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                                <outputDirectory>${project.reporting.outputDirectory}/jacoco-merged</outputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

#### Modifications du POM PlaygroundWeb

Modifiez la configuration de l'agent JaCoCo pour inclure tous les modules :

```xml
<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco-it.exec,includes=org.lzw.*
                </jvmArgs>
                <!-- Le reste de la configuration reste inchangé -->
            </configuration>
        </execution>
        <!-- Le reste des exécutions reste inchangé -->
    </executions>
</plugin>
```

Notez l'ajout de `includes=org.lzw.*` dans la configuration de l'agent JaCoCo. Cela garantit que toutes les classes du package `org.lzw` (dans tous les modules) sont incluses dans le rapport de couverture.

### 3. Flux d'exécution

Le flux d'exécution recommandé serait :

```bash
# Construire tous les modules
mvn clean install

# Exécuter les tests d'intégration avec couverture
mvn verify -Pintegration-test
```

Cela va :
1. Compiler tous les modules
2. Démarrer Jetty avec l'agent JaCoCo attaché
3. Exécuter les tests d'intégration Python
4. Arrêter Jetty
5. Générer un rapport de couverture fusionné pour tous les modules

### 4. Adaptation aux projets plus importants

Pour un projet plus important avec dix modules :

1. **Les modules web** (comme `PlaygroundWeb`) seraient configurés pour exécuter l'application avec l'agent JaCoCo attaché.
2. **Les modules utilitaires** (comme `PlaygroundUtils`) n'auraient pas besoin de configuration spéciale.
3. Le POM parent gérerait la fusion des données de couverture de tous les modules.

Si vous avez plusieurs modules web qui doivent être testés indépendamment, vous pourriez créer des profils Maven séparés pour chaque module web et exécuter les tests d'intégration pour chacun séparément, puis fusionner toutes les données de couverture au niveau parent.

### 5. Gestion de la complexité de JaCoCo

Pour gérer la complexité de JaCoCo :

1. **Encapsuler la configuration** dans des profils Maven pour garder le POM principal propre
2. **Documenter clairement le processus** pour que les membres de l'équipe comprennent comment exécuter les tests et générer les rapports
3. **Envisager l'automatisation CI/CD** pour réduire la complexité manuelle pour les développeurs

## Résumé

L'approche recommandée consolide la collecte de couverture en exécutant l'application web une seule fois avec l'agent JaCoCo attaché, en exécutant tous les tests d'intégration Python contre cette instance, et en générant un rapport de couverture consolidé. Cette approche est plus efficace, évolutive et fournit une vue unifiée de la couverture sur l'ensemble de votre application.

Cette stratégie devrait résoudre vos défis actuels et s'adapter bien à la croissance de votre projet, tout en simplifiant la gestion de la complexité de JaCoCo.