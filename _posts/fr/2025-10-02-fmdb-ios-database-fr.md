---
audio: false
generated: true
image: false
lang: fr
layout: post
model: deepseek/deepseek-v3.2-exp
title: FMDB pour les opérations de base de données iOS
translated: true
type: note
---

FMDB est un wrapper Objective-C autour de SQLite qui facilite et rend plus intuitives les opérations sur les bases de données pour les développeurs iOS et macOS.

## Qu'est-ce que FMDB ?

FMDB fournit une interface plus propre et plus orientée objet à SQLite avec des fonctionnalités comme :
- Gestion automatique des connexions
- Gestion des erreurs
- Sûreté du thread (Thread safety)
- Méthodes pratiques pour les opérations courantes

## Installation

### Utilisation de CocoaPods
Ajoutez à votre Podfile :
```ruby
pod 'FMDB'
```

### Utilisation de Swift Package Manager
Ajoutez la dépendance de package : `https://github.com/ccgus/fmdb`

## Utilisation de base

### 1. Importation et Configuration
```swift
import FMDB

class DatabaseManager {
    private let database: FMDatabase
    
    init() {
        let documentsPath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
        let databaseURL = documentsPath.appendingPathComponent("mydatabase.sqlite")
        database = FMDatabase(url: databaseURL)
    }
}
```

### 2. Ouvrir et Fermer la Base de Données
```swift
func openDatabase() -> Bool {
    guard database.open() else {
        print("Impossible d'ouvrir la base de données: \(database.lastErrorMessage())")
        return false
    }
    return true
}

func closeDatabase() {
    database.close()
}
```

### 3. Créer des Tables
```swift
func createTables() {
    guard openDatabase() else { return }
    
    let createTableSQL = """
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    );
    """
    
    do {
        try database.executeUpdate(createTableSQL, values: nil)
        print("Table créée avec succès")
    } catch {
        print("Erreur lors de la création de la table: \(error.localizedDescription)")
    }
    
    closeDatabase()
}
```

### 4. Insérer des Données
```swift
func insertUser(name: String, email: String, age: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let insertSQL = "INSERT INTO Users (name, email, age) VALUES (?, ?, ?)"
    
    do {
        try database.executeUpdate(insertSQL, values: [name, email, age])
        print("Utilisateur inséré avec succès")
        closeDatabase()
        return true
    } catch {
        print("Erreur lors de l'insertion de l'utilisateur: \(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

### 5. Interroger les Données
```swift
func getAllUsers() -> [User] {
    guard openDatabase() else { return [] }
    
    let querySQL = "SELECT * FROM Users"
    var users: [User] = []
    
    do {
        let resultSet = try database.executeQuery(querySQL, values: nil)
        
        while resultSet.next() {
            let id = resultSet.int(forColumn: "id")
            let name = resultSet.string(forColumn: "name") ?? ""
            let email = resultSet.string(forColumn: "email") ?? ""
            let age = resultSet.int(forColumn: "age")
            
            let user = User(id: Int(id), name: name, email: email, age: Int(age))
            users.append(user)
        }
    } catch {
        print("Erreur lors de la requête des utilisateurs: \(error.localizedDescription)")
    }
    
    closeDatabase()
    return users
}
```

### 6. Mettre à Jour les Données
```swift
func updateUserAge(userId: Int, newAge: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let updateSQL = "UPDATE Users SET age = ? WHERE id = ?"
    
    do {
        try database.executeUpdate(updateSQL, values: [newAge, userId])
        print("Utilisateur mis à jour avec succès")
        closeDatabase()
        return true
    } catch {
        print("Erreur lors de la mise à jour de l'utilisateur: \(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

### 7. Supprimer des Données
```swift
func deleteUser(userId: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let deleteSQL = "DELETE FROM Users WHERE id = ?"
    
    do {
        try database.executeUpdate(deleteSQL, values: [userId])
        print("Utilisateur supprimé avec succès")
        closeDatabase()
        return true
    } catch {
        print("Erreur lors de la suppression de l'utilisateur: \(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

## Utilisation de FMDatabaseQueue pour la Sûreté du Thread

Pour les applications multi-threads, utilisez `FMDatabaseQueue` :

```swift
class ThreadSafeDatabaseManager {
    private let databaseQueue: FMDatabaseQueue
    
    init() {
        let documentsPath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
        let databaseURL = documentsPath.appendingPathComponent("mydatabase.sqlite")
        databaseQueue = FMDatabaseQueue(url: databaseURL)!
    }
    
    func insertUserThreadSafe(name: String, email: String, age: Int) {
        databaseQueue.inDatabase { db in
            let insertSQL = "INSERT INTO Users (name, email, age) VALUES (?, ?, ?)"
            do {
                try db.executeUpdate(insertSQL, values: [name, email, age])
                print("Utilisateur inséré avec succès")
            } catch {
                print("Erreur lors de l'insertion de l'utilisateur: \(error.localizedDescription)")
            }
        }
    }
    
    func getAllUsersThreadSafe(completion: @escaping ([User]) -> Void) {
        databaseQueue.inDatabase { db in
            var users: [User] = []
            let querySQL = "SELECT * FROM Users"
            
            do {
                let resultSet = try db.executeQuery(querySQL, values: nil)
                
                while resultSet.next() {
                    let id = resultSet.int(forColumn: "id")
                    let name = resultSet.string(forColumn: "name") ?? ""
                    let email = resultSet.string(forColumn: "email") ?? ""
                    let age = resultSet.int(forColumn: "age")
                    
                    let user = User(id: Int(id), name: name, email: email, age: Int(age))
                    users.append(user)
                }
                
                DispatchQueue.main.async {
                    completion(users)
                }
            } catch {
                print("Erreur lors de la requête des utilisateurs: \(error.localizedDescription)")
                DispatchQueue.main.async {
                    completion([])
                }
            }
        }
    }
}
```

## Transactions

```swift
func performTransaction() {
    guard openDatabase() else { return }
    
    do {
        try database.beginTransaction()
        
        // Opérations multiples
        try database.executeUpdate("INSERT INTO Users (name, email, age) VALUES (?, ?, ?)", 
                                 values: ["John", "john@example.com", 25])
        try database.executeUpdate("INSERT INTO Users (name, email, age) VALUES (?, ?, ?)", 
                                 values: ["Jane", "jane@example.com", 30])
        
        try database.commit()
        print("Transaction terminée avec succès")
    } catch {
        try? database.rollback()
        print("Échec de la transaction: \(error.localizedDescription)")
    }
    
    closeDatabase()
}
```

## Bonnes Pratiques

1. **Toujours fermer la base de données** lorsque vous avez terminé
2. **Utilisez FMDatabaseQueue** pour les applications multi-threads
3. **Utilisez des requêtes paramétrées** pour prévenir l'injection SQL
4. **Gérez les erreurs correctement** - vérifiez les valeurs de retour et capturez les exceptions
5. **Utilisez les transactions** pour les opérations multiples liées

## Exemple de Modèle de Données

```swift
struct User {
    let id: Int
    let name: String
    let email: String
    let age: Int
}
```

FMDB fournit un moyen robuste et efficace de travailler avec les bases de données SQLite dans les applications iOS, rendant les opérations sur les bases de données plus gérables tout en conservant la puissance et la flexibilité de SQLite.