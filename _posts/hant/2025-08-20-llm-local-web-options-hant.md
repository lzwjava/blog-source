---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 輕量級本地LLM網頁客戶端選項
translated: true
type: note
---

如果你正在尋找輕量級、開源的網頁客戶端來本地運行大型語言模型（LLMs）——且依賴項比 Open WebUI 更少——以下是一些優秀的替代方案：

**1. Lobe Chat**
- 輕量且可擴展的 Lobe Chat 同時支援本地與遠端 LLMs。它提供外掛系統和簡潔的用戶界面，可透過 Docker 或直接在電腦上運行。其以易於設定和與 Ollama 及其他後端的良好效能而聞名。

**2. LM Studio**
- LM Studio 是一款桌面應用程式，支援 GGUF 模型（如 Mistral、Phi 3 和 Gemma），並提供簡單易用的界面。它非常適合快速進行本地推理，無需複雜設定或大量依賴項。

**3. text-generation-webui (Oobabooga)**
- 這是一款功能豐富的 Gradio 網頁界面，支援多種後端（transformers、GPTQ、AWQ、EXL2、llama.cpp）。它高度可自訂且廣泛使用，儘管設定上比 LM Studio 稍為複雜。

**4. AnythingLLM**
- 一款多功能的自行託管聊天界面，適用於本地與雲端模型。它專為通用用途設計，並提供桌面應用程式版本，使其既靈活又相對輕量。

**5. Jan**
- Jan 是一款跨平台、具離線功能的聊天界面，支援拖放自訂和預建模板。它針對效能進行了優化，並支援多種 LLM API，是注重隱私的用戶的理想選擇。

**6. Ollama UI**
- 專為 Ollama 設計，此界面極簡且易於部署，若你已使用 Ollama 進行模型服務，它將是絕佳搭配。

**7. Open-LLM-WebUI**
- 一個簡潔的開源網頁界面，用於本地運行精簡型 LLMs。它設計注重易用性和最小化設定，是追求簡單直接方案的理想替代品。

**總結表格：**

| 客戶端                 | 主要特點                              | 設定複雜度       | 最適合場景               |
|------------------------|---------------------------------------|------------------|-------------------------|
| Lobe Chat              | 外掛、Docker 支援、簡潔界面           | 低               | 通用用途、Ollama        |
| LM Studio              | 桌面應用、GGUF 支援、簡單界面          | 極低             | 快速本地推理            |
| text-generation-webui  | 多後端支援、高度可自訂                | 中               | 進階用戶                |
| AnythingLLM            | 桌面應用、靈活、通用用途              | 低               | 本地/雲端混合使用       |
| Jan                    | 離線功能、拖放操作、模板              | 低               | 隱私保護、自訂需求      |
| Ollama UI              | 極簡、專為 Ollama 設計                | 極低             | Ollama 用戶             |
| Open-LLM-WebUI         | 簡潔、輕量                            | 低               | 精簡型 LLMs            |

若你追求最輕量的選擇，**LM Studio** 或 **Ollama UI** 是極佳的起點。若需要更多功能與靈活性，**Lobe Chat** 或 **text-generation-webui** 則是強力選擇。

是否需要關於設定或特定使用場景的更多詳細資訊？