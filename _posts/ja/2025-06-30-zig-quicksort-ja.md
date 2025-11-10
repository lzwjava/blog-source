---
audio: false
generated: true
lang: ja
layout: post
title: Zigクイックソート実装
translated: true
type: note
---

以下はZigでの同等のクイックソート実装です。

```zig
const std = @import("std");

// クイックソート関数
fn quickSort(arr: []i32) void {
    if (arr.len <= 1) {
        return;
    }

    const pivot_index = partition(arr);

    // 配列を左パーティションと右パーティションに分割
    // 注意: Zigのスライス分割はRustとは若干異なります
    // ピボット要素を注意深く扱う必要があります
    var left_slice = arr[0..pivot_index];
    var right_slice = arr[pivot_index + 1 .. arr.len]; // 右スライスからピボットを除外

    quickSort(left_slice);
    quickSort(right_slice);
}

// パーティション関数
fn partition(arr: []i32) usize {
    const len = arr.len;
    // シンプルにするため、Rustの例と同様に最後の要素をピボットとして使用します。
    // プロダクションクイックソートでは、より良い平均ケース性能のためにランダムピボットや中央値を使用することがあります。
    const pivot = arr[len - 1];
    var i: usize = 0; // より小さい要素のインデックス

    for (0..(len - 1)) |j| {
        if (arr[j] <= pivot) {
            std.mem.swap(i32, &arr[i], &arr[j]);
            i += 1;
        }
    }

    // ピボットを正しい位置に配置
    std.mem.swap(i32, &arr[i], &arr[len - 1]);

    return i;
}

pub fn main() !void {
    var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };

    // クイックソート関数用に配列から可変スライスを作成
    var slice: []i32 = &arr;

    std.debug.print("Before: {any}\n", .{slice});

    quickSort(slice);

    std.debug.print("After: {any}\n", .{slice});
}

```

### 変更点とZigの概念の説明:

1.  **`const std = @import("std");`**: この行はZig標準ライブラリをインポートします。これにより、`std.debug.print`（出力用）や`std.mem.swap`（要素の交換用）などの便利なユーティリティが提供されます。
2.  **`fn quickSort(arr: []i32) void`**:
      * `fn`は関数を宣言します。
      * `arr: []i32`は`arr`を`i32`（32ビット整数）のスライスとして宣言します。Zigでは、`[]T`は型`T`の可変スライスを表します。Rustのような別個の`&mut`はなく、スライスを保持する変数が可変かどうかによって可変性が暗示されます。
      * `void`は関数が値を返さないことを示します。
3.  **`if (arr.len <= 1)`**: 条件文では条件を括弧で囲みます。
4.  **`const pivot_index = partition(arr);`**: `const`は不変変数に使用されます。
5.  **Zigでのスライス分割**:
      * `var left_slice = arr[0..pivot_index];`
      * `var right_slice = arr[pivot_index + 1 .. arr.len];`
      * Rustの`split_at_mut`（重複しない2つの可変スライスを作成）とは異なり、Zigのスライシング`arr[start..end]`は元の配列への新しいスライス（ビュー）を作成します。
      * 重要な点として、再帰呼び出しでは、ピボットが`partition`の後に最終的なソート位置にあるため、左右のサブ配列の両方からピボットを*除外しなければなりません*。Rustコードでは、`right[1..]`が`right`スライスの最初の要素（ピボット）を実質的にスキップすることでこれを実現しています。私たちは`right_slice`の開始位置に`pivot_index + 1`を使用することでこれを再現しています。
6.  **`std.mem.swap(i32, &arr[i], &arr[j]);`**:
      * `std.mem.swap`は要素の交換に使用されます。
      * 最初の引数（`i32`）は交換される要素の型です。
      * 後続の引数は交換されるメモリ位置へのポインタです（`&arr[i]`と`&arr[j]`）。
7.  **`for (0..(len - 1)) |j| { ... }`**: これは`0`から`len - 1`まで（`len - 1`を含まずに）反復する`for`ループです。ループ変数は`j`としてキャプチャされます。
8.  **`pub fn main() !void { ... }`**:
      * `pub`は`main`関数を公開アクセス可能にします。
      * `!void`は関数がエラーを返す可能性があることを示しますが、この場合は明示的にエラーを処理していません。シンプルなプログラムでは`void`で十分ですが、Zigでは堅牢なエラー処理を奨励するため`!void`がよく見られます。
9.  **`var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };`**:
      * `[_]i32`は`i32`の固定サイズ配列を宣言します。`_`はコンパイラに初期化リストからサイズを推論するように指示します。
10. **`var slice: []i32 = &arr;`**: `quickSort`がスライスを期待するため、固定サイズ配列`arr`から可変スライス（`[]i32`）を作成します。
11. **`std.debug.print("Before: {any}\n", .{slice});`**:
      * `std.debug.print`はデバッグ出力用のZigの`println!`に相当します。
      * `{any}`は、値を人間が読み取り可能なデバッグフレンドリーな形式で出力するようにZigに指示するフォーマット指定子です。
      * `.{slice}`はフォーマット文字列に引数を渡すために使用される「構造体リテラル」（匿名構造体）です。

このZigコードをコンパイルして実行するには:

1.  `quick_sort.zig`として保存します。
2.  同じディレクトリでターミナルを開きます。
3.  `zig run quick_sort.zig`を実行します。