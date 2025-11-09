---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: iPerf3 ネットワーク帯域幅テストツール
translated: true
type: note
---

### iPerf3とは？

iPerf3は、ネットワーク帯域幅とパフォーマンスを測定するために設計されたオープンソースのコマンドラインツールです。2つのエンドポイント（1つがサーバー、もう1つがクライアントとして機能）間でトラフィックをシミュレートすることにより、IPネットワークで達成可能な最大スループットをテストするためによく使用されます。これにより、ローカルエリアネットワークや広域ネットワークにおける遅延、パケット損失、ボトルネックなどの問題の診断に役立ちます。

#### 主な機能：
- **対応プロトコル**: TCP、UDP、SCTPによる柔軟なテストシナリオ
- **カスタマイズ性**: バッファサイズ、テスト時間、双方向トラフィックなどのパラメータの調整が可能
- **出力**: 帯域幅、ジッタ、データグラム損失に関する詳細な統計を提供

#### 基本的な使用例：
2台のマシン間の帯域幅をテストするには：
1. サーバー側: `iperf3 -s`（サーバーを起動）
2. クライアント側: `iperf3 -c <サーバーのIPアドレス>`（接続し、デフォルトで10秒間のテストを実行）

軽量でクロスプラットフォーム（Linux、Windows、macOSで動作）であり、ネットワーク管理者、開発者、ITプロフェッショナルによってトラブルシューティングに広く使用されています。

#### 歴史：
iPerf3は、オリジナルのiPerfツールを完全に書き直したもので、2009年にESnet (Energy Sciences Network) によって開始され、2014年に最初にリリースされました。この再設計では、精度を向上させながら、より小さく保守しやすいコードベースを目指しました。

詳細については、公式サイトまたはGitHubリポジトリを確認してください。

### 参考文献
- [iPerf - The TCP, UDP and SCTP network bandwidth measurement tool](https://iperf.fr/)
- [iperf3: A TCP, UDP, and SCTP network bandwidth measurement tool](https://github.com/esnet/iperf)
- [Iperf - Wikipedia](https://en.wikipedia.org/wiki/Iperf)