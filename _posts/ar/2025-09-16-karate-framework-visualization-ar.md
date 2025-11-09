---
audio: false
generated: true
image: false
lang: ar
layout: post
model: mistralai/mistral-medium-3.1
title: تصور هندسة إطار اختبار الكاراتي
translated: true
type: note
---

```python
import networkx as nx
import matplotlib.pyplot as plt

# محاولة استخدام Graphviz للحصول على تخطيط أنظف إذا كان متاحًا؛ والتراجع إلى التخطيط الزنبركي خلاف ذلك.
def get_layout(G):
    try:
        # محاولة PyGraphviz
        from networkx.drawing.nx_agraph import graphviz_layout
        return graphviz_layout(G, prog="dot")
    except Exception:
        try:
            # محاولة pydot
            from networkx.drawing.nx_pydot import graphviz_layout
            return graphviz_layout(G, prog="dot")
        except Exception:
            # التراجع: التخطيط الزنبركي
            return nx.spring_layout(G, k=1.2, seed=42)

G = nx.DiGraph()

# تعريف العقد مجمعة حسب الفئة
nodes = {
    # التأليف
    "Feature files (.feature)": "Authoring",
    "Reusable features (call/read)": "Authoring",
    "karate-config.js / properties": "Authoring",
    "Test data (JSON/CSV)": "Authoring",

    # التنفيذ
    "Runner (CLI/JUnit5/Maven/Gradle)": "Execution",
    "Parallel runner": "Execution",

    # وقت التشغيل
    "Karate engine (DSL interpreter)": "Runtime",
    "JS engine": "Runtime",
    "Variable/context": "Runtime",
    "Assertions & matchers": "Runtime",

    # البروتوكولات / الإدخال والإخراج
    "HTTP/REST/SOAP/GraphQL": "Protocols",
    "WebSocket": "Protocols",
    "UI driver (web)": "Protocols",
    "Mock server": "Protocols",

    # الخارجية
    "External systems/services": "External",

    # التقارير
    "Reports (HTML, JUnit, JSON)": "Reporting",
    "CI/CD": "Reporting",
}

# إضافة العقد مع سمة الفئة
for n, cat in nodes.items():
    G.add_node(n, category=cat)

# تعريف الحواف (u -> v) مع تسميات اختيارية
edges = [
    # من التأليف إلى التنفيذ
    ("Feature files (.feature)", "Runner (CLI/JUnit5/Maven/Gradle)", "execute"),
    ("karate-config.js / properties", "Runner (CLI/JUnit5/Maven/Gradle)", "configure"),
    ("Test data (JSON/CSV)", "Feature files (.feature)", "data-driven"),
    ("Reusable features (call/read)", "Feature files (.feature)", "reuse"),

    # من التنفيذ إلى وقت التشغيل
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Parallel runner", "optional"),
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Karate engine (DSL interpreter)", "invoke"),
    ("Parallel runner", "Karate engine (DSL interpreter)", "parallelize"),

    # العمليات الداخلية لوقت التشغيل
    ("Karate engine (DSL interpreter)", "JS engine", "script expressions"),
    ("Karate engine (DSL interpreter)", "Variable/context", "manage state"),

    # من المحرك إلى البروتوكولات
    ("Karate engine (DSL interpreter)", "HTTP/REST/SOAP/GraphQL", "call APIs"),
    ("Karate engine (DSL interpreter)", "WebSocket", "send/receive"),
    ("Karate engine (DSL interpreter)", "UI driver (web)", "drive UI"),
    ("Karate engine (DSL interpreter)", "Mock server", "start/stub"),

    # من البروتوكولات إلى الأنظمة الخارجية
    ("HTTP/REST/SOAP/GraphQL", "External systems/services", "requests"),
    ("WebSocket", "External systems/services", "messages"),
    ("UI driver (web)", "External systems/services", "browser/app"),
    ("Mock server", "External systems/services", "simulate"),

    # تدفق الردود مرة أخرى إلى المحرك
    ("External systems/services", "Karate engine (DSL interpreter)", "responses"),

    # التأكيدات وإعداد التقارير
    ("Karate engine (DSL interpreter)", "Assertions & matchers", "verify"),
    ("Assertions & matchers", "Reports (HTML, JUnit, JSON)", "results"),
    ("Karate engine (DSL interpreter)", "Reports (HTML, JUnit, JSON)", "runtime logs"),
    ("Reports (HTML, JUnit, JSON)", "CI/CD", "publish"),
]

# إضافة الحواف إلى الرسم البياني
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# الألوان لكل فئة
category_colors = {
    "Authoring": "#4C78A8",
    "Execution": "#F58518",
    "Runtime": "#B279A2",
    "Protocols": "#54A24B",
    "External": "#9A9A9A",
    "Reporting": "#E45756",
}

# بناء قائمة الألوان للعقد
node_colors = [category_colors[G.nodes[n]["category"]] for n in G.nodes()]

# حساب التخطيط
pos = get_layout(G)

plt.figure(figsize=(14, 10))
# رسم العقد
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, alpha=0.9, linewidths=1.2, edgecolors="black")
# رسم الحواف
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=16, width=1.2, connectionstyle="arc3,rad=0.06")
# رسم التسميات
nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")

# رسم مجموعة فرعية من تسميات الحواف لتقليل الفوضى
important_edge_labels = {
    (u, v): d["label"]
    for u, v, d in G.edges(data=True)
    if d["label"] in {"execute", "invoke", "parallelize", "call APIs", "start/stub", "verify", "results", "publish"}
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=important_edge_labels, font_size=8, label_pos=0.5, rotate=False)

# وسيلة الإيضاح (الأسطورة)
import matplotlib.patches as mpatches
legend_patches = [mpatches.Patch(color=col, label=cat) for cat, col in category_colors.items()]
plt.legend(handles=legend_patches, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.05), frameon=False)

plt.title("How the Karate Test Framework Works (High-Level Flow)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
```

ما يوضحه هذا الرسم البياني:
- **التأليف**: تكتب ملفات .feature، يمكنك إعادة استخدام الميزات الأخرى، التهيئة عبر karate-config، وتغذية البيانات.
- **التنفيذ**: تشغّل عبر CLI/JUnit5/Maven/Gradle، ويمكن أن يكون بشكل متوازٍ اختياريًا.
- **وقت التشغيل**: يُفسر محرك Karate لغة DSL، ويستخدم محرك JS للتعبيرات، ويدير حالة السيناريو.
- **البروتوكولات/الإدخال والإخراج**: يقود المحرك HTTP (REST/SOAP/GraphQL)، وWebSocket، والواجهةالمستخدمة (عبر مشغّل Karate). يمكنه أيضًا بدء خادم وهمي (mock server) لاستبدال التبعيات.
- **الأنظمة الخارجية**: تستجيب الخدمات الحقيقية أو الخدمات المُقلَّدة.
- **إعداد التقارير**: تنتج التأكيدات (Assertions) تقارير (HTML، JUnit XML، JSON)، والتي يمكن لـ CI/CD نشرها.

إذا كنت تريد تخصيص الرسم البياني لجزء معين (مثل اختبارات API فقط، أو التركيز على المحاكاة أو الواجهةالمستخدمة)، أخبرني وسأقوم بتعديل العقد/الحواف.