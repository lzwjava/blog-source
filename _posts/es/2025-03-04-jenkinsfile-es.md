---
audio: false
generated: true
lang: es
layout: post
title: Escribir un Jenkinsfile
translated: true
type: note
---

Para escribir un Jenkinsfile que incorpore una librería compartida, un parámetro de tipo string, un bloque try-catch, un bloque node y una sentencia if, puedes utilizar el siguiente enfoque. Los Jenkinsfiles se escriben en Groovy y pueden definir un pipeline para automatizar procesos de build, test y deployment. A continuación se muestra un ejemplo completo de un Jenkinsfile scripted que cumple con estos requisitos.

Primero, para usar una librería compartida, necesitas importarla con la anotación `@Library`. Las librerías compartidas en Jenkins contienen código reutilizable que puede ser llamado desde múltiples pipelines. Por ejemplo, si tu librería compartida se llama `my-shared-library`, la incluyes en la parte superior del Jenkinsfile de esta manera:

```groovy
@Library('my-shared-library') _
```

El guión bajo (`_`) después de la anotación es necesario para importar correctamente la librería.

A continuación, para definir un parámetro de tipo string, utiliza el paso `properties`. Esto permite a los usuarios pasar un valor string al pipeline cuando se ejecuta. Así es como se añade un parámetro string llamado `MY_STRING`:

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Un parámetro string')
    ])
])
```

El bloque `node` especifica dónde se ejecuta el pipeline, por ejemplo, en cualquier agente disponible. Dentro de este bloque, puedes incluir la lógica de tu pipeline:

```groovy
node {
    // Los pasos del pipeline van aquí
}
```

Para manejar errores potenciales, envuelve tus pasos en un bloque `try-catch`. Esto asegura que si algo falla, puedes capturar la excepción y manejarla adecuadamente. Adicionalmente, una sentencia `if` puede usarse para tomar decisiones basadas en el valor del parámetro string (`params.MY_STRING`).

Aquí está el Jenkinsfile completo que combina todos estos elementos:

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Un parámetro string')
    ])
])

node {
    try {
        // Llama a una función de la librería compartida (asumiendo que existe)
        myLibraryFunction()
        
        // Usa una sentencia if basada en el parámetro string
        if (params.MY_STRING == 'test') {
            echo "Ejecutando test"
        } else {
            echo "No ejecutando test"
        }
    } catch (Exception e) {
        echo "Ocurrió un error: ${e.message}"
    }
}
```

### Explicación de los Componentes

- **`@Library('my-shared-library') _`**: Importa una librería compartida llamada `my-shared-library`. Reemplaza `my-shared-library` con el nombre real de tu librería. Se asume que la función `myLibraryFunction()` está definida en esta librería.
- **`properties`**: Define un parámetro string `MY_STRING` con un valor por defecto de `'default'` y una descripción. Puedes acceder a este parámetro en el pipeline usando `params.MY_STRING`.
- **`node`**: Ejecuta el pipeline en cualquier agente disponible. Puedes especificar un agente en particular (ej., `node('linux')`) si es necesario.
- **`try-catch`**: Ejecuta los pasos dentro del bloque `try` y captura cualquier excepción en el bloque `catch`, imprimiendo un mensaje de error si algo sale mal.
- **`if`**: Verifica si `MY_STRING` es igual a `'test'` e imprime un mensaje en consecuencia. Puedes modificar la condición y las acciones según sea necesario.

### Notas
- Este ejemplo asume un pipeline scripted, que ofrece más flexibilidad con la sintaxis de Groovy. Si necesitas un pipeline declarativo, la estructura sería ligeramente diferente (ej., usando bloques `pipeline` y `script` para el código Groovy).
- La llamada `myLibraryFunction()` es un marcador de posición. Asegúrate de que tu librería compartida defina esta función, o reemplázala con una función real de tu librería.
- Puedes expandir este Jenkinsfile añadiendo stages (ej., `stage('Build')`) o lógica más compleja dependiendo de tus requisitos.

¡Este Jenkinsfile proporciona una base sólida que incluye todos los elementos que solicitaste: una librería compartida, un parámetro string, un bloque try-catch, un bloque node y una sentencia if. Ajusta los detalles (nombre de la librería, llamadas a funciones o condiciones) para que se adapten a tu caso de uso!