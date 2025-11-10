---
audio: false
generated: true
image: false
lang: de
layout: post
title: Kalman-Filter für saubere Blog-Daten
translated: true
type: note
---

Tolle Repo! Für einen Jekyll-Blog wie diesen ist ein Kalman-Filter perfekt, um verrauschte Zeitreihen in saubere Visualisierungen oder interaktive Demos zu verwandeln. Hier sind praktische Anwendungsmöglichkeiten – und eine einsatzbereite Pipeline, die du direkt in deine Repo einfügen kannst.

## Was du mit Kalman in deinem Blog machen kannst

* Rauschende **Pageview-Statistiken** glätten (tägliche Besucher, Absprungrate, Sitzungslänge), damit Leser Trends und kein Rauschen sehen.
* **Build-/Test-Metriken** entrauschen (z.B. Warnungen pro Tag, Fehler in `conversion_errors.log`), bevor sie geplottet werden.
* **Sensor-ähnliche Zeitreihen** bereinigen, die du teilen möchtest – GPS-Pfade, Tippgeschwindigkeit über die Zeit, Scroll-Tiefe, etc.
* **Lehrreiche Beiträge** veröffentlichen: Interaktive Demos, die zeigen, wie Prozess-/Messrauschen die Schätzung verändern.

---

## Schneller Erfolg: Verwandele deinen Python-Code in ein statisches Diagramm für den Blog

Wenn du nur eine Grafik für einen Beitrag benötigst, ersetze die letzte Zeile deines Skripts von `plt.show()` durch:

```python
plt.savefig("assets/kalman/toy.png", dpi=200, bbox_inches="tight")
```

Dann in einem Beitrag einbetten:

```markdown
![Kalman-Demo](/assets/kalman/toy.png)
```

---

## Einsatzbereite Pipeline: Glätte jede CSV-Zeitreihe und veröffentliche PNG + JSON

### 1) Lege deine Daten hier ab

Erstelle `assets/data/pageviews.csv` entweder mit `t,value` oder `date,value`:

```
date,value
2025-07-01, 1023
2025-07-02, 980
2025-07-03, 1135
```

### 2) Füge ein wiederverwendbares Skript hinzu

Erstelle `scripts/kalman/smooth_series.py`:

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

### 3) Füge ein Make-Target hinzu

In `Makefile`:

```make
kalman:
	python3 scripts/kalman/smooth_series.py --in assets/data/pageviews.csv \
		--out-prefix assets/kalman/pageviews --dt 1.0 --q 0.05 --r 4.0
```

Ausführen mit:

```bash
make kalman
```

Du erhältst:

* `assets/kalman/pageviews.png` – bereit zum Einbetten
* `assets/kalman/pageviews.json` – für optionale Interaktivität

### 4) In einem Beitrag einbetten (statisch)

Erstelle `notes/2025-08-17-kalman-pageviews.md`:

```markdown
---
layout: post
title: Smoothing blog stats with a Kalman filter
---

Unten: Rote Punkte sind die rohen täglichen Pageviews; die blaue Linie ist die Kalman-Schätzung.

![Pageviews (Kalman)](/assets/kalman/pageviews.png)
```

---

## Optional: Eine kleine clientseitige Visualisierung (ohne Bibliotheken)

Füge diesen Code-Snippet nach dem Generieren des JSON in den Beitrag ein. Es zeichnet zwei Polylinien (Rohdaten vs. Schätzung) mit einfachem SVG.

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

## Anmerkungen zu deinem Python-Snippet

* Dein Modell ist der Standard-**Constant-Velocity**-Zustand `[Position, Geschwindigkeit]` mit Messung der Position. Dein `Q` entspricht der Form des konstanten Beschleunigungs-Rauschens. Gut!
* Für numerische Stabilität habe ich die Kovarianz-Aktualisierung auf die **Joseph-Form** umgestellt, die `P` positiv semidefinit hält.
* Für Blogging bevorzuge `plt.savefig(...)` gegenüber `plt.show()`, damit dein Build (lokal oder CI) Artefakte in `assets/` erzeugt.

---

## Weitere interessante Blog-Ideen

* Stelle eine **Mouse-Tracking-Demo** vor: Zeige eine rohe Cursor-Spur vs. eine Kalman-geglättete Spur.
* Teile einen **GPS-Walk**: Lade eine CSV mit Lat/Long hoch, glätte sie mit Kalman und rendere sie als SVG-Pfad.
* **AB-Test-Metriken**: Entrausche Konversionsraten vor dem Plotten, damit Leser nicht auf Rauschen überreagieren.
* **Rust/Python im Vergleich**: Implementiere den gleichen Filter in `rust/` und `scripts/` und vergleiche die Ausgaben (keine Tabelle nötig – nur zwei überlagerte Plots).

Wenn du möchtest, sag mir, welchen Datensatz du zuerst glätten möchtest (Pageviews, Fehlerzahlen, etc.), und ich passe das CSV-Schema und die `q/r`-Standardwerte für dich an.