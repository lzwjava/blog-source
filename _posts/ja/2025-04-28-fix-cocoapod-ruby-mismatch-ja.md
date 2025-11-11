---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: macOSでのCocoaPod Rubyバージョン不一致の修正
translated: true
type: note
---

状況がわかりました：あなたのシステムのRubyとgemの設定が少し混ざっているため、`pod deintegrate`コマンドがCocoaPodsを見つけられないのです。順を追って説明します：

---

### 問題点
- あなたはmacOS（おそらく`arm64`、M1/M2）を使用しています
- Rubyを（Homebrew経由で3.4.1に）更新しました
- あなたの`pod`実行ファイルは古いRuby（3.3.0 gemパス: `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`）に属しています
- しかし現在はRuby 3.4.1がアクティブなため、正しい場所に`cocoapods` gemを見つけられません

この不一致が失敗の原因です。

---

### 解決策

#### 1. 実際に実行しているRubyを使用してCocoaPodsを再インストール
```bash
gem install cocoapods
```

その後、以下で確認：
```bash
which pod
pod --version
```

---

#### 2. `brew`のRubyを使用している場合、Homebrew経由でCocoaPodsをインストールするのが最適
```bash
brew install cocoapods
```

これでRubyバージョンの不一致を完全に回避できます。

---

#### 3. `rbenv`または`rvm`を使用している場合、正しいRubyバージョン環境にいることを確認
例：`rbenv`の場合：
```bash
rbenv global 3.4.1
gem install cocoapods
```

---

#### 4. 古いpodバイナリシンボリックリンクをクリーンアップ
孤立した`pod`コマンドの出所を確認：
```bash
which pod
```
もし`/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`を指している場合、それを削除するか、正しいものを使用するように`PATH`を更新してください。

---

✅ 推奨（簡単で安定）：以下のコマンドを実行   
```bash
brew install cocoapods
```
その後、再試行：
```bash
pod deintegrate
```

---

**PATHを修正して常に正しいpodバイナリを選択するように**手伝いましょうか？それとも最も簡単な再インストールの修正だけを行いますか？