---
audio: false
generated: true
image: false
lang: ar
layout: post
title: مرشحات كالمان لتنقية بيانات المدونات
translated: true
type: note
---

مستودع رائع! بالنسبة لمدونة على نمط Jekyll مثل هذه، فإن مرشح كالمان مثالي لتحويل السلاسل الزمنية المضطربة إلى مرئيات نظيفة أو عروض تفاعلية. إليك طرقًا عملية لاستخدامه— وخط أنابيب جاهز يمكنك لصقه في مستودعك.

## ما يمكنك فعله باستخدام Kalman في مدونتك

* تنعيم **إحصائيات مشاهدات الصفحة** المضطربة (الزوار اليوميون، معدل الارتداد، مدة الجلسة) حتى يرى القراء الاتجاهات، وليس التقلبات.
* إزالة الضوضاء من **مقاييس البناء والاختبار** (على سبيل المثال، التحذيرات يوميًا، الأخطاء في `conversion_errors.log`) قبل التخطيط.
* تنقية **السلاسل الشبيهة بالبيانات المستشعرة** التي قد تشاركها— مسارات GPS، سرعة الكتابة مع مرور الوقت، عمق التمرير، إلخ.
* نشر **منشورات تعليمية**: عروض تفاعلية توضح كيف يتغير التقدير مع ضوضاء العملية/القياس.

---

## فوز سريع: تحويل Python الخاص بك إلى مخطط ثابت في المدونة

إذا كنت تريد فقط شكلًا لمنشور، غيّر السطر الأخير من البرنامج النصي الخاص بك من `plt.show()` إلى:

```python
plt.savefig("assets/kalman/toy.png", dpi=200, bbox_inches="tight")
```

ثم قم بتضمينه في منشور:

```markdown
![عرض Kalman](/assets/kalman/toy.png)
```

---

## خط أنابيب جاهز: تنعيم أي سلسلة CSV ونشر PNG + JSON

### ١) ضع بياناتك هنا

أنشئ `assets/data/pageviews.csv` إما بـ `t,value` أو `date,value`:

```
date,value
2025-07-01, 1023
2025-07-02, 980
2025-07-03, 1135
```

### ٢) أضف برنامجًا نصيًا قابلاً لإعادة الاستخدام

أنشئ `scripts/kalman/smooth_series.py`:

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

### ٣) أضف هدف Make

في `Makefile`:

```make
kalman:
	python3 scripts/kalman/smooth_series.py --in assets/data/pageviews.csv \
		--out-prefix assets/kalman/pageviews --dt 1.0 --q 0.05 --r 4.0
```

شغّل:

```bash
make kalman
```

ستحصل على:

* `assets/kalman/pageviews.png` – جاهز للتضمين
* `assets/kalman/pageviews.json` – للتفاعلية الاختيارية

### ٤) تضمين في منشور (ثابت)

أنشئ `notes/2025-08-17-kalman-pageviews.md`:

```markdown
---
layout: post
title: Smoothing blog stats with a Kalman filter
---

Below: red dots are raw daily pageviews; blue line is the Kalman estimate.

![Pageviews (Kalman)](/assets/kalman/pageviews.png)
```

---

## اختياري: مرئيات صغيرة من جانب العميل (بدون مكتبات)

أسقط هذه القطعة في المنشور بعد إنشاء JSON. ترسم خطين متعددين (البيانات الخام مقابل التقدير) باستخدام SVG عادي.

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

## ملاحظات على مقتطف Python الخاص بك

* نموذجك هو حالة **السرعة الثابتة** القياسية `[الموضع، السرعة]` مع قياس الموضع. الـ `Q` الخاص بك يتطابق مع شكل ضوضاء القيادة ذات التسارع الثابت. جيد!
* من أجل الاستقرار العددي، قمت بتبديل تحديث التباين إلى **شكل Joseph**، والذي يحافظ على `P` موجب شبه محدد.
* للمدونات، يُفضل استخدام `plt.savefig(...)` بدلاً من `plt.show()` حتى ينتج البناء الخاص بك (المحلي أو CI) الملفات في `assets/`.

---

## أفكار أخرى ممتعة للمدونة

* انشر **عرضًا توضيحيًا لتتبع الفأرة**: اعرض أثر المؤشر الخام مقابل الأثر المنعم بـ Kalman.
* شارك **مشية GPS**: حمّل CSV لخطوط الطول والعرض، ونعّمها بـ Kalman، وعرضها كمسار SVG.
* **مقاييس اختبار A/B**: أزل الضوضاء من معدلات التحويل قبل التخطيط حتى لا يبالغ القراء في رد فعلهم تجاه الضوضاء.
* **Rust/Python جنبًا إلى جنب**: نفّذ نفس المرشح في `rust/` و `scripts/` وقارن المخرجات (لا حاجة لجدول— فقط مخططان متراكبان).

إذا أردت، أخبرني أي مجموعة بيانات تود تنعيمها أولاً (مشاهدات الصفحة، أعداد الأخطاء، إلخ)، وسأخصص مخطط CSV والقيم الافتراضية لـ `q/r` من أجلك.