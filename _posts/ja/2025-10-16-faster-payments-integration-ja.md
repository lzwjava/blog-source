---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 高速決済システム統合ガイドライン
translated: true
type: note
---

香港の高速決済システム（FPS）は、香港金融管理局（HKMA）の監督下で香港銀行間決済有限公司（HKICL）によって運営されており、銀行が統合するための公開SDKを提供していません。統合はFPSインフラへの直接接続によって処理され、技術仕様は参加銀行（決済参加行）に対してオンボーディングプロセス中に非公開で共有されます。これらの仕様は銀行がアクセス用にシステムを強化するための指針となりますが、公式文書で言及されている既製のSDKや開発者キットは存在しません。

APIに関して、FPS自体は現在、外部またはサードパーティ統合のための専用APIを提供していません。しかし、FPSは香港銀行セクター向けのHKMAの広範なオープンAPIフレームワーク（2018年に導入され2025年まで段階的に更新）に沿っており、銀行が特定の機能をサードパーティサービスプロバイダー向けにAPIを通じて公開することを奨励しています（例：口座情報や支払い開始）。FPS取引は支払い開始などの機能に対して間接的にこのフレームワークを活用できますが、FPS固有のAPIはまだ利用できず、セキュリティと規制上の理由からアクセスは必要に応じて制限されたままです。HKMAは継続的に監視し、将来的にAPIサポートを拡大する可能性があります。

### 銀行向け主要統合詳細
- **接続方法**: 銀行はリアルタイムモードではIBM MQメッセージングを、バッチモードではファイル転送（例：HKICLの安全なICLNETネットワーク経由）を介して接続します。システムは24時間365日稼働します。
- **メッセージング標準**: 全ての通信はISO 20022形式を使用し、豊富なデータ、中国語文字、相互運用性をサポートします。
- **オンボーディングプロセス**: 銀行はHKMA（香港ドル建て）または中国銀行（香港）（人民元建て）に登録し、FPS規則契約に署名し、提供された仕様にシステムを適合させ、HKICLのテストを経て稼働開始します。全ての認可銀行は直接決済参加行として参加する必要があります。
- **その他の機能**: プロキシID（電話番号/メールアドレスなど）、QRコード（EMV標準）、多通貨（香港ドル/人民元）送金をサポートします。認証はHKMAの二要素認証ガイドラインに従い、取引限度額は各行が独自に設定します。

詳細な技術仕様については、銀行は登録時にHKICLに直接問い合わせる必要があります。これらは公開ダウンロード可能ではありません。

[高速決済システム（FPS） - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/financial-market-infrastructure/faster-payment-system-fps/)  
[スキーム文書 - HKICL FPS](https://fps.hkicl.com.hk/eng/fps/about_fps/scheme_documentation.php)  
[世界銀行FPSケーススタディ：香港](https://fastpayments.worldbank.org/sites/default/files/2021-09/World_Bank_FPS_Hong_Kong_SAR_China_FPS_Case_Study.pdf)  
[銀行セクター向けオープンAPIフレームワーク - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/fintech/open-application-programming-interface-api-for-the-banking-sector/)