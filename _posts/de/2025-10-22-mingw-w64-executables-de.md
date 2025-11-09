---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: MinGW-w64 enthaltene ausführbare Dateien
translated: true
type: note
---

### In MinGW-w64 enthaltene ausführbare Dateien

MinGW-w64 ist in erster Linie eine minimale Toolchain zum Cross-Compilieren nativer Windows-Anwendungen mit GCC und verwandten Tools. Der Fokus liegt auf Entwicklungswerkzeugen und nicht auf einer vollständigen Sammlung von Unix-ähnlichen Befehlen (z. B. enthält es standardmäßig **nicht** `gpg` oder GnuPG – diese sind in Umgebungen wie MSYS2 als separate Pakete verfügbar). Das `bin`-Verzeichnis der Kerninstallation enthält typischerweise die folgenden ausführbaren Dateien (basierend auf einem Standard-Standalone-Download, z. B. von den offiziellen SourceForge-Releases). Diese Liste kann je nach Version und Build leicht variieren, aber dies sind die gängigsten:

| Ausführbare Datei | Beschreibung |
|------------|-------------|
| `gcc.exe` | GNU C-Compiler |
| `g++.exe` | GNU C++-Compiler |
| `cpp.exe` | C-Präprozessor |
| `gfortran.exe` | GNU Fortran-Compiler (falls im Build enthalten) |
| `ld.exe` | GNU Linker |
| `as.exe` | GNU Assembler |
| `ar.exe` | Archivierer zum Erstellen von Bibliotheken |
| `ranlib.exe` | Erzeugt Index für Archivbibliotheken |
| `nm.exe` | Listet Symbole aus Objektdateien auf |
| `objdump.exe` | Zeigt Informationen aus Objektdateien an |
| `objcopy.exe` | Kopiert und übersetzt Objektdateien |
| `strip.exe` | Entfernt Symbole aus ausführbaren Dateien |
| `size.exe` | Listet Abschnittsgrößen von Objektdateien auf |
| `strings.exe` | Gibt druckbare Zeichenketten in Dateien aus |
| `readelf.exe` | Zeigt ELF-Dateiinformationen an (für Cross-Tools) |
| `dlltool.exe` | Erstellt DLL-Import-/Export-Dateien |
| `windres.exe` | Kompiliert Windows-Ressourcendateien |
| `gendef.exe` | Erzeugt .def-Dateien aus DLLs |
| `genidl.exe` | Erzeugt .idl-Dateien aus DLLs |
| `widl.exe` | Kompiliert IDL-Dateien für Wine/Winelib |
| `gcc-ar.exe` | GCC-Wrapper für ar |
| `gcc-nm.exe` | GCC-Wrapper für nm |
| `gcc-ranlib.exe` | GCC-Wrapper für ranlib |

Hierbei handelt es sich hauptsächlich um Compiler-, Linker- und Binärmanipulations-Tools von GCC und Binutils. Für eine umfassendere Unix-ähnliche Umgebung mit Tools wie `gpg`, `make`, `bash` usw. sollten Sie die Installation von MSYS2 (das MinGW-w64 als Komponente enthält) in Betracht ziehen und Pakete über `pacman` hinzufügen.

[MinGW-w64 Offizielle Website](https://www.mingw-w64.org/)  
[MSYS2 Pakete (für Erweiterungen wie GnuPG)](https://packages.msys2.org/package/mingw-w64-x86_64-gnupg)  
[SourceForge MinGW-w64 Downloads](https://sourceforge.net/projects/mingw-w64/files/)