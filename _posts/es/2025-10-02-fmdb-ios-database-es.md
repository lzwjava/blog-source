---
audio: false
generated: true
image: false
lang: es
layout: post
model: deepseek/deepseek-v3.2-exp
title: FMDB para Operaciones de Base de Datos en iOS
translated: true
type: note
---

FMDB es un wrapper de Objective-C alrededor de SQLite que facilita y hace más intuitivas las operaciones de base de datos para los desarrolladores de iOS y macOS.

## ¿Qué es FMDB?

FMDB proporciona una interfaz más limpia y orientada a objetos para SQLite con características como:
- Gestión automática de conexiones
- Manejo de errores
- Seguridad para hilos (thread safety)
- Métodos convenientes para operaciones comunes

## Instalación

### Usando CocoaPods
Añade a tu Podfile:
```ruby
pod 'FMDB'
```

### Usando Swift Package Manager
Añade la dependencia del paquete: `https://github.com/ccgus/fmdb`

## Uso Básico

### 1. Importar y Configurar
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

### 2. Abrir y Cerrar la Base de Datos
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

### 3. Crear Tablas
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

### 4. Insertar Datos
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

### 5. Consultar Datos
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

### 6. Actualizar Datos
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

### 7. Eliminar Datos
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

## Usando FMDatabaseQueue para Seguridad en Hilos

Para aplicaciones multi-hilo, usa `FMDatabaseQueue`:

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

## Transacciones

```swift
func performTransaction() {
    guard openDatabase() else { return }
    
    do {
        try database.beginTransaction()
        
        // Múltiples operaciones
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

## Mejores Prácticas

1. **Siempre cierra la base de datos** cuando termines de usarla
2. **Usa FMDatabaseQueue** para aplicaciones multi-hilo
3. **Usa consultas parametrizadas** para prevenir inyección SQL
4. **Maneja los errores adecuadamente** - verifica los valores de retorno y captura las excepciones
5. **Usa transacciones** para múltiples operaciones relacionadas

## Ejemplo de Modelo de Datos

```swift
struct User {
    let id: Int
    let name: String
    let email: String
    let age: Int
}
```

FMDB proporciona una forma robusta y eficiente de trabajar con bases de datos SQLite en aplicaciones iOS, haciendo que las operaciones de base de datos sean más manejables mientras mantiene el poder y la flexibilidad de SQLite.