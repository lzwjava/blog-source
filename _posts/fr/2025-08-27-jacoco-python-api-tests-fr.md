---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide JaCoCo pour les tests d'API Python
translated: true
type: note
---

Bonne question — c'est un problème classique d'intégration entre les **outils de couverture de code Java** (JaCoCo) et les **harnesses de test non-Java** (comme Python `unittest` interrogeant vos endpoints REST).

---

### Pourquoi JaCoCo fonctionne avec JUnit mais pas directement avec les tests Python

* JaCoCo fonctionne en attachant un **agent Java** (`-javaagent:jacocoagent.jar`) à la JVM.
* Lorsque vos tests s'exécutent **dans la même JVM** (JUnit, TestNG, etc.), JaCoCo peut voir quelles classes et méthodes sont chargées/exécutées et générer des rapports de couverture détaillés.
* Si vous utilisez Python `unittest` + `requests` pour interroger vos endpoints d'API, vous exercez le **serveur en cours d'exécution** depuis l'extérieur de la JVM.
  Cela signifie que JaCoCo ne voit pas automatiquement la couverture, sauf si le processus du serveur lui-même a l'agent attaché.

---

### Comment vous pouvez obtenir une couverture précise avec JaCoCo et les tests Python

Vous n'avez pas besoin de passer à JUnit. Vous pouvez toujours utiliser JaCoCo, mais vous devez **attacher l'agent à la JVM où votre gros projet Java (le serveur) s'exécute**, et non au lanceur de tests.

1. **Exécutez votre application Java avec l'agent JaCoCo**
   Ajoutez l'agent au démarrage de votre serveur Java :

   ```bash
   java -javaagent:/chemin/vers/jacocoagent.jar=destfile=jacoco-it.exec,output=file,append=false \
        -jar myserver.jar
   ```

   Cela collectera les données d'exécution (`jacoco-it.exec`) pendant que vos tests Python interrogent les endpoints.

2. **Exécutez vos tests Python normalement**

   ```bash
   python -m unittest discover tests/
   ```

   Puisque le serveur est déjà en cours d'exécution avec l'agent, toutes les classes et méthodes interrogées par les requêtes HTTP seront enregistrées.

3. **Arrêtez le serveur**
   Le fichier `.exec` sera vidé.

4. **Générez un rapport de couverture**
   Utilisez le plugin Maven ou la CLI pour convertir le fichier `.exec` en rapports HTML/XML :

   ```bash
   mvn jacoco:report -Djacoco.dataFile=jacoco-it.exec
   ```

   ou avec la CLI :

   ```bash
   java -jar jacococli.jar report jacoco-it.exec \
        --classfiles target/classes \
        --sourcefiles src/main/java \
        --html report
   ```

---

### Deux modes de test avec JaCoCo

* **Tests unitaires (dans la JVM avec JUnit) :** fonctionne nativement avec le plugin Maven (`prepare-agent` + `report`).
* **Tests d'intégration (clients externes comme Python) :** nécessite de démarrer la JVM avec l'agent, puis de fusionner les données `.exec` dans les rapports.

---

### À propos de votre idée avec log4j

Compter les instructions de journalisation par fichier est extrêmement grossier :

* Toutes les méthodes ne journalisent pas.
* Les journaux ne couvrent pas les conditionnelles ou les branches.
* La couverture n'est pas fiable.

JaCoCo, en revanche, mesure la **couverture des classes, des méthodes, des lignes et des branches** — une granularité bien plus fine.

---

✅ **Réponse :** Oui, vous pouvez absolument utiliser l'approche JaCoCo même si vos tests sont en Python. L'astuce est d'**attacher JaCoCo au processus Java sous test** (votre serveur), et non au lanceur de tests. Ensuite, générez le rapport après coup. De cette façon, vous obtiendrez la même couverture au niveau méthode et branche qu'avec JUnit.

---

Souhaitez-vous que je rédige un **exemple de configuration Maven** qui met en place un profil spécial pour les "tests d'intégration" avec JaCoCo, afin que vous puissiez exécuter votre serveur, l'interroger avec des tests Python, puis générer la couverture en une seule commande ?