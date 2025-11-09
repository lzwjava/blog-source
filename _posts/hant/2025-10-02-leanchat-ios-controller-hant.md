---
audio: false
generated: true
image: false
lang: hant
layout: post
model: deepseek/deepseek-v3.2-exp
title: LeanChat iOS 聊天室控制器
translated: true
type: note
---

這是一個來自 LeanChat iOS 應用程式的**聊天室視圖控制器**（`CDChatRoomVC`），它實現了功能完整的聊天介面。以下是其核心功能的細分說明：

## 🏗️ **核心架構**
- **繼承自** `XHMessageTableViewController`（一個訊息 UI 框架）
- **使用 LeanCloud**（AVIM）作為即時通訊的後端
- **管理** AVIMConversation 用於群組或一對一聊天

## 📱 **主要功能**

### **訊息處理**
- **傳送訊息**：文字、圖片、影片、語音、表情和位置
- 透過通知**即時接收訊息**
- **訊息狀態追蹤**：傳送中、已傳送、已送達、傳送失敗
- **重試失敗的訊息**
- 透過分頁**載入訊息記錄**

### **媒體支援**
- **圖片**：從相機拍攝或從相簿選取
- **語音訊息**：錄製並播放，帶有視覺動畫
- **影片**：傳送和顯示
- **位置分享**：帶有地圖預覽
- **表情/貼圖**：自訂表情包

### **UI 元件**
- **訊息氣泡**：針對傳送/接收的不同樣式
- **輸入工具列**：帶有表情選擇器和媒體選項
- **狀態指示器**：顯示連線狀態
- **時間戳顯示**：用於訊息
- **用戶頭像顯示**

### **資料管理**
- **本地快取**訊息和用戶資料
- **離線支援**，帶有失敗訊息儲存
- **媒體檔案快取**（圖片、影片、音訊）
- **對話狀態持久化**

## 🔧 **技術實現**

### **生命週期管理**
```objc
- viewDidLoad: 設定 UI、註冊通知、載入初始訊息
- viewDidAppear/Disappear: 管理對話狀態和音訊播放
- dealloc: 清理觀察者和資源
```

### **通知處理**
- `kCDNotificationMessageReceived`：新進訊息
- `kCDNotificationMessageDelivered`：訊息送達確認
- `kCDNotificationConversationUpdated`：對話元資料變更
- `kCDNotificationConnectivityUpdated`：網路連線變更

### **訊息處理流程**
1. **轉換** AVIM 訊息為 XHMessage 格式以供顯示
2. **快取**媒體檔案和用戶資料到本地
3. **更新** UI 並滾動至最新訊息
4. **追蹤**送達狀態並相應更新

### **錯誤處理**
- **網路故障**：自動重試並提供視覺回饋
- **檔案操作**：本地儲存錯誤處理
- **訊息傳送**：失敗時回退到本地儲存

此控制器作為主要的聊天介面，處理從用戶互動到後端通訊的所有事務，同時提供流暢、響應迅速的訊息體驗。