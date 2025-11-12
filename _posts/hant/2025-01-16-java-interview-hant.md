---
audio: false
generated: false
lang: hant
layout: post
title: Java後端工程師面試
translated: true
type: note
---

**Java 核心 (20 分)**

1. 理解 OOP 原則：封裝、繼承、多型、抽象。

2. Java 泛型：型別參數的使用、有界型別和萬用字元泛型。

3. Java 多執行緒：建立執行緒、執行緒生命週期和執行緒間通訊。

4. JVM 記憶體管理：堆疊、堆疊、PermGen/Survivor 空間、垃圾回收演算法。

5. 異常處理：受檢異常與非受檢異常、try-catch 區塊、finally 和多重 catch。

6. Java 序列化：Serializable 介面、使用 writeObject 和 readObject 的自訂序列化。

7. Java Collections Framework：List、Set、Map、Queue 介面及其實作。

8. Lambda 表達式和函數式介面：使用 predicates、consumers、suppliers 和 functions。

9. Stream API：中間操作和終端操作、並行串流和串流管道。

10. Reflection API：在執行時存取類別、方法和欄位、註解處理。

11. Java IO 與 NIO：檔案處理的差異、基於通道的 I/O 和非阻塞 I/O。

12. Java Date and Time API：使用 LocalDate、LocalDateTime 和 Duration。

13. Java 網路：Socket 程式設計、URL 連線和 HTTP 客戶端。

14. Java 安全性：加密、數位簽章和安全編碼實踐。

15. Java 模組：理解 JPMS 和模組化。

16. Java 列舉：enum 的使用、ordinal 值和 enum 中的自訂方法。

17. Java 註解：內建註解、自訂註解和註解處理。

18. Java Concurrency Utilities：CountDownLatch、CyclicBarrier、Semaphore 和 Exchanger。

19. Java 記憶體洩漏：原因、偵測和預防策略。

20. Java 效能調校：JVM 選項、分析工具和記憶體最佳化技術。

**Spring 生態系統 (20 分)**

21. Spring IoC 容器：依賴注入、bean 生命週期和範圍。

22. Spring Boot 自動設定：Spring Boot 如何自動設定 bean。

23. Spring Data JPA：儲存庫模式、CRUD 操作和查詢方法。

24. Spring Security：身份驗證、授權和保護 REST API。

25. Spring MVC：控制器方法、請求映射和視圖解析。

26. Spring Cloud：使用 Eureka 進行服務發現、使用 Ribbon 進行負載平衡。

27. Spring AOP：面向切面程式設計、橫切關注點和通知類型。

28. Spring Boot Actuator：監控端點、健康檢查和指標收集。

29. Spring Profiles：環境特定設定和設定檔啟動。

30. Spring Boot Starter Dependencies：使用 starters 簡化依賴管理。

31. Spring Integration：整合不同系統、訊息傳遞和配接器。

32. Spring Batch：批次處理、作業排程和步驟實作。

33. Spring Cache：快取策略、註解和快取管理器。

34. Spring WebFlux：響應式程式設計、非阻塞 I/O 和 WebFlux 框架。

35. Spring Cloud Config：微服務的集中式設定管理。

36. Spring Cloud Gateway：API 閘道模式、路由和過濾。

37. Spring Boot Testing：使用 @SpringBootTest、MockMvc 和 TestRestClient。

38. Spring Data REST：將儲存庫公開為 RESTful 服務。

39. Spring Cloud Stream：與 RabbitMQ 和 Kafka 等訊息代理整合。

40. Spring Cloud Sleuth：微服務中的分散式追蹤和記錄。

**微服務架構 (20 分)**

41. 服務發現：Eureka、Consul 和 Zookeeper 的工作原理。

42. API 閘道：API 閘道中的模式、路由和安全性。

43. 斷路器：使用 Hystrix、Resilience4j 實現韌性。

44. 事件驅動架構：事件溯源、訊息代理和事件處理器。

45. RESTful API 設計：HATEOAS、無狀態設計和 REST 約束。

46. GraphQL：實作 GraphQL API、結構定義和解析器。

47. 微服務通訊：同步與非同步通訊。

48. Saga 模式：跨服務管理分散式交易。

49. 健康檢查：實作存活性和就緒性探針。

50. 合約優先開發：使用 Swagger 處理 API 合約。

51. API 版本控制：RESTful API 的版本控制策略。

52. 速率限制：實作速率限制以防止濫用。

53. 斷路器模式：實作後備和重試機制。

54. 微服務部署：使用 Docker、Kubernetes 和雲端平台。

55. 服務網格：理解 Istio、Linkerd 及其優勢。

56. 事件協作：Saga 與編排模式。

57. 微服務安全性：OAuth2、JWT 和 API 閘道。

58. 監控與追蹤：Prometheus、Grafana 和 Jaeger 等工具。

59. 微服務測試：整合測試、合約測試和端到端測試。

60. 每個服務的資料庫：微服務中的資料管理和一致性。

**資料庫與快取 (20 分)**

61. SQL 聯結：內聯結、外聯結、左聯結、右聯結和交叉聯結。

62. ACID 屬性：交易中的原子性、一致性、隔離性、持久性。

63. NoSQL 資料庫：文件儲存、鍵值儲存和圖形資料庫。

64. Redis 快取：記憶體內資料儲存、資料結構和持久化選項。

65. Memcached 與 Redis：快取解決方案比較。

66. 資料庫分片：水平分割和負載平衡。

67. ORM 框架：Hibernate、MyBatis 和 JPA 規範。

68. JDBC 連線池：DataSource 實作和連線生命週期。

69. 全文搜尋：在 Elasticsearch 等資料庫中實作搜尋。

70. 時間序列資料庫：用於時間序列資料的 InfluxDB、OpenTSDB。

71. 交易隔離等級：讀未提交、讀已提交、可重複讀、序列化。

72. 索引策略：B-tree、雜湊索引和複合索引。

73. 資料庫複寫：主從、主主設定。

74. 資料庫備份與復原：資料保護策略。

75. 資料庫分析：SQL Profiler、慢查詢記錄等工具。

76. NoSQL 一致性模型：最終一致性、CAP 定理。

77. 資料庫遷移：使用 Flyway、Liquibase 進行結構描述變更。

78. 快取策略：Cache-aside、read-through、write-through 模式。

79. 快取失效：管理快取過期和失效。

80. 資料庫連線池：HikariCP、Tomcat JDBC 池設定。

**並行與多執行緒 (20 分)**

81. 執行緒生命週期：新建、可執行、執行中、阻塞、等待、終止。

82. 同步機制：鎖、synchronized 區塊和內建鎖。

83. 可重入鎖：相對於 synchronized 區塊的優勢、公平性和超時。

84. Executor Framework：ThreadPoolExecutor、ExecutorService 和執行緒池設定。

85. Callable 與 Runnable：差異與使用場景。

86. Java 記憶體模型：可見性、happens-before 關係和記憶體一致性。

87. Volatile 關鍵字：確保變數變更在執行緒間的可見性。

88. 死結預防：避免和偵測死結。

89. 非同步程式設計：使用 CompletableFuture 進行非阻塞操作。

90. ScheduledExecutorService：以固定速率和延遲排程任務。

91. 執行緒池：固定、快取和排程執行緒池。

92. 鎖分段：使用分段鎖減少鎖競爭。

93. 讀寫鎖：允許多個讀取者或單一寫入者。

94. 等待與通知機制：使用 wait/notify 進行執行緒間通訊。

95. 執行緒中斷：處理中斷和設計可中斷任務。

96. 執行緒安全類別：實作執行緒安全的單例模式。

97. Concurrency Utilities：CountDownLatch、CyclicBarrier、Semaphore。

98. Java 8+ 並行功能：並行串流、fork-join 框架。

99. 多核心程式設計：並行處理的挑戰與解決方案。

100. 執行緒傾印與分析：使用執行緒傾印識別問題。

**網頁伺服器與負載平衡 (20 分)**

101. Apache Tomcat 設定：設定連接器、context.xml 和 server.xml。

102. Nginx 作為反向代理：設定 proxy_pass、上游伺服器和負載平衡。

103. HAProxy 用於高可用性：設定故障轉移和工作階段持久性。

104. 網頁伺服器安全性：SSL/TLS 設定、安全標頭和防火牆規則。

105. 負載平衡演算法：輪詢、最少連線、IP 雜湊。

106. 伺服器端快取：使用 Varnish、Redis 或記憶體內快取。

107. 監控工具：使用 Prometheus、Grafana 和 New Relic 進行伺服器監控。

108. 生產環境記錄：使用 ELK stack 或 Graylog 進行集中式記錄。

109. 水平與垂直擴充：理解權衡與使用場景。

110. 網頁伺服器效能調校：調整工作執行緒、連線超時和緩衝區。

111. 反向代理快取：設定快取標頭和過期時間。

112. 網頁伺服器負載測試：使用 Apache JMeter、Gatling 等工具進行效能測試。

113. SSL 卸載：在負載平衡器處理 SSL/TLS 終止。

114. 網頁伺服器強化：安全最佳實踐和弱點評估。

115. 動態與靜態內容服務：最佳化伺服器設定。

116. 網頁伺服器叢集：為高可用性設定叢集。

117. 網頁伺服器身份驗證：實作基本、摘要和 OAuth 身份驗證。

118. 網頁伺服器記錄格式：常見記錄格式和解析工具。

119. 網頁伺服器資源限制：設定連線、請求和頻寬的限制。

120. 網頁伺服器備份與復原：災難復原策略。

**CI/CD 與 DevOps (20 分)**

121. Jenkins Pipeline as Code：為 CI/CD 管道編寫 Jenkinsfile。

122. Docker 容器化：Dockerfile 建立、多階段建置和容器編排。

123. Kubernetes 編排：部署、服務、Pod 和擴充策略。

124. GitOps 原則：使用 Git 進行基礎設施和設定管理。

125. Maven 和 Gradle 建置工具：依賴管理、外掛和建置生命週期。

126. 單元與整合測試：使用 JUnit、Mockito 和 TestNG 編寫測試。

127. 程式碼覆蓋率工具：使用 Jacoco 測量程式碼覆蓋率。

128. 靜態程式碼分析：使用 SonarQube 等工具進行程式碼品質檢查。

129. 基礎設施即程式碼：使用 Terraform、CloudFormation 進行基礎設施佈建。

130. 藍綠部署：在部署期間最小化停機時間。

131. 金絲雀部署：新功能的漸進式發布。

132. CI 管道中的自動化測試：將測試整合到建置階段。

133. 環境管理：使用 Ansible、Chef 或 Puppet 進行設定管理。

134. CI/CD 最佳實踐：持續整合、持續部署和持續交付。

135. 回滾策略：在部署失敗時實作自動回滾。

136. 安全掃描：在管道中整合 SAST、DAST 等安全檢查。

137. 微服務的 CI/CD 管道：管理多個服務的管道。

138. 監控 CI/CD 管道：對管道失敗和效能問題發出警報。

139. DevOps 工具生態系統：理解 Docker、Kubernetes、Jenkins、Ansible 等工具。

140. 雲端原生應用的 CI/CD：在雲端平台上部署應用程式。

**設計模式與最佳實踐 (20 分)**

141. 單例模式：實作執行緒安全的單例。

142. 工廠模式：在不指定具體類別的情況下建立物件。

143. 策略模式：封裝演算法並在它們之間切換。

144. SOLID 原則：理解並應用單一職責、開閉、里氏替換、介面隔離、依賴反轉。

145. 依賴注入：減少耦合並提高程式碼可維護性。

146. 事件溯源模式：儲存事件以重建應用程式狀態。

147. CQRS 架構：分離命令和查詢職責。

148. 可擴充性設計：使用水平擴充、分片和負載平衡。

149. 程式碼重構技術：提取方法、重新命名變數和簡化條件式。

150. 整潔程式碼實踐：編寫可讀、可維護和自我說明的程式碼。

151. 測試驅動開發：在實作之前編寫測試。

152. 程式碼版本控制：使用 GitFlow、主幹式開發等 Git 分支策略。

153. 可維護性設計：使用模組化設計、關注點分離。

154. 需避免的反模式：God classes、義大利麵程式碼和緊密耦合。

155. 安全性設計：實作最小權限、深度防禦。

156. 效能設計：最佳化演算法、減少 I/O 操作。

157. 可靠性設計：實作冗餘、容錯和錯誤處理。

158. 可擴充性設計：使用外掛、擴充功能和開放 API。

159. 可用性設計：確保 API 直觀且文件完善。

160. 可測試性設計：編寫易於測試和模擬的程式碼。

**安全性 (20 分)**

161. OAuth2 與 JWT：實作基於令牌的身份驗證。

162. 基於角色的存取控制：為使用者分配角色和權限。

163. 安全標頭：實作內容安全政策、X-Frame-Options。

164. SQL 注入預防：使用預備語句和參數化查詢。

165. 跨網站指令碼保護：清理輸入和輸出。

166. 加密與解密：使用 AES、RSA 保護資料。

167. 安全編碼實踐：避免緩衝區溢位等常見弱點。

168. 實作審計追蹤：記錄使用者操作和系統事件。

169. 處理敏感資料：使用雜湊演算法安全儲存密碼。

170. 合規性：GDPR、PCI-DSS 和資料保護法規。

171. 實作雙重身份驗證：增加額外的安全層。

172. 安全測試：滲透測試、弱點評估。

173. 安全通訊協定：實作 SSL/TLS 進行資料加密。

174. 安全工作階段管理：管理工作階段令牌和超時。

175. 實作網頁應用程式防火牆：防範常見攻擊。

176. 安全監控與警報：使用 SIEM 等工具進行威脅偵測。

177. 微服務中的安全最佳實踐：保護服務對服務的通訊。

178. 實作 CAPTCHA 防範機器人：防止自動化攻擊。

179. CI/CD 管道中的安全性：在建置期間掃描弱點。

180. 實作安全設計：從開發過程開始就納入安全性。

**效能調校與最佳化 (20 分)**

181. 分析 Java 應用程式：使用 JProfiler、VisualVM 等工具進行效能分析。

182. 垃圾回收調校：調整 GC 參數以提升效能。

183. 資料庫查詢最佳化：索引、查詢重寫和使用執行計畫。

184. 快取策略：使用分散式快取、快取失效機制。

185. 負載測試與壓力測試：識別效能瓶頸。

186. 最佳化 RESTful API：減少回應時間、最小化資料傳輸。

187. 減少網路延遲：使用 CDN、最佳化 API 呼叫。

188. 連線池大小調整：確定資料庫和連線的最佳池大小。

189. 監控與警報設定：使用 Prometheus、Grafana 進行即時監控。

190. 識別與解決瓶頸：分析 CPU、記憶體和 I/O 使用情況。

191. 最佳化 Java 堆積設定：為不同環境設定適當的堆積大小。

192. 減少垃圾回收暫停：使用 G1GC、ZGC 用於低延遲應用。

193. 最佳化磁碟 I/O：使用 SSD、RAID 組態和檔案系統最佳化。

194. 快取與儲存：決定何時快取資料而非儲存在資料庫中。

195. 最佳化記錄：減少記錄開銷和管理記錄量。

196. 最佳化並行存取：有效使用鎖並最小化競爭。

197. 分析記憶體使用：識別記憶體洩漏和最佳化物件配置。

198. 最佳化執行緒池大小：在過少和過多執行緒之間取得平衡。

199. 最佳化資料結構：為特定使用案例選擇正確的資料結構。

200. 效能指標與 KPI：為應用程式定義和追蹤關鍵效能指標。