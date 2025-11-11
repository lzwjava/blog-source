---
audio: false
generated: true
lang: ja
layout: post
title: App StoreへのiOSアプリ公開
translated: true
type: note
---

Apple Developer Program を使用して iOS アプリをアップロードするには、個人利用か法人利用かを問わず、プログラムに登録し、アプリを準備してパッケージ化し、アップロードし、アップデートを管理する必要があります。以下では、法人利用における Dun & Bradstreet (D-U-N-S) 番号の要件、アプリのパッケージ化、アーカイブのアップロード、Apple のサイト経由でのアプリ更新など、お問い合わせのすべての側面に対応するステップバイステップのガイドを提供します。

---

### 1. Apple Developer Program への登録

#### 個人の場合 (個人利用)
- **Apple ID の作成**:
  お持ちでない場合は、[appleid.apple.com](https://appleid.apple.com) にアクセスし、個人のメールアドレスを使用してサインアップしてください。
- **プログラムへの登録**:
  - [developer.apple.com/programs/](https://developer.apple.com/programs/) にアクセスし、「Enroll」をクリックします。
  - Apple ID でサインインします。
  - 利用規約に同意し、個人の法的氏名と住所を提供し、年間費用 99 米ドルを支払います。
- **重要な注意点**: App Store 上の販売者名として個人名が表示されます。

#### 法人の場合 (組織での利用)
- **D-U-N-S 番号の取得**:
  - D-U-N-S 番号は、Dun & Bradstreet によって割り当てられ、組織の法的実体ステータスを確認するための固有の 9 桁の識別子です。Apple は法人アカウントにこれを要求します。
  - お持ちの組織が既に番号を持っているかどうかは [dnb.com](https://www.dnb.com) で確認してください。ない場合は、同サイトから無料でリクエストできます。処理には最大 2 週間かかる場合があります。
- **プログラムへの登録**:
  - 組織に関連付けられた Apple ID (例: ビジネスメール) を使用します。
  - [developer.apple.com/programs/](https://developer.apple.com/programs/) にアクセスし、「Enroll」をクリックします。
  - 「Organization」を選択し、以下を提供します:
    - 法的実体名
    - 本社住所
    - D-U-N-S 番号
  - 登録を行う人物は、組織に代わって Apple の利用規約に同意する法的権限を持っている必要があります。
  - 年間費用 99 米ドルを支払います。
- **重要な注意点**: App Store 上の販売者名として組織名が表示されます。

---

### 2. アプリの準備とパッケージ化
- **Xcode でのアプリ開発**:
  - Apple の公式開発ツールである Xcode を使用して iOS アプリをビルドします。
  - [App Store レビューガイドライン](https://developer.apple.com/app-store/review/guidelines/) を満たしていることを確認してください。
  - プロジェクト設定で、デプロイメントターゲットを設定し、アプリのバージョンとビルド番号を更新します。
- **アプリのアーカイブ**:
  - Xcode でプロジェクトを開きます。
  - ビルドターゲットとして「Generic iOS Device」(または任意のシミュレータ) を選択します。
  - メニューバーから **Product** > **Archive** に移動します。
  - Xcode はアプリをコンパイルし、コード、リソース、署名情報を含む配布準備が整ったパッケージ版であるアーカイブを作成します。

---

### 3. アプリアーカイブのアップロード
- **Xcode を使用する場合**:
  - アーカイブ後、Xcode で Organizer ウィンドウが自動的に開きます。
  - アーカイブを選択し、**Distribute App** をクリックします。
  - 配布方法として **App Store Connect** を選択します。
  - 表示されるプロンプトに従って、アーカイブを検証し、App Store Connect にアップロードします。
- **Transporter を使用する場合 (代替手段)**:
  - Mac App Store から [Transporter アプリ](https://apps.apple.com/us/app/transporter/id1450874784) をダウンロードします。
  - Apple ID でサインインします。
  - アーカイブされたアプリファイル (Xcode から `.ipa` ファイルとしてエクスポートされたもの) を追加し、App Store Connect にアップロードします。
  - このオプションは、上級ユーザーや一括アップロードに便利です。

---

### 4. Apple のサイト (App Store Connect) を使用したアプリの更新
- **App Store Connect へのアクセス**:
  - [appstoreconnect.apple.com](https://appstoreconnect.apple.com) にアクセスし、Apple ID でログインします。
- **アプリの管理**:
  - ダッシュボードからアプリを選択します。
  - **App Store** タブに移動します。
  - メタデータ (アプリの説明、スクリーンショット、キーワードなど) を更新します。
  - 「Versions」で、アップロードした新しいビルドを選択します。
- **レビュー申請**:
  - **Submit for Review** をクリックして、アップデートを Apple のレビューチームに送信します。
  - 承認後、手動でリリースするか、自動リリースをスケジュールできます。

---

### 追加の注意点
- **法人固有の詳細**:
  - 登録の遅延を避けるため、D-U-N-S 番号と組織情報が正確であることを確認してください。
  - App Store Connect 経由でチームメンバー (開発者、テスターなど) をアカウントに招待し、「Developer」や「Admin」などの役割を割り当てることができます。
- **一般的な課題とヒント**:
  - **コード署名の問題**: Xcode の **Signing & Capabilities** で証明書とプロビジョニングプロファイルを確認してください。不明な場合は「Automatically manage signing」オプションを使用します。
  - **アプリレビュー拒否**: Apple のガイドラインに準拠し、遅延を避けるためにアプリを徹底的にテストしてください。
  - **D-U-N-S 番号取得の遅延**: 法人の場合は、登録の前提条件である D-U-N-S 番号を早めに申請してください。

---

これらのステップに従うことで、個人または法人として、Apple Developer Program を利用して iOS アプリをアップロードおよび更新することができます。詳細については、[developer.apple.com](https://developer.apple.com) の Apple 公式ドキュメントを参照してください。