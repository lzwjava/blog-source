---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Xcodeのジャンクファイルを削除してディスク容量を解放
translated: true
type: note
---

良い質問ですね 👍 Xcode（およびiOS Simulator）は時間の経過とともに大量の「ジャンク」を蓄積します — ビルドキャッシュ、Derived Data、シミュレータデバイス、デバイスサポートファイル、ログなどです。これらをクリーンアップするとギガバイト単位の空き容量が増えます。以下に体系的なアプローチを紹介します：

---

### 1. Derived Data（ビルドキャッシュ）をクリア

これにより古いビルド生成物、中間ファイル、インデックスが削除されます。

* **Xcode UIから**：
  `Xcode → Settings → Locations → Derived Data → 矢印をクリック → フォルダを削除`
* **ターミナルから**：

  ```bash
  rm -rf ~/Library/Developer/Xcode/DerivedData/*
  ```

---

### 2. シミュレータデータをクリーン

* シミュレータのコンテンツをリセットまたは削除：

  ```bash
  xcrun simctl erase all
  ```

  （アプリとデータを消去しますが、デバイス定義は保持されます）

* 使用されていないすべてのシミュレータデバイスを削除（古いiOSバージョンが蓄積されている場合）：

  ```bash
  xcrun simctl delete unavailable
  ```

* すべてのシミュレータデバイスを削除（注意：すべてを削除します）：

  ```bash
  xcrun simctl delete all
  ```

* 重いディレクトリを手動で削除：

  ```bash
  rm -rf ~/Library/Developer/CoreSimulator/Devices/*
  ```

---

### 3. 古いデバイスサポートファイルを削除

実機を接続すると、Xcodeは各iOSバージョンのデバッグシンボルをダウンロードします。これらが蓄積されます。

```bash
rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*
```

---

### 4. アーカイブをクリーン

「Product → Archive」からのアプリアーカイブは大量の容量を消費します。

* XcodeのOrganizerから：Archives → 古いアーカイブを削除
* またはターミナルから：

  ```bash
  rm -rf ~/Library/Developer/Xcode/Archives/*
  ```

---

### 5. ログをクリーン

```bash
rm -rf ~/Library/Developer/Xcode/DocumentationCache/*
rm -rf ~/Library/Developer/Xcode/ios device logs/*
rm -rf ~/Library/Logs/CoreSimulator/*
```

---

### 6. Derived Indexes & Module Cacheをクリーン

```bash
rm -rf ~/Library/Developer/Xcode/DerivedDataModuleCache/*
```

---

### 7. オプション：完全リセット

Xcode関連のキャッシュを完全にリセットしたい場合：

```bash
rm -rf ~/Library/Developer/Xcode/*
rm -rf ~/Library/Developer/CoreSimulator/*
```

（これによりすべてが削除されます：シミュレータ、アーカイブ、Derived Dataなど。次回Xcode起動時は「新規インストール」のような状態になります）

---

⚠️ **ヒント**

* これらのコマンドを実行する前は常にXcodeとSimulatorを終了してください。
* `du -sh ~/Library/Developer/*` を使用してどのフォルダが最も大きいか確認できます。
* Xcodeの `Clean Build Folder` (`⇧⌘K`) で十分な場合もありますが、ディープクリーニングではより多くの空き容量が得られます。

---

一般的なジャンクを一度にクリーンアップするための**単一スクリプト**を（オプションフラグ付きで）お伝えしましょうか？