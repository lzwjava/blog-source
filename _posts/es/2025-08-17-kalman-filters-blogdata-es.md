---
audio: false
generated: true
image: false
lang: es
layout: post
title: Filtros de Kalman para Datos de Blog Limpios
translated: true
type: note
---

¡Buen repositorio! Para un blog con estilo Jekyll como este, un filtro de Kalman es perfecto para convertir series temporales ruidosas en visualizaciones limpias o demostraciones interactivas. Aquí tienes formas prácticas de usarlo—y una pipeline lista para usar que puedes pegar en tu repositorio.

## Lo que puedes hacer con Kalman en tu blog

* Suavizar **estadísticas de visitas a la página** ruidosas (visitantes diarios, tasa de rebote, duración de sesión) para que los lectores vean tendencias, no fluctuaciones.
* Eliminar ruido de **métricas de compilación/pruebas** (por ejemplo, advertencias por día, errores en `conversion_errors.log`) antes de graficar.
* Limpiar **series tipo sensor** que puedas compartir—trayectorias GPS, velocidad de escritura en el tiempo, profundidad de scroll, etc.
* Publicar **posts educativos**: demostraciones interactivas que muestren cómo el ruido del proceso/de la medición cambia la estimación.

---

## Victoria rápida: convierte tu Python en un gráfico estático para el blog

Si solo quieres una figura para un post, cambia la última línea de tu script de `plt.show()` a:

```python
plt.savefig("assets/kalman/toy.png", dpi=200, bbox_inches="tight")
```

Luego incrusta en un post:

```markdown
![Demo de Kalman](/assets/kalman/toy.png)
```

---

## Pipeline lista para usar: suaviza cualquier serie CSV y publica PNG + JSON

### 1) Coloca tus datos aquí

Crea `assets/data/pageviews.csv` con `t,valor` o `fecha,valor`:

```
fecha,valor
2025-07-01, 1023
2025-07-02, 980
2025-07-03, 1135
```

### 2) Añade un script reutilizable

Crea `scripts/kalman/smooth_series.py`:

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
        # Q para el ruido de conducción de aceleración constante (σ_a^2 = q)
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
        # z es una medición escalar de la posición
        z = np.array([[float(z)]])
        y = z - (self.H @ self.x)
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        I = np.eye(self.P.shape[0])
        # Forma de Joseph para estabilidad numérica
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
                # Convertir a espaciado ordinal; trataremos las muestras como separadas por 1 paso visualmente
                ts.append(datetime.fromisoformat(row[cols["date"]]).toordinal())
            else:
                ts.append(float(row[cols.get("t", "t")]))
            ys.append(float(row[cols.get("value", "value")]))
    # Si se usaron fechas, reindexar t como 0..N-1 para simplicidad al graficar
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
    plt.plot(t, y, ".", label="Mediciones")
    plt.plot(t, est, "-", linewidth=2, label="Estimación de Kalman")
    plt.xlabel("t")
    plt.ylabel("valor")
    plt.title("Suavizado de Kalman (modelo de velocidad constante)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    plt.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="CSV de entrada (t,valor) o (fecha,valor)")
    ap.add_argument("--out-prefix", required=True, help="ej. assets/kalman/pageviews")
    ap.add_argument("--dt", type=float, default=1.0, help="paso de tiempo entre muestras")
    ap.add_argument("--q", type=float, default=0.05, help="varianza del proceso (aceleración^2)")
    ap.add_argument("--r", type=float, default=4.0, help="varianza de la medición")
    args = ap.parse_args()

    t, y = read_csv_series(args.inp)
    est = smooth_series(t, y, dt=args.dt, q=args.q, r=args.r)

    out_png = f"{args.out_prefix}.png"
    out_json = f"{args.out_prefix}.json"
    plot_and_save(t, y, est, out_png)

    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w") as f:
        json.dump({"t": t.tolist(), "y": y.tolist(), "est": est.tolist()}, f)
    print(f"Se escribieron {out_png} y {out_json}")

if __name__ == "__main__":
    main()
```

### 3) Añade un objetivo en el Makefile

En `Makefile`:

```make
kalman:
	python3 scripts/kalman/smooth_series.py --in assets/data/pageviews.csv \
		--out-prefix assets/kalman/pageviews --dt 1.0 --q 0.05 --r 4.0
```

Ejecuta:

```bash
make kalman
```

Obtendrás:

* `assets/kalman/pageviews.png` – lista para incrustar
* `assets/kalman/pageviews.json` – para interactividad opcional

### 4) Incrusta en un post (estático)

Crea `notes/2025-08-17-kalman-pageviews.md`:

```markdown
---
layout: post
title: Suavizando estadísticas del blog con un filtro de Kalman
---

Abajo: los puntos rojos son las visitas diarias brutas; la línea azul es la estimación de Kalman.

![Visitas a la página (Kalman)](/assets/kalman/pageviews.png)
```

---

## Opcional: una pequeña visualización del lado del cliente (sin bibliotecas)

Coloca este fragmento en el post después de generar el JSON. Dibuja dos polilíneas (bruto vs. estimación) con SVG simple.

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

## Notas sobre tu fragmento de código Python

* Tu modelo es el estado estándar de **velocidad constante** `[posición, velocidad]` con medición de la posición. Tu `Q` coincide con la forma del ruido de conducción de aceleración constante. ¡Bien!
* Para estabilidad numérica, cambié la actualización de la covarianza a la **forma de Joseph**, que mantiene `P` semidefinida positiva.
* Para blogs, prefiere `plt.savefig(...)` sobre `plt.show()` para que tu compilación (local o CI) produzca artefactos en `assets/`.

---

## Otras ideas divertidas para el blog

* Publica una **demo de seguimiento del ratón**: muestra un rastro del cursor bruto versus un rastro suavizado por Kalman.
* Comparte un **paseo GPS**: sube un CSV de lat/long, suavízalo con Kalman y renderízalo como una ruta SVG.
* **Métricas de prueba A/B**: elimina el ruido de las tasas de conversión antes de graficar para que los lectores no reaccionen excesivamente al ruido.
* **Rust/Python lado a lado**: implementa el mismo filtro en `rust/` y `scripts/` y compara las salidas (no se necesita tabla—solo dos gráficos superpuestos).

Si quieres, dime con qué conjunto de datos te gustaría empezar a suavizar (visitas a la página, conteos de errores, etc.), y adaptaré el esquema del CSV y los valores predeterminados de `q/r` para ti.