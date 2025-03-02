---
audio: true
generated: false
lang: ja
layout: post
title: macOSのシステム情報
translated: true
---

macOSでシステム情報を取得するには、いくつかの組み込みツールとコマンドを使用できます。以下に、さまざまな種類のシステム情報を取得する方法をいくつか紹介します。

### 1. **システム情報ユーティリティ**
システム情報アプリは、Macのハードウェアとソフトウェアの包括的な概要を提供します。

- **Spotlight Search** を `Cmd + Space` で開き、「システム情報」と入力し、Enterを押します。
- または、**Apple メニュー** > **このMacについて** > **システムレポート** から開くこともできます。

### 2. **このMacについて**
これは、Macの仕様の簡単な概要を提供します。

- 画面の左上隅にある **Apple メニュー** をクリックします。
- **このMacについて** を選択します。これにより、macOSのバージョン、プロセッサ、メモリ、シリアル番号などの基本情報が表示されます。

### 3. **ターミナルコマンド**
ターミナルを使用して、さまざまなコマンドで詳細なシステム情報を取得できます。

- `Applications` > `Utilities` > `Terminal` から **Terminal** を開くか、Spotlightで検索します。

#### 基本システム情報
```sh
system_profiler SPHardwareDataType
```

#### 詳細システム情報
```sh
system_profiler
```

#### CPU情報
```sh
sysctl -n machdep.cpu.brand_string
```

#### メモリ情報
```sh
sysctl hw.memsize
```

#### ディスク使用量
```sh
df -h
```

#### ネットワーク情報
```sh
ifconfig
```

#### バッテリー情報（ノートPC用）
```sh
pmset -g batt
```

#### インストールされたソフトウェアの一覧
```sh
ls /Applications
```

#### macOSバージョン
```sh
sw_vers
```

#### ユーザー情報
```sh
id
```

#### 実行中のプロセスの一覧
```sh
ps aux
```

#### インストールされたBrewパッケージの一覧
```sh
brew list
```

#### インストールされたPipパッケージの一覧
```sh
pip list
```

#### インストールされたGemパッケージの一覧
```sh
gem list
```

### 4. **アクティビティモニター**
このアプリは、MacのCPU、メモリ、エネルギー、ディスク、ネットワークの使用状況についてリアルタイムの情報を提供します。

- `Applications` > `Utilities` > `Activity Monitor` から **アクティビティモニター** を開くか、Spotlightで検索します。

### 5. **ディスクユーティリティ**
このアプリは、ストレージデバイスについての情報を提供します。

- `Applications` > `Utilities` > `Disk Utility` から **ディスクユーティリティ** を開くか、Spotlightで検索します。

### 6. **サードパーティツール**
**iStat Menus** や **CoconutBattery** のようなサードパーティアプリケーションもあり、詳細なシステム情報とモニタリング機能を提供します。

これらの方法を使用することで、macOSで広範なシステム情報を収集できます。