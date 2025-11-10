---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Correlación de Capturas de Pantalla y Registros del Servidor en Diferentes
  Zonas Horarias
translated: true
type: note
---

Entendido 👍 – quieres **correlacionar capturas de pantalla (que los testers suben a Confluence) con los registros del servidor de UAT** (generados por Java + log4j/slf4j), y la parte complicada son las múltiples zonas horarias y marcas de tiempo.

Desglosemos esto cuidadosamente:

---

## 1. ¿Qué marcas de tiempo tienes?

**Desde la captura de pantalla (Windows):**
- El reloj **visible dentro de la barra de tareas de la captura de pantalla** = hora **local** de la máquina cliente (hora del sistema, en su zona horaria).
- Los metadatos del archivo (si aún los tienes fuera de Confluence) pueden mostrar las marcas de tiempo `Creado` / `Modificado` = también en la zona horaria de ese cliente.

**Desde Confluence:**
- La marca de tiempo de subida = cuando el archivo adjunto llegó al servidor de Confluence.
- Normalmente se almacena/muestra en *hora del servidor* o convertida a la *zona horaria del perfil del usuario de Confluence*.
(Puedes verificar tu perfil de Confluence → Configuración → Zona horaria para confirmar lo que ves).

**Desde los registros de UAT (log4j/slf4j):**
- Las marcas de tiempo son generadas por la **zona horaria de la JVM del proceso Java** (comúnmente establecida por el sistema operativo del servidor por defecto, a menos que se anule).
- El formato está determinado por tu patrón de registro (ej. `yyyy-MM-dd HH:mm:ss,SSS [thread] ...`). Normalmente esta es la hora local de la JVM, no UTC, a menos que esté configurada explícitamente.

---

## 2. Por qué las cosas no coincidirán directamente
- La captura de pantalla muestra la hora **local del portátil del tester**.
- Confluence almacena la **hora de subida en la zona horaria del servidor/BD**.
- Los registros muestran la **zona horaria del servidor Java**.
Estas tres no están garantizadas a ser la misma.

---

## 3. Método para reconciliar
Aquí te explicamos cómo comparar de manera consistente una captura de pantalla de un tester con los registros del servidor:

1. **Elige un estándar de tiempo común – normalmente UTC**
   - Convierte todas las marcas de tiempo relevantes a UTC (Excel, scripts, o manualmente).
   - Esto evita confusiones entre zonas horarias.

2. **Verifica la zona horaria de la JVM / registros**
   - Confirma en el servidor de UAT: `java -Duser.timezone` o verifica una entrada de registro conocida vs `date` en Linux.
   - Si los registros no están en UTC, anota el desplazamiento.

3. **Verifica la zona horaria del servidor/perfil de Confluence**
   - Verifica si la marca de tiempo de subida que ves ya está ajustada a la zona horaria de tu perfil.
   - Ajústala de nuevo a UTC puro.

4. **Alinea con el reloj de la captura de pantalla**
   - Si la captura de pantalla muestra `2024-02-10 13:45` y sabes que el tester estaba en `Asia/Kolkata (UTC+5:30)`, entonces eso equivale a `2024-02-10 08:15 UTC`.
   - Si los registros muestran un evento a las `2024-02-10 08:15:23 UTC`, puedes hacerlos coincidir.

---

## 4. Flujo de trabajo del proceso (recomendado)

- **Paso 1:** Pide a los testers (o exige en las instrucciones de UAT) que incluyan su **zona horaria/ubicación** al subir capturas de pantalla, o mejor aún, solicítales que configuren correctamente el reloj del sistema.
- **Paso 2:** Al revisar los registros, primero convierte la marca de tiempo de la captura de pantalla (reloj local del tester) → UTC.
- **Paso 3:** Convierte la marca de tiempo del registro → UTC (aplicando la zona horaria de la JVM).
- **Paso 4:** Compara.

---

## 5. Ejemplo de mapeo

- Captura de pantalla: muestra `2024-06-01 14:05` (tester en Berlín, UTC+2).
  → UTC = `2024-06-01 12:05`.

- Confluence muestra la subida = `2024-06-01 12:07 UTC`.
  (tiene sentido – subida en ~2 minutos).

- Registro de UAT:
  ```
  2024-06-01 12:05:20,456 INFO UAT-Service [thread-19] ...
  ```
  Zona horaria de la JVM = UTC.
  → Coincidencia perfecta.

---

✅ **Punto clave:** Debes normalizar todas las marcas de tiempo a la misma zona horaria (normalmente UTC). Las capturas de pantalla de Windows muestran la hora local. Los registros de Java usan la zona horaria de la JVM. Confluence muestra la hora de subida en la zona horaria del servidor o del perfil de usuario. Sin esa normalización, nunca podrás alinearlos.

---

¿Te gustaría que redacte una **mini guía** para tu equipo de UAT, para que los testers sepan qué capturar (como "anotar siempre tu zona horaria al subir capturas de pantalla") y así sea más fácil la correlación con los registros?