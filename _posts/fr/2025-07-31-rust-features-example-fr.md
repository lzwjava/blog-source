---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Exemple des principales fonctionnalités de Rust
translated: true
type: note
---

Voici un exemple de code Rust simple qui démontre plusieurs fonctionnalités clés, incluant l'emprunt, la mutabilité, la propriété, les structs, les enums, le pattern matching et plus encore. Je le garderai concis mais illustratif, avec des commentaires expliquant chaque fonctionnalité.

```rust
// Définition d'une struct pour représenter un Point
struct Point {
    x: i32,
    y: i32,
}

// Définition d'un enum pour différentes formes
enum Shape {
    Circle(Point, f32), // Point central et rayon
    Rectangle(Point, i32, i32), // Point en haut à gauche, largeur, hauteur
}

// Implémentation de méthodes pour Point
impl Point {
    // Emprunt immuable pour calculer la distance depuis l'origine
    fn distance_from_origin(&self) -> f32 {
        ((self.x.pow(2) + self.y.pow(2)) as f32).sqrt()
    }

    // Emprunt mutable pour translater le point
    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

// Fonction démontrant la propriété et l'emprunt
fn describe_shape(shape: &Shape) -> String {
    match shape {
        Shape::Circle(center, radius) => {
            // Emprunt immuable du centre
            format!(
                "Cercle en ({}, {}) avec un rayon {}",
                center.x, center.y, radius
            )
        }
        Shape::Rectangle(top_left, width, height) => {
            // Emprunt immuable du point en haut à gauche
            format!(
                "Rectangle en ({}, {}) avec une largeur {}, hauteur {}",
                top_left.x, top_left.y, width, height
            )
        }
    }
}

fn main() {
    // Liaison de variable mutable
    let mut point = Point { x: 3, y: 4 };
    
    // Emprunt immuable pour appeler une méthode
    println!("Distance depuis l'origine: {}", point.distance_from_origin());
    
    // Emprunt mutable pour modifier le point
    point.translate(2, 1);
    println!("Après translation: ({}, {})", point.x, point.y);
    
    // Création d'une forme (propriété transférée à la variable)
    let circle = Shape::Circle(point, 5.0);
    
    // Emprunt immuable de la forme pour la décrire
    println!("Forme: {}", describe_shape(&circle));
    
    // Vecteur avec propriété des éléments
    let mut shapes: Vec<Shape> = Vec::new();
    shapes.push(circle);
    shapes.push(Shape::Rectangle(Point { x: 0, y: 0 }, 10, 20));
    
    // Itération avec emprunt immuable
    for shape in &shapes {
        println!("Forme dans le vec: {}", describe_shape(shape));
    }
    
    // Option et pattern matching
    let maybe_number: Option<i32> = Some(42);
    match maybe_number {
        Some(num) => println!("Reçu un nombre: {}", num),
        None => println!("Aucun nombre"),
    }
    
    // Result pour la gestion d'erreurs
    let result: Result<i32, &str> = Ok(100);
    if let Ok(value) = result {
        println!("Valeur du résultat: {}", value);
    }
}
```

### Fonctionnalités Clés Démontrées :
1. **Structs** : Struct `Point` pour représenter un point 2D.
2. **Enums** : Enum `Shape` pour représenter différentes formes (Cercle, Rectangle).
3. **Propriété** : La variable `circle` prend possession de `point` lors de sa création.
4. **Emprunt** :
   - Emprunt immuable (`&self`) dans `distance_from_origin`.
   - Emprunt mutable (`&mut self`) dans `translate`.
   - Emprunt immuable (`&Shape`) dans `describe_shape`.
5. **Mutabilité** : Mot-clé `mut` pour les variables mutables (`point`, `shapes`).
6. **Pattern Matching** : Utilisé avec `match` dans `describe_shape` et pour `Option`.
7. **Méthodes** : Définies dans le bloc `impl Point`.
8. **Vecteurs** : `Vec<Shape>` pour stocker une collection de formes.
9. **Option** : Gestion de valeurs optionnelles avec `Some` et `None`.
10. **Result** : Gestion d'erreurs basique avec `Ok` et `Err`.
11. **Formatage de chaînes** : Utilisation de `format!` pour les chaînes dynamiques.

### Sortie (lors de l'exécution) :
```
Distance depuis l'origine: 5
Après translation: (5, 5)
Forme: Cercle en (5, 5) avec un rayon 5
Forme dans le vec: Cercle en (5, 5) avec un rayon 5
Forme dans le vec: Rectangle en (0, 0) avec une largeur 10, hauteur 20
Reçu un nombre: 42
Valeur du résultat: 100
```

Ce code est concis mais met en valeur les concepts fondamentaux de Rust comme la propriété, l'emprunt et la mutabilité, ainsi que son système de type et sa gestion d'erreurs. Vous pouvez l'exécuter en utilisant `rustc` ou un projet Rust avec `cargo run`. Faites-moi savoir si vous souhaitez une exploration plus approfondie de n'importe quelle fonctionnalité spécifique !