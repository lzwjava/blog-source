---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía de Configuración de Depuración Remota de IntelliJ
translated: true
type: note
---

Respuesta corta: sí—si mantienes sincronizada la compilación y la JVM en ejecución, el depurador remoto de IntelliJ se conectará correctamente. Aquí tienes una forma sólida y sin complicaciones de hacerlo tanto con Liberty localmente como en Cloud Foundry.

## 1) Previene el "desajuste de clases" antes de conectarte

* Siempre alinea los JDK: la versión principal del JDK utilizada por la compilación de Maven, la JVM de Liberty y (si está en CF) el JDK del buildpack de Java debe coincidir. En Maven, fíjala con `maven-compiler-plugin` (`release` o `source/target`) y asegúrate de que Liberty/CF use el mismo.
* Limpia el bytecode obsoleto al cambiar de ramas o activar/desactivar módulos: `mvn clean package -DskipTests` es la barrera de protección más simple.
* En IntelliJ, también haz "Rebuild Project" una vez si previamente mezclaste compilaciones del IDE y de Maven.

## 2) Recompilación automática solo cuando es importante (regla de los 30 minutos)

Si quieres recompilar solo cuando las clases compiladas tengan más de 30 minutos, envuelve Maven en una pequeña verificación.

### Bash (macOS/Linux)

```bash
#!/usr/bin/env bash
set -euo pipefail

CLASSES_DIR="target/classes"
THRESHOLD_MIN=30

needs_build() {
  # ¿No hay clases todavía?
  [[ ! -d "$CLASSES_DIR" ]] && return 0
  # ¿La última modificación de una clase es más antigua que el umbral?
  last_mod_epoch=$(find "$CLASSES_DIR" -type f -name '*.class' -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
  [[ -z "${last_mod_epoch:-}" ]] && return 0
  now_epoch=$(date +%s)
  diff_min=$(( ( now_epoch - ${last_mod_epoch%.*} ) / 60 ))
  (( diff_min >= THRESHOLD_MIN ))
}

if needs_build; then
  echo "Las clases son antiguas (>= ${THRESHOLD_MIN}m) o no existen — compilando…"
  mvn clean package -DskipTests
else
  echo "Las clases son recientes (< ${THRESHOLD_MIN}m) — omitiendo compilación."
fi
```

### PowerShell (Windows)

```powershell
$classes = "target\classes"
$thresholdMin = 30

function Needs-Build {
  if (-not (Test-Path $classes)) { return $true }
  $last = Get-ChildItem $classes -Recurse -Filter *.class |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
  if (-not $last) { return $true }
  $age = (New-TimeSpan -Start $last.LastWriteTime -End (Get-Date)).TotalMinutes
  return ($age -ge $thresholdMin)
}

if (Needs-Build) {
  Write-Host "Las clases son antiguas (>= $thresholdMin m) o no existen — compilando…"
  mvn clean package -DskipTests
} else {
  Write-Host "Las clases son recientes (< $thresholdMin m) — omitiendo compilación."
}
```

## 3) Liberty (local) — inicia en modo debug y conéctate desde IntelliJ

Tienes dos opciones fáciles:

**A. Inicio de depuración único**

```bash
server debug myServer   # JDWP por defecto en el puerto 7777
```

**B. Configuración permanente**

* En `wlp/usr/servers/myServer/jvm.options`:

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777
```

* O mediante variable de entorno:

```
WLP_DEBUG_ADDRESS=7777
WLP_DEBUG_SUSPEND=false
```

**Conexión desde IntelliJ**

* Run → “Edit Configurations…” → “Remote JVM Debug”.
* Host: `localhost`, Port: `7777`.
* Pulsa Debug; deberías ver “Connected to the target VM…” y los puntos de interrupción se vincularán.

> Consejo: después de una recompilación, Liberty carga las clases actualizadas para la mayoría de las características via hot swap. Si la firma de un método o la estructura de una clase cambió, necesitarás reiniciar el servidor para que esos cambios se carguen.

## 4) Cloud Foundry (PCF) — qué es realista

CF ejecuta aplicaciones detrás de su capa de enrutamiento; típicamente no puedes exponer un puerto JDWP directamente. Tienes dos patrones viables:

**Opción 1: Depuración del buildpack + túnel SSH (solo para dev/staging)**

1. Habilita la depuración JVM en el buildpack de Java:

   * Establece la variable de entorno antes del push (los nombres varían ligeramente según la versión del buildpack):

   ```
   cf set-env <APP> JBP_CONFIG_DEBUG '{enabled: true, port: 7777}'
   ```
2. Reorganiza (restage):

   ```
   cf restage <APP>
   ```
3. Abre un túnel SSH:

   ```
   cf ssh -N -L 7777:localhost:7777 <APP>
   ```
4. En IntelliJ, conéctate a `localhost:7777`.

**Opción 2: Usar JMX/Diagnósticos de CF SSH en lugar de JDWP**

* Cuando JDWP directo no esté permitido, recurre a:

  * logs de la aplicación + loggers específicos,
  * volcados de hilos/memoria (thread/heap dumps) via `cf ssh` + `jcmd`/`jmap` (si están presentes),
  * flags de características como el trace de Liberty y los endpoints de health.

> Comprobación de la realidad: muchas organizaciones de CF deshabilitan los puertos de depuración en prod. Trata el JDWP remoto en CF como una ruta solo para depuración en espacios que no sean de producción. Si tu equipo de plataforma lo bloquea, recurre a los logs + diagnósticos SSH.

## 5) Causas comunes de "no se pudieron vincular los puntos de interrupción" (y soluciones)

* **Desajuste de archivo de clase**: recompilación limpia (clean rebuild); verifica que solo haya una copia de la clase en el classpath de ejecución (cuidado con los fat JARs o módulos duplicados).
* **Puerto JDWP incorrecto**: confirma que Liberty esté realmente escuchando (logs de `server debug` o `netstat` localmente; para CF, la línea del túnel SSH debe coincidir).
* **JDK principal diferente**: asegúrate de que los JDK de Maven/Liberty/CF sean los mismos (ej., todos Java 17).
* **Información de depuración del compilador eliminada**: asegúrate de que `maven-compiler-plugin` no esté usando `-g:none`. El valor por defecto está bien; si está personalizado, incluye `-g`.
* **Recarga necesaria**: después de cambios de firma, reinicia Liberty (o haz restage en CF).

---

Si lo configuras como se indicó arriba—ya sea siempre con `mvn clean package` o con el wrapper de "frescura de 30 minutos"—el depurador remoto de IntelliJ se conectará de forma fiable a Liberty, y puede funcionar en CF a través de un túnel SSH en entornos que no sean de producción.