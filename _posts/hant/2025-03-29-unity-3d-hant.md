---
audio: false
generated: true
lang: hant
layout: post
title: Unity3D
translated: true
type: note
---

Unity3D 是一款強大的遊戲引擎，用於創建 2D 和 3D 遊戲、模擬及互動應用程式。以下是入門步驟指南：

---

### **1. 安裝 Unity**
1. 從 [Unity 官方網站](https://unity.com/) 下載並安裝 **Unity Hub**。
2. 在 Unity Hub 內安裝 **最新穩定版本的 Unity**。
3. 如有需要，安裝額外模組（例如 Android/iOS 支援）。

---

### **2. 創建新專案**
1. 開啟 **Unity Hub** → 點擊 **New Project**。
2. 選擇 **模板**（例如 2D、3D 或 URP 以獲得更好的圖形效果）。
3. 設定 **專案名稱** 和儲存位置 → 點擊 **Create**。

---

### **3. 認識 Unity 介面**
- **Scene View**：構建遊戲世界的工作區。
- **Game View**：顯示玩家將看到的畫面。
- **Hierarchy**：包含場景中的所有物件。
- **Inspector**：允許編輯物件屬性。
- **Project Panel**：儲存所有資源（模型、腳本、音效等）。
- **Console**：顯示錯誤、警告和日誌。

---

### **4. 創建第一個遊戲物件**
1. 前往 **GameObject** → **3D Object** → **Cube**（或任何其他形狀）。
2. 在 **Hierarchy** 中點選它，然後在 **Inspector** 中使用 **Transform** 組件調整其位置。

---

### **5. 編寫第一個腳本**
1. 前往 **Assets → Create → C# Script**。
2. 將其命名為 **PlayerController** 並雙擊以在 **Visual Studio** 中開啟。
3. 編寫一個簡單的腳本來移動物件：

   ```csharp
   using UnityEngine;

   public class PlayerController : MonoBehaviour
   {
       public float speed = 5f;

       void Update()
       {
           float moveX = Input.GetAxis("Horizontal") * speed * Time.deltaTime;
           float moveZ = Input.GetAxis("Vertical") * speed * Time.deltaTime;
           transform.Translate(moveX, 0, moveZ);
       }
   }
   ```

4. 儲存腳本並在 Inspector 中 **將其附加到 GameObject**。

---

### **6. 播放與測試**
1. 點擊工具列中的 **Play** 來測試遊戲。
2. 使用 **WASD 或方向鍵** 移動你的物件。
3. 按下 **Stop** 返回編輯模式。

---

### **7. 深入學習與改進**
- **探索 Unity Asset Store** 以獲取免費模型和腳本。
- **使用 Unity Learn** ([learn.unity.com](https://learn.unity.com/)) 查看官方教程。
- **加入 Unity 社群**，參與論壇、YouTube 或 Discord。

---

需要協助開發特定類型的遊戲嗎？🚀