---
audio: false
generated: true
lang: de
layout: post
title: Mozilla-Lesezeichendatei parsen
translated: true
type: note
---

Die Datei, die Sie betrachten, ist eine **Firefox-Lesezeichen-Sicherung** im `.jsonlz4`-Format. Das bedeutet, es handelt sich um eine **JSON-Datei, die mit dem LZ4-Kompressionsalgorithmus komprimiert** wurde und Ihre Firefox-Lesezeichen enthält.

### 📁 Dateiname:
```
bookmarks-2025-06-21_10_MU9VVxxx.jsonlz4
```

Dies ist ein Standard-Namensmuster für Firefox-Lesezeichen-Sicherungen.

---

## ✅ Ziel: Wie man sie analysiert

Sie können diese Datei nicht direkt lesen, da sie **mit LZ4 komprimiert** ist. Sie müssen:

1. Sie **dekomprimieren** (LZ4 → JSON)
2. Das resultierende JSON **formatieren** oder parsen

---

## 🔧 Schritt-für-Schritt-Anleitung

### Option 1: Python verwenden (Empfohlen)

Installieren Sie die Abhängigkeiten:

```bash
pip install lz4
```

Führen Sie dann dieses Python-Skript aus:

```python
import json
import lz4.block
import sys

def decompress_jsonlz4(file_path):
    with open(file_path, 'rb') as f:
        # Erste 8 Bytes lesen - Header Magic
        magic = f.read(8)
        if magic != b'mozLz40\0':
            raise ValueError("Ungültiger Dateiheader - keine JSON-LZ4-Datei")

        # Rest der Datei lesen und dekomprimieren
        compressed_data = f.read()
        json_bytes = lz4.block.decompress(compressed_data)
        json_str = json_bytes.decode('utf-8')
        return json.loads(json_str)

# Beispielverwendung
if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    data = decompress_jsonlz4(file_path)
    print(json.dumps(data, indent=4))
```

Speichern Sie es als `parse_bookmarks.py`, dann führen Sie aus:

```bash
python parse_bookmarks.py 'bookmarks-2025-06-21_10_MU9VV5NmyUCq9RTxuMze5iBNh7sKyRPF_ZlV5EpMqZo=.jsonlz4'
```

> 🔍 Die Ausgabe wird ein schön formatierter JSON-Baum Ihrer Lesezeichen sein.

---

### Option 2: Ein Online-Tool verwenden (Schnell, aber riskant bei sensiblen Daten)

Es gibt Tools wie:

- [https://arewecompressedyet.com/jsonlz4/](https://arewecompressedyet.com/jsonlz4/)
- Oder suchen Sie nach "jsonlz4 decoder"

⚠️ **Warnung:** Laden Sie keine sensiblen Dateien in Online-Tools hoch, es sei denn, Sie sind sicher, dass diese sicher und vertrauenswürdig sind.

---

### Option 3: Node.js verwenden

Wenn Sie JavaScript/Node bevorzugen:

```bash
npm install firefox-jsonlz4
```

Oder sehen Sie sich dieses Repo an: https://github.com/overdodactyl/firefox-jsonlz4

---

## 📊 Was ist drin?

Sobald geparst, erhalten Sie eine JSON-Struktur wie diese:

```json
{
  "title": "Bookmarks Menu",
  "children": [
    {
      "title": "Mozilla Firefox",
      "children": [
        {
          "title": "Get Help",
          "uri": "https://support.mozilla.org/products/firefox/"
        },
        ...
      ]
    }
  ]
}
```

Sie können diese Daten nutzen, um:
- Alte Lesezeichen zu durchsuchen
- Lesezeichen zu migrieren
- Ihre Surf-/Lesezeichengewohnheiten zu analysieren

---

## ✅ Zusammenfassung

| Schritt | Aktion |
|------|--------|
| 1 | Erkennen, dass `.jsonlz4` eine **komprimierte JSON-Datei** ist |
| 2 | Python oder andere Tools verwenden, um sie **zu dekomprimieren und zu parsen** |
| 3 | Die strukturierte JSON-Darstellung Ihrer Firefox-Lesezeichen ansehen/exportieren |

Lassen Sie mich wissen, wenn Sie dies in CSV, HTML konvertieren oder bestimmte URLs extrahieren möchten!

---

Gute Frage! Lassen Sie uns aufschlüsseln, **warum Mozilla das `.jsonlz4`-Format** für Lesezeichen verwendet anstatt von Plain JSON, und Ihre Bedenken bezüglich **Sicherheit** ansprechen.

---

## 🔍 Warum Mozilla `.jsonlz4` anstatt Plain JSON verwendet

### ✅ 1. **Kompressionseffizienz**
- `.jsonlz4` sind **JSON-Daten, die mit dem LZ4-Algorithmus komprimiert** wurden.
- LZ4 ist **schnell**, **leichtgewichtig** und bietet gute Kompressionsraten – ideal für den Anwendungsfall von Firefox.
- Dies reduziert die Dateigröße erheblich (oft um **50–70%**), was:
  - Speicherplatz spart
  - Sicherungen und Wiederherstellungen beschleunigt
  - I/O beim Lesen/Schreiben von Lesezeichendateien reduziert

> 📦 Beispiel: Eine 2MB große Plain-JSON-Lesezeichendatei kann sich mit LZ4 auf ~600KB–800KB komprimieren.

---

### ✅ 2. **Performance**
- LZ4 ist für **Geschwindigkeit über maximale Kompression** optimiert.
- Firefox kann diese Dateien schnell komprimieren und dekomprimieren, ohne spürbare Verzögerung.
- Andere Algorithmen wie gzip oder zstd sind leistungsfähiger, aber langsamer oder komplexer.

---

### ✅ 3. **Internes Format**
- Firefox stellt dies nicht als benutzerorientiertes Format bereit; es wird intern verwendet für:
  - Lesezeichen-Sicherungen (`bookmarkbackups/`)
  - Sitzungswiederherstellung (`sessionstore-backups/`)
- Es ist nicht für die Bearbeitung durch Benutzer oder Interoperabilität gedacht (wie der Export für den Chrome-Import).

> Für Export/Import bietet Firefox **Plain JSON** über das "Importieren und Sichern"-Menü.

---

## 🔒 Ist `.jsonlz4` weniger sicher als JSON?

Nein, **nicht von Natur aus**.

Lassen Sie uns das klären:

| Aspekt | JSON | JSONLZ4 |
|-------|------|---------|
| **Datenformat** | Lesbarer Text | Binär-komprimiert |
| **Sicherheit** | Keine eingebaute | Keine eingebaute |
| **Verschlüsselung?** | Nein | Nein |
| **Manipulationsschutz?** | Nein | Nein |

Beide Formate sind standardmäßig **unverschlüsselt** und **ungeschützt**.

Also:
- Wenn jemand Zugriff auf Ihr Firefox-Profil hat, kann er beide Dateien lesen.
- Keines der Formate schützt sensible Daten wie URLs oder Titel.

---

## 💡 Warum also nicht verschlüsselte oder sichere Formate verwenden?

Mozilla **verschlüsselt lokale Profildaten standardmäßig nicht**, einschließlich:
- Lesezeichen
- Verlauf
- Cookies
- Passwörter

### Hier ist der Grund:
- **Benutzererfahrung**: Verschlüsselung fügt Komplexität hinzu.
- **Wiederherstellung**: Benutzer könnten Daten verlieren, wenn sie Passwörter vergessen.
- **Vertrauensannahme**: Firefox geht davon aus, dass Ihr System sicher ist.
- **Alternative Tools existieren**: Sie können Ihren Firefox-Profilordner manuell mit Betriebssystem-Tools verschlüsseln (z.B. VeraCrypt, BitLocker, etc.).

Wenn Sie verschlüsselte Profile möchten:
- Verwenden Sie **Firefox Lockwise** für die Passwortverschlüsselung.
- Verwenden Sie **Drittanbieter-Tools**, um den gesamten Profilordner zu verschlüsseln.
- Oder wechseln Sie zu einem portablen Firefox auf einem verschlüsselten USB-Laufwerk.

---

## 🧠 Bonus-Tipp: Wie man `.jsonlz4` → `.json` konvertiert

Sie wissen bereits wie aus der vorherigen Antwort, aber hier ist eine kurze Zusammenfassung mit Python:

```bash
python parse_bookmarks.py bookmarks-*.jsonlz4 > bookmarks.json
```

Oder verwenden Sie diese Einzeiler, wenn Sie sich mit Shell + Python auskennen:

```bash
cat bookmarks-*.jsonlz4 | python3 -c '
import lz4.block, sys, json
data = sys.stdin.buffer.read()[8:]
print(json.dumps(json.loads(lz4.block.decompress(data)), indent=2))' > bookmarks.json
```

---

## ✅ Zusammenfassung

| Frage | Antwort |
|--------|--------|
| **Warum `.jsonlz4` anstatt JSON?** | Kompression, Performance, interne Verwendung |
| **Ist `.jsonlz4` weniger sicher als JSON?** | Nein – beide sind unverschlüsselt und lesbar |
| **Kann jemand meine Lesezeichen stehlen?** | Ja, wenn er Zugriff auf Ihren Rechner hat |
| **Wie kann man es sicherer machen?** | Verschlüsseln Sie Ihren Firefox-Profilordner manuell |

---

Wenn Sie Bedenken bezüglich Privatsphäre oder Sicherheit haben, ist die eigentliche Lösung, **den Zugriff auf Ihren Computer zu schützen** oder **Ihren Firefox-Profilordner zu verschlüsseln**, und sich nicht nur auf Dateiformate zu verlassen.

Lassen Sie mich wissen, wenn Sie Hilfe bei der Erstellung eines Skripts zur Automatisierung der Entschlüsselung oder Verschlüsselung von Sicherungen benötigen!