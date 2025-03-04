---
audio: false
generated: true
lang: ja
layout: post
title: iOSアプリをApp Storeに公開する
translated: true
---

Apple Developer Program を使用して iOS アプリをアップロードするには、個人用または企業用に関係なく、プログラムに登録し、アプリを準備・パッケージ化し、アップロードし、更新を管理する必要があります。以下は、あなたの質問のすべての側面に対するステップバイステップのガイドです。企業用の場合の Dun & Bradstreet (D-U-N-S) 番号の要件、アプリのパッケージ化、アーカイブのアップロード、Apple のサイトを通じたアプリの更新についても含まれています。

---

### 1. Apple Developer Program に登録する

#### 個人用（個人用）
- **Apple ID を作成する**:
  Apple ID がなければ、[appleid.apple.com](https://appleid.apple.com) にアクセスして個人用のメールアドレスを使用してサインアップします。
- **プログラムに登録する**:
  - [developer.apple.com/programs/](https://developer.apple.com/programs/) にアクセスし、「登録」をクリックします。
  - Apple ID でサインインします。
  - 条件に同意し、個人の法的な名前と住所を提供し、年額 $99 USD の料金を支払います。
- **注意点**: あなたの個人名が App Store の販売者として表示されます。

#### 企業用（組織用）
- **D-U-N-S 番号を取得する**:
  - D-U-N-S 番号は、Dun & Bradstreet によって割り当てられる一意の 9 桁の識別子で、組織の法的実体の状態を確認するために Apple が要求します。
  - [dnb.com](https://www.dnb.com) で組織がすでに持っているかどうかを確認します。持っていない場合は、ウェブサイトから無料でリクエストし、処理には最大 2 周間かかります。
- **プログラムに登録する**:
  - 組織に関連付けられた Apple ID（例：ビジネス用のメール）を使用します。
  - [developer.apple.com/programs/](https://developer.apple.com/programs/) にアクセスし、「登録」をクリックします。
  - 「組織」を選択し、以下を提供します：
    - 法的実体名
    - 本社の住所
    - D-U-N-S 番号
  - 登録する人は、組織の代表として Apple の条件に同意する法的権限を持つ必要があります。
  - 年額 $99 USD の料金を支払います。
- **注意点**: あなたの組織の名前が App Store の販売者として表示されます。

---

### 2. アプリの準備とパッケージ化
- **Xcode でアプリを開発する**:
  - Apple の公式開発ツールである Xcode を使用して iOS アプリを構築します。
  - [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) を満たすようにします。
  - プロジェクト設定でデプロイターゲットを設定し、アプリのバージョンとビルド番号を更新します。
- **アプリをアーカイブする**:
  - Xcode でプロジェクトを開きます。
  - ビルドターゲットとして「Generic iOS Device」（またはシミュレーター）を選択します。
  - メニューバーから **Product** > **Archive** を選択します。
  - Xcode はアプリをコンパイルし、コード、リソース、署名情報を含む配布用のアーカイブを作成します。

---

### 3. アプリのアーカイブをアップロードする
- **Xcode を使用する**:
  - アーカイブ後、Xcode で自動的に Organizer ウィンドウが開きます。
  - アーカイブを選択し、**Distribute App** をクリックします。
  - 配布方法として **App Store Connect** を選択します。
  - プロンプトに従ってアーカイブを App Store Connect に検証し、アップロードします。
- **Transporter を使用する（代替手段）**:
  - [Transporter アプリ](https://apps.apple.com/us/app/transporter/id1450874784) を Mac App Store からダウンロードします。
  - Apple ID でサインインします。
  - Xcode からエクスポートされた `.ipa` ファイルとしてアーカイブされたアプリファイルを追加し、App Store Connect にアップロードします。
  - このオプションは、高度なユーザーや一括アップロードに便利です。

---

### 4. Apple のサイトを使用してアプリを更新する（App Store Connect）
- **App Store Connect にアクセスする**:
  - [appstoreconnect.apple.com](https://appstoreconnect.apple.com) にアクセスし、Apple ID でログインします。
- **アプリを管理する**:
  - ダッシュボードからアプリを選択します。
  - **App Store** タブに移動します。
  - メタデータ（例：アプリの説明、スクリーンショット、キーワード）を更新します。
  - 「Versions」の下で、アップロードした新しいビルドを選択します。
- **レビューに提出する**:
  - **Submit for Review** をクリックして、更新を Apple のレビューチームに送信します。
  - 承認後、手動でリリースするか、自動リリースをスケジュールできます。

---

### 追加の注意事項
- **企業固有の詳細**:
  - D-U-N-S 番号と組織情報が正確であることを確認し、登録の遅延を避けます。
  - App Store Connect を通じて、チームメンバー（例：開発者、テスター）をアカウントに招待し、「Developer」や「Admin」などの役割を割り当てることができます。
- **一般的な課題とヒント**:
  - **コード署名の問題**: Xcode の **Signing & Capabilities** で証明書とプロビジョニングプロファイルを確認します。確信がない場合は、「署名を自動的に管理」オプションを使用します。
  - **アプリレビューの拒否**: Apple のガイドラインに準拠し、遅延を避けるためにアプリを徹底的にテストします。
  - **D-U-N-S の遅延**: 企業の場合は、D-U-N-S 番号を早めに申請してください。これは登録の前提条件です。

---

これらの手順を実行することで、個人用または企業用として Apple Developer Program を使用して iOS アプリをアップロードし、更新することができます。さらに詳しい情報については、Apple の公式ドキュメントを参照してください [developer.apple.com](https://developer.apple.com)。