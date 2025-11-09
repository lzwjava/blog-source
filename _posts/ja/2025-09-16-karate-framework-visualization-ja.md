---
audio: false
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: 空手テストフレームワークアーキテクチャ可視化
translated: true
type: note
---

以下は、Karateテストフレームワークの高レベルなアーキテクチャ/フローを描画する、NetworkXとMatplotlibを使用した独立したPythonスクリプトです。コンポーネントを役割（作成、実行、ランタイム、プロトコル/IO、外部システム、レポート）ごとにグループ化し、フィーチャーファイルからエンジンを経由してプロトコルおよびレポートへの典型的なフローを示します。

手順:
- pip install networkx matplotlib
- より良いレイアウトを希望する場合は、オプションで pygraphviz または pydot + graphviz をインストールしてください。スクリプトは自動検出し、フォールバックとしてスプリングレイアウトを使用します。

コード:

```python
import networkx as nx
import matplotlib.pyplot as plt

# 利用可能な場合はより整理されたレイアウトのためにGraphvizを使用。それ以外の場合はspring_layoutにフォールバック。
def get_layout(G):
    try:
        # PyGraphvizを試す
        from networkx.drawing.nx_agraph import graphviz_layout
        return graphviz_layout(G, prog="dot")
    except Exception:
        try:
            # pydotを試す
            from networkx.drawing.nx_pydot import graphviz_layout
            return graphviz_layout(G, prog="dot")
        except Exception:
            # フォールバック: スプリングレイアウト
            return nx.spring_layout(G, k=1.2, seed=42)

G = nx.DiGraph()

# カテゴリごとにグループ化されたノードを定義
nodes = {
    # 作成
    "Feature files (.feature)": "Authoring",
    "Reusable features (call/read)": "Authoring",
    "karate-config.js / properties": "Authoring",
    "Test data (JSON/CSV)": "Authoring",

    # 実行
    "Runner (CLI/JUnit5/Maven/Gradle)": "Execution",
    "Parallel runner": "Execution",

    # ランタイム
    "Karate engine (DSL interpreter)": "Runtime",
    "JS engine": "Runtime",
    "Variable/context": "Runtime",
    "Assertions & matchers": "Runtime",

    # プロトコル / IO
    "HTTP/REST/SOAP/GraphQL": "Protocols",
    "WebSocket": "Protocols",
    "UI driver (web)": "Protocols",
    "Mock server": "Protocols",

    # 外部
    "External systems/services": "External",

    # レポート
    "Reports (HTML, JUnit, JSON)": "Reporting",
    "CI/CD": "Reporting",
}

# カテゴリ属性を持つノードを追加
for n, cat in nodes.items():
    G.add_node(n, category=cat)

# エッジ (u -> v) を定義（オプションのラベル付き）
edges = [
    # 作成から実行へ
    ("Feature files (.feature)", "Runner (CLI/JUnit5/Maven/Gradle)", "execute"),
    ("karate-config.js / properties", "Runner (CLI/JUnit5/Maven/Gradle)", "configure"),
    ("Test data (JSON/CSV)", "Feature files (.feature)", "data-driven"),
    ("Reusable features (call/read)", "Feature files (.feature)", "reuse"),

    # 実行からランタイムへ
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Parallel runner", "optional"),
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Karate engine (DSL interpreter)", "invoke"),
    ("Parallel runner", "Karate engine (DSL interpreter)", "parallelize"),

    # ランタイム内部
    ("Karate engine (DSL interpreter)", "JS engine", "script expressions"),
    ("Karate engine (DSL interpreter)", "Variable/context", "manage state"),

    # エンジンからプロトコルへ
    ("Karate engine (DSL interpreter)", "HTTP/REST/SOAP/GraphQL", "call APIs"),
    ("Karate engine (DSL interpreter)", "WebSocket", "send/receive"),
    ("Karate engine (DSL interpreter)", "UI driver (web)", "drive UI"),
    ("Karate engine (DSL interpreter)", "Mock server", "start/stub"),

    # プロトコルから外部システムへ
    ("HTTP/REST/SOAP/GraphQL", "External systems/services", "requests"),
    ("WebSocket", "External systems/services", "messages"),
    ("UI driver (web)", "External systems/services", "browser/app"),
    ("Mock server", "External systems/services", "simulate"),

    # エンジンへのレスポンスの流れ
    ("External systems/services", "Karate engine (DSL interpreter)", "responses"),

    # アサーションとレポート
    ("Karate engine (DSL interpreter)", "Assertions & matchers", "verify"),
    ("Assertions & matchers", "Reports (HTML, JUnit, JSON)", "results"),
    ("Karate engine (DSL interpreter)", "Reports (HTML, JUnit, JSON)", "runtime logs"),
    ("Reports (HTML, JUnit, JSON)", "CI/CD", "publish"),
]

# グラフにエッジを追加
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# カテゴリごとの色
category_colors = {
    "Authoring": "#4C78A8",
    "Execution": "#F58518",
    "Runtime": "#B279A2",
    "Protocols": "#54A24B",
    "External": "#9A9A9A",
    "Reporting": "#E45756",
}

# ノード用の色リストを作成
node_colors = [category_colors[G.nodes[n]["category"]] for n in G.nodes()]

# レイアウトを計算
pos = get_layout(G)

plt.figure(figsize=(14, 10))
# ノードを描画
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, alpha=0.9, linewidths=1.2, edgecolors="black")
# エッジを描画
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=16, width=1.2, connectionstyle="arc3,rad=0.06")
# ラベルを描画
nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")

# エッジラベルのサブセットを描画して煩雑さを軽減
important_edge_labels = {
    (u, v): d["label"]
    for u, v, d in G.edges(data=True)
    if d["label"] in {"execute", "invoke", "parallelize", "call APIs", "start/stub", "verify", "results", "publish"}
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=important_edge_labels, font_size=8, label_pos=0.5, rotate=False)

# 凡例
import matplotlib.patches as mpatches
legend_patches = [mpatches.Patch(color=col, label=cat) for cat, col in category_colors.items()]
plt.legend(handles=legend_patches, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.05), frameon=False)

plt.title("How the Karate Test Framework Works (High-Level Flow)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
```

この図が伝える内容:
- **作成**: .featureファイルを記述し、他のフィーチャーを再利用し、karate-configで設定し、データを投入できます。
- **実行**: CLI/JUnit5/Maven/Gradle経由で実行し、オプションで並列実行します。
- **ランタイム**: KarateエンジンがDSLを解釈し、JSエンジンを式に使用し、シナリオの状態を管理します。
- **プロトコル/IO**: エンジンはHTTP (REST/SOAP/GraphQL)、WebSocket、UI (Karateのドライバー経由) を駆動します。また、依存関係をスタブするためにモックサーバーを起動することもできます。
- **外部システム**: 実際のサービスまたはモック化されたサービスが応答します。
- **レポート**: アサーションがレポート (HTML、JUnit XML、JSON) を生成し、CI/CDがそれを公開できます。

図を特定の側面 (例: APIテストのみ、またはモックやUIを強調) に合わせて調整したい場合は、お知らせください。ノード/エッジを調整します。