---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration von Ubuntu-Proxy-Bypass-Hosts
translated: true
type: note
---

### Mehrere Hosts in den manuellen Proxy-Einstellungen von Ubuntu festlegen

In der manuellen Proxy-Konfiguration von Ubuntu (zu finden unter **Einstellungen > Netzwerk > Netzwerk-Proxy > Manuell**) erlaubt das Feld „Hosts ignorieren“ die Angabe einer durch Semikolons getrennten Liste von Hosts, Domänen oder IP-Bereichen, die den Proxy umgehen sollen. Dies wird häufig für lokalen Datenverkehr wie Localhost oder interne Netzwerke verwendet. Diese können nicht als *Proxy-Server*-Adresse festgelegt werden (welche einen einzelnen Host:Port erwartet), passen aber perfekt in „Hosts ignorieren“.

#### Schritte zur Konfiguration über die GUI:
1. Öffnen Sie **Einstellungen** (suchen Sie danach in der Aktivitätenübersicht).
2. Gehen Sie zu **Netzwerk** > **Netzwerk-Proxy**.
3. Setzen Sie die Methode auf **Manuell**.
4. Tragen Sie im Feld **Hosts ignorieren** Ihre Liste, getrennt durch Semikolons (ohne Leerzeichen um sie herum), ein:
   ```
   localhost;127.0.0.1;192.168.1.1;192.168.2.1;::1
   ```
   - `localhost`: Wird zu Loopback-Adressen aufgelöst.
   - `127.0.0.1`: IPv4 Loopback.
   - `192.168.1.1` und `192.168.2.1`: Spezifische lokale IPs (fügen Sie so viele hinzu, wie benötigt).
   - `::1`: IPv6 Loopback.

5. Klicken Sie auf **Übernehmen**, um zu speichern. Dies gilt systemweit (betrifft Apps wie Browser, apt, etc.).

#### Verwendung von Wildcards wie `192.168.1.*`:
- Direkte Wildcards (z.B. `192.168.1.*`) werden im Feld „Hosts ignorieren“ **nicht unterstützt** – es ist für exakte Hosts, Domänensuffixe (z.B. `*.local`) oder CIDR-Notation für IP-Bereiche konzipiert.
- Verwenden Sie stattdessen **CIDR-Notation** für Bereiche:
  - Für `192.168.1.*` (alle IPs im 192.168.1.0/24-Subnetz) verwenden Sie `192.168.1.0/24`.
  - Beispiel einer aktualisierten Liste:
    ```
    localhost;127.0.0.1;::1;192.168.1.0/24;192.168.2.1
    ```
  - Für breitere lokale Netzwerke fügen Sie `10.0.0.0/8;172.16.0.0/12;192.168.0.0/16` hinzu (gängige private Bereiche).

#### Befehlszeilen-Alternative (für Skripte oder Präzision):
Wenn Sie das Terminal bevorzugen (oder automatisieren müssen), verwenden Sie `gsettings` (modernes Ubuntu) oder bearbeiten Sie `/etc/environment` für systemweite Gültigkeit:
- Aktuelle Ignore-Liste anzeigen:
  ```
  gsettings get org.gnome.system.proxy ignore-hosts
  ```
- Liste setzen (ersetzen Sie sie mit Ihren Werten):
  ```
  gsettings set org.gnome.system.proxy ignore-hosts "['localhost', '127.0.0.1', '::1', '192.168.1.0/24', '192.168.2.1']"
  ```
- Für permanente Umgebungsvariable (betrifft einige Apps): Fügen Sie zu `/etc/environment` hinzu:
  ```
  no_proxy="localhost,127.0.0.1,::1,192.168.1.0/24,192.168.2.1"
  ```
  Starten Sie dann neu oder führen Sie `source /etc/environment` aus.

Testen Sie, indem Sie einen gelisteten Host anpingen oder das Proxy-Verhalten in einem Browser prüfen. Falls Probleme auftreten (z.B. mit bestimmten Apps), deckt die Methode mit der Umgebungsvariablen oft mehr ab.

[Setting up proxy to ignore all local addresses](https://askubuntu.com/questions/11274/setting-up-proxy-to-ignore-all-local-addresses)  
[How to Configure Proxy Settings on Ubuntu](https://phoenixnap.com/kb/ubuntu-proxy-settings)  
[Set a network range in the no_proxy environment variable](https://unix.stackexchange.com/questions/23452/set-a-network-range-in-the-no-proxy-environment-variable)