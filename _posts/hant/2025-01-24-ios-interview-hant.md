---
audio: false
generated: false
lang: hant
layout: post
title: iOS 工程師面試
translated: true
type: note
---

### SwiftUI

1. 什麼是 SwiftUI？它與 UIKit 有何不同？
   - SwiftUI 是 Apple 用於構建使用者介面的現代化框架，與 UIKit 的命令式方法相比，它提供了宣告式語法。它簡化了 UI 的建立和更新。

2. 解釋 SwiftUI 中的宣告式 UI 概念。
   - 宣告式 UI 描述的是期望的結果，而非實現該結果的步驟。SwiftUI 會根據宣告的狀態來構建和更新 UI。

3. 如何在 SwiftUI 中建立自訂視圖？
   - 建立一個符合 `View` 協議的新結構體，並在 `body` 屬性中定義其內容。

4. 使用 SwiftUI 相比 UIKit 有哪些優勢？
   - 優勢包括宣告式語法、更簡易的狀態管理，以及為 macOS、iOS 和其他 Apple 平台提供統一的介面。

5. 如何在 SwiftUI 中處理狀態管理？
   - 使用 `@State` 管理本地狀態，`@ObservedObject` 管理可觀察類別，以及 `@EnvironmentObject` 管理全域狀態。

6. 解釋 `@State` 和 `@Binding` 之間的區別。
   - `@State` 用於本地狀態管理，而 `@Binding` 用於在視圖之間共享狀態。

7. 如何在 SwiftUI 中使用 `@EnvironmentObject`？
   - `@EnvironmentObject` 用於存取在視圖層級結構中向下傳遞的物件。

8. `@ObservedObject` 和 `@StateObject` 的用途是什麼？
   - `@ObservedObject` 觀察物件中的變化，而 `@StateObject` 管理物件的生命週期。

9. 如何在 SwiftUI 中處理視圖動畫？
   - 使用動畫修飾符，如 `.animation()` 或 `withAnimation {}` 來為 UI 變化添加動畫效果。

10. `ViewBuilder` 和 `@ViewBuilder` 之間有什麼區別？
    - `ViewBuilder` 是用於構建視圖的協議，而 `@ViewBuilder` 是用於返回視圖的函式的屬性包裝器。

### CocoaPods 與依賴管理

11. 什麼是 CocoaPods？它在 iOS 開發中如何被使用？
    - CocoaPods 是 Swift 和 Objective-C Cocoa 專案的依賴管理器，可簡化程式庫的整合。

12. 如何安裝 CocoaPods？
    - 透過 Ruby gem 安裝：`sudo gem install cocoapods`。

13. 什麼是 Podfile？如何配置它？
    - Podfile 列出了專案的依賴項。透過指定 pods 及其版本來進行配置。

14. 如何使用 CocoaPods 將依賴項添加到你的專案中？
    - 將 pod 添加到 Podfile 中，然後執行 `pod install`。

15. `pod install` 和 `pod update` 之間有什麼區別？
    - `pod install` 會按照指定安裝依賴項，而 `pod update` 會更新到最新版本。

16. 如何解決不同 pods 之間的衝突？
    - 使用相容的 pod 版本，或在 Podfile 中指定版本。

17. 什麼是 Carthage？它與 CocoaPods 有何不同？
    - Carthage 是另一個依賴管理器，它建置並連結程式庫，而不會深度整合到專案中。

18. 如何為不同的建置配置管理不同的 pods？
    - 在 Podfile 中根據建置配置使用條件語句。

19. 什麼是 podspec 檔案？它如何被使用？
    - podspec 檔案描述了 pod 的版本、原始碼、依賴項和其他元數據。

20. 如何對 CocoaPods 的問題進行疑難排解？
    - 檢查 pod 版本、清理專案，並查閱 CocoaPods 問題追蹤器。

### UI 佈局

21. 如何在 iOS 中建立響應式佈局？
    - 使用 Auto Layout 和約束來使視圖適應不同的螢幕尺寸。

22. 解釋 `Stack View` 和 `Auto Layout` 之間的區別。
    - Stack Views 簡化了在行或列中佈局視圖的過程，而 Auto Layout 則提供了對定位的精確控制。

23. 如何在 iOS 中使用 `UIStackView`？
    - 將視圖添加到 Stack View 中，並配置其軸線、分佈和對齊方式。

24. iOS 中 `frame` 和 `bounds` 有什麼區別？
    - `frame` 定義了視圖相對於其父視圖的位置和尺寸，而 `bounds` 定義了視圖自身的座標系統。

25. 如何在 iOS 中處理不同的螢幕尺寸和方向？
    - 使用 Auto Layout 和尺寸類別來使 UI 適應各種裝置和方向。

26. 解釋如何在 iOS 中使用 `Auto Layout` 約束。
    - 在視圖之間設定約束以定義它們的關係和位置。

27. 在 Auto Layout 中，`leading` 和 `trailing` 有什麼區別？
    - Leading 和 trailing 會適應文字方向，而 left 和 right 則不會。

28. 如何在 iOS 中建立自訂佈局？
    - 子類化 `UIView` 並覆寫 `layoutSubviews()` 以手動定位子視圖。

29. 解釋如何使用 `UIPinchGestureRecognizer` 和 `UIRotationGestureRecognizer`。
    - 將手勢識別器附加到視圖上，並在委派方法中處理它們的動作。

30. 如何為不同裝置類型（iPhone、iPad）處理佈局變化？
    - 使用尺寸類別和自適應佈局來為不同裝置調整 UI。

### Swift

31. Swift 和 Objective-C 的主要區別是什麼？
    - Swift 更安全、更簡潔，並支援閉包和泛型等現代語言特性。

32. 解釋 Swift 中可選項（optionals）的概念。
    - 可選項表示可以為 `nil` 的值，表示值的缺失。

33. `nil` 和 `optional` 之間有什麼區別？
    - `nil` 是值的缺失，而可選項可以包含一個值，也可以是 `nil`。

34. 如何在 Swift 中處理錯誤？
    - 使用 `do-catch` 區塊，或使用 `throw` 傳播錯誤。

35. 解釋 `let` 和 `var` 之間的區別。
    - `let` 宣告常量，而 `var` 宣告可以修改的變數。

36. Swift 中類別（class）和結構體（struct）有什麼區別？
    - 類別支援繼承並且是參考類型，而結構體是值類型。

37. 如何在 Swift 中建立枚舉（enum）？
    - 使用 `enum` 關鍵字和 case 來定義枚舉，case 可以有關聯值。

38. 解釋 Swift 中協議導向程式設計（protocol-oriented programming）的概念。
    - 協議定義了方法、屬性和要求，符合協議的類型必須實作這些內容。

39. 協議（protocol）和委派（delegate）之間有什麼區別？
    - 協議定義方法，而委派為特定的互動實作協議方法。

40. 如何在 Swift 中使用泛型（generics）？
    - 使用泛型類型來編寫靈活、可重複使用的程式碼，這些程式碼適用於任何資料類型。

### 網路

41. 如何在 iOS 中處理網路請求？
    - 使用 URLSession 處理網路任務，或使用像 Alamofire 這樣的程式庫來獲取更高層級的抽象。

42. 什麼是 URLSession？
    - URLSession 處理網路請求，提供資料任務、上傳任務和下載任務。

43. 如何在 Swift 中處理 JSON 解析？
    - 使用 `Codable` 協議將 JSON 資料解碼為 Swift 結構體或類別。

44. 解釋同步請求和異步請求之間的區別。
    - 同步請求會阻塞呼叫執行緒，而異步請求則不會。

45. 如何在背景執行緒中管理網路請求？
    - 使用 GCD 或 OperationQueue 在非主執行緒上執行請求。

46. 什麼是 Alamofire？它與 URLSession 有何不同？
    - Alamofire 是一個第三方網路程式庫，與 URLSession 相比，它簡化了 HTTP 請求。

47. 如何處理網路錯誤和重試？
    - 在完成處理程序中實作錯誤處理，並針對暫時性錯誤考慮重試機制。

48. 解釋如何使用 `URLSessionDataDelegate` 方法。
    - 實作委派方法來處理請求進度、身份驗證等。

49. GET 和 POST 請求有什麼區別？
    - GET 用於檢索資料，而 POST 用於向伺服器發送資料以建立或更新資源。

50. 如何保護網路通訊？
    - 使用 HTTPS 加密傳輸中的資料，並妥善處理憑證。

### 最佳實踐與問題解決

51. 你如何確保專案中的程式碼品質？
    - 使用 linting 工具、編寫單元測試，並遵循編碼標準。

52. 解釋你會如何除錯 SwiftUI 視圖。
    - 使用 Xcode 的除錯工具、預覽畫布和 print 語句來識別問題。

53. 你使用什麼策略來優化應用程式效能？
    - 使用 Instruments 分析應用程式、優化資料獲取，並減少 UI 層級數量。

54. 如何在 Swift 中處理記憶體管理？
    - 使用 ARC（自動參考計數）並避免循環參考。

55. 解釋你會如何重構遺留程式碼。
    - 識別程式碼異味、編寫測試，並逐步重構。

56. 你在 CI/CD 流水線方面有什麼經驗？
    - 使用 Jenkins、GitHub Actions 或 Fastlane 等工具設定流水線，以實現自動化建置和部署。

57. 你如何跟進最新的 iOS 發展動態？
    - 關注 Apple 的開發者資源、參加會議，並參與開發者社群。

58. 描述一次你在專案中解決困難錯誤的經歷。
    - 描述識別、隔離和修復問題的過程。

59. 你對版本控制的方法是什麼？
    - 使用 Git 進行分支、提交和有效協作。

60. 你如何在專案中處理截止日期和壓力？
    - 優先處理任務、有效溝通，並高效管理時間。