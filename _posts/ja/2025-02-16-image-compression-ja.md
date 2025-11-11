---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 線形代数を用いた画像圧縮
translated: true
type: note
---

画像圧縮は、視覚的品質を維持しながら画像の保存サイズを削減することを目的とした、デジタル画像処理における基本的なタスクです。これを実現する強力な方法の一つが線形代数、特に特異値分解（SVD）を利用することです。この技術により、画像行列をよりコンパクトな形式で表現し、本質的な特徴を保持しながら重要度の低い情報を効果的に捨てることができます。

以下のPythonコードは、SVDを使用して画像を圧縮する方法を示しています。このプロセスでは、画像を構成要素に分解し、最も重要な特徴の一部のみを保持してこれらの要素を圧縮し、その後、圧縮された画像を再構成します。このアプローチはグレースケール画像とカラー画像の両方に適用でき、画像サイズを削減するための柔軟で数学的に健全な方法を提供します。

```python
import numpy as np
from PIL import Image
import argparse
import os

def compress_image(image_path, compression_factor=0.1):
    # 画像を開き、numpy配列に変換する
    img = Image.open(image_path)
    img_array = np.array(img, dtype=float)

    # 画像がグレースケールかカラーかをチェックする
    if len(img_array.shape) == 2:  # グレースケール画像
        # 画像配列に対してSVDを実行する
        U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

        # 上位の特異値のみを保持して画像を圧縮する
        k = int(compression_factor * min(img_array.shape))
        S_compressed = np.diag(S[:k])
        U_compressed = U[:, :k]
        Vt_compressed = Vt[:k, :]

        # 圧縮された画像を再構成する
        img_compressed = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))
    else:  # カラー画像
        # 各チャンネルに対して個別にSVDを実行する
        img_compressed = np.zeros_like(img_array)
        for i in range(img_array.shape[2]):  # 各チャンネルを反復処理
            channel = img_array[:, :, i]
            U, S, Vt = np.linalg.svd(channel, full_matrices=False)

            # 上位の特異値のみを保持してチャンネルを圧縮する
            k = int(compression_factor * min(channel.shape))
            S_compressed = np.diag(S[:k])
            U_compressed = U[:, :k]
            Vt_compressed = Vt[:k, :]

            # 圧縮されたチャンネルを再構成する
            img_compressed[:, :, i] = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))

    # 値を0から255の間にクリップし、uint8に変換し直す
    img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)

    # 元のファイル名に '_compressed' を追加して出力パスを生成する
    file_name, file_extension = os.path.splitext(image_path)
    output_path = f"{file_name}_compressed{file_extension}"

    # 圧縮された画像を保存する
    compressed_img = Image.fromarray(img_compressed)
    compressed_img.save(output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SVDを使用して画像を圧縮する。")
    parser.add_argument("input_file", help="入力画像ファイルへのパス")
    parser.add_argument("--compression_factor", type=float, default=0.1, help="圧縮係数 (デフォルト: 0.1)")
    args = parser.parse_args()

    output_file = compress_image(args.input_file, args.compression_factor)
    print(f"圧縮された画像が保存されました: {output_file}")

```