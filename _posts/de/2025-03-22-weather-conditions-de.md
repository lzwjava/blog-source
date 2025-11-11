---
audio: false
generated: true
lang: de
layout: post
title: Vollständige Wetterbedingungen in iOS Kurzbefehlen
translated: true
type: note
---

Hier ist eine umfassende Aufschlüsselung aller verfügbaren Wetterbedingungs-Wertebereiche in iOS Shortcuts:

## UV-Index
- **Bereich**: 0-11+
- **Skala**:
  - 0-2: Niedrig
  - 3-5: Mäßig
  - 6-7: Hoch
  - 8-10: Sehr hoch
  - 11+: Extrem

## Temperatur
- **Bereich**: Variiert je nach Standort
- **Einheiten**: Celsius (°C) oder Fahrenheit (°F)
- **Typischer Bereich**: -50°C bis 50°C (-58°F bis 122°F)

## Gefühlte Temperatur
- **Bereich**: Ähnlich der tatsächlichen Temperatur
- **Einheiten**: Celsius (°C) oder Fahrenheit (°F)
- **Faktoren**: Kombiniert Temperatur, Luftfeuchtigkeit, Windchill

## Luftfeuchtigkeit
- **Bereich**: 0-100%

## Sichtweite
- **Bereich**: 0-10+ Meilen oder 0-16+ Kilometer

## Windgeschwindigkeit
- **Bereich**: 0-100+ mph oder 0-160+ km/h
- **Einheiten**: mph, km/h, m/s oder Knoten

## Windrichtung
- **Bereich**: 0-359 Grad
- **Himmelsrichtungen**: N (0°), O (90°), S (180°), W (270°)

## Luftqualitätsindex (AQI)
- **Bereich**: 0-500+
- **Skala**: Gut (0-50) bis Gefährlich (301+)

## Niederschlagswahrscheinlichkeit
- **Bereich**: 0-100%
- **Interpretation**: Wahrscheinlichkeit von Niederschlag im Vorhersagezeitraum

## Niederschlagsmenge
- **Bereich**: 0 bis 100+ mm oder Zoll
- **Einheiten**: mm oder Zoll
- **Zeitraum**: Normalerweise pro Stunde oder pro Tag gemessen

## Niederschlagsintensität
- **Bereich**:
  - Kein: 0 mm/h
  - Leicht: 0,1-2,5 mm/h
  - Mäßig: 2,5-10 mm/h
  - Stark: 10-50 mm/h
  - Heftig: 50+ mm/h

## Luftdruck
- **Bereich**: Typisch 950-1050 hPa/mb
- **Einheiten**: hPa, mb oder inHg
- **Standarddruck**: 1013,25 hPa auf Meereshöhe

## Taupunkt
- **Bereich**: Ähnlich dem Temperaturbereich
- **Einheiten**: Celsius (°C) oder Fahrenheit (°F)
- **Komfortstufen**:
  - <55°F (<13°C): Trocken und angenehm
  - 55-65°F (13-18°C): Angenehm
  - >65°F (>18°C): Zunehmend schwül und unangenehm

## Bewölkung
- **Bereich**: 0-100%

## Wetterzustand
- **Werte**: Textbeschreibungen (Klar, Teilweise bewölkt, Regen, Schnee, etc.)

## Sonnenaufgang/Sonnenuntergang Zeiten
- **Bereich**: Zeitwerte in lokaler Zeitzone

## Mondphase
- **Bereich**: 0-1 (0 = Neumond, 0,5 = Vollmond, 1 = Neumond)
- **Textwerte**: Neumond, Zunehmende Sichel, Erstes Viertel, etc.

## Pollenflug
- **Bereich**: Normalerweise 0-12
- **Skala**: Niedrig, Mäßig, Hoch, Sehr Hoch

## Hitzeindex
- **Bereich**: Temperaturbereich, aber nur berechnet, wenn die Temperatur über 80°F (27°C) liegt
- **Einheiten**: Wie Temperatur

## Schneemenge
- **Bereich**: 0 bis 100+ cm oder Zoll
- **Einheiten**: cm oder Zoll
- **Zeitraum**: Normalerweise pro Stunde oder pro Tag

Diese Wetterbedingungswerte können in bedingten Anweisungen innerhalb von Shortcuts verwendet werden, um ausgefeilte, wetterbasierte Automatisierungen zu erstellen, die auf bestimmte Bedingungen zugeschnitten sind.