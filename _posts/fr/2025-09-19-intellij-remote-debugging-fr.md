---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide de configuration du débogage distant IntelliJ
translated: true
type: note
---

Réponse courte : oui — si vous maintenez la synchronisation entre la build et la JVM d'exécution, le débogage distant d'IntelliJ s'attachera correctement. Voici une méthode robuste et sans complications pour y parvenir localement avec Liberty et sur Cloud Foundry.

## 1) Empêcher l'« incompatibilité de classe » avant de vous attacher

* Alignez toujours les JDK : la version majeure du JDK utilisé par la compilation Maven, la JVM de Liberty et (si sur CF) le JDK du buildpack Java doivent correspondre. Dans Maven, fixez-la avec `maven-compiler-plugin` (`release` ou `source/target`) et assurez-vous que Liberty/CF utilise la même.
* Nettoyez le bytecode obsolète lors du changement de branche ou de l'activation/désactivation de modules : `mvn clean package -DskipTests` est la garde-fou la plus simple.
* Dans IntelliJ, effectuez aussi un « Rebuild Project » une fois si vous avez mélangé auparavant la build de l'IDE et la build Maven.

## 2) Reconstruire automatiquement seulement quand c'est nécessaire (règle des 30 minutes)

Si vous souhaitez ne reconstruire que lorsque les classes compilées ont plus de 30 minutes, encapsulez Maven dans une petite vérification.

### Bash (macOS/Linux)

```bash
#!/usr/bin/env bash
set -euo pipefail

CLASSES_DIR="target/classes"
THRESHOLD_MIN=30

needs_build() {
  # aucune classe pour l'instant ?
  [[ ! -d "$CLASSES_DIR" ]] && return 0
  # la date de modif de la dernière classe est-elle supérieure au seuil ?
  last_mod_epoch=$(find "$CLASSES_DIR" -type f -name '*.class' -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
  [[ -z "${last_mod_epoch:-}" ]] && return 0
  now_epoch=$(date +%s)
  diff_min=$(( ( now_epoch - ${last_mod_epoch%.*} ) / 60 ))
  (( diff_min >= THRESHOLD_MIN ))
}

if needs_build; then
  echo "Les classes sont anciennes (>= ${THRESHOLD_MIN}m) ou manquantes — construction…"
  mvn clean package -DskipTests
else
  echo "Les classes sont récentes (< ${THRESHOLD_MIN}m) — pas de build."
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
  Write-Host "Les classes sont anciennes (>= $thresholdMin m) ou manquantes — construction…"
  mvn clean package -DskipTests
} else {
  Write-Host "Les classes sont récentes (< $thresholdMin m) — pas de build."
}
```

## 3) Liberty (local) — démarrer en mode debug et s'attacher depuis IntelliJ

Vous avez deux options simples :

**A. Démarrage debug unique**

```bash
server debug myServer   # JDWP par défaut sur le port 7777
```

**B. Configuration permanente**

* Dans `wlp/usr/servers/myServer/jvm.options` :

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777
```

* Ou via les variables d'environnement :

```
WLP_DEBUG_ADDRESS=7777
WLP_DEBUG_SUSPEND=false
```

**Attachement IntelliJ**

* Run → « Edit Configurations… » → « Remote JVM Debug ».
* Host : `localhost`, Port : `7777`.
* Cliquez sur Debug ; vous devriez voir « Connected to the target VM… » et les points d'arrêt se lieront.

> Astuce : après une reconstruction, Liberty récupère les classes mises à jour pour la plupart des fonctionnalités via le hot swap. Si une signature de méthode ou la structure d'une classe a changé, vous devrez redémarrer le serveur pour que ces changements soient chargés.

## 4) Cloud Foundry (PCF) — ce qui est réaliste

CF exécute les applications derrière sa couche de routage ; vous ne pouvez généralement pas exposer directement un port JDWP. Vous avez deux modèles utilisables :

**Option 1 : Debug du buildpack + tunnel SSH (uniquement pour dev/staging)**

1. Activez le debug JVM dans le buildpack Java :

   * Définissez les variables d'environnement avant le push (les noms varient légèrement selon la version du buildpack) :

   ```
   cf set-env <APP> JBP_CONFIG_DEBUG '{enabled: true, port: 7777}'
   ```
2. Restagez :

   ```
   cf restage <APP>
   ```
3. Ouvrez un tunnel SSH :

   ```
   cf ssh -N -L 7777:localhost:7777 <APP>
   ```
4. Dans IntelliJ, attachez-vous à `localhost:7777`.

**Option 2 : Utiliser CF SSH JMX/Diagnostics au lieu de JDWP**

* Lorsque le JDWP direct n'est pas autorisé, utilisez :

  * les logs de l'application + les loggers ciblés,
  * les thread/heap dumps via `cf ssh` + `jcmd`/`jmap` (s'ils sont présents),
  * les feature flags comme les endpoints de trace et de santé de Liberty.

> Vérification de la réalité : de nombreuses organisations CF désactivent les ports de debug en prod. Considérez le JDWP distant sur CF comme une voie de debug uniquement pour les environnements non-prod. Si votre équipe plateforme le bloque, revenez aux logs + diagnostics SSH.

## 5) Causes courantes des « échecs de liaison des points d'arrêt » (et correctifs)

* **Incompatibilité des fichiers de classe** : reconstruction propre ; vérifiez qu'il n'existe qu'une seule copie de la classe dans le classpath d'exécution (attention aux fat JARs ou modules dupliqués).
* **Mauvais port JDWP** : confirmez que Liberty écoute réellement (logs `server debug` ou `netstat` en local ; pour CF, la ligne du tunnel SSH doit correspondre).
* **JDK majeur différent** : assurez-vous que les JDK Maven/Liberty/CF sont les mêmes (par ex., tous en Java 17).
* **Infos de debug du compilateur supprimées** : assurez-vous que `maven-compiler-plugin` n'utilise pas `-g:none`. La valeur par défaut est correcte ; si elle est personnalisée, incluez `-g`.
* **Rechargement nécessaire** : après des changements de signature, redémarrez Liberty (ou restagez sur CF).

---

Si vous le configurez comme ci-dessus — soit toujours `mvn clean package` soit avec le wrapper de « fraîcheur 30 minutes » — le débogage distant d'IntelliJ s'attachera de manière fiable à Liberty, et cela peut fonctionner sur CF via un tunnel SSH en environnement non-prod.