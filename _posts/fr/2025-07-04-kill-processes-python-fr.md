---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Mettre fin aux processus avec Python
translated: true
type: note
---

### Utilisation de Python pour tuer des processus sur Windows

Pour tuer des processus de manière programmatique sur Windows, vous utiliserez principalement le module `subprocess` pour invoquer des commandes système comme `taskkill`. Le module `signal` est axé sur Unix et ne gère pas de manière fiable la terminaison de processus sur Windows (les signaux comme SIGKILL ne sont pas pris en charge nativement ; `os.kill()` peut envoyer des signaux limités, mais ce n'est pas idéal pour une terminaison complète des processus). Le module `platform` peut aider à confirmer que vous êtes sur Windows pour un comportement spécifique au système d'exploitation.

#### Étape 1 : Installer et importer les modules
- `subprocess`, `signal` et `platform` font partie de la bibliothèque standard de Python, donc aucune installation n'est nécessaire.
- Exemple d'imports :

```python
import subprocess
import platform
import os  # Pour l'accès au PID, si nécessaire
```

#### Étape 2 : Détecter le système d'exploitation Windows (en utilisant `platform`)
- Confirmer l'environnement pour éviter les problèmes multiplateformes :

```python
if platform.system() == 'Windows':
    print("Exécution sur Windows - utilisation de méthodes de terminaison compatibles.")
```

#### Étape 3 : Tuer un processus
- Pour tuer un processus existant par son identifiant de processus (PID) ou son nom, utilisez `taskkill` via `subprocess`. C'est la méthode native fiable sous Windows, car `subprocess.terminate()` ou `.kill()` ne fonctionne que sur les processus que vous avez lancés avec `subprocess.Popen`.
- Exemple : Tuer un processus par PID (de force avec l'option `/F`). Remplacez `1234` par le PID réel.

```python
def kill_process_by_pid(pid):
    try:
        subprocess.call(['taskkill', '/PID', str(pid), '/F'])
        print(f"Processus {pid} terminé.")
    except subprocess.CalledProcessError as e:
        print(f"Échec de la terminaison du processus {pid} : {e}")

# Utilisation
kill_process_by_pid(1234)
```

- Tuer par nom de processus (par exemple, 'notepad.exe'), ce qui tue tous les processus correspondants :

```python
def kill_process_by_name(name):
    try:
        subprocess.call(['taskkill', '/IM', name, '/F'])
        print(f"Processus correspondant à '{name}' terminés.")
    except subprocess.CalledProcessError as e:
        print(f"Échec de la terminaison des processus '{name}' : {e}")

# Utilisation
kill_process_by_name('notepad.exe')
```

#### Limitations et notes
- `subprocess` invoque des commandes externes, assurez-vous donc que votre script dispose des autorisations appropriées (par exemple, exécutez en tant qu'administrateur pour les processus système).
- Pour un processus lancé via `subprocess.Popen`, utilisez `.terminate()` (arrêt poli) ou `.kill()` (forcé) directement :

```python
proc = subprocess.Popen(['notepad.exe'])  # Lancement
proc.kill()  # Le tuer
```

- Module `signal` : L'utilisation de `os.kill(pid, signal.SIGTERM)` peut fonctionner pour certains signaux sur Windows (Python 3.2+), mais c'est moins robuste et peut ne pas terminer tous les processus. Par exemple :

```python
import signal
os.kill(pid, signal.SIGTERM)  # Peut se fermer doucement ; pas garanti
```

Évitez de compter sur `signal` pour la terminaison sous Windows - utilisez `subprocess` avec `taskkill` pour de meilleurs résultats.

Si vous avez besoin de lister les PID (par exemple, via la commande `tasklist`), vous pouvez d'abord les interroger pour une terminaison dynamique. Pour une gestion avancée des processus, envisagez des bibliothèques tierces comme `psutil`, mais les méthodes ci-dessus n'utilisent que des modules standard.