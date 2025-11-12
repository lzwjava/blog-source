---
audio: false
generated: true
lang: de
layout: post
title: Verstärkerkonfigurationen
translated: true
type: note
---

Hier ist eine umfassende Erklärung der **drei grundlegenden Verstärkerschaltungen** – **Common Emitter (CE)**, **Common Collector (CC)** (auch bekannt als **Emitterfolger**), und **Common Base (CB)** – mit Fokus auf ihren Aufbau, Signaleigenschaften, Vorteilen, Nachteilen und typischen Anwendungen.

---

## 🔷 1. Common Emitter (CE) Verstärker

### 🔧 Konfiguration
- **Eingang**: Liegt zwischen Basis und Emitter.
- **Ausgang**: Wird zwischen Kollektor und Emitter abgegriffen.
- **Gemeinsame Elektrode**: Der Emitter ist für Eingang und Ausgang gemeinsam.

### 🔍 Wichtige Eigenschaften

| Eigenschaft             | Beschreibung                       |
|-------------------------|------------------------------------|
| **Spannungsverstärkung** | Hoch                               |
| **Stromverstärkung**    | Mittel bis hoch                    |
| **Leistungsverstärkung**| Hoch                               |
| **Phasenverschiebung**  | 180° (invertierter Ausgang)        |
| **Eingangsimpedanz**    | Mittel                             |
| **Ausgangsimpedanz**    | Mittel                             |

### ✅ Vorteile
- Geeignet für Spannungs- und Leistungsverstärkung.
- Am weitesten verbreitete Konfiguration.

### ❌ Nachteile
- Invertiert das Signal (180° Phasenverschiebung).
- Weniger geeignet für Impedanzanpassung.

### 🧰 Anwendungen
- Allgemeine Signalverstärkung.
- Audioverstärker.
- Zwischenstufen in Verstärkern.

---

## 🔷 2. Common Collector (CC) Verstärker — *Emitterfolger*

### 🔧 Konfiguration
- **Eingang**: Liegt zwischen Basis und Kollektor.
- **Ausgang**: Wird zwischen Emitter und Kollektor abgegriffen.
- **Gemeinsame Elektrode**: Der Kollektor ist für Eingang und Ausgang gemeinsam.

### 🔍 Wichtige Eigenschaften

| Eigenschaft             | Beschreibung                           |
|-------------------------|----------------------------------------|
| **Spannungsverstärkung** | ≈1 (Einheitsverstärkung)              |
| **Stromverstärkung**    | Hoch                                   |
| **Leistungsverstärkung**| Mittel                                 |
| **Phasenverschiebung**  | 0° (keine Invertierung)                |
| **Eingangsimpedanz**    | Hoch                                   |
| **Ausgangsimpedanz**    | Niedrig                                |

### ✅ Vorteile
- Hervorragende Pufferstufe.
- Gute Impedanzanpassung (hohe Eingangs-, niedrige Ausgangsimpedanz).
- Keine Signalinvertierung.

### ❌ Nachteile
- Keine Spannungsverstärkung.
- Nicht geeignet als eigenständiger Verstärker, wo Spannungsverstärkung benötigt wird.

### 🧰 Anwendungen
- Puffer zwischen Stufen.
- Treiben niederohmiger Lasten.
- Spannungsfolger.

---

## 🔷 3. Common Base (CB) Verstärker

### 🔧 Konfiguration
- **Eingang**: Liegt zwischen Emitter und Basis.
- **Ausgang**: Wird zwischen Kollektor und Basis abgegriffen.
- **Gemeinsame Elektrode**: Die Basis ist für Eingang und Ausgang gemeinsam.

### 🔍 Wichtige Eigenschaften

| Eigenschaft             | Beschreibung                             |
|-------------------------|------------------------------------------|
| **Spannungsverstärkung** | Hoch                                     |
| **Stromverstärkung**    | Kleiner als 1                            |
| **Leistungsverstärkung**| Mittel                                   |
| **Phasenverschiebung**  | 0° (keine Invertierung)                  |
| **Eingangsimpedanz**    | Sehr niedrig                             |
| **Ausgangsimpedanz**    | Hoch                                     |
| **Frequenzgang**        | Sehr breit (gut für Hochfrequenzanwendungen) |

### ✅ Vorteile
- Hervorragendes Hochfrequenzverhalten.
- Stabile Betriebsweise.

### ❌ Nachteile
- Niedrige Eingangsimpedanz – erfordert sorgfältige Auslegung der Treiberstufe.
- Begrenzte Stromverstärkung.

### 🧰 Anwendungen
- HF-Verstärker (Hochfrequenzverstärker).
- Hochfrequente Signalverstärkung.
- Impedanzanpassung (für niederohmige Quellen an hochohmige Lasten).

---

## 🧠 Zusammenfassungstabelle

| Konfiguration          | Spannungsverstärkung | Stromverstärkung | Phasenverschiebung | Eingangsimpedanz | Ausgangsimpedanz | Anwendung                    |
|------------------------|----------------------|------------------|--------------------|------------------|------------------|------------------------------|
| **Common Emitter (CE)**   | Hoch                 | Hoch             | 180°               | Mittel           | Mittel           | Allgemeine Verstärkung       |
| **Common Collector (CC)** | ≈1 (Einheit)         | Hoch             | 0°                 | Hoch             | Niedrig          | Pufferung, Impedanzanpassung |
| **Common Base (CB)**      | Hoch                 | <1               | 0°                 | Niedrig          | Hoch             | Hochfrequenzanwendungen      |

---

Möchten Sie visuelle Schaltbilder dieser Konfigurationen oder eine Beispielschaltung für eine davon analysiert haben?