---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correction de l'estimation de la charge de la batterie
translated: true
type: note
---

L'erreur `Cannot estimate time to full charge (sysfs files not found)` indique que le script n'a pas pu trouver les fichiers d'informations de batterie attendus dans `/sys/class/power_supply/BAT0/`. Cela peut arriver si :
1. La batterie a un nom différent de `BAT0` (par exemple, `BAT1` ou un autre nom).
2. Les fichiers spécifiques (`charge_now`, `charge_full`, `current_now`) ne sont pas disponibles ou ont des noms différents sur votre ordinateur portable Lenovo.
3. L'utilisateur exécutant le script n'a pas la permission d'accéder à ces fichiers.

Voici un script Python corrigé qui détecte dynamiquement le nom de la batterie et gère les variations dans les noms de fichiers sysfs (par exemple, `energy_now` au lieu de `charge_now` pour certains systèmes). Il inclut également une meilleure gestion des erreurs et des vérifications de permissions :

```python
import psutil
import os
import glob

def find_battery_path():
    """Trouve le répertoire de la batterie dans /sys/class/power_supply."""
    battery_paths = glob.glob('/sys/class/power_supply/BAT*')
    if not battery_paths:
        return None
    return battery_paths[0]  # Retourne la première batterie trouvée (ex: BAT0 ou BAT1)

def get_battery_info():
    try:
        # Obtenir les informations de la batterie en utilisant psutil
        battery = psutil.sensors_battery()
        
        if battery is None:
            print("Aucune batterie détectée.")
            return

        # Pourcentage de batterie
        percent = battery.percent
        print(f"Pourcentage de batterie : {percent:.2f}%")

        # Vérifier si la batterie est en charge
        is_charging = battery.power_plugged
        status = "En charge" if is_charging else "Décharge"
        print(f"Statut : {status}")

        # Estimer le temps restant (uniquement lors de la décharge)
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"Temps restant estimé : {hours} heures, {minutes} minutes")
        elif is_charging:
            # Essayer d'estimer le temps jusqu'à la charge complète en utilisant sysfs
            battery_path = find_battery_path()
            if not battery_path:
                print("Impossible d'estimer le temps jusqu'à la charge complète (aucune batterie trouvée dans sysfs).")
                return

            try:
                # Vérifier les fichiers basés sur la charge ou l'énergie
                charge_now_file = os.path.join(battery_path, 'charge_now')
                energy_now_file = os.path.join(battery_path, 'energy_now')
                charge_full_file = os.path.join(battery_path, 'charge_full')
                energy_full_file = os.path.join(battery_path, 'charge_full_design')
                current_now_file = os.path.join(battery_path, 'current_now')

                # Déterminer quels fichiers utiliser (charge ou énergie)
                if os.path.exists(charge_now_file) and os.path.exists(charge_full_file):
                    now_file, full_file = charge_now_file, charge_full_file
                elif os.path.exists(energy_now_file) and os.path.exists(energy_full_file):
                    now_file, full_file = energy_now_file, energy_full_file
                else:
                    print("Impossible d'estimer le temps jusqu'à la charge complète (fichiers charge/énergie non trouvés).")
                    return

                # Lire les données de la batterie
                with open(now_file, 'r') as f:
                    charge_now = int(f.read().strip())
                with open(full_file, 'r') as f:
                    charge_full = int(f.read().strip())
                with open(current_now_file, 'r') as f:
                    current_now = int(f.read().strip())

                if current_now > 0:
                    charge_remaining = charge_full - charge_now
                    seconds_to_full = (charge_remaining / current_now) * 3600
                    hours = int(seconds_to_full // 3600)
                    minutes = int((seconds_to_full % 3600) // 60)
                    print(f"Temps estimé jusqu'à la charge complète : {hours} heures, {minutes} minutes")
                else:
                    print("Impossible d'estimer le temps jusqu'à la charge complète (current_now est à 0).")
            except PermissionError:
                print("Impossible d'estimer le temps jusqu'à la charge complète (permission refusée). Essayez de lancer avec sudo.")
            except FileNotFoundError:
                print(f"Impossible d'estimer le temps jusqu'à la charge complète (fichiers sysfs non trouvés dans {battery_path}).")
            except Exception as e:
                print(f"Erreur lors de l'estimation du temps jusqu'à la charge complète : {e}")
        else:
            print("Aucune estimation de temps restant disponible.")

    except Exception as e:
        print(f"Erreur lors de la récupération des informations de la batterie : {e}")

if __name__ == "__main__":
    get_battery_info()
```

### Modifications apportées
1. **Détection dynamique de la batterie** :
   - Utilise `glob.glob('/sys/class/power_supply/BAT*')` pour trouver le répertoire de la batterie (ex: `BAT0`, `BAT1`) au lieu de coder en dur `BAT0`.
   - Retourne la première batterie trouvée ou `None` si aucune batterie n'est détectée.

2. **Support des fichiers de charge et d'énergie** :
   - Vérifie la présence des fichiers `charge_now`/`charge_full` et `energy_now`/`energy_full`, car certains systèmes utilisent des métriques basées sur l'énergie (en watt-heures) au lieu de la charge (en microampère-heures).
   - Sélectionne la paire de fichiers appropriée en fonction de leur disponibilité.

3. **Gestion améliorée des erreurs** :
   - Gère `PermissionError` séparément pour suggérer l'exécution avec `sudo` si l'accès est refusé.
   - Fournit des retours spécifiques si les fichiers sysfs ne sont pas trouvés ou si `current_now` est zéro.

4. **Sortie formatée** :
   - Limite le pourcentage de batterie à deux décimales (`{percent:.2f}`) pour une sortie plus claire.

### Comment utiliser
1. **Installer `psutil` (si ce n'est pas déjà fait)** :
   ```bash
   sudo pip3 install psutil
   ```

2. **Sauvegarder le script** :
   - Sauvegardez le script mis à jour sous, par exemple, `battery_info.py`.

3. **Exécuter le script** :
   - Exécutez dans un terminal :
     ```bash
     python3 battery_info.py
     ```
   - Si vous obtenez une erreur "permission denied", essayez d'exécuter avec des privilèges élevés :
     ```bash
     sudo python3 battery_info.py
     ```

4. **Vérifier le chemin de la batterie** :
   - Pour vérifier le nom de la batterie et les fichiers disponibles, exécutez :
     ```bash
     ls /sys/class/power_supply
     ```
     Ensuite, vérifiez le contenu du répertoire de la batterie (ex: `BAT0` ou `BAT1`) :
     ```bash
     ls /sys/class/power_supply/BAT0
     ```
   - Recherchez des fichiers comme `charge_now`, `charge_full`, `energy_now`, `energy_full`, ou `current_now`. S'ils diffèrent (par exemple, `energy_full_design` au lieu de `charge_full`), le script devrait le gérer, mais faites-moi savoir si vous avez besoin d'ajustements supplémentaires.

### Conseils de débogage
- Si le script signale toujours "sysfs files not found", vérifiez les noms exacts des fichiers dans `/sys/class/power_supply/BAT*`. Certains ordinateurs portables Lenovo peuvent utiliser des noms non standard ou avoir un support sysfs limité.
- Si vous voyez "permission denied", l'exécution avec `sudo` devrait résoudre le problème, mais soyez prudent avec les privilèges élevés.
- Si la batterie est détectée mais aucune estimation de temps n'est fournie, cela peut être dû au fait que `current_now` est zéro (courant lorsque le système ne rapporte pas activement le courant de charge). Dans ce cas, le script indiquera qu'aucune estimation n'est disponible.

### Exemple de sortie
Sur votre système (Lenovo XiaoXin-14-IAH8), vous pourriez voir quelque chose comme :
```
Pourcentage de batterie : 49.62%
Statut : En charge
Temps estimé jusqu'à la charge complète : 1 heures, 45 minutes
```
Ou, si les fichiers sont toujours manquants :
```
Pourcentage de batterie : 49.62%
Statut : En charge
Impossible d'estimer le temps jusqu'à la charge complète (fichiers sysfs non trouvés dans /sys/class/power_supply/BAT0).
```

### Si les problèmes persistent
Si le script échoue toujours à trouver les fichiers sysfs, veuillez partager la sortie de :
```bash
ls -l /sys/class/power_supply
ls -l /sys/class/power_supply/BAT*/*
```
Cela aidera à identifier les noms exacts des fichiers et les permissions. Je pourrai alors adapter davantage le script pour correspondre à la configuration de votre système.

[Documentation psutil](https://psutil.readthedocs.io/en/latest/)  
[Linux sysfs Power Supply](https://www.kernel.org/doc/html/latest/power/power_supply_class.html)