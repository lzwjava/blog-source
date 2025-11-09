---
audio: false
generated: true
image: false
lang: de
layout: post
model: deepseek/deepseek-v3.2-exp
title: FMDB für iOS Datenbankoperationen
translated: true
type: note
---

FMDB ist ein Objective-C-Wrapper um SQLite, der Datenbankoperationen für iOS- und macOS-Entwickler einfacher und intuitiver macht.

## Was ist FMDB?

FMDB bietet eine sauberere, objektorientiertere Schnittstelle zu SQLite mit Funktionen wie:
- Automatische Verbindungsverwaltung
- Fehlerbehandlung
- Thread-Sicherheit
- Praktische Methoden für gängige Operationen

## Installation

### CocoaPods verwenden
Fügen Sie dies zu Ihrer Podfile hinzu:
```ruby
pod 'FMDB'
```

### Swift Package Manager verwenden
Fügen Sie die Paketabhängigkeit hinzu: `https://github.com/ccgus/fmdb`

## Grundlegende Verwendung

### 1. Import und Einrichtung
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

### 2. Datenbank öffnen und schließen
```swift
func openDatabase() -> Bool {
    guard database.open() else {
        print("Unable to open database: \(database.lastErrorMessage())")
        return false
    }
    return true
}

func closeDatabase() {
    database.close()
}
```

### 3. Tabellen erstellen
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
        print("Table created successfully")
    } catch {
        print("Error creating table: \(error.localizedDescription)")
    }
    
    closeDatabase()
}
```

### 4. Daten einfügen
```swift
func insertUser(name: String, email: String, age: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let insertSQL = "INSERT INTO Users (name, email, age) VALUES (?, ?, ?)"
    
    do {
        try database.executeUpdate(insertSQL, values: [name, email, age])
        print("User inserted successfully")
        closeDatabase()
        return true
    } catch {
        print("Error inserting user: \(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

### 5. Daten abfragen
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
        print("Error querying users: \(error.localizedDescription)")
    }
    
    closeDatabase()
    return users
}
```

### 6. Daten aktualisieren
```swift
func updateUserAge(userId: Int, newAge: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let updateSQL = "UPDATE Users SET age = ? WHERE id = ?"
    
    do {
        try database.executeUpdate(updateSQL, values: [newAge, userId])
        print("User updated successfully")
        closeDatabase()
        return true
    } catch {
        print("Error updating user: \(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

### 7. Daten löschen
```swift
func deleteUser(userId: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let deleteSQL = "DELETE FROM Users WHERE id = ?"
    
    do {
        try database.executeUpdate(deleteSQL, values: [userId])
        print("User deleted successfully")
        closeDatabase()
        return true
    } catch {
        print("Error deleting user: \(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

## Verwendung von FMDatabaseQueue für Thread-Sicherheit

Für mehrthreadige Anwendungen verwenden Sie `FMDatabaseQueue`:

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
                print("User inserted successfully")
            } catch {
                print("Error inserting user: \(error.localizedDescription)")
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
                print("Error querying users: \(error.localizedDescription)")
                DispatchQueue.main.async {
                    completion([])
                }
            }
        }
    }
}
```

## Transaktionen

```swift
func performTransaction() {
    guard openDatabase() else { return }
    
    do {
        try database.beginTransaction()
        
        // Mehrere Operationen
        try database.executeUpdate("INSERT INTO Users (name, email, age) VALUES (?, ?, ?)", 
                                 values: ["John", "john@example.com", 25])
        try database.executeUpdate("INSERT INTO Users (name, email, age) VALUES (?, ?, ?)", 
                                 values: ["Jane", "jane@example.com", 30])
        
        try database.commit()
        print("Transaction completed successfully")
    } catch {
        try? database.rollback()
        print("Transaction failed: \(error.localizedDescription)")
    }
    
    closeDatabase()
}
```

## Best Practices

1. **Schließen Sie die Datenbank immer**, wenn Sie fertig sind
2. **Verwenden Sie FMDatabaseQueue** für mehrthreadige Anwendungen
3. **Verwenden Sie parametrisierte Abfragen**, um SQL-Injection zu verhindern
4. **Behandeln Sie Fehler ordnungsgemäß** - überprüfen Sie Rückgabewerte und fangen Sie Ausnahmen ab
5. **Verwenden Sie Transaktionen** für mehrere zusammenhängende Operationen

## Datenmodell-Beispiel

```swift
struct User {
    let id: Int
    let name: String
    let email: String
    let age: Int
}
```

FMDB bietet eine robuste und effiziente Möglichkeit, mit SQLite-Datenbanken in iOS-Anwendungen zu arbeiten, macht Datenbankoperationen besser handhabbar und behält dabei die Leistungsfähigkeit und Flexibilität von SQLite bei.