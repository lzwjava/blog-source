---
audio: false
generated: true
image: false
lang: hant
layout: post
model: deepseek/deepseek-v3.2-exp
title: iOS 數據庫操作之 FMDB
translated: true
type: note
---

FMDB 是一個封裝 SQLite 的 Objective-C 套件，讓 iOS 和 macOS 開發者能更輕鬆直覺地進行資料庫操作。

## 什麼是 FMDB？

FMDB 為 SQLite 提供了更清晰、更具物件導向風格的介面，具備以下功能：
- 自動連線管理
- 錯誤處理
- 執行緒安全
- 常用操作的便捷方法

## 安裝方式

### 使用 CocoaPods
在 Podfile 中加入：
```ruby
pod 'FMDB'
```

### 使用 Swift Package Manager
添加套件依賴：`https://github.com/ccgus/fmdb`

## 基礎用法

### 1. 導入與設定
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

### 2. 開啟與關閉資料庫
```swift
func openDatabase() -> Bool {
    guard database.open() else {
        print("無法開啟資料庫：\(database.lastErrorMessage())")
        return false
    }
    return true
}

func closeDatabase() {
    database.close()
}
```

### 3. 建立資料表
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
        print("資料表建立成功")
    } catch {
        print("建立資料表時發生錯誤：\(error.localizedDescription)")
    }
    
    closeDatabase()
}
```

### 4. 插入資料
```swift
func insertUser(name: String, email: String, age: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let insertSQL = "INSERT INTO Users (name, email, age) VALUES (?, ?, ?)"
    
    do {
        try database.executeUpdate(insertSQL, values: [name, email, age])
        print("使用者資料插入成功")
        closeDatabase()
        return true
    } catch {
        print("插入使用者資料時發生錯誤：\(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

### 5. 查詢資料
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
        print("查詢使用者資料時發生錯誤：\(error.localizedDescription)")
    }
    
    closeDatabase()
    return users
}
```

### 6. 更新資料
```swift
func updateUserAge(userId: Int, newAge: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let updateSQL = "UPDATE Users SET age = ? WHERE id = ?"
    
    do {
        try database.executeUpdate(updateSQL, values: [newAge, userId])
        print("使用者資料更新成功")
        closeDatabase()
        return true
    } catch {
        print("更新使用者資料時發生錯誤：\(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

### 7. 刪除資料
```swift
func deleteUser(userId: Int) -> Bool {
    guard openDatabase() else { return false }
    
    let deleteSQL = "DELETE FROM Users WHERE id = ?"
    
    do {
        try database.executeUpdate(deleteSQL, values: [userId])
        print("使用者資料刪除成功")
        closeDatabase()
        return true
    } catch {
        print("刪除使用者資料時發生錯誤：\(error.localizedDescription)")
        closeDatabase()
        return false
    }
}
```

## 使用 FMDatabaseQueue 實現執行緒安全

在多執行緒應用程式中，請使用 `FMDatabaseQueue`：

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
                print("使用者資料插入成功")
            } catch {
                print("插入使用者資料時發生錯誤：\(error.localizedDescription)")
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
                print("查詢使用者資料時發生錯誤：\(error.localizedDescription)")
                DispatchQueue.main.async {
                    completion([])
                }
            }
        }
    }
}
```

## 交易處理

```swift
func performTransaction() {
    guard openDatabase() else { return }
    
    do {
        try database.beginTransaction()
        
        // 多個操作
        try database.executeUpdate("INSERT INTO Users (name, email, age) VALUES (?, ?, ?)", 
                                 values: ["John", "john@example.com", 25])
        try database.executeUpdate("INSERT INTO Users (name, email, age) VALUES (?, ?, ?)", 
                                 values: ["Jane", "jane@example.com", 30])
        
        try database.commit()
        print("交易完成成功")
    } catch {
        try? database.rollback()
        print("交易失敗：\(error.localizedDescription)")
    }
    
    closeDatabase()
}
```

## 最佳實踐

1. **操作完成後務必關閉資料庫**
2. **多執行緒應用請使用 FMDatabaseQueue**
3. **使用參數化查詢防止 SQL 注入**
4. **妥善處理錯誤** - 檢查回傳值並捕獲例外
5. **多個相關操作請使用交易處理**

## 資料模型範例

```swift
struct User {
    let id: Int
    let name: String
    let email: String
    let age: Int
}
```

FMDB 為 iOS 應用程式提供了強大且高效的方式來操作 SQLite 資料庫，讓資料庫操作更易管理，同時保持 SQLite 的強大功能與靈活性。