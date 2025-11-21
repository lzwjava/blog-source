---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphere 9.0と8.0の主な相違点
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 9.0 と 8.0 の主な違い

IBM WebSphere Application Server (WAS) は、エンタープライズグレードの Java EE アプリケーションサーバーです。バージョン 8.0 (2011年リリース) では Java EE 6 準拠が導入され、バージョン 9.0 (2017年リリース) では Java EE 7 に進化し、Liberty のような軽量でクラウドフレンドリーなランタイムに合わせて従来型プロファイルを近代化することに焦点が当てられました。以下では、公式 IBM ドキュメントとリリースノートに基づき、Java サポート、標準準拠、アーキテクチャ、デプロイメントにおける主な違いを明確にするために表で概要を説明します。

| 観点                      | WAS 8.0                                                                 | WAS 9.0                                                                 |
|---------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Java SE サポート**      | デフォルトは Java SE 6。設定により Java SE 7 をオプションでサポート。 | 主要プラットフォームとして Java SE 8 をデフォルトとし、Oracle Java 8 との完全な互換性のために IBM SDK Java 8 を使用。これにより、ラムダ式、ストリーム、その他の SE 8 機能が利用可能。 |
| **Java EE 準拠**          | JPA 2.0、JSF 2.0、Servlet 3.0 を含む、完全な Java EE 6 サポート。       | WebSocket 1.0、JSON-P 1.0、Batch 1.0、強化されたコンカレンシーユーティリティなどの機能を追加した、完全な Java EE 7 サポート。これにより、従来型エディションが以前のバージョンの Liberty の機能と同等になる。 |
| **Liberty プロファイル統合** | Liberty は 8.5 で導入 (8.0 のコアにはなし)。8.0 は従来型のフルプロファイルのみに焦点。 | 軽量でモジュール式のフルプロファイル代替として、クラウドネイティブアプリ向けに最適化された Liberty ランタイム (バージョン 16.0.0.2) を深く統合。Liberty はバンドルされ、継続的デリバリーをサポート。 |
| **デプロイメントモデル**    | 主にオンプレミス。Installation Manager 経由でインストール。Base および Network Deployment (ND) エディションでクラスタリングを提供。 | オンプレミス版と IBM Cloud 上の as-a-Service 版が同時リリースされた最初のバージョン。優れたコンテナ化フックによるハイブリッドクラウドデプロイメントをサポート。 |
| **パフォーマンスと管理**  | WAS 7 比で最大 20-26% のスループット向上。ND エディションでのインテリジェントな管理。 | 8.0 を基盤とし、リソース効率のためのさらなる最適化。移行と設定比較のための強化された管理ツール。 |
| **サポート終了**          | 延長サポートは 2019 年に終了。修正は提供されない。                      | 少なくとも 2027 年までアクティブサポート。定期的なフィックスパック (例: 9.0.5.x) でセキュリティと互換性に対応。 |
| **移行に関する考慮事項**  | N/A (ベースライン)。                                                    | Configuration Comparison Tool などのツールによる 8.x からの容易な移行。自動ポート調整および非推奨 API の扱いによる Java SE 8 への移行サポート。 |

#### 主なポイント
- **最大の進化**: Java EE 7 および Java SE 8 への移行が最も重要であり、以前に Liberty で先行導入されていたモダンな Java 機能と標準が利用可能になります。レガシーな Java EE 6 アプリケーションを実行している場合、9.0 への移行は straightforward ですが、SE 8 固有の変更に対するテストが必要になる場合があります。
- **アップグレードの判断**: クラウド/ハイブリッドのニーズや EE 7 機能が必要な場合は 9.0 を選択。古いアプリケーションの短期的なメンテナンスのみの場合は 8.0 (または 8.5.5 にパッチ適用) に留まります。
- 詳細な移行ガイドについては、IBM の公式ドキュメントを確認してください。

**参考文献**:
- [IBM WebSphere Application Server Wikipedia](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)
- [Java SE 8 in WAS Traditional V9](https://www.ibm.com/docs/en/was/9.0.5?topic=waso-java-se-8-in-websphere-application-server-traditional-v9)
- [WAS Version Comparison Slides](https://www.slideshare.net/ejlp12/ibm-websphere-application-server-version-to-version-comparison)
- [WAS Configuration Comparison Tool](https://www.ibm.com/support/pages/websphere-application-server-configuration-comparison-tool)