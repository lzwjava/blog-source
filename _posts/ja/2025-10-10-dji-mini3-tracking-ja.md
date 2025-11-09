---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: DJI Mini 3 のトラッキング制限と回避策
translated: true
type: note
---

DJI Mini 3（ベースモデル）には、動く車の写真や動画を自動で追跡したり上空でホバリングしたりするためのActiveTrack（視覚的物体追従）やFollow Meモード（GPSベースの追跡）といった組み込み機能はありません。これはハイエンドのDJIドローンと比較した際の重要な制限事項です。ただし、DJI Mini 3 ProはActiveTrackをサポートしており、ドローンのカメラを使用して車、人、乗り物などの被写体を後方から、上方から、またはその他の位置から視覚的に追跡・追従することができます。これにより、ドローンが設定された距離と高度を維持しながら、動的なショットを撮影することが可能です。

カスタム開発に関するAPIについて：
- DJIのMobile SDK（Android/iOSアプリ向け）はMini 3シリーズをサポートしており、仮想スティックコマンド（位置/速度を手動で調整する場合など）やウェイポイントミッションのような基本的な飛行制御が可能です。車からのリアルタイムのGPSデータ（Bluetooth、コンパニオンアプリ、または外部トランスミッター経由）を統合すれば、車の経路をドローンに追従させるカスタムアプリを構築できます。これは「プラグアンドプレイ」の視覚的追跡ではありませんが、オフセット（例：後方10-20メートル、上方50メートル）を計算することで、上空や後方からの追跡を近似させることができます。
- しかし、SDKのActiveTrackミッションAPI（自動視覚追従用）は、Mini 3またはMini 3 Proでは**サポートされていません**。これらはMavic Air 2やAir 2Sなどの旧モデルに限定されています。
- 飛行中の写真撮影については、SDKのカメラAPIを使用して、タイマー、距離、または独自のロジックに基づいて自動的にシャッターを切ることができます。

サードパーティ製アプリ（内部でSDKを利用しているもの）を使用できる場合：
- DronelinkやLitchiのようなアプリは、あなたのスマートフォンのGPS（または外部デバイス）を使用して、Mini 3で基本的な「Follow Me」モードを有効にすることができます。特定の車を追跡するには、車両上のGPSビーコン（例：スマートフォンのホットスポット経由、またはアプリにデータを供給するTileやAirTagの代替となる専用トラッカー）とペアリングする必要があります。このセットアップは、道路やトレイルで車を追跡するユーザーによって機能しており、ドローンは上空に留まったり後方を追従したりして映像を撮影します。

法的/安全上の注意点を念頭に置いてください：動く車両のドローン追跡は、現地の規制（例：米国のFAA規則では目視範囲内の運用が必須、目視範囲外の操作は禁止）に準拠する必要があります。障害物を避けるために開放された地域でテストを行ってください。また、Mini 3の軽量設計は高速追跡時の耐風性を制限します。

### 参考文献
- [DJI Mini 3 Active Track HACK DJI Mini 3 Follow Me](https://www.youtube.com/watch?v=UYzSdd3iJwA)
- [Does the mini 3 have ai tracking to follow objects like cars](https://www.facebook.com/groups/djimini3ukowners/posts/2726498670890510/)
- [Can someone explain follow me mode? And if it's on mini 3?](https://www.reddit.com/r/dji/comments/13pqbw7/can_someone_explain_follow_me_mode_and_if_its_on/)
- [DJI Mini 3 / Mini 3 Pro - Follow Me Mode With Dronelink](https://www.youtube.com/watch?v=Rhneo8QoXV0)
- [DJI Product SDK Compatibility](https://support.dji.com/help/content?customId=01700000763&spaceId=17&re=US&lang=en&documentType=&paperDocType=ARTICLE)
- [DJI has released MSDK 5.3.0 with support for Mini 3 Pro and Mini 3](https://forum.flylitchi.com/t/dji-has-released-msdk-5-3-0-with-support-for-mini-3-pro-and-mini-3/9512)
- [class ActiveTrackOperator - DJI Mobile SDK Documentation](https://developer.dji.com/api-reference/android-api/Components/Missions/DJIActiveTrackMissionOperator.html)