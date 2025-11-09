---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Vermeidung von Jekyll CSS Cache Busting
translated: true
type: note
---

Was du siehst, ist Jekyll (über das Theme oder die `jekyll-assets`/`jekyll-feed`/`minima` Pipeline), das automatisch einen **Fingerprint (Hash)** an deine Stylesheet-URL für Cache-Busting anhängt. Deshalb hat die gleiche CSS-Datei nach einem Rebuild unterschiedliche `?v=...` Query-Strings.

Wenn du nicht möchtest, dass Jekyll diesen Query-String bei jedem Build ändert, kannst du das "Cache-Busting"/"Digest"-Verhalten deaktivieren oder überschreiben:

### Option 1: Verwende einen festen Link

Anstatt Jekylls Helper-Tag (z.B. `{{ "/assets/css/style.css" | relative_url }}` oder `{{ "/assets/css/style.css" | asset_path }}`) zu verwenden, setze den Link einfach fest:

```html
<link rel="stylesheet" href="/assets/css/style.css">
```

Auf diese Weise wird kein Fingerprint eingefügt.

### Option 2: Deaktiviere Asset Digesting

Wenn du **jekyll-assets** oder ein Theme verwendest, das Dateien mit Fingerprints versieht, kannst du Digesting in `_config.yml` deaktivieren:

```yml
assets:
  digest: false
```

### Option 3: Verwende `relative_url` ohne Digest

Wenn dein Theme etwas wie folgt verwendet:

```liquid
<link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
```

stelle sicher, dass du es nicht durch `asset_path` oder `absolute_url` leitest, wenn Digest aktiviert ist. Verwende einfach `relative_url`.

---

👉 Kurz gesagt:

* Wenn du möchtest, dass es sich **niemals ändert**, setze den Pfad fest.
* Wenn du es über die Konfiguration steuern möchtest, setze `assets.digest: false`.
* Wenn du immer noch Versionierung, aber eine stabile Version möchtest, müsstest du deinen eigenen `?v=...` Query-String manuell verwalten.

Möchtest du, dass es **komplett statisch** ist (ändert sich nie), oder möchtest du nur verhindern, dass Jekyll **bei jedem Build neue Hashes generiert**?