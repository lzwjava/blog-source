---
audio: false
generated: true
lang: de
layout: post
title: Linux-Systeminformationen
translated: true
type: note
---

In Ubuntu können Sie Systeminformationen wie die Systemarchitektur (32-Bit oder 64-Bit), die Betriebssystemversion, die Größe des Arbeitsspeichers (RAM) und die Festplattengröße mit den folgenden Befehlen abrufen. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung:

### 1. Bestimmen, ob das System 32-Bit oder 64-Bit ist
- **Befehl**: `uname -m`
- **Erklärung**: Dieser Befehl zeigt den Namen der Maschinenhardware an.
  - Wenn die Ausgabe `x86_64` lautet, ist Ihr System **64-Bit**.
  - Wenn die Ausgabe `i686` oder `i386` lautet, ist Ihr System **32-Bit**.
- **Beispielausgabe**:
  ```
  x86_64
  ```
  Dies weist auf ein 64-Bit-System hin.

### 2. Betriebssystemversion (OS-Version) abrufen
- **Befehl**: `lsb_release -a`
- **Erklärung**: Dieser Befehl liefert detaillierte Informationen über die Linux Standard Base (LSB) und die Distribution.
  - Suchen Sie nach der Zeile `Description`, um die Ubuntu-Version zu sehen.
- **Beispielausgabe**:
  ```
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description:    Ubuntu 20.04.3 LTS
  Release:        20.04
  Codename:       focal
  ```
  Hier ist das Betriebssystem **Ubuntu 20.04.3 LTS**.

### 3. Größe des Arbeitsspeichers (RAM) abrufen
- **Befehl**: `free -h`
- **Erklärung**: Dieser Befehl zeigt die Speichernutzung in einem menschenlesbaren Format an (z. B. GB oder MB).
  - Sehen Sie sich die Spalte `total` in der Zeile `Mem:` an, um den gesamten installierten Arbeitsspeicher zu finden.
- **Beispielausgabe**:
  ```
              total        used        free      shared  buff/cache   available
  Mem:          15Gi       2.3Gi       9.5Gi       300Mi       3.8Gi        12Gi
  Swap:        2.0Gi         0B       2.0Gi
  ```
  In diesem Fall beträgt der gesamte Arbeitsspeicher **15 GB**.

### 4. Festplattengröße abrufen
- **Befehl**: `lsblk -d -o NAME,SIZE`
- **Erklärung**: Dieser Befehl listet alle Festplattenlaufwerke (ohne Partitionen) mit ihren Größen auf.
  - Das Flag `-d` stellt sicher, dass nur Festplattenlaufwerke (z. B. `/dev/sda`) und nicht deren Partitionen angezeigt werden.
  - Suchen Sie nach dem Festplattennamen (z. B. `sda`) und der entsprechenden Größe.
- **Beispielausgabe**:
  ```
  NAME   SIZE
  sda    1T
  sdb    500G
  ```
  Hier hat das System zwei Festplatten: `/dev/sda` mit einer Größe von **1 Terabyte** und `/dev/sdb` mit **500 Gigabyte**. Wenn Sie nur eine Festplatte haben, wird diese typischerweise als `sda` aufgeführt.

### Hinweise
- Diese Befehle verwenden Standard-Tools, die in Ubuntu verfügbar sind und keine zusätzlichen Installationen erfordern.
- Für die Festplattengröße: Wenn Ihr System mehrere Festplatten hat, werden alle in der Ausgabe aufgelistet. Typischerweise ist `/dev/sda` die primäre Festplatte.
- Führen Sie diese Befehle in einem Terminal aus, um die für Ihr System spezifischen Ergebnisse zu sehen.

Mit diesen Befehlen können Sie schnell die wesentlichen Systeminformationen sammeln, die Sie auf Ihrer Ubuntu-Maschine benötigen!