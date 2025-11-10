---
audio: false
generated: true
image: false
lang: de
layout: post
title: Aufschlüsselung der mehrsprachigen Windows-Architektur
translated: true
type: note
---

Windows 10 Enterprise wird nicht nur in einer Sprache erstellt – es ist ein großes Betriebssystem mit vielen Komponenten, die jeweils in verschiedenen Programmiersprachen geschrieben sind, die für ihre Stärken ausgewählt wurden. Hier die Aufschlüsselung:

**Kernsystem und Kernel**

* Hauptsächlich in **C** und **C++** geschrieben.
* Leistungskritische Teile (wie der Windows NT-Kernel, Speichermanager, E/A-System) sind meistens C, mit etwas Assembly für sehr low-level Operationen.

**Systemdienste und APIs**

* **C und C++** dominieren auch hier (z.B. Win32 API, DirectX, Systembibliotheken).
* Einige Teile des .NET Framework und neuerer APIs sind in **C#**.

**Benutzeroberfläche (Shell, Explorer, etc.)**

* Historisch **C++ mit COM (Component Object Model)**.
* Moderne Schnittstellenschichten, wie Teile der UWP-Apps (Universal Windows Platform) und Einstellungen von Windows 10, sind in **C#, XAML und JavaScript** geschrieben.
* Fluent Design und XAML-UI-Elemente werden im Kern von C++ angetrieben, sind aber über höhere Programmiersprachen zugänglich.

**Verwaltung, Skripterstellung und Automatisierung**

* **PowerShell** (basiert auf .NET und größtenteils in **C#** geschrieben).
* Viele Systemdienstprogramme bieten ebenfalls Skriptschnittstellen.

**Sicherheit und Treiber**

* Kernel-Mode-Treiber: meistens **C**, etwas **C++** und Assembly.
* User-Mode-Treiber: oft **C++**, manchmal **C#** für höhere Tools.

Zusammenfassend lässt sich also sagen:

* **C und C++** sind die Grundlage.
* **C# und .NET-Sprachen** werden häufig in Verwaltungstools und Apps verwendet.
* **Assembly** ist nach wie vor für low-level Boot- und leistungskritische Routinen vorhanden.
* **XAML/JavaScript** für Teile des modernen UI-Stacks.

👉 Möchten Sie, dass ich eine **geschichtete Karte** von Windows 10 Enterprise (Kernel, Treiber, Systemdienste, UI, Verwaltungstools) erstelle, die zeigt, welche Sprachen in welcher Schicht dominieren? Das könnte das Bild klarer machen.