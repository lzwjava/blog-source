---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: AWS 重大故障歷史回顧
translated: true
type: note
---

### AWS 史上的重大服務中斷

自 2006 年以來，Amazon Web Services（AWS）支撐了互聯網的大部分運作，但如同任何大規模基礎設施，它偶爾也會面臨服務中斷。相對於其龐大的業務規模，中斷事件並不頻繁，但重大事故可能對依賴其服務的社交媒體到金融平台等造成連鎖影響。下表總結了歷史上關鍵的中斷事件，聚焦於影響範圍廣泛或衝擊力較高的事故。這些事件取材於記錄在案、影響多項服務或知名客戶的案例。

| 日期              | 受影響服務/區域           | 原因                          | 影響 |
|-------------------|---------------------------|--------------------------------|--------|
| 2008年2月15日 | S3、EC2（全球）         | 未說明的技術故障 | 中斷了多個網站的圖片儲存與託管服務，標誌著 AWS 早期遭遇的重大問題之一。 |
| 2011年4月21日    | 多項服務（美國東部-1） | 數據中心長時間故障 | 導致 Reddit、Quora 等高流量網站癱瘓數小時，凸顯了早期可靠性疑慮。 |
| 2017年2月28日 | EC2、S3、RDS 等多項服務（美國東部-1） | 人為失誤：除錯期間輸入錯誤指令 | 長達數小時的中斷影響了 Slack、Docker、Exora 等服務；估計損失達數億美元；AWS 雲端儀表板亦當機。 |
| 2021年12月7日  | 控制層服務包括 EC2、RDS、Lambda（美國東部-1） | 容錯轉移期間控制層軟件漏洞引發連鎖故障 | 近年歷時最長的中斷（超過 8 小時）；影響 Netflix、Disney+、Capital One 及政府網站；12月15日發生第二次較小規模中斷，影響類似服務。 |
| 2023年6月13日     | EC2 及相關服務（多區域） | 未說明的區域性問題 | 大範圍當機波及新聞機構（如美聯社、波士頓環球報）及交通系統（紐約大都會運輸署），持續數小時。 |
| 2025年10月20日  | DynamoDB 端點、EC2 啟動及多項服務（美國東部-1，並產生全球連鎖影響） | DynamoDB 服務端點 DNS 解析失敗 | 長達整日的服務中斷（始於10月19日太平洋時間晚間，至10月20日下午解決）；影響 Snapchat、Reddit、Roblox、Fortnite、銀行（如勞埃德銀行）及英國稅務海關總署；因阻礙約三分之一互聯網應用程式存取而影響數百萬用戶；AWS 為恢復服務限流部分操作。 |

這些事件通常源於人為錯誤、網絡問題或環境因素，而 AWS 已透過多區域部署等冗余措施提升韌性。2025年的中斷事件再次凸顯過度依賴 AWS 最繁忙區域——美國東部-1 的持續風險。

詳細資訊請參閱：
- [AWS 雲端與數據中心中斷史](https://www.datacenterknowledge.com/outages/a-history-of-aws-cloud-and-data-center-outages)
- [史上最大 AWS 中斷：2021年12月7日事件](https://aws.plainenglish.io/the-biggest-aws-outage-in-history-the-december-7-2021-us-east-1-meltdown-and-lessons-learned-2efab5a02de5)
- [AWS 中斷原因解析](https://www.bbc.com/news/articles/cev1en9077ro)
- [AWS 關於2025年10月中斷事件的最新說明](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)