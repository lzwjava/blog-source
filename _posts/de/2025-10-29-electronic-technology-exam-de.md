---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Prüfungsfragen zu Grundlagen der Elektronik
translated: true
type: note
---

### Beispielprüfungsfragen: Grundlagen der Elektronik (III)  
*(Basierend auf der Wen Xidong Edition, National Higher Education Selbststudienprüfung)*  

Dieser Satz stammt aus früheren 自考-Prüfungen für den Kurs 电子技术基础（三）. Die Themen umfassen Wechselstromkreisanalyse, Halbleiter, Transistoren und Operationsverstärker. Die Fragen sind aus Gründen der Übersichtlichkeit auf Englisch (übersetzt aus den chinesischen Originalen). Jede Single-Choice-Frage ist 1 Punkt wert; die Analysefrage ist 5 Punkte wert.

#### Abschnitt I: Single-Choice-Fragen  
Wählen Sie die richtige Option (A, B, C oder D) für jede Frage.

1. **Unter den folgenden Beschreibungen der Eigenschaften einer idealen Spannungsquelle ist die richtige:**  
   A. Der Innenwiderstand der idealen Spannungsquelle strebt gegen unendlich.  
   B. Ideale Spannungsquellen können jederzeit parallel geschaltet werden.  
   C. Die Ausgangsspannung der idealen Spannungsquelle hängt von der Last ab.  
   D. Der Strom, der durch die ideale Spannungsquelle fließt, hängt von der Last ab.

2. **Gegeben sei der Phasenstrom, der durch die induktive Reaktanz \\( \omega L = 2 \, \Omega \\) fließt, als \\( I = 10 \angle 30^\circ \\) mA, dann ist die Phasorspannung daran:**  
   A. \\( U = 20 \angle 0^\circ \\) mV  
   B. \\( U = 20 \angle 120^\circ \\) mV  
   C. \\( U = 20 \angle 30^\circ \\) mV  
   D. \\( U = 20 \angle -60^\circ \\) mV

3. **Angenommen, der Kondensator \\( C = 1 \, \mu \mathrm{F} \\), die Spannung am Kondensator beträgt \\( \cos(100 \pi t) \\) mV, dann ist der Strom durch den Kondensator:**  
   A. \\( i_c(t) = -0.1 \times 10^{-6} \pi \sin(100 \pi t) \\) A  
   B. \\( i_c(t) = 0.1 \times 10^{-6} \pi \sin(100 \pi t) \\) A  
   C. \\( i_c(t) = -0.1 \times 10^{-6} \sin(100 \pi t) \\) A  
   D. \\( i_c(t) = 0.1 \times 10^{-6} \sin(100 \pi t) \\) A

4. **Der Majoritätsträger im P-Typ-Halbleiter ist:**  
   A. Freie Elektronen  
   B. Löcher  
   C. Dreiwertige Störstellenatome  
   D. Dreiwertige Störstellenionen

5. **Gegeben seien die Potentiale der drei Elektroden eines bestimmten Kristalldreipols, wie in der Abbildung gezeigt (Emitter-Basis-Kollektor-Spannungen, die NPN-Silizium-Transistoreigenschaften anzeigen), der Typ dieses Transistors ist:**  
   *(Abbildungsbeschreibung: Emitter bei 0V, Basis bei 0,7V, Kollektor bei 5V – typische vorwärts vorgespannte NPN-Silizium-Sperrschicht.)*  
   A. PNP-Typ Germaniumröhre  
   B. NPN-Typ Germaniumröhre  
   C. PNP-Typ Siliziumröhre  
   D. NPN-Typ Siliziumröhre

#### Abschnitt II: Analysefrage  
**Frage 31 (5 Punkte):** In der in Abbildung 31 gezeigten Schaltung (eine grundlegende invertierende Operationsverstärker-Konfiguration mit Eingangswiderstand \\( R_i = 10 \, \mathrm{k} \Omega \\), Rückkopplungswiderstand \\( R_f = 20 \, \mathrm{k} \Omega \\), Eingangsspannung \\( U_i = 10 \\) V), berechnen Sie die Ausgangsspannung \\( U_o \\).

*(Abbildungsbeschreibung: Standard-invertierender Operationsverstärker; nicht-invertierender Eingang geerdet. Verwenden Sie die Verstärkungsformel: \\( U_o = - \frac{R_f}{R_i} \times U_i \\).)*

**Lösungshinweis:** Wenden Sie das Prinzip des virtuellen Massepunktes an (invertierender Eingang auf 0V-Potential). Der Spannungsabfall über \\( R_i \\) entspricht \\( U_i \\), also Strom \\( I = \frac{U_i}{R_i} \\). Dann ist \\( U_o = -I \times R_f \\). Erwartetes Ergebnis: \\( U_o = -20 \\) V.

Diese Fragen entsprechen Kapiteln wie Wechselstrom-Phasoren (Kap. 2), Halbleiter (Kap. 3–4) und Operationsverstärker (Kap. 5). Übungstipp: Wiederholen Sie Phasorenrechnung, Ladungsträgertransport und die Regeln für ideale Operationsverstärker.

**Referenzen:**  
- [04730 电子技术基础(三) 2010.07 自考 历年真题 试题](https://wenku.baidu.com/view/a2a96333b90d6c85ec3ac6bf.html)  
- [自考电子技术基础（三）04730真题及答案免费分享](http://www.s9w.cn/zkzt408/)