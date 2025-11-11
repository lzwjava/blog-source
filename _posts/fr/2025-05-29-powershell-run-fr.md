---
audio: false
generated: true
lang: fr
layout: post
title: 'PowerShell : Exécuter des commandes dans le terminal actuel'
translated: true
type: note
---

Pour exécuter des commandes comme `mvn` ou des commandes de serveur WebSphere directement dans le terminal PowerShell actuel sans ouvrir une nouvelle invite de commande, vous pouvez utiliser l'opérateur d'appel (`&`) ou invoquer directement la commande. Cette approche garantit que la commande s'exécute dans la session PowerShell existante, en conservant la sortie et les erreurs dans le même terminal.

Voici comment procéder :

1. **Exécuter Directement la Commande** :
   Si la commande (par exemple, `mvn`) se trouve dans le PATH de votre système ou est accessible dans le répertoire courant, tapez simplement la commande comme vous le feriez dans un terminal :

   ```powershell
   mvn clean install
   ```

   Cela exécute `mvn` directement dans la session PowerShell, et la sortie reste dans le terminal actuel.

2. **Utiliser l'Opérateur d'Appel (`&`)** :
   Si vous devez spécifier le chemin vers l'exécutable ou si la commande est stockée dans une variable, utilisez l'opérateur d'appel :

   ```powershell
   & "C:\chemin\vers\maven\bin\mvn.cmd" clean install
   ```

   Pour les commandes de serveur WebSphere, si vous exécutez quelque chose comme `wsadmin` ou `startServer`, vous pouvez faire :

   ```powershell
   & "C:\chemin\vers\WebSphere\AppServer\bin\startServer.bat" server1
   ```

   L'opérateur `&` garantit que la commande s'exécute dans la session PowerShell actuelle.

3. **Gérer les Commandes avec Espaces ou Variables** :
   Si le chemin de la commande contient des espaces ou est stocké dans une variable, utilisez `&` avec le chemin entre guillemets :

   ```powershell
   $mvnPath = "C:\Program Files\Apache Maven\bin\mvn.cmd"
   & $mvnPath clean install
   ```

4. **Définir les Variables d'Environnement (si nécessaire)** :
   Certaines commandes comme `mvn` ou les scripts WebSphere peuvent nécessiter des variables d'environnement (par exemple, `JAVA_HOME` ou `WAS_HOME`). Définissez-les dans le script avant d'exécuter la commande :

   ```powershell
   $env:JAVA_HOME = "C:\chemin\vers\jdk"
   $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
   mvn --version
   ```

   Pour WebSphere :

   ```powershell
   $env:WAS_HOME = "C:\chemin\vers\WebSphere\AppServer"
   & "$env:WAS_HOME\bin\startServer.bat" server1
   ```

5. **Capturer la Sortie ou Gérer les Erreurs** :
   Pour capturer la sortie de la commande ou gérer les erreurs, utilisez les mécanismes standard de PowerShell :

   ```powershell
   try {
       $output = & mvn clean install 2>&1
       Write-Output $output
   } catch {
       Write-Error "Échec de l'exécution de Maven : $_"
   }
   ```

6. **Éviter `Start-Process`** :
   Contrairement à `Start-Process`, qui lance un nouveau processus (souvent dans une fenêtre séparée), les méthodes ci-dessus conservent l'exécution dans la session actuelle. Évitez d'utiliser `Start-Process` comme ceci :

   ```powershell
   # Cela ouvrira une nouvelle fenêtre d'invite de commande
   Start-Process -FilePath "mvn" -ArgumentList "clean install"
   ```

   Utilisez plutôt l'exécution directe ou `&`.

### Exemple de Script
Voici un exemple de script PowerShell pour exécuter `mvn` et une commande WebSphere dans le terminal actuel :

```powershell
# Définir les variables d'environnement si nécessaire
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11"
$env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
$env:WAS_HOME = "C:\IBM\WebSphere\AppServer"

# Exécuter la commande Maven
Write-Output "Exécution de Maven..."
& mvn clean install

# Exécuter la commande du serveur WebSphere
Write-Output "Démarrage du serveur WebSphere..."
& "$env:WAS_HOME\bin\startServer.bat" server1
```

### Notes
- Assurez-vous que les outils en ligne de commande (`mvn`, `startServer.bat`, etc.) sont dans votre PATH ou fournissez le chemin complet vers l'exécutable.
- Si la commande nécessite un répertoire de travail spécifique, utilisez `Set-Location` (ou `cd`) avant de l'exécuter :

   ```powershell
   Set-Location "C:\chemin\vers\projet"
   & mvn clean install
   ```

- Pour les commandes qui dépendent de fichiers `.bat` ou `.cmd` (courant avec WebSphere), l'opérateur `&` fonctionne bien, mais assurez-vous que le script s'exécute dans PowerShell, et non dans `cmd.exe`.
- Si vous rencontrez des problèmes avec les variables d'environnement ou le PATH, vérifiez-les avec `Get-ChildItem Env:`.

Cette approche maintient tout dans le terminal PowerShell actuel, évitant de nouvelles fenêtres et conservant un flux de travail propre. Si vous avez une commande ou une configuration spécifique posant problème, partagez plus de détails et je pourrai adapter la solution davantage.