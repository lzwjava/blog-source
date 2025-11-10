---
audio: false
generated: true
image: false
lang: fr
layout: post
title: JaCoCo pour la Couverture JVM Liberty
translated: true
type: note
---

Vous pouvez le faire — attachez JaCoCo à la **JVM Liberty** qui exécute votre EAR. La clé est : JaCoCo doit se trouver dans la même JVM que Liberty, pas dans votre exécuteur Python.

Voici des configurations fiables (choisissez-en une).

---

## 1) Simple et robuste : écriture dans un fichier à la sortie de la JVM

**Quand l'utiliser :** vous pouvez arrêter le serveur Liberty après les tests.

1.  **Rendre l'agent jar disponible** (une fois dans votre build)

```xml
<!-- copie l'agent jacoco dans target/jacoco/jacocoagent.jar -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-dependency-plugin</artifactId>
  <version>3.6.1</version>
  <executions>
    <execution>
      <id>copy-jacoco-agent</id>
      <phase>prepare-package</phase>
      <goals><goal>copy</goal></goals>
      <configuration>
        <artifactItems>
          <artifactItem>
            <groupId>org.jacoco</groupId>
            <artifactId>org.jacoco.agent</artifactId>
            <version>0.8.12</version>
            <classifier>runtime</classifier>
            <destFileName>jacocoagent.jar</destFileName>
          </artifactItem>
        </artifactItems>
        <outputDirectory>${project.build.directory}/jacoco</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

2.  **Ajouter une option JVM Liberty** (fichier : `wlp/usr/servers/<serverName>/jvm.options`)

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=file,append=false,includes=com.myco.*,excludes=org.slf4j.*,destfile=${server.output.dir}/jacoco/jacoco-it.exec
```

*   Placez `jacocoagent.jar` dans `wlp/usr/servers/<serverName>/jacoco/` (ou tout autre chemin lisible).
*   Ajustez `includes`/`excludes` selon vos packages.

3.  **Flux d'exécution**

*   Démarrez Liberty (`server start <serverName>`), déployez l'EAR.
*   Exécutez vos `unittest` Python (ils accèdent aux endpoints).
*   Arrêtez Liberty (`server stop <serverName>`).
  → L'agent écrit `${server.output.dir}/jacoco/jacoco-it.exec`.

4.  **Générer le rapport**

*   Si votre projet est multi-module (EAR + EJB + WAR), utilisez un pom agrégateur et `report-aggregate` :

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-aggregate</goal></goals>
      <configuration>
        <dataFile>${env.SERVER_OUTPUT_DIR}/jacoco/jacoco-it.exec</dataFile>
        <includes>
          <include>com/myco/**</include>
        </includes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

(Ou utilisez `jacococli` :)

```bash
java -jar jacococli.jar report /path/to/jacoco-it.exec \
  --classfiles module1/target/classes --classfiles module2/target/classes \
  --sourcefiles module1/src/main/java --sourcefiles module2/src/main/java \
  --html target/jacoco-it-report
```

---

## 2) Extraction en direct sans arrêter Liberty (mode serveur TCP)

**Quand l'utiliser :** vous voulez laisser Liberty en fonctionnement et récupérer la couverture à la demande.

1.  `jvm.options` :

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=tcpserver,address=*,port=6300,append=false,includes=com.myco.*
```

2.  Exécutez Liberty, lancez les tests Python, puis **extrayez** :

```bash
# récupère la couverture via TCP et écrit un .exec localement
java -jar jacococli.jar dump --address 127.0.0.1 --port 6300 --destfile jacoco-it.exec --reset
```

Générez maintenant le rapport comme ci-dessus.
Astuce : `--reset` remet les compteurs à zéro pour prendre plusieurs instantanés pendant une longue exécution.

---

## 3) Conteneurs / CI (style variable d'environnement)

*   Si vous exécutez Liberty dans Docker/K8s, montez l'agent et définissez :

  *   `jvm.options` comme ci-dessus, **ou**
  *   La variable d'environnement `WLP_JAVA_OPTIONS` / `JAVA_TOOL_OPTIONS` contenant le même `-javaagent=...`.
*   Pour les clusters avec plusieurs JVMs Liberty, donnez à chacune un port TCP ou un chemin de fichier distinct, puis **fusionnez** :

```bash
java -jar jacococli.jar merge node1.exec node2.exec --destfile merged.exec
```

---

## Notes et pièges

*   La **structure de l'EAR n'importe pas** pour JaCoCo ; il instrumente le bytecode en mémoire. La génération de rapports a juste besoin des **fichiers de classes originaux** de vos modules (`target/classes`) et de leurs sources pour le joli HTML.
*   Utilisez **JaCoCo récent (0.8.12+)** pour la compatibilité Java 17/21 (Liberty fonctionne souvent sur OpenJ9/HotSpot — les deux conviennent).
*   Surveillez `includes/excludes` pour éviter de compter les librairies tierces.
*   Si le fichier `.exec` est vide, vous avez probablement :

  *   oublié d'attacher l'agent,
  *   filtré vos packages,
  *   ou extrait le dump avant que le trafic n'atteigne le code.

---

Si vous partagez la structure des modules de votre EAR (modules EJB/WAR et racines des packages), je peux fournir une configuration `report-aggregate` exacte et un petit script pour : démarrer Liberty → exécuter les tests Python → récupérer le dump → construire le rapport HTML en une seule fois.