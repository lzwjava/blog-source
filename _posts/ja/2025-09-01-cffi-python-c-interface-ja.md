---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: CFFI Python Cインターフェースガイド
translated: true
type: note
---

### CFFIとは？
CFFI（C Foreign Function Interface）は、PythonコードからC関数を呼び出すためのPythonライブラリです。CPythonとPyPyの両方と互換性があり、ctypesのようなライブラリよりも安全で移植性の高い代替手段を提供します。主に2つのモードをサポートしています：ABI（既存の共有ライブラリを呼び出す）とAPI（Cコードをインラインでコンパイルする）。

### インストール方法
pipを使用してCFFIをインストールします：
```bash
pip install cffi
```
CFFIはモジュールをビルドするためにCコンパイラ（例：LinuxではGCC、WindowsではVisual Studio）が必要です。

### 基本的な使用例
以下は、APIモード（新しいコードに推奨）を使用して2つの整数を加算するC関数を呼び出す簡単な使用例のステップバイステップガイドです。

1. **FFIのインポートとセットアップ**：
   ```python
   from cffi import FFI
   ffibuilder = FFI()
   ```

2. **C宣言の定義**：
   文字列でC関数のシグネチャを指定します：
   ```python
   ffibuilder.cdef("""
       int add(int a, int b);
   """)
   ```

3. **Cソースコードの提供**：
   Cの実装を含めます：
   ```python
   ffibuilder.set_source("_example",
       """
       int add(int a, int b) {
           return a + b;
       }
       """)
   ```

4. **モジュールのコンパイル**：
   このスクリプトを一度実行してC拡張をビルドします：
   ```python
   if __name__ == "__main__":
       ffibuilder.compile(verbose=True)
   ```
   これによりコンパイルされたモジュール（例：`_example.cpython-39-x86_64-linux-gnu.so`）が生成されます。

5. **コンパイル済みモジュールの使用**：
   Pythonコードで関数をインポートして呼び出します：
   ```python
   from _example import lib
   result = lib.add(5, 3)
   print(result)  # 出力: 8
   ```

### 主要な概念
- **FFIオブジェクト**: `FFI()`で作成されるメインインターフェース。宣言には`cdef()`を、コードには`set_source()`を使用します。
- **宣言**: Cの型、構造体、関数などをPythonに伝えます。文字列はCの構文と正確に一致する必要があります。
- **型変換**: CFFIは基本型（int、float、ポインタ）を自動的に処理します。配列、構造体、コールバックを使用して複雑な処理を行います。
- **エラーハンドリング**: 無効なC定義に対しては`CDefError`などの例外が発生します。Cランタイムエラー（例：`errno`経由）は`ffi.errno`で確認できます。
- **メモリ管理**: Cの構造体/配列には`ffi.new()`を使用し、適切な解放を行ってメモリリークを回避します。

### モード：ABI vs API
- **ABIモード**（既存ライブラリ用）：共有ライブラリをロード（例：`ffi.dlopen("mylib.so")`）して関数を直接呼び出します。例：
  ```python
  from cffi import FFI
  ffi = FFI()
  ffi.cdef("int add(int a, int b);")
  lib = ffi.dlopen("/path/to/libmylib.so")
  result = lib.add(5, 3)
  ```
  これは事前ビルドされたライブラリに対して高速ですが、移植性が低く、正確なバイナリが必要です。

- **APIモード**（推奨）：上記の例のようにCコードをインラインでコンパイルします。より安全で最適化が効き、クロスプラットフォームで動作します。

### 高度な機能
- **構造体と共用体**: `cdef("struct Point { int x, y; }")`のように複雑な型を定義します。
- **配列とポインタ**: 配列には`ffi.new("int[10]")`を、キャストには`ffi.cast("int*", ptr)`を使用します。
- **コールバック**: `ffi.callback()`を使用してPython関数をCに渡します。
- **パッケージとの統合**: 多くのライブラリ（暗号化、NumPyなど）がパフォーマンス向上のためにCFFIを使用しています。
- **パフォーマンスのヒント**: コンパイルには時間がかかるため、配布にはインプレースビルドやcffiパッケージを使用します。ループ内での重いPython-C遷移は避けてください。

詳細なドキュメントは[公式CFFIドキュメント](https://cffi.readthedocs.io/)を参照してください。これらは基本をカバーしていますので、例を実験して自分のニーズに合わせてください。特定の使用ケースがある場合は、詳細を提供していただければ具体的なアドバイスを提供します。