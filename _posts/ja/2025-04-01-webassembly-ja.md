---
audio: false
generated: true
lang: ja
layout: post
title: WebAssembly
translated: true
type: note
---

WebAssembly（Wasm）に関する包括的なガイドを詳しく見ていきましょう。以下のセクションに分けて説明します：Wasmとは何か、その仕組み、重要性、使用方法、そして今後の展開です。最後まで読めば、WebAssemblyの基本をしっかり理解し、使い始めることができるようになります。

---

### **1. WebAssemblyとは？**
WebAssemblyは、プログラミング言語のためのポータブルで高性能なコンパイルターゲットとして設計されたバイナリ命令フォーマットです。低レベルでアセンブリ言語に似た、コンパクトなバイナリ表現を持ちますが、人間が直接記述することを意図したものではありません。代わりに、C、C++、Rust、Go、さらにはPythonなどの高水準言語からコンパイルによって生成されます。

- **主な特徴:**
  - **パフォーマンス:** ハードウェアの能力を活用することで、ネイティブに近い速度で実行されます。
  - **移植性:** （ブラウザ、サーバー、IoTデバイスなど）プラットフォームを問わず一貫して動作します。
  - **セキュリティ:** サンドボックス環境で動作し、ホストシステムから隔離されます。
  - **相互運用性:** JavaScriptと対立するのではなく、連携して動作します。

- **歴史:**
  - 2015年にMozilla、Google、Microsoft、Appleの協業により導入されました。
  - 2019年にW3C勧告となり、公式のウェブ標準として認定されました。

- **ユースケース:**
  - Webゲーム（例：UnityやUnreal Engineのエクスポート）
  - パフォーマンスがクリティカルなアプリ（例：FigmaなどのビデオエディタやPhotoshopに似たツール）
  - サーバーサイドアプリケーション（例：Node.jsを使用）
  - モダンな環境でのレガシーコードベースの実行

---

### **2. WebAssemblyの仕組み**
WebAssemblyは、高水準コードとマシン実行の間のギャップを埋めます。そのプロセスは以下の通りです：

1. **ソースコード:** C++やRustなどの言語でコードを記述します。
2. **コンパイル:** コンパイラ（例：C/C++用のEmscripten、Rust用の`wasm-pack`）がコードをWebAssemblyのバイナリフォーマット（`.wasm`ファイル）に変換します。
3. **実行:**
   - ブラウザ内では、`.wasm`ファイルが（多くの場合JavaScript経由で）フェッチされ、検証され、ブラウザのWasmランタイムによってマシンコードにコンパイルされます。
   - ランタイムはサンドボックス内でそれを実行し、安全性を確保します。

- **テキストフォーマット (WAT):** WebAssemblyには、人間が読めるテキスト表現（`.wat`）もあり、デバッグや学習に役立ちます。例：
  ```wat
  (module
    (func (export "add") (param i32 i32) (result i32)
      local.get 0
      local.get 1
      i32.add)
  )
  ```
  これは、2つの32ビット整数を受け取り、その和を返す`add`関数を定義しています。

- **メモリモデル:** Wasmは線形メモリモデルを使用します—プログラムが読み書きできるバイトのフラットな配列です。これは手動で、またはソース言語のランタイムを介して管理されます。

- **JavaScriptとの連携:** JavaScriptで`WebAssembly.instantiate()`や`fetch()`を使用してWasmモジュールをロードし、エクスポートされた関数を呼び出します。WasmはJavaScriptをコールバックすることもできます。

---

### **3. WebAssemblyを使用する理由**
- **速度:** プリコンパイルされたバイナリは、インタプリタ形式のJavaScriptよりも高速に実行されます。
- **言語の柔軟性:** JavaScriptに縛られず、C、Rustなどを使用できます。
- **サイズ効率:** `.wasm`ファイルは同等のJavaScriptよりも小さく、ロード時間を短縮します。
- **クロスプラットフォーム:** 一度書けば、どこでも実行—ブラウザ、サーバー、組み込みデバイス。
- **セキュリティ:** サンドボックス化により、悪意のあるコードがホストシステムにアクセスするのを防ぎます。

**トレードオフ:**
- 直接のDOMアクセスは不可（そのためにはJavaScriptが必要です）。
- ツーリングは初心者には複雑な場合があります。
- デバッグはJavaScriptよりも困難です。

---

### **4. WebAssemblyを使ってみよう**
簡単な例を見てみましょう：C関数をWebAssemblyにコンパイルし、ブラウザで実行します。

#### **ステップ 1: ツールのインストール**
- **Emscripten:** C/C++をWebAssemblyにコンパイルするためのツールチェーン。
  - インストール: [Emscriptenのガイド](https://emscripten.org/docs/getting_started/downloads.html)に従ってください（Python、CMakeなどが必要です）。
- **Node.js:** オプション、ブラウザ外でWasmを実行する場合。
- **Webサーバー:** ブラウザは`.wasm`ファイルがHTTP経由で提供されることを要求します（例：`python -m http.server`を使用）。

#### **ステップ 2: コードを書く**
`add.c`ファイルを作成：
```c
int add(int a, int b) {
    return a + b;
}
```

#### **ステップ 3: WebAssemblyにコンパイル**
以下のEmscriptenコマンドを実行：
```bash
emcc add.c -s EXPORTED_FUNCTIONS='["_add"]' -s EXPORT_ES6=1 -s MODULARIZE=1 -o add.js
```
- `add.js`（グルースクリプト）と`add.wasm`（バイナリ）を出力します。

#### **ステップ 4: HTMLで使用**
`index.html`を作成：
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <script type="module">
        import init, { add } from './add.js';
        async function run() {
            await init();
            console.log(add(5, 3)); // 8を出力
        }
        run();
    </script>
</body>
</html>
```

#### **ステップ 5: サーバーで提供してテスト**
- ローカルサーバーを起動：`python -m http.server 8080`
- ブラウザで`http://localhost:8080`を開き、コンソールを確認します。

Rustの場合、`cargo`と`wasm-pack`を使用します—プロセスは同様ですが、ツールチェーンが異なります。

---

### **5. エコシステムとツール**
- **言語:**
  - **C/C++:** Emscripten。
  - **Rust:** `wasm-pack`、`wasm-bindgen`。
  - **Go:** 組み込みのWasmサポート（`GOOS=js GOARCH=wasm`）。
  - **AssemblyScript:** WasmのためのTypeScriptライクなシンタックス。

- **ランタイム:**
  - **ブラウザ:** Chrome、Firefox、Safari、Edge。
  - **Node.js:** `--experimental-wasm-modules`付き。
  - **スタンドアロン:** Wasmtime、Wasmer、WasmEdge。

- **ライブラリ:**
  - **WebGL:** グラフィックス用（例：ゲーム）。
  - **WASI:** 非Webユースケース（ファイルI/Oなど）のためのWebAssembly System Interface。

---

### **6. 高度な機能**
- **スレッド:** SharedArrayBufferによる並列処理をサポート。
- **SIMD:** 数学演算が集中するタスク（例：画像処理）のためのベクトル命令。
- **WASI:** システムコールを追加し、WasmをWeb以外に拡張。
- **動的リンク:** 複数の`.wasm`モジュールをロードし、実行時にリンク。

---

### **7. WebAssemblyの未来**
- **広範な採用:** より多くの言語やフレームワークがWasmサポートを追加しています。
  - **サーバーレスコンピューティング:** Wasmの軽量な性質はエッジコンピューティングに適しています。
  - **標準化:** ガベージコレクションや例外処理などの提案が進行中です。
  - **非Webでの成長:** WASIやWasmerなどのランタイムにより、WasmはIoT、デスクトップアプリなどへ進出しています。

---

### **8. さらに学ぶためのリソース**
- **公式サイト:** [webassembly.org](https://webassembly.org/)
- **MDN ドキュメント:** [MDNでのWebAssembly](https://developer.mozilla.org/ja/docs/WebAssembly)
- **チュートリアル:** 「Rust and WebAssembly」ブック (rustwasm.github.io/book) やEmscriptenドキュメント。
- **Xでの投稿:** Xで#WebAssemblyを検索して、実例や議論を探せます。

---

### **簡単なまとめ**
WebAssemblyは、パフォーマンスと移植性においてゲームチェンジャーです。お気に入りの言語で書き、`.wasm`にコンパイルし、どこでも高速に実行できます。万能薬ではありませんが（JavaScriptは依然としてWebのインタラクティビティを支配しています）、モダンな開発者のツールキットにおける強力なツールです。

特定の例を試してみたい、ユースケースを探求したい、何かトラブルシューティングをしたい場合は、お知らせください！