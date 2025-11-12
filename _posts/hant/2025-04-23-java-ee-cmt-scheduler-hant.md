---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Java EE 容器管理任務排程器
translated: true
type: note
---

**ManagedScheduledExecutorService** 是由應用程式伺服器（例如 WebSphere、WebLogic、WildFly）提供的 Java EE（Jakarta EE）資源，允許您排程任務在未來或定期執行，類似於標準 Java SE 中的 `ScheduledExecutorService`，但具有**容器管理的優勢**：

---

### 運作原理

* **與容器整合**
  它由應用程式伺服器管理，這意味著任務會以應用程式的安全上下文、類別載入器和交易邊界執行。這避免了 Java EE 中非管理執行緒的常見問題。

* **排程功能**
  您可以排程任務：

  * 延遲後執行一次。
  * 以固定速率執行（例如每 5 秒）。
  * 在執行之間以固定延遲執行。

* **生命週期管理**
  容器負責執行緒池的生命週期、清理和資源管理。您不需要像普通的 `ExecutorService` 那樣手動關閉它。

---

### 逾時設定

* 執行緒池本身沒有單一的「逾時」設定，但有兩個相關事項：

  * **任務執行逾時**：您可以使用 `ManagedTaskListener` 包裝任務，並指定如 `ManagedTask.TIMEOUT` 的屬性（取決於廠商支援）。有些伺服器允許您設定預設任務逾時，以便容器取消懸置的任務。
  * **Future get() 逾時**：與常規 `ScheduledExecutorService` 一樣，您可以使用 `future.get(timeout, unit)` 來限制等待結果的時間。

因此，「逾時」通常是針對每個任務，而不是在池層級。

---

### 池大小配置

* 每個應用程式伺服器都有其後端執行緒池的配置。
  例如：

  * **WebSphere Liberty / Traditional**：在 `server.xml` 中的 `<managedScheduledExecutorService>` 下配置池，具有如 `corePoolSize` 和 `maximumPoolSize` 的屬性。
  * **WebLogic**：透過管理主控台或 `weblogic-managed-executor` 進行配置。
  * **WildFly / JBoss EAP**：在 EE 子系統下配置。

* 典型的池配置包括：

  * **核心池大小**：保持存活的最小執行緒數。
  * **最大池大小**：最大並發執行緒數。
  * **佇列大小 / 拒絕策略**：當所有執行緒都忙碌時會發生什麼。
  * **保持存活時間**：空閒執行緒在釋放前保持存活的時間。

---

✅ **總結**：
`ManagedScheduledExecutorService` 類似於 Java SE 的排程器，但具有容器感知能力，因此您可以在 Java EE 應用程式中獲得安全的執行緒處理。逾時通常按任務應用（透過 API 或伺服器配置），而池大小（核心/最大執行緒數）在容器層級配置，而不是在您的應用程式代碼中。

---

您想讓我展示 **WebSphere Liberty 範例配置片段** 來設定池大小和逾時嗎？