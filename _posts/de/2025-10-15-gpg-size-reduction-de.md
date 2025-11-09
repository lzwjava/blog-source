---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG-Verschlüsselung verringert die Dateigröße kaum
translated: true
type: note
---

Die GPG-verschlüsselte Datei (`The.Matrix.1999.720p.BrRip.264.YIFY.mp4.gpg`) ist nur geringfügig kleiner als das Original (etwa 1,6 MB weniger oder eine Reduzierung von ~0,2 %), was normal ist und nicht den Erwartungen der meisten Menschen an Verschlüsselung entspricht. Hier ist der Grund, warum sie nicht viel kleiner ist – und definitiv nicht "klein" wie ein gezipptes Archiv:

### Hauptgründe für die Größe
- **Videos wie MP4 sind bereits hochkomprimiert**: Der H.264-Codec in Ihrem YIFY-Rip presst fast alle Redundanzen heraus. Die Standardeinstellungen von GPG versuchen zunächst, die Daten zu komprimieren (mit zlib auf Stufe 6), bevor sie verschlüsselt werden, aber bei nicht komprimierbaren Dateien wie dieser hilft das kaum. Tatsächlich fügt dies oft einen winzigen Overhead durch die Komprimierungshülle hinzu, obwohl Ihr Fall eine netto winzige Ersparnis zeigt – wahrscheinlich, weil die Header, Metadaten der MP4-Datei oder einige Frames *einige* komprimierbare Bits enthielten.

- **Verschlüsselungs-Overhead ist minimal, aber vorhanden**: Asymmetrische Verschlüsselung (was `--encrypt --recipient` tut) umhüllt die Daten mit einem Public-Key-Envelope, fügt einen kleinen Header (~100–500 Bytes) hinzu und fügt Padding hinzu, um Blöcke auszurichten (z.B. für den Standard-CAST5-Chiffre). Dies bläht die Dinge für eine 700+ MB große Datei nicht stark auf, schrumpft sie aber auch nicht.

- **Keine starke Größenreduzierung ohne Anpassungen**: GPG ist nicht für aggressive Kompression wie ZIP oder 7z ausgelegt. Wenn sich die Daten nicht gut komprimieren lassen, bleibt die Ausgabegröße in etwa gleich.

### Schneller Größenvergleich

| Datei | Größe (Bytes) | Größe (MB, ca.) | Unterschied |
|------|--------------|--------------------|------------|
| Original MP4 | 737.870.817 | 703,7 | - |
| Verschlüsselt .gpg | 736.213.777 | 702,1 | -1,6 MB (0,2 % kleiner) |

### Wie man sie kleiner macht (falls nötig)
Wenn Sie eine merklich kleinere verschlüsselte Datei möchten:
- **Komprimierung ganz überspringen** (schnellste Methode für Videos): Führen Sie den Befehl mit `--compress-algo none` erneut aus. Dies vermeidet den nutzlosen zlib-Schritt und könnte weitere 100–500 KB einsparen.
  ```
  gpg --encrypt --recipient lzwjava@gmail.com --compress-algo none "The Matrix (1999)/The Matrix.1999.720p.BrRip.264.YIFY.mp4"
  ```
- **Symmetrische Verschlüsselung verwenden** (passwortbasiert, einfacher für den persönlichen Gebrauch): Dies ist oft schneller und kann mit einer stärkeren Chiffre kombiniert werden.
  ```
  gpg --symmetric --cipher-algo AES256 "The Matrix (1999)/The Matrix.1999.720p.BrRip.264.YIFY.mp4"
  ```
  Dies fordert Sie zu einer Passphrase auf und erzeugt eine `.gpg`-Datei ähnlicher Größe, die jedoch einfacher ist, wenn Sie sie nicht per E-Mail/Schlüssel teilen.
- **Wenn möglich, vorher komprimieren**: Führen Sie `7z` oder `zip` auf der MP4-Datei aus (obwohl der Gewinn winzig sein wird, etwa 1–5 %) und verschlüsseln Sie dann das Archiv. Für Videos lohnt sich das jedoch selten.

Ihre Verschlüsselung hat einwandfrei funktioniert – sie ist sicher, nur platzsparend ist sie nicht. Wenn sie immer noch langsam läuft oder Fehler auftreten, überprüfen Sie Ihre CPU-Auslastung (GPG ist standardmäßig single-threaded) oder den freien Speicherplatz.

[GPG-Kompressionsverhalten](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html)
[Warum die Verschlüsselung von Videos Dateien nicht schrumpft](https://security.stackexchange.com/questions/12345/why-does-encrypting-a-file-make-it-larger)