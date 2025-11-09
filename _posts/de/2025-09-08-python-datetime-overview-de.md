---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Übersicht des Python-Datetime-Moduls
translated: true
type: note
---

### Überblick über Pythons datetime-Modul

Pythons `datetime`-Modul bietet Klassen zur Manipulation von Datumsangaben, Uhrzeiten und Zeitstempeln. Es ist Teil der Standardbibliothek, daher ist keine Installation erforderlich. Wichtige Klassen sind:
- `date`: Verarbeitet Datumsangaben (Jahr, Monat, Tag).
- `time`: Verarbeitet Uhrzeiten (Stunde, Minute, Sekunde, Mikrosekunde).
- `datetime`: Kombiniert Datum und Uhrzeit.
- `timedelta`: Stellt eine Dauer dar (z. B. für Datumsarithmetik).

Es ist nützlich für Aufgaben wie das Protokollieren von Zeitstempeln, das Berechnen von Dauern oder das Formatieren von Datumsangaben für die Anzeige/Ausgabe.

### Importieren des Moduls

Importieren Sie das gesamte Modul oder spezifische Klassen nach Bedarf:

```python
import datetime  # Vollständiges Modul

# Oder importieren Sie spezifische Klassen
from datetime import datetime, date, time, timedelta
```

### Aktuelles Datum und Uhrzeit abrufen

Verwenden Sie `datetime.now()`, um das aktuelle lokale Datum und die Uhrzeit als `datetime`-Objekt zu erhalten.

```python
import datetime

now = datetime.datetime.now()
print(now)  # Ausgabe: z.B. 2023-10-05 14:30:45.123456
print(type(now))  # <class 'datetime.datetime'>
```

Für UTC-Zeit verwenden Sie `datetime.utcnow()` (bevorzugt wird jedoch `datetime.now(timezone.utc)` mit Imports aus `datetime.timezone` für Zeitzonenbewusstsein).

### Erstellen von Datums- und Zeitobjekten

Erstellen Sie Objekte manuell mit ihren Konstruktoren.

```python
# Datum: Jahr, Monat, Tag
d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05

# Zeit: Stunde, Minute, Sekunde, Mikrosekunde (optional)
t = datetime.time(14, 30, 45)
print(t)  # 14:30:45

# Datetime: Kombiniert Datum und Uhrzeit
dt = datetime.datetime(2023, 10, 5, 14, 30, 45)
print(dt)  # 2023-10-05 14:30:45
```

Teile, die nicht benötigt werden, können weggelassen werden (z. B. erstellt `datetime.datetime(2023, 10, 5)` ein datetime-Objekt um Mitternacht).

### Formatieren von Datumsangaben (strftime)

Wandeln Sie Datumsangaben in Strings um, indem Sie `strftime` mit Formatcodes verwenden (z. B. `%Y` für Jahr, `%m` für Monat).

```python
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # z.B. 2023-10-05 14:30:45

# Häufige Formate:
# %A: Vollständiger Wochentag (z.B. Thursday)
# %B: Vollständiger Monat (z.B. October)
# %Y-%m-%d: ISO-Datum
```

### Parsen von Datumsangaben aus Strings (strptime)

Wandeln Sie Strings in `datetime`-Objekte um, indem Sie `strptime` mit passenden Formaten verwenden.

```python
date_str = "2023-10-05 14:30:45"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2023-10-05 14:30:45
print(type(parsed))  # <class 'datetime.datetime'>
```

Das Format muss exakt übereinstimmen, sonst wird ein `ValueError` ausgelöst.

### Datumsarithmetik mit timedelta

Addieren oder subtrahieren Sie Zeitintervalle mit `timedelta`.

```python
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)  # Aktuelles Datum + 1 Tag

# Subtrahieren
yesterday = now - one_day

# Teile: Tage, Sekunden, Mikrosekunden, Millisekunden, Minuten, Stunden, Wochen
one_week = datetime.timedelta(weeks=1)
```

Für Differenzen zwischen Datumsangaben:

```python
date1 = datetime.datetime(2023, 10, 5)
date2 = datetime.datetime(2023, 10, 10)
delta = date2 - date1
print(delta.days)  # 5
```

### Zeitzonen (Erweiterte Verwendung)

Für zeitzonenbewusste Operationen verwenden Sie `timezone` (Python 3.3+). Das Modul behandelt Zeitzonenkonvertierungen nicht nativ; kombinieren Sie es für eine robuste Handhabung mit der `pytz`-Bibliothek.

```python
from datetime import datetime, timezone

# Naive datetime (keine Zeitzone)
naive = datetime.now()

# UTC-aware
utc = datetime.now(timezone.utc)

# Benutzerdefinierte Zeitzone (erfordert tzinfo)
import pytz  # Might need pip install pytz
eastern = pytz.timezone("US/Eastern")
eastern_time = naive.astimezone(eastern)
```

### Häufige Tipps und Fallstricke
- **Unveränderliche Objekte**: `datetime`-Objekte können nicht direkt modifiziert werden; Arithmetik erstellt neue.
- **Monatstage**: Verwenden Sie 29 für Februar in Schaltjahren; das Modul behandelt dies mit `calendar` oder `dateutil` für Schaltjahresprüfungen.
- **Performance**: Vermeiden Sie häufige `now()`-Aufrufe in Schleifen; speichern Sie den Wert.
- **Fehler**: Achten Sie auf ungültige Datumsangaben (z. B. löst `date(2023, 2, 30)` einen `ValueError` aus).
- **Bibliothekserweiterungen**: Für erweitertes Parsen ziehen Sie `dateutil` oder `arrow` Pakete in Betracht.

Die vollständige Dokumentation finden Sie in den offiziellen Python-Docs unter [docs.python.org](https://docs.python.org/3/library/datetime.html). Üben Sie mit diesen Beispielen in einem Python-Interpreter.