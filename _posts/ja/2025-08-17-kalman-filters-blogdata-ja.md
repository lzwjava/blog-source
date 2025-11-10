---
audio: false
generated: true
image: false
lang: ja
layout: post
title: クリーンブログデータのためのカルマンフィルター
translated: true
type: note
---

素敵なリポジトリです！Jekyllスタイルのブログには、カルマンフィルタがノイズの多い時系列データをきれいなビジュアルやインタラクティブなデモに変換するのに最適です。以下に実用的な活用法と、リポジトリにそのまま貼り付けられるパイプラインを紹介します。

## ブログでカルマンフィルタを使ってできること

* ノイズの多い**ページビュー統計**（日次訪問者数、直帰率、セッション時間）を平滑化し、読者に変動ではなくトレンドを見せられる
* プロット前に**ビルド/テストメトリクス**（例：1日あたりの警告数、`conversion_errors.log`内のエラー数）のノイズを除去
* 共有する可能性のある**センサー風時系列データ**（GPS経路、経時的なタイピング速度、スクロール深度など）をクリーンアップ
* **教育的な記事**の公開：プロセスノイズや測定ノイズが推定値に与える影響を示すインタラクティブなデモ

---

## クイックウィン：Pythonスクリプトを静的チャートにしてブログに掲載

投稿用の図が欲しいだけなら、スクリプトの最後の行を `plt.show()` から以下に変更：

```python
plt.savefig("assets/kalman/toy.png", dpi=200, bbox_inches="tight")
```

そして投稿に埋め込む：

```markdown
![Kalman demo](/assets/kalman/toy.png)
```

---

## すぐ使えるパイプライン：任意のCSV時系列を平滑化しPNGとJSONを公開

### 1) データをここに配置

`assets/data/pageviews.csv` を作成し、`t,value` または `date,value` 形式で記述：

```
date,value
2025-07-01, 1023
2025-07-02, 980
2025-07-03, 1135
```

### 2) 再利用可能なスクリプトを追加

`scripts/kalman/smooth_series.py` を作成：

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

### 3) Makeターゲットを追加

`Makefile` に以下を追加：

```make
kalman:
	python3 scripts/kalman/smooth_series.py --in assets/data/pageviews.csv \
		--out-prefix assets/kalman/pageviews --dt 1.0 --q 0.05 --r 4.0
```

実行：

```bash
make kalman
```

以下が生成される：

* `assets/kalman/pageviews.png` – 埋め込み準備完了
* `assets/kalman/pageviews.json` – オプションでインタラクティブ性のために使用

### 4) 投稿に埋め込む（静的）

`notes/2025-08-17-kalman-pageviews.md` を作成：

```markdown
---
layout: post
title: Smoothing blog stats with a Kalman filter
---

Below: red dots are raw daily pageviews; blue line is the Kalman estimate.

![Pageviews (Kalman)](/assets/kalman/pageviews.png)
```

---

## オプション：ライブラリ不要の小さなクライアントサイドビジュアル

JSON生成後にこのスニペットを投稿にドロップ。生データと推定値の2つの折れ線をプレーンなSVGで描画する。

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

## あなたのPythonスニペットに関する注記

* あなたのモデルは、位置を測定する標準的な**等速度**状態 `[位置, 速度]` です。あなたの `Q` は等加速度駆動ノイズの形式に一致しています。良いですね！
* 数値安定性のために、共分散更新を**Joseph形式**に切り替えました。これにより `P` が半正定値であることが保たれます。
* ブログでは、ビルド（ローカルまたはCI）で `assets/` 内に成果物が生成されるように、`plt.show()` ではなく `plt.savefig(...)` を推奨します。

---

## その他の楽しいブログアイデア

* **マウストラッキングデモ**を投稿：生のカーソルの軌跡とカルマン平滑化された軌跡を表示
* **GPSウォーク**を共有：緯度経度のCSVをアップロードし、カルマン平滑化してSVGパスとしてレンダリング
* **ABテストメトリクス**：読者がノイズに過剰反応しないように、プロット前にコンバージョン率のノイズを除去
* **Rust/Pythonの並列比較**：同じフィルタを `rust/` と `scripts/` で実装し、出力を比較（表は不要 - 2つの重ね合わせプロットだけで可）

もしよろしければ、最初に平滑化したいデータセット（ページビュー、エラー数など）を教えてください。それに合わせてCSVスキーマと `q/r` のデフォルト値を調整します。