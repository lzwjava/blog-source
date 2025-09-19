---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 花卉識別應用程式
translated: true
---

這是來自 GitHub 項目的 README.md [https://github.com/lzwjava/flower-recognition](https://github.com/lzwjava/flower-recognition)。

---

### 花卉識別應用程式

這是一個幫助使用者通過拍攝照片並繪製圓圈來識別花卉的 Android 應用程式。

#### 功能：
- **拍攝照片**：使用者可以在應用程式中直接拍攝花卉的照片。
- **繪圖功能**：能夠在花卉圖片上繪製圓圈和註釋以輔助識別。
- **認證**：使用登錄畫面進行安全的用戶認證。
- **結果顯示**：在用戶友好的界面上顯示識別結果。
- **材料設計**：應用材料設計原則，提供現代化和直觀的用戶體驗。

#### 文件結構：
```
└── com
    └── lzw
        └── flower
            ├── activity
            │   ├── LoginActivity.java
            │   └── PhotoActivity.java
            ├── adapter
            │   └── PhotoAdapter.java
            ├── avobject
            │   └── Photo.java
            ├── base
            │   ├── App.java
            │   ├── ImageLoader.java
            │   └── SplashActivity.java
            ├── deprecated
            │   ├── CameraActivity.java
            │   └── Deprecated.java
            ├── draw
            │   ├── Draw.java
            │   ├── DrawActivity.java
            │   ├── DrawFragment.java
            │   ├── DrawView.java
            │   ├── HelpBtn.java
            │   ├── History.java
            │   ├── Tooltip.java
            │   └── ZoomImageView.java
            ├── fragment
            │   ├── RecogFragment.java
            │   └── WaitFragment.java
            ├── material
            │   └── MaterialActivity.java
            ├── result
            │   ├── FlowerAdapter.java
            │   ├── FlowerData.java
            │   ├── Image.java
            │   ├── ResultActivity.java
            │   └── ResultFragment.java
            ├── service
            │   └── PhotoService.java
            ├── utils
            │   ├── BitmapUtils.java
            │   ├── Crop.java
            │   ├── ImageListDialogBuilder.java
            │   ├── Logger.java
            │   ├── PathUtils.java
            │   └── Utils.java
            └── web
                ├── Upload.java
                ├── UploadImage.java
                └── Web.java
```

#### 元件：
- **Activities**：包含處理不同應用程式活動（如登錄、拍攝照片和啟動畫面）的類。
- **Adapters**：處理照片和識別結果的顯示。
- **AVObject**：表示具有相關元數據的照片對象。
- **Drawing**：與在花卉圖片上繪製圓圈和註釋相關的類。
- **Fragments**：提供顯示識別結果和等待指示器的 UI 元件。
- **Material**：可能與實施材料設計指南有關。
- **Services**：處理與照片相關的背景任務和數據操作。
- **Utils**：包含各種任務的實用工具類，如圖像操作和記錄。

#### 使用方法：
1. 克隆此存儲庫。
2. 打開 Android Studio 中的項目。
3. 在 Android 設備或模擬器上構建並運行應用程式。

#### 許可證：
此項目根據 [MIT 許可證](LICENSE) 進行授權。