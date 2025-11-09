---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'BMAD Core: Agile KI-Entwicklungsgrundlage'
translated: true
type: note
---

BMAD Core ist die grundlegende Komponente der BMAD-Methode (Breakthrough Method for Agile AI-Driven Development), ein Open-Source-Framework, das entwickelt wurde, um die KI-gestützte Softwareentwicklung (und erweiterbar auf andere Bereiche wie kreatives Schreiben oder Business-Strategy) zu optimieren, indem spezialisierte KI-Agents in einem agilen Workflow orchestriert werden.

### Wichtige Aspekte von BMAD Core:
- **Rolle und Zweck**: Es fungiert als eine "schlanke, schnelle Grundlage", die KI-Agents, Workflows, Richtlinien und Templates standardisiert, um vorhersehbare, hochwertige Ergebnisse zu gewährleisten. Dies behebt häufige Probleme bei der KI-Entwicklung, wie Kontextverlust und inkonsistente Planung, durch die Verwendung strukturierter Markdown-/YAML-Dateien für Agenten-Personas, Aufgaben und Übergaben.
- **Kernkomponenten**:
  - **Agents**: Eigenständige Markdown-Dateien (z.B. in `bmad-core/agents/`), die Rollen wie BMAD Master (Aufseher), Scrum Master (Planung), Dev (Programmierung) und QA (Tests) definieren. Jede enthält YAML-Konfigurationen für Persona, Befehle und Abhängigkeiten.
  - **Templates und Markup**: Eine benutzerdefinierte Auszeichnungssprache (definiert in `bmad-core/utils/template-format.md`) für wiederverwendbare Prompts und Verarbeitungslogik, die dynamische Dokumentenerstellung ohne separate Aufgaben ermöglicht.
  - **Konfiguration**: Zentralisiert in Dateien wie `core-config.yaml`, die API-Schlüssel, LLM-Integrationen (z.B. OpenAI, Claude) und Lazy-Loading von Ressourcen verwaltet, um Überlastung zu vermeiden.
  - **Workflows**: YAML-basierte Blaupausen, die Aufgaben, Abhängigkeiten und Agenten-Kollaborationen über "Story-Dateien" sequenzieren (z.B. für PRD-Erstellung, Architekturdesign und iterative Entwicklungszyklen).
- **Installation und Verwendung**: Einrichtung via Python (3.9+ erforderlich) in einem Projektverzeichnis, wobei ein versteckter `.bmad-core`-Ordner mit allen Essentials erstellt wird. Integriert sich mit IDEs wie Cursor oder VS Code für nahtlose Agenten-Interaktionen.
- **Erweiterbarkeit**: Unterstützt "Expansion Packs" für domainspezifische Agents (z.B. Infrastructure DevOps oder Game Dev), wodurch der Kern generisch und modular bleibt.

Das Framework wird auf GitHub gehostet (bmad-code-org/BMAD-METHOD) und legt den Schwerpunkt auf natürliche Sprache statt auf starre Programmierung, was es für Einzelentwickler oder Teams, die auf Enterprise-Niveau skalieren, zugänglich macht. Es gewann 2025 an Bedeutung für "Vibe Coding" und agentische Agilität, obwohl einige Benutzer eine Lernkurve für das anfängliche PRD-Setup feststellen. Für die praktische Einrichtung siehe die offizielle Dokumentation oder die Website unter bmadcodes.com.