---
audio: false
lang: hant
layout: post
title: PyTorch
translated: true
type: note
---

### torch 函數

*   `torch.Tensor`：包含單一數據類型元素的多維陣列。
*   `torch.tensor`：使用數據和屬性構造張量。
*   `torch.zeros`：返回一個填充零的張量。
*   `torch.ones`：返回一個填充一的張量。
*   `torch.arange`：返回一個等間距數值的 1 維張量。
*   `torch.linspace`：返回在指定區間內等間距數值的 1 維張量。
*   `torch.rand`：返回一個填充來自區間 [0, 1) 均勻分佈隨機數的張量。
*   `torch.randn`：返回一個填充來自均值為 0、方差為 1 的正態分佈隨機數的張量。
*   `torch.empty`：返回一個具有未初始化數據的張量。
*   `torch.full`：創建一個指定大小並填充指定值的張量。
*   `torch.eye`：返回一個對角線為 1、其他位置為 0 的 2 維張量。

### 張量運算

*   `torch.add`：逐元素相加兩個張量。
*   `torch.sub`：逐元素相減兩個張量。
*   `torch.mul`：逐元素相乘兩個張量。
*   `torch.div`：逐元素相除兩個張量。
*   `torch.matmul`：執行矩陣乘法。
*   `torch.pow`：將張量的每個元素提升至指定冪次。
*   `torch.exp`：計算張量每個元素的指數。
*   `torch.log`：計算張量每個元素的自然對數。
*   `torch.sqrt`：計算張量每個元素的平方根。
*   `torch.abs`：計算張量每個元素的絕對值。
*   `torch.neg`：對張量每個元素取負值。
*   `torch.round`：將張量每個元素四捨五入到最接近的整數。
*   `torch.floor`：返回張量每個元素的向下取整值。
*   `torch.ceil`：返回張量每個元素的向上取整值。
*   `torch.clamp`：將輸入中的所有元素鉗制在 [min, max] 範圍內。
*   `torch.sum`：返回輸入張量中所有元素的總和。
*   `torch.mean`：返回輸入張量中所有元素的平均值。
*   `torch.std`：返回輸入張量中所有元素的標準差。
*   `torch.var`：返回輸入張量中所有元素的方差。
*   `torch.max`：返回輸入張量中所有元素的最大值。
*   `torch.min`：返回輸入張量中所有元素的最小值。
*   `torch.argmax`：返回輸入張量中所有元素最大值的索引。
*   `torch.argmin`：返回輸入張量中所有元素最小值的索引。
*   `torch.sort`：沿給定維度對輸入張量的元素進行排序。
*   `torch.topk`：返回輸入張量沿給定維度的 k 個最大元素。
*   `torch.reshape`：返回一個與輸入數據和元素數量相同但具有指定形狀的張量。
*   `torch.transpose`：返回一個維度交換後的輸入張量視圖。
*   `torch.squeeze`：返回一個移除了輸入中所有大小為 1 的維度的張量。
*   `torch.unsqueeze`：返回一個在指定位置插入大小為 1 的維度的新張量。
*   `torch.cat`：在給定維度上連接給定的張量。
*   `torch.stack`：沿新維度連接一系列張量。
*   `torch.chunk`：將張量分割成特定數量的塊。
*   `torch.split`：將張量分割成特定大小的塊。

### 神經網絡模組

*   `torch.nn.Module`：所有神經網絡模組的基類。
*   `torch.nn.Linear`：對輸入數據應用線性變換。
*   `torch.nn.Conv2d`：對由多個輸入平面組成的輸入信號應用 2D 卷積。
*   `torch.nn.MaxPool2d`：對輸入信號應用 2D 最大池化。
*   `torch.nn.ReLU`：逐元素應用整流線性單元函數。
*   `torch.nn.Sigmoid`：逐元素應用 sigmoid 函數。
*   `torch.nn.Tanh`：逐元素應用雙曲正切函數。
*   `torch.nn.BatchNorm2d`：對 4D 輸入應用批次歸一化。
*   `torch.nn.Dropout`：在訓練期間，以概率 p 隨機將輸入張量的部分元素設為零。
*   `torch.nn.Embedding`：一個存儲固定字典和大小的嵌入的簡單查找表。

### 損失函數

*   `torch.nn.MSELoss`：創建一個衡量輸入和目標之間每個元素的均方誤差（平方 L2 範數）的標準。
*   `torch.nn.CrossEntropyLoss`：此標準計算輸入和目標之間的交叉熵損失。
*   `torch.nn.BCELoss`：創建一個衡量目標和輸出之間二元交叉熵的標準。
*   `torch.nn.L1Loss`：創建一個衡量輸入和目標之間每個元素的平均絕對誤差 (MAE) 的標準。

### 優化器

*   `torch.optim.SGD`：實現隨機梯度下降（可選帶動量）。
*   `torch.optim.Adam`：實現 Adam 算法。
*   `torch.optim.RMSprop`：實現 RMSprop 算法。

### Autograd

*   `torch.autograd.grad`：計算並返回輸出相對於輸入的梯度總和。

### 實用工具

*   `torch.device`：代表 torch.Tensor 已分配或將要分配的設備。
*   `torch.cuda.is_available`：如果 CUDA 可用則返回 True。
*   `torch.save`：將張量儲存到磁碟。
*   `torch.load`：從磁碟加載張量。

### 其他

*   `torch.no_grad`：禁用梯度計算的上下文管理器。
*   `torch.set_grad_enabled`：根據其參數啟用或禁用梯度。