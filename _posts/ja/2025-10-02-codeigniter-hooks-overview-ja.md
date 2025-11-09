---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniterフックの概要
translated: true
type: note
---

### CodeIgniterのフックとは？

CodeIgniterのフックは、フレームワークのコアファイルを変更することなく機能を拡張する方法です。コントローラの読み込み前後、出力の上書き、キャッシュ処理など、実行サイクルの特定のポイントでカスタムコードを実行できます。これにより、公式コードベースから独自のコードを分離し、アップグレード可能性を維持できます。

フックは `application/config/hooks.php` で定義され、`application/config/config.php` で `$config['enable_hooks'] = TRUE;` を設定することで有効になります。

### フックの有効化

1. `application/config/config.php` を開きます
2. 設定変数を設定します：
   ```php
   $config['enable_hooks'] = TRUE;
   ```
   これにより、CodeIgniterはフックファイルをチェックして実行するようになります

### フックの定義

フックは `application/config/hooks.php` で配列の配列として設定されます。各フック配列は以下を指定します：
- `class`: （必須）クラス名（ファイル名と一致する必要があります）
- `function`: （必須）クラス内のメソッド名
- `filename`: （必須）クラスのファイル名（.phpなし）
- `filepath`: （オプション）ファイルへのフォルダパス、デフォルトは `application/hooks/`
- `params`: （オプション）メソッドに渡すパラメータの配列

フッククラスは `application/hooks/` に配置してください

### フックポイント

CodeIgniterは以下の定義済みポイントでフックを実行できます：
- **pre_system**: システムが読み込まれる前に実行（他の何も実行されていない状態）
- **pre_controller**: コントローラが呼び出される直前に実行
- **post_controller_constructor**: コントローラがインスタンス化された後、メソッドが実行される前に実行
- **post_controller**: コントローラの処理終了後に実行
- **display_override**: ブラウザへの出力の代わりに実行（_display create/exit controller fileを上書き）
- **cache_override**: キャッシュの読み込みの代わりに実行（_display the cacheを上書き）
- **post_system**: Webページが完全にブラウザに送信された後に実行

### 使用例

コントローラ実行前にすべてのリクエストをログに記録したい場合、`pre_controller` 用のフックを作成します

1. `application/hooks/my_hook.php` ファイルを作成：
   ```php
   <?php
   class My_hook {
       public function log_request() {
           // 例：ファイルやデータベースにログを記録
           log_message('info', 'Controller about to be called: ' . $this->uri->uri_string());
       }
   }
   ```

2. `application/config/hooks.php` に追加：
   ```php
   $hook['pre_controller'] = array(
       'class' => 'My_hook',
       'function' => 'log_request',
       'filename' => 'my_hook.php',
       'filepath' => 'hooks', // オプション、デフォルトは application/hooks/
       'params' => array() // オプションのパラメータ
   );
   ```

これで、コントローラが実行される直前に毎回 `log_request` が実行されます

### ベストプラクティス
- フックは控えめに使用し、可能であればコントローラの拡張やライブラリの使用を検討してください
- フックがコアロジックに干渉しないことを確認するため、必ず開発環境でテストしてください
- 詳細については、公式CodeIgniterユーザーガイドのフックの項目を参照してください