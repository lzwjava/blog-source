---
audio: false
generated: true
lang: de
layout: post
title: 'qBittorrent-Dateiverifikation: SHA-1-Hashing'
translated: true
type: note
---

Wenn Sie Dateispeicherorte in qBittorrent verschieben und es die Dateien erneut überprüft, bevor es das Seeding fortsetzt, stellt es sicher, dass die Dateien am neuen Speicherort dieselben sind, mit denen es ursprünglich gearbeitet hat. Diese Verifizierung ist beim Torrenting entscheidend, um das Teilen falscher oder beschädigter Daten zu verhindern. So funktioniert der Prozess und welchen Algorithmus er verwendet:

### Wie qBittorrent Dateien verifiziert
qBittorrent vertraut nicht einfach darauf, dass die verschobenen Dateien korrekt sind – es überprüft ihre Integrität, indem es sie mit den in der Torrent-Datei gespeicherten Informationen vergleicht. Beim Torrenting werden Daten in kleinere Teile, sogenannte **Pieces**, aufgeteilt, und jedes Piece hat einen eindeutigen Hash-Wert. Diese Hashes sind in der Torrent-Datei enthalten und dienen als Fingerabdruck für jedes Datenstück. Wenn Sie Dateien an einen neuen Speicherort verschieben, verwendet qBittorrent diese Piece-Hashes, um zu bestätigen, dass sich die Dateien nicht verändert haben.

Der Prozess lässt sich in folgende Schritte unterteilen:

1. **Neuen Speicherort angeben**: Sie teilen qBittorrent mit, wo sich die Dateien jetzt befinden, indem Sie den neuen Dateipfad festlegen.
2. **Dateien dem Torrent zuordnen**: qBittorrent ordnet die Dateien am neuen Speicherort den in der Torrent-Datei aufgeführten Dateien zu, typischerweise anhand von Dateinamen und -größen (da diese Informationen in der Torrent-Datei enthalten sind).
3. **Piece-Hashes überprüfen**: qBittorrent liest die Daten aus den neuen Dateien Stück für Stück, berechnet einen Hash für jedes Piece und vergleicht ihn mit dem entsprechenden, in der Torrent-Datei gespeicherten Hash.
4. **Integrität bestätigen**: Wenn alle berechneten Hashes mit den Hashes der Torrent-Datei übereinstimmen, wird bestätigt, dass die Dateien identisch sind, und qBittorrent kann das Seeding fortsetzen. Wenn der Hash eines Pieces nicht übereinstimmt, wird dieses Piece als unvollständig oder fehlend markiert, und qBittorrent muss es möglicherweise erneut herunterladen.

### Welchen Algorithmus verwendet es?
qBittorrent verwendet keine vollständige Dateiprüfsumme (wie MD5 oder SHA-256 für die gesamte Datei), da dies langsam und ineffizient wäre, insbesondere für große Dateien. Stattdessen verlässt es sich auf die **Piece-Hashes**, die durch das BitTorrent-Protokoll definiert sind. Der für diese Piece-Hashes verwendete Algorithmus ist **SHA-1**, eine weit verbreitete kryptografische Hash-Funktion. Jedes Datenstück (das je nach Torrent einige Kilobyte bis einige Megabyte groß sein kann) wird mit SHA-1 gehasht, und diese Hashes sind es, die qBittorrent überprüft.

Die Verwendung von Piece-Hashes anstelle einer vollständigen Dateiprüfsumme hat zwei große Vorteile:
- **Effizienz**: Das Überprüfen kleinerer Teile ist schneller als das Hashen einer gesamten Datei.
- **Granularität**: Wenn etwas nicht stimmt, kann qBittorrent genau eingrenzen, welche Pieces repariert werden müssen, anstatt die gesamte Datei abzulehnen.

### Warum das wichtig ist
Diese hash-basierte Verifizierung stellt sicher, dass die Daten, die Sie vom neuen Speicherort aus seeden, dem entsprechen, was andere Peers erwarten, und erhält so die Integrität des Torrent Schwarms. Ohne diese Überprüfung könnte das Verschieben von Dateien zum Teilen beschädigter oder nicht übereinstimmender Daten führen, was den Torrenting-Prozess stören würde.

Kurz gesagt: Wenn Sie Dateispeicherorte in qBittorrent verschieben, überprüft es die Dateien erneut, indem es **SHA-1-Hashes** für jedes Piece berechnet und sie mit den Hashes in der Torrent-Datei vergleicht. So stellt es sicher, dass alles korrekt ist, bevor das Seeding fortgesetzt wird.

---

Um zu demonstrieren, wie qBittorrent die Dateiintegrität mithilfe von Piece-Hashes (speziell SHA-1-Hashes) beim Verschieben von Dateispeicherorten überprüft, folgt hier ein einfaches Python-Skript. qBittorrent, das dem BitTorrent-Protokoll folgt, teilt Dateien in Pieces auf, berechnet SHA-1-Hashes für jedes Piece und verwendet diese Hashes, um sicherzustellen, dass der Dateiinhalt unverändert bleibt, unabhängig vom Speicherort. Dieses Skript simuliert diesen Prozess, indem es eine Beispieldatei erstellt, ihre Piece-Hashes berechnet, eine identische Kopie verifiziert und dann zeigt, wie eine Modifikation zu einem Fehlschlagen der Verifizierung führt.

### Erklärung
- **Piece-Hashes**: Das Skript teilt eine Datei in Pieces fester Größe (z.B. 10 Bytes) auf und berechnet SHA-1-Hashes für jedes Piece, ähnlich wie eine Torrent-Datei diese Hashes speichert.
- **Verifizierung**: Es prüft, ob die berechneten Hashes einer Datei mit den erwarteten Hashes übereinstimmen, um so die Integrität sicherzustellen.
- **Simulation**: Es erstellt eine Datei, kopiert sie (simuliert einen Umzug), verifiziert sie, modifiziert dann die Kopie und verifiziert sie erneut, um zu zeigen, wie Änderungen erkannt werden.

Hier ist das Skript mit Kommentaren zur Verdeutlichung:

```python
import hashlib
import shutil
import os

def compute_piece_hashes(file_path, piece_size):
    """Berechne SHA-1-Hashes für jedes Piece der Datei."""
    hashes = []
    with open(file_path, 'rb') as f:
        while True:
            piece = f.read(piece_size)
            if not piece:
                break
            hash_obj = hashlib.sha1(piece)
            hashes.append(hash_obj.hexdigest())
    return hashes

def verify_file_integrity(file_path, piece_size, expected_hashes):
    """Verifiziere die Integrität der Datei durch Vergleich der Piece-Hashes."""
    current_hashes = compute_piece_hashes(file_path, piece_size)
    if len(current_hashes) != len(expected_hashes):
        return False
    for current, expected in zip(current_hashes, expected_hashes):
        if current != expected:
            return False
    return True

# Erstelle eine Beispieldatei mit bekanntem Inhalt
with open('file1.txt', 'w') as f:
    f.write("Hello, this is a test file.")

piece_size = 10  # Bytes, klein für die Demonstration

# Berechne die erwarteten Hashes von file1.txt (simuliert Torrent-Hashes)
expected_hashes = compute_piece_hashes('file1.txt', piece_size)
print("Erwartete Hashes:", [h[:8] for h in expected_hashes])  # Zeige die ersten 8 Zeichen zur besseren Lesbarkeit

# Kopiere file1.txt zu file2.txt, um das Verschieben der Datei zu simulieren
shutil.copyfile('file1.txt', 'file2.txt')

# Verifiziere file2.txt mit den erwarteten Hashes (sollte bestehen)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verifizierung von file2.txt (unverändert):", "Gültig" if is_valid else "Ungültig")

# Modifiziere file2.txt, um eine Beschädigung oder Änderung zu simulieren
with open('file2.txt', 'a') as f:
    f.write(" Modified")

# Verifiziere erneut (sollte fehlschlagen aufgrund des geänderten Inhalts)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verifizierung von file2.txt (modifiziert):", "Gültig" if is_valid else "Ungültig")

# Räume die erstellten Dateien auf
os.remove('file1.txt')
os.remove('file2.txt')
```

### Wie es funktioniert
1. **Dateierstellung**: Schreibt "Hello, this is a test file." (25 Bytes) in `file1.txt`.
2. **Hash-Berechnung**: Teilt `file1.txt` in Pieces von je 10 Bytes auf (z.B. "Hello, thi", "s is a tes", "t file."), berechnet die SHA-1-Hashes und speichert sie als `expected_hashes`.
3. **Simuliere Umzug**: Kopiert `file1.txt` zu `file2.txt`, was einen Dateiumzug an einen neuen Speicherort darstellt.
4. **Erste Verifizierung**: Prüft `file2.txt` gegen `expected_hashes`. Da der Inhalt identisch ist, wird "Gültig" ausgegeben.
5. **Modifikation**: Hängt " Modified" an `file2.txt` an, verändert so deren Inhalt und Größe (jetzt 34 Bytes, aufgeteilt in 4 Pieces).
6. **Zweite Verifizierung**: Prüft die modifizierte `file2.txt`. Die Anzahl der Pieces oder deren Hashes unterscheidet sich, daher wird "Ungültig" ausgegeben.
7. **Aufräumen**: Löscht die temporären Dateien.

### Beispielhafte Ausgabe
```
Erwartete Hashes: ['dffd6021', 'a2b3c4d5', 'e6f789ab']  # Beispielhafte Hash-Präfixe
Verifizierung von file2.txt (unverändert): Gültig
Verifizierung von file2.txt (modifiziert): Ungültig
```
(Die tatsächlichen Hash-Werte variieren, folgen aber diesem Muster.)

Dieses Skript veranschaulicht, wie qBittorrent die Dateiintegrität durch den Vergleich von Piece-Hashes sicherstellt und dabei jegliche Änderungen erkennt, selbst nachdem eine Datei verschoben wurde. Es ist eine einfache, aber effektive Demonstration des Prozesses.