---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'Analoge Modulationsverfahren: AM, FM, PM'
translated: true
type: note
---

### Modulationsverfahren: AM, FM und PM

Im Kontext von Kommunikationssystemen und Signalverarbeitung beziehen sich **AM**, **FM** und **PM** auf grundlegende **analoge Modulationsverfahren**. Diese Methoden werden verwendet, um ein informationsführendes Signal (wie Audio oder Daten) auf eine höherfrequente Trägerwelle zu kodieren (oder zu "modulieren"), um eine effiziente Übertragung über Medien wie Radiowellen, Kabel oder drahtlose Kanäle zu ermöglichen. Während sie primär mit analoger Kommunikation assoziiert werden, können sie in hybriden Systemen – beispielsweise wenn digital abgetastete Signale zur Übertragung moduliert werden oder wenn empfangene modulierte Signale digitalisiert werden – mit Analog-Digital (A/D) und Digital-Analog (D/A) Wandlungen in Berührung kommen.

Hier eine Aufschlüsselung der einzelnen Verfahren:

- **AM (Amplitudenmodulation)**:  
  Die Amplitude (Stärke oder Höhe) der Trägerwelle wird proportional zur Amplitude des Modulationssignals variiert, während die Frequenz des Trägers konstant bleibt. Dies ist einfach und wird weit verbreitet im AM-Rundfunk eingesetzt. Sie ist anfällig für Rauschen, da Störungen die Amplitude direkt beeinflussen.  
  *Beispiel*: Bei der Sprachübertragung erhöhen lautere Töne die Amplitudenpeaks des Trägers.

- **FM (Frequenzmodulation)**:  
  Die Frequenz der Trägerwelle wird entsprechend der Amplitude und Frequenz des Modulationssignals variiert, während die Amplitude des Trägers konstant bleibt. FM bietet eine bessere Rauschunterdrückung und ist üblich im FM-Rundfunk, bei TV-Ton und in Sprechfunkgeräten.  
  *Beispiel*: Höher frequentierte Audiosignale verschieben die Trägerfrequenz proportional nach oben oder unten.

- **PM (Phasenmodulation)**:  
  Die Phase (Zeitpunkt oder Versatz) der Trägerwelle wird basierend auf den Änderungen des Modulationssignals verändert, bei konstanter Amplitude und Frequenz. PM ist ähnlich zur FM (sie sind mathematisch über Differentiation verwandt) und wird oft in digitalen Systemen wie Phase-Shift Keying (PSK) verwendet, aber in analoger Form findet sie Anwendung in einigen Satelliten- und Mobilfunkkommunikationssystemen.  
  *Beispiel*: Eine Änderung im Modulationssignal bringt den Wellenformzyklus des Trägers vor oder verzögert ihn.

#### Bezug zu A/D- und D/A-Wandlungen
Diese Verfahren sind direkter mit der analogen Übertragung verbunden, aber in modernen Systemen:
- Während der **D/A-Wandlung** könnte ein digitales Signal in eine analoge Modulationswellenform rekonstruiert werden, bevor AM/FM/PM angewendet wird, um es für die HF (Hochfrequenz)-Übertragung vorzubereiten.
- Bei der **A/D-Wandlung** wird ein empfangenes analoges moduliertes Signal (z.B. FM-Radio) zuerst demoduliert, dann abgetastet und in digitale Form quantisiert.

Für vertiefende Informationen siehe Ressourcen zur analogen Modulation in der Signalverarbeitung.

[Analoge Modulationsverfahren](https://en.wikipedia.org/wiki/Modulation#Analog_modulation_methods)  
[FM vs AM Vergleich](https://www.electronics-tutorials.ws/accircuits/amplitude-modulator.html)