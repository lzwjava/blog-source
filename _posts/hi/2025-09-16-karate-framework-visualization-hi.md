---
audio: false
generated: true
image: false
lang: hi
layout: post
model: mistralai/mistral-medium-3.1
title: कराटे परीक्षण ढांचा वास्तुकला दृश्यीकरण
translated: true
type: note
---

नीचे एक स्वतंत्र पायथन स्क्रिप्ट है जो नेटवर्कएक्स और मैटप्लॉटलिब का उपयोग करके यह दर्शाती है कि कराटे टेस्ट फ्रेमवर्क कैसे काम करता है (हाई-लेवल आर्किटेक्चर/फ्लो)। यह कंपोनेंट्स को भूमिका के अनुसार समूहित करती है (ऑथरिंग, एक्सीक्यूशन, रनटाइम, प्रोटोकॉल/आईओ, एक्सटर्नल सिस्टम्स, और रिपोर्टिंग), और फीचर फाइल्स से लेकर इंजन, प्रोटोकॉल और रिपोर्टिंग तक के सामान्य फ्लो को दिखाती है।

निर्देश:
- pip install networkx matplotlib
- वैकल्पिक रूप से pygraphviz या pydot + graphviz इंस्टॉल करें अगर आप बेहतर लेआउट चाहते हैं; स्क्रिप्ट स्वचालित रूप से पता लगा लेती है और स्प्रिंग लेआउट पर फॉल बैक करती है।

कोड:

```python
import networkx as nx
import matplotlib.pyplot as plt

# लेआउट के लिए Graphviz का उपयोग करने का प्रयास करें यदि उपलब्ध हो; अन्यथा spring_layout पर वापस आ जाएं।
def get_layout(G):
    try:
        # PyGraphviz का प्रयास करें
        from networkx.drawing.nx_agraph import graphviz_layout
        return graphviz_layout(G, prog="dot")
    except Exception:
        try:
            # pydot का प्रयास करें
            from networkx.drawing.nx_pydot import graphviz_layout
            return graphviz_layout(G, prog="dot")
        except Exception:
            # फॉलबैक: स्प्रिंग लेआउट
            return nx.spring_layout(G, k=1.2, seed=42)

G = nx.DiGraph()

# नोड्स को श्रेणी के अनुसार परिभाषित करें
nodes = {
    # ऑथरिंग
    "Feature files (.feature)": "Authoring",
    "Reusable features (call/read)": "Authoring",
    "karate-config.js / properties": "Authoring",
    "Test data (JSON/CSV)": "Authoring",

    # एक्सीक्यूशन
    "Runner (CLI/JUnit5/Maven/Gradle)": "Execution",
    "Parallel runner": "Execution",

    # रनटाइम
    "Karate engine (DSL interpreter)": "Runtime",
    "JS engine": "Runtime",
    "Variable/context": "Runtime",
    "Assertions & matchers": "Runtime",

    # प्रोटोकॉल / आईओ
    "HTTP/REST/SOAP/GraphQL": "Protocols",
    "WebSocket": "Protocols",
    "UI driver (web)": "Protocols",
    "Mock server": "Protocols",

    # एक्सटर्नल
    "External systems/services": "External",

    # रिपोर्टिंग
    "Reports (HTML, JUnit, JSON)": "Reporting",
    "CI/CD": "Reporting",
}

# नोड्स को श्रेणी विशेषता के साथ जोड़ें
for n, cat in nodes.items():
    G.add_node(n, category=cat)

# एजेस को परिभाषित करें (u -> v) वैकल्पिक लेबल के साथ
edges = [
    # ऑथरिंग से एक्सीक्यूशन
    ("Feature files (.feature)", "Runner (CLI/JUnit5/Maven/Gradle)", "execute"),
    ("karate-config.js / properties", "Runner (CLI/JUnit5/Maven/Gradle)", "configure"),
    ("Test data (JSON/CSV)", "Feature files (.feature)", "data-driven"),
    ("Reusable features (call/read)", "Feature files (.feature)", "reuse"),

    # एक्सीक्यूशन से रनटाइम
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Parallel runner", "optional"),
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Karate engine (DSL interpreter)", "invoke"),
    ("Parallel runner", "Karate engine (DSL interpreter)", "parallelize"),

    # रनटाइम आंतरिक
    ("Karate engine (DSL interpreter)", "JS engine", "script expressions"),
    ("Karate engine (DSL interpreter)", "Variable/context", "manage state"),

    # इंजन से प्रोटोकॉल
    ("Karate engine (DSL interpreter)", "HTTP/REST/SOAP/GraphQL", "call APIs"),
    ("Karate engine (DSL interpreter)", "WebSocket", "send/receive"),
    ("Karate engine (DSL interpreter)", "UI driver (web)", "drive UI"),
    ("Karate engine (DSL interpreter)", "Mock server", "start/stub"),

    # प्रोटोकॉल से एक्सटर्नल सिस्टम्स
    ("HTTP/REST/SOAP/GraphQL", "External systems/services", "requests"),
    ("WebSocket", "External systems/services", "messages"),
    ("UI driver (web)", "External systems/services", "browser/app"),
    ("Mock server", "External systems/services", "simulate"),

    # प्रतिक्रियाएं इंजन में वापस आती हैं
    ("External systems/services", "Karate engine (DSL interpreter)", "responses"),

    # असेर्शन और रिपोर्टिंग
    ("Karate engine (DSL interpreter)", "Assertions & matchers", "verify"),
    ("Assertions & matchers", "Reports (HTML, JUnit, JSON)", "results"),
    ("Karate engine (DSL interpreter)", "Reports (HTML, JUnit, JSON)", "runtime logs"),
    ("Reports (HTML, JUnit, JSON)", "CI/CD", "publish"),
]

# ग्राफ में एजेस जोड़ें
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# श्रेणी के अनुसार रंग
category_colors = {
    "Authoring": "#4C78A8",
    "Execution": "#F58518",
    "Runtime": "#B279A2",
    "Protocols": "#54A24B",
    "External": "#9A9A9A",
    "Reporting": "#E45756",
}

# नोड्स के लिए रंग सूची बनाएं
node_colors = [category_colors[G.nodes[n]["category"]] for n in G.nodes()]

# लेआउट की गणना करें
pos = get_layout(G)

plt.figure(figsize=(14, 10))
# नोड्स बनाएं
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, alpha=0.9, linewidths=1.2, edgecolors="black")
# एजेस बनाएं
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=16, width=1.2, connectionstyle="arc3,rad=0.06")
# लेबल बनाएं
nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")

# अव्यवस्था कम करने के लिए एज लेबल्स का एक सबसेट बनाएं
important_edge_labels = {
    (u, v): d["label"]
    for u, v, d in G.edges(data=True)
    if d["label"] in {"execute", "invoke", "parallelize", "call APIs", "start/stub", "verify", "results", "publish"}
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=important_edge_labels, font_size=8, label_pos=0.5, rotate=False)

# लीजेंड
import matplotlib.patches as mpatches
legend_patches = [mpatches.Patch(color=col, label=cat) for cat, col in category_colors.items()]
plt.legend(handles=legend_patches, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.05), frameon=False)

plt.title("How the Karate Test Framework Works (High-Level Flow)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
```

यह डायग्राम क्या दर्शाता है:
- **ऑथरिंग**: आप .feature फाइल्स लिखते हैं, अन्य फीचर्स को पुन: उपयोग कर सकते हैं, karate-config के माध्यम से कॉन्फ़िगर करते हैं, और डेटा फीड करते हैं।
- **एक्सीक्यूशन**: आप CLI/JUnit5/Maven/Gradle के माध्यम से चलाते हैं, वैकल्पिक रूप से समानांतर में।
- **रनटाइम**: कराटे इंजन DSL की व्याख्या करता है, एक्सप्रेशंस के लिए JS इंजन का उपयोग करता है, और सिनेरियो स्टेट को प्रबंधित करता है।
- **प्रोटोकॉल/आईओ**: इंजन HTTP (REST/SOAP/GraphQL), WebSocket, और UI (कराटे के ड्राइवर के माध्यम से) को चलाता है। यह निर्भरताओं को स्टब करने के लिए एक मॉक सर्वर भी शुरू कर सकता है।
- **एक्सटर्नल सिस्टम्स**: वास्तविक सेवाएं या मॉक की गई सेवाएं प्रतिक्रिया देती हैं।
- **रिपोर्टिंग**: असेर्शन रिपोर्ट्स (HTML, JUnit XML, JSON) उत्पन्न करते हैं, जिन्हें आपका CI/CD प्रकाशित कर सकता है।

यदि आप डायग्राम को किसी विशिष्ट भाग के लिए अनुकूलित करना चाहते हैं (जैसे, केवल API टेस्टिंग, या मॉक्स या UI पर जोर देना), तो मुझे बताएं और मैं नोड्स/एजेस को समायोजित कर दूंगा।