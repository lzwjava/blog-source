---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Pythonダイアグラム・アズ・コードツールの代替案
translated: true
type: note
---

以下は、Graphviz や NetworkX を超えた、ソフトウェア設計/アーキテクチャ図の生成を簡単にする Python フレンドリーなオプションです。ユースケース別にグループ分けし、簡単なメモと小さな例を記載しています。

図をコードで記述 (UML, C4, フローチャート, シーケンス図)
- PlantUML (python-plantuml 経由、またはローカルの JAR を使用)
  - UML (クラス図、シーケンス図、コンポーネント図、状態図、アクティビティ図、配置図) に最適。
  - CI やドキュメントとの連携が良好。
  - 例:
    @startuml
    class User
    class Order
    User "1" --> "*" Order
    @enduml
- Mermaid (CLI または Kroki サーバーを使用; Python からレンダラーを呼び出し可能)
  - シーケンス図、クラス図、フローチャート、ER図、状態図など、シンプルな記法。
  - 多くのドキュメントツールや Wiki で美しくレンダリングされる。
  - 例:
    flowchart LR
      API --> DB
- BlockDiag ファミリー (blockdiag, seqdiag, actdiag, nwdiag)
  - シンプルなテキストからブロック図、シーケンス図、アクティビティ図、ネットワーク図を生成する Pure-Python ツール。
  - 例 (seqdiag):
    seqdiag {
      Client -> API [label = "GET /users"];
      API -> DB [label = "query"];
    }
- Structurizr (C4 モデル; コミュニティ製 Python クライアント)
  - ソフトウェアアーキテクチャ (コンテキスト、コンテナ、コンポーネント) をモデリングし、Structurizr または PlantUML 経由でレンダリング。
  - マルチビューでのアーキテクチャ文書や ADR ワークフローに強力。
- Kroki (diagram-as-a-service; Python クライアント利用可能)
  - 多数の DSL (PlantUML, Mermaid, Graphviz, BPMN など) を、Python から単一の HTTP API を介してレンダリング。

クラウドおよびインフラストラクチャアーキテクチャ
- Diagrams (mingrammer 作)
  - 公式プロバイダーアイコン (AWS, Azure, GCP, K8s, オンプレミス) を使用した、クラウド/システムアーキテクチャの Diagram-as-code。
  - アーキテクチャの概要図に非常に人気。
  - 例:
    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    with Diagram("Web Service", show=False):
        EC2("api") >> RDS("db")

インタラクティブなネットワーク/グラフ可視化 (システムマップ、依存関係に便利)
- PyVis (vis.js)
  - 最小限のコードでインタラクティブな HTML グラフを生成。
  - 例:
    from pyvis.network import Network
    net = Network(); net.add_nodes(["API","DB"]); net.add_edge("API","DB"); net.show("arch.html")
- Dash Cytoscape / ipycytoscape (Cytoscape.js)
  - Dash アプリや Jupyter でインタラクティブかつカスタマイズ可能なグラフを作成。依存関係やフローの探索に適している。
- Plotly
  - カスタムスタイリング可能なインタラクティブなノードリンク図を構築。埋め込み・共有が容易。
- Bokeh / HoloViews
  - ネットワークサポートを備えたインタラクティブなプロット。Python 中心のダッシュボードに適している。
- python-igraph
  - 組み込みのプロット機能を備えた高速なグラフライブラリ。レイアウトアルゴリズムとエクスポート可能な図の両方が必要な場合に適している。

ドキュメント連携 (図をドキュメントの近くに保つ)
- Sphinx 拡張: sphinxcontrib-plantuml, sphinxcontrib-mermaid, sphinxcontrib-blockdiag
  - reStructuredText/Markdown 内に図をインラインで記述し、ドキュメントパイプライン内でビルド。
- MkDocs プラグイン (Mermaid/PlantUML 用)
  - モダンな静的サイトに便利。

コードとアーキテクチャのリバースエンジニアリング
- pylint の pyreverse
  - Python コードから UML クラス図とパッケージ図を生成 (多くの場合 Graphviz 経由でレンダリングされるが、ワークフローはシンプル)。
- pydeps
  - Python パッケージのインポート/依存関係グラフを作成。大規模なコードベースでのアーキテクチャマップに便利。

特殊な図
- SchemDraw
  - Python によるプログラム的な回路/ロジック/フローチャート図。クリーンなベクター出力。
- railroad-diagrams
  - 構文/文法図を生成 (プロトコル/仕様書のドキュメントに有用)。

選択のヒント
- 素早い UML/シーケンス図のドキュメント: PlantUML または Mermaid。
- クラウド/システムアーキテクチャのポスター: Diagrams (mingrammer)。
- インタラクティブな探索と共有: PyVis または Dash Cytoscape。
- C4 モデルとライブなアーキテクチャ文書: Structurizr (PlantUML/Mermaid へのエクスポート経由)。
- コードからの自動図生成: pyreverse, pydeps。

対象とする図の種類 (UML クラス図、シーケンス図、C4、クラウド、データフロー、パッケージ依存関係) と出力形式 (PNG/SVG/HTML/ドキュメント埋め込み) を教えていただければ、最小限のセットアップとスターターテンプレートを提案できます。