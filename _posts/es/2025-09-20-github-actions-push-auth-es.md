---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Corrección de Errores de Autenticación en Push de GitHub Actions
translated: true
type: note
---

Ese error 403 significa que el push se está autenticando como **`lzwjava` sin un token que tenga acceso de escritura** (a menudo porque el job todavía usa el `GITHUB_TOKEN` por defecto, que no puede hacer push a otro repositorio). Soluciónalo **inyectando una credencial real para el checkout/push de destino**.

Aquí tienes tres formas sólidas—elige una. Mostraré la más rápida primero.

---

### Opción A — Usar un PAT e incrustarlo en el remote (más rápido)

1. Crea un **PAT clásico** con el alcance `repo` (o un PAT de grano fino con **Contents: Read & Write** para `lzwjava/lzwjava.github.io`). Guárdalo en el repositorio fuente como `DEPLOY_TOKEN`.

2. Actualiza el paso de deploy en tu workflow para **forzar al remote a usar ese token**:

```yaml
- name: Check out destination repo
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    token: ${{ secrets.DEPLOY_TOKEN }}
    path: destination
    fetch-depth: 0

- name: Push built site to destination
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll

    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # Fuerza al remote a usar el PAT explícitamente (evita conflictos con credential-helper)
    git remote set-url origin https://${{ secrets.DEPLOY_TOKEN }}@github.com/lzwjava/lzwjava.github.io.git

    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

Si aún ves el 403, a tu PAT le faltan alcances o (si el repositorio estuviera en una organización) necesita autorización SSO. Regenera con el alcance `repo` e inténtalo de nuevo.

---

### Opción B — Evitar la contaminación de credenciales: deshabilitar las credenciales por defecto en el primer checkout

A veces el **primer checkout** escribe el `GITHUB_TOKEN` por defecto en el asistente de credenciales y se reutiliza después. Deshabilítalo:

```yaml
- name: Check out source repo
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    persist-credentials: false   # <- importante
```

Luego mantén el checkout del destino con tu PAT como se muestra en la Opción A (puedes omitir la línea `remote set-url` si las cosas ya funcionan, pero es inofensiva).

---

### Opción C — Clave de deploy SSH (muy robusta)

1. En tu máquina: `ssh-keygen -t ed25519 -C "deploy@actions" -f deploy_key`
2. Añade la **clave pública** (`deploy_key.pub`) como una **Deploy key** en `lzwjava/lzwjava.github.io` con **Write access**.
3. Añade la **clave privada** (`deploy_key`) como secreto `ACTIONS_DEPLOY_KEY` en el repositorio **fuente**.

Workflow:

```yaml
- name: Check out destination repo via SSH
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    ssh-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
    path: destination
    fetch-depth: 0

- name: Push built site (SSH)
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll
    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

---

### Diagnóstico rápido si vuelve a fallar

Ejecuta estos comandos justo antes de hacer push para ver qué autenticación está realmente configurada:

```bash
cd destination
git remote -v
git config --get user.name
git config --get user.email
git config --get url.https://github.com/.insteadof || true
git config --global --list | sed -n 's/^credential\.helper.*/&/p'
```

Si `remote -v` muestra un `https://github.com/...` **sin** tu PAT inyectado (Opción A) o `git@github.com:` (Opción C), todavía estás usando la credencial incorrecta.

---

### Problemas comunes

* **PAT de grano fino** debe otorgar explícitamente **Contents: Read & Write** **a ese repositorio exacto**.
* **Branch protection** en `main` puede bloquear los pushes del bot (requiere checks/firmas). Si es así, despliega a una rama no protegida (ej., `gh-pages`) o ajusta las reglas.
* **PAT caducado** → regenera.
* **SSO de organización** (no es tu caso si es un repositorio de usuario) → autoriza el PAT para la organización.

Haz una de las tres opciones anteriores y el error 403 desaparecerá.