---
audio: false
generated: true
lang: hant
layout: post
title: 基於卷積神經網絡與視覺變換器的圖像處理
translated: true
type: note
---

以下是使用 **卷積神經網絡 (CNNs)** 和 **Vision Transformers (ViT)** 在 Python 中透過 **PyTorch** 處理影像的程式碼範例。

---

## **1. 使用 CNN（卷積神經網絡）進行影像處理**
CNN 廣泛應用於影像分類、物件偵測和特徵提取。

### **範例：使用預訓練的 CNN（ResNet）**
```python
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# 載入預訓練的 ResNet 模型
model = models.resnet18(pretrained=True)
model.eval()  # 設定為評估模式

# 定義影像預處理流程
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 載入並預處理影像
image = Image.open("example.jpg")  # 請替換為你的影像路徑
input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)  # 添加批次維度

# 如果可用則移至 GPU
if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    model.to('cuda')

# 提取特徵（在最終分類層之前）
with torch.no_grad():
    features = model(input_batch)

print("特徵向量形狀:", features.shape)  # 例如：torch.Size([1, 1000])
```
**說明**：
1. **ResNet18** 是在 ImageNet 上預訓練的 CNN 架構。
2. 影像經過預處理（調整大小、標準化）。
3. 模型將影像轉換為**特徵向量**（例如 ResNet18 的 1000 維向量）。

---

## **2. 使用 Vision Transformer (ViT) 進行影像處理**
ViT 將影像視為圖塊序列，並使用自注意力機制（類似於 NLP 中的方法）。

### **範例：使用預訓練的 ViT（Hugging Face）**
```python
from transformers import ViTFeatureExtractor, ViTModel
from PIL import Image
import torch

# 載入預訓練的 Vision Transformer (ViT)
model_name = "google/vit-base-patch16-224-in21k"
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTModel.from_pretrained(model_name)

# 載入影像
image = Image.open("example.jpg")  # 請替換為你的影像路徑

# 預處理影像（轉換為圖塊）
inputs = feature_extractor(images=image, return_tensors="pt")

# 提取特徵（CLS 符記或圖塊嵌入）
with torch.no_grad():
    outputs = model(**inputs)

# 取得特徵向量（CLS 符記）
features = outputs.last_hidden_state[:, 0, :]  # 形狀：[1, 768]

print("特徵向量形狀:", features.shape)  # 例如：torch.Size([1, 768])
```
**說明**：
1. **ViT** 將影像分割為 **16x16 圖塊**，並像處理 NLP 中的符記一樣處理它們。
2. `CLS 符記`（第一個符記）代表整個影像的特徵向量。
3. 輸出是一個 **768 維向量**（針對 `vit-base`）。

---

## **3. CNN 與 ViT 特徵提取比較**

| 模型 | 方法 | 特徵向量大小 | 函式庫 |
|-------|----------|---------------------|-----------|
| **CNN (ResNet18)** | 卷積層 + 池化 | 1000 (ImageNet 類別) | `torchvision` |
| **ViT (Google ViT-Base)** | 圖塊嵌入 + Transformer | 768 (隱藏維度) | `transformers` |

---

## **4. 影像特徵向量的應用**
- **影像搜尋**：比較特徵向量（例如餘弦相似度）。
- **遷移學習**：使用預訓練特徵進行自訂任務。
- **物件偵測**：從特徵中提取感興趣區域 (ROI)。

```python
# 範例：計算兩張影像之間的相似度
from sklearn.metrics.pairwise import cosine_similarity

# 假設 features1 和 features2 是提取的向量
similarity = cosine_similarity(features1, features2)
print("相似度分數:", similarity[0][0])
```

---

## **關鍵要點**
1. **CNN**（例如 ResNet）使用**卷積層**來提取層次化特徵。
2. **ViT**（例如 Google 的 ViT）將影像視為**圖塊序列**並使用**自注意力機制**。
3. 兩者都將影像轉換為**特徵向量**以供後續任務使用。

需要關於**從頭訓練自訂 CNN/ViT** 的範例嗎？告訴我吧！🚀