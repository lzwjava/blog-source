---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Schallreaktive LED-Schaltung Bauen
translated: true
type: note
---

### Einfache musikreaktive LED-Schaltung auf dem Steckbrett

Es klingt, als erinnerst du dich an ein cooles soundreaktives LED-Projekt von 2021 – im Grunde eine Schaltung, bei der LEDs im Takt der Musik pulsieren oder "tanzen", erkannt über ein Mikrofon oder Audioeingang. Die "Bubble Lights" sind wahrscheinlich einfach nur farbige LEDs auf dem Steckbrett, und der "Volume Down"-Teil könnte sich auf das Anpassen der Empfindlichkeit oder die Verwendung eines Potentiometers zur Kontrolle der LED-Helligkeit/Reaktion beziehen.

Für eine super einfache Version (kein Mikrocontroller nötig, nur grundlegende Bauteile) kannst du eine bauen, die mehrere LEDs im Rhythmus von nahegelegener Musik oder Geräuschen aufleuchten lässt. Diese verwendet ein Elektretmikrofon (oft in grundlegenden Tutorials als "Lautsprecher" aufgeführt, agiert hier aber als Mikrofon) zur Audioaufnahme, einige Dioden zur Signalverarbeitung und Transistoren implizit durch die Zenerdioden zum Ansteuern der LEDs. Es ist steckbrettfreundlich und kostet unter 10 € an Bauteilen.

#### Benötigte Hardwarekomponenten
Hier ist eine minimale Liste für 6 LEDs (skaliere nach unten, wenn du weniger möchtest):

| Bauteil         | Wert/Spezifikation | Menge   |
|-----------------|--------------------|---------|
| Widerstand     | 56Ω               | 6       |
| Kondensator    | 470µF             | 2       |
| Diode          | 1N4007 (oder ähnlich) | 2    |
| Zenerdiode     | 1N4148            | 5       |
| Elektretmikrofon (kleiner Lautsprecher/Mikrofon) | 8Ω, 0.5W | 1 |
| LED            | Beliebige Farbe, 5mm | 6    |
| Steckbrett     | Standardgröße     | 1       |
| Steckbrücken   | Male-Male         | ~20     |
| Stromversorgung | 9V-Batterie oder 5-12V Netzteil | 1 |

Optional für "Lautstärkeregelung": Füge einen 10kΩ-Potentiometer in Reihe mit dem Mikrofon hinzu, um die Empfindlichkeit anzupassen (wie das Drehen der "Lautstärke" des Eingangssignals).

#### Kurzer Aufbauüberblick
1. **Richte den Mikrofoneingang ein**: Verbinde das Mikrofon über einen Kondensator (für das AC-Audiosignal) zwischen Stromversorgung und Masse. Dies nimmt Schallschwingungen auf und wandelt sie in elektrische Impulse um.
2. **Signalverarbeitung**: Verwende die Dioden und Zenerdioden in einem Gleichrichter/Filter-Aufbau, um die Audio-Wellenform in Impulse umzuwandeln, die die LEDs bei unterschiedlichen Intensitäten basierend auf Lautstärke/Beatstärke auslösen. Die Zenerdioden schützen vor Spannungsspitzen.
3. **LED-Ansteuerung**: Verkable jede LED parallel mit einem 56Ω-Widerstand zur Strombegrenzung. Verbinde das verarbeitete Signal mit den LED-Anoden – lautere Bässe oder Beats lassen sie heller/schneller flackern.
4. **Stromversorgung anschließen**: An 9V anschließen. Spiele Musik in der Nähe ab (Handylautsprecher funktioniert), und die LEDs sollten sich zum Rhythmus synchronisieren. Die Kondensatoren glätten das Signal für einen "tanzenden" Effekt.
5. **Steckbrett-Tipps**: Platziere das Mikrofon auf einer Seite, Dioden/Kondensatoren in der Mitte, LEDs in einer Reihe auf der anderen Seite. Teste mit einem Multimeter auf Durchgang, bevor du die Stromversorgung anschaltest.

Dies erzeugt diese hypnotische Lichtshow ohne ausgefallene Teile. Wenn du ein Potentiometer zur Lautstärkeeinstellung hinzufügen möchtest, baue es einfach in die Mikrofonsignalleitung ein – es regelt die LED-Reaktion herunter, wie du erwähnt hast.

Für vollständige Schaltpläne und Schritte siehe diese Links:

[Simple Sound Reactive LEDs Circuit](https://www.circuits-diy.com/simple-sound-reactive-leds-circuit/)
[Creating an Audio-Reactive LED Circuit (even simpler single-LED version)](https://www.instructables.com/Creating-An-Audio-Reactive-LED-Circuit/)