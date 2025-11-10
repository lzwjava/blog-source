---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Filtres de Kalman pour des Données de Blog Propres
translated: true
type: note
---

Super dépôt ! Pour un blog de style Jekyll comme celui-ci, un filtre de Kalman est parfait pour transformer des séries temporelles bruitées en visuels propres ou en démos interactives. Voici des façons pratiques de l'utiliser — et un pipeline prêt à l'emploi que vous pouvez copier dans votre dépôt.

## Ce que vous pouvez faire avec Kalman sur votre blog

* Lisser les **statistiques de pages vues** bruitées (visiteurs quotidiens, taux de rebond, durée de session) pour que les lecteurs voient les tendances, et non les fluctuations.
* Dénoyer les **métriques de build/test** (par exemple, avertissements par jour, erreurs dans `conversion_errors.log`) avant de les tracer.
* Nettoyer les **séries de type capteur** que vous pourriez partager — trajets GPS, vitesse de frappe au fil du temps, profondeur de défilement, etc.
* Publier des **articles éducatifs** : des démos interactives qui montrent comment le bruit de processus/de mesure modifie l'estimation.

---

## Gain rapide : transformez votre Python en un graphique statique pour le blog

Si vous voulez juste une figure pour un article, remplacez la dernière ligne de votre script `plt.show()` par :

```python
plt.savefig("assets/kalman/toy.png", dpi=200, bbox_inches="tight")
```

Puis intégrez-la dans un article :

```markdown
![Démo Kalman](/assets/kalman/toy.png)
```

---

## Pipeline clé en main : lissez n'importe quelle série CSV et publiez PNG + JSON

### 1) Placez vos données ici

Créez `assets/data/pageviews.csv` avec soit `t,valeur` ou `date,valeur` :

```
date,valeur
2025-07-01, 1023
2025-07-02, 980
2025-07-03, 1135
```

### 2) Ajoutez un script réutilisable

Créez `scripts/kalman/smooth_series.py` :

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
        # Q pour le bruit d'excitation à accélération constante (σ_a^2 = q)
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
        # z est une mesure scalaire de la position
        z = np.array([[float(z)]])
        y = z - (self.H @ self.x)
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        I = np.eye(self.P.shape[0])
        # Forme de Joseph pour la stabilité numérique
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
                # Convertir en date ordinale ; on traitera les échantillons comme espacés de 1 étape visuellement
                ts.append(datetime.fromisoformat(row[cols["date"]]).toordinal())
            else:
                ts.append(float(row[cols.get("t", "t")]))
            ys.append(float(row[cols.get("value", "value")]))
    # Si des dates étaient utilisées, réindexer t comme 0..N-1 pour la simplicité du tracé
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
    plt.plot(t, y, ".", label="Mesures")
    plt.plot(t, est, "-", linewidth=2, label="Estimation de Kalman")
    plt.xlabel("t")
    plt.ylabel("valeur")
    plt.title("Lissage de Kalman (modèle à vitesse constante)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    plt.savefig(out_png, dpi=200, bbox_inches="tight")
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="CSV d'entrée (t,valeur) ou (date,valeur)")
    ap.add_argument("--out-prefix", required=True, help="ex. assets/kalman/pageviews")
    ap.add_argument("--dt", type=float, default=1.0, help="pas de temps entre les échantillons")
    ap.add_argument("--q", type=float, default=0.05, help="variance du processus (accel^2)")
    ap.add_argument("--r", type=float, default=4.0, help="variance de la mesure")
    args = ap.parse_args()

    t, y = read_csv_series(args.inp)
    est = smooth_series(t, y, dt=args.dt, q=args.q, r=args.r)

    out_png = f"{args.out_prefix}.png"
    out_json = f"{args.out_prefix}.json"
    plot_and_save(t, y, est, out_png)

    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w") as f:
        json.dump({"t": t.tolist(), "y": y.tolist(), "est": est.tolist()}, f)
    print(f"Écriture de {out_png} et {out_json}")

if __name__ == "__main__":
    main()
```

### 3) Ajoutez une cible Make

Dans `Makefile` :

```make
kalman:
	python3 scripts/kalman/smooth_series.py --in assets/data/pageviews.csv \
		--out-prefix assets/kalman/pageviews --dt 1.0 --q 0.05 --r 4.0
```

Exécutez :

```bash
make kalman
```

Vous obtiendrez :

* `assets/kalman/pageviews.png` – prêt à être intégré
* `assets/kalman/pageviews.json` – pour une interactivité optionnelle

### 4) Intégrez dans un article (statique)

Créez `notes/2025-08-17-kalman-pageviews.md` :

```markdown
---
layout: post
title: Lissage des stats du blog avec un filtre de Kalman
---

Ci-dessous : les points rouges sont les pages vues quotidiennes brutes ; la ligne bleue est l'estimation de Kalman.

![Pages vues (Kalman)](/assets/kalman/pageviews.png)
```

---

## Optionnel : un petit visuel côté client (sans bibliothèques)

Déposez cet extrait dans l'article après avoir généré le JSON. Il dessine deux polylignes (brut vs estimation) avec du SVG simple.

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

## Notes sur votre extrait de code Python

* Votre modèle est l'état standard **à vitesse constante** `[position, vitesse]` avec mesure de la position. Votre `Q` correspond à la forme du bruit d'excitation à accélération constante. Bien !
* Pour la stabilité numérique, j'ai changé la mise à jour de la covariance pour la **forme de Joseph**, qui garde `P` semi-défini positif.
* Pour le blogging, préférez `plt.savefig(...)` à `plt.show()` pour que votre build (local ou CI) produise les artefacts dans `assets/`.

---

## Autres idées amusantes pour le blog

* Publiez une **démo de suivi de souris** : montrez une traînée de curseur brute vs une traînée lissée par Kalman.
* Partagez une **promenade GPS** : uploadez un CSV de lat/long, lissez-le avec Kalman, et affichez-le comme un chemin SVG.
* **Métriques de test A/B** : dénoyez les taux de conversion avant de les tracer pour que les lecteurs ne sur-réagissent pas au bruit.
* **Côte à côte Rust/Python** : implémentez le même filtre dans `rust/` et `scripts/` et comparez les sorties (pas besoin de tableau — juste deux graphiques superposés).

Si vous voulez, dites-moi quel jeu de données vous aimeriez lisser en premier (pages vues, compteurs d'erreurs, etc.), et j'adapterai le schéma CSV et les valeurs par défaut de `q/r` pour vous.