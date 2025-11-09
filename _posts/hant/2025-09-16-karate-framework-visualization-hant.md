---
audio: false
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 空手道測試框架架構視覺化
translated: true
type: note
---

以下是一個獨立的 Python 腳本，使用 NetworkX 和 Matplotlib 繪製 Karate 測試框架的高層次架構/流程圖。它按角色分組元件（編寫、執行、運行時、協定/IO、外部系統和報告），並顯示從功能檔案透過引擎到協定和報告的典型流程。

操作說明：
- pip install networkx matplotlib
- 可選安裝 pygraphviz 或 pydot + graphviz 以獲得更好的佈局；腳本會自動偵測並回退到彈簧佈局。

程式碼：

```python
import networkx as nx
import matplotlib.pyplot as plt

# 嘗試使用 Graphviz 以獲得較整潔的佈局；否則回退到彈簧佈局。
def get_layout(G):
    try:
        # 嘗試 PyGraphviz
        from networkx.drawing.nx_agraph import graphviz_layout
        return graphviz_layout(G, prog="dot")
    except Exception:
        try:
            # 嘗試 pydot
            from networkx.drawing.nx_pydot import graphviz_layout
            return graphviz_layout(G, prog="dot")
        except Exception:
            # 回退：彈簧佈局
            return nx.spring_layout(G, k=1.2, seed=42)

G = nx.DiGraph()

# 按類別定義節點
nodes = {
    # 編寫
    "Feature files (.feature)": "Authoring",
    "Reusable features (call/read)": "Authoring",
    "karate-config.js / properties": "Authoring",
    "Test data (JSON/CSV)": "Authoring",

    # 執行
    "Runner (CLI/JUnit5/Maven/Gradle)": "Execution",
    "Parallel runner": "Execution",

    # 運行時
    "Karate engine (DSL interpreter)": "Runtime",
    "JS engine": "Runtime",
    "Variable/context": "Runtime",
    "Assertions & matchers": "Runtime",

    # 協定 / IO
    "HTTP/REST/SOAP/GraphQL": "Protocols",
    "WebSocket": "Protocols",
    "UI driver (web)": "Protocols",
    "Mock server": "Protocols",

    # 外部
    "External systems/services": "External",

    # 報告
    "Reports (HTML, JUnit, JSON)": "Reporting",
    "CI/CD": "Reporting",
}

# 添加帶有類別屬性的節點
for n, cat in nodes.items():
    G.add_node(n, category=cat)

# 定義邊（u -> v）及可選標籤
edges = [
    # 編寫到執行
    ("Feature files (.feature)", "Runner (CLI/JUnit5/Maven/Gradle)", "execute"),
    ("karate-config.js / properties", "Runner (CLI/JUnit5/Maven/Gradle)", "configure"),
    ("Test data (JSON/CSV)", "Feature files (.feature)", "data-driven"),
    ("Reusable features (call/read)", "Feature files (.feature)", "reuse"),

    # 執行到運行時
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Parallel runner", "optional"),
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Karate engine (DSL interpreter)", "invoke"),
    ("Parallel runner", "Karate engine (DSL interpreter)", "parallelize"),

    # 運行時內部
    ("Karate engine (DSL interpreter)", "JS engine", "script expressions"),
    ("Karate engine (DSL interpreter)", "Variable/context", "manage state"),

    # 引擎到協定
    ("Karate engine (DSL interpreter)", "HTTP/REST/SOAP/GraphQL", "call APIs"),
    ("Karate engine (DSL interpreter)", "WebSocket", "send/receive"),
    ("Karate engine (DSL interpreter)", "UI driver (web)", "drive UI"),
    ("Karate engine (DSL interpreter)", "Mock server", "start/stub"),

    # 協定到外部系統
    ("HTTP/REST/SOAP/GraphQL", "External systems/services", "requests"),
    ("WebSocket", "External systems/services", "messages"),
    ("UI driver (web)", "External systems/services", "browser/app"),
    ("Mock server", "External systems/services", "simulate"),

    # 回應流回引擎
    ("External systems/services", "Karate engine (DSL interpreter)", "responses"),

    # 斷言和報告
    ("Karate engine (DSL interpreter)", "Assertions & matchers", "verify"),
    ("Assertions & matchers", "Reports (HTML, JUnit, JSON)", "results"),
    ("Karate engine (DSL interpreter)", "Reports (HTML, JUnit, JSON)", "runtime logs"),
    ("Reports (HTML, JUnit, JSON)", "CI/CD", "publish"),
]

# 添加邊到圖形
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# 每個類別的顏色
category_colors = {
    "Authoring": "#4C78A8",
    "Execution": "#F58518",
    "Runtime": "#B279A2",
    "Protocols": "#54A24B",
    "External": "#9A9A9A",
    "Reporting": "#E45756",
}

# 建立節點顏色列表
node_colors = [category_colors[G.nodes[n]["category"]] for n in G.nodes()]

# 計算佈局
pos = get_layout(G)

plt.figure(figsize=(14, 10))
# 繪製節點
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, alpha=0.9, linewidths=1.2, edgecolors="black")
# 繪製邊
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=16, width=1.2, connectionstyle="arc3,rad=0.06")
# 繪製標籤
nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")

# 繪製部分邊標籤以減少混亂
important_edge_labels = {
    (u, v): d["label"]
    for u, v, d in G.edges(data=True)
    if d["label"] in {"execute", "invoke", "parallelize", "call APIs", "start/stub", "verify", "results", "publish"}
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=important_edge_labels, font_size=8, label_pos=0.5, rotate=False)

# 圖例
import matplotlib.patches as mpatches
legend_patches = [mpatches.Patch(color=col, label=cat) for cat, col in category_colors.items()]
plt.legend(handles=legend_patches, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.05), frameon=False)

plt.title("How the Karate Test Framework Works (High-Level Flow)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
```

此圖表傳達的內容：
- 編寫：您編寫 .feature 檔案，可以重複使用其他功能，透過 karate-config 進行配置，並提供數據。
- 執行：您透過 CLI/JUnit5/Maven/Gradle 運行，可選擇並行執行。
- 運行時：Karate 引擎解釋 DSL，使用 JS 引擎處理表達式，並管理場景狀態。
- 協定/IO：引擎驅動 HTTP（REST/SOAP/GraphQL）、WebSocket 和 UI（透過 Karate 的驅動程式）。它還可以啟動模擬伺服器以存根依賴項。
- 外部系統：真實服務或模擬服務進行回應。
- 報告：斷言產生報告（HTML、JUnit XML、JSON），您的 CI/CD 可以發布這些報告。

如果您希望圖表針對特定部分進行定制（例如僅限 API 測試，或強調模擬或 UI），請告訴我，我將調整節點/邊。