---
title: Preventing Jekyll CSS Cache Busting
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
model: openai/gpt-5
---

What you’re seeing is Jekyll (via the theme or `jekyll-assets`/`jekyll-feed`/`minima` pipeline) automatically appending a **fingerprint (hash)** to your stylesheet URL for cache-busting. That’s why the same CSS file ends up with different `?v=...` query strings when rebuilt.

If you don’t want Jekyll to change that query string each build, you can disable or override the “cache busting”/“digest” behavior:

### Option 1. Use a fixed link

Instead of Jekyll’s helper tag (e.g. `{{ "/assets/css/style.css" | relative_url }}` or `{{ "/assets/css/style.css" | asset_path }}`), just hardcode:

```html
<link rel="stylesheet" href="/assets/css/style.css">
```

That way, no fingerprint gets injected.

### Option 2. Disable asset digesting

If you’re using **jekyll-assets** or a theme that fingerprints files, you can disable digesting in `_config.yml`:

```yml
assets:
  digest: false
```

### Option 3. Use `relative_url` without digest

If your theme uses something like:

```liquid
<link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
```

make sure you are not piping it through `asset_path` or `absolute_url` with digest enabled. Just use `relative_url`.

---

👉 In short:

* If you want it **never to change**, hardcode the path.
* If you want to control it via config, set `assets.digest: false`.
* If you still want versioning but keep it stable, you’d need to manage your own `?v=...` manually.

Do you want it **completely static** (never changes), or do you just want to stop Jekyll from **generating new hashes every build**?