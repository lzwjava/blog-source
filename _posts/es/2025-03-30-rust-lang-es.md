---
audio: false
generated: true
lang: es
layout: post
title: Lenguaje de Programación Rust
translated: true
type: note
---

**I. Introducción a Rust**

* **¿Qué es Rust?**
    * Rust es un lenguaje de programación compilado, de tipado estático y multiparadigma, diseñado para el rendimiento y la seguridad, especialmente en áreas como la programación de sistemas, motores de videojuegos, web assembly y sistemas embebidos.
    * Logra seguridad de memoria sin un recolector de basura a través de un sistema de propiedad, préstamo y tiempos de vida.
    * Rust enfatiza las abstracciones de costo cero, lo que significa que obtienes características de alto nivel sin una sobrecarga significativa en tiempo de ejecución.
* **Características Principales y Principios de Diseño:**
    * **Seguridad de Memoria:** Previene errores comunes como desreferencias de punteros nulos, carreras de datos y desbordamientos de búfer en tiempo de compilación.
    * **Concurrencia sin Carreras de Datos:** El sistema de propiedad facilita la escritura de código concurrente seguro.
    * **Rendimiento:** El control de bajo nivel, las abstracciones de costo cero y la compilación eficiente conducen a un rendimiento excelente, a menudo comparable a C++.
    * **Sistema de Tipos Expresivo:** Potente inferencia de tipos, genéricos, traits (similares a interfaces o type classes) y tipos de datos algebraicos.
    * **Herramientas Excelentes:** Cargo (sistema de compilación y gestor de paquetes), rustfmt (formateador de código), clippy (linter).
    * **Ecosistema en Crecimiento:** Una comunidad vibrante y activa con un número creciente de bibliotecas y frameworks.
* **Casos de Uso:**
    * Sistemas Operativos
    * Motores de Videojuegos
    * Web Assembly (Wasm)
    * Sistemas Embebidos
    * Herramientas de Línea de Comandos
    * Programación de Redes
    * Criptomonedas
    * Computación de Alto Rendimiento

**II. Configuración del Entorno de Rust**

* **Instalación:**
    * La forma recomendada de instalar Rust es usando `rustup`, el instalador oficial de la cadena de herramientas de Rust.
    * Visita [https://rustup.rs/](https://rustup.rs/) y sigue las instrucciones para tu sistema operativo.
    * En sistemas tipo Unix, normalmente ejecutarás un comando como: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
* **Verificación de la Instalación:**
    * Abre tu terminal o símbolo del sistema y ejecuta:
        * `rustc --version`: Muestra la versión del compilador de Rust.
        * `cargo --version`: Muestra la versión de Cargo.
* **Cargo: El Sistema de Compilación y Gestor de Paquetes de Rust:**
    * Cargo es esencial para gestionar proyectos de Rust. Se encarga de:
        * Compilar tu código.
        * Gestionar dependencias (crates).
        * Ejecutar tests.
        * Publicar bibliotecas.
    * **Crear un Nuevo Proyecto:** `cargo new <nombre_del_proyecto>` (crea un proyecto binario). `cargo new --lib <nombre_de_la_biblioteca>` (crea un proyecto de biblioteca).
    * **Estructura del Proyecto:** Un proyecto típico de Cargo tiene:
        * `Cargo.toml`: El archivo manifiesto que contiene metadatos del proyecto y dependencias.
        * `src/main.rs`: El punto de entrada para proyectos binarios.
        * `src/lib.rs`: El punto de entrada para proyectos de biblioteca.
        * `Cargo.lock`: Registra las versiones exactas de las dependencias utilizadas en el proyecto.
    * **Compilar:** `cargo build` (compila el proyecto en modo debug). `cargo build --release` (compila el proyecto con optimizaciones para release).
    * **Ejecutar:** `cargo run` (compila y ejecuta el binario).
    * **Añadir Dependencias:** Añade nombres y versiones de crates a la sección `[dependencies]` de `Cargo.toml`. Cargo las descargará y compilará automáticamente.
    * **Actualizar Dependencias:** `cargo update`.

**III. Sintaxis Básica y Conceptos de Rust**

* **¡Hola, Mundo!**
    ```rust
    fn main() {
        println!("¡Hola, mundo!");
    }
    ```
    * `fn main()`: La función principal donde comienza la ejecución del programa.
    * `println!()`: Un macro (indicado por el `!`) que imprime texto en la consola.
* **Variables y Mutabilidad:**
    * Las variables son inmutables por defecto. Para hacer una variable mutable, usa la palabra clave `mut`.
    * Declaración: `let nombre_variable = valor;` (inferencia de tipo). `let nombre_variable: Tipo = valor;` (anotación de tipo explícita).
    * Variable mutable: `let mut contador = 0; contador = 1;`
    * Constantes: Se declaran con `const`, deben tener una anotación de tipo y su valor debe ser conocido en tiempo de compilación. `const PUNTOS_MAXIMOS: u32 = 100_000;`
    * Sombreado: Puedes declarar una nueva variable con el mismo nombre que una anterior; la nueva variable sombrea a la anterior.
* **Tipos de Datos:**
    * **Tipos Escalares:** Representan un único valor.
        * **Enteros:** `i8`, `i16`, `i32`, `i64`, `i128`, `isize` (con signo, del tamaño del puntero); `u8`, `u16`, `u32`, `u64`, `u128`, `usize` (sin signo, del tamaño del puntero). Los literales enteros pueden tener sufijos (ej., `10u32`).
        * **Números de Punto Flotante:** `f32` (precisión simple), `f64` (precisión doble).
        * **Booleanos:** `bool` (`true`, `false`).
        * **Caracteres:** `char` (valores escalares Unicode, 4 bytes).
        * **Tipo Unitario:** `()` (representa una tupla vacía o la ausencia de un valor).
    * **Tipos Compuestos:** Agrupan múltiples valores.
        * **Tuplas:** Secuencias ordenadas de tamaño fijo de elementos con tipos potencialmente diferentes. `let mi_tupla = (1, "hola", 3.14); let (x, y, z) = mi_tupla; let primero = mi_tupla.0;`
        * **Arrays:** Colecciones de tamaño fijo de elementos del mismo tipo. `let mi_array = [1, 2, 3, 4, 5]; let meses: [&str; 12] = ["...", "..."]; let primero = mi_array[0];`
        * **Slices:** Vistas de tamaño dinámico sobre una secuencia contigua de elementos en un array u otro slice. `let slice = &mi_array[1..3];`
    * **Otros Tipos Importantes:**
        * **Cadenas de Texto (Strings):**
            * `String`: Datos de cadena crecibles, mutables y con propiedad. Se crean usando `String::from("...")` o convirtiendo otros tipos de cadena.
            * `&str`: Slice de cadena, una vista inmutable a datos de cadena. A menudo se denomina "literal de cadena" cuando está incrustado directamente en el código (ej., `"hola"`).
        * **Vectores (`Vec<T>`):** Arrays redimensionables que pueden crecer o reducirse. `let mut mi_vec: Vec<i32> = Vec::new(); mi_vec.push(1); let otro_vec = vec![1, 2, 3];`
        * **Mapas Hash (`HashMap<K, V>`):** Almacenan pares clave-valor donde las claves son únicas y de un tipo hasheable. Requiere `use std::collections::HashMap;`.
* **Operadores:**
    * **Aritméticos:** `+`, `-`, `*`, `/`, `%`.
    * **Comparación:** `==`, `!=`, `>`, `<`, `>=`, `<=`.
    * **Lógicos:** `&&` (Y), `||` (O), `!` (NO).
    * **Bit a Bit:** `&` (Y), `|` (O), `^` (XOR), `!` (NO), `<<` (Desplazamiento a Izquierda), `>>` (Desplazamiento a Derecha).
    * **Asignación:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
* **Flujo de Control:**
    * **`if`, `else if`, `else`:** Ejecución condicional.
        ```rust
        let numero = 7;
        if numero < 5 {
            println!("la condición era verdadera");
        } else if numero == 7 {
            println!("el número es siete");
        } else {
            println!("la condición era falsa");
        }
        ```
    * **`loop`:** Bucle infinito (usa `break` para salir).
        ```rust
        loop {
            println!("¡de nuevo!");
            break;
        }
        ```
    * **`while`:** Bucle que continúa mientras una condición sea verdadera.
        ```rust
        let mut contador = 0;
        while contador < 5 {
            println!("el contador es {}", contador);
            contador += 1;
        }
        ```
    * **`for`:** Iterar sobre colecciones.
        ```rust
        let a = [10, 20, 30, 40, 50];
        for elemento in a.iter() {
            println!("el valor es: {}", elemento);
        }

        for numero in 1..5 { // Itera desde 1 hasta (pero sin incluir) 5
            println!("{}", numero);
        }
        ```
    * **`match`:** Constructo de flujo de control potente que compara un valor contra una serie de patrones.
        ```rust
        let numero = 3;
        match numero {
            1 => println!("uno"),
            2 | 3 => println!("dos o tres"),
            4..=6 => println!("cuatro, cinco, o seis"),
            _ => println!("algo más"), // El patrón comodín
        }
        ```
    * **`if let`:** Una forma más concisa de manejar enums u opciones donde solo te importa una o pocas variantes.
        ```rust
        let algun_valor = Some(5);
        if let Some(x) = algun_valor {
            println!("El valor es: {}", x);
        }
        ```

**IV. Propiedad, Préstamo y Tiempos de Vida**

Este es el núcleo de las garantías de seguridad de memoria de Rust.

* **Propiedad:**
    * Cada valor en Rust tiene una variable que es su *propietaria*.
    * Solo puede haber un propietario de un valor a la vez.
    * Cuando el propietario sale del ámbito, el valor se eliminará (su memoria se desasigna).
* **Préstamo:**
    * En lugar de transferir la propiedad, puedes crear referencias a un valor. Esto se llama *préstamo*.
    * **Préstamo Inmutable (`&`):** Puedes tener múltiples referencias inmutables a un valor al mismo tiempo. Los préstamos inmutables no permiten modificar el valor prestado.
    * **Préstamo Mutable (`&mut`):** Puedes tener como máximo una referencia mutable a un valor a la vez. Los préstamos mutables permiten modificar el valor prestado.
    * **Reglas del Préstamo:**
        1.  En cualquier momento dado, puedes tener *una* referencia mutable *o* cualquier número de referencias inmutables.
        2.  Las referencias siempre deben ser válidas.
* **Tiempos de Vida:**
    * Los tiempos de vida son anotaciones que describen el ámbito para el cual una referencia es válida. El compilador de Rust usa la información de los tiempos de vida para garantizar que las referencias no sobrevivan a los datos a los que apuntan (punteros colgantes).
    * En muchos casos, el compilador puede inferir los tiempos de vida automáticamente (elisión de tiempos de vida).
    * Puede que necesites anotar explícitamente los tiempos de vida en firmas de funciones o definiciones de estructuras cuando los tiempos de vida de las referencias no estén claros.
    * Ejemplo de anotación explícita de tiempo de vida:
        ```rust
        fn mas_larga<'a>(x: &'a str, y: &'a str) -> &'a str {
            if x.len() > y.len() {
                x
            } else {
                y
            }
        }
        ```
        El `'a` indica que el slice de cadena devuelto vivirá al menos tanto como ambos slices de cadena de entrada.

**V. Estructuras, Enumeraciones y Módulos**

* **Estructuras:** Tipos de datos definidos por el usuario que agrupan campos con nombre.
    ```rust
    struct Usuario {
        activo: bool,
        nombre_usuario: String,
        email: String,
        contador_inicios_sesion: u64,
    }

    fn main() {
        let mut usuario1 = Usuario {
            activo: true,
            nombre_usuario: String::from("algunnombre123"),
            email: String::from("alguien@ejemplo.com"),
            contador_inicios_sesion: 1,
        };

        usuario1.email = String::from("otro@ejemplo.com");

        let usuario2 = Usuario {
            email: String::from("otro@ejemplo.com"),
            ..usuario1 // Sintaxis de actualización de estructura, campos restantes de usuario1
        };
    }
    ```
    * Estructuras de tupla: Tuplas con nombre sin campos con nombre. `struct Color(i32, i32, i32);`
    * Estructuras tipo unidad: Estructuras sin campos. `struct SiempreIgual;`
* **Enums (Enumeraciones):** Definen un tipo enumerando sus posibles variantes.
    ```rust
    enum Mensaje {
        Salir,
        Mover { x: i32, y: i32 }, // Estructura anónima
        Escribir(String),
        CambiarColor(i32, i32, i32), // Tipo tupla
    }

    fn main() {
        let q = Mensaje::Salir;
        let m = Mensaje::Mover { x: 10, y: 5 };
        let w = Mensaje::Escribir(String::from("hola"));

        match m {
            Mensaje::Salir => println!("Salir"),
            Mensaje::Mover { x, y } => println!("Mover a x={}, y={}", x, y),
            Mensaje::Escribir(texto) => println!("Escribir: {}", texto),
            Mensaje::CambiarColor(r, g, b) => println!("Cambiar color a r={}, g={}, b={}", r, g, b),
        }
    }
    ```
    * Los enums pueden contener datos directamente dentro de sus variantes.
* **Módulos:** Organizan el código dentro de crates (paquetes).
    * Usa la palabra clave `mod` para definir un módulo.
    * Los módulos pueden contener otros módulos, estructuras, enums, funciones, etc.
    * Controla la visibilidad con `pub` (público) y privado (por defecto).
    * Accede a elementos dentro de módulos usando la ruta del módulo (ej., `mi_modulo::mi_funcion()`).
    * Trae elementos al ámbito actual con la palabra clave `use` (ej., `use std::collections::HashMap;`).
    * Separa módulos en archivos diferentes (convención: un módulo llamado `mi_modulo` va en `src/mi_modulo.rs` o `src/mi_modulo/mod.rs`).

**VI. Traits y Genéricos**

* **Traits:** Similares a interfaces o type classes en otros lenguajes. Definen un conjunto de métodos que un tipo debe implementar para cumplir un cierto contrato.
    ```rust
    pub trait Resumen {
        fn resumir(&self) -> String;
    }

    pub struct ArticuloNoticia {
        pub titular: String,
        pub ubicacion: String,
        pub autor: String,
        pub contenido: String,
    }

    impl Resumen for ArticuloNoticia {
        fn resumir(&self) -> String {
            format!("{}, por {} ({})", self.titular, self.autor, self.ubicacion)
        }
    }

    pub struct Tweet {
        pub nombre_usuario: String,
        pub contenido: String,
        pub respuesta: bool,
        pub retweet: bool,
    }

    impl Resumen for Tweet {
        fn resumir(&self) -> String {
            format!("{}: {}", self.nombre_usuario, self.contenido)
        }
    }

    fn main() {
        let tweet = Tweet {
            nombre_usuario: String::from("horse_ebooks"),
            contenido: String::from("por supuesto, como probablemente ya sabes, gente"),
            respuesta: false,
            retweet: false,
        };

        println!("¡Nuevo tweet disponible! {}", tweet.resumir());
    }
    ```
    * Los traits pueden tener implementaciones por defecto para los métodos.
    * Los traits pueden usarse como restricciones para tipos genéricos.
* **Genéricos:** Escribe código que pueda funcionar con múltiples tipos sin conocer los tipos específicos en tiempo de compilación.
    ```rust
    fn mas_grande<T: PartialOrd + Copy>(lista: &[T]) -> T {
        let mut mas_grande = lista[0];

        for &item in lista.iter() {
            if item > mas_grande {
                mas_grande = item;
            }
        }

        mas_grande
    }

    fn main() {
        let lista_numeros = vec![34, 50, 25, 100, 65];
        let resultado = mas_grande(&lista_numeros);
        println!("El número más grande es {}", resultado);

        let lista_caracteres = vec!['y', 'm', 'a', 'q'];
        let resultado = mas_grande(&lista_caracteres);
        println!("El carácter más grande es {}", resultado);
    }
    ```
    * Los parámetros de tipo se declaran dentro de corchetes angulares `<T>`.
    * Las restricciones de trait (`T: PartialOrd + Copy`) especifican qué funcionalidad debe implementar el tipo genérico.
    * `PartialOrd` permite la comparación usando `>`, y `Copy` significa que el tipo puede ser copiado por valor.

**VII. Manejo de Errores**

Rust enfatiza el manejo explícito de errores.

* **Enum `Result`:** Representa éxito (`Ok`) o fallo (`Err`).
    ```rust
    enum Result<T, E> {
        Ok(T),
        Err(E),
    }
    ```
    * `T` es el tipo del valor de éxito.
    * `E` es el tipo del valor de error.
    * Se usa comúnmente para operaciones que pueden fallar (ej., E/S de archivos, peticiones de red).
    * El operador `?` es azúcar sintáctico para manejar valores `Result`. Si el `Result` es `Ok`, extrae el valor; si es `Err`, devuelve el error temprano desde la función actual.
* **Macro `panic!`:** Hace que el programa falle inmediatamente. Generalmente se usa para errores irrecuperables.
    ```rust
    fn main() {
        let v = vec![1, 2, 3];
        // v[99]; // Esto causará un panic en tiempo de ejecución
        panic!("¡Choca y quema!");
    }
    ```
* **Enum `Option`:** Representa un valor que puede o no estar presente.
    ```rust
    enum Option<T> {
        Some(T),
        None,
    }
    ```
    * Se usa para evitar punteros nulos.
    * Se usan métodos como `unwrap()`, `unwrap_or()`, `map()`, y `and_then()` para trabajar con valores `Option`.
    ```rust
    fn dividir(a: i32, b: i32) -> Option<i32> {
        if b == 0 {
            None
        } else {
            Some(a / b)
        }
    }

    fn main() {
        let resultado1 = dividir(10, 2);
        match resultado1 {
            Some(valor) => println!("Resultado: {}", valor),
            None => println!("No se puede dividir por cero"),
        }

        let resultado2 = dividir(5, 0);
        println!("Resultado 2: {:?}", resultado2.unwrap_or(-1)); // Devuelve -1 si es None
    }
    ```

**VIII. Cierres e Iteradores**

* **Cierres:** Funciones anónimas que pueden capturar variables de su ámbito circundante.
    ```rust
    fn main() {
        let x = 4;
        let igual_a_x = |z| z == x; // Cierre que captura x

        println!("¿Es 5 igual a x? {}", igual_a_x(5));
    }
    ```
    * Sintaxis de cierre: `|parametros| -> tipo_retorno { cuerpo }` (el tipo de retorno a menudo se puede inferir).
    * Los cierres pueden capturar variables por referencia (`&`), por referencia mutable (`&mut`) o por valor (moviendo la propiedad). Rust infiere el tipo de captura. Usa la palabra clave `move` para forzar la transferencia de propiedad.
* **Iteradores:** Proporcionan una forma de procesar una secuencia de elementos.
    * Se crean llamando al método `iter()` en colecciones como vectores, arrays y mapas hash (para iteración inmutable), `iter_mut()` para iteración mutable, y `into_iter()` para consumir la colección y tomar propiedad de sus elementos.
    * Los iteradores son perezosos; solo producen valores cuando se consumen explícitamente.
    * Adaptadores de iteradores comunes (métodos que transforman iteradores): `map()`, `filter()`, `take()`, `skip()`, `zip()`, `enumerate()`, etc.
    * Consumidores de iteradores comunes (métodos que producen un valor final): `collect()`, `sum()`, `product()`, `fold()`, `any()`, `all()`, etc.
    ```rust
    fn main() {
        let v1 = vec![1, 2, 3];

        let v1_iter = v1.iter(); // Crea un iterador sobre v1

        for val in v1_iter {
            println!("Se obtuvo: {}", val);
        }

        let v2: Vec<_> = v1.iter().map(|x| x + 1).collect(); // Transformar y recolectar
        println!("v2: {:?}", v2);

        let suma: i32 = v1.iter().sum(); // Consume el iterador para obtener una suma
        println!("Suma de v1: {}", suma);
    }
    ```

**IX. Punteros Inteligentes**

Los punteros inteligentes son estructuras de datos que actúan como punteros pero también tienen metadatos y capacidades adicionales. Hacen cumplir diferentes conjuntos de reglas que las referencias normales.

* **`Box<T>`:** El puntero inteligente más simple. Asigna memoria en el montón y proporciona propiedad del valor. Cuando el `Box` sale del ámbito, el valor en el montón se elimina. Útil para:
    * Datos cuyo tamaño no se conoce en tiempo de compilación.
    * Transferir propiedad de grandes cantidades de datos.
    * Crear estructuras de datos recursivas.
* **`Rc<T>` (Recuento de Referencias):** Permite que múltiples partes del programa tengan acceso de solo lectura a los mismos datos. Los datos solo se limpian cuando el último puntero `Rc` sale del ámbito. No es seguro para hilos.
* **`Arc<T>` (Recuento de Referencias Atómico):** Similar a `Rc<T>` pero seguro para hilos para usar en escenarios concurrentes. Tiene cierta sobrecarga de rendimiento en comparación con `Rc<T>`.
* **`Cell<T>` y `RefCell<T>` (Mutabilidad Interior):** Permiten modificar datos incluso cuando hay referencias inmutables a ellos. Esto viola las reglas habituales de préstamo de Rust y se usa en situaciones específicas y controladas.
    * `Cell<T>`: Para tipos que son `Copy`. Permite establecer y obtener el valor.
    * `RefCell<T>`: Para tipos que no son `Copy`. Proporciona comprobaciones de préstamo en tiempo de ejecución (entra en pánico si se violan las reglas de préstamo en tiempo de ejecución).
* **`Mutex<T>` y `RwLock<T>` (Primitivas de Concurrencia):** Proporcionan mecanismos para un acceso compartido mutable seguro entre hilos.
    * `Mutex<T>`: Permite que solo un hilo mantenga el bloqueo y acceda a los datos a la vez.
    * `RwLock<T>`: Permite múltiples lectores o un único escritor acceder a los datos.

**X. Concurrencia**

Rust tiene un excelente soporte incorporado para la concurrencia.

* **Hilos:** Genera nuevos hilos del SO usando `std::thread::spawn`.
    ```rust
    use std::thread;
    use std::time::Duration;

    fn main() {
        let manejador = thread::spawn(|| {
            for i in 1..10 {
                println!("¡hola número {} desde el hilo generado!", i);
                thread::sleep(Duration::from_millis(1));
            }
        });

        for i in 1..5 {
            println!("¡hola número {} desde el hilo principal!", i);
            thread::sleep(Duration::from_millis(1));
        }

        manejador.join().unwrap(); // Espera a que el hilo generado termine
    }
    ```
* **Paso de Mensajes:** Usa canales (proporcionados por `std::sync::mpsc`) para enviar datos entre hilos.
    ```rust
    use std::sync::mpsc;
    use std::thread;
    use std::time::Duration;

    fn main() {
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let valor = String::from("hola");
            tx.send(valor).unwrap();
            // println!("valor es {}", valor); // Error: valor ha sido movido
        });

        let recibido = rx.recv().unwrap();
        println!("Recibido: {}", recibido);
    }
    ```
* **Concurrencia de Estado Compartido:** Usa punteros inteligentes como `Mutex<T>` y `Arc<T>` para un acceso mutable compartido seguro entre múltiples hilos.

**XI. Macros**

Las macros son una forma de metaprogramación en Rust. Te permiten escribir código que escribe otro código.

* **Macros Declarativas (`macro_rules!`):** Coinciden con patrones y los reemplazan con otro código. Potentes para reducir código repetitivo.
    ```rust
    macro_rules! vec {
        ( $( $x:expr ),* ) => {
            {
                let mut temp_vec = Vec::new();
                $(
                    temp_vec.push($x);
                )*
                temp_vec
            }
        };
    }

    fn main() {
        let mi_vec = vec![1, 2, 3, 4];
        println!("{:?}", mi_vec);
    }
    ```
* **Macros Procedimentales:** Más potentes y complejas que las macros declarativas. Operan en el árbol de sintaxis abstracta (AST) del código de Rust. Hay tres tipos:
    * **Macros similares a funciones:** Parecen llamadas a funciones.
    * **Macros similares a atributos:** Se usan con la sintaxis `#[...]`.
    * **Macros derive:** Se usan con `#[derive(...)]` para implementar traits automáticamente.

**XII. Testing**

Rust tiene soporte incorporado para escribir y ejecutar tests.

* **Tests Unitarios:** Prueban unidades individuales de código (funciones, módulos). Normalmente se colocan en el mismo archivo que el código que prueban, dentro de un módulo `#[cfg(test)]`.
    ```rust
    pub fn sumar(izquierda: usize, derecha: usize) -> usize {
        izquierda + derecha
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn funciona() {
            let resultado = sumar(2, 2);
            assert_eq!(resultado, 4);
        }
    }
    ```
* **Tests de Integración:** Prueban cómo funcionan juntas diferentes partes de tu biblioteca o binario. Se colocan en un directorio `tests` separado en el nivel superior de tu proyecto.
* **Ejecutar Tests:** Usa el comando `cargo test`.

**XIII. Rust Inseguro**

Las garantías de seguridad de Rust las aplica el compilador. Sin embargo, hay situaciones en las que podrías necesitar evitar estas garantías. Esto se hace usando la palabra clave `unsafe`.

* **Bloque `unsafe`:** El código dentro de un bloque `unsafe` puede realizar operaciones que el compilador no puede garantizar que sean seguras, como:
    * Desreferenciar punteros en bruto (`*const T`, `*mut T`).
    * Llamar a funciones o métodos `unsafe`.
    * Acceder a campos de `union`s.
    * Enlazar a código externo (no Rust).
* **Funciones `unsafe`:** Las funciones que contienen operaciones `unsafe` se marcan ellas mismas como `unsafe`. Llamar a una función `unsafe` requiere un bloque `unsafe`.
* **Razones para Usar `unsafe`:** Interfaz con bibliotecas C, programación de sistemas de bajo nivel, código crítico para el rendimiento donde los invariantes de seguridad se mantienen manualmente.
* **Nota Importante:** `unsafe` debe usarse con moderación y con extrema precaución. Es tu responsabilidad garantizar la seguridad de la memoria dentro de los bloques `unsafe`.

**XIV. El Ecosistema de Rust**

* **Crates (Paquetes):** Bibliotecas o ejecutables que se pueden usar en proyectos de Rust. Se encuentran en [https://crates.io/](https://crates.io/).
* **Crates Populares:**
    * `serde`: Serialización y deserialización.
    * `tokio`, `async-std`: Programación asíncrona.
    * `actix-web`, `rocket`: Frameworks web.
    * `diesel`, `sea-orm`: Mapeadores objeto-relacional (ORMs).
    * `clap`, `structopt`: Análisis de argumentos de línea de comandos.
    * `log`, `env_logger`: Registro de logs.
    * `rand`: Generación de números aleatorios.
* **Biblioteca Estándar de Rust (`std`):** Proporciona funcionalidades esenciales.

**XV. Recursos de Aprendizaje**

* **El Libro de Rust:** La guía oficial y completa ([https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/)).
* **Rust by Example:** Una colección de ejemplos ejecutables que ilustran varias características de Rust ([https://doc.rust-lang.org/rust-by-example/](https://doc.rust-lang.org/rust-by-example/)).
* **El Curso Rustlings:** Un conjunto de pequeños ejercicios para acostumbrarte a leer y escribir código Rust ([https://github.com/rust-lang/rustlings](https://github.com/rust-lang/rustlings)).
* **Documentación de Rust:** La documentación oficial de la API ([https://doc.rust-lang.org/std/](https://doc.rust-lang.org/std/)).
* **El Blog de Rust:** Anuncios y actualizaciones oficiales ([https://blog.rust-lang.org/](https://blog.rust-lang.org/)).
* **Reddit (r/rust), Discord, y otras plataformas comunitarias.**

Esta guía proporciona una base sólida para aprender Rust. La mejor manera de volverse competente es practicar escribiendo código Rust, explorar el ecosistema y participar en la comunidad. ¡Buena suerte en tu viaje con Rust