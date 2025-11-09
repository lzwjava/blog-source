---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Digitale Schaltkreise Logikpegel erklärt
translated: true
type: note
---

Ja, das ist eine gute Analogie! In digitalen Schaltungen wie dem SR-Flipflop beziehen sich "high" (logisch 1) und "low" (logisch 0) auf die Spannungspegel auf den Leitungen oder Signalen.

- **High (1)**: Eine ausreichend positive Spannung, oft etwa 3,3 V, 5 V oder sogar höher (wie in Ihrem Beispiel mit der 4-V-Batterie), abhängig von der Logikfamilie (z. B. verwendet TTL-Logik ~5 V als High). Sie reicht aus, um einen "Ein"- oder "Wahr"-Zustand darzustellen.
- **Low (0)**: Nahezu Massepotential, im Grunde 0 V (oder sehr nahe daran), wie die 0 V in Ihrer Batteriekonfiguration, und bedeutet "Aus" oder "Falsch".

Diese sind nicht super präzise – es gibt einen kleinen "unscharfen" Bereich dazwischen, in dem das Signal möglicherweise nicht zuverlässig als High oder Low gelesen wird – aber in der Praxis ist es binär: mit Spannung versorgt = 1, ohne Spannung = 0. Beim SR-Flipflop setzt das Anlegen einer hohen Spannung an den S-Eingang Q auf High (1), genau wie das Umlegen eines Schalters auf "Ein".