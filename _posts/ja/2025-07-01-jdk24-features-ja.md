---
audio: false
generated: true
lang: ja
layout: post
title: JDK 24：主な機能とアップデート
translated: true
type: note
---

### JDK 24 の紹介

Java Development Kit (JDK) 24 は、Java SE (Standard Edition) プラットフォームの機能リリースであり、Java Community Process の JSR 399 で規定されたバージョン 24 のリファレンス実装として、2025年3月18日に正式にリリースされました。これは Oracle の6か月ごとのリリースサイクルを継続するもので、開発者の生産性、パフォーマンス、セキュリティを向上させる堅牢な拡張機能を提供します。JDK 24 には 24 の JDK Enhancement Proposals (JEP) が含まれており、これは2018年に時間ベースのリリーススケジュールが始まって以来最も多い機能数であり、Java の進化における重要なマイルストーンとなっています。これは、2025年9月に予定されている次の長期サポート (LTS) リリースである JDK 25 への足がかりとなります。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://openjdk.org/projects/jdk/24/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### 長期サポート (LTS) ステータス

JDK 24 は、**長期サポート (LTS) リリースでは**ありません。これは短期サポートリリースであり、Oracle からのプレミアレベルサポートは 2025年9月までの6か月間のみ受けられます。その後、JDK 25 に置き換えられます。対照的に、JDK 21 (2023年9月) や今後の JDK 25 (2025年9月) などの LTS リリースは、少なくとも5年間のプレミアサポートを受けるため、エンタープライズの安定性にとって望ましい選択肢となります。Oracle の LTS サイクルは2年ごとに発生し、JDK 21 が最新の LTS、JDK 25 が次の LTS となる予定です。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)

### リリースと安定性

JDK 24 は、**安定した、プロダクションレディなリリース**であり、2025年3月18日に一般提供 (GA) 開始となりました。プロダクションレディなバイナリは、Oracle No-Fee Terms and Conditions (NFTC) および OpenJDK の GNU General Public License (GPLv2) に基づき Oracle から利用可能であり、他のベンダーのバイナリも続いて提供されます。このリリースには、24の JEP に加えて 3,000 以上のバグ修正と小さな拡張が含まれており、一般的な使用における安定性を確保しています。ただし、非 LTS リリースであるため、長期的な安定性を必要とするエンタープライズというよりも、新しい機能をテストしたい開発者を主な対象としています。[](https://openjdk.org/projects/jdk/24/)[](https://www.theregister.com/2025/03/18/oracle_jdk_24/)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)

### JDK 24 の新機能

JDK 24 は 24 の JEP を導入し、コアライブラリの拡張、言語の改善、セキュリティ機能、HotSpot JVM の最適化、Java ツールに分類されます。このうち、14 が恒久機能、7 がプレビュー機能、2 が実験的機能、1 がインキュベータモジュールです。以下に、開発者とデプロイメントに関連する最も注目すべき機能の一部を示します：

1.  **Stream Gatherers (JEP 485)** - 恒久
    - `Gatherer` インターフェースを導入して Stream API を強化し、開発者がストリームパイプライン用のカスタム中間操作を定義できるようにします。これにより、終端操作用の既存の `Collector` インターフェースを補完する、より柔軟なデータ変換が可能になります。
    - 例: `StreamGatherers.groupBy` を使用した単語の長さによるグループ化。
    - 利点: 開発者にとって複雑なストリーム処理を簡素化します。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

2.  **Ahead-of-Time Class Loading & Linking (JEP 483)** - 実験的
    - Project Leyden の一部であり、準備段階でクラスをキャッシュに事前ロードおよびリンクすることで、Java アプリケーションの起動時間を短縮します。このキャッシュは実行時に再利用され、コストのかかるクラスロードステップをバイパスします。
    - 利点: クラウドおよびマイクロサービスアプリケーションのパフォーマンスを向上させます。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

3.  **Compact Object Headers (JEP 450)** - 実験的
    - Project Lilliput の一部であり、64ビットアーキテクチャ上の Java オブジェクトヘッダーサイズを 96–128 ビットから 64 ビットに削減し、ヒープ使用量を減らし、メモリ効率を向上させます。
    - 利点: メモリフットプリントを削減し、データの局所性を高めてパフォーマンスを向上させます。[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)[](https://www.happycoders.eu/java/java-24-features/)

4.  **Generational Shenandoah Garbage Collector (JEP 404)** - 恒久
    - Shenandoah GC の世代別モードを実験的段階から製品機能へ移行し、オブジェクトを新世代と旧世代に分けることで、スループット、負荷スパイクへの耐性、メモリ使用率を改善します。
    - 利点: 要求の厳しいワークロードのパフォーマンスを向上させます。[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3846172/jdk-25-the-new-features-in-java-25.html)

5.  **Module Import Declarations (JEP 494)** - 第二プレビュー
    - モジュールによってエクスポートされたすべてのパッケージを `module-info.java` ファイルを必要とせずに直接インポートできるようにすることで (例: `import module java.sql;`)、モジュラープログラミングを簡素化します。
    - 利点: 軽量アプリケーションとスクリプティングのオーバーヘッドを削減し、初心者と迅速なプロトタイピングを支援します。[](https://codefarm0.medium.com/java-24-features-a-deep-dive-into-whats-coming-81e77382b39c)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

6.  **Flexible Constructor Bodies (JEP 492)** - 第三プレビュー
    - `super()` または `this()` 呼び出しの前にコンストラクタ内でステートメントを許可し、補助メソッドなしで、フィールド初期化ロジックをより自然に配置できるようにします。
    - 利点: 特にサブクラス化において、コードの信頼性と可読性を向上させます。[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

7.  **Key Derivation Function (KDF) API (JEP 487)** - プレビュー
    - HMAC-based Extract-and-Expand や Argon2 などの暗号鍵導出関数のための API を導入し、安全なパスワードハッシュと暗号ハードウェアとの連携をサポートします。
    - 利点: 高度な暗号化を必要とするアプリケーションのセキュリティを強化します。[](https://www.jrebel.com/blog/whats-new-java-24)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

8.  **Permanently Disable the Security Manager (JEP 486)** - 恒久
    - JDK 17 で非推奨となった Security Manager を、もはや Java アプリケーションを保護する主要な手段 (コンテナベースのサンドボックスに置き換えられた) ではないため、削除します。
    - 注意: Security Manager に依存するアプリケーションは、アーキテクチャの変更が必要になる可能性があります。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

9.  **Late Barrier Expansion for G1 Garbage Collector (JEP 464)** - 恒久
    - バリアの展開をコンパイルパイプラインの後半に移動することで G1 GC のバリア実装を簡素化し、コンパイル時間を短縮し、保守性を向上させます。
    - 利点: G1 GC を使用するアプリケーションのパフォーマンスを向上させます。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

10. **Quantum-Resistant Cryptography (JEP 452, 453)** - プレビュー
    - Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) と Digital Signature Algorithm (ML-DSA) を導入し、量子コンピューティング攻撃から保護します。
    - 利点: ポスト量子時代のセキュリティに向けて Java アプリケーションを将来性のあるものにします。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

11. **Scoped Values (JEP 480)** - 第四プレビュー
    - スレッドローカル変数よりも安全に、スレッド内およびスレッド間で不変データを共有できるようにします。これにより、並行性の扱いが改善されます。
    - 利点: 並行コードについての推論を簡素化します。[](https://www.jrebel.com/blog/whats-new-java-24)

12. **Deprecate 32-bit x86 Port (JEP 501)** - 恒久
    - 32ビット x86 ポートを JDK 25 での削除を目指して非推奨とし、アーキテクチャに依存しない Zero ポートを 32ビットシステム向けの代替とします。
    - 利点: メンテナンスのオーバーヘッドを削減し、現代のアーキテクチャに焦点を当てます。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

13. **Vector API (JEP 489)** - 第九インキュベータ
    - SIMD プログラミングのための Vector API を改良し続け、クロスレーン操作と算術演算の拡張を行います。
    - 利点: 計算集約型アプリケーションのパフォーマンスを向上させます。[](https://www.infoq.com/news/2025/02/java-24-so-far/)

14. **Linking Run-Time Images without JMODs (JEP 493)** - 恒久
    - `jlink` ツールが JMOD ファイルなしでカスタムランタイムイメージを作成できるようにし、JDK サイズを約 25% 削減します。
    - 利点: カスタム Java ランタイムのデプロイメント効率を向上させます。[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### 追加注記

-   **プレビューおよび実験的機能**: Scoped Values や KDF API など、多くの機能はプレビューまたは実験的段階にあり、開発者はそれらが JDK 25 以降で恒久的になる前にテストし、フィードバックを提供できます。これらは最終決定前に変更される可能性があります。[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoq.com/news/2025/02/java-24-so-far/)
-   **プロジェクト統合**: JDK 24 は、Leyden (起動最適化)、Lilliput (メモリ効率)、Panama (ネイティブ相互運用性) などの OpenJDK プロジェクトの要素を導入し、将来の拡張の基盤を築いています。[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)
-   **セキュリティと非推奨化**: Security Manager の削除や 32ビット x86 ポートの非推奨化などの機能は、時代遅れのコンポーネントを段階的に廃止することで Java を近代化するという Oracle の焦点を反映しています。[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### 結論

JDK 24 は、Java のパフォーマンス、開発者の生産性、セキュリティを前進させる、安定した機能豊富なリリースです。LTS リリースではありませんが、その 24 の JEP は重要な改善を提供し、その多くは今後の LTS リリースである JDK 25 で最終決定される予定です。開発者は、Stream Gatherers や Module Import Declarations などの機能を活用して即座に生産性を高めることができ、Compact Object Headers や Ahead-of-Time Class Loading などの実験的機能は、現代のワークロードに向けた Java の継続的な最適化を示しています。エンタープライズでの使用には、延長サポートが受けられる JDK 21 のような LTS リリースを継続使用するか、JDK 25 を待つことが推奨されます。[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

詳細については、以下をご覧ください：
-   [Oracle JDK 24 リリースノート](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)
-   [OpenJDK JDK 24](https://openjdk.org/projects/jdk/24/)[](https://openjdk.org/projects/jdk/24/)
-   機能のハイライトについては [JavaOne 2025 カンファレンス](https://www.oracle.com/javaone) [](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)