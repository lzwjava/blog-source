---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用線性代數進行圖像壓縮
translated: true
type: note
---

影像壓縮是數位影像處理中的基礎任務，旨在減少影像的儲存大小同時維持其視覺品質。實現此目標的一種有效方法是透過線性代數，特別是奇異值分解（SVD）。這項技術讓我們能以更緊湊的形式表示影像矩陣，有效捨棄次要資訊同時保留關鍵特徵。

以下 Python 程式碼展示如何使用 SVD 壓縮影像。流程包括將影像分解為組成元件，透過僅保留部分最重要特徵來壓縮這些元件，然後重構壓縮後的影像。此方法可同時應用於灰階與彩色影像，為減小影像尺寸提供了靈活且數學嚴謹的解決方案。

```python
import numpy as np
from PIL import Image
import argparse
import os

def compress_image(image_path, compression_factor=0.1):
    # 開啟影像並轉換為 numpy 陣列
    img = Image.open(image_path)
    img_array = np.array(img, dtype=float)

    # 檢查影像為灰階或彩色
    if len(img_array.shape) == 2:  # 灰階影像
        # 對影像陣列執行 SVD
        U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

        # 僅保留頂部奇異值來壓縮影像
        k = int(compression_factor * min(img_array.shape))
        S_compressed = np.diag(S[:k])
        U_compressed = U[:, :k]
        Vt_compressed = Vt[:k, :]

        # 重構壓縮影像
        img_compressed = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))
    else:  # 彩色影像
        # 分別對每個通道執行 SVD
        img_compressed = np.zeros_like(img_array)
        for i in range(img_array.shape[2]):  # 遍歷每個通道
            channel = img_array[:, :, i]
            U, S, Vt = np.linalg.svd(channel, full_matrices=False)

            # 僅保留頂部奇異值來壓縮通道
            k = int(compression_factor * min(channel.shape))
            S_compressed = np.diag(S[:k])
            U_compressed = U[:, :k]
            Vt_compressed = Vt[:k, :]

            # 重構壓縮通道
            img_compressed[:, :, i] = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))

    # 將數值限制在 0 到 255 之間，並轉換回 uint8 格式
    img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)

    # 在原始檔名後添加 '_compressed' 生成輸出路徑
    file_name, file_extension = os.path.splitext(image_path)
    output_path = f"{file_name}_compressed{file_extension}"

    # 儲存壓縮影像
    compressed_img = Image.fromarray(img_compressed)
    compressed_img.save(output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="使用 SVD 壓縮影像")
    parser.add_argument("input_file", help="輸入影像檔案路徑")
    parser.add_argument("--compression_factor", type=float, default=0.1, help="壓縮係數（預設值：0.1）")
    args = parser.parse_args()

    output_file = compress_image(args.input_file, args.compression_factor)
    print(f"壓縮影像已儲存為：{output_file}")

```