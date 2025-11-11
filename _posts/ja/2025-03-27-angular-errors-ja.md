---
audio: false
generated: true
lang: ja
layout: post
title: Angularエラー
translated: true
type: note
---

Angularでの開発において、開発者は特定の例外やエラーに頻繁に遭遇します。以下は、一般的な問題とその原因、解決策を分類したリストです：

---

### **テンプレート & データバインディングエラー**
1. **`ExpressionChangedAfterItHasBeenCheckedError`**  
   - **原因**: Angularの変更検知サイクル後のコンポーネントデータ変更（例: `ngAfterViewInit` や `ngOnChanges` 内での変更）  
   - **修正**: `ChangeDetectorRef.detectChanges()` を使用するか、データ変更が変更検知終了前に完了するようにする

2. **`Cannot read property 'X' of undefined`**  
   - **原因**: テンプレート内で未初期化のオブジェクトプロパティへのアクセス（例: `user` が `null` 時の `{{ user.name }}`）  
   - **修正**: セーフナビゲーション演算子（`{{ user?.name }}`）を使用するか、オブジェクトを適切に初期化する

3. **`Can't bind to 'X' since it isn't a known property of 'Y'`**  
   - **原因**: コンポーネント/ディレクティブの宣言不足、またはプロパティ名のタイポ  
   - **修正**: ディレクティブ/コンポーネントをモジュールにインポートするか、タイポを確認する

---

### **依存性の注入（DI）エラー**
4. **`NullInjectorError: No provider for XService`**  
   - **原因**: サービスがモジュール/コンポーネントに提供されていない、または循環依存  
   - **修正**: サービスをモジュール/コンポーネントの `providers` 配列に追加する

5. **`No value accessor for form control`**  
   - **原因**: カスタムフォームコントロールに `ControlValueAccessor` の実装がない、または不正な `formControlName` バインディング  
   - **修正**: カスタムコントロールに `ControlValueAccessor` を実装するか、フォームバインディングを確認する

---

### **TypeScript & ビルドエラー**
6. **`Type 'X' is not assignable to type 'Y'`**  
   - **原因**: 型の不一致（例: コンポーネントへの不正なデータ型の受け渡し）  
   - **修正**: 型の整合性を確保するか、（意図的な場合）型アサーションを使用する

7. **`ERROR in Cannot find module 'X'`**  
   - **原因**: npmパッケージの不足、または不正なインポートパス  
   - **修正**: パッケージをインストール（`npm install X`）するか、インポートパスを修正する

---

### **コンポーネント & モジュールエラー**
8. **`Component is not part of any NgModule`**  
   - **原因**: コンポーネントがモジュールに宣言されていない、またはモジュールがインポートされていない  
   - **修正**: コンポーネントをモジュールの `declarations` に追加するか、モジュールをインポートする

9. **`ViewDestroyedError: Attempt to use a destroyed view`**  
   - **原因**: コンポーネント破棄後のサブスクリプションや非同期処理の実行  
   - **修正**: `ngOnDestroy` 内でアンサブスクライブするか、`async` パイプを使用する

---

### **HTTP & APIエラー**
10. **`HttpClient provider not found`**  
    - **原因**: モジュールでの `HttpClientModule` インポート不足  
    - **修正**: `AppModule` で `HttpClientModule` をインポートする

11. **CORS問題**  
    - **原因**: バックエンドがフロントエンドオリジンからのリクエストを許可していない  
    - **修正**: サーバーでCORSを設定するか、Angularでプロキシを使用する（`proxy.conf.json`）

---

### **ルーティングエラー**
12. **`Route not found`**  
    - **原因**: 不正なルート定義、または遅延ロードモジュールの不足  
    - **修正**: ルートパスと遅延ロード構文（`loadChildren: () => import(...)`）を確認する

---

### **フォームエラー**
13. **`FormControl not found`**  
    - **原因**: `[formGroup]` でのラップなしでの `formControlName` 使用  
    - **修正**: 親フォームグループが初期化され、バインドされていることを確認する

---

### **その他**
14. **`Maximum call stack size exceeded`**  
    - **原因**: 再帰関数または循環依存  
    - **修正**: 再帰/循環参照を排除するようにコードをリファクタリングする

15. **`Zone.js Promise rejection`**  
    - **原因**: 未処理のPromise拒否  
    - **修正**: `.catch()` を追加するか、`async/await` で `try/catch` を使用する

16. **AOTコンパイルエラー**  
    - **原因**: Ahead-of-Timeコンパイルと互換性のないテンプレート構文  
    - **修正**: テンプレート内の複雑な式を避けるか、Angular互換構文を使用する

---

### **エラー回避のためのベストプラクティス**
- オブザーバブルには `async` パイプを使用して自動アンサブスクライブを実現
- 厳格なTypeScriptチェックを有効化（`tsconfig.json` で `strict: true`）
- `ng lint` を実行してコード品質の問題を検出
- `--prod` フラグでAOTビルドをシミュレートしてテスト

これらの一般的な問題に体系的に対処することで、Angular開発を効率化し、デバッグ時間を削減できます。