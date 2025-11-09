---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ウルル以外のLeanCloud API
translated: true
type: note
---

いいえ、LeanCloudは公開APIを「Uluru API」とは呼んでいません。公式APIはLeanCloud REST API（データストレージ、クエリなど）、Cloud Engine REST API（サーバーサイド機能とフック）、そしてプッシュ通知やファイルストレージなどのサービス固有のエンドポイントとして提供されています。これらは開発者サイト（docs.leancloud.cn）で広範に文書化されており、「Uluru」への言及は一切ありません。

しかし、「Uluru」は同社の製品やSDK開発に関連する内部または初期のコードネームであったようです。これは、**uluru-js-sdk**（バージョン0.1.0、約12年前に「avos」パブリッシャーアカウントで公開）というアーカイブされたnpmパッケージに基づいています。AVOS Cloudはブランド変更前のLeanCloudの元の名称であり、このパッケージは「PAAS（Platform as a Service）向けJavaScript SDK」と説明されており、LeanCloudのバックエンドサービスと一致しています。これはブラウザとNode.js環境の両方をサポートし、データ操作などのコア機能を提供します（LeanCloudの初期サービスに合致）が、主要なSDKとして公に宣伝されることはありませんでした。現在のSDKは「LeanCloud SDK」（Java、Python、JavaScriptなど向け）としてブランド化され、GitHubのleancloud/で公開されています。

これがより最近または特定のもの（例：非公開/内部ツール）を指す場合、公的文書にはありません。公式APIの詳細については、[LeanCloud Docs](https://docs.leancloud.cn/en/)を確認してください。