---
audio: false
generated: true
lang: hant
layout: post
title: 發佈你的 Android 應用程式
translated: true
type: note
---

這是一份詳細指南，針對您關於將 Android 應用程式上傳到小米商店、上傳到 Google Play 以及混淆 Java 程式碼的問題提供解答。

---

### 將 Android 應用程式上傳到小米商店

要將您的 Android 應用程式上傳到小米商店（通常稱為 Mi App Store 或小米 GetApps），您需要遵循小米特定的提交流程。雖然確切細節可能隨時間變化，但以下是基於典型應用商店工作流程的一般概述：

1.  **建立開發者帳戶**：訪問小米的開發者入口網站（可能透過其官方開發者網站進入），並註冊開發者帳戶。這可能需要付費或進行驗證流程。
2.  **準備您的應用程式**：確保您的應用程式符合小米的指南，這可能包括技術要求（例如 APK 格式）、內容政策以及為其用戶群（特別是在中國）進行本地化。
3.  **提交您的應用程式**：登入開發者入口網站，上傳您的 APK 或 App Bundle，並提供必要的詳細資訊，例如應用程式描述、螢幕截圖和類別。您可能需要使用 keystore 為您的應用程式簽名，類似於其他應用商店。
4.  **審核流程**：小米將在發佈前審核您的應用程式以確保合規。

由於這裡無法提供具體的最新說明，我強烈建議您查閱小米的官方開發者文件或聯繫其開發者支援以獲取最新要求和入口網站訪問資訊。由於地區政策，小米的流程可能與西方應用商店不同，因此官方來源是您的最佳選擇。

---

### 將 Android 應用程式上傳到 Google Play

將應用程式上傳到 Google Play 是一個有完善文件的流程。以下是逐步操作方法：

1.  **建立 Google Play 開發者帳戶**：
    *   前往 [Google Play Console](https://play.google.com/console) 並註冊。您需要一個 Google 帳戶和一次性費用 25 美元。

2.  **準備發佈版本的應用程式**：
    *   **建置發佈版本**：在 Android Studio 中，生成已簽名的 APK 或 App Bundle（Google 推薦使用 AAB）。使用 "Build > Generate Signed Bundle/APK" 選項。
    *   **應用程式簽名**：您必須使用 keystore 為您的應用程式簽名。您可以：
        *   管理自己的簽署金鑰（請安全儲存）。
        *   選擇加入 **Play App Signing**，在此模式下，您在設定期間上傳金鑰後，由 Google 管理您的金鑰。推薦此方式以方便金鑰管理。
    *   確保您的應用程式符合 Google 的政策（例如內容、隱私）。

3.  **在 Play Console 中設定您的應用程式**：
    *   登入 Play Console，點擊 "Create App"，並填寫詳細資訊，如應用程式名稱、描述、類別和聯絡資訊。
    *   在 "App Releases" 部分上傳您已簽名的 APK 或 AAB（從內部測試軌道開始以驗證所有功能正常）。
    *   添加商店列表資源：螢幕截圖、圖示、功能圖形和隱私政策 URL。

4.  **測試和發佈**：
    *   使用測試軌道（內部、封閉或公開）與選定用戶測試您的應用程式。
    *   準備好後，在 "Production" 下提交審核，並等待 Google 的批准（通常需要幾小時到幾天）。

5.  **發佈後**：透過 Play Console 監控效能並根據需要進行更新。

有關詳細指南，請參閱 Google 官方的 [發佈應用程式](https://developer.android.com/distribute/console) 文件。

---

### 在 Android 應用程式中混淆 Java 程式碼

混淆透過將類別、方法和變數重新命名為無意義的字串、移除未使用的程式碼並對其進行優化，使您的 Java 程式碼更難被反向工程。以下是操作方法：

#### 為什麼要混淆？
*   透過使反編譯的程式碼難以閱讀來保護智慧財產權。
*   透過移除未使用的程式碼來減小 APK 大小。
*   注意：這不是完全的安全措施——敏感資料（例如 API 金鑰）應進行加密或在伺服器端處理。

#### 用於混淆的工具
*   **ProGuard**：一個廣泛使用的工具，與 Android Studio 捆綁，用於縮小、混淆和優化程式碼。
*   **R8**：ProGuard 的現代替代品（自 Android Gradle Plugin 3.4.0 起預設使用），提供類似的功能但具有更好的優化。

#### 如何進行混淆
1.  **在您的專案中啟用混淆**：
    *   打開您應用程式的 `build.gradle` 文件（通常是 `app/build.gradle`）。
    *   在 `buildTypes` 部分，為發佈版本啟用 `minifyEnabled`：
      ```gradle
      android {
          buildTypes {
              release {
                  minifyEnabled true
                  proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
              }
          }
      }
      ```
    *   `minifyEnabled true` 會啟動 R8（或如果明確配置則為 ProGuard）。
    *   `proguardFiles` 指定用於自定義的規則文件。

2.  **自定義規則（可選）**：
    *   編輯您應用程式根目錄中的 `proguard-rules.pro` 文件。
    *   如果需要，添加規則以保持特定的類別或方法不被混淆（例如，為了反射或第三方函式庫）。範例：
      ```proguard
      -keep class com.example.MyClass { *; }
      ```

3.  **建置您的應用程式**：
    *   為發佈版本生成已簽名的 APK/AAB。R8/ProGuard 將自動混淆您的 Java 程式碼。
    *   徹底測試——如果規則設定不正確，混淆可能會破壞功能。

4.  **驗證混淆**：
    *   反編譯您的 APK（例如使用 APKTool 或 JADX）以確保類別/方法名稱已被遮蔽。

#### 限制
*   混淆不能防止所有反向工程；有決心的攻擊者仍然可以分析行為。
*   避免在程式碼中儲存敏感資料——請改用安全的替代方案。

更多資訊，請參閱 Android 的 [縮小、混淆和優化程式碼](https://developer.android.com/studio/build/shrink-code) 指南。

---

### 總結

*   **小米商店**：註冊成為開發者，準備您的應用程式，並透過他們的入口網站提交（請查閱官方文件以獲取具體細節）。
*   **Google Play**：設定開發者帳戶，透過 Play Console 簽署並上傳您的應用程式，並管理發佈。
*   **混淆 Java 程式碼**：在 Android Studio 中使用 ProGuard 或 R8 來保護您的程式碼，但需配合其他安全措施。

如果您在任何部分需要更多詳細資訊，請告訴我！