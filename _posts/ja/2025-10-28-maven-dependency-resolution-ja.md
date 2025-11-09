---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Mavenマルチモジュール依存関係解決
translated: true
type: note
---

はい、その通りです。Mavenのマルチモジュールプロジェクトにおいて、あるモジュール（例: EARモジュール）が別のモジュール（例: WARモジュール）に依存している場合、Mavenはデフォルトで他のモジュールの`target/`ディレクトリから直接ではなく、ローカルの`.m2/repository`から依存関係を解決します。これは、Mavenがモジュール間の依存関係を標準的なアーティファクト参照（外部ライブラリのように）として扱うためであり、依存するアーティファクトはインストールされている（あるいは、少なくともパッケージ化され、ビルドリアクターを介して発見可能である）必要があるからです。

### この挙動が起こる理由
- **ローカルリポジトリ解決**: Mavenの依存関係解決メカニズムは、まずローカルリポジトリ内でアーティファクトを探します。`target/`ディレクトリは単一モジュールのビルド中に一時的に使用されるのみで、モジュール間参照の場合は、アーティファクトが「公開」されている（インストールされている）ことを期待します。
- **リアクタービルドは役立つが、常に十分とは限らない**: **親POM**のルートから`mvn package`（または`mvn install`）を実行すると、Mavenのリアクターは自動的にモジュールをトポロジカル順序でビルドします。これは、セッション中に他のモジュールの新しい`target/`出力から取得することで、明示的なインストールを必要とせずにモジュール間の依存関係をその場で解決します。しかし、依存モジュール（例: EAR）を**個別に**ビルドする場合（例: `cd ear-module && mvn package`）、それはWARの`target/`を認識せず、WARアーティファクトが既に`.m2`に存在しない限り失敗します。

### WARからEARへのパッケージングに特化して
EARプロジェクトでは:
- EARプラグイン (`maven-ear-plugin`) は、EARアーカイブ（例: EAR POM内の`<modules>`を介して）に含めるための解決済みアーティファクトとして、WAR（および他のモジュール）を期待します。
- WARがインストールされていない場合、「Could not resolve dependencies」のようなエラーや、EAR内のモジュール不足が発生します。

**解決策**: 個別にビルドする場合は、一般的に、「元の」（依存先の）モジュールに対して最初に`mvn install`（または、少なくともフルリアクタービルドでの`mvn package`）を実行する必要があります。ベストプラクティス:
1.  **推奨: 親からビルド**: プロジェクトルートで`mvn clean install`を実行します。これにより、すべてが`.m2`にインストールされ、順序が自動的に処理されます。
2.  **モジュールを個別にビルドする場合**:
    - `cd war-module && mvn clean install` (WAR JARを`.m2`にインストール)。
    - その後、`cd ear-module && mvn clean package` (または`install` — EARは多くの場合`package`のみで十分)。
3.  **直接のTarget参照は避ける**: `<systemPath>`や`target/`へのファイルパスを使用してこの問題を回避しようとしないでください — それは脆く、Mavenのチェックサム/推移性をスキップします。

この挙動は、最近のMavenバージョン（2025年現在、3.9.xまで）でも変更されていません。詳細は、公式のマルチモジュールガイドを参照してください。

[Introduction to the Build Lifecycle - Multi-module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#multi-module)  
[Maven EAR Plugin Documentation](https://maven.apache.org/plugins/maven-ear-plugin/ear-mojo.html)