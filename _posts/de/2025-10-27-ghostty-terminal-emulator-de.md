---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'Ghostty: Schneller plattformübergreifender Terminalemulator'
translated: true
type: note
---

Ghostty ist ein plattformübergreifender Terminal-Emulator, der für Geschwindigkeit, Funktionsumfang und native Integration unter macOS und Linux entwickelt wurde (mit Windows-Unterstützung in Arbeit). Er ist hauptsächlich in **Zig** geschrieben, einer modernen Systemprogrammiersprache, die sich auf Sicherheit, Leistung und Einfachheit konzentriert – und nicht in Rust, wie Sie gefragt hatten.

### Wichtige Implementierungsdetails
- **Kern-Architektur**: Der gemeinsame Kern (verantwortlich für Terminalemulation, Rendering und einen Großteil der Logik) ist in Zig geschrieben. Dies ermöglicht Low-Level-Kontrolle und hohe Leistung, einschließlich GPU-Beschleunigung via Metal (auf macOS) oder Vulkan/OpenGL (plattformübergreifend).
- **Plattformspezifische Ebenen**: Um ein natives Gefühl zu erreichen, werden plattformspezifische Toolkits für die GUI verwendet:
  - macOS: Swift/AppKit für Windowing und UI.
  - Linux: GTK für Windowing.
  - Eine gemeinsame Rendering-Pipeline in Zig verbindet alles.
- **Bemerkenswerte Funktionen aufgrund des Designs**:
  - Blitzschnelles Starten und Rendering (z.B. bewältigt große Ausgaben ohne Verzögerung).
  - Unterstützt Ligaturen, Emoji und erweiterte Typografie.
  - Konfigurierbar via Lua-Skripte für Erweiterbarkeit.
  - Kein Ballast – er ist minimalistisch, aber mit Essentials wie Tabs, Suche und OSC 52 Clipboard-Integration ausgestattet.
- **Entwicklungsphilosophie**: Erstellt von Mitchell Hashimoto (bekannt durch HashiCorp), betont er Korrektheit und Effizienz gegenüber Kompatibilitäts-Hacks, die in älteren Terminals wie xterm üblich sind. Er ist quelloffen unter der MIT-Lizenz.

Wenn Sie interessiert sind, daran zu bauen oder zu hacken, sehen Sie sich das GitHub-Repo für die Zig-Codebasis und Build-Anleitungen an (erfordert Zig 0.13+).

### Referenzen
- [Ghostty GitHub Repository](https://github.com/ghostty-org/ghostty)
- [Introducing Ghostty (Mitchell Hashimoto's Blog)](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Ghostty 1.0 Release Notes](https://dansasser.me/posts/ghostty-1-0-a-terminal-emulator-built-for-speed-features-and-native-integration/)