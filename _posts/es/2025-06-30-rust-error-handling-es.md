---
audio: false
generated: true
lang: es
layout: post
title: Manejo de Errores en Rust Sin Excepciones
translated: true
type: note
---

Rust **no** tiene excepciones en el sentido tradicional, como Java o C\#. En su lugar, maneja los errores principalmente a través de **valores de retorno**, similar al patrón `if err != nil` de Go, pero con un enfoque más robusto y seguro en cuanto a tipos.

Aquí tienes un desglose de cómo Rust maneja los errores:

**1. El Enum `Result<T, E>` para Errores Recuperables:**

Esta es la forma más común e idiomática de manejar errores en Rust.

  * `Result<T, E>` es un enum con dos variantes:
      * `Ok(T)`: Representa éxito y contiene el valor exitoso de tipo `T`.
      * `Err(E)`: Representa fallo y contiene un valor de error de tipo `E`.
  * Cuando una función puede fallar, retorna un `Result`. Esto obliga a quien llama a tratar explícitamente tanto el caso de éxito (`Ok`) como el de fallo (`Err`).
  * Se usan expresiones `match` o varios métodos auxiliares (como `map`, `and_then`, `unwrap_or`, `unwrap_or_else`, etc.) para manejar las variantes `Ok` y `Err`.

**Ejemplo:**

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problema creando el archivo: {:?}", e),
            },
            other_error => panic!("Problema abriendo el archivo: {:?}", other_error),
        },
    };

    println!("Archivo abierto o creado exitosamente: {:?}", greeting_file);
}
```

**2. El Enum `Option<T>` para Valores Opcionales:**

Aunque no es estrictamente para "errores", `Option<T>` es similar a `Result` en que representa la *posibilidad de ausencia*.

  * `Option<T>` tiene dos variantes:
      * `Some(T)`: El valor está presente.
      * `None`: El valor está ausente.
  * Se usa cuando una función puede legítimamente no retornar un valor (ej., buscar un elemento en una lista que podría no existir).

**3. El Operador `?` (Operador de Signo de Interrogación):**

Es un poderoso azúcar sintáctico que hace que propagar errores sea mucho más conciso, similar a cómo `if err != nil { return err }` es común en Go.

  * Si un valor `Result` es `Ok`, el operador `?` extrae el valor `Ok` y la ejecución continúa.
  * Si un valor `Result` es `Err`, el operador `?` retorna inmediatamente el valor `Err` de la función actual.
  * La función que usa `?` debe ella misma retornar un `Result` (o un `Option` si está extrayendo un `Option`).

**Ejemplo con `?`:**

```rust
use std::fs::File;
use std::io::{self, Read}; // Importar el trait io::Read

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?; // Propaga el error si el archivo no existe
    let mut username = String::new();
    username_file.read_to_string(&mut username)?; // Propaga el error si falla la lectura
    Ok(username)
}

fn main() {
    match read_username_from_file() {
        Ok(username) => println!("Nombre de usuario: {}", username),
        Err(e) => println!("Error leyendo el nombre de usuario: {}", e),
    }
}
```

**4. La Macro `panic!` para Errores Irrecuperables:**

`panic!` se usa para errores irrecuperables, que típicamente indican un bug en el programa (ej., acceder a un array fuera de sus límites).

  * Cuando se llama a `panic!`, el programa terminará (o "desenrollará" la pila, dependiendo de la configuración).
  * Generalmente se desaconseja su uso para errores recuperables que tu programa debería manejar de forma controlada.

**Diferencias Clave con las Excepciones Tradicionales:**

  * **Explicitud:** El manejo de errores de Rust es muy explícito. La firma de la función indica claramente que puede retornar un error, y el compilador te *obliga* a manejarlo. No puedes ignorar un error por accidente.
  * **Sin Bloques "Catch-all":** No hay bloques `try-catch` que capturen silenciosamente cualquier excepción. Se tratan tipos de error específicos.
  * **Seguridad de Tipos:** Los errores son valores de tipos específicos (`Result<T, E>`), permitiendo un manejo de errores preciso y evitando la ambigüedad de los tipos de excepción genéricos.
  * **Rendimiento:** Retornar valores `Result` es generalmente más eficiente en rendimiento que lanzar y capturar excepciones, ya que las excepciones a menudo conllevan una sobrecarga significativa (desenrollado de pila, etc.). Rust está diseñado para aplicaciones críticas en cuanto a rendimiento.

En resumen, el modelo de manejo de errores de Rust está mucho más cerca de la filosofía de Go de "verificar en cada nivel" que a las excepciones de Java o C\#. Sin embargo, con el enum `Result` y el operador `?`, Rust proporciona herramientas poderosas y ergonómicas para hacer este manejo explícito de errores manejable e incluso agradable.