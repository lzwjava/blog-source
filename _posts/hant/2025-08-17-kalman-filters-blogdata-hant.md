---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 卡爾曼濾波器應用於潔淨博客數據
translated: true
type: note
---

不錯的程式庫！對於像這樣的 Jekyll 風格部落格來說，卡爾曼濾波器非常適合將帶有雜訊的時間序列轉換成清晰的視覺化圖表或互動式演示。以下是實際應用方式——以及一個可直接貼到程式庫中的現成處理流程。

## 你可以在部落格中用卡爾曼濾波器做什麼

* 平滑帶有雜訊的**頁面瀏覽統計數據**（每日訪客、跳出率、工作階段長度），讓讀者看到趨勢而非波動。
* 在繪圖前對**建置/測試指標**進行降噪處理（例如每日警告數、`conversion_errors.log`中的錯誤數）。
* 清理你可能分享的**類感測器序列**——GPS路徑、打字速度隨時間變化、捲動深度等。
* 發布**教育類文章**：展示過程/量測雜訊如何改變估計值的互動式演示。

---

## 快速取勝：將你的 Python 程式碼轉為部落格中的靜態圖表

如果你只想在文章中插入圖表，將腳本的最後一行從 `plt.show()` 改為：

```python
plt.savefig("assets/kalman/toy.png", dpi=200, bbox_inches="tight")
```

然後在文章中嵌入：

```markdown
![卡爾曼演示](/assets/kalman/toy.png)
```

---

## 現成處理流程：平滑任何 CSV 序列並發布 PNG + JSON

### 1) 放置你的數據

建立 `assets/data/pageviews.csv`，包含 `t,value` 或 `date,value`：

```
date,value
2025-07-01, 1023
2025-07-02, 980
2025-07-03, 1135
```

### 2) 添加可重複使用的腳本

建立 `scripts/kalman/smooth_series.py`：

```python
#!/usr/bin/env python3
import argparse, csv, json, math, os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class Kalman1DConstVel:
    def __init__(self, dt, q, r, x0=None, v0=0.0):
        self.dt = float(dt)
        self.A = np.array([[1.0, self.dt],
                           [0.0, 1.0]])
        self.H = np.array([[1.0, 0.0]])
        # Q for constant-acceleration driving noise (σ_a^2 = q)
        self.Q = q * np.array([[0.25*self.dt**4, 0.5*self.dt**3],
                               [0.5*self.dt**3,    self.dt**2]])
        self.R = np.array([[r]])
        self.x = np.array([[x0 if x0 is not None else 0.0],
                           [v0]])
        self.P = np.eye(2) * 1.0

    def predict(self):
        self.x = self.A @ self.x
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, z):
        # z is scalar measurement of position
        z = np.array([[float(z)]])
        y = z - (self.H @ self.x)
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        I = np.eye(self.P.shape[0])
        # Joseph form for numerical stability
        self.P = (I - K @ self.H) @ self.P @ (I - K @ self.H).T + K @ self.R @ K.T

    def current_pos(self):
        return float(self.x[0, 0])

def read_csv_series(path):
    ts, ys = [], []
    with open(path, newline="") as f:
        r = csv.DictReader(f)
        cols = {k.lower(): k for k in r.fieldnames}
        has_date = "date" in cols
        for row in r:
            if has_date:
                # Convert to ordinal spacing; we’ll treat samples as 1-step apart visually
                ts.append(datetime.fromisoformat(row[cols["date"]]).toordinal())
            else:
                ts.append(float(row[cols.get("t", "t")]))
            ys.append(float(row[cols.get("value", "value")]))
    # If dates were used, reindex t as 0..N-1 for plotting simplicity
    if len(ts) and isinstance(ts[0], int):
        ts = list(range(len(ts)))
    return np.array(ts, dtype=float), np.array(ys, dtype=float)

def smooth_series(t, y, dt, q, r):
    kf = Kalman1DConstVel(dt=dt, q=q, r=r, x0=y[0])
    est = []
    for z in y:
        kf.predict()
        kf.update(z)
        est.append(kf.current_pos())
    return np.array(est, dtype=float)

def plot_and_save(t, y, est, out_png):
    plt.figure(figsize=(10, 5))
    plt.plot(t, y, ".", label="Measurements")
    plt.plot(t, est, "-", linewidth=2, label="Kalman estimate")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Kalman smoothing (constant-velocity model)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    plt.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="input CSV (t,value) or (date,value)")
    ap.add_argument("--out-prefix", required=True, help="e.g. assets/kalman/pageviews")
    ap.add_argument("--dt", type=float, default=1.0, help="time step between samples")
    ap.add_argument("--q", type=float, default=0.05, help="process variance (accel^2)")
    ap.add_argument("--r", type=float, default=4.0, help="measurement variance")
    args = ap.parse_args()

    t, y = read_csv_series(args.inp)
    est = smooth_series(t, y, dt=args.dt, q=args.q, r=args.r)

    out_png = f"{args.out_prefix}.png"
    out_json = f"{args.out_prefix}.json"
    plot_and_save(t, y, est, out_png)

    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w") as f:
        json.dump({"t": t.tolist(), "y": y.tolist(), "est": est.tolist()}, f)
    print(f"Wrote {out_png} and {out_json}")

if __name__ == "__main__":
    main()
```

### 3) 添加 Make 目標

在 `Makefile` 中：

```make
kalman:
	python3 scripts/kalman/smooth_series.py --in assets/data/pageviews.csv \
		--out-prefix assets/kalman/pageviews --dt 1.0 --q 0.05 --r 4.0
```

執行：

```bash
make kalman
```

你將得到：

* `assets/kalman/pageviews.png` – 可立即嵌入
* `assets/kalman/pageviews.json` – 用於可選的互動功能

### 4) 在文章中嵌入（靜態）

建立 `notes/2025-08-17-kalman-pageviews.md`：

```markdown
---
layout: post
title: 使用卡爾曼濾波器平滑部落格統計數據
---

下圖：紅點是原始每日頁面瀏覽量；藍線是卡爾曼估計值。

![頁面瀏覽量（卡爾曼）](/assets/kalman/pageviews.png)
```

---

## 可選：輕量級客戶端視覺化（無需函式庫）

在生成 JSON 後，將此程式碼片段放入文章中。它使用純 SVG 繪製兩條折線（原始數據 vs 估計值）。

```html
<div id="kalman-chart"></div>
<script>
(async function () {
  const res = await fetch("/assets/kalman/pageviews.json");
  const { t, y, est } = await res.json();
  const W = 800, H = 240, pad = 20;
  const xmin = 0, xmax = t.length - 1;
  const ymin = Math.min(...y, ...est), ymax = Math.max(...y, ...est);
  const sx = x => pad + (x - xmin) / (xmax - xmin || 1) * (W - 2*pad);
  const sy = v => H - pad - (v - ymin) / (ymax - ymin || 1) * (H - 2*pad);
  const toPts = arr => arr.map((v,i)=>`${sx(i)},${sy(v)}`).join(" ");

  const svg = `
  <svg viewBox="0 0 ${W} ${H}" width="100%" height="auto" style="background:#fff;border:1px solid #eee">
    <polyline points="${toPts(y)}" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1"/>
    <polyline points="${toPts(est)}" fill="none" stroke="currentColor" stroke-width="2"/>
  </svg>`;
  document.getElementById("kalman-chart").innerHTML = svg;
})();
</script>
```

---

## 關於你的 Python 程式碼片段說明

* 你的模型是標準的**恆定速度**狀態 `[位置, 速度]`，並對位置進行量測。你的 `Q` 符合恆定加速度驅動雜訊形式。很好！
* 為了數值穩定性，我將協方差更新切換為**Joseph 形式**，這能保持 `P` 為半正定。
* 對於部落格，建議使用 `plt.savefig(...)` 而非 `plt.show()`，這樣你的建置（本地或 CI）就能在 `assets/` 中產生成品。

---

## 其他有趣的部落格點子

* 發布**滑鼠軌跡演示**：顯示原始游標軌跡與卡爾曼平滑後的軌跡。
* 分享**GPS 步行路線**：上傳經緯度的 CSV 檔案，用卡爾曼濾波器平滑處理，並渲染為 SVG 路徑。
* **AB 測試指標**：在繪圖前對轉換率進行降噪，避免讀者對雜訊過度解讀。
* **Rust/Python 並排比較**：在 `rust/` 和 `scripts/` 中實現相同的濾波器，並比較輸出（無需表格——只需兩個疊加圖表）。

如果你需要，告訴我你想先平滑哪個數據集（頁面瀏覽量、錯誤計數等），我會為你量身定制 CSV 結構和 `q/r` 的預設值。