---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ZedのEmacsキーバインド設定
translated: true
type: note
---

### ZedエディタをEmacsキーバインドで設定する

「Zigエディタ」は標準的なツールを指すものではありません（Zigは組み込みエディタのないプログラミング言語です）ので、おそらく**Zed**（高性能コードエディタ）のことをお考えだと思います。もし違う場合はご指摘ください！ZedにはEmacsキーバインドの組み込みサポート（「Emacs (Beta)」と表示）があります。これには移動（`Ctrl-b/f/n/p`）や編集（`Ctrl-d`で文字削除、`Ctrl-k`で行末まで切り取り）など多くの基本操作が最初から含まれています。簡単に有効化でき、必要に応じてさらにカスタマイズも可能です。

#### ステップ1: 組み込みのEmacsキーマップを有効にする
ZedのEmacsモードは事前定義されており、基本的な操作のために手動でバインドを設定する必要はありません。有効化する方法は以下の通りです：

1. Zedの設定を開く：
   - macOS: `Cmd-,`
   - Windows/Linux: `Ctrl-,`

2. 設定UIで「base keymap」を検索し、**Emacs**に設定する。

   *または、`settings.json`を直接編集*（macOSでは`Cmd-Alt-,`、Windows/Linuxでは`Ctrl-Alt-,`で開く）：
   ```json
   {
     "base_keymap": "Emacs"
   }
   ```

   保存してZedを再読み込み（`Cmd-R`または`Ctrl-R`）。これだけで、ベータ版のEmacsキーマップがすぐに有効になります。

   別の方法として、コマンドパレット（`Cmd-Shift-P`または`Ctrl-Shift-P`）を開き、「toggle base keymap」と入力してEmacsを選択します。

これで、追加作業なしにEmacsのコアな操作性が得られます。組み込みのバインドの完全なリストは、Zedのデフォルトキーマップファイル（例：GitHub経由）で確認できますが、基本操作には以下が含まれます：
- **移動**: `Ctrl-b`（左の文字）、`Ctrl-f`（右の文字）、`Ctrl-p`（上の行）、`Ctrl-n`（下の行）、`Alt-b/f`（前/次の単語）。
- **編集**: `Ctrl-d`（文字削除）、`Ctrl-k`（行末まで切り取り）、`Ctrl-y`（ヤンク/貼り付け）、`Ctrl-@`（リージョンのマーク設定）、`Ctrl-w`（リージョン切り取り）。
- **その他**: `Ctrl-x Ctrl-s`（保存）、`Ctrl-g`（キャンセル）、`Ctrl-/`（元に戻す）。

#### ステップ2: 基本的なバインドを追加またはカスタマイズする（必要に応じて）
調整やよりEmacsらしい動作（例：ホーム/エンドや段落ナビゲーションの改善）のために、`keymap.json`を編集します：
- コマンドパレットから開く：「open keymap file」と入力。
- パス：`~/.config/zed/keymap.json`（macOS/Linux）または`~\AppData\Roaming\Zed\keymap.json`（Windows）。

「Editor」などのコンテキストでJSON配列としてバインドを追加します。以下は基本移動と編集の**最小限の例**です（互換性のためにコミュニティ設定を基にしているため、配列に貼り付けてください）：

```json
[
  {
    "context": "Editor",
    "bindings": {
      // 基本移動
      "ctrl-a": "editor::MoveToBeginningOfLine",
      "ctrl-e": "editor::MoveToEndOfLine",
      "ctrl-b": "editor::MoveLeft",
      "ctrl-f": "editor::MoveRight",
      "ctrl-p": "editor::MoveLineUp",
      "ctrl-n": "editor::MoveLineDown",
      "alt-b": "editor::MoveToPreviousWordStart",
      "alt-f": "editor::MoveToNextWordEnd",

      // 基本編集
      "ctrl-d": "editor::DeleteRight",
      "ctrl-k": "editor::CutToEndOfLine",
      "ctrl-y": "editor::Paste",
      "ctrl-w": "editor::Cut",
      "ctrl-@": ["editor::SetSelectionAnchor", { "selection_id": 0 }],  // マーク設定
      "ctrl-x ctrl-x": "editor::FlipSelectionAnchor",  // ポイントとマークを交換

      // ナビゲーション追加
      "ctrl-home": "editor::MoveToBeginning",
      "ctrl-end": "editor::MoveToEnd",
      "ctrl-g": "editor::Cancel"
    }
  }
]
```

- 保存してZedを再読み込み。これらはベースのEmacsマップを上書きまたは追加します。
- エディタバッファでテスト。選択には`Ctrl-Space`（または`Ctrl-@`）でマークを設定し、移動してリージョンを選択します。
- プロのヒント：競合を避けるために、settings.jsonで`vim_mode: false`と組み合わせて使用。

#### ヒント
- **ベータ版ステータス**: Emacsモードは改善中（進捗は[こちら](https://github.com/zed-industries/zed/issues/4856)で確認）。問題はZedのGitHubで報告。
- **完全なカスタム設定**: 高度な設定（例：`Ctrl-x o`でのペイン切り替え）については、以下のディスカッションでコミュニティ例を参照。
- Vim/Helixモードを併用したい場合は、設定で`vim_mode: true`または`helix_mode: true`を設定—これらは上層に重なります。

これで基本的なEmacsの操作性の80%が得られるはずです。まずは組み込み機能から始め、繰り返し調整してください！

[キーバインドのドキュメント](https://zed.dev/docs/key-bindings)  
[Zedの設定](https://zed.dev/docs/configuring-zed)  
[Emacsキーマップのディスカッション](https://github.com/zed-industries/zed/discussions/6572)  
[Emacs互換性の問題](https://github.com/zed-industries/zed/issues/4856)