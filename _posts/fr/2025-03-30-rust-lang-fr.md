---
audio: false
generated: true
lang: fr
layout: post
title: Langage de Programmation Rust
translated: true
type: note
---

**I. Introduction à Rust**

* **Qu'est-ce que Rust ?**
    * Rust est un langage de programmation compilé, multi-paradigme et statiquement typé conçu pour la performance et la sécurité, en particulier dans des domaines comme la programmation système, les moteurs de jeu, le Web Assembly et les systèmes embarqués.
    * Il garantit la sécurité mémoire sans garbage collector grâce à un système de propriété, d'emprunt et de durées de vie.
    * Rust met l'accent sur les abstractions à coût nul, ce qui signifie que vous bénéficiez de fonctionnalités de haut niveau sans surcharge d'exécution significative.
* **Caractéristiques et principes de conception clés :**
    * **Sécurité mémoire :** Empêche les bogues courants comme les déréférencements de pointeurs nuls, les courses aux données et les dépassements de mémoire tampon au moment de la compilation.
    * **Concurrence sans courses aux données :** Le système de propriété facilite l'écriture de code concurrent sûr.
    * **Performance :** Le contrôle de bas niveau, les abstractions à coût nul et une compilation efficace conduisent à d'excellentes performances, souvent comparables à C++.
    * **Système de types expressif :** Inférence de types puissante, génériques, traits (similaires aux interfaces ou aux classes de types) et types algébriques.
    * **Outillage excellent :** Cargo (système de build et gestionnaire de paquets), rustfmt (formateur de code), clippy (linter).
    * **Écosystème croissant :** Une communauté dynamique et active avec un nombre croissant de bibliothèques et de frameworks.
* **Cas d'utilisation :**
    * Systèmes d'exploitation
    * Moteurs de jeu
    * Web Assembly (Wasm)
    * Systèmes embarqués
    * Outils en ligne de commande
    * Programmation réseau
    * Cryptomonnaies
    * Calcul haute performance

**II. Configuration de l'environnement Rust**

* **Installation :**
    * La méthode recommandée pour installer Rust est d'utiliser `rustup`, l'installateur officiel de la chaîne d'outils Rust.
    * Visitez [https://rustup.rs/](https://rustup.rs/) et suivez les instructions pour votre système d'exploitation.
    * Sur les systèmes de type Unix, vous exécuterez généralement une commande comme : `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
* **Vérification de l'installation :**
    * Ouvrez votre terminal ou invite de commande et exécutez :
        * `rustc --version` : Affiche la version du compilateur Rust.
        * `cargo --version` : Affiche la version de Cargo.
* **Cargo : Le système de build et le gestionnaire de paquets Rust :**
    * Cargo est essentiel pour gérer les projets Rust. Il gère :
        * La construction de votre code.
        * La gestion des dépendances (crates).
        * L'exécution des tests.
        * La publication des bibliothèques.
    * **Création d'un nouveau projet :** `cargo new <nom_du_projet>` (crée un projet binaire). `cargo new --lib <nom_de_la_bibliothèque>` (crée un projet de bibliothèque).
    * **Structure du projet :** Un projet Cargo typique a :
        * `Cargo.toml` : Le fichier manifeste contenant les métadonnées du projet et les dépendances.
        * `src/main.rs` : Le point d'entrée pour les projets binaires.
        * `src/lib.rs` : Le point d'entrée pour les projets de bibliothèque.
        * `Cargo.lock` : Enregistre les versions exactes des dépendances utilisées dans le projet.
    * **Construction :** `cargo build` (construit le projet en mode debug). `cargo build --release` (construit le projet avec les optimisations pour la version release).
    * **Exécution :** `cargo run` (construit et exécute le binaire).
    * **Ajout de dépendances :** Ajoutez les noms et versions des crates dans la section `[dependencies]` de `Cargo.toml`. Cargo les téléchargera et les construira automatiquement.
    * **Mise à jour des dépendances :** `cargo update`.

**III. Syntaxe et concepts de base de Rust**

* **Hello, World !**
    ```rust
    fn main() {
        println!("Hello, world!");
    }
    ```
    * `fn main()` : La fonction principale où l'exécution du programme commence.
    * `println!()` : Une macro (indiquée par le `!`) qui imprime du texte dans la console.
* **Variables et mutabilité :**
    * Les variables sont immuables par défaut. Pour rendre une variable mutable, utilisez le mot-clé `mut`.
    * Déclaration : `let nom_variable = valeur;` (inférence de type). `let nom_variable: Type = valeur;` (annotation de type explicite).
    * Variable mutable : `let mut compteur = 0; compteur = 1;`
    * Constantes : Déclarées avec `const`, doivent avoir une annotation de type, et leur valeur doit être connue à la compilation. `const MAX_POINTS: u32 = 100_000;`
    * Ombrage : Vous pouvez déclarer une nouvelle variable avec le même nom qu'une précédente ; la nouvelle variable masque l'ancienne.
* **Types de données :**
    * **Types scalaires :** Représentent une valeur unique.
        * **Entiers :** `i8`, `i16`, `i32`, `i64`, `i128`, `isize` (signé de la taille d'un pointeur) ; `u8`, `u16`, `u32`, `u64`, `u128`, `usize` (non signé de la taille d'un pointeur). Les littéraux entiers peuvent avoir des suffixes (ex. : `10u32`).
        * **Nombres à virgule flottante :** `f32` (simple précision), `f64` (double précision).
        * **Booléens :** `bool` (`true`, `false`).
        * **Caractères :** `char` (valeurs scalaires Unicode, 4 octets).
        * **Type unité :** `()` (représente un tuple vide ou l'absence de valeur).
    * **Types composés :** Regroupent plusieurs valeurs.
        * **Tuples :** Séquences ordonnées de taille fixe d'éléments avec potentiellement des types différents. `let mon_tuple = (1, "hello", 3.14); let (x, y, z) = mon_tuple; let premier = mon_tuple.0;`
        * **Tableaux :** Collections de taille fixe d'éléments du même type. `let mon_tableau = [1, 2, 3, 4, 5]; let mois: [&str; 12] = ["...", "..."]; let premier = mon_tableau[0];`
        * **Tranches :** Vues de taille dynamique sur une séquence contiguë d'éléments dans un tableau ou une autre tranche. `let tranche = &mon_tableau[1..3];`
    * **Autres types importants :**
        * **Chaînes de caractères :**
            * `String` : Données de chaîne possédées, mutables et pouvant grandir. Créées en utilisant `String::from("...")` ou en convertissant d'autres types de chaînes.
            * `&str` : Tranche de chaîne, vue immuable sur des données de chaîne. Souvent appelée "littéral de chaîne" lorsqu'elle est directement intégrée dans le code (ex. : `"hello"`).
        * **Vecteurs (`Vec<T>`) :** Tableaux redimensionnables qui peuvent grandir ou rétrécir. `let mut mon_vec: Vec<i32> = Vec::new(); mon_vec.push(1); let autre_vec = vec![1, 2, 3];`
        * **Tables de hachage (`HashMap<K, V>`) :** Stockent des paires clé-valeur où les clés sont uniques et d'un type hachable. Nécessite `use std::collections::HashMap;`.
* **Opérateurs :**
    * **Arithmétiques :** `+`, `-`, `*`, `/`, `%`.
    * **Comparaison :** `==`, `!=`, `>`, `<`, `>=`, `<=`.
    * **Logiques :** `&&` (ET), `||` (OU), `!` (NON).
    * **Binaires :** `&` (ET), `|` (OU), `^` (OU exclusif), `!` (NON), `<<` (Décalage à gauche), `>>` (Décalage à droite).
    * **Affectation :** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
* **Flux de contrôle :**
    * **`if`, `else if`, `else` :** Exécution conditionnelle.
        ```rust
        let nombre = 7;
        if nombre < 5 {
            println!("la condition était vraie");
        } else if nombre == 7 {
            println!("le nombre est sept");
        } else {
            println!("la condition était fausse");
        }
        ```
    * **`loop` :** Boucle infinie (utilisez `break` pour sortir).
        ```rust
        loop {
            println!("encore !");
            break;
        }
        ```
    * **`while` :** Boucle qui continue tant qu'une condition est vraie.
        ```rust
        let mut compteur = 0;
        while compteur < 5 {
            println!("le compteur est {}", compteur);
            compteur += 1;
        }
        ```
    * **`for` :** Itération sur des collections.
        ```rust
        let a = [10, 20, 30, 40, 50];
        for element in a.iter() {
            println!("la valeur est : {}", element);
        }

        for nombre in 1..5 { // Itère de 1 jusqu'à (mais sans inclure) 5
            println!("{}", nombre);
        }
        ```
    * **`match` :** Constructeur de flux de contrôle puissant qui compare une valeur à une série de motifs.
        ```rust
        let nombre = 3;
        match nombre {
            1 => println!("un"),
            2 | 3 => println!("deux ou trois"),
            4..=6 => println!("quatre, cinq ou six"),
            _ => println!("autre chose"), // Le motif joker
        }
        ```
    * **`if let` :** Une manière plus concise de gérer les enums ou les options lorsque vous ne vous souciez que d'une ou quelques variantes.
        ```rust
        let some_value = Some(5);
        if let Some(x) = some_value {
            println!("La valeur est : {}", x);
        }
        ```

**IV. Propriété, emprunt et durées de vie**

C'est le cœur des garanties de sécurité mémoire de Rust.

* **Propriété :**
    * Chaque valeur en Rust a une variable qui en est le *propriétaire*.
    * Il ne peut y avoir qu'un seul propriétaire d'une valeur à la fois.
    * Lorsque le propriétaire sort de la portée, la valeur sera libérée (sa mémoire est désallouée).
* **Emprunt :**
    * Au lieu de transférer la propriété, vous pouvez créer des références vers une valeur. C'est ce qu'on appelle l'*emprunt*.
    * **Emprunt immuable (`&`) :** Vous pouvez avoir plusieurs références immuables vers une valeur en même temps. Les emprunts immuables ne permettent pas la modification de la valeur empruntée.
    * **Emprunt mutable (`&mut`) :** Vous pouvez avoir au plus une référence mutable vers une valeur à la fois. Les emprunts mutables permettent la modification de la valeur empruntée.
    * **Règles de l'emprunt :**
        1. À tout moment, vous pouvez avoir *soit* une référence mutable *soit* un nombre quelconque de références immuables.
        2. Les références doivent toujours être valides.
* **Durées de vie :**
    * Les durées de vie sont des annotations qui décrivent la portée pour laquelle une référence est valide. Le compilateur Rust utilise les informations de durée de vie pour s'assurer que les références ne survivent pas aux données qu'elles pointent (pointeurs pendants).
    * Dans de nombreux cas, le compilateur peut inférer automatiquement les durées de vie (élision des durées de vie).
    * Vous devrez peut-être annoter explicitement les durées de vie dans les signatures de fonction ou les définitions de struct lorsque les durées de vie des références ne sont pas claires.
    * Exemple d'annotation explicite de durée de vie :
        ```rust
        fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
            if x.len() > y.len() {
                x
            } else {
                y
            }
        }
        ```
        Le `'a` indique que la tranche de chaîne retournée vivra au moins aussi longtemps que les deux tranches de chaîne d'entrée.

**V. Structs, Enums et Modules**

* **Structs :** Types de données définis par l'utilisateur qui regroupent des champs nommés.
    ```rust
    struct User {
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64,
    }

    fn main() {
        let mut user1 = User {
            active: true,
            username: String::from("someusername123"),
            email: String::from("someone@example.com"),
            sign_in_count: 1,
        };

        user1.email = String::from("another@example.com");

        let user2 = User {
            email: String::from("another@example.com"),
            ..user1 // Syntaxe de mise à jour de struct, champs restants de user1
        };
    }
    ```
    * Structs tuple : Tuples nommés sans champs nommés. `struct Color(i32, i32, i32);`
    * Structs unité : Structs sans champs. `struct AlwaysEqual;`
* **Enums (Énumérations) :** Définissent un type en énumérant ses variantes possibles.
    ```rust
    enum Message {
        Quit,
        Move { x: i32, y: i32 }, // Struct anonyme
        Write(String),
        ChangeColor(i32, i32, i32), // Style tuple
    }

    fn main() {
        let q = Message::Quit;
        let m = Message::Move { x: 10, y: 5 };
        let w = Message::Write(String::from("hello"));

        match m {
            Message::Quit => println!("Quitter"),
            Message::Move { x, y } => println!("Se déplacer vers x={}, y={}", x, y),
            Message::Write(text) => println!("Écrire : {}", text),
            Message::ChangeColor(r, g, b) => println!("Changer la couleur en r={}, g={}, b={}", r, g, b),
        }
    }
    ```
    * Les enums peuvent contenir des données directement dans leurs variantes.
* **Modules :** Organisent le code au sein des crates (paquets).
    * Utilisez le mot-clé `mod` pour définir un module.
    * Les modules peuvent contenir d'autres modules, structs, enums, fonctions, etc.
    * Contrôlez la visibilité avec `pub` (public) et privé (par défaut).
    * Accédez aux éléments dans les modules en utilisant le chemin du module (ex. : `mon_module::ma_fonction()`).
    * Importez les éléments dans la portée courante avec le mot-clé `use` (ex. : `use std::collections::HashMap;`).
    * Séparez les modules dans différents fichiers (convention : un module nommé `my_module` va dans `src/my_module.rs` ou `src/my_module/mod.rs`).

**VI. Traits et Génériques**

* **Traits :** Similaires aux interfaces ou aux classes de types dans d'autres langages. Ils définissent un ensemble de méthodes qu'un type doit implémenter pour remplir un certain contrat.
    ```rust
    pub trait Summary {
        fn summarize(&self) -> String;
    }

    pub struct NewsArticle {
        pub headline: String,
        pub location: String,
        pub author: String,
        pub content: String,
    }

    impl Summary for NewsArticle {
        fn summarize(&self) -> String {
            format!("{}, par {} ({})", self.headline, self.author, self.location)
        }
    }

    pub struct Tweet {
        pub username: String,
        pub content: String,
        pub reply: bool,
        pub retweet: bool,
    }

    impl Summary for Tweet {
        fn summarize(&self) -> String {
            format!("{}: {}", self.username, self.content)
        }
    }

    fn main() {
        let tweet = Tweet {
            username: String::from("horse_ebooks"),
            content: String::from("of course, as you probably already know, people"),
            reply: false,
            retweet: false,
        };

        println!("Nouveau tweet disponible ! {}", tweet.summarize());
    }
    ```
    * Les traits peuvent avoir des implémentations par défaut pour les méthodes.
    * Les traits peuvent être utilisés comme contraintes pour les types génériques.
* **Génériques :** Écrivez du code qui peut fonctionner avec plusieurs types sans connaître les types spécifiques au moment de la compilation.
    ```rust
    fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
        let mut largest = list[0];

        for &item in list.iter() {
            if item > largest {
                largest = item;
            }
        }

        largest
    }

    fn main() {
        let number_list = vec![34, 50, 25, 100, 65];
        let result = largest(&number_list);
        println!("Le plus grand nombre est {}", result);

        let char_list = vec!['y', 'm', 'a', 'q'];
        let result = largest(&char_list);
        println!("Le plus grand caractère est {}", result);
    }
    ```
    * Les paramètres de type sont déclarés entre des chevrons `<T>`.
    * Les contraintes de trait (`T: PartialOrd + Copy`) spécifient les fonctionnalités que le type générique doit implémenter.
    * `PartialOrd` permet la comparaison en utilisant `>`, et `Copy` signifie que le type peut être copié par valeur.

**VII. Gestion des erreurs**

Rust met l'accent sur la gestion explicite des erreurs.

* **Enum `Result` :** Représente soit un succès (`Ok`) soit un échec (`Err`).
    ```rust
    enum Result<T, E> {
        Ok(T),
        Err(E),
    }
    ```
    * `T` est le type de la valeur de succès.
    * `E` est le type de la valeur d'erreur.
    * Couramment utilisé pour les opérations qui peuvent échouer (ex. : E/S de fichiers, requêtes réseau).
    * L'opérateur `?` est un sucre syntaxique pour gérer les valeurs `Result`. Si le `Result` est `Ok`, il extrait la valeur ; si c'est `Err`, il retourne l'erreur prématurément de la fonction courante.
* **Macro `panic!` :** Fait planter le programme immédiatement. Généralement utilisée pour des erreurs irrécupérables.
    ```rust
    fn main() {
        let v = vec![1, 2, 3];
        // v[99]; // Cela provoquera un panic à l'exécution
        panic!("Crash and burn!");
    }
    ```
* **Enum `Option` :** Représente une valeur qui peut être présente ou non.
    ```rust
    enum Option<T> {
        Some(T),
        None,
    }
    ```
    * Utilisé pour éviter les pointeurs nuls.
    * Des méthodes comme `unwrap()`, `unwrap_or()`, `map()`, et `and_then()` sont utilisées pour travailler avec les valeurs `Option`.
    ```rust
    fn divide(a: i32, b: i32) -> Option<i32> {
        if b == 0 {
            None
        } else {
            Some(a / b)
        }
    }

    fn main() {
        let result1 = divide(10, 2);
        match result1 {
            Some(value) => println!("Résultat : {}", value),
            None => println!("Division par zéro impossible"),
        }

        let result2 = divide(5, 0);
        println!("Résultat 2: {:?}", result2.unwrap_or(-1)); // Retourne -1 si None
    }
    ```

**VIII. Fermetures et Itérateurs**

* **Fermetures :** Fonctions anonymes qui peuvent capturer des variables de leur portée environnante.
    ```rust
    fn main() {
        let x = 4;
        let equal_to_x = |z| z == x; // Fermeture qui capture x

        println!("Est-ce que 5 est égal à x ? {}", equal_to_x(5));
    }
    ```
    * Syntaxe des fermetures : `|paramètres| -> type_retour { corps }` (le type de retour peut souvent être inféré).
    * Les fermetures peuvent capturer des variables par référence (`&`), par référence mutable (`&mut`) ou par valeur (transfert de propriété). Rust infère le type de capture. Utilisez le mot-clé `move` pour forcer le transfert de propriété.
* **Itérateurs :** Fournissent un moyen de traiter une séquence d'éléments.
    * Créés en appelant la méthode `iter()` sur des collections comme les vecteurs, les tableaux et les tables de hachage (pour l'itération immuable), `iter_mut()` pour l'itération mutable, et `into_iter()` pour consommer la collection et prendre possession de ses éléments.
    * Les itérateurs sont paresseux ; ils ne produisent des valeurs que lorsqu'ils sont explicitement consommés.
    * Adaptateurs d'itérateurs courants (méthodes qui transforment les itérateurs) : `map()`, `filter()`, `take()`, `skip()`, `zip()`, `enumerate()`, etc.
    * Consommateurs d'itérateurs courants (méthodes qui produisent une valeur finale) : `collect()`, `sum()`, `product()`, `fold()`, `any()`, `all()`, etc.
    ```rust
    fn main() {
        let v1 = vec![1, 2, 3];

        let v1_iter = v1.iter(); // Crée un itérateur sur v1

        for val in v1_iter {
            println!("Reçu : {}", val);
        }

        let v2: Vec<_> = v1.iter().map(|x| x + 1).collect(); // Transforme et collecte
        println!("v2: {:?}", v2);

        let sum: i32 = v1.iter().sum(); // Consomme l'itérateur pour obtenir une somme
        println!("Somme de v1: {}", sum);
    }
    ```

**IX. Pointeurs intelligents**

Les pointeurs intelligents sont des structures de données qui agissent comme des pointeurs mais qui ont également des métadonnées et des capacités supplémentaires. Ils imposent des ensembles de règles différents des références classiques.

* **`Box<T>` :** Le pointeur intelligent le plus simple. Il alloue de la mémoire sur le tas et fournit la propriété de la valeur. Lorsque la `Box` sort de la portée, la valeur sur le tas est libérée. Utile pour :
    * Les données dont la taille n'est pas connue à la compilation.
    * Le transfert de propriété de grandes quantités de données.
    * La création de structures de données récursives.
* **`Rc<T>` (Comptage de références) :** Permet à plusieurs parties du programme d'avoir un accès en lecture seule aux mêmes données. Les données ne sont nettoyées que lorsque le dernier pointeur `Rc` sort de la portée. Non thread-safe.
* **`Arc<T>` (Comptage de références atomique) :** Similaire à `Rc<T>` mais thread-safe pour une utilisation dans des scénarios concurrents. A une surcharge de performance par rapport à `Rc<T>`.
* **`Cell<T>` et `RefCell<T>` (Mutabilité intérieure) :** Permettent de modifier des données même lorsqu'il existe des références immuables vers elles. Cela viole les règles d'emprunt habituelles de Rust et est utilisé dans des situations spécifiques et contrôlées.
    * `Cell<T>` : Pour les types qui sont `Copy`. Permet de définir et d'obtenir la valeur.
    * `RefCell<T>` : Pour les types qui ne sont pas `Copy`. Fournit des vérifications d'emprunt à l'exécution (panique si les règles d'emprunt sont violées à l'exécution).
* **`Mutex<T>` et `RwLock<T>` (Primitives de concurrence) :** Fournissent des mécanismes pour un accès mutable partagé sûr entre les threads.
    * `Mutex<T>` : Permet à un seul thread de détenir le verrou et d'accéder aux données à la fois.
    * `RwLock<T>` : Permet à plusieurs lecteurs ou à un seul écrivain d'accéder aux données.

**X. Concurrence**

Rust a un excellent support intégré pour la concurrence.

* **Threads :** Lancez de nouveaux threads du système d'exploitation en utilisant `std::thread::spawn`.
    ```rust
    use std::thread;
    use std::time::Duration;

    fn main() {
        let handle = thread::spawn(|| {
            for i in 1..10 {
                println!("salut numéro {} du thread lancé !", i);
                thread::sleep(Duration::from_millis(1));
            }
        });

        for i in 1..5 {
            println!("salut numéro {} du thread principal !", i);
            thread::sleep(Duration::from_millis(1));
        }

        handle.join().unwrap(); // Attend que le thread lancé se termine
    }
    ```
* **Passage de messages :** Utilisez des canaux (fournis par `std::sync::mpsc`) pour envoyer des données entre les threads.
    ```rust
    use std::sync::mpsc;
    use std::thread;
    use std::time::Duration;

    fn main() {
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let val = String::from("salut");
            tx.send(val).unwrap();
            // println!("val est {}", val); // Erreur : val a été déplacé
        });

        let received = rx.recv().unwrap();
        println!("Reçu : {}", received);
    }
    ```
* **Concurrence par état partagé :** Utilisez des pointeurs intelligents comme `Mutex<T>` et `Arc<T>` pour un accès mutable partagé sûr entre plusieurs threads.

**XI. Macros**

Les macros sont une forme de métaprogrammation en Rust. Elles vous permettent d'écrire du code qui écrit d'autres codes.

* **Macros déclaratives (`macro_rules!`) :** Correspondent à des motifs et les remplacent par d'autres codes. Puissantes pour réduire le code boilerplate.
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
        let my_vec = vec![1, 2, 3, 4];
        println!("{:?}", my_vec);
    }
    ```
* **Macros procédurales :** Plus puissantes et complexes que les macros déclaratives. Elles opèrent sur l'arbre de syntaxe abstraite (AST) du code Rust. Il en existe trois types :
    * **Macros de type fonction :** Ressemblent à des appels de fonction.
    * **Macros de type attribut :** Utilisées avec la syntaxe `#[...]`.
    * **Macros derive :** Utilisées avec `#[derive(...)]` pour implémenter automatiquement des traits.

**XII. Tests**

Rust a un support intégré pour écrire et exécuter des tests.

* **Tests unitaires :** Testent des unités individuelles de code (fonctions, modules). Généralement placés dans le même fichier que le code qu'ils testent, dans un module `#[cfg(test)]`.
    ```rust
    pub fn add(left: usize, right: usize) -> usize {
        left + right
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn it_works() {
            let result = add(2, 2);
            assert_eq!(result, 4);
        }
    }
    ```
* **Tests d'intégration :** Testent comment les différentes parties de votre bibliothèque ou binaire fonctionnent ensemble. Placés dans un répertoire `tests` séparé à la racine de votre projet.
* **Exécution des tests :** Utilisez la commande `cargo test`.

**XIII. Rust non sécurisé**

Les garanties de sécurité de Rust sont appliquées par le compilateur. Cependant, il existe des situations où vous pourriez avoir besoin de contourner ces garanties. Cela se fait en utilisant le mot-clé `unsafe`.

* **Bloc `unsafe` :** Le code dans un bloc `unsafe` peut effectuer des opérations que le compilateur ne peut pas garantir comme sûres, telles que :
    * Déréférencer des pointeurs bruts (`*const T`, `*mut T`).
    * Appeler des fonctions ou méthodes `unsafe`.
    * Accéder aux champs d'`union`s.
    * Lier du code externe (non Rust).
* **Fonctions `unsafe` :** Les fonctions qui contiennent des opérations `unsafe` sont elles-mêmes marquées comme `unsafe`. Appeler une fonction `unsafe` nécessite un bloc `unsafe`.
* **Raisons d'utiliser `unsafe` :** Interface avec des bibliothèques C, programmation système de bas niveau, code critique en performance où les invariants de sécurité sont maintenus manuellement.
* **Note importante :** `unsafe` doit être utilisé avec parcimonie et une extrême prudence. C'est votre responsabilité de garantir la sécurité mémoire dans les blocs `unsafe`.

**XIV. L'écosystème Rust**

* **Crates (Paquets) :** Bibliothèques ou exécutables qui peuvent être utilisés dans les projets Rust. Trouvés sur [https://crates.io/](https://crates.io/).
* **Crates populaires :**
    * `serde` : Sérialisation et désérialisation.
    * `tokio`, `async-std` : Programmation asynchrone.
    * `actix-web`, `rocket` : Frameworks web.
    * `diesel`, `sea-orm` : Object-relational mappers (ORMs).
    * `clap`, `structopt` : Analyse des arguments de ligne de commande.
    * `log`, `env_logger` : Journalisation.
    * `rand` : Génération de nombres aléatoires.
* **Bibliothèque standard Rust (`std`) :** Fournit les fonctionnalités essentielles.

**XV. Ressources d'apprentissage**

* **The Rust Programming Language Book :** Le guide officiel et complet ([https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/)).
* **Rust by Example :** Une collection d'exemples exécutables illustrant diverses fonctionnalités de Rust ([https://doc.rust-lang.org/rust-by-example/](https://doc.rust-lang.org/rust-by-example/)).
* **The Rustlings Course :** Un ensemble de petits exercices pour vous habituer à lire et écrire du code Rust ([https://github.com/rust-lang/rustlings](https://github.com/rust-lang/rustlings)).
* **Rust Documentation :** La documentation API officielle ([https://doc.rust-lang.org/std/](https://doc.rust-lang.org/std/)).
* **The Rust Blog :** Annonces et mises à jour officielles ([https://blog.rust-lang.org/](https://blog.rust-lang.org/)).
* **Reddit (r/rust), Discord, et autres plateformes communautaires.**

Ce guide fournit une base solide pour apprendre Rust. La meilleure façon de devenir compétent est de pratiquer l'écriture de code Rust, d'explorer l'écosystème et d'interagir avec la communauté. Bonne chance dans votre parcours Rust !