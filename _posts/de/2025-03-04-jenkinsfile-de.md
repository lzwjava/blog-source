---
audio: true
generated: true
lang: de
layout: post
title: Jenkinsfile schreiben
translated: true
---

Um eine Jenkinsfile zu schreiben, die eine Shared Library, einen String-Parameter, einen Try-Catch-Block, einen Node-Block und eine If-Anweisung enthält, können Sie den folgenden Ansatz verwenden. Jenkinsfiles werden in Groovy geschrieben und können eine Pipeline definieren, um Build-, Test- und Deployment-Prozesse zu automatisieren. Hier ist ein vollständiges Beispiel für eine scriptbasierte Jenkinsfile, die diese Anforderungen erfüllt.

Zunächst müssen Sie die Shared Library mit der `@Library`-Annotation importieren, um sie zu verwenden. Shared Libraries in Jenkins enthalten wiederverwendbaren Code, der von mehreren Pipelines aufgerufen werden kann. Wenn Ihre Shared Library beispielsweise `my-shared-library` heißt, fügen Sie sie oben in der Jenkinsfile wie folgt ein:

```groovy
@Library('my-shared-library') _
```

Das Unterstrich (`_`) nach der Annotation ist erforderlich, um die Bibliothek korrekt zu importieren.

Als Nächstes definieren Sie einen String-Parameter mit dem `properties`-Schritt. Dies ermöglicht es Benutzern, einen String-Wert an die Pipeline zu übergeben, wenn sie ausgeführt wird. Hier ist, wie Sie einen String-Parameter mit dem Namen `MY_STRING` hinzufügen:

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Ein String-Parameter')
    ])
])
```

Der `node`-Block gibt an, wo die Pipeline ausgeführt wird, z.B. auf einem beliebigen verfügbaren Agenten. In diesem Block können Sie Ihre Pipeline-Logik einschließen:

```groovy
node {
    // Pipeline-Schritte gehen hier hin
}
```

Um mögliche Fehler zu behandeln, umschließen Sie Ihre Schritte in einem `try-catch`-Block. Dies stellt sicher, dass Sie die Ausnahme fangen und sie anmutig behandeln können, wenn etwas schiefgeht. Zusätzlich kann eine `if`-Anweisung verwendet werden, um Entscheidungen basierend auf dem Wert des String-Parameters (`params.MY_STRING`) zu treffen.

Hier ist die vollständige Jenkinsfile, die alle diese Elemente kombiniert:

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Ein String-Parameter')
    ])
])

node {
    try {
        // Rufen Sie eine Funktion aus der Shared Library auf (vorausgesetzt, sie existiert)
        myLibraryFunction()

        // Verwenden Sie eine If-Anweisung basierend auf dem String-Parameter
        if (params.MY_STRING == 'test') {
            echo "Test wird ausgeführt"
        } else {
            echo "Test wird nicht ausgeführt"
        }
    } catch (Exception e) {
        echo "Ein Fehler ist aufgetreten: ${e.message}"
    }
}
```

### Erklärung der Komponenten

- **`@Library('my-shared-library') _`**: Importiert eine Shared Library mit dem Namen `my-shared-library`. Ersetzen Sie `my-shared-library` durch den tatsächlichen Namen Ihrer Bibliothek. Die Funktion `myLibraryFunction()` wird angenommen, in dieser Bibliothek definiert zu sein.
- **`properties`**: Definiert einen String-Parameter `MY_STRING` mit einem Standardwert von `'default'` und einer Beschreibung. Sie können diesen Parameter in der Pipeline mit `params.MY_STRING` verwenden.
- **`node`**: Führt die Pipeline auf einem beliebigen verfügbaren Agenten aus. Sie können einen bestimmten Agenten angeben (z.B. `node('linux')`), wenn dies erforderlich ist.
- **`try-catch`**: Führt die Schritte im `try`-Block aus und fängt alle Ausnahmen im `catch`-Block ab, wobei eine Fehlermeldung gedruckt wird, wenn etwas schiefgeht.
- **`if`**: Überprüft, ob `MY_STRING` gleich `'test'` ist, und druckt eine entsprechende Nachricht. Sie können die Bedingung und die Aktionen nach Bedarf ändern.

### Hinweise

- Dieses Beispiel geht von einer scriptbasierten Pipeline aus, die mehr Flexibilität mit der Groovy-Syntax bietet. Wenn Sie stattdessen eine deklarative Pipeline benötigen, würde sich die Struktur leicht ändern (z.B. Verwendung von `pipeline` und `script`-Blöcken für Groovy-Code).
- Der Aufruf von `myLibraryFunction()` ist ein Platzhalter. Stellen Sie sicher, dass Ihre Shared Library diese Funktion definiert, oder ersetzen Sie sie durch eine tatsächliche Funktion aus Ihrer Bibliothek.
- Sie können diese Jenkinsfile erweitern, indem Sie Stages (z.B. `stage('Build')`) oder komplexere Logik hinzufügen, je nach Ihren Anforderungen.

Diese Jenkinsfile bietet eine solide Grundlage, die alle von Ihnen angeforderten Elemente enthält: eine Shared Library, einen String-Parameter, einen Try-Catch-Block, einen Node-Block und eine If-Anweisung. Passen Sie die Details (Bibliotheksname, Funktionsaufrufe oder Bedingungen) an, um sie an Ihren Anwendungsfall anzupassen!