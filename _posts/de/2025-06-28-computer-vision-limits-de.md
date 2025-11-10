---
audio: false
generated: true
lang: de
layout: post
title: Computersehen bleibt hinter menschlicher Leistung zurück
translated: true
type: note
---

Der Blogbeitrag von Yin Wang argumentiert, dass Computer-Vision-Systeme, selbst fortschrittliche aus dem Jahr 2019, weit davon entfernt waren, menschenähnliche Leistungen zu erbringen. Er behauptet, dass diese Systeme mit grundlegender Objekterkennung (z.B. der Identifizierung eines Autos) zu kämpfen haben und leicht durch adversarial Examples oder geringfügige Bildveränderungen in die Irre geführt werden können, anders als Menschen, die Objekte mühelos erkennen. Wang schlägt vor, dass das Feld seine Fortschritte übertreibt und dass wahrhaft menschenähnliche Computer Vision aufgrund grundlegender Einschränkungen in der Art und Weise, wie diese Systeme Bilder verarbeiten und verstehen, nach wie vor unerreicht bleibt.

### Ist das wahr?
Zum Zeitpunkt der Veröffentlichung des Beitrags im Oktober 2019 hatte Wangs Argumentation basierend auf dem Stand der Computer Vision zu dieser Zeit Berechtigung:

- **Eingeschränkte Generalisierung**: Computer-Vision-Modelle wie Convolutional Neural Networks (CNNs) waren stark auf Mustererkennung innerhalb der Trainingsdaten angewiesen. Sie scheiterten oft daran, auf neue Kontexte zu generalisieren oder Edge Cases gut zu bewältigen, wie Wang beschreibt. Beispielsweise konnten Modelle Objekte falsch klassifizieren, wenn sich Beleuchtung, Blickwinkel oder Hintergrund signifikant änderten.

- **Anfälligkeit für Adversarial Attacks**: Wangs Punkt zu adversarial Examples – Bilder, die subtil verändert wurden, um Modelle fehlzuleiten – war zutreffend. Forschung, wie z.B. von Goodfellow et al. (2014), zeigte, dass kleine, nicht wahrnehmbare Störungen Modelle dazu bringen konnten, Bilder mit hoher Zuversicht falsch zu klassifizieren, was eine Lücke zwischen menschlichem und maschinellem Sehen aufzeigte.

- **Übertriebene Behauptungen**: Der Beitrag kritisiert den Hype um Computer Vision. Im Jahr 2019 zeigten Modelle wie ResNet, YOLO und frühe Transformer zwar beeindruckende Ergebnisse in Benchmarks (z.B. ImageNet), doch handelte es sich dabei um kontrollierte Datensätze. Anwendungen in der realen Welt offenbarten oft Schwächen, wie z.B. Fehlidentifikationen in autonomen Fahrzeugen oder Gesichtserkennungssystemen.

Allerdings ist der Ton des Beitrags absolut und behauptet, „es gibt keine menschenähnliche Computer Vision“. Dies übersieht Fortschritte in bestimmten Aufgaben. Zum Beispiel:
- **Aufgabenspezifischer Erfolg**: Bis 2019 übertrafen Computer-Vision-Systeme die menschliche Leistung in eng umrissenen Aufgaben, wie der Klassifizierung bestimmter medizinischer Bilder (z.B. der Erkennung von diabetischer Retinopathie) oder der Erkennung spezifischer Objekte in kontrollierten Umgebungen.
- **Fortschritte seit 2019**: Bis 2025 haben Fortschritte wie Vision Transformer (z.B. ViT, CLIP) und großskalige multimodale Modelle (z.B. GPT-4o, DALL·E 3) die Lücke verkleinert. Diese Modelle verarbeiten vielfältigere Eingaben, generalisieren besser über Kontexte hinweg und integrieren Sprache und Vision für verbessertes Reasoning. Dennoch replizieren sie nicht vollständig die Robustheit, das Kontextbewusstsein oder das intuitive Verständnis des menschlichen Sehens.

### Kritische Bewertung
Wangs Kernaussage – dass Computer Vision im Jahr 2019 nicht menschenähnlich war – ist weitgehend zutreffend. Den Modellen fehlte die Generalisierungsfähigkeit, Robustheit und das intuitive Verständnis des menschlichen Sehens. Seine Abweisung der Fortschritte könnte jedoch übermäßig pessimistisch sein, da seitdem bedeutende Schritte gemacht wurden. Selbst im Jahr 2025, während Computer Vision in spezifischen Domänen hervorragend abschneidet, bleibt sie in offenen Weltszenarien hinter der menschlichen Wahrnehmung zurück, aufgrund von Problemen wie:
- **Kontextuelles Reasoning**: Menschen integrieren sensorische Daten mühelos mit Weltwissen; Maschinen tun sich damit schwer.
- **Edge Cases**: Modelle können in seltenen oder neuartigen Situationen versagen, in denen Menschen sich schnell anpassen.
- **Energieeffizienz**: Das menschliche Sehen ist weitaus energieeffizienter als Computermodelle.

Der Beitrag bleibt relevant als Kritik an der Übertreibung von KI-Fähigkeiten, berücksichtigt aber nicht den raschen Fortschritt auf diesem Gebiet. Keine einzelne Quelle bestätigt, dass bis 2025 „menschenähnliches“ Sehen erreicht wurde, aber die Lücke hat sich erheblich verkleinert.[](https://yinwang0.wordpress.com/2019/10/20/human-level-computer-vision/)