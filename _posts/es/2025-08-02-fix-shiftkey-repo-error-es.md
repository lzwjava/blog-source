---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección del Error de Firma GPG de APT
translated: true
type: note
---

El error que estás viendo significa que APT se niega a actualizar desde el repositorio de ShiftKey porque no puede verificar su firma GPG. Tienes dos formas sencillas de solucionarlo:

---

## 1. **Eliminar o deshabilitar el repositorio dañado**

Si realmente no necesitas `https://apt.packages.shiftkey.dev/ubuntu`, simplemente deshabilítalo:

```bash
# Encuentra el archivo que define ese repositorio (estará en /etc/apt/sources.list.d/)
ls /etc/apt/sources.list.d/shiftkey*

# Elimínalo (reemplaza con el nombre de archivo real)
sudo rm /etc/apt/sources.list.d/shiftkey.packages.shiftkey.dev.list

# Luego actualiza e instala
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

## 2. **Importar la clave de firma del repositorio**

Si quieres seguir usando los paquetes de ShiftKey, necesitas obtener e instalar su clave pública:

```bash
# Descarga y convierte su clave GPG en el keyring de APT
curl -fsSL https://apt.packages.shiftkey.dev/ubuntu/pubkey.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-archive-keyring.gpg > /dev/null

# Edita el archivo del repositorio para que haga referencia a ese keyring.  
# Abre /etc/apt/sources.list.d/shiftkey*.list en tu editor y cambia la línea deb a:
#   deb [signed-by=/usr/share/keyrings/shiftkey-archive-keyring.gpg] https://apt.packages.shiftkey.dev/ubuntu any main

# Luego actualiza e instala
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

Una vez que APT pueda actualizarse sin errores GPG, podrás instalar `pkg-config` y `libssl-dev`, y luego recompilar:

```bash
cargo clean
cargo run
```