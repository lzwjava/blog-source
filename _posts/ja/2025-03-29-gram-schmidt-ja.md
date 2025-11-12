---
audio: false
generated: true
lang: ja
layout: post
title: グラム・シュミットの正規直交化法
translated: true
type: note
---

**グラム・シュミットの正規直交化法**は、線形代数において、線形独立なベクトルの集合を、同じ部分空間を張る正規直交ベクトルの集合に変換するために用いられる手法です。これは、QR分解、最小二乗法の問題解決、ベクトル空間における計算の簡素化など、様々な応用において特に有用です。

### **主な概念**

- **線形独立なベクトル**: 互いに他のベクトルの線形結合として表すことができないベクトル。
- **直交ベクトル**: 互いに直交するベクトル。つまり、それらの内積がゼロである。
- **正規直交集合**: ベクトルが互いに直交しており、かつ単位ベクトル（ノルムが1）であるような集合。

### **グラム・シュミットの過程の目的**

- **直交化**: ベクトルの集合を、各ベクトルが互いに直交する集合に変換する。
- **正規化**: 各ベクトルの長さを調整して単位ベクトルにする。
- **簡素化**: ベクトル空間内での射影、分解、変換における計算を容易にする。

### **過程の説明**

内積空間（例えば \\( \mathbb{R}^n \\)）内の線形独立なベクトルの集合 \\( \{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \} \\) が与えられたとき、グラム・シュミットの過程は以下の手順に従って正規直交集合 \\( \{ \mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n \} \\) を構築します：

1. **最初のベクトルの初期化**:
   \\[
   \mathbf{u}_1 = \mathbf{v}_1
   \\]
   正規化して以下を得る：
   \\[
   \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|}
   \\]

2. **反復的な直交化と正規化**（\\( k = 2 \\) から \\( n \\) まで）:
   - **直交化**:
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proj}_{\mathbf{q}_j} \mathbf{v}_k
     \\]
     ここで、射影 \\( \text{proj}_{\mathbf{q}_j} \mathbf{v}_k \\) は以下のように計算される：
     \\[
     \text{proj}_{\mathbf{q}_j} \mathbf{v}_k = (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **正規化**:
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **詳細な手順**

1. **\\( \mathbf{u}_1 \\) と \\( \mathbf{q}_1 \\) の計算**:
   - \\( \mathbf{u}_1 = \mathbf{v}_1 \\)
   - \\( \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|} \\)

2. **後続の各ベクトル \\( \mathbf{v}_k \\) に対して**:
   - **全ての前の \\( \mathbf{q}_j \\) への射影を引く**:
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **\\( \mathbf{u}_k \\) を正規化して \\( \mathbf{q}_k \\) を得る**:
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **例**

\\( \mathbb{R}^2 \\) 内のベクトル \\( \mathbf{v}_1 = [1, 1] \\) と \\( \mathbf{v}_2 = [1, 0] \\) にグラム・シュミットの過程を適用してみましょう。

1. **最初のベクトル**:
   - \\( \mathbf{u}_1 = \mathbf{v}_1 = [1, 1] \\)
   - 正規化：
     \\[
     \| \mathbf{u}_1 \| = \sqrt{1^2 + 1^2} = \sqrt{2}
     \\]
     \\[
     \mathbf{q}_1 = \frac{[1, 1]}{\sqrt{2}} = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right]
     \\]

2. **二番目のベクトル**:
   - \\( \mathbf{v}_2 \\) の \\( \mathbf{q}_1 \\) への射影を計算：
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = (\mathbf{v}_2 \cdot \mathbf{q}_1) \mathbf{q}_1
     \\]
     \\[
     \mathbf{v}_2 \cdot \mathbf{q}_1 = [1, 0] \cdot \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = \frac{1}{\sqrt{2}} \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \left[ \frac{1}{2}, \frac{1}{2} \right]
     \\]
   - 射影を引く：
     \\[
     \mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = [1, 0] - \left[ \frac{1}{2}, \frac{1}{2} \right] = \left[ \frac{1}{2}, -\frac{1}{2} \right]
     \\]
   - \\( \mathbf{u}_2 \\) を正規化：
     \\[
     \| \mathbf{u}_2 \| = \sqrt{\left( \frac{1}{2} \right)^2 + \left( -\frac{1}{2} \right)^2} = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \mathbf{q}_2 = \frac{\left[ \frac{1}{2}, -\frac{1}{2} \right]}{\frac{1}{\sqrt{2}}} = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
     \\]

### **結果**

正規直交集合は以下の通り：
\\[
\mathbf{q}_1 = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right], \quad \mathbf{q}_2 = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
\\]

これらのベクトルは直交し（\\( \mathbf{q}_1 \cdot \mathbf{q}_2 = 0 \\)）、かつ単位長である（\\( \| \mathbf{q}_1 \| = \| \mathbf{q}_2 \| = 1 \\)）。

### **応用**

- **QR分解**: 行列を直交行列 \\( Q \\) と上三角行列 \\( R \\) に分解する。
- **最小二乗法の問題**: 過剰決定系に対する最良の近似解を見つける。
- **数値解法**: 計算アルゴリズムの安定性と効率を向上させる。

### **まとめ**

グラム・シュミットの正規直交化法は、内積空間におけるベクトルの集合を正規直交化する体系的な手法であり、元のベクトルが張る空間を保ちながら、新しい集合を扱いやすくします。これは線形代数の基礎をなすものであり、数学、物理学、工学において広範な応用があります。