---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Fortschritte bei der ImageNet-Klassifikation 2025
translated: true
type: note
---

Der State-of-the-Art (SOTA) auf ImageNet (speziell dem ImageNet-1K-Validierungssatz für Bildklassifizierung) hat sich seit den dramatischen Verbesserungen nach 2012 stetig weiterentwickelt. Stand November 2025 erreichen die führenden Modelle Top-1-Genauigkeiten von etwa 91 %, was einer Top-1-Fehlerrate von ~9 % entspricht. Die Top-5-Genauigkeiten sind sogar noch höher und liegen typischerweise über 99 %, für eine Top-5-Fehlerrate von unter 1 %.

### Wichtige SOTA-Modelle (Top 5 vom Papers With Code Leaderboard)
Hier ist eine Momentaufnahme der aktuell leistungsstärksten Modelle (feinabgestimmt auf ImageNet-1K), basierend auf der Top-1-Genauigkeit. Top-5-Genauigkeiten werden für diese sehr leistungsstarken Modelle nicht immer explizit neu berichtet (da sie nahezu perfekte Werte erreichen), aber der Abgleich mit ähnlichen, aktuellen Architekturen legt Top-5-Fehler von unter 1 % für alle nahe:

| Rang | Modell | Top-1-Genauigkeit | Geschätzte Top-5-Genauigkeit | Parameter | Anmerkungen |
|------|--------|----------------|---------------------|------------|-------|
| 1 | CoCa (feinabgestimmt) | 91,0 % (9,0 % Fehler) | ~99,5 % (<0,5 % Fehler) | 2,1 Mrd. | Multimodales Bild-Text-Modell; überragend in Zero-Shot (86,3 % Top-1) und Frozen-Encoder-Szenarien (90,6 % Top-1). |
| 2 | Model Soups (BASIC-L) | 90,98 % (9,02 % Fehler) | ~99,4 % (<0,6 % Fehler) | ~1 Mrd. | Ensemble-Durchschnitt von feinabgestimmten Modellen für verbesserte Robustheit. |
| 3 | Model Soups (ViT-G/14) | 90,94 % (9,06 % Fehler) | ~99,4 % (<0,6 % Fehler) | 1,8 Mrd. | ViT-basiert; starke Generalisierung auf Out-of-Distribution-Daten. |
| 4 | DaViT-Giant | 90,4 % (9,6 % Fehler) | ~99,3 % (<0,7 % Fehler) | 1,4 Mrd. | ViT mit dualer Aufmerksamkeit; trainiert auf 1,5 Mrd. Bild-Text-Paaren. |
| 5 | ConvNeXt V2-Huge | 88,9 % (11,1 % Fehler) | ~99,0 % (~1,0 % Fehler) | 660 Mio. | CNN-Revival mit Masked Autoencoder Pre-Training; effizient für Edge Devices. |

### Klarstellung zu "<3 % Heute"
- Dies bezieht sich auf die **Top-5-Fehlerrate**, nicht auf Top-1. Vor-2012-Baselines (z.B. SVMs) lagen bei etwa 25 % Top-5-Fehler. Bis 2017 (SENet) sank sie auf ~2,3 %. Moderne SOTA-Modelle haben sie unter 1 % gedrückt, was Top-5-Vorhersagen für die meisten realen Anwendungsfälle im Wesentlichen zuverlässig macht.
- Die Top-1-Fehlerrate bleibt höher (~9 %), da sie eine exakte Übereinstimmung der *besten* Vorhersage erfordert, was strenger ist und empfindlicher auf Grenzfälle wie mehrdeutige Bilder reagiert.

Der Fortschritt hat sich in den letzten Jahren aufgrund von Datensatzsättigung verlangsamt – Gewinne kommen jetzt von massivem Pre-Training (z.B. auf ImageNet-21K oder Web-scale-Daten) und Techniken wie Model Ensembling oder Distillation. Die Leistung menschlicher Experten wird auf ~5 % Top-1-Fehler (oder 2-12 % Top-5, je nach Studie) geschätzt, daher hat die KI bei diesem Benchmark den Menschen übertroffen.

[ImageNet Benchmark (Papers With Code)](https://paperswithcode.com/sota/image-classification-on-imagenet)  
[Image Classification: State-of-the-Art Models in 2025 (HiringNet)](https://hiringnet.com/image-classification-state-of-the-art-models-in-2025)  
[CoCa: Contrastive Captioners are Image-Text Foundation Models (arXiv)](https://arxiv.org/abs/2205.01917)