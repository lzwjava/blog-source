---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Unix-Erbe von macOS und Linux
translated: true
type: note
---

### Gemeinsame Ursprünge von macOS und Linux

macOS (früher OS X) und Linux haben konzeptionelle Wurzeln in Unix, einem bahnbrechenden Multitasking-Betriebssystem, das in den 1970er Jahren bei Bell Labs entwickelt wurde. Linux, erschaffen von Linus Torvalds im Jahr 1991, ist ein Open-Source-Kernel, der nach dem Vorbild von Unix entwickelt, aber unabhängig programmiert wurde – es leitet sich nicht vom Unix-Quellcode ab. macOS hingegen basiert auf Darwin (einem Unix-ähnlichen Betriebssystem von Apple, das auf FreeBSD basiert), das Unix-Komponenten enthält und von The Open Group als Unix-konform zertifiziert ist. Dieses gemeinsame Erbe erklärt viele Ähnlichkeiten in Tools und Befehlen, da beide darauf abzielen, Unix-ähnliche Funktionalität bereitzustellen.

Unterstützende Belege: Die Unix-Standards (z.B. POSIX) beeinflussten beide Systeme, um Kompatibilität sicherzustellen. Linux-Distributionen wie Ubuntu sind ausdrücklich Unix-ähnlich, und macOS erbt Unix-Tools durch BSD (Berkeley Software Distribution), einen weiteren frühen Unix-Zweig.

### Warum beide den 'ps'-Befehl haben

Der 'ps'-Befehl (process status) zeigt Informationen über laufende Prozesse an und stammt direkt von Unix, wo er erstmals in den 1970er Jahren implementiert wurde. Sowohl macOS als auch Linux beinhalten 'ps', weil:
- Es Teil ihres Unix-Erbes ist: macOS über Darwin/FreeBSD und Linux über das PROC-Dateisystem und Standard-Utilities von GNU oder POSIX-Spezifikationen.
- Es essentiell für Systemdiagnose, Scripting und Administration ist, weshalb es standardmäßig in ihren Kern-Toolsets gebündelt ist (z.B. in macOS's Terminal oder Linux's Shell).

Die Befehls-Syntax, wie `ps -p pid -o pid,ppid,lstart,etime,command`, wird auf beiden Systemen aufgrund gemeinsamer POSIX-Standards unterstützt, obwohl sich die Optionen leicht unterscheiden können (z.B. hat macOS BSD-geprägte Flags, während Linux oft GNU-Varianten verwendet). Dies ist kein Zufall – es ist eine direkte Abstammung von Unix.

### Kann man sagen, dass macOS und Linux beide Unix sind?

Nicht genau: "Unix" ist eine Familie von Betriebssystemen und eine eingetragene Marke. macOS qualifiziert sich als Unix, weil Darwin zertifiziert ist (von The Open Group) und der Single Unix Specification (SUS) entspricht. Linux hingegen ist ein Kernel, der die Basis für vollständige Betriebssysteme (Distros wie Debian) bildet, aber der Kernel selbst und seine Distributionen sind offiziell nicht "Unix" – sie sind Unix-ähnlich oder Unix-kompatibel, da sie POSIX entsprechen, ohne vollständige Zertifizierung oder gemeinsame Codebasis.

Man könnte sagen, sie sind "Unix-ähnlich" oder "Bewahrer der Unix-Traditionen", aber Linux als "Unix" zu bezeichnen, wäre ungenau. In der Praxis spielt dies für die meisten Benutzer keine große Rolle, da sie sich bei Befehlen wie 'ps' ähnlich verhalten. Wenn strikte Genauigkeit entscheidend ist, sollte man auf Zertifizierungen achten oder die offiziellen Definitionen konsultieren.