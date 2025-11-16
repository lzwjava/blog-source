---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: ResNet Revolutionierte Deep Learning
translated: true
type: note
---

ResNet (Residual Network) ist einer der wichtigsten Durchbrüche in der Geschichte des Deep Learning. Es wurde 2015 von Kaiming He et al. von Microsoft Research vorgestellt und gewann im selben Jahr den ImageNet-Wettbewerb mit einer verblüffenden Top-5-Fehlerrate von nur 3,57 % (besser als die menschliche Leistung zu dieser Zeit).

Hier ist der Grund, warum ResNet so ein großer Durchbruch war:

1.  **Es löste das "Degradationsproblem" (Verschwindende/explodierende Gradienten in sehr tiefen Netzen)**  
    Vor ResNet dachte man: "Wenn 20 Schichten gut funktionieren, sollten 56 Schichten noch besser funktionieren." In der Praxis verschlechterte das Stapeln weiterer Schichten jedoch die Genauigkeit – nicht aufgrund von Overfitting, sondern weil die Optimierung selbst schwieriger wurde. ResNet bewies, dass man Netze mit 100+ Schichten trainieren konnte (sie zeigten 152 Schichten, später gingen Leute zu 1000+ Schichten) und dennoch eine bessere Leistung erzielen konnte.

2.  **Residual-Blöcke + Skip Connections (die Schlüsselidee)**  
    Anstatt die Schicht zu bitten, H(x) direkt zu lernen, lernt ResNet das Residuum F(x) = H(x) − x, sodass der Block x + F(x) berechnet.  
    Mathematisch:  
    y = F(x, {W_i}) + x  
    Diese "Identity Shortcut" ermöglicht es den Gradienten, direkt durch das Netz über die Skip Connections zu fließen, was ein extrem tiefes Training möglich macht.

3.  **Unmittelbare und massive praktische Auswirkung**  
    - Wurde von 2016 bis ~2020 zum Backbone fast aller State-of-the-Art Vision-Modelle (und wird auch heute noch häufig verwendet).  
    - Verwendet in Objekterkennung (Faster R-CNN + ResNet), Segmentierung (DeepLab, Mask R-CNN), generativen Modellen (StyleGAN, etc.), Video, medizinischer Bildverarbeitung, etc.  
    - Varianten wie ResNet-50, ResNet-101, ResNeXt, Wide ResNet und ResNet-RS sind auch 2025 noch Standard-Baselines.

4.  **Ermöglichte die gesamte Ära "Deep Learning wird wirklich tief"**  
    Vor ResNet: Die besten ImageNet-Modelle hatten ~20–30 Schichten (VGG, GoogLeNet).  
    Nach ResNet: 100–1000+ Schichten wurden normal. Diese Tiefe war entscheidend, um reichhaltigere Features zu lernen.

5.  **Extrem einfache Idee, aber dennoch transformativ**  
    Das Paper ist berühmt für seine Klarheit und fügt nur einen cleveren Trick hinzu (Skip Connections + elementweise Addition). Keine neuen ausgefallenen Aktivierungsfunktionen, keine neuen Loss-Funktionen – nur architektonische Einsicht.

Kurz gesagt: ResNet bewies, dass "tiefer ist besser" wirklich funktionieren kann, wenn man die Architektur richtig entwirft, und es wurde der Standard-Ausgangspunkt für fast jedes Computer-Vision-Modell im folgenden Jahrzehnt.

Selbst heute, im Jahr 2025, wenn Transformer- und ConvNeXt/ViT-basierte Modelle die Bestenlisten dominieren, ist ResNet-50 immer noch der gebräuchlichste Benchmark-Backbone, weil es schnell, gut verstanden und extrem zuverlässig ist.

Paper (immer noch lesenswert):  
[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)