---
audio: false
date: 2025-09-09
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Configuración de OPENAI_REVERSE_PROXY en LibreChat
translated: true
type: note
---

Entendido 👍 Estás editando el `.env` de LibreChat.
Ese archivo es exactamente donde configuras `OPENAI_REVERSE_PROXY`.

---

### 1. Qué hace la variable

`OPENAI_REVERSE_PROXY` se utiliza si quieres que LibreChat enrute las solicitudes a la API de OpenAI a través de un servidor proxy (por ejemplo, si ejecutas un proxy inverso auto-alojado para agregar registro, almacenamiento en caché, enrutamiento regional o para evitar restricciones).

---

### 2. Cómo configurarla

En tu `.env`, simplemente asígnale la URL base de tu proxy inverso. Por ejemplo:

```ini
OPENAI_REVERSE_PROXY=https://tu-proxy.ejemplo.com/v1
```

Notas:

* La URL debe apuntar a tu endpoint proxy que imita la API `/v1` de OpenAI.
* No incluyas una barra diagonal final (`/`) a menos que tu proxy lo requiera.
* Mantenla vacía (`OPENAI_REVERSE_PROXY=`) si no usas un proxy.

---

### 3. Aplicar los cambios

Después de editar `.env`, reinicia tus contenedores de LibreChat para que tomen el nuevo valor:

```bash
docker compose down
docker compose up -d --force-recreate
```

---

### 4. Verificar

Puedes verificar dentro del contenedor en ejecución:

```bash
docker compose exec librechat env | grep OPENAI_REVERSE_PROXY
```

Debería mostrar el valor que configuraste.

---

¿Ya tienes una URL de proxy inverso (como `https://openrouter.ai/api/v1` o tu propia instancia de Nginx), o quieres que te muestre cómo **configurar uno** para LibreChat?