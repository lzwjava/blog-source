---
audio: false
generated: false
image: false
lang: de
layout: post
title: Einrichten eines Google Cloud Servers
translated: true
---

Das Einrichten eines Proxy-Servers in Google Cloud ermöglicht es Ihnen, Ihren Internetverkehr sicher über eine Cloud-Instanz zu leiten, was die Privatsphäre erhöht und Einschränkungen umgeht. In dieser Anleitung führen wir Sie durch den Prozess der Einrichtung eines grundlegenden Proxy-Servers in Google Cloud und der Konfiguration der erforderlichen Firewall-Regeln, um den Datenverkehr zu ermöglichen.

## Inhaltsverzeichnis
1. [Erstellen einer Google Cloud VM-Instanz](#creating-a-google-cloud-vm-instance)
2. [Konfigurieren des Proxy-Servers](#configuring-the-proxy-server)
3. [Einrichten von Firewall-Regeln](#setting-up-firewall-rules)
4. [Testen des Proxy-Servers](#testing-the-proxy-server)
5. [Fazit](#conclusion)

---

## Erstellen einer Google Cloud VM-Instanz

Bevor Sie den Proxy-Server einrichten, müssen Sie eine virtuelle Maschine (VM) in Google Cloud erstellen.

1. Melden Sie sich bei der Google Cloud Console an: Gehen Sie zur [Google Cloud Console](https://console.cloud.google.com/) und melden Sie sich bei Ihrem Konto an.
   
2. Erstellen Sie eine neue VM-Instanz:
   - Navigieren Sie zu Compute Engine > VM-Instanzen.
   - Klicken Sie auf Instanz erstellen.
   - Wählen Sie die gewünschte Region und den Maschinentyp. Zur Vereinfachung können Sie die Standardeinstellungen verwenden oder eine leichte Konfiguration wie die `e2-micro`-Instanz wählen.
   - Wählen Sie im Abschnitt Firewall sowohl HTTP-Datenverkehr zulassen als auch HTTPS-Datenverkehr zulassen aus, um den Webzugriff zu ermöglichen.
   
3. Richten Sie den SSH-Zugriff ein:
   - Fügen Sie im Abschnitt SSH-Schlüssel Ihren öffentlichen SSH-Schlüssel hinzu, um auf die Instanz remote zugreifen zu können. Dies ist entscheidend für die spätere Konfiguration Ihres Proxy-Servers.
   
4. Klicken Sie auf Erstellen, um Ihre VM zu starten.

Nachdem die VM eingerichtet ist, können Sie sich über SSH entweder über die Google Cloud Console oder über das Terminal mit folgendem Befehl verbinden:

```bash
gcloud compute ssh <dein-vm-name>
```

---

## Konfiguration des Proxy-Servers

Sobald Ihre VM eingerichtet ist, können Sie einen Proxy-Server Ihrer Wahl konfigurieren. Die Proxy-Software sollte installiert und so konfiguriert werden, dass sie Verbindungen auf dem gewünschten Port (z. B. `3128` für gängige Proxy-Einrichtungen) akzeptiert. Stellen Sie sicher, dass die Software Verbindungen von entfernten Clients zulässt.

---

## Einrichten von Firewall-Regeln

Um den Datenverkehr zu Ihrem Proxy-Server zu ermöglichen, müssen Sie die Google Cloud Firewall-Regeln konfigurieren, um den erforderlichen Port zu öffnen.

1. Navigieren Sie zu Firewall-Regeln in der Google Cloud Console:
   - Gehen Sie zu VPC-Netzwerk > Firewall-Regeln in der Google Cloud Console.

2. Erstellen Sie eine neue Firewall-Regel:
   - Klicken Sie auf „Firewall-Regel erstellen“.
   - Geben Sie einen Namen für die Regel ein, z. B. `allow-proxy-access`.
   - Setzen Sie die Richtung des Datenverkehrs auf „Eingehend“ (eingehender Datenverkehr).
   - Setzen Sie die Aktion bei Übereinstimmung auf „Zulassen“.
   - Setzen Sie die Ziele auf „Alle Instanzen im Netzwerk“ oder „Spezifische Ziel-Tags“ (wenn Sie mehr Kontrolle bevorzugen).
   - Unter „Quell-IP-Bereiche“ können Sie `0.0.0.0/0` eingeben, um den Zugriff von allen IP-Adressen zu erlauben, oder ihn auf bestimmte IPs oder Bereiche beschränken, um die Sicherheit zu erhöhen.
   - Wählen Sie unter „Protokolle und Ports“ die Option „Spezifizierte Protokolle und Ports“ aus und geben Sie den von Ihrem Proxy-Server verwendeten Port ein (z. B. `tcp:3128`).

3. Speichern Sie die Firewall-Regel:
   Nachdem Sie die Regel konfiguriert haben, klicken Sie auf Erstellen, um die Firewall zu aktivieren.

---

## Testen des Proxy-Servers

Nachdem Sie die Firewall konfiguriert haben, ist es an der Zeit, Ihren Proxy-Server zu testen.

1. Proxy von Ihrem lokalen Rechner testen:

Sie können die Browser- oder System-Proxy-Einstellungen Ihres lokalen Computers so konfigurieren, dass sie die externe IP-Adresse Ihrer Google Cloud VM und den Port verwenden, den Ihr Proxy-Server überwacht (z. B. `3128`).

2. Testen mit der Befehlszeile:

   Sie können den Proxy auch mit `curl` testen, indem Sie die Proxy-Umgebungsvariablen setzen:

```bash
export http_proxy=http://<deine-vm-externe-ip>:3128
export https_proxy=http://<deine-vm-externe-ip>:3128
curl -I http://example.com
```

Wenn die Verbindung erfolgreich ist, sollten Sie eine Antwort von der Website erhalten.

---

## Fazit

Indem Sie dieser Anleitung gefolgt sind, haben Sie gelernt, wie man einen Proxy-Server auf Google Cloud einrichtet und Firewall-Regeln konfiguriert, um eingehenden Datenverkehr zuzulassen. Dieses Setup bietet eine einfache Möglichkeit, Ihren Internetverkehr sicher durch die Cloud zu leiten, Netzwerkbeschränkungen zu umgehen und die Privatsphäre zu verbessern.