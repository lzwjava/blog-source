---
audio: false
generated: true
lang: hant
layout: post
title: RocksDB 的 Java API
translated: true
type: note
---

要使用 `org.rocksdb` 函式庫（即 RocksDB 的 Java API——一個針對鍵值資料的高效能嵌入式資料庫），您需要遵循以下步驟。RocksDB 針對快速儲存和檢索進行了優化，非常適合需要通過已知鍵快速存取資料的應用程式。以下是一份完整的入門指南：

---

### 1. **添加依賴項**
要在 Java 專案中使用 `org.rocksdb`，您需要包含 RocksDB JNI（Java Native Interface）依賴項。如果您使用 Maven，請將以下內容添加到您的 `pom.xml` 檔案中：

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

對於 Gradle，請將以下內容添加到您的 `build.gradle`：

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**注意**：請檢查 [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) 以獲取最新版本，因為 `7.10.2` 可能不是當前版本。

---

### 2. **載入原生函式庫**
RocksDB 依賴於原生的 C++ 程式碼，因此在使用前必須載入原生函式庫。在程式碼開頭添加這一行：

```java
RocksDB.loadLibrary();
```

如果未執行此操作，將導致執行時錯誤。

---

### 3. **開啟資料庫**
要開始使用 RocksDB，您需要透過指定資料庫儲存檔案的檔案路徑來開啟資料庫實例。使用 `Options` 類別來配置設定，例如在資料庫不存在時建立資料庫：

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/path/to/db");
```

- **`options`**：配置資料庫行為（例如，`setCreateIfMissing(true)` 確保在資料庫不存在時建立資料庫）。
- **`/path/to/db`**：請將其替換為系統上有效的目錄路徑，資料庫檔案將儲存在此處。

---

### 4. **執行基本操作**
RocksDB 是一個鍵值儲存庫，其核心操作是 `put`、`get` 和 `delete`。鍵和值以位元組陣列的形式儲存，因此您需要將資料（例如字串）轉換為位元組。

- **Put**：插入或更新鍵值對。
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get**：檢索與鍵關聯的值。
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // 輸出 "value"
  } else {
      System.out.println("Key not found");
  }
  ```

- **Delete**：移除鍵值對。
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **關閉資料庫**
正確關閉資料庫對於釋放資源至關重要。最簡單的方法是使用 try-with-resources 區塊，該區塊會在操作完成後自動關閉資料庫：

```java
try (RocksDB db = RocksDB.open(options, "/path/to/db")) {
    // 在此處執行操作
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **處理異常**
RocksDB 操作可能會拋出 `RocksDBException`，因此請始終包含異常處理，以防止資源洩漏或資料損壞：

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **配置選項**
您可以使用 `Options` 類別微調 RocksDB 的效能。例如：

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // 64MB 寫入緩衝區
```

常見選項包括：
- `setWriteBufferSize`：控制用於寫入的記憶體。
- `setMaxOpenFiles`：限制開啟檔案的數量。
- `setCompactionStyle`：調整磁碟上資料的壓縮方式。

請參閱 [RocksDB 文件](https://github.com/facebook/rocksdb/wiki) 以獲取更多選項。

---

### 8. **簡單範例**
以下是一個完整的範例，演示如何開啟資料庫、儲存鍵值對並檢索它：

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // 載入原生函式庫
        Options options = new Options().setCreateIfMissing(true);
        
        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // 放入鍵值對
            db.put("hello".getBytes(), "world".getBytes());
            
            // 獲取值
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // 輸出 "world"
            } else {
                System.out.println("Key not found");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**輸出**：`world`

---

### 關鍵注意事項
- **嵌入式特性**：RocksDB 在您的應用程式進程內運行，而不是作為單獨的伺服器。
- **位元組陣列**：鍵和值是 `byte[]`，因此對於複雜物件，您需要處理序列化/反序列化。
- **效能**：RocksDB 在快速儲存（例如 SSD）上表現出色，並被用於高效能系統，例如其開發者 Facebook 的系統。
- **非關聯式**：它是一個鍵值儲存庫，而不是關聯式資料庫——沒有 SQL 或聯結。

---

### 常見陷阱
- **忘記 `RocksDB.loadLibrary()`**：導致 `UnsatisfiedLinkError`。
- **不當的資源管理**：未關閉資料庫可能導致問題，尤其是在資源受限的系統上。
- **資料類型錯誤**：直接傳遞字串或物件，而不是轉換為 `byte[]`。

---

### 進一步學習
- **進階功能**：探索交易、快照或列族以應對更複雜的使用場景。
- **資源**：查看 [RocksDB Java API](https://github.com/facebook/rocksdb/tree/main/java) 和 [RocksDB Wiki](https://github.com/facebook/rocksdb/wiki) 以獲取詳細的文件和範例。

本指南為使用 `org.rocksdb` 提供了堅實的基礎。如果您需要有關特定功能或用例的幫助，請隨時提問！