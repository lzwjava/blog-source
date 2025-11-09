---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: AWS 服務中斷案例分析 2025年10月
translated: true
type: note
---

### 2025年10月20日AWS中斷事件：詳細案例分析

2025年10月20日的AWS中斷是一場源自美國東部（北維吉尼亞）區域（us-east-1）的重大服務中斷，此區域是AWS規模最大且最關鍵的數據中心。事件始於太平洋夏令時間10月19日深夜，持續約16小時，影響超過140項服務，並因該區域的依賴性而產生全球連鎖效應。此事件凸顯了DNS解析、服務相互依賴性及恢復流程中的脆弱環節，對數百萬應用程式、網站及服務用戶造成影響。以下根據AWS官方事後檢討報告及同期記錄進行分析。

#### 時間線
此次中斷事件分階段展開，從問題偵測開始，逐步升級為連鎖故障，最後進入分階段恢復。關鍵時間點（均為太平洋夏令時間）：

| 時間 | 事件 |
|------|-------|
| 晚上11:49（10月19日） | 偵測到us-east-1區域多項AWS服務錯誤率及延遲時間增加。 |
| 凌晨12:11（10月20日） | AWS公開通報錯誤率升高；監測網站如DownDetector上的用戶回報激增。 |
| 凌晨12:26 | 問題鎖定為us-east-1區域DynamoDB API端點的DNS解析失敗。 |
| 凌晨1:26 | 確認DynamoDB API（包括Global Tables）錯誤率偏高。 |
| 凌晨2:22 | 實施初步緩解措施；出現早期恢復跡象。 |
| 凌晨2:24 | DynamoDB DNS問題解決，觸發部分服務恢復——但出現EC2啟動功能受損及Network Load Balancer（NLB）健康檢查失敗。 |
| 凌晨3:35 | DNS完全緩解；多數DynamoDB操作成功，但跨可用區域（AZ）的EC2啟動功能仍受損。 |
| 凌晨4:08 | 持續處理EC2錯誤及Lambda對SQS事件源映射的輪詢延遲。 |
| 凌晨5:48 | 部分可用區域的EC2啟動功能局部恢復；SQS積壓開始清除。 |
| 早上6:42 | 跨可用區域實施緩解措施；AWS對新EC2執行個體啟動實施速率限制以穩定系統。 |
| 早上7:14 | 多項服務持續出現API錯誤及連線問題；對用戶影響的故障達到高峰（例如應用程式中斷）。 |
| 早上8:04 | 調查聚焦於EC2內部網路。 |
| 早上8:43 | 確定網路問題根本原因：EC2內部用於NLB健康監控的子系統出現故障。 |
| 早上9:13 | 對NLB健康檢查實施額外緩解措施。 |
| 早上9:38 | NLB健康檢查完全恢復。 |
| 上午10:03 – 中午12:15 | EC2啟動功能逐步改善；跨可用區域分階段穩定Lambda調用及連線能力。 |
| 下午1:03 – 2:48 | 降低節流限制；處理如Redshift、Amazon Connect及CloudTrail等服務的積壓。 |
| 下午3:01 | 所有服務恢復完全正常運作；預期數小時內清除少量積壓（例如AWS Config、Redshift）。 |
| 下午3:53 | AWS宣布中斷事件解決。 |

用戶在DownDetector等平台上的回報於太平洋夏令時間早上6點左右達到高峰，事件數超過5,000宗後開始下降。

#### 根本原因
此次中斷源於影響us-east-1區域DynamoDB服務端點的DNS解析失敗。DynamoDB作為NoSQL資料庫服務，是許多AWS功能的關鍵「控制平面」——負責處理元資料、工作階段及路由。當DNS無法解析這些端點時，DynamoDB API出現延遲及錯誤率升高。

此初始問題迅速解決，但引發連鎖反應：
- EC2執行個體啟動因依賴DynamoDB儲存元資料而失敗。
- EC2內部子系統（負責監控NLB健康狀態）的潛在錯誤加劇網路連線問題，導致負載平衡及API調用出現更廣泛故障。
- 恢復工作包括實施節流（例如限制EC2啟動及Lambda調用）以防過載，但依賴服務的重試機制進一步加重系統負擔。

AWS確認此非網絡攻擊，而是基礎設施相關故障，可能與有問題的DNS資料庫更新或備份系統失效有關。全球波及效應的發生，是因為us-east-1托管了關鍵控制平面（如IAM及Lambda），即使其他區域的資源亦受影響。

#### 受影響服務
超過142項AWS服務受影響，主要為依賴DynamoDB、EC2或us-east-1端點的服務。核心類別包括：

- **資料庫與儲存**：DynamoDB（主要）、RDS、Redshift、SQS（積壓）。
- **運算與協調**：EC2（啟動）、Lambda（調用、輪詢）、ECS、EKS、Glue。
- **網路與負載平衡**：Network Load Balancer（健康檢查）、API Gateway。
- **監控與管理**：CloudWatch、CloudTrail、EventBridge、IAM（更新）、AWS Config。
- **其他**：Amazon Connect、Athena及全域功能如DynamoDB Global Tables。

並非所有服務完全中斷——許多出現部分錯誤或延遲——但互聯性質意味著即使輕微問題亦會擴散。

#### 影響範圍
此次中斷影響約三分之一依賴互聯網的應用程式，全球估計超過1億用戶受波及。知名案例包括：
- **社交與媒體**：Snapchat（登入失敗）、Reddit（服務中斷）、Twitch（串流問題）。
- **遊戲**：Roblox（伺服器崩潰）、Fortnite（配對失敗）。
- **金融與支付**：Venmo、滙豐銀行等銀行（交易延遲）、英國稅務海關總署（稅務服務）。
- **零售與電子商務**：亞馬遜自身零售網站部分功能；航空公司報到服務（例如達美航空、聯合航空延誤）。
- **其他**：Alexa裝置（語音失敗）、Twilio（通訊故障）。

經濟損失估計超過5億美元，用戶恐慌導致網絡安全掃描激增300%。事件凸顯互聯網集中化問題：us-east-1處理約30%的AWS流量，儘管設計上採用多可用區域，仍成為單點故障源。

#### 解決方案與經驗教訓
AWS透過針對性緩解措施解決問題：DNS修復、EC2/NLB子系統修補及逐步降低節流限制。事後建議包括：
- 重試失敗請求。
- 清除DNS快取。
- 將資源分佈於多個可用區域/區域（例如透過Auto Scaling Groups）。
- 使用服務配額及快取機制緩衝重試帶來的負荷。

更廣泛的啟示包括控制平面需更好冗余、採用AI驅動異常檢測以加速問題分類，及多元化雲端策略。AWS承諾向客戶提供完整根本原因分析（RCA），強調此類事件雖罕見，但揭露了超大規模運營的擴展挑戰。

這是自2021年以來AWS在us-east-1區域最具破壞性的中斷事件，但得益於自動化工具，恢復速度較歷史同類事件更快。

#### 參考資料
- [AWS Health Dashboard: Service Health - 2025年10月20日](https://health.aws.amazon.com/health/status?eventID=arn:aws:health:us-east-1::event/MULTIPLE_SERVICES/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE_BA540_514A652BE1A)
- [AWS中斷分析：2025年10月20日](https://www.thousandeyes.com/blog/aws-outage-analysis-october-20-2025)
- [亞馬遜大規模AWS中斷揭露現代互聯網關鍵弱點](https://finance.yahoo.com/news/amazons-massive-aws-outage-points-to-a-key-weakness-in-the-modern-internet-145418180.html)
- [亞馬遜AWS中斷成因及為何眾多主要應用程式離線？](https://www.aljazeera.com/news/2025/10/21/what-caused-amazons-aws-outage-and-why-did-so-many-major-apps-go-offline)
- [10月20日AWS中斷：DynamoDB的DNS故障如何癱瘓互聯網](https://medium.com/@ansababy/aws-outage-on-october-20-how-a-dns-glitch-in-dynamodb-disrupted-the-internet-40e1f0440a12)
- [更新 - AWS服務正常運作](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)
- [AWS服務中斷——大規模中斷後即時更新](https://www.tomsguide.com/news/live/amazon-outage-october-2025)