---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: macOSへのChromiumインストール
translated: true
type: note
---

はい、macOSでもGoogle Chromeの代替としてChromiumをインストールすることはもちろん可能です。ChromiumはChromeの基盤となるオープンソースプロジェクトであり、機能は非常に似ていますが、自動更新や一部のコーデックなど、Google独自の機能は含まれていません。

### インストール方法
いくつかの簡単な方法があります：

1. **Homebrew経由（ほとんどのユーザーにとって最も簡単）**:
   - まだインストールしていない場合はHomebrewをインストール: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   - その後実行: `brew install --cask chromium`
   - これはIntelとApple Silicon（M1/M2/M3）両方のMacで動作します

2. **直接ダウンロード**:
   - 公式Chromiumサイトにアクセスし、Mac用の最新ビルドをダウンロード
   - 解凍してアプリケーションをApplicationsフォルダにドラッグ

3. **開発者やカスタムビルド向け**:
   - Woolyssなどのツールを使用してプレビルド版を入手するか、必要に応じてソースからビルド（Xcodeが必要）

インストール後、システム設定 > デスクトップとDock > デフォルトのWebブラウザでChromiumをデフォルトブラウザに設定できます。

[Chromiumをダウンロード](https://www.chromium.org/getting-involved/download-chromium/)  
[Homebrew Formula](https://formulae.brew.sh/cask/chromium)  
[Apple Siliconへのインストール](https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i)  
[MacUpdateダウンロード](https://chromium.macupdate.com/)  
[最新リリース](https://chromium.woolyss.com/download/en/)