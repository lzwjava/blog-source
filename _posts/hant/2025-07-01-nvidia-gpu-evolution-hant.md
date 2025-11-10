---
audio: false
generated: true
lang: hant
layout: post
title: NVIDIA 人工智能與 GPU 革命
translated: true
type: note
---

NVIDIA在過去十年中徹底改變了計算領域，從主要為遊戲提供顯示卡的公司轉型為加速計算的強大力量，特別是在人工智慧（AI）和高效能計算（HPC）領域。

### NVIDIA GPU：簡史（過去十年）

過去十年見證了NVIDIA GPU的顯著演進，從傳統的圖形渲染擴展到數據中心和AI領域的關鍵組件。重要里程碑包括：

* **Pascal架構（約2016年）：** 隨著GeForce GTX 10系列顯示卡推出，Pascal為遊戲帶來了顯著的效能提升，並透過Tesla P100擴展了NVIDIA在深度學習領域的佈局。
* **Volta架構（2017年）：** 這對AI領域具有革命性意義。基於Volta的Tesla V100引入了Tensor Core，這是專為加速深度學習訓練和推理關鍵的矩陣乘法而設計的處理單元，鞏固了NVIDIA在AI硬體領域的主導地位。
* **Turing架構（2018年）：** 隨著GeForce RTX 20系列推出，Turing將即時光線追蹤和DLSS（深度學習超級取樣）帶入消費級GPU，利用Tensor Core和新的RT Core實現更逼真的圖形。
* **Ampere架構（2020年）：** GeForce RTX 30系列和專注於數據中心的A100 GPU（基於Ampere）進一步突破了界限。A100在V100的AI效能基礎上顯著提升，提供更高的吞吐量和記憶體頻寬，成為許多AI研究和部署計畫的主力。
* **Ada Lovelace架構（2022年）：** 此架構驅動著GeForce RTX 40系列，包括旗艦型號RTX 4090。它擁有顯著提升的效能、效率，並透過第四代Tensor Core和第三代RT Core增強了AI能力，進一步完善了光線追蹤和DLSS 3。
* **Hopper架構（2022年）：** H100 GPU是Hopper世代的旗艦產品，專為大規模AI和HPC設計。它在Ampere基礎上進一步提升，配備更強大的Tensor Core、專用於LLM的Transformer Engine，以及用於大規模擴展的NVLink Switch System。
* **Blackwell架構（2024年發布）：** NVIDIA的最新架構Blackwell有望成為AI領域的下一個重大飛躍，B200和GB200（結合Grace CPU與Blackwell GPU）旨在為未來的大型語言模型提供前所未有的訓練和推理效能。

### 知名的NVIDIA GPU：H100與RTX 4090

* **NVIDIA H100 Tensor Core GPU：** 這是NVIDIA當前基於Hopper架構的頂級數據中心GPU。它專為AI和HPC工作負載設計，特別是大型語言模型（LLM）。與前代產品（A100）相比，H100帶來了數量級的效能飛躍，具備先進的Tensor Core、Transformer Engine和高頻寬記憶體（HBM3/HBM3e）。它設計用於大型集群部署，透過NVIDIA的NVLink Switch System連接以實現大規模擴展。
* **NVIDIA GeForce RTX 4090：** 這是基於Ada Lovelace架構的旗艦消費級遊戲GPU。雖然在遊戲方面極其強大（透過光線追蹤和DLSS 3提供超高效能和逼真圖形），但其底層架構和強大的處理能力也使其成為需要大量本地GPU加速但可能不需要數據中心級部署的個人創作者、AI開發者和研究人員的熱門選擇。它擁有24GB GDDR6X記憶體和大量的CUDA Core、RT Core及Tensor Core。

### 大型科技公司近年來使用的技術

大型科技公司是NVIDIA高端數據中心GPU（特別是A100和現在的H100）需求的主要推動者。它們競相構建更大、更複雜的AI模型，而NVIDIA的GPU提供了所需的無與倫比的計算能力：

* **微軟：** 大量採購NVIDIA GPU用於其Azure雲端服務和自身的AI開發，包括大型語言模型。
* **Google（Alphabet）：** 使用NVIDIA GPU，特別是在Google Cloud Platform及其AI研究中（例如訓練Gemini等模型）。雖然Google也開發自己的客製化AI晶片（TPU），但在更廣泛的AI基礎設施上仍嚴重依賴NVIDIA。
* **亞馬遜（AWS）：** 作為大客戶，在其AWS雲端服務中利用NVIDIA GPU，為廣泛客戶提供AI和HPC服務。
* **Meta Platforms：** 大量投資NVIDIA GPU以推動其AI雄心，包括為其各種平台訓練大型語言模型。
* **Oracle：** 同樣是重要買家，透過NVIDIA強大的GPU擴展其雲端服務。

這些公司通常採購數以萬計的GPU來構建其AI超級計算機和基礎設施，並將這些GPU作為服務提供給其雲端客戶。

### 雲端平台中的選項

主要雲端供應商提供多種NVIDIA GPU作為服務，讓企業和研究人員無需大量前期硬體投資即可使用強大的計算資源。這些平台通常提供各種GPU類型，並根據使用量計費：

* **亞馬遜網路服務（AWS）：** 提供多樣化選擇，包括NVIDIA A100和H100 GPU（例如在p5執行個體中），以及較舊世代如A10。
* **Google Cloud Platform（GCP）：** 提供多種NVIDIA GPU，包括最新的L4 GPU（適合生成式AI）、H100、A100、T4和V100。他們通常能快速提供新的NVIDIA硬體。
* **微軟Azure：** 提供NVIDIA A100、H100及其他GPU（如A10），用於各種機器學習和HPC工作負載。
* **Oracle Cloud Infrastructure（OCI）：** 越來越多地提供強大的NVIDIA GPU，包括H100。
* **其他專業雲端GPU供應商：** 如CoreWeave、Lambda、Paperspace、DigitalOcean和E2E Cloud等公司專注於GPU加速雲端計算，通常提供具競爭力的價格和多種NVIDIA GPU，包括最新的H100、A100和RTX A6000/RTX 6000 Ada。

這些雲端平台提供了按需擴展計算資源的靈活性，使更廣泛的用戶能夠使用高效能的NVIDIA GPU。