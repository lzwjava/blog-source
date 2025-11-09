---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: RFC 4122 UUID仕様概要
translated: true
type: note
---

RFC 4122は、2005年7月にInternet Engineering Task Force (IETF)によって公開された技術仕様です。これはUniversally Unique Identifier (UUID) 、またの名をGlobally Unique Identifier (GUID) と呼ばれる識別子のためのUniform Resource Name (URN) 名前空間を定義しています。

UUIDは、識別子を管理する中央機関を必要とせずに、コンピュータシステム内の情報を一意に識別するために使用される128ビットの数値です。この標準は、5つのバージョンのUUID（例：タイムスタンプとMACアドレスに基づくバージョン1、ランダムビットに基づくバージョン4）、それらの生成方法、エンコーディング形式（ハイフン付きの16進数文字列: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` など）、およびプロトコルやアプリケーションでの使用に関するガイドラインを概説しています。これにより、異なるシステムやネットワーク間での相互運用性が保証されます。

この仕様は、データベースキー、セッションID、分散システムなど、ソフトウェア開発において広く採用されています。

[ RFC 4122 - A Universally Unique IDentifier (UUID) URN Namespace](https://datatracker.ietf.org/doc/html/rfc4122)  
[ Universally unique identifier - Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)