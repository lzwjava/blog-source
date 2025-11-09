---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Ghostty plattformübergreifender Terminalemulator
translated: true
type: note
---

Ja, Ghostty ist als plattformübergreifender Terminal-Emulator konzipiert, was tatsächlich einer seiner Hauptvorteile ist – er wurde entwickelt, um konsistent auf mehreren Betriebssystemen mit hoher Leistung via GPU-Beschleunigung und nativer UI-Integration zu laufen. Allerdings ist der vollständige Support Stand Oktober 2025 derzeit auf macOS und Linux beschränkt, während Windows sich noch in der Planungsphase befindet, aber noch nicht veröffentlicht ist.

Was die Erfahrung betrifft: Sie ist nicht *exakt* identisch auf allen Plattformen, da Ghostty native UI-Komponenten verwendet (z.B. Cocoa auf macOS, GTK auf Linux), um sich auf jeder Plattform idiomatisch und integriert anzufühlen – wie eine speziell für das System entwickelte App und nicht wie eine universelle Portierung. Dennoch sind die Kernfunktionalität, die Features (wie Tabs, Split-Screens, Suche und erweiterte Terminal-Protokolle) und die Leistung überall dort, wo es unterstützt wird, sehr ähnlich und zuverlässig ausgelegt, um plattformspezifische Eigenheiten, wie man sie in weniger ausgereiften Emulatoren sehen könnte, zu minimieren.

Falls Windows bald erscheint (basierend auf laufenden GitHub-Diskussionen), sollte es demselben nativen Ansatz folgen, um auch dort ein nahtloses Gefühl zu gewährleisten.

[Ghostty Offizielle Features](https://ghostty.org/docs/features)  
[Ghostty GitHub Repo](https://github.com/ghostty-org/ghostty)  
[Ghostty Release Notes](https://ghostty.org/docs/install/release-notes)