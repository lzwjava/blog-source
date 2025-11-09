---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Azure 歷史上重大服務中斷事件
translated: true
type: note
---

Microsoft Azure 自 2010 年推出以來，曾因組態錯誤、硬體故障或天氣等外部事件經歷多次重大中斷。以下按時間順序彙整影響範圍跨區域或服務的顯著事件，內容援引官方報告、歷史分析與事件審查，並標註日期、原因、受影響區域及持續時間（若可取得）。

| 日期 | 原因 | 受影響區域/服務 | 持續時間/影響 |
|------|-------|---------------------------|-----------------|
| 2012年2月29日 | 程式碼中閏年計算錯誤 | 北美（Azure 計算服務） | 約8小時；用戶應用程式管理與服務中斷 |
| 2012年7月26日 | 網路設備配置錯誤 | 西歐（Azure 計算服務） | 超過2小時；歐洲部分服務不可用 |
| 2013年2月22日 | SSL 憑證過期 | 全球（Azure 儲存服務） | 數小時；發放服務抵扣額；波及 Xbox Live、Music 及 Video |
| 2013年10月30日 | 部分計算服務中斷（節流機制問題） | 全球（Azure 計算服務、管理功能） | 約3-4小時；影響檔案上傳與網站管理 |
| 2013年11月22日 | 儲存與網路問題 | 美國中北部（Xbox Live） | Xbox One 上市日當天數小時；客戶影響輕微但關注度極高 |
| 2014年11月19日 | 組態變更導致 Blob 儲存無限迴圈 | 全球（20多項服務，含 Azure 儲存服務） | 約6-10小時；多區域容量下降；影響 Xbox Live、MSN 及 Visual Studio Online |
| 2016年9月15日 | 全球 DNS 中斷 | 全球（Azure DNS） | 約2小時；廣泛服務中斷 |
| 2017年3月7日及23日 | 多重事件（網路與儲存問題） | 全球（Office 365、Skype、Xbox Live） | 每次最長超過16小時；大範圍用戶存取問題 |
| 2017年9月29日 | 維護期間消防氣體釋放觸發系統關機 | 美國區域（多項服務） | 約7小時；間歇性故障 |
| 2018年9月4日 | 雷擊導致電壓突波及冷卻系統失效 | 美國中南部、多區域（40多項服務） | 超過25小時，部分影響持續達3天；服務大規模停擺 |
| 2020年1月25日 | Azure SQL 資料庫後端相依性故障 | 全球（幾乎所有區域，含美國政府/國防部） | 約6小時；影響 SQL 資料庫、Application Gateway、Bastion 及防火牆 |
| 2021年4月1日 | 網路基礎架構廣泛 DNS 問題 | 全球（美國、歐洲、亞洲等） | 約1.5小時；影響核心網路相依服務 |
| 2022年6月1日 | Azure Active Directory 登入記錄問題 | 全球（多區域） | 約9.5小時；影響 AAD、Sentinel、Monitor 及 Resource Manager |
| 2022年6月29日 | 未說明的後端不穩定 | 全球（數十個區域） | 約24小時間歇性中斷；影響防火牆、Synapse、備份等服務 |
| 2023年1月25日 | 有缺陷的路由器指令導致網路中斷 | 全球（25個以上區域，含美國東部、西歐） | 約3.5小時；M365（Teams、Outlook）、SharePoint 及 Office 365 延遲與故障 |
| 2023年6月9日 | 匿名組織 Anonymous Sudan 聲稱的 DDoS 攻擊 | 全球（Azure 入口網站與雲端服務） | 約2.5小時；入口網站及相關服務癱瘓 |
| 2024年11月13日 | 儲存服務 DNS 解析失敗 | 多區域（美國東部/2、美國中部、美國西部/2等） | 約8.5小時；影響 Databricks 與儲存帳戶 |
| 2024年12月26日 | 可用性區域電力事件 | 美國中南部（03區域） | 約18小時；影響儲存、虛擬機器、Cosmos DB、SQL 資料庫等 |
| 2025年1月9日 | 網路中斷 | 美國東部2 | 超過48小時；影響 Databricks、Synapse、Functions、App Service 及虛擬機器 |
| 2025年9月10日 | 節流變更導致分配器服務超載 | 美國東部2（02/03區域） | 約10.5小時；虛擬機器操作效能下降，影響備份、Batch、Kubernetes 及 Synapse |
| 2025年9月26-27日 | 組態變更中的憑證值格式錯誤 | 瑞士北部（多區域） | 約22小時；API 管理、App Service、Cosmos DB、虛擬機器及 Sentinel 大範圍中斷 |
| 2025年10月9日 | Azure Front Door 控制平面缺陷 | 歐洲與非洲 | 約8小時；入口網站與服務延遲/超時（非洲故障率達17%） |
| 2025年10月9日 | 自動化腳本後續移除組態 | 全球（管理入口網站） | 約4小時；AFD 事件後 Azure 入口網站等存取問題 |

這些事件僅為總體事件中的一部分，但依影響範圍與持續時間皆屬最嚴重類別。微軟通常會發布事後審查報告供學習參考，隨著時間推移服務可用性已提升，其服務等級協議目標為 99.99% 正常運行時間。

## 參考資料
- [Microsoft Azure 中斷事件歷史](https://www.datacenterknowledge.com/outages/a-history-of-microsoft-azure-outages)
- [Microsoft Azure 中斷歷史概覽](https://statusgator.com/blog/azure-outage-history/)
- [Azure 狀態歷史](https://azure.status.microsoft/en-us/status/history/)
- [Microsoft Azure 維基百科 - 中斷事件章節](https://en.wikipedia.org/wiki/Microsoft_Azure#Outages)