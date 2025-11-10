---
audio: false
generated: true
lang: hant
layout: post
title: GPU 雲端市場佔有率 2025
translated: true
type: note
---

### 2025年AI/LLM訓練的GPU雲端市場佔有率

GPU雲端市場，特別是針對大型語言模型（LLM）及其他AI工作負載的訓練領域，是更廣泛雲端基礎設施（IaaS）市場中的一個子集。雖然專門針對GPU實例的市場佔有率細分數據並未廣泛公佈（由於該領域快速演變及數據專有性），整體雲端市場佔有率仍可作為重要參考指標。這是因為主要供應商如AWS、Azure和Google Cloud透過其整合式AI/ML服務主導了GPU產品供應。而利基型供應商如Lambda Cloud則因提供成本效益高且專注於GPU存取的特點，在初創企業和研究人員中逐漸受到關注，但目前仍佔據較小的市場份額。

根據2025年第一季及2024年末的最新可用數據：
- **Amazon Web Services (AWS)**：在雲端基礎設施市場約佔29-31%的市佔率。AWS透過EC2實例（例如配備NVIDIA A100/H100 GPU）及SageMaker託管式LLM工作流程，在AI訓練的GPU雲端領域處於領先地位。因其可擴展性、Spot Instances（最高可享90%折扣）以及與其他AWS服務的整合優勢，深受需要大規模企業級訓練的用戶青睞。
- **Microsoft Azure**：約佔21-25%的市佔率。Azure的N系列虛擬機器（配備NVIDIA A100/V100/H100 GPU）及Azure Machine Learning被廣泛應用於LLM訓練，尤其深受已採用微軟生態系的組織偏好。該平台提供Spot定價與保留實例以實現成本節約。
- **Google Cloud Platform (GCP)**：約佔10-12%的市佔率。GCP的突出優勢在於除了NVIDIA GPU（例如A3 Ultra實例中的H200）外，還提供TPU（張量處理器），並透過Vertex AI支援LLM開發。其免費層級（如用於測試的Colab）與持續使用折扣政策，使其在研究與小規模訓練領域特別具吸引力。
- **Lambda Cloud**：雖無具體市佔率百分比報告，但估計全球佔比低於5%，主要聚焦於利基用戶群。Lambda在獨立開發者、初創公司及研究團隊（據稱擁有超過10,000名用戶）中極受歡迎，因其提供價格實惠且預先配置的GPU虛擬機器（例如NVIDIA A100/H100），並預載了PyTorch等深度學習框架。其優勢在於操作簡便、相較於超大型雲端廠商更低的成本，以及專注於AI工作負載而無需受制於廣泛的雲端鎖定。

AWS、Azure與GCP的合計市佔率在雲端基礎設施領域約為63%，此主導地位同樣延伸至AI/LLM訓練的GPU服務領域。整體GPU即服務（GPUaaS）市場在2025年的估值約為49.6至50.5億美元，並因AI需求而快速成長。新興的「新雲端」（專精於GPU的供應商）如CoreWeave（擁有超過45,000個GPU並與NVIDIA合作）、Voltage Park及其他超過80家廠商，雖共同佔據較小的市場份額（可能為10-20%總和），但對面臨超大型雲端廠商GPU短缺或高成本的用戶具吸引力。

#### LLM訓練的常用平台選擇
選擇取決於規模、預算與生態系統：
- **大型企業與集團**：通常偏好**AWS、Azure或GCP**，因其具備強大的整合能力（例如AWS SageMaker提供端到端LLM流程、Azure的watsonx類工具、GCP的BigQuery用於資料處理）、安全性與全球可用性。這些平台能處理大規模訓練任務，但成本可能較高（例如H100 GPU每小時4-10美元），且有時因需求旺盛而面臨資源可用性問題。
- **初創公司、研究人員與獨立開發者**：許多選擇**Lambda Cloud**或類似利基平台如CoreWeave，以獲得更經濟的價格（例如A100每小時1-3美元）、簡易設置（預載Jupyter notebooks與CUDA）及靈活性。Lambda因無超額訂閱與快速資源配置而備受讚譽，非常適合原型開發或小規模LLM微調。
- **影響選擇的關鍵因素**：
  - **成本**：超大型雲端廠商提供折扣（Spot/保留實例），但如Lambda等利基平台在純GPU計算上提供更佳性價比。
  - **可用性**：GPU短缺（例如H100）促使用戶尋求替代方案；Lambda與CoreWeave通常有較佳的庫存狀況。
  - **功能**：在託管式訓練方面，超大型雲端廠商佔優；在原始算力方面，利基型供應商表現出色。
  - **趨勢**：2025年，混合方法日益普及——例如在Lambda/CoreWeave上進行訓練，並於AWS/Azure上部署。GCP/AWS的免費層級對初學者具吸引力。

總體而言，儘管超大型雲端廠商在企業級LLM訓練中佔據主導地位，但如Lambda等AI專用供應商的崛起正逐步改變市場份額分佈，尤其對成本敏感型用戶而言更是如此。

[2025年機器學習與AI的GPU：本地部署與雲端對比](https://mobidev.biz/blog/gpu-machine-learning-on-premises-vs-cloud)  
[2025年頂級30家雲端GPU供應商及其GPU規格](https://research.aimultiple.com/cloud-gpu-providers/)  
[2025年AI雲端供應商比較：Coreweave、Lambda...](https://www.ankursnewsletter.com/p/comparing-ai-cloud-providers-in-2025)  
[2025年全球21+家頂級雲端服務供應商](https://www.cloudzero.com/blog/cloud-service-providers/)  
[2025年AWS vs. Azure vs. Google Cloud：雲端服務綜合比較](https://www.channelinsider.com/cloud-computing/aws-vs-azure-vs-google-cloud/)  
[2025年第一季雲端市場佔有率：AWS微幅下滑，微軟與Google持續成長...](https://www.crn.com/news/cloud/2025/cloud-market-share-q1-2025-aws-dips-microsoft-and-google-show-growth)  
[2025年15+家頂級雲端GPU供應商推薦](https://www.analyticsvidhya.com/blog/2023/12/top-gpus-you-must-explore/)  
[GPU即服務市場規模預計於2034年達318.9億美元](https://www.precedenceresearch.com/gpu-as-a-service-market)  
[2025年雲端運算市場規模與趨勢分析](https://www.cloudzero.com/blog/cloud-computing-market-size/)  
[2025年12家最佳AI/ML GPU雲端供應商](https://northflank.com/blog/12-best-gpu-cloud-providers)  
[亞馬遜與微軟持續領跑全球雲端市場](https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/)