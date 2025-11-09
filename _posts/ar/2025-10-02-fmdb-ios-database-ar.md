---
audio: false
generated: true
image: false
lang: ar
layout: post
model: deepseek/deepseek-v3.2-exp
title: إف إم دي بي لعمليات قاعدة بيانات آي أو إس
translated: true
type: note
---

FMDB هو غلاف Objective-C حول SQLite يجعل عمليات قاعدة البيانات أسهل وأكثر بديهية لمطوري iOS وmacOS.

## ما هو FMDB؟

يوفر FMDB واجهة أنظف وأكثر توجهاً للكائنات لـ SQLite مع ميزات مثل:
- إدارة اتصال تلقائية
- معالجة الأخطاء
- أمان الخيوط
- طرق ملائمة للعمليات الشائعة

## التثبيت

### باستخدام CocoaPods
أضف إلى ملف Podfile الخاص بك:
```ruby
pod 'FMDB'
```

### باستخدام Swift Package Manager
أضف تبعية الحزمة: `https://github.com/ccgus/fmdb`

## الاستخدام الأساسي

### 1. الاستيراد والإعداد
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

### 2. فتح وإغلاق قاعدة البيانات
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

### 3. إنشاء الجداول
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

### 4. إدراج البيانات
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

### 5. استعلام البيانات
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

### 6. تحديث البيانات
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

### 7. حذف البيانات
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

## استخدام FMDatabaseQueue لأمان الخيوط

للتطبيقات متعددة الخيوط، استخدم `FMDatabaseQueue`:

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

## المعاملات

```swift
func performTransaction() {
    guard openDatabase() else { return }
    
    do {
        try database.beginTransaction()
        
        // عمليات متعددة
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

## أفضل الممارسات

1. **أغلق قاعدة البيانات دائماً** عندما تنتهي منها
2. **استخدم FMDatabaseQueue** للتطبيقات متعددة الخيوط
3. **استخدم الاستعلامات المعلمة** لمنع حقن SQL
4. **تعامل مع الأخطاء بشكل صحيح** - تحقق من القيم المرتجعة والتقط الاستثناءات
5. **استخدم المعاملات** للعمليات المتعددة المرتبطة

## مثال نموذج البيانات

```swift
struct User {
    let id: Int
    let name: String
    let email: String
    let age: Int
}
```

يوفر FMDB طريقة قوية وفعالة للعمل مع قواعد بيانات SQLite في تطبيقات iOS، مما يجعل عمليات قاعدة البيانات أكثر قابلية للإدارة مع الحفاظ على قوة ومرونة SQLite.