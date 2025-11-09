---
audio: false
date: 2025-09-06
generated: true
image: false
lang: de
layout: post
title: Optimale Modellauswahl für Kosten und Leistung
translated: true
type: note
---

Bei der Betrachtung Ihrer Claude Code-Konfiguration möchten Sie sowohl Kosten als auch Leistung optimieren. Hier sind einige Empfehlungen für die Auswahl "kostengünstiger und leistungsstarker" Modelle in Ihrem Router-Setup:

## Beste Kosten-/Leistungsmodelle aus Ihrer Liste:

**Für die meisten Aufgaben (Standard):**
- `deepseek/deepseek-chat-v3.1` - Hervorragende Leistung bei sehr niedrigen Kosten
- `deepseek/deepseek-r1` - Große Reasoning-Fähigkeiten, immer noch kosteneffektiv

**Für Hintergrundaufgaben:**
- `deepseek/deepseek-chat-v3.1` - Bereits eine gute Wahl
- `google/gemini-2.5-flash` - Schnell und kostengünstig

**Für Denk-/Reasoning-Aufgaben:**
- `deepseek/deepseek-r1` - Speziell für Reasoning-Aufgaben entwickelt
- `z-ai/glm-4.5` - Ihre aktuelle Wahl ist akzeptabel

**Aktualisierter Router-Vorschlag:**
```json
"Router": {
  "default": "openrouter,deepseek/deepseek-chat-v3.1",
  "background": "openrouter,google/gemini-2.5-flash",
  "think": "openrouter,deepseek/deepseek-r1",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "webSearch": "openrouter,google/gemini-2.5-flash"
}
```

## Wichtige Überlegungen:
- **DeepSeek-Modelle** bieten derzeit das beste Preis-Leistungs-Verhältnis
- **Gemini 2.5 Flash** ist sehr schnell und günstig für einfachere Aufgaben
- Behalten Sie **Kimi** für lange Kontexte, da es 200k+ Tokens gut verarbeitet
- **Gemini 2.5 Pro**, wenn Sie mehr Leistungsfähigkeit als Flash benötigen

Sie können die aktuellen Preise auf der OpenRouter-Website überprüfen, um die genauen Kosten zu vergleichen, aber DeepSeek-Modelle sind typischerweise 10-20x günstiger als GPT-4-Level-Modelle bei wettbewerbsfähiger Leistung.