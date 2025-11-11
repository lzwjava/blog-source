---
audio: false
generated: true
lang: de
layout: post
title: Schreiben einer Jenkinsfile
translated: true
type: note
---

Um ein Jenkinsfile zu schreiben, das eine Shared Library, einen String-Parameter, einen try-catch-Block, einen node-Block und eine if-Anweisung enthält, können Sie wie folgt vorgehen. Jenkinsfiles werden in Groovy geschrieben und können eine Pipeline definieren, um Build-, Test- und Bereitstellungsprozesse zu automatisieren. Nachfolgend finden Sie ein vollständiges Beispiel für ein scripted Jenkinsfile, das diese Anforderungen erfüllt.

Zuerst, um eine Shared Library zu verwenden, müssen Sie sie mit der `@Library`-Annotation importieren. Shared Libraries in Jenkins enthalten wiederverwendbaren Code, der von mehreren Pipelines aufgerufen werden kann. Wenn Ihre Shared Library beispielsweise `my-shared-library` heißt, binden Sie sie wie folgt am Anfang des Jenkinsfiles ein:

```groovy
@Library('my-shared-library') _
```

Der Unterstrich (`_`) nach der Annotation ist erforderlich, um die Library korrekt zu importieren.

Als nächstes verwenden Sie den `properties`-Step, um einen String-Parameter zu definieren. Dies ermöglicht es Benutzern, beim Ausführen der Pipeline einen String-Wert zu übergeben. So fügen Sie einen String-Parameter namens `MY_STRING` hinzu:

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Ein String-Parameter')
    ])
])
```

Der `node`-Block gibt an, wo die Pipeline ausgeführt wird, z.B. auf einem beliebigen verfügbaren Agenten. Innerhalb dieses Blocks können Sie Ihre Pipeline-Logik unterbringen:

```groovy
node {
    // Pipeline-Steps kommen hierhin
}
```

Um potenzielle Fehler abzufangen, wickeln Sie Ihre Steps in einen `try-catch`-Block ein. Dies stellt sicher, dass Sie eine Exception abfangen und angemessen behandeln können, falls etwas schiefgeht. Zusätzlich kann eine `if`-Anweisung verwendet werden, um Entscheidungen basierend auf dem Wert des String-Parameters (`params.MY_STRING`) zu treffen.

Hier ist das vollständige Jenkinsfile, das alle diese Elemente kombiniert:

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Ein String-Parameter')
    ])
])

node {
    try {
        // Rufen Sie eine Funktion aus der Shared Library auf (angenommen, sie existiert)
        myLibraryFunction()
        
        // Verwenden Sie eine if-Anweisung basierend auf dem String-Parameter
        if (params.MY_STRING == 'test') {
            echo "Running test"
        } else {
            echo "Not running test"
        }
    } catch (Exception e) {
        echo "An error occurred: ${e.message}"
    }
}
```

### Erklärung der Komponenten

- **`@Library('my-shared-library') _`**: Importiert eine Shared Library namens `my-shared-library`. Ersetzen Sie `my-shared-library` durch den tatsächlichen Namen Ihrer Library. Die Funktion `myLibraryFunction()` wird als in dieser Library definiert angenommen.
- **`properties`**: Definiert einen String-Parameter `MY_STRING` mit einem Standardwert von `'default'` und einer Beschreibung. Sie können in der Pipeline über `params.MY_STRING` auf diesen Parameter zugreifen.
- **`node`**: Führt die Pipeline auf einem beliebigen verfügbaren Agenten aus. Sie können bei Bedarf einen bestimmten Agenten angeben (z.B. `node('linux')`).
- **`try-catch`**: Führt die Steps innerhalb des `try`-Blocks aus und fängt alle Exceptions im `catch`-Block ab, wobei eine Fehlermeldung ausgegeben wird, falls etwas schiefgeht.
- **`if`**: Prüft, ob `MY_STRING` gleich `'test'` ist, und gibt entsprechend eine Nachricht aus. Sie können die Bedingung und Aktionen nach Bedarf anpassen.

### Hinweise
- Dieses Beispiel geht von einer scripted Pipeline aus, die mehr Flexibilität mit der Groovy-Syntax bietet. Wenn Sie stattdessen eine declarative Pipeline benötigen, würde die Struktur leicht abweichen (z.B. Verwendung von `pipeline`- und `script`-Blöcken für Groovy-Code).
- Der Aufruf `myLibraryFunction()` ist ein Platzhalter. Stellen Sie sicher, dass Ihre Shared Library diese Funktion definiert, oder ersetzen Sie sie durch eine tatsächliche Funktion aus Ihrer Library.
- Sie können dieses Jenkinsfile erweitern, indem Sie Stages (z.B. `stage('Build')`) oder komplexere Logik hinzufügen, je nach Ihren Anforderungen.

Dieses Jenkinsfile bietet eine solide Grundlage, die alle von Ihnen gewünschten Elemente enthält: eine Shared Library, einen String-Parameter, einen try-catch-Block, einen node-Block und eine if-Anweisung. Passen Sie die Details (Library-Name, Funktionsaufrufe oder Bedingungen) an Ihren Anwendungsfall an!