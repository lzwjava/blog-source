---
audio: false
generated: true
lang: hant
layout: post
title: Zig 快速排序實現
translated: true
type: note
---

以下是 Zig 的等效快速排序實作。

```zig
const std = @import("std");

// 快速排序函數
fn quickSort(arr: []i32) void {
    if (arr.len <= 1) {
        return;
    }

    const pivot_index = partition(arr);

    // 將陣列分割為左右分區
    // 注意：Zig 的切片分割方式與 Rust 略有不同
    // 我們需要小心處理樞軸元素
    var left_slice = arr[0..pivot_index];
    var right_slice = arr[pivot_index + 1 .. arr.len]; // 從右切片中排除樞軸

    quickSort(left_slice);
    quickSort(right_slice);
}

// 分割函數
fn partition(arr: []i32) usize {
    const len = arr.len;
    // 為簡化起見，我們將使用最後一個元素作為樞軸，類似於 Rust 範例。
    // 在生產環境的快速排序中，您可能會選擇隨機樞軸或三數中值以獲得更好的平均效能。
    const pivot = arr[len - 1];
    var i: usize = 0; // 較小元素的索引

    for (0..(len - 1)) |j| {
        if (arr[j] <= pivot) {
            std.mem.swap(i32, &arr[i], &arr[j]);
            i += 1;
        }
    }

    // 將樞軸放置到正確位置
    std.mem.swap(i32, &arr[i], &arr[len - 1]);

    return i;
}

pub fn main() !void {
    var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };

    // 從陣列建立可變切片以供快速排序函數使用
    var slice: []i32 = &arr;

    std.debug.print("排序前: {any}\n", .{slice});

    quickSort(slice);

    std.debug.print("排序後: {any}\n", .{slice});
}

```

### 變更說明與 Zig 概念解析：

1.  **`const std = @import("std");`**：此行匯入 Zig 標準函式庫，提供實用工具如 `std.debug.print` 用於列印及 `std.mem.swap` 用於交換元素。
2.  **`fn quickSort(arr: []i32) void`**：
      * `fn` 宣告函數。
      * `arr: []i32` 將 `arr` 宣告為 `i32`（32 位元整數）的可變切片。在 Zig 中，`[]T` 表示型別 `T` 的可變切片。與 Rust 不同，沒有獨立的 `&mut`；可變性由持有切片的變數是否可變來暗示。
      * `void` 表示函數不傳回值。
3.  **`if (arr.len <= 1)`**：條件語句在條件周圍使用括號。
4.  **`const pivot_index = partition(arr);`**：`const` 用於不可變變數。
5.  **Zig 中的切片分割**：
      * `var left_slice = arr[0..pivot_index];`
      * `var right_slice = arr[pivot_index + 1 .. arr.len];`
      * 與 Rust 的 `split_at_mut`（建立兩個不重疊的可變切片）不同，Zig 的切片操作 `arr[start..end]` 會建立指向原始陣列的新切片（視圖）。
      * 關鍵在於，在遞迴呼叫中，我們*必須*從左右子陣列中排除樞軸，因為在 `partition` 後，樞軸已處於其最終排序位置。在 Rust 程式碼中，`right[1..]` 透過跳過 `right` 切片的第一個元素（即樞軸）來實現這一點。我們透過對 `right_slice` 的起始位置使用 `pivot_index + 1` 來複現此行為。
6.  **`std.mem.swap(i32, &arr[i], &arr[j]);`**：
      * `std.mem.swap` 用於交換元素。
      * 第一個參數（`i32`）是要交換元素的型別。
      * 後續參數是指向要交換的記憶體位置的指標（`&arr[i]` 和 `&arr[j]`）。
7.  **`for (0..(len - 1)) |j| { ... }`**：這是一個 `for` 迴圈，從 `0` 迭代到（但不包括）`len - 1`。迴圈變數被捕獲為 `j`。
8.  **`pub fn main() !void { ... }`**：
      * `pub` 使 `main` 函數可公開存取。
      * `!void` 表示函數可能傳回錯誤，但在本例中我們未明確處理任何錯誤。對於簡單程式，`void` 即可，但在 Zig 中常見到 `!void`，因為它鼓勵穩健的錯誤處理。
9.  **`var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };`**：
      * `[_]i32` 宣告一個固定大小的 `i32` 陣列。`_` 告訴編譯器從初始化列表推斷大小。
10. **`var slice: []i32 = &arr;`**：我們從固定大小陣列 `arr` 建立一個可變切片（`[]i32`），因為 `quickSort` 預期接收切片。
11. **`std.debug.print("排序前: {any}\n", .{slice});`**：
      * `std.debug.print` 是 Zig 中用於除錯輸出的等效於 `println!` 的函數。
      * `{any}` 是一個格式指定符，告訴 Zig 以人類可讀、除錯友好的格式列印值。
      * `.{slice}` 是一個「結構字面值」（匿名結構），用於將參數傳遞給格式字串。

要編譯並執行此 Zig 程式碼：

1.  將其儲存為 `quick_sort.zig`。
2.  在相同目錄中開啟終端機。
3.  執行：`zig run quick_sort.zig`