---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4.1-fast
title: Spring BootがLibertyを追い越した
translated: true
type: note
---

IBM WebSphere Application Server Liberty Profile（略称WLPまたは単にLiberty）は、IBMが2012年から2013年頃に開始した、重量級の従来型WebSphere Application Server（WAS）を近代化する試みであり、軽量で構成可能なクラウド対応のJakarta EE（旧Java EE）ランタイムです。技術的に堅牢で一部の領域では優れているものの（高速起動、低メモリフットプリント、Open Libertyによる優れたMicroProfileサポート）、**2010年代半ば以降の新しいJava Web/マイクロサービス開発において、LibertyはSpring Bootの人気競争に「敗北」** しました。

### Spring BootがLibertyを支配した主な理由

| 理由 | Spring Bootの利点 | Liberty / 従来型アプリケーションサーバーの欠点 |
|--------|-----------------------|-------------------------------------------|
| **開発者の生産性と使いやすさ** | 設定より規約、自動設定、組み込みサーバー（デフォルトでTomcat/Jetty/Undertow）、`spring-boot-starter-*`によるボイラープレートの排除。数分でのゼロ設定のプロダクションレディアプリ。 | 完全版WASより軽量とはいえ、依然としてserver.xmlの設定、フィーチャーの有効化、より手動でのセットアップが必要。多くの開発者にとって「旧来的」に感じられる。 |
| **スタンドアロン実行可能モデル** | 組み込みサーバーを含むFat JAR / uber-JAR → `java -jar`でどこでも実行可能、Docker/KubernetesやDevOpsに最適。外部サーバー管理不要。 | 主にWAR/EARをデプロイする別個のサーバー（後期に実行可能JARサポートを追加したが、後付け感があり、デフォルトのワークフローにはならなかった）。 |
| **エコシステムとコミュニティ** | 大規模なオープンソースコミュニティ（Pivotal/VMware）、多数のサードパーティスターター、優れたドキュメント、Stack Overflowでの回答、チュートリアル。 | 小規模なコミュニティ；主にIBMのドキュメントと有償サポート。既成の統合ソリューションが少ない。 |
| **タイミングとマインドシェア** | Spring Boot 1.0は2014年にリリース - マイクロサービス、Docker、クラウドネイティブが爆発的に普及した時期と完全に一致。新しいJavaサービスのデファクトスタンダードとなった。 | Libertyは早期（2012-2013年）に登場したが、開発者が重量級の商用サーバー（WebSphere, WebLogic）から離れつつある時期に、「IBMのアプリケーションサーバー」という認識が残った。 |
| **ベンダー中立性とコスト** | 完全無料のオープンソース、ベンダーロックインの懸念なし。 | IBM製品 → 高額なライセンスの印象（Liberty Coreに無料ティアがあり、Open Libertyは完全オープンソースだが、従来型WASからのブランドイメージが重荷となった）。 |
| **マイクロサービスとクラウド適合性** | 初日からマイクロサービス向けに設計；アクチュエーター、ヘルスチェック、外部化設定、容易な12-factorアプリ。 | 非常にクラウドフレンドリー（特にOpen Liberty）だが、多くの開発者はLibertyの強みを知る前にSpring Bootを選択していた。 |
| **市場の勢い** | 2018年から2020年頃までに、調査ではTomcat（Spring Bootに組み込み）がJavaランタイムの約60%のシェアを占め、全てのフルアプリケーションサーバーを合わせたものを凌駕。2025年現在、Spring Bootは18,000以上の既知企業で使用；従来型アプリケーションサーバーはニッチ。 | Liberty/Open LibertyはIBMが強みを持つ企業やJakarta EE/MicroProfileでは人気を保つが、新規開発での採用ははるかに遅れている。 |

### Libertyが依然として優位な領域（ニッチなケース）
- Spring依存のない純粋なJakarta EE / MicroProfileアプリケーション。
- IBMスタックに既にロックインされている企業（Red Hat OpenShift with WebSphereライセンス、IBM Cloud Pak）。
- 最適化されたSpring Bootデプロイメント（一部のベンチマークでは、Libertyは組み込みTomcatよりも小さなDockerイメージと高いスループットでSpring Bootアプリを実行可能）。
- 商業サポート/認証が必要な規制産業。

要約すると、**Libertyが技術的に劣っていたために負けたのではなく、Spring Bootが劇的に高い開発者生産性を提供し、完璧な文化的瞬間に登場し、止められないエコシステムの勢いを構築したために負けたのです。** 2025年現在、ほとんどの新しいJavaバックエンドプロジェクトは、別個のアプリケーションサーバーではなく、Spring Boot（またはQuarkus/Helidon/Micronaut）で開始されます。

[Spring Boot vs Websphere Liberty | 違いは何ですか？](https://stackshare.io/stackups/spring-boot-vs-websphere-liberty)  
[2020 Java Technology Report | JRebel](https://www.jrebel.com/blog/2020-java-technology-report)  
[How does Open Liberty’s performance compare to other cloud-native Java runtimes](https://openliberty.io/blog/2022/10/17/memory-footprint-throughput-update.html)  
[Spring Boot market share data (6sense)](https://6sense.com/tech/programming-framework/spring-boot-market-share)