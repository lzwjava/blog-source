---
audio: false
generated: true
lang: es
layout: post
title: Escribir un Jenkinsfile
translated: true
---

Para escribir un Jenkinsfile que incorpore una biblioteca compartida, un parámetro de cadena, un bloque try-catch, un bloque node y una instrucción if, puedes usar el siguiente enfoque. Los Jenkinsfiles se escriben en Groovy y pueden definir una canalización para automatizar procesos de construcción, prueba y despliegue. A continuación se muestra un ejemplo completo de un Jenkinsfile de script que cumple con estos requisitos.

Primero, para usar una biblioteca compartida, debes importarla con la anotación `@Library`. Las bibliotecas compartidas en Jenkins contienen código reutilizable que se puede llamar desde múltiples canalizaciones. Por ejemplo, si tu biblioteca compartida se llama `my-shared-library`, la incluyes al principio del Jenkinsfile de la siguiente manera:

```groovy
@Library('my-shared-library') _
```

El guion bajo (`_`) después de la anotación es necesario para importar correctamente la biblioteca.

A continuación, para definir un parámetro de cadena, usa el paso `properties`. Esto permite a los usuarios pasar un valor de cadena a la canalización cuando se ejecuta. Aquí tienes cómo agregar un parámetro de cadena llamado `MY_STRING`:

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Un parámetro de cadena')
    ])
])
```

El bloque `node` especifica dónde se ejecuta la canalización, como en cualquier agente disponible. Dentro de este bloque, puedes incluir la lógica de tu canalización:

```groovy
node {
    // Los pasos de la canalización van aquí
}
```

Para manejar posibles errores, envuelve tus pasos en un bloque `try-catch`. Esto asegura que, si algo falla, puedas capturar la excepción y manejarla con gracia. Además, una instrucción `if` se puede usar para tomar decisiones basadas en el valor del parámetro de cadena (`params.MY_STRING`).

Aquí tienes el Jenkinsfile completo que combina todos estos elementos:

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'Un parámetro de cadena')
    ])
])

node {
    try {
        // Llama a una función de la biblioteca compartida (suponiendo que exista)
        myLibraryFunction()

        // Usa una instrucción if basada en el parámetro de cadena
        if (params.MY_STRING == 'test') {
            echo "Ejecutando prueba"
        } else {
            echo "No ejecutando prueba"
        }
    } catch (Exception e) {
        echo "Ocurrió un error: ${e.message}"
    }
}
```

### Explicación de los Componentes

- **`@Library('my-shared-library') _`**: Importa una biblioteca compartida llamada `my-shared-library`. Reemplaza `my-shared-library` con el nombre real de tu biblioteca. La función `myLibraryFunction()` se asume que está definida en esta biblioteca.
- **`properties`**: Define un parámetro de cadena `MY_STRING` con un valor predeterminado de `'default'` y una descripción. Puedes acceder a este parámetro en la canalización usando `params.MY_STRING`.
- **`node`**: Ejecuta la canalización en cualquier agente disponible. Puedes especificar un agente particular (por ejemplo, `node('linux')`) si es necesario.
- **`try-catch`**: Ejecuta los pasos dentro del bloque `try` y captura cualquier excepción en el bloque `catch`, imprimiendo un mensaje de error si algo sale mal.
- **`if`**: Verifica si `MY_STRING` es igual a `'test'` e imprime un mensaje en consecuencia. Puedes modificar la condición y las acciones según sea necesario.

### Notas

- Este ejemplo asume una canalización de script, que ofrece más flexibilidad con la sintaxis de Groovy. Si necesitas una canalización declarativa en su lugar, la estructura sería ligeramente diferente (por ejemplo, usando bloques `pipeline` y `script` para el código de Groovy).
- La llamada a `myLibraryFunction()` es un marcador de posición. Asegúrate de que tu biblioteca compartida defina esta función, o reemplázala con una función real de tu biblioteca.
- Puedes expandir este Jenkinsfile agregando etapas (por ejemplo, `stage('Build')`) o lógica más compleja según tus necesidades.

Este Jenkinsfile proporciona una base sólida que incluye todos los elementos que solicitaste: una biblioteca compartida, un parámetro de cadena, un bloque try-catch, un bloque node y una instrucción if. Ajusta los detalles (nombre de la biblioteca, llamadas a funciones o condiciones) para que se adapten a tu caso de uso.