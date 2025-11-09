---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ghosttyの設定ファイルを理解する
translated: true
type: note
---

### Ghostty設定ファイルの仕組み

Ghosttyの設定ファイルは、`key = value`形式のシンプルなテキストベースのフォーマットを使用しています。直感的に理解できるように設計されており、デフォルト値から変更したい設定だけを上書きできます。Ghosttyはそれ以外のすべての設定に対して適切なデフォルト値をあらかじめ備えているため、最小限の設定ファイル、あるいは空の設定ファイルでも問題なく動作します。

#### 構文の簡単な説明
- **キーと値**: キーは常に小文字で、大文字と小文字は区別されます（例: `font-family = JetBrains Mono`）。値は、スペースや特殊文字を含まない限り引用符で囲む必要はありません（例: `font-family = "JetBrains Mono Nerd Font"`）。`=`の前後のスペースは任意です。
- **コメント**: 行頭に`#`を付けるとコメントになります（例: `# 私のカスタムテーマ`）。値の後ろにインラインコメントを記述することはできません。値の一部としてパースされてしまいます。
- **デフォルト値へのリセット**: `key =`のように空の値を設定すると、その設定をGhosttyの組み込みデフォルト値に戻します。
- **特別な値**: 一部のオプションは、期間（例: `resize-overlay-duration = 4s 200ms`）など独自のフォーマットを持っています。詳細はドキュメントを参照してください。
- **ファイルの読み込み**: Ghosttyは設定ファイルを`~/.config/ghostty/config`（Linux/Windows）または`~/Library/Application Support/com.mitchellh.ghostty/config`（macOS）で探します。モジュール式の設定を行うために、`config-file = path/to/other.conf`で他のファイルをインクルードできます。
- **CLIによる上書き**: どの設定もコマンドラインフラグで設定できます（例: `ghostty --font-family="Fira Code"`）。これらは設定ファイルの値より優先されます。

変更を反映するには、デフォルトのキーバインド（macOSではCmd+Shift+,、Linux/WindowsではCtrl+Shift+,）でリロードするか、`ghostty +reload-config`を実行します。

すべてのオプションとデフォルト値を確認するには、ターミナルで`ghostty +show-config --default --docs`を実行してください。

### 一般的な設定例
「一般的な」設定ファイルは、多くの場合最小限です。フォント、色、パディングなど、使いやすさのためにほんの少しだけ変更するのが普通です。Ghosttyのデフォルト設定には、JetBrains Monoフォントファミリー（Nerd Fontサポート組み込み）、クリーンな背景/前景色のスキーム、余分なパディングなし、などが含まれています。

以下は、人気のフォントを使用したダークテーマに、パディングと基本的なキーバインドを加えた、シンプルで典型的な例です。これを`config`ファイルとして保存してください:

```
# パディングとカスタムフォントを備えた基本的なダークテーマ
background = 1e1e1e
foreground = f8f8f2
font-family = "JetBrains Mono Nerd Font"
font-size = 14

# テキストの周囲に余白を追加
window-padding-x = 8
window-padding-y = 8

# カスタムキーバインド（必要に応じてデフォルトを上書き）
keybind = cmd+t=new_tab
keybind = cmd+w=close_tab
keybind = cmd+d=new_split:right
```

これは、必要な部分をカスタマイズしつつ、軽量な状態を保ちます。ドキュメントにあるより多くの色（例: `color0 = 282a36`のようなパレットエントリ）やテーマを追加して拡張できます。

[Ghostty設定ドキュメント](https://ghostty.org/docs/config)