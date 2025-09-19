---
audio: false
generated: false
image: false
lang: ja
layout: post
title: LZAlbumは
translated: true
---

これは GitHub プロジェクト [https://github.com/lzwjava/LZAlbum](https://github.com/lzwjava/LZAlbum) の README.md です。

---

# LZAlbum

これは、LeanCloud の Moments 機能を基に、LeanCloud 上での一対一および一対多の関係のモデリング方法を示しています。

![album](https://cloud.githubusercontent.com/assets/5022872/9563818/dd9588ba-4ec3-11e5-940a-3d1e84b967f0.gif)

# サポート

使用中に問題が発生した場合は、[issue](https://github.com/lzwjava/LZAlbum/issues) を作成してください。GitHub で対応いたします。

# 実行方法
```
   pod install --no-repo-update --verbose （ライブラリが見つからないエラーが発生した場合は、--no-repo-update を削除してください）
   open LZAlbum.xcworkspace
```

# クレジット

UI デザインは [MessageDisplayKit](https://github.com/xhzengAIB/MessageDisplayKit) を参考にしています。データは LeanCloud に保存されています。両方に感謝します。

# バックエンド

![image](https://cloud.githubusercontent.com/assets/5022872/7449102/2390131e-f260-11e4-8978-cead60e2f272.png)

https://leancloud.cn で公開アカウントでログインし、認証情報: leancloud@163.com/Public123 を入力し、LCAlbum アプリを選択してテーブル構造を確認してください。
**注意: バックエンドのデータを変更しないでください。ただ見るだけにしてください。そうしないと、クライアントがクラッシュする可能性があります。**
**注意: 上記の認証情報はこのアプリにログインするためのものではなく、LeanCloud バックエンド用のものです。アプリのログインは、登録ページで新しいアカウントを登録してください。**

# ドキュメント

[関連するドキュメント](https://leancloud.cn/docs/ios_os_x_guide.html)

# ライセンス
MIT