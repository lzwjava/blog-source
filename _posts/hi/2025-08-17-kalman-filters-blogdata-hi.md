---
audio: false
generated: true
image: false
lang: hi
layout: post
title: स्वच्छ ब्लॉग डेटा के लिए कालमैन फिल्टर
translated: true
type: note
---

बढ़िया रेपो! इस तरह के Jekyll-style ब्लॉग के लिए, Kalman filter शोर-भरी time-series को साफ visuals या interactive demos में बदलने के लिए एकदम सही है। यहां इसके इस्तेमाल के व्यावहारिक तरीके दिए गए हैं—साथ ही एक drop-in pipeline जिसे आप अपने रेपो में paste कर सकते हैं।

## अपने ब्लॉग पर Kalman से आप क्या कर सकते हैं

* शोर-भरे **पेजव्यू स्टैट्स** (रोजाना विज़िटर, बाउंस, सत्र की अवधि) को smooth करें ताकि पाठकों को उतार-चढ़ाव दिखे, अस्थिरता नहीं।
* प्लॉट करने से पहले **बिल्ड/टेस्ट मेट्रिक्स** (जैसे, प्रति दिन चेतावनियाँ, `conversion_errors.log` में त्रुटियाँ) को denoise करें।
* **सेंसर जैसी श्रृंखलाओं** को साफ करें जो आप साझा कर सकते हैं—GPS पथ, समय के साथ टाइपिंग स्पीड, स्क्रॉल डेप्थ, आदि।
* **शैक्षिक पोस्ट** प्रकाशित करें: interactive डेमो जो दिखाएं कि process/measurement noise अनुमान को कैसे बदलते हैं।

---

## त्वरित सफलता: अपने Python को ब्लॉग में static chart में बदलें

अगर आप सिर्फ एक पोस्ट के लिए एक figure चाहते हैं, तो अपनी स्क्रिप्ट की आखिरी लाइन को `plt.show()` से बदलकर यह करें:

```python
plt.savefig("assets/kalman/toy.png", dpi=200, bbox_inches="tight")
```

फिर एक पोस्ट में embed करें:

```markdown
![Kalman demo](/assets/kalman/toy.png)
```

---

## Turn-key pipeline: किसी भी CSV series को smooth करें और PNG + JSON publish करें

### 1) अपना डेटा यहाँ रखें

`assets/data/pageviews.csv` बनाएँ जिसमें या तो `t,value` या `date,value` हो:

```
date,value
2025-07-01, 1023
2025-07-02, 980
2025-07-03, 1135
```

### 2) एक reusable स्क्रिप्ट जोड़ें

`scripts/kalman/smooth_series.py` बनाएँ:

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

### 3) एक Make target जोड़ें

`Makefile` में:

```make
kalman:
	python3 scripts/kalman/smooth_series.py --in assets/data/pageviews.csv \
		--out-prefix assets/kalman/pageviews --dt 1.0 --q 0.05 --r 4.0
```

Run करें:

```bash
make kalman
```

आपको मिलेंगे:

* `assets/kalman/pageviews.png` – embed करने के लिए तैयार
* `assets/kalman/pageviews.json` – वैकल्पिक इंटरैक्टिविटी के लिए

### 4) एक पोस्ट में embed करें (static)

`notes/2025-08-17-kalman-pageviews.md` बनाएँ:

```markdown
---
layout: post
title: Smoothing blog stats with a Kalman filter
---

नीचे: लाल बिंदु raw रोजाना पेजव्यू हैं; नीली लाइन Kalman estimate है।

![Pageviews (Kalman)](/assets/kalman/pageviews.png)
```

---

## वैकल्पिक: एक छोटा client-side visual (कोई libraries नहीं)

JSON generate करने के बाद इस snippet को पोस्ट में डालें। यह दो polylines (raw बनाम estimate) plain SVG के साथ draw करता है।

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

## आपकी Python snippet पर नोट्स

* आपका मॉडल standard **constant-velocity** state `[position, velocity]` है जिसमें position का measurement होता है। आपका `Q` constant-acceleration driving noise form से मेल खाता है। बढ़िया!
* numerical stability के लिए मैंने covariance update को **Joseph form** में बदल दिया है, जो `P` को positive semidefinite बनाए रखता है।
* ब्लॉगिंग के लिए, `plt.show()` के बजाय `plt.savefig(...)` को प्राथमिकता दें ताकि आपका build (local या CI) `assets/` में artifacts produce करे।

---

## ब्लॉग के लिए अन्य मजेदार विचार

* एक **माउस-ट्रैकिंग डेमो** पोस्ट करें: एक raw cursor trail बनाम एक Kalman-smoothed trail दिखाएं।
* एक **GPS वॉक** साझा करें: lat/long की एक CSV upload करें, इसे Kalman-smooth करें, और इसे एक SVG path के रूप में render करें।
* **AB-test मेट्रिक्स**: शोर पर overreact करने से रोकने के लिए प्लॉट करने से पहले conversion rates को denoise करें।
* **Rust/Python साइड-बाय-साइड**: एक ही filter को `rust/` और `scripts/` में implement करें और outputs की तुलना करें (किसी table की आवश्यकता नहीं—बस दो overlaid plots)।

अगर आप चाहें, तो मुझे बताएं कि आप पहले कौन सा डेटासेट smooth करना चाहेंगे (पेजव्यू, त्रुटि गिनती, आदि), और मैं आपके लिए CSV schema और `q/r` defaults को tailor कर दूंगा।