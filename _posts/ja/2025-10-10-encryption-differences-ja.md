---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 対称暗号と非対称暗号の違い
translated: true
type: note
---

### 対称アルゴリズム
対称アルゴリズムは、対称鍵暗号とも呼ばれ、データの**暗号化（スクランブル）と復号（アンスクランブル）の両方に同じ秘密鍵**を使用します。これにより、大量のデータを高速かつ効率的に処理できますが、課題は傍受されることなく関係者間で鍵を安全に共有することです。

- **例**: AES (Advanced Encryption Standard)、DES (Data Encryption Standard)
- **長所**: 高速、計算オーバーヘッドが小さい
- **短所**: 鍵の配布と管理にリスクがある

### 非対称アルゴリズム
非対称アルゴリズムは、一般に非対称暗号または公開鍵暗号と呼ばれ、**関連する鍵のペア**を使用します：公開鍵（暗号化用に自由に共有）と秘密鍵（復号用に秘密に保持）。これにより、単一の鍵を安全に交換する必要がなくなります。

- **例**: RSA、ECC (Elliptic Curve Cryptography)
- **長所**: 安全な鍵交換、デジタル署名と否認防止をサポート
- **短所**: 対称方式よりも低速でリソースを多く消費する

### 主な違い

| 観点              | 対称                           | 非対称                         |
|---------------------|------------------------------------|-------------------------------------|
| **鍵の使用方法**      | 暗号化/復号に1つの鍵を使用        | 公開鍵で暗号化、秘密鍵で復号 |
| **速度**          | より高速                            | より低速                             |
| **セキュリティ**       | 鍵の秘密性に依存            | 数学的な問題の困難さに依存（例：大きな素数の因数分解） |
| **使用例**      | バルクデータの暗号化（例：ファイルストレージ） | 安全な通信の確立（例：HTTPSハンドシェイク）、デジタル証明書 |

実際には、これらは組み合わせて使用されることが多いです：初期の鍵交換に非対称方式を、実際のデータ転送に対称方式を使用します（例：TLS/SSL）。

詳細は、以下を参照してください：
- [Symmetric vs Asymmetric Encryption - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-symmetric-and-asymmetric-key-encryption/)
- [Symmetric and Asymmetric Encryption - AWS](https://aws.amazon.com/what-is/symmetric-encryption/)