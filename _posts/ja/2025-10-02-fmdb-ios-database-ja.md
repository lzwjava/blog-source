---
audio: false
generated: true
image: false
lang: ja
layout: post
model: deepseek/deepseek-v3.2-exp
title: iOSデータベース操作のためのFMDB
translated: true
type: note
---

FMDBは、iOSおよびmacOS開発者向けにデータベース操作をより簡単で直感的にするSQLiteのObjective-Cラッパーです。

## FMDBとは？

FMDBは、以下のような機能を備えたSQLiteへのよりクリーンでオブジェクト指向なインターフェースを提供します：
- 自動接続管理
- エラーハンドリング
- スレッドセーフティ
- 一般的な操作のための便利なメソッド

## インストール

### CocoaPodsを使用する場合
Podfileに追加：
```ruby
pod 'FMDB'
```

### Swift Package Managerを使用する場合
パッケージ依存関係を追加：`https://github.com/ccgus/fmdb`

## 基本的な使用方法

### 1. インポートとセットアップ
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

### 2. データベースのオープンとクローズ
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

### 3. テーブルの作成
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

### 4. データの挿入
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

### 5. データのクエリ
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

### 6. データの更新
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

### 7. データの削除
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

## スレッドセーフティのためのFMDatabaseQueueの使用

マルチスレッドアプリケーションでは、`FMDatabaseQueue`を使用します：

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

## トランザクション

```swift
func performTransaction() {
    guard openDatabase() else { return }
    
    do {
        try database.beginTransaction()
        
        // 複数の操作
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

## ベストプラクティス

1. **データベースは必ずクローズする** - 使用が終わったら必ずクローズすること
2. **マルチスレッドアプリケーションではFMDatabaseQueueを使用する**
3. **SQLインジェクションを防ぐためにパラメータ化されたクエリを使用する**
4. **エラーを適切に処理する** - 戻り値をチェックし、例外をキャッチすること
5. **複数の関連する操作にはトランザクションを使用する**

## データモデルの例

```swift
struct User {
    let id: Int
    let name: String
    let email: String
    let age: Int
}
```

FMDBは、iOSアプリケーションでSQLiteデータベースを扱うための堅牢で効率的な方法を提供し、SQLiteのパワーと柔軟性を維持しながらデータベース操作をより管理しやすくします。