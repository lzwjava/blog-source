---
audio: false
generated: true
lang: fr
layout: post
title: La Gestion des Erreurs en Rust Sans Exceptions
translated: true
type: note
---

Rust n'a **pas** d'exceptions au sens traditionnel, comme Java ou C\#. Au lieu de cela, il gère les erreurs principalement via des **valeurs de retour**, similaire au modèle `if err != nil` de Go, mais avec une approche plus robuste et type-safe.

Voici une explication de la manière dont Rust gère les erreurs :

**1. L'énumération `Result<T, E>` pour les erreurs récupérables :**

C'est la manière la plus courante et idiomatique de gérer les erreurs en Rust.

  * `Result<T, E>` est une énumération avec deux variantes :
      * `Ok(T)` : Représente le succès et contient la valeur de succès de type `T`.
      * `Err(E)` : Représente l'échec et contient une valeur d'erreur de type `E`.
  * Lorsqu'une fonction peut échouer, elle retourne un `Result`. Cela force l'appelant à traiter explicitement à la fois les cas de succès (`Ok`) et d'échec (`Err`).
  * Vous utilisez des expressions `match` ou diverses méthodes utilitaires (comme `map`, `and_then`, `unwrap_or`, `unwrap_or_else`, etc.) pour gérer les variantes `Ok` et `Err`.

**Exemple :**

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
                Err(e) => panic!("Problème lors de la création du fichier : {:?}", e),
            },
            other_error => panic!("Problème lors de l'ouverture du fichier : {:?}", other_error),
        },
    };

    println!("Fichier ouvert ou créé avec succès : {:?}", greeting_file);
}
```

**2. L'énumération `Option<T>` pour les valeurs optionnelles :**

Bien que n'étant pas strictement destinée aux "erreurs", `Option<T>` est similaire à `Result` en ce sens qu'elle représente la *possibilité d'une absence*.

  * `Option<T>` a deux variantes :
      * `Some(T)` : La valeur est présente.
      * `None` : La valeur est absente.
  * Ceci est utilisé lorsqu'une fonction peut légitimement ne pas retourner de valeur (par exemple, trouver un élément dans une liste qui pourrait ne pas exister).

**3. L'opérateur `?` (Opérateur point d'interrogation) :**

C'est un sucre syntaxique puissant qui rend la propagation des erreurs beaucoup plus concise, similaire à la manière dont `if err != nil { return err }` est courant en Go.

  * Si une valeur `Result` est `Ok`, l'opérateur `?` déballer la valeur `Ok` et l'exécution continue.
  * Si une valeur `Result` est `Err`, l'opérateur `?` retourne immédiatement la valeur `Err` depuis la fonction courante.
  * La fonction utilisant `?` doit elle-même retourner un `Result` (ou un `Option` si elle déballer un `Option`).

**Exemple avec `?` :**

```rust
use std::fs::File;
use std::io::{self, Read}; // Importe le trait io::Read

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?; // Propage l'erreur si le fichier n'existe pas
    let mut username = String::new();
    username_file.read_to_string(&mut username)?; // Propage l'erreur si la lecture échoue
    Ok(username)
}

fn main() {
    match read_username_from_file() {
        Ok(username) => println!("Nom d'utilisateur : {}", username),
        Err(e) => println!("Erreur lors de la lecture du nom d'utilisateur : {}", e),
    }
}
```

**4. La macro `panic!` pour les erreurs irrécupérables :**

`panic!` est utilisée pour les erreurs irrécupérables, qui indiquent typiquement un bogue dans le programme (par exemple, accéder à un tableau en dehors de ses limites).

  * Lorsque `panic!` est appelée, le programme se terminera (ou "déroulera" la pile, selon la configuration).
  * Son utilisation est généralement déconseillée pour les erreurs récupérables que votre programme devrait gérer gracieusement.

**Différences clés par rapport aux exceptions traditionnelles :**

  * **Explicité :** La gestion des erreurs en Rust est très explicite. La signature de la fonction indique clairement qu'elle peut retourner une erreur, et le compilateur vous *force* à la gérer. Vous ne pouvez pas ignorer accidentellement une erreur.
  * **Pas de blocs "attrape-tout" :** Il n'y a pas de blocs `try-catch` qui attrapent silencieusement n'importe quelle exception. Vous traitez des types d'erreur spécifiques.
  * **Type Safety :** Les erreurs sont des valeurs de types spécifiques (`Result<T, E>`), permettant une gestion d'erreur précise et évitant l'ambiguïté des types d'exception génériques.
  * **Performance :** Retourner des valeurs `Result` est généralement plus performant que de lever et attraper des exceptions, car les exceptions impliquent souvent une surcharge significative (déroulement de pile, etc.). Rust est conçu pour des applications critiques en termes de performance.

En résumé, le modèle de gestion d'erreur de Rust est beaucoup plus proche de la philosophie "vérifier à chaque niveau" de Go que des exceptions de Java ou C\#. Cependant, avec l'énumération `Result` et l'opérateur `?`, Rust fournit des outils puissants et ergonomiques pour rendre cette gestion d'erreur explicite gérable et même agréable.