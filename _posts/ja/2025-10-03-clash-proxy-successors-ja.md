---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: クラスプロキシの後継とLinuxサポート
translated: true
type: note
---

Clashは、Shadowsocksと同様のルールベースのプロキシツールですが、2023年に中国での規制圧力により作者によってオリジナルのリポジトリが削除されました。コミュニティはフォークと後継プロジェクトを通じて開発を継続しており、その中でもClash.Meta（現在は正式にMihomoと呼ばれる）は、最も信頼性が高く、活発にメンテナンスされている代替プロジェクトとして広く認識されています。これはLinuxバイナリ（Ubuntu用を含む）をサポートし、DNS over HTTPS (DoH)、トンネリング、ルールベースのルーティングなどの機能を含みます。

Linux/Ubuntu用の信頼できるGitHubリポジトリについては、主要な継続プロジェクトを推奨します。コミュニティでの採用状況、更新頻度、Linuxサポートに基づくトップオプションの概要を以下に示します：

### 推奨リポジトリ
- **MetaCubeX/mihomo (Clash.Meta Core)**: これはClashの主要な後継プロジェクトで、オリジナル削除後にコミュニティによってフォークされメンテナンスされています。完全なプロキシ機能、頻繁な更新、Linux（x86_64およびarm64）向けのプリビルドバイナリを提供します。Ubuntu互換性は非常に高く、バージョン18.04以上でテストされたバイナリがあります。オープンソース、広告なし、YAML設定ファイルによる高いカスタマイズ性が特徴です。
  - GitHub: https://github.com/MetaCubeX/mihomo
  - 信頼性の理由: 14k以上のスター、活発なコミュニティ、ルーティング用のGeoIPデータベースを含むバイナリ。リリースセクションにLinux CLIバイナリの直接ダウンロードリンクあり。
  - Ubuntuへのインストール: リリースから最新の「mihomo-linux-amd64」バイナリをダウンロードし、実行可能にし(`chmod +x mihomo`)、実行します。プロキシルールを含むconfig.yamlファイルが必要です。[1][2]
  - コアが合わない場合の代替案:
    - **CarlDegio/verge**: Clash.Meta用のTauriベースのGUIラッパーで、Linux（Ubuntu含む）向けの直感的なダッシュボードを提供します。安定性のためにMihomoを基盤としています。
      - GitHub: https://github.com/CarlDegio/verge
      - 信頼性の理由: デスクトップ向けGUIサポート、2k以上のスター、簡単なプロファイル切り替え、システムトレイアイコン。Ubuntu用はAppImageをダウンロード。[3]
    - **chen08209/FlClash**: Clash.Metaベースのマルチプラットフォームクライアント（Linuxバイナリ含む）。シンプルさと広告なしの設計に焦点を当て、設定用のシンプルなインターフェースを備えています。
      - GitHub: https://github.com/chen08209/FlClash
      - 信頼性の理由: 軽量、deb/AppImageビルドによるUbuntuサポート、Mihomoバインディングを統合。[4]
  - レガシーバックアップ用: Kuingsmile/clash-coreは、削除前のコアのアーカイブビルドを提供しており、メンテナンスされていないが歴史的なバージョンを希望する場合にLinuxダウンロード用のリリースがあります。[5]

### 追加注記
- **インストールのヒント**: Ubuntuではlibc (glibc 2.17+) がインストールされていることを確認してください。`systemd`や`screen`などのツールを使用して、バックグラウンドサービスとして実行します。セキュリティのため、SHA256ハッシュによるダウンロード検証を行ってください。
- **信頼性の基準**: これらのリポジトリは、活発なコントリビューション、大規模なユーザーベース（高いスター/フォーク数）、2023年以降の放棄されたプロジェクトのリスクを回避しています。Clash.Premin（おそらくPremiumの誤記）は有料のフォークですが、オープンソース中心ではありません。
- **法的/使用上の注意**: Clashは検閲回避のために使用されます。制限のある地域では使用により注意を引く可能性があるため、現地の法律への準拠を確認してください。
- UIや特定の機能（例: マルチプラットフォーム）が必要な場合は、コアのMihomo CLIよりもvergeやFlClashの方がユーザーフレンドリーです。詳細については、各リポジトリのREADMEを確認してください。問題が発生した場合は、Mihomoリポジトリに詳細なドキュメントがあります。[6][7][1][8]

どれも合わない場合、またはUbuntu用のステップバイステップガイドが必要な場合は、詳細を提供してください！

引用:
[1] https://github.com/djoeni/Clash.Meta
[2] https://discussion.fedoraproject.org/t/rhbz-2305079-review-request-clash-meta-a-rule-based-network-proxy-tool-aka-mihomo/146312
[3] https://github.com/CarlDegio/verge
[4] https://github.com/chen08209/FlClash
[5] https://github.com/Kuingsmile/clash-core/releases
[6] https://github.com/fengwz17/Clash-For-Ubuntu
[7] https://news.ycombinator.com/item?id=38126160
[8] https://github.com/hiddify/Clash.Meta