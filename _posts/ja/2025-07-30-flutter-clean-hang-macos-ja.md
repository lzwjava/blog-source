---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: macOSでのFlutter Cleanハングの解決
translated: true
type: note
---

ああ、なるほど 👍  
macOS では `flutter clean` が「ハング」しているように見えることがあります — 特に生成されたファイルが多い場合や、Xcode の `DerivedData` フォルダが巨大な場合に発生します。

---

### ✅ 試してみる手順

1. **固まったコマンドをキャンセル**  
   `CTRL + C` を押します。

2. **手動でクリーンアップ (`flutter clean` と同じ効果)**  
   以下のビルド/キャッシュフォルダを自分で削除できます:
   ```bash
   rm -rf build/ .dart_tool/ ios/Pods ios/Podfile.lock ios/Flutter/Flutter.framework ios/Flutter/Flutter.podspec
   ```

   Xcode のキャッシュも削除したい場合:
   ```bash
   rm -rf ~/Library/Developer/Xcode/DerivedData
   ```

3. **依存関係を再取得**
   ```bash
   flutter pub get
   ```

4. **CocoaPods を再インストール (iOS 用)**
   ```bash
   cd ios
   pod install --repo-update
   cd ..
   ```

5. **再度ビルド/実行**
   ```bash
   flutter run
   ```

---

⚡ **ヒント:** クリーン後の初回は少し時間がかかる場合があります (Flutter が `.dart_tool`、`.pub-cache`、iOS Pods などを再生成する必要があるため) が、永遠に固まったままになることはありません。それでも「固まる」現象が続く場合は、以下の要因が関係している可能性があります:

- **Flutter SDK が古い** → `flutter upgrade` を実行
- **CocoaPods が古い** → `sudo gem install cocoapods` を実行  
- **Rosetta / M1 チップの問題**: Apple Silicon を使用している場合、設定によっては `ios` フォルダ内で `arch -x86_64 pod install` を実行する必要があることがあります。

---

👉 `flutter clean` の固まり問題をデバッグする代わりに、ビルドキャッシュをワイプして Pods をリセットする（基本的に「スーパークリーン」な）**ワンライナースクリプト**をお伝えしましょうか？