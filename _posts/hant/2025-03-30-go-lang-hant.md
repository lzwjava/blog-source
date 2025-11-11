---
audio: false
generated: true
lang: hant
layout: post
title: Go 程式語言全面指南
translated: true
type: note
---

本指南旨在全面概述 Go 程式語言，涵蓋其基礎知識、核心概念及進階功能。無論是具備一些程式設計經驗的初學者，還是希望從其他語言轉換過來的開發者，本指南都適用。

**I. Go 語言簡介**

* **什麼是 Go？**
    * Go（通常稱為 Golang）是一種靜態型別、編譯式程式語言，由 Google 的 Robert Griesemer、Rob Pike 和 Ken Thompson 設計。
    * 它強調簡潔性、並行處理和效能。
    * Go 是開源的，並擁有一個充滿活力且不斷成長的社群。
* **主要特性與設計原則：**
    * **簡潔性與可讀性：** 語法簡潔、關鍵字極少，專注於做好一件事。
    * **並行處理：** 內建對輕量級 goroutine 和 channel 的支援，使並行程式設計更簡單、更高效。
    * **效能：** 編譯語言，具有高效的記憶體管理（垃圾回收），執行速度快。
    * **強型別：** 有助於在開發過程早期發現錯誤。
    * **靜態連結：** 產生自包含的可執行檔，簡化部署。
    * **垃圾回收：** 自動記憶體管理，減輕開發者負擔。
    * **標準庫：** 豐富而全面的標準庫，提供各種任務的工具。
    * **工具鏈：** 優秀的內建工具，用於格式化（gofmt）、代碼檢查（golint、staticcheck）、測試（go test）和依賴管理（go modules）。
* **使用案例：**
    * 系統程式設計
    * 網路程式設計（API、網頁伺服器）
    * 雲端基礎設施（Docker、Kubernetes）
    * 命令列工具
    * 分散式系統
    * 大數據處理

**II. 設定 Go 開發環境**

* **安裝：**
    * 從官方網站（[https://go.dev/dl/](https://go.dev/dl/)）下載適合您作業系統的 Go 發行版。
    * 按照您平台的安裝說明進行操作。
* **驗證安裝：**
    * 開啟終端機或命令提示字元，執行 `go version`。這應該會顯示已安裝的 Go 版本。
* **工作區與 `GOPATH`（舊版）：**
    * 歷史上，Go 專案是在 `GOPATH` 環境變數內組織的。雖然仍受支援，但已大多被 Go Modules 取代。
* **Go Modules（推薦）：**
    * Go Modules 是官方的依賴管理解決方案。
    * 要使用 modules 啟動新專案，請在終端機中導航至您的專案目錄，並執行 `go mod init <your_module_path>`（例如：`go mod init github.com/yourusername/myproject`）。
    * 依賴項在 `go.mod` 檔案中宣告。

**III. 基本 Go 語法與概念**

* **Hello, World!**
    ```go
    package main

    import "fmt"

    func main() {
        fmt.Println("Hello, World!")
    }
    ```
    * `package main`：宣告該套件為可執行程式的進入點。
    * `import "fmt"`：導入 "fmt" 套件，該套件提供格式化 I/O 功能。
    * `func main()`：程式執行開始的 main 函式。
    * `fmt.Println()`：向控制台輸出一行文字。
* **套件與導入：**
    * Go 程式碼組織成套件。
    * 套件有助於程式碼組織、可重用性和避免命名衝突。
    * 使用 `import` 關鍵字從其他套件（標準庫或第三方）引入功能。
    * 導入路徑可以是單一套件（例如 `"fmt"`）或嵌套的（例如 `"net/http"`）。
    * 導入別名：`import f "fmt"`（現在可以使用 `f.Println`）。
    * 用於副作用（side effects）的空白識別符（`_`）：`import _ "net/http/pprof"`（初始化 pprof 處理程序而不直接使用）。
* **變數：**
    * 宣告：
        * `var name type`（例如：`var age int`）
        * `var name = value`（型別推斷，例如：`var name = "Alice"`）
        * `name := value`（短變數宣告，僅在函式內部使用，例如：`count := 0`）
    * 多重宣告：
        ```go
        var (
            firstName string = "John"
            lastName  string = "Doe"
            age       int    = 30
        )
        ```
    * 常數：
        * `const PI float64 = 3.14159`
        * 常數必須在編譯時宣告。
        * 無型別常數可根據其使用情況採用不同的型別。
* **資料型別：**
    * **基本型別：**
        * **整數：** `int`、`int8`、`int16`、`int32`（`rune` - `int32` 的別名）、`int64`、`uint`、`uint8`（`byte` - `uint8` 的別名）、`uint16`、`uint32`、`uint64`、`uintptr`（大到足以容納指標的無號整數）。
        * **浮點數：** `float32`、`float64`。
        * **複數：** `complex64`、`complex128`。
        * **布林值：** `bool`（`true`、`false`）。
        * **字串：** `string`（位元組的不可變序列，通常為 UTF-8 編碼）。
    * **複合型別：**
        * **陣列：** 固定大小的相同型別元素序列（例如：`[5]int`）。
        * **切片：** 動態大小、對陣列元素的靈活視圖（最常用）。
        * **對映：** 無序的鍵值對集合（雜湊表）。
        * **結構：** 將零個或多個不同型別的具名字段組合在一起的複合資料型別。
        * **指標：** 儲存值的記憶體位址。
        * **函式：** 一等公民，可以賦值給變數並作為參數傳遞。
        * **介面：** 定義型別必須實作的一組方法。
        * **通道：** 為 goroutine 提供通訊和同步的方式。
* **運算子：**
    * **算術：** `+`、`-`、`*`、`/`、`%`、`++`、`--`。
    * **比較：** `==`、`!=`、`>`、`<`、`>=`、`<=`。
    * **邏輯：** `&&` (AND)、`||` (OR)、`!` (NOT)。
    * **位元：** `&` (AND)、`|` (OR)、`^` (XOR)、`&^` (AND NOT)、`<<` (左移)、`>>` (右移)。
    * **賦值：** `=`、`+=`、`-=`、`*=`、`/=`、`%=`、`&=`、`|=`、`^=`、`<<=`、`>>=`。
* **控制流程：**
    * **`if`、`else if`、`else`：** 條件執行。
        ```go
        if age >= 18 {
            fmt.Println("Adult")
        } else if age >= 13 {
            fmt.Println("Teenager")
        } else {
            fmt.Println("Child")
        }
        ```
    * **`for` 迴圈：** Go 中唯一的迴圈結構。
        * 基本 `for` 迴圈：
            ```go
            for i := 0; i < 5; i++ {
                fmt.Println(i)
            }
            ```
        * 類似 `while` 的迴圈：
            ```go
            j := 0
            for j < 5 {
                fmt.Println(j)
                j++
            }
            ```
        * 無限迴圈：
            ```go
            for {
                // 執行某些操作
            }
            ```
        * 遍歷集合（`range`）：
            ```go
            numbers := []int{1, 2, 3}
            for index, value := range numbers {
                fmt.Printf("Index: %d, Value: %d\n", index, value)
            }

            m := map[string]string{"a": "apple", "b": "banana"}
            for key, val := range m {
                fmt.Printf("Key: %s, Value: %s\n", key, val)
            }
            ```
    * **`switch` 語句：** 多路條件執行。
        ```go
        grade := "B"
        switch grade {
        case "A":
            fmt.Println("Excellent!")
        case "B":
            fmt.Println("Good")
        case "C":
            fmt.Println("Average")
        default:
            fmt.Println("Needs improvement")
        }
        ```
        * 沒有自動 fallthrough（如果需要，使用 `fallthrough` 關鍵字）。
        * Case 可以有多個值。
        * 無條件的 Switch（類似 `if-else if-else`）。
    * **`defer` 語句：** 安排一個函式呼叫在周圍函式結束時執行（常用於清理任務，如關閉檔案）。
        ```go
        func example() {
            f, err := os.Open("file.txt")
            if err != nil {
                fmt.Println(err)
                return
            }
            defer f.Close() // f.Close() 將在 example() 返回時被呼叫

            // ... 處理檔案 ...
        }
        ```
    * **`goto` 語句：** 將控制轉移到帶標籤的語句（謹慎使用，可能導致程式碼混亂）。
    * **`break` 和 `continue`：** 控制迴圈執行。

**IV. 複合資料型別詳解**

* **陣列：**
    * 固定大小，相同型別的元素。
    * 比切片較少使用。
    * 範例：`var a [3]int; a[0] = 1; a[1] = 2; a[2] = 3` 或 `b := [2]string{"hello", "world"}`。
* **切片：**
    * 動態大小，由底層陣列支援。
    * 使用切片字面值（例如：`[]int{1, 2, 3}`）、`make()` 函式（`make([]int, length, capacity)`）或透過切片現有陣列或切片（`mySlice[start:end]`）建立。
    * `len()`：返回切片中的元素數量。
    * `cap()`：返回底層陣列的容量。
    * `append()`：將元素添加到切片末尾（如果容量已滿，可能會重新分配底層陣列）。
    * `copy()`：將元素從一個切片複製到另一個切片。
* **對映：**
    * 無序的鍵值對集合。
    * 鍵必須是可比較的型別（例如：整數、字串、布林值、僅包含可比較欄位的結構）。
    * 值可以是任何型別。
    * 使用對映字面值（例如：`map[string]int{"apple": 1, "banana": 2}`）或 `make()` 函式（`make(map[string]string)`）建立。
    * 存取值：`value := myMap["key"]`（返回值以及一個指示鍵是否存在的布林值）。
    * 檢查鍵是否存在：`value, ok := myMap["key"]`（如果鍵存在，`ok` 為 `true`）。
    * 新增/更新條目：`myMap["newKey"] = "newValue"`。
    * 刪除條目：`delete(myMap, "keyToDelete")`。
* **結構：**
    * 將不同型別的具名字段組合在一起的使用者定義型別。
    * 用於表示具有多個屬性的實體。
    * 宣告：
        ```go
        type Person struct {
            FirstName string
            LastName  string
            Age       int
        }
        ```
    * 建立實例：
        ```go
        var p1 Person
        p1.FirstName = "Alice"
        p1.LastName = "Smith"
        p1.Age = 25

        p2 := Person{FirstName: "Bob", LastName: "Johnson", Age: 30}

        p3 := Person{"Charlie", "Brown", 20} // 如果省略欄位名稱，順序很重要
        ```
    * 存取欄位：`p1.FirstName`。
    * 嵌入結構（組合）。
    * 匿名欄位。
* **指標：**
    * 儲存值的記憶體位址。
    * 使用 `*` 運算子宣告（例如：`var ptr *int`）。
    * 使用 `&` 運算子取得變數的位址（例如：`ptr = &age`）。
    * 使用 `*` 運算子解參考指標以存取其指向的值（例如：`value := *ptr`）。
    * Go 沒有明確的指標算術。
    * 指標對於透過參考傳遞資料、直接修改值以及處理某些資料結構非常有用。

**V. 函式**

* **函式宣告：**
    ```go
    func functionName(parameterName1 type1, parameterName2 type2) returnType {
        // 函式主體
        return returnValue
    }
    ```
    * 相同型別的多個參數可以一起宣告：`func sum(a, b int) int`。
    * 可變參數函式（接受可變數量的參數）：`func sum(numbers ...int) int`。
    * 多個返回值：
        ```go
        func divide(a, b float64) (float64, error) {
            if b == 0 {
                return 0, fmt.Errorf("division by zero")
            }
            return a / b, nil
        }

        result, err := divide(10, 2)
        if err != nil {
            fmt.Println("Error:", err)
        } else {
            fmt.Println("Result:", result)
        }
        ```
    * 命名返回值。
* **一等函式：**
    * 函式可以賦值給變數、作為參數傳遞給其他函式，以及從函式返回。
    * 範例：
        ```go
        func add(a, b int) int { return a + b }

        func operate(f func(int, int) int, x, y int) int {
            return f(x, y)
        }

        result := operate(add, 5, 3) // result 將為 8
        ```
* **匿名函式（閉包）：**
    * 沒有名稱的函式，通常用作內聯回呼。
    * 可以捕獲其周圍作用域中的變數（閉包）。
    * 範例：
        ```go
        func multiplier(factor int) func(int) int {
            return func(x int) int {
                return x * factor
            }
        }

        double := multiplier(2)
        fmt.Println(double(5)) // 輸出：10
        ```

**VI. 方法**

* **方法宣告：**
    * 方法是與特定接收器型別關聯的函式。
    * 語法：
        ```go
        func (receiver Type) methodName(parameters) returnType {
            // 方法主體
        }
        ```
    * 接收器可以是值或指標。
    * 值接收器操作接收器的副本。
    * 指標接收器操作原始接收器並可以修改其狀態。
* **範例：**
    ```go
    type Circle struct {
        Radius float64
    }

    func (c Circle) Area() float64 {
        return math.Pi * c.Radius * c.Radius
    }

    func (c *Circle) SetRadius(newRadius float64) {
        c.Radius = newRadius
    }

    func main() {
        myCircle := Circle{Radius: 5}
        fmt.Println("Area:", myCircle.Area()) // 在值接收器上呼叫 Area 方法

        myCircle.SetRadius(10) // 在指標接收器上呼叫 SetRadius 方法
        fmt.Println("New Area:", myCircle.Area())
    }
    ```

**VII. 介面**

* **介面定義：**
    * 介面定義一組方法簽章。
    * 如果一個型別為介面中定義的所有方法提供了實作，則該型別實作了該介面。
    * 介面是隱式滿足的（沒有明確的 `implements` 關鍵字）。
    * 語法：
        ```go
        type Writer interface {
            Write(p []byte) (n int, err error)
        }

        type Reader interface {
            Read(p []byte) (n int, err error)
        }

        type ReadWriter interface {
            Reader
            Writer // 嵌入介面
            Close() error
        }
        ```
* **介面使用：**
    * 實現多型（以統一的方式處理不同型別的物件）。
    * 透過針對介面而非具體型別進行程式設計來解耦程式碼。
    * 範例：
        ```go
        import "io"
        import "os"

        func writeData(w io.Writer, data []byte) error {
            _, err := w.Write(data)
            return err
        }

        func main() {
            file, err := os.Create("output.txt")
            if err != nil {
                fmt.Println("Error creating file:", err)
                return
            }
            defer file.Close()

            data :=[]byte("Hello, Go interfaces!\n")
            err = writeData(file, data)
            if err != nil {
                fmt.Println("Error writing to file:", err)
                return
            }

            // 我們也可以使用同樣實作了 io.Writer 的 os.Stdout
            err = writeData(os.Stdout, []byte("Writing to stdout through the interface.\n"))
            if err != nil {
                fmt.Println("Error writing to stdout:", err)
                return
            }
        }
        ```
* **空介面（`interface{}`）：**
    * 空介面沒有任何方法。
    * 所有型別都實作了空介面。
    * 可用於表示任何型別的值，但通常需要型別斷言來存取底層值。
    ```go
    var i interface{}
    i = 42
    fmt.Println(i)
    i = "hello"
    fmt.Println(i)

    value, ok := i.(string) // 型別斷言為 string
    if ok {
        fmt.Println("The value is a string:", value)
    } else {
        fmt.Println("The value is not a string")
    }
    ```
* **型別斷言與型別 Switch：**
    * **型別斷言：** 用於從介面變數中提取底層具體值。
        * 語法：`value, ok := interfaceVar.(ConcreteType)`
        * 如果斷言正確，`value` 將持有具體值，`ok` 將為 `true`。
        * 如果斷言不正確，並且您不檢查 `ok`，將會導致 panic。
    * **型別 Switch：** 用於根據介面變數持有的具體型別執行不同的操作。
        ```go
        func describe(i interface{}) {
            switch v := i.(type) {
            case int:
                fmt.Printf("Twice %v is %v\n", v, v*2)
            case string:
                fmt.Printf("%q is %v bytes long\n", v, len(v))
            default:
                fmt.Printf("I don't know about type %T!\n", v)
            }
        }

        func main() {
            describe(42)
            describe("hello")
            describe(true)
        }
        ```

**VIII. Goroutine 與並行處理**

Go 的並行模型基於 goroutine 和 channel。

* **Goroutine：**
    * 輕量級的並行函式。
    * 使用 `go` 關鍵字後跟函式呼叫來建立。
    * Goroutine 與其他函式和 goroutine 並行執行。
    * 建立和管理的成本遠低於傳統的作業系統執行緒。
    ```go
    package main

    import (
        "fmt"
        "time"
    )

    func say(s string) {
        for i := 0; i < 5; i++ {
            time.Sleep(100 * time.Millisecond)
            fmt.Println(s)
        }
    }

    func main() {
        go say("world") // 啟動一個新的 goroutine
        say("hello")    // 在主 goroutine 中執行

        // 等待一段時間以查看 goroutine 的輸出
        time.Sleep(time.Second)
    }
    ```
* **通道：**
    * 類型化的管道，goroutine 可以透過它發送和接收值。
    * 為並行程式碼提供安全的方式來通訊和同步。
    * 使用 `make(chan Type)` 語法建立。
    * 發送到通道：`channel <- value`
    * 從通道接收：`value := <-channel`
    ```go
    package main

    import "fmt"

    func sum(s []int, c chan int) {
        sum := 0
        for _, v := range s {
            sum += v
        }
        c <- sum // 將 sum 發送到通道
    }

    func main() {
        s := []int{7, 2, 8, -9, 4, 0}

        c := make(chan int)
        go sum(s[:len(s)/2], c) // 在一個 goroutine 中計算前半部分的總和
        go sum(s[len(s)/2:], c) // 在一個 goroutine 中計算後半部分的總和
        x, y := <-c, <-c       // 從通道接收結果

        fmt.Println(x, y, x+y)
    }
    ```
* **緩衝通道：**
    * 具有容量的通道，可以在沒有接收者立即準備好的情況下容納一定數量的值。
    * 使用 `make(chan Type, capacity)` 建立。
    * 僅當緩衝區已滿時，發送到緩衝通道才會阻塞。
    * 僅當緩衝區為空時，接收才會阻塞。
* **通道方向：**
    * 您可以在通道型別中指定資料流的方向：
        * `chan<- int`：僅發送通道（只能發送整數）。
        * `<-chan int`：僅接收通道（只能接收整數）。
    * 對於限制函式中通道的使用方式非常有用。
    ```go
    func sender(out chan<- string) {
        out <- "Hello from sender"
    }

    func receiver(in <-chan string) {
        msg := <-in
        fmt.Println("Received:", msg)
    }

    func main() {
        ch := make(chan string)
        go sender(ch)
        go receiver(ch)
        time.Sleep(time.Second)
    }
    ```
* **`select` 語句：**
    * 允許一個 goroutine 等待多個通訊操作。
    * 阻塞直到其中一個 case 可以進行，然後執行該 case。
    * 如果多個 case 準備就緒，則隨機選擇一個。
    * 可以有一個 `default` case，如果沒有其他 case 準備就緒，則立即執行。
    ```go
    package main

    import (
        "fmt"
        "time"
    )

    func main() {
        c1 := make(chan string)
        c2 := make(chan string)

        go func() {
            time.Sleep(1 * time.Second)
            c1 <- "one"
        }()
        go func() {
            time.Sleep(2 * time.Second)
            c2 <- "two"
        }()

        for i := 0; i < 2; i++ {
            select {
            case msg1 := <-c1:
                fmt.Println("received", msg1)
            case msg2 := <-c2:
                fmt.Println("received", msg2)
            }
        }
    }
    ```
* **同步原語：**
    * **`sync.WaitGroup`：** 等待一組 goroutine 完成。
    * **`sync.Mutex`：** 提供基本的互斥鎖。
    * **`sync.RWMutex`：** 提供讀者/寫者鎖，允許多個讀者或單個寫者。
    * **`sync.Once`：** 確保函式僅執行一次。

**IX. 錯誤處理**

Go 傾向於使用 `error` 介面進行明確的錯誤處理。

* **`error` 介面：**
    * 定義為：`type error interface { Error() string }`
    * 可能失敗的函式通常會返回一個型別為 `error` 的值作為最後一個返回值。
    * `nil` 值表示成功；非 `nil` 的 `error` 值表示失敗。
* **建立錯誤：**
    * 使用 `errors` 套件中的 `errors.New()` 函式建立簡單的錯誤值。
    * 使用 `fmt.Errorf()` 建立格式化的錯誤訊息。
* **處理錯誤：**
    * 在呼叫可能失敗的函式後檢查返回的 `error` 值。
    * 使用 `if err != nil` 來處理錯誤。
    * 您可以使用像 `fmt.Errorf()` 與 `%w` 這樣的函式庫來包裝錯誤以提供更多上下文。
* **自訂錯誤型別：**
    * 您可以透過定義一個實作了 `error` 介面（即具有 `Error() string` 方法）的結構來建立自己的錯誤型別。
    ```go
    package main

    import (
        "errors"
        "fmt"
        "time"
    )

    type TimeoutError struct {
        duration time.Duration
    }

    func (e *TimeoutError) Error() string {
        return fmt.Sprintf("operation timed out after %v", e.duration)
    }

    func performOperation(timeout time.Duration) error {
        time.Sleep(timeout + 1*time.Second) // 模擬長時間操作
        return &TimeoutError{duration: timeout}
    }

    func main() {
        err := performOperation(2 * time.Second)
        if err != nil {
            fmt.Println("Error:", err)
            if te, ok := err.(*TimeoutError); ok {
                fmt.Printf("It was a timeout error of %v\n", te.duration)
            }
        } else {
            fmt.Println("Operation successful")
        }
    }
    ```
* **`panic` 和 `recover`：**
    * `panic` 用於表示程式無法恢復的執行時錯誤。它會停止目前函式的執行並展開堆疊，沿途呼叫任何延遲的函式。
    * `recover` 是一個內建函式，可以重新獲得對發生 panic 的 goroutine 的控制。它應該在延遲函式內呼叫。`recover` 返回傳遞給 `panic` 的值，如果 goroutine 沒有發生 panic，則返回 `nil`。
    * `panic` 和 `recover` 應謹慎使用，主要用於關鍵的、無法恢復的錯誤。對於大多數預期的錯誤，請使用 `error` 介面。
    ```go
    package main

    import "fmt"

    func mightPanic() {
        panic("something went wrong")
    }

    func recoverFunc() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from panic:", r)
        }
    }

    func main() {
        defer recoverFunc()
        fmt.Println("Before mightPanic")
        mightPanic()
        fmt.Println("After mightPanic (this will not be reached)")
    }
    ```

**X. 套件與模組**

Go 程式碼組織成套件。

* **套件：**
    * 同一目錄中一起編譯的原始碼檔案集合。
    * 提供命名空間以避免命名衝突。
    * 套件名稱通常是目錄的名稱。
    * 可執行程式必須有一個帶有 `main` 函式的 `main` 套件。
    * 函式庫可以有任何套件名稱。
* **導入：**
    * 使用 `import` 關鍵字從其他套件引入功能。
    * 標準庫套件透過其短名稱導入（例如：`"fmt"`、`"net/http"`）。
    * 第三方套件通常使用其模組路徑導入（例如：`"github.com/gin-gonic/gin"`）。
    * **導入路徑：**
        * 相對導入（不鼓勵，且在模組內有特定規則）。
        * 絕對導入（推薦），以模組路徑開頭。
    * **導入別名：** 您可以使用別名在本地為套件指定不同的名稱：`import f "fmt"`。
    * **空白識別符（`_`）：** 用於僅為了其副作用（例如：初始化內部狀態）而導入套件：`import _ "net/http/pprof"`。
* **模組（Go 1.11 及更高版本）：**
    * 在 Go 中管理依賴的主要方式。
    * 由專案根目錄下的 `go.mod` 檔案定義。
    * `go.mod` 檔案追蹤模組路徑和專案的依賴項。
    * **`go mod init <module_path>`：** 初始化一個新模組。
    * **`go get <package>@<version>`：** 新增或更新依賴項。
    * **`go build`、`go run`、`go test`：** 自動管理模組依賴項。
    * **`go.sum`：** 包含依賴項的加密雜湊以確保完整性。
* **可見性：**
    * 以大寫字母開頭的識別符（變數、函式、型別等）是導出的（公開的），可以從其他套件存取。
    * 以小寫字母開頭的識別符是未導出的（私有的），只能在同一套件內存取。

**XI. 測試**

Go 內建對測試的支援。

* **測試檔案：**
    * 測試檔案以 `_test.go` 為後綴命名（例如：`myfunction_test.go`）。
    * 它們與被測試的程式碼位於同一套件中。
* **測試函式：**
    * 測試函式的名稱以 `Test` 開頭，並接受一個型別為 `*testing.T` 的參數。
    * 使用 `*testing.T` 上的方法（例如：`t.Log`、`t.Error`、`t.Errorf`、`t.Fatal`、`t.Fatalf`）來報告測試結果。
* **測試範例：**
    ```go
    // myfunction.go
    package mypackage

    func Add(a, b int) int {
        return a + b
    }

    // myfunction_test.go
    package mypackage_test

    import "testing"

    func TestAdd(t *testing.T) {
        result := Add(2, 3)
        expected := 5
        if result != expected {
            t.Errorf("Add(2, 3) returned %d, expected %d", result, expected)
        }
    }
    ```
* **執行測試：**
    * 在包含您的套件的目錄中使用 `go test` 命令。
    * `go test -v`：詳細輸出，顯示每個測試的名稱。
    * `go test ./...`：在目前目錄和所有子目錄中執行測試。
    * `go test -run <pattern>`：僅執行名稱符合給定正規表示式的測試。
* **基準測試：**
    * 測量程式碼的效能。
    * 基準測試函式的名稱以 `Benchmark` 開頭，並接受一個型別為 `*testing.B` 的參數。
    * 使用 `b.N` 迴圈多次執行被基準測試的程式碼。
    ```go
    // myfunction_test.go
    package mypackage_test

    import (
        "testing"
    )

    func BenchmarkAdd(b *testing.B) {
        for i := 0; i < b.N; i++ {
            Add(2, 3)
        }
    }
    ```
    * 使用 `go test -bench=.` 執行基準測試。
* **範例測試：**
    * 在套件文件中提供可執行的範例。
    * 範例函式的名稱以 `Example` 開頭。
    * 它們在測試期間被編譯和執行，並將其輸出與函式內的註解進行比較。

這結束了全面的 Go 程式語言指南。請記住，練習和探索是掌握任何程式語言的關鍵。祝您好運！