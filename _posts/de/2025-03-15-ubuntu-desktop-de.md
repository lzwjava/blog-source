---
audio: false
generated: true
lang: de
layout: post
title: Installation einer Desktop-Umgebung auf Ubuntu
translated: true
type: note
---

Es klingt so, als ob auf Ihrem Ubuntu-System möglicherweise keine grafische Benutzeroberfläche (GUI) installiert ist, was erklären würde, warum Sie keinen Dateibrowser (oft Dateimanager unter Linux genannt) oder eine Art "Finder" sehen. Dies könnte passiert sein, wenn Sie eine Server-Version von Ubuntu installiert, eine Minimal-Installation gewählt haben oder ein Problem das Laden der GUI verhindert. Keine Sorge – wir können das beheben, indem wir eine GUI wie GNOME (Ubuntus Standard-Desktop-Umgebung) oder eine andere Option installieren, wenn Sie bevorzugen. Hier ist eine Schritt-für-Schritt-Anleitung.

### Schritt 1: Aktualisieren Sie Ihr System
Bevor Sie etwas installieren, ist es eine gute Idee, sicherzustellen, dass Ihre Paketlisten auf dem neuesten Stand sind und Ihr System vollständig aktualisiert ist. Öffnen Sie ein Terminal und führen Sie diese Befehle aus:

```bash
sudo apt update
```
Dies aktualisiert die Liste der verfügbaren Pakete.

```bash
sudo apt upgrade
```
Dies aktualisiert alle derzeit installierten Pakete auf ihre neuesten Versionen. Drücken Sie, falls dazu aufgefordert, `Y` zur Bestätigung.

### Schritt 2: Installieren Sie die GNOME-Desktop-Umgebung
Da Sie eine GUI "wie GNOME oder andere" erwähnt haben, beginnen wir mit GNOME, da es der Standard für Ubuntu Desktop ist und einen Dateimanager namens Nautilus enthält. Führen Sie zur Installation aus:

```bash
sudo apt install ubuntu-desktop
```
Dieser Befehl installiert die vollständige GNOME-Desktop-Umgebung zusammen mit Standardanwendungen wie einem Dateimanager, Webbrowser und mehr. Die Installation kann einige Minuten dauern, abhängig von Ihrer Internetgeschwindigkeit und Ihrem System. Wenn Sie aufgefordert werden, einen Display-Manager (z.B. GDM oder LightDM) auszuwählen, können Sie in der Regel die Standardoption (GDM für GNOME) durch Drücken der Eingabetaste beibehalten.

### Schritt 3: Starten Sie Ihr System neu
Starten Sie Ihr System nach Abschluss der Installation neu, um die GUI zu starten:

```bash
sudo reboot
```
Sobald Ihr System neu gestartet ist, sollten Sie einen grafischen Anmeldebildschirm sehen. Melden Sie sich an, und Sie haben einen voll funktionsfähigen Desktop mit einem Dateimanager (Nautilus), mit dem Sie Dateien durchsuchen können.

### Was tun, wenn es nicht funktioniert?
Wenn Sie nach dem Neustart immer noch keine GUI sehen, könnte ein Problem mit dem Display-Manager oder den Grafiktreibern vorliegen. Sie können versuchen, den Display-Manager manuell zu starten, um dies zu testen:

```bash
sudo systemctl start gdm
```
Wenn dies einen Anmeldebildschirm anzeigt, perfekt! Um sicherzustellen, dass er bei jedem