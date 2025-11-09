---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GitHub内表示設定ウィンドウ
translated: true
type: note
---

### 概要
このXMLファイルは、macOSアプリケーション用のInterface Builder XIB（XML Interface Builder）ドキュメントです。XIBファイルはXcodeでユーザーインターフェースを宣言的に定義するために使用され、特にCocoaアプリのウィンドウ、ビュー、コントロールに用いられます。この特定のファイルは、**Reveal-In-GitHub**（おそらくIDEやファイルシステムからGitHubでソースコードファイルやリポジトリを素早く開くためのユーティリティ）というアプリの設定ウィンドウのユーザーインターフェースを定義しています。

このファイルはmacOS（Cocoaランタイム）を対象とし、Auto Layout（`useAutolayout="YES"`）を使用しています。メインのウィンドウオブジェクトを中心に構成され、カスタムコントローラクラス（`RIGSettingWindowController`）への接続、主要なビューへのアウトレット、およびボタン、ラベル、カスタムコンテナなどのさまざまなUIサブビューが含まれています。

主なメタデータ：
- **ツールバージョン**: Xcode 9.0.1（toolsVersion="9059"）、macOS 10.12.6上でビルド（systemVersion="14F27"）。
- **ウィンドウの動作**: タイトルバーあり、閉じる、最小化、リサイズが可能。キービューループを自動再計算せず、デフォルトのアニメーションを使用。
- **初期位置/サイズ**: スクリーン位置（527, 176）にサイズ651x497ピクセルで開く（1440x877スクリーン上）。

ファイルのルートは`<document>`要素で、`<dependencies>`（Cocoaプラグイン用）と`<objects>`（実際のUI階層）を含みます。

### 主要コンポーネント

#### 1. **File's Owner（カスタムコントローラ）**
   - **クラス**: `RIGSettingWindowController`
   - これはウィンドウのコントローラとして機能し、設定の読み込み/保存などのロジックを管理します。
   - **アウトレット**（UI要素への接続）:
     - `configsView` → 設定オプションを表示するためのカスタムビュー（ID: `IKd-Ev-B9V`）。
     - `mainView` → ウィンドウのコンテンツビュー（ID: `se5-gp-TjO`）。
     - `window` → 設定ウィンドウ自体（ID: `F0z-JX-Cv5`）。
   - ウィンドウの`delegate`もこのコントローラに接続されています。

#### 2. **標準オブジェクト**
   - **First Responder**（`-1`）: キーボードイベント処理のためのプレースホルダ。
   - **Application**（`-3`）: NSApplicationインスタンスを表す（ここでは直接使用されていない）。

#### 3. **設定ウィンドウ**
   - **ID**: `F0z-JX-Cv5`
   - **タイトル**: "Reveal-In-GitHub Settings"
   - **コンテンツビュー**（ID: `se5-gp-TjO`）: ウィンドウとともに自動リサイズするフルサイズのビュー（651x497）。すべてのサブビューを含み、固定フレームで配置されています（Auto Layoutが有効ですが、制約はプログラム的にまたは.storyboardコンパニオンで追加されている可能性があります）。

   **サブビューのレイアウト**（すべて固定フレームを使用して配置。y座標は上から下に向かって増加）:

   | 要素 | タイプ | 位置 (x, y) | サイズ (w x h) | 説明 |
   |---------|------|-----------------|--------------|-------------|
   | **Save Button** | `NSButton`（ID: `EuN-9g-Vcg`） | (14, 13) | 137x32 | 左下の「Save」ボタン（角丸ベゼル）。コントローラの`saveButtonClcked:`アクションをトリガー。スモールシステムフォント（13pt）使用。 |
   | **Reset Default Menus Button** | `NSButton`（ID: `KvN-fn-w7m`） | (151, 12) | 169x32 | 近くの「Reset Default Menus」ボタン。`resetMenusButtonClicked:`アクションをトリガー。スモールシステムフォント（13pt）使用。 |
   | **Config View** | `NSView`（カスタム, ID: `IKd-Ev-B9V`） | (20, 54) | 611x330 | 中央の大きなカスタムビューで「Config View」とラベル付け。GitHubリポジトリ設定（リポジトリパス、認証トークンなど）のためのテーブル、リスト、トグルなどの動的コンテンツのコンテナである可能性が高い。`configsView`アウトレットに接続。 |
   | **Custom Menu Items Label** | `NSTextField`（ID: `G1C-Td-n9Y`） | (18, 425) | 187x17 | 下部近くの静的ラベル「Custom Menu Items」。Helvetica Neue（17pt）、ラベルカラー。 |
   | **Clear Default Repos Button** | `NSButton`（ID: `KvN-fn-w7m`） | (14, 449) | 164x32 | 左下の「Clear Default Repos」ボタン。`clearButtonClicked:`アクションをトリガー。スモールシステムフォント（13pt）使用。 |
   | **Menu Title Label** | `NSTextField`（ID: `UUf-Cr-5zs`） | (20, 392) | 77x18 | 静的ラベル「Menu Title」。Helvetica Neue（14pt）、ラベルカラー。 |
   | **Keyboard Shortcut Label** | `NSTextField`（ID: `rMv-by-SKS`） | (112, 391) | 63x19 | 静的ラベル「⌃⇧⌘ +」（Control+Shift+Command +）。Lucida Grande UI（15pt）、ラベルカラー。アプリのメニュー用のカスタマイズ可能なグローバルショートカットを示す。 |
   | **URL Pattern Label** | `NSTextField`（ID: `zW4-cw-Rhb`） | (410, 392) | 94x18 | 静的ラベル「URL Pattern 」。システムフォント（15pt）、ラベルカラー。GitHub URLテンプレート（ファイルやblameビューへのディープリンク用など）の設定用と思われる。 |

   - **レイアウトに関する注記**:
     - 要素はコンパクトでフォームのようなデザインのためにほとんど左揃え（x=14-20）。
     - 上部: アクションボタン（Save/Reset）。
     - 中央: 大きなConfig View（リポジトリ/設定管理のための大部分のスペース）。
     - 下部: メニューカスタマイズ用のラベルとクリアボタン。
     - すべてのテキストフィールドは編集不可（静的ラベル）であり、ユーザー入力はConfig View内またはここで定義されていない別のフィールドで行われることを示唆。
     - 色: システムデフォルト（アクセシビリティのためのラベル/コントロールカラー）。
     - フォント: ネイティブなmacOS感覚のためのシステム、Helvetica Neue、Lucida Grandeの混在。

### 目的と機能
この設定ウィンドウにより、ユーザーは以下を行うことができます：
- **リポジトリ/設定の管理**: 中央の「Config View」を介して（例：デフォルトのGitHubリポジトリの追加/削除）。
- **メニューのカスタマイズ**: メニュータイトル、グローバルキーボードショートカット（⌃⇧⌘+）、GitHubでファイルを表示するためのURLパターンを設定。
- **変更の永続化**: 専用ボタンで設定を保存、またはデフォルトをリセット/クリア。

コントローラ（`RIGSettingWindowController`）はボタンアクションを処理：
- `saveButtonClcked:` – ユーザーの変更を保存（例：UserDefaultsまたはplistへ）。
- `resetMenusButtonClicked:` – 工場出荷時のメニュー設定を復元。
- `clearButtonClicked:` – デフォルトのリポジトリエントリを削除。

このXIBは、おそらくアプリのコード内でプログラム的に読み込まれ（例：`NSNib(nibNamed: "Settings", bundle: nil)`）、カスタムビューは動的に（例：リポジトリリスト用のNSTableViewで）設定されます。

このアプリを構築または変更する場合、XcodeのInterface BuilderでXIBを開いてレイアウトを視覚的に表示/編集できます。コード統合については、コントローラクラス内でアクションセレクタに一致するIBActionメソッドを探してください。