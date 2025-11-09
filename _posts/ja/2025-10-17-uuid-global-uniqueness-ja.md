---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: UUIDによる調整不要のグローバル一意性保証
translated: true
type: note
---

UUIDは中央機関なしでグローバルに一意な識別を実現します。これは128ビットという膨大なアドレス空間（約3.4×10^38通りの可能な値）を持つためです。この数値は、現実世界のすべてのシステムで実際に生成されるUUIDの数を大幅に上回ります。バージョン4のUUID（共有されたランダムなUUIDなど）では、122ビットが高品質な乱数で埋められ、重複が事実上不可能となっています。

衝突について：理論上は2つのUUIDが同一になる可能性がありますが、その確率は極めて低く、実世界では無視できるレベルです。これは確率論の「誕生日のパラドックス」に従います：

- ランダムなバージョン4 UUID同士が衝突する確率は約2.71×10^18分の1です
- たった1組の重複が50%の確率で発生するには、約4.8×10^18個（地球上の全人口がそれぞれ6億個ずつ所有する量）のUUIDを生成する必要があります
- 参考までに、1兆個（10^12個）のUUIDを生成した場合でも、衝突リスクは約10億分の1以下です

異なるUUIDバージョンには追加の保護策があります：バージョン1はタイムスタンプとMACアドレスを使用し、バージョン5は名前空間を使用した名前のハッシュ化など。しかしバージョン4のランダム性だけでも、分散システム、データベース、または連携のないアプリケーションにおいて一意性を保証します。

[衝突確率の詳細](https://jhall.io/archive/2021/05/19/what-are-the-odds/)  
[UUID - Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)  
[Java UUID.randomUUIDの衝突確率](https://stackoverflow.com/questions/24876188/how-big-is-the-chance-to-get-a-java-uuid-randomuuid-collision)