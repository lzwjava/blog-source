---
audio: false
generated: true
lang: ja
layout: post
title: Squirrel SQL クライアントへの Oracle JDBC ドライバの追加
translated: true
type: note
---

Oracle JDBC ドライバを Squirrel SQL Client に追加するには、以下の詳細な手順に従ってください。このプロセスでは、ドライバの設定と Oracle データベースへの接続エイリアスの設定を行います。

### ステップ 1: 必要なファイルの場所を確認
Oracle JDBC ドライバファイル、具体的には `ojdbc.jar` が必要です。このファイルには、Squirrel SQL Client が Oracle データベースに接続するために必要なクラスが含まれています。このファイル（例: Oracle のウェブサイトまたはデータベース管理者から入手）をダウンロードし、システム上の保存場所を把握していることを確認してください。

### ステップ 2: Squirrel SQL Client を起動
お使いのコンピュータで Squirrel SQL Client アプリケーションを開きます。

### ステップ 3: ドライバータブにアクセス
Squirrel SQL Client インターフェースの左側にある **Drivers** タブを見つけてクリックします。このセクションでは、アプリケーションで利用可能な JDBC ドライバを管理できます。

### ステップ 4: 新しいドライバを追加
- Drivers タブで、**"+"** ボタンをクリックして "Add Driver" ダイアログボックスを開きます。

### ステップ 5: ドライバに名前を付ける
- "Add Driver" ダイアログの "Name" フィールドに、**Oracle Thin Driver** と入力します。これは Squirrel SQL Client 内で Oracle ドライバを識別するための説明的な名前です。

### ステップ 6: `ojdbc.jar` ファイルを追加
- "Add Driver" ダイアログ内で **Extra Class Path** タブに切り替えます。
- **Add** ボタンをクリックします。
- システム上の `ojdbc.jar` ファイルの場所に移動し、選択して、ドライバのクラスパスに追加することを確定します。

### ステップ 7: Java ドライバクラスを指定
- "Class Name" フィールドに、Java ドライバクラス **oracle.jdbc.OracleDriver** を入力します。これにより、Squirrel SQL Client は `ojdbc.jar` ファイル内のどのクラスを使用して Oracle データベース接続を処理するかを認識します。

### ステップ 8: 接続URLの例を入力
- オプションで、Oracle データベースに接続するための接続URLフォーマットの例を指定できます：
  - **SID 経由で接続する場合**: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **サービス名経由で接続する場合**: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- `HOST`、`PORT`、`DB` は、後で（エイリアス設定時に）実際の値に置き換えてください。

### ステップ 9: ドライバ設定を保存
- **OK** をクリックしてドライバ設定を保存し、"Add Driver" ダイアログを閉じます。"Oracle Thin Driver" が Drivers タブに緑色のチェックマークとともに表示され、正しく設定されたことを示します。

### ステップ 10: データベースのエイリアスを作成
- Squirrel SQL Client の左側にある **Aliases** タブに切り替えます。
- **"+"** ボタンをクリックして "Add Alias" ダイアログボックスを開きます。

### ステップ 11: エイリアスを設定
- "Add Alias" ダイアログで：
  - **Name**: この接続の名前を入力します（例: "My Oracle DB"）。
  - **Driver**: ドロップダウンメニューから **Oracle Thin Driver** を選択します。
  - **URL**: 特定の Oracle データベースへの接続 URL を入力します：
    - SID 経由: `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - サービス名経由: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - `HOST`（例: localhost または IP アドレス）、`PORT`（デフォルトは 1521）、`DB`（SID またはサービス名）をデータベースの詳細に置き換えます。
  - **Username**: データベースのユーザー名を入力します。
  - **Password**: データベースのパスワードを入力します。

### ステップ 12: 接続をテスト
- "Add Alias" ダイアログの **Test** ボタンをクリックし、Squirrel SQL Client が提供された詳細情報を使用して Oracle データベースに接続できることを確認します。成功すると、確認メッセージが表示されます。

### ステップ 13: エイリアスを保存
- テスト接続が成功したら、**OK** をクリックしてエイリアスを保存します。新しいエイリアスが Aliases タブに表示されます。

### ステップ 14: データベースに接続
- Aliases タブで、新しく作成したエイリアス（例: "My Oracle DB"）を選択します。
- **Connect** ボタンをクリックして Oracle データベースへの接続を確立します。接続されると、Squirrel SQL Client を使用してデータベースのクエリを開始できます。

### 主要情報のまとめ
- **必要なファイル**: `ojdbc.jar`
- **Java ドライバクラス**: `oracle.jdbc.OracleDriver`
- **URL フォーマット**:
  - SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - サービス名: `jdbc:oracle:thin:@//HOST[:PORT]/DB`

これらの手順に従うことで、Squirrel SQL Client に Oracle JDBC ドライバを正常に追加し、Oracle データベースへの接続を設定できます。接続の問題を避けるために、すべての詳細情報（ファイルパス、URL、認証情報）が正確であることを確認してください。