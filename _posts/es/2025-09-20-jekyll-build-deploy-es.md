---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Flujo de Trabajo Automatizado de Compilación e Implementación de Jekyll
translated: true
type: note
---

Puedes hacer esto completamente en GitHub Actions: construir el sitio en el runner, luego hacer checkout del repositorio destino en una subcarpeta y enviar el contenido de `_site/` allí.

A continuación, un workflow listo para usar que puedes agregar a tu repositorio **fuente** (donde viven tus scripts de Python y contenido de Jekyll):

```yaml
# .github/workflows/build-and-deploy.yml
name: Construir & Desplegar Jekyll a Repositorio Externo

on:
  push:
    branches: [ main ]
  workflow_dispatch:

# Usaremos un PAT para el push al repositorio destino
permissions:
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Hacer checkout del repositorio fuente
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Configurar Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: Instalar dependencias de Jekyll
        run: |
          bundle install --jobs 4 --retry 3

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Instalar dependencias de Python
        if: hashFiles('requirements.txt') != ''
        run: pip install -r requirements.txt

      - name: Ejecutar tu pipeline de workflow local (modo CI)
        env:
          # agrega aquí cualquier clave que necesiten tus scripts
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        run: |
          # Ejecuta exactamente los mismos pasos que orquestan tus scripts.
          # Si quieres, puedes llamar tu script directamente:
          python scripts/workflow_local.py
          # O, si prefieres pasos explícitos:
          # python scripts/generate/update_notes_link.py
          # python scripts/translation/update_lang.py --max_files 9 --model gemini-flash --commits 1000
          # python -m unittest discover -s tests/workflow
          # python scripts/release/update_release.py

      - name: Construir Jekyll (a _site)
        run: |
          # Si tu módulo de Python establece DEFAULT_DESTINATION en otro lugar, aún puedes anularlo aquí.
          bundle exec jekyll build --destination _site

      - name: Hacer checkout del repositorio destino
        uses: actions/checkout@v4
        with:
          repository: lzwjava/lzwjava.github.io   # <-- tu DESTINATION_REPO_URL objetivo
          token: ${{ secrets.WORKFLOW_ACCESS_TOKEN }}      # <-- PAT con alcance "repo"
          path: destination
          fetch-depth: 0

      - name: Sincronizar sitio construido al repositorio destino
        run: |
          mkdir -p destination/_site
          rsync -av --delete _site/ destination/_site/
          cd destination
          # Opcional: asegura que Pages no procese Jekyll nuevamente
          touch _site/.nojekyll

          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit --amend --no-edit
            # ajusta la rama si tu destino usa algo diferente (ej., gh-pages)
            git push --force-with-lease origin HEAD:main
          else
            echo "No changes to deploy."
          fi

      - name: (Opcional) Subir artifact del sitio construido
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site
```

### Lo que necesitas configurar

* **PAT para el push al destino**: crea un Token de Acceso Personal clásico con alcance `repo` en tu cuenta de GitHub (o usa un token de grano fino que otorgue acceso de escritura al repositorio destino). Guárdalo en la configuración del repositorio fuente como `WORKFLOW_ACCESS_TOKEN` (es decir, `Settings → Secrets and variables → Actions → New repository secret`).
* **Nombres de rama y repositorio**: en el paso `Check out destination repo`, establece `repository:` al repositorio externo (puede ser público o privado). En el comando push, establece la rama a la que quieres desplegar (a menudo `main` o `gh-pages`).
* **Configuración de GitHub Pages** (si estás sirviendo desde el repositorio destino): en la **Settings → Pages** de ese repositorio, elige la **Branch** correcta (ej., `main` / root), y mantén `CNAME`/dominio personalizado como desees.
* **Expectativas de historial**: el paso de despliegue enmienda el último commit y usa `--force-with-lease`; asegúrate de que esta rama esté dedicada a artifacts de despliegue para que reescribir el historial sea aceptable.

### Notas sobre tu script de Python

* No necesitas `open_destination_repo_in_browser()` en CI, así que está bien dejarlo como está; simplemente no se llamará aquí. El workflow hace push directamente desde el runner.
* Tampoco necesitas `push_destination_repo()` en CI. El workflow maneja el segundo checkout y push, así que puedes mantener tu script sin cambios para ejecuciones locales.
* Si tu `build_site()` escribe a un `DEFAULT_DESTINATION` diferente, aún puedes anularlo ejecutando el paso de construcción de Jekyll explícito mostrado arriba, que escribe a `_site/`. El paso de despliegue sincroniza desde `_site/`.

### ¿Repositorio destino privado?

* No hay problema. GitHub Pages solo sirve repositorios públicos (o ramas públicas en organizaciones con Pages habilitado), pero si tu objetivo es solo enviar artifacts a un repositorio privado por cualquier razón, lo anterior aún funciona. Si sí quieres alojamiento con Pages, asegúrate de que ese repositorio/rama destino esté configurado para servir Pages (público donde sea requerido) o usa un host alternativo (ej., Cloudflare Pages, Netlify) y despliega allí.

Eso es todo—ahora construirás en los runners de GitHub y enviarás `_site/` a otro repositorio en la nube.