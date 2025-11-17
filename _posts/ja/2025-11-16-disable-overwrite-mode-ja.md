---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: VS Code上書きモードの無効化
translated: true
type: note
---

Visual Studio Code のデフォルト動作は **挿入モード**（テキストを入力すると既存のテキストが押し出される）です。  
**上書きモード**（入力が既存のテキストを置き換える）は、キーボードの **Insert** キーを押すと有効になります。このキー操作で挿入モードと上書きモードが切り替わります。

### 上書きモードから挿入モードに戻す方法

1. キーボードの **Insert** キーを一度押します。  
   → 右下のステータスバーが **OVR** (Overwrite) から **INS** (Insert) に変わります。

### 誤って上書きモードに入らないようにしたい場合

Insert キーの切り替え機能を完全に無効にできます：

#### 方法 1: キーボードショートカット（推奨）
`Ctrl + Shift + P` → **"Toggle Insert/Overwrite"** と入力 →  
`Preferences: Toggle Insert on Paste and Overtype` または類似のコマンドが表示されます。  
より確実に設定するには：

#### 方法 2: `settings.json` に追加
```json
// Insert キーによる上書きモードの切り替えを無効化
"editor.occurencesHighlight": true,
"editor.overtypeMode": false,

// これが主要な設定:
"keyboard.dispatch": "keyCode"
```

実際には、以下が最も一般的な解決策です：

```json
// VS Code で Insert キーを完全に無効化
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite",
    "when": "editorTextFocus"
}
```

またはグローバルに上書きをオフにします：

```json
"editor.occurrencesHighlight": true,
"editor.overwriteMode": false   // 実際の設定ではないので無視

// 上書き切り替えを無効化する正しい方法:
{
    "key": "insert",
    "command": "noop"   // またはデフォルトのバインディングを削除
}
```

#### 最も簡単な恒久的な解決策（多くのユーザーが使用）:
1. 設定を開く (`Ctrl + ,`)
2. **"overwrite"** を検索
3. **Editor: Overtype** のチェックを外す（存在する場合）、またはより良い方法：
4. 以下の行を `settings.json` に追加（Ctrl + Shift + P → "Preferences: Open Settings (JSON)"）:

```json
// Insert キーによる上書きモード切り替えを完全に無効化
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite"
}
```

これを追加後、Insert キーは VS Code で何もせず、常に挿入モードを維持します。

これは、誤って Insert キーを押してしまう（特に台湾/アジアの小さなキーボードを持つノートパソコンで Insert キーが押しやすい）開発者が最も一般的に使用する信頼性の高い解決策です。

もし macOS をご利用の場合（異なるキーを使用）や、ステータスバークリックによる解決策をご希望の場合はお知らせください！