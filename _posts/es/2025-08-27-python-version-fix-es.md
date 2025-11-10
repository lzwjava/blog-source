---
audio: false
generated: true
image: false
lang: es
layout: post
title: Cómo Solucionar el Problema de Versión de Python
translated: true
type: note
---

Entendido — estás experimentando un problema de **desajuste de versiones de Python**.

Tus registros muestran:

* `python3` → **3.10.12**
* `python` → **3.13.7**

Así que cuando Claude Code (o tu script de agente de investigación) invoca `python3`, usa la versión 3.10, que no tiene `pyperclip` instalado. Tú instalaste `pyperclip` en el entorno de 3.13, por lo que 3.10 no puede verlo.

Aquí tienes algunas formas de solucionarlo:

---

### 1. Ejecutar Claude Code con el Python que deseas

Si quieres que Claude Code siempre use Python 3.13, establece explícitamente el ejecutable en tu shell:

```bash
export PYTHON_EXECUTABLE=$(which python)
```

O si quieres `python3` específicamente:

```bash
export PYTHON_EXECUTABLE=$(which python3)
```

Luego, al iniciar Claude Code o tu agente, puede leer esa variable de entorno.

---

### 2. Dirigir `python3` a Python 3.13

En Ubuntu puedes actualizar el sistema de `alternatives`:

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 2
sudo update-alternatives --config python3
```

Luego elige Python 3.13.

---

### 3. Instalar `pyperclip` en Python 3.10

Si quieres seguir usando 3.10 para `python3`, simplemente instálalo ahí:

```bash
python3 -m pip install --user pyperclip
```

Esto asegura que `python3` pueda importarlo.

---

### 4. Usar un entorno virtual

La mejor práctica: crea un venv con el Python que quieras y ejecuta Claude Code dentro de él:

```bash
python3.13 -m venv ~/.venvs/claude
source ~/.venvs/claude/bin/activate
pip install pyperclip
```

Luego inicia tu agente dentro de este venv, para que siempre use 3.13.

---

👉 Pregunta para ti: ¿quieres que Claude Code **siempre se ejecute con Python 3.13**, o prefieres mantener 3.10 como `python3` y simplemente solucionar el módulo faltante?