---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: PIL Pillow 圖像處理指南
translated: true
type: note
---

### 什麼是 PIL/Pillow？
PIL 原本是 Python Imaging Library 的縮寫，但現在以 Pillow 套件（現代化分支）的形式維護。你在程式碼中會以 `PIL` 匯入它，但需要透過 pip 安裝 Pillow。它用於在 Python 中開啟、處理和儲存影像檔案。支援 JPEG、PNG、GIF、BMP 等格式。

### 安裝
要使用 PIL，請安裝 Pillow：
```bash
pip install pillow
```

### 基本匯入與使用
安裝後，在你的 Python 腳本中這樣匯入：
```python
from PIL import Image
```
不需要使用 `import PIL.Image`——這會直接匯入 Image 模組。

### 常見影像操作
以下是執行基本任務的方法。假設你的目錄中有一個名為 `example.jpg` 的影像檔案。

#### 1. 開啟影像
```python
image = Image.open('example.jpg')  # 開啟影像檔案
image.show()  # 顯示影像（在具備影像檢視器的系統上有效）
```

#### 2. 取得影像資訊
```python
print(image.format)  # 例如 'JPEG'
print(image.size)    # 元組：(寬度, 高度)
print(image.mode)    # 例如彩色影像的 'RGB'
```

#### 3. 調整影像大小
```python
resized = image.resize((800, 600))  # 調整為 800x600 像素
resized.save('resized_example.jpg')  # 儲存調整後的影像
```

#### 4. 轉換格式
```python
image.convert('L').save('grayscale_example.png')  # 轉換為灰階並儲存為 PNG
```

#### 5. 旋轉影像
```python
rotated = image.rotate(90)  # 順時針旋轉 90 度
rotated.save('rotated_example.jpg')
```

#### 6. 裁剪影像
```python
left, top, right, bottom = 100, 100, 300, 300  # 定義裁剪框 (x1, y1, x2, y2)
cropped = image.crop((left, top, right, bottom))
cropped.save('cropped_example.jpg')
```

#### 7. 應用濾鏡（需要額外匯入）
使用濾鏡時，需匯入 `ImageFilter`：
```python
from PIL import ImageFilter
blurred = image.filter(ImageFilter.BLUR)  # 應用模糊濾鏡
blurred.save('blurred_example.jpg')
```

### 進階範例：批次處理多個影像
```python
import os
from PIL import Image

# 將資料夾中所有 JPEG 影像調整為 200x200
input_folder = 'images/'
output_folder = 'resized_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(input_folder, filename))
        resized = image.resize((200, 200))
        resized.save(os.path.join(output_folder, filename))
```

### 提示與注意事項
- **錯誤處理**：對無效檔案使用 try-except，例如 `try: image = Image.open('file.jpg')`。
- **記憶體效率**：對於大型影像，在操作後使用 `image.close()` 釋放記憶體。
- **文件**：查閱 Pillow 的完整文件 [pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/) 以獲取更多功能，如繪圖、添加文字或 EXIF 資料處理。
- **相依性**：在某些系統設定中，Pillow 可能需要系統函式庫（例如 libjpeg）；如果遇到問題，請參閱安裝指南。

如果你有特定任務或錯誤，請提供更多細節以獲得針對性的幫助！