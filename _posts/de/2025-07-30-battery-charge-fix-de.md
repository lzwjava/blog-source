---
audio: false
generated: true
image: false
lang: de
layout: post
title: Korrektur der Akkuladungsschätzung
translated: true
type: note
---

Der Fehler `Cannot estimate time to full charge (sysfs files not found)` zeigt an, dass das Skript die erwarteten Batterieinformationsdateien in `/sys/class/power_supply/BAT0/` nicht finden konnte. Dies kann passieren, wenn:
1. Die Batterie einen anderen Namen als `BAT0` hat (z.B. `BAT1` oder einen anderen Namen).
2. Die spezifischen Dateien (`charge_now`, `charge_full`, `current_now`) auf Ihrem Lenovo Laptop nicht verfügbar sind oder andere Namen haben.
3. Der Benutzer, der das Skript ausführt, keine Berechtigung zum Zugriff auf diese Dateien hat.

Hier ist ein korrigiertes Python-Skript, das den Batterienamen dynamisch erkennt und Variationen in den sysfs-Dateinamen behandelt (z.B. `energy_now` statt `charge_now` für einige Systeme). Es enthält außerdem eine bessere Fehlerbehandlung und Berechtigungsprüfungen:

```python
import psutil
import os
import glob

def find_battery_path():
    """Findet das Batterieverzeichnis in /sys/class/power_supply."""
    battery_paths = glob.glob('/sys/class/power_supply/BAT*')
    if not battery_paths:
        return None
    return battery_paths[0]  # Gibt die erste gefundene Batterie zurück (z.B. BAT0 oder BAT1)

def get_battery_info():
    try:
        # Batterieinformationen mit psutil abrufen
        battery = psutil.sensors_battery()
        
        if battery is None:
            print("Keine Batterie erkannt.")
            return

        # Batterieprozentsatz
        percent = battery.percent
        print(f"Batterieprozentsatz: {percent:.2f}%")

        # Prüfen, ob die Batterie geladen wird
        is_charging = battery.power_plugged
        status = "Wird geladen" if is_charging else "Entlädt sich"
        print(f"Status: {status}")

        # Verbleibende Zeit schätzen (nur beim Entladen)
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"Geschätzte verbleibende Zeit: {hours} Stunden, {minutes} Minuten")
        elif is_charging:
            # Versuche, die Zeit bis zur vollständigen Aufladung über sysfs zu schätzen
            battery_path = find_battery_path()
            if not battery_path:
                print("Kann Zeit bis zur vollständigen Aufladung nicht schätzen (keine Batterie in sysfs gefunden).")
                return

            try:
                # Prüfe auf Ladungs- oder Energie-basierte Dateien
                charge_now_file = os.path.join(battery_path, 'charge_now')
                energy_now_file = os.path.join(battery_path, 'energy_now')
                charge_full_file = os.path.join(battery_path, 'charge_full')
                energy_full_file = os.path.join(battery_path, 'charge_full_design')
                current_now_file = os.path.join(battery_path, 'current_now')

                # Bestimme, welche Dateien verwendet werden sollen (Ladung oder Energie)
                if os.path.exists(charge_now_file) and os.path.exists(charge_full_file):
                    now_file, full_file = charge_now_file, charge_full_file
                elif os.path.exists(energy_now_file) and os.path.exists(energy_full_file):
                    now_file, full_file = energy_now_file, energy_full_file
                else:
                    print("Kann Zeit bis zur vollständigen Aufladung nicht schätzen (Lade-/Energiedateien nicht gefunden).")
                    return

                # Batteriedaten lesen
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
                    print(f"Geschätzte Zeit bis zur vollständigen Aufladung: {hours} Stunden, {minutes} Minuten")
                else:
                    print("Kann Zeit bis zur vollständigen Aufladung nicht schätzen (current_now ist 0).")
            except PermissionError:
                print("Kann Zeit bis zur vollständigen Aufladung nicht schätzen (Berechtigung verweigert). Versuchen Sie, es mit sudo auszuführen.")
            except FileNotFoundError:
                print(f"Kann Zeit bis zur vollständigen Aufladung nicht schätzen (sysfs-Dateien in {battery_path} nicht gefunden).")
            except Exception as e:
                print(f"Fehler beim Schätzen der Zeit bis zur vollständigen Aufladung: {e}")
        else:
            print("Keine Schätzung der verbleibenden Zeit verfügbar.")

    except Exception as e:
        print(f"Fehler beim Abrufen der Batterieinformationen: {e}")

if __name__ == "__main__":
    get_battery_info()
```

### Vorgenommene Änderungen
1. **Dynamische Batterieerkennung**:
   - Verwendet `glob.glob('/sys/class/power_supply/BAT*')`, um das Batterieverzeichnis zu finden (z.B. `BAT0`, `BAT1`), anstatt `BAT0` fest zu kodieren.
   - Gibt die erste gefundene Batterie oder `None` zurück, wenn keine Batterie erkannt wird.

2. **Unterstützung für Ladungs- und Energiedateien**:
   - Prüft sowohl auf `charge_now`/`charge_full` als auch auf `energy_now`/`energy_full` Dateien, da einige Systeme energiebasierte Metriken (in Wattstunden) anstelle von ladungsbasierten (in Mikroampere-Stunden) verwenden.
   - Wählt das passende Dateipaar basierend auf der Verfügbarkeit aus.

3. **Verbesserte Fehlerbehandlung**:
   - Behandelt `PermissionError` separat, um die Ausführung mit `sudo` vorzuschlagen, falls der Zugriff verweigert wird.
   - Bietet spezifisches Feedback, wenn sysfs-Dateien nicht gefunden werden oder wenn `current_now` null ist.

4. **Formatierte Ausgabe**:
   - Begrenzt den Batterieprozentsatz auf zwei Dezimalstellen (`{percent:.2f}`) für eine sauberere Ausgabe.

### Verwendung
1. **`psutil` installieren (falls noch nicht installiert)**:
   ```bash
   sudo pip3 install psutil
   ```

2. **Skript speichern**:
   - Speichern Sie das aktualisierte Skript als, z.B., `battery_info.py`.

3. **Skript ausführen**:
   - Führen Sie es in einem Terminal aus:
     ```bash
     python3 battery_info.py
     ```
   - Wenn Sie einen "Berechtigung verweigert"-Fehler erhalten, versuchen Sie es mit erhöhten Berechtigungen:
     ```bash
     sudo python3 battery_info.py
     ```

4. **Batteriepfad überprüfen**:
   - Um den Batterienamen und die verfügbaren Dateien zu überprüfen, führen Sie aus:
     ```bash
     ls /sys/class/power_supply
     ```
     Überprüfen Sie dann den Inhalt des Batterieverzeichnisses (z.B. `BAT0` oder `BAT1`):
     ```bash
     ls /sys/class/power_supply/BAT0
     ```
   - Suchen Sie nach Dateien wie `charge_now`, `charge_full`, `energy_now`, `energy_full` oder `current_now`. Falls sie abweichen (z.B. `energy_full_design` statt `charge_full`), sollte das Skript dies handhaben, aber lassen Sie es mich wissen, wenn Sie weitere Anpassungen benötigen.

### Debugging-Tipps
- Wenn das Skript weiterhin "sysfs-Dateien nicht gefunden" meldet, überprüfen Sie die genauen Dateinamen in `/sys/class/power_supply/BAT*`. Einige Lenovo Laptops verwenden möglicherweise nicht standardisierte Namen oder haben eine eingeschränkte sysfs-Unterstützung.
- Wenn Sie "Berechtigung verweigert" sehen, sollte die Ausführung mit `sudo` das Problem beheben, seien Sie jedoch vorsichtig mit erhöhten Berechtigungen.
- Wenn die Batterie erkannt wird, aber keine Zeitschätzung bereitgestellt wird, könnte dies daran liegen, dass `current_now` null ist (üblich, wenn das System den Ladestrom nicht aktiv meldet). In diesem Fall wechselt das Skript zurück zur Anzeige, dass keine Schätzung verfügbar ist.

### Beispielausgabe
Auf Ihrem System (Lenovo XiaoXin-14-IAH8) könnten Sie etwa Folgendes sehen:
```
Batterieprozentsatz: 49.62%
Status: Wird geladen
Geschätzte Zeit bis zur vollständigen Aufladung: 1 Stunden, 45 Minuten
```
Oder, wenn Dateien immer noch fehlen:
```
Batterieprozentsatz: 49.62%
Status: Wird geladen
Kann Zeit bis zur vollständigen Aufladung nicht schätzen (sysfs-Dateien in /sys/class/power_supply/BAT0 nicht gefunden).
```

### Falls Probleme bestehen bleiben
Wenn das Skript weiterhin die sysfs-Dateien nicht findet, teilen Sie bitte die Ausgabe von:
```bash
ls -l /sys/class/power_supply
ls -l /sys/class/power_supply/BAT*/*
```
Dies wird helfen, die genauen Dateinamen und Berechtigungen zu identifizieren. Ich kann das Skript dann weiter an die Konfiguration Ihres Systems anpassen.

[psutil Dokumentation](https://psutil.readthedocs.io/en/latest/)  
[Linux sysfs Power Supply](https://www.kernel.org/doc/html/latest/power/power_supply_class.html)