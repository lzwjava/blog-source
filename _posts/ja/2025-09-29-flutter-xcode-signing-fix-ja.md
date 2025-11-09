---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Flutter Xcodeコード署名失敗の修正
translated: true
type: note
---

あなたが遭遇しているのは、Flutter/Xcodeでよくあるコード署名の失敗です。Xcode/`security`が有効な署名アイデンティティを見つけられないため、`flutter run`が実機用にアプリを署名できません。以下に、明確で順序立てた修正方法とトラブルシューティングコマンドを示します。今すぐシミュレーターで実行するか、実機で実行するための署名を設定するか、どちらかのパスを選択してください。追加情報は求めず、今すぐこれを修正したいと想定します。

---

# クイックオプション（いずれかを選択）

**A — シミュレーターで実行（コード署名不要）**
証明書を扱わずに素早く実行したい場合：

1. シミュレーターを開く: `open -a Simulator`
2. シミュレーターをターゲットにFlutterを実行:
   `flutter run -d "$(xcrun simctl list devices | grep -m1 -o "iPhone.*(Simulator)" | sed 's/ (Simulator)//')"`
   または、より簡単に: `flutter run -d iPhone-14` (`xcrun simctl list`で表示される利用可能なシミュレーター名に置き換えてください)。

**B — 実機デプロイ用に署名を修正（実機テストに推奨）**
以下の手順を順に実行してください。

---

# 実機デプロイ用に署名を修正する手順

## 1) 環境と基本的なチェックの確認

以下を実行し、出力を確認してください:

```bash
flutter doctor -v
xcode-select --print-path
xcodebuild -version
security find-identity -p codesigning -v
xcrun simctl list devices
```

`security find-identity -p codesigning -v` は少なくとも1つのアイデンティティを表示するはずです。あなたの環境では `0 valid identities found` と表示されています — これが失敗の原因です。

## 2) Xcodeの自動署名を使用する（最も簡単）

1. ワークスペースを開く:
   `open ios/Runner.xcworkspace`
2. Xcodeで: `Runner`プロジェクト → `Runner`ターゲット → **Signing & Capabilities** を選択。
3. **Team** をあなたのApple ID / Apple Developerアカウントに設定。Apple IDが追加されていない場合:

   * Xcode → Preferences → Accounts → `+` → Apple IDを追加。
4. **Automatically manage signing** にチェックを入れる。
5. **Bundle Identifier** が一意であることを確認（逆DNSスタイル、例: `com.yourname.yourapp`）。
6. Xcodeが開発証明書とプロビジョニングプロファイルを作成しようとします。プロンプトが表示されたら、Xcodeに管理を許可してください。

> 注意: 任意の実機への完全なデプロイには、Apple Developerメンバーシップ（$99/年）が必要です。Xcodeは無料のApple IDを「無料プロビジョニング」に使用できますが、制限があります（デバイス数、特定の権利なし）。

## 3) デバイスを登録する（必要な場合）

Xcodeが自動的にデバイスを登録できない場合、Apple Developer Portal → Certificates, IDs & Profiles → Devices → デバイスUDIDを追加に移動します。デバイスを接続し、XcodeのDevices and Simulatorsウィンドウで選択することで、デバイスUDIDを取得できます。

## 4) 証明書を手動で生成/インポート（既にp12がある場合）

`.p12`証明書と秘密鍵がある場合:

```bash
security import /path/to/certificate.p12 -k ~/Library/Keychains/login.keychain-db -P "P12_PASSWORD" -T /usr/bin/codesign
```

その後、`security find-identity -p codesigning -v` を再実行して表示されることを確認してください。

## 5) Xcodeに証明書を作成させることを希望する場合

Xcode → Accounts → あなたのApple IDを選択 → Manage Certificates → `+` → **iOS Development** を追加。これにより、キーチェーン内に証明書が作成され、`security find-identity`に表示されます。

## 6) Command Line Toolsが設定されていることを確認

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

必要に応じてライセンスを承諾:

```bash
sudo xcodebuild -license accept
```

## 7) 署名設定後、ターミナルから実行

プロジェクトルートから:

```bash
flutter clean
flutter pub get
flutter run
```

複数デバイスがある場合は、`-d <device-id>` を指定してください。

---

# トラブルシューティングのヒントとよくある落とし穴

* **「0 valid identities found」が解消しない** — 証明書の秘密鍵がログインキーチェーンにあることを確認（Keychain Access → login を開く）。証明書をインポートしても秘密鍵をインポートしていない場合、署名は失敗します。
* **Bundle IDの不一致** — Developer PortalのApp IDは、Xcodeのバンドル識別子と完全に一致する必要があります（一部の場合、ワイルドカードが許可されます）。
* **チームが選択されていない** — Xcodeが「No account」を表示 — Xcode Preferences → AccountsでApple IDを追加。
* **プロビジョニングプロファイルの期限切れ** — Developer Portalをチェックし、プロビジョニングプロファイルを再生成。
* **無料プロビジョニングの制限** — 無料のApple IDを使用している場合、7日ごとに再プロビジョニングが必要で、デバイス数が制限されることがあります。
* **CI / 自動化** — `fastlane match` または App Store Connect APIを使用して、証明書とプロファイルを一元的に管理。
* **Codesign権限エラー** — キーチェーン項目がcodesignアクセスを許可していることを確認。時々、`/usr/bin/codesign`がキーチェーン内の秘密鍵にアクセスすることを手動で許可する必要があります。
* **`flutter run`がまだ失敗する場合**、Xcodeビルドを実行して詳細なエラーを確認: ワークスペースを開き、XcodeでRunを押す。Signing & CapabilitiesのエラーをUIでチェック。

---

# 便利なコマンド（コピー＆ペースト用）

コード署名アイデンティティのリスト:

```bash
security find-identity -p codesigning -v
```

`.p12`のインポート:

```bash
security import /path/to/yourcert.p12 -k ~/Library/Keychains/login.keychain-db -P "P12PASSWORD" -T /usr/bin/codesign
```

Xcodeコマンドラインツールの設定:

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

iOSワークスペースを開く:

```bash
open ios/Runner.xcworkspace
```

---

# 必要であれば、以下ができます

* 証明書/プロファイルを作成するためのXcodeでの正確なクリック順序をステップバイステップで提供（核心的な手順は既に含まれています）、または
* 複数マシン/CI用の自動化を希望する場合、`fastlane`/`match`のサンプルコマンドを提供、または
* Xcode自動署名ルートを試した後の新しいエラー出力を解釈するのを支援。

どのパスを選択したか（今すぐシミュレーター / Xcode自動 / 手動p12インポート / CI）を教え、まだ失敗する場合は新しいエラーを貼り付けてください — 次のステップを案内します。