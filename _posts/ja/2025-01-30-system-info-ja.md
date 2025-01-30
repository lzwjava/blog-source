---
audio: false
lang: ja
layout: post
title: マクOSのシステム情報
translated: true
---

### macOS システム情報の取得方法
macOS でシステム情報を取得するには、いくつかのビルトインツールやコマンドを使用できます。以下に、さまざまな種類のシステム情報を取得する方法を紹介します。

### 1. **システム情報ユーティリティ**
システム情報アプリは、Macのハードウェアとソフトウェアに関する包括的な概要を提供します。

- Spotlight Search を開くには `Cmd + Space` を押し、「System Information」と入力して Enter を押します。
- または、Apple メニュー > このMac > システムレポートから開くこともできます。

### 2. **このMacについて**
Macの仕様を迅速に確認するための方法です。

- 画面の左上隅の **Apple メニュー** をクリックします。
- **このMac** を選択します。これにより、macOS バージョン、プロセッサ、メモリ、シリアル番号などの基本情報が表示されます。

### 3. **ターミナルコマンド**
ターミナルを使用して詳細なシステム情報を取得することもできます。

- ターミナルを開くには、`Applications` > `Utilities` > `Terminal` から開き、または Spotlight で検索します。

#### 基本的なシステム情報
```sh
system_profiler SPHardwareDataType
```

#### 詳細なシステム情報
```sh
system_profiler
```

#### CPU 情報
```sh
sysctl -n machdep.cpu.brand_string
```

#### メモリ情報
```sh
sysctl hw.memsize
```

#### ディスク使用状況
```sh
df -h
```

#### ネットワーク情報
```sh
ifconfig
```

#### バッテリー情報（ノートパソコン用）
```sh
pmset -g batt
```

#### インストールされているソフトウェアのリスト
```sh
ls /Applications
```

#### macOS バージョン
```sh
sw_vers
```

#### ユーザ情報
```sh
id
```

#### 実行中のプロセスのリスト
```sh
ps aux
```

#### インストールされている Brew パッケージのリスト
```sh
brew list
```

#### インストールされている Pip パッケージのリスト
```sh
pip list
```

#### インストールされている Gem パッケージのリスト
```sh
gem list
```

### 4. **アクティビティモニター**
このアプリは、Macの CPU、メモリ、エネルギー、ディスク、ネットワーク使用状況に関するリアルタイム情報を提供します。

- アクティビティモニターを開くには、`Applications` > `Utilities` > `Activity Monitor` から開き、または Spotlight で検索します。

### 5. **ディスクユーティリティ**
このアプリは、ストレージデバイスに関する情報を提供します。

- ディスクユーティリティを開くには、`Applications` > `Utilities` > `Disk Utility` から開き、または Spotlight で検索します。

### 6. **第三者ツール**
また、iStat Menus や CoconutBattery などの第三者アプリも詳細なシステム情報とモニタリング機能を提供します。

これらの方法を使用することで、macOS で幅広いシステム情報を収集することができます。