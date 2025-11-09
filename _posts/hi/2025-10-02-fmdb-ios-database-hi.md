---
audio: false
generated: true
image: false
lang: hi
layout: post
model: deepseek/deepseek-v3.2-exp
title: आईओएस डेटाबेस ऑपरेशन के लिए एफएमडीबी
translated: true
type: note
---

FMDB एक SQLite के चारों ओर बना Objective-C रैपर है जो iOS और macOS डेवलपर्स के लिए डेटाबेस ऑपरेशन्स को आसान और अधिक सहज बनाता है।

## FMDB क्या है?

FMDB SQLite के लिए एक साफ़, अधिक ऑब्जेक्ट-ओरिएंटेड इंटरफेस प्रदान करता है जिसमें फीचर्स शामिल हैं जैसे:
- स्वचालित कनेक्शन प्रबंधन
- एरर हैंडलिंग
- थ्रेड सेफ्टी
- सामान्य ऑपरेशन्स के लिए सुविधाजनक मेथड्स

## इंस्टालेशन

### CocoaPods का उपयोग करके
अपनी Podfile में जोड़ें:
```ruby
pod 'FMDB'
```

### Swift Package Manager का उपयोग करके
पैकेज डिपेंडेंसी जोड़ें: `https://github.com/ccgus/fmdb`

## बेसिक उपयोग

### 1. इम्पोर्ट और सेटअप
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

### 2. डेटाबेस खोलना और बंद करना
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

### 3. टेबल बनाना
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

### 4. डेटा इन्सर्ट करना
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

### 5. डेटा क्वेरी करना
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

### 6. डेटा अपडेट करना
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

### 7. डेटा डिलीट करना
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

## थ्रेड सेफ्टी के लिए FMDatabaseQueue का उपयोग

मल्टी-थ्रेडेड एप्लिकेशन्स के लिए, `FMDatabaseQueue` का उपयोग करें:

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

## ट्रांजैक्शन्स

```swift
func performTransaction() {
    guard openDatabase() else { return }
    
    do {
        try database.beginTransaction()
        
        // एक से अधिक ऑपरेशन्स
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

## बेस्ट प्रैक्टिसेज़

1. **डेटाबेस को हमेशा बंद करें** जब आप इसके साथ काम पूरा कर लें
2. **मल्टी-थ्रेडेड एप्लिकेशन्स के लिए FMDatabaseQueue का उपयोग करें**
3. **SQL इंजेक्शन को रोकने के लिए पैरामीटराइज्ड क्वेरीज़ का उपयोग करें**
4. **एरर्स को ठीक से हैंडल करें** - रिटर्न वैल्यूज़ चेक करें और एक्सेप्शन्स कैच करें
5. **एक से अधिक संबंधित ऑपरेशन्स के लिए ट्रांजैक्शन्स का उपयोग करें**

## डेटा मॉडल उदाहरण

```swift
struct User {
    let id: Int
    let name: String
    let email: String
    let age: Int
}
```

FMDB iOS एप्लिकेशन्स में SQLite डेटाबेस के साथ काम करने का एक मजबूत और कुशल तरीका प्रदान करता है, जो डेटाबेस ऑपरेशन्स को अधिक प्रबंधनीय बनाते हुए SQLite की शक्ति और लचीलापन बनाए रखता है।