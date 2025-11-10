---
audio: false
generated: true
lang: de
layout: post
title: Rusts Verhältnis zu C
translated: true
type: note
---

Nein, Rust ist nicht "auf C aufgebaut" in dem Sinne, dass es nach C kompiliert oder C als grundlegende Schicht für seinen eigenen Betrieb benötigt. Rust ist eine separate, moderne Systemprogrammiersprache.

Hier ist eine Aufschlüsselung der Beziehung zwischen Rust und C und wie Rust mit C-Bibliotheken interagiert:

**Ist Rust auf C aufgebaut?**

* **Compiler:** Der Rust-Compiler (`rustc`) ist hauptsächlich in Rust selbst geschrieben. Frühe Versionen des Compilers wurden mit OCaml gebootstrappt, aber er ist jetzt selbst-hostend.
* **Low-Level-Interaktion:** Rust ist eine Low-Level-Sprache, die direkt mit dem Betriebssystem und der Hardware interagieren kann, ähnlich wie C oder C++. Sie verlässt sich nicht auf C als Vermittler für diese grundlegenden Operationen.
* **LLVM:** Rusts Compiler verwendet LLVM (Low Level Virtual Machine) als Backend für Codegenerierung und Optimierung. LLVM selbst ist größtenteils in C++ geschrieben. Das bedeutet, dass Rust-Code letztendlich in LLVM Intermediate Representation (IR) übersetzt wird, die dann optimiert und in Maschinencode kompiliert wird. In diesem Sinne gibt es also eine Abhängigkeit von einer C++-basierten Toolchain (LLVM), aber Rust selbst ist nicht "auf C aufgebaut."

**Kann Rust alle C-Bibliotheken verwenden?**

Ja, Rust bietet eine hervorragende Interoperabilität mit C-Bibliotheken durch seine **Foreign Function Interface (FFI)**. Das bedeutet, Sie können Funktionen aufrufen und Datenstrukturen aus bestehenden C-Bibliotheken direkt in Ihrem Rust-Code verwenden.

Im Allgemeinen funktioniert das so:

1.  **`extern "C"`-Blöcke:** Sie definieren einen `extern "C"`-Block in Ihrem Rust-Code, um die Signaturen der C-Funktionen zu deklarieren, die Sie aufrufen möchten. Dies teilt dem Rust-Compiler mit, dass diese Funktionen der C Application Binary Interface (ABI) entsprechen, die festlegt, wie Funktionen aufgerufen und Daten im Speicher angeordnet werden.
2.  **`#[link]`-Attribut:** Sie verwenden das Attribut `#[link(name = "foo")]`, um dem Rust-Linker mitzuteilen, dass er gegen die angegebene C-Bibliothek (z.B. `libfoo.so` oder `foo.lib`) linken soll.
3.  **`unsafe`-Blöcke:** Aufrufe von C-Funktionen werden typischerweise in `unsafe`-Blöcken in Rust gekapselt. Dies ist notwendig, weil Rusts starke Speichersicherheitsgarantien nicht durchgesetzt werden können, wenn mit "fremdem" Code interagiert wird, der nicht Rusts Regeln folgt. Sie als Programmierer sind für die Sicherheit dieser Aufrufe verantwortlich.
4.  **`bindgen`:** Für größere C-Bibliotheken kann das manuelle Schreiben aller `extern "C"`-Deklarationen mühsam sein. Tools wie `bindgen` können automatisch Rust-FFI-Bindings aus C-Header-Dateien generieren, was den Prozess erheblich vereinfacht.
5.  **`cty`-Crate:** Die `cty`-Crate stellt C-kompatible primitive Datentypen (wie `c_int`, `c_char`, etc.) bereit, um eine korrekte Datentyp-Zuordnung zwischen Rust und C sicherzustellen.

**Warum C-Bibliotheken in Rust verwenden?**

* **Bestehenden Code nutzen:** Es gibt ein riesiges Ökosystem von gut getesteten und hochoptimierten C-Bibliotheken für verschiedene Aufgaben (z.B. Systemaufrufe, Kryptographie, numerisches Rechnen, Grafik). Rust ermöglicht es Ihnen, auf diese bestehende Ressource zuzugreifen, ohne alles von Grund auf neu schreiben zu müssen.
* **Betriebssystem-Schnittstellen:** Betriebssysteme stellen viele ihrer Funktionalitäten über C-kompatible Schnittstellen bereit. Rust muss in der Lage sein, diese Funktionen aufzurufen, um mit dem OS zu interagieren.
* **Leistungskritische Abschnitte:** Während Rust im Allgemeinen sehr schnell ist, könnte es bereits hochspezialisierten, leistungskritischen Code in C geben, der direkt integriert werden kann.

Zusammenfassend lässt sich sagen, dass Rust nicht "auf C aufgebaut" ist, aber robuste Mechanismen (FFI) für nahtlose Interoperabilität mit C-Bibliotheken bereitstellt, die es Rust-Entwicklern ermöglichen, das umfangreiche C-Ökosystem zu nutzen.