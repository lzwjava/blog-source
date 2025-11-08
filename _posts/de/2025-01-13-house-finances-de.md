---
audio: false
generated: false
image: false
lang: de
layout: post
title: Verfolgung unserer Haushaltsfinanzen
translated: true
type: post
---

Kürzlich habe ich ein Markdown-Dokument erstellt, um die finanziellen Transaktionen unseres Hauses zu verfolgen.

Das Haus gehört meiner Frau und mir. Meine Eltern haben uns Geld gegeben, und wir haben Geld von meiner Schwester und meinem Onkel mütterlicherseits geliehen. Obwohl mein Onkel mütterlicherseits mir Geld geschickt hat, hat mein Vater diesen Betrag später zurückgezahlt.

Wir haben 50% des Gesamtpreises unseres Hauses als Anzahlung gezahlt, und die andere Hälfte haben wir von der Agricultural Bank of China geliehen. Der Vertrag läuft über 20 Jahre, und der derzeitige Zinssatz beträgt 3,65%.

Als ich arbeitslos war, haben meine Frau und mein Vater mir Mittel zur Verfügung gestellt, um die monatlichen Hypothekenzahlungen zu decken. Folglich gibt es viele Transaktionen, die damit verbunden sind.

Ich verwende die China Merchants Bank als meine primäre Bank. Die China Merchants Bank ermöglicht das Filtern von Transaktionen nach eingehenden oder ausgehenden Zahlungen und nach einem Mindestbetrag. Sie unterstützt auch das Filtern nach Schlüsselwörtern, was sehr hilfreich ist.

Ein weiterer hilfreicher Aspekt ist die Verbreitung von KI. Sie kann ebenfalls bei dieser Aufgabe helfen. Mit KI-gestützter OCR, insbesondere Grok, konnte ich Text aus den Transaktionsaufzeichnungen mit dem Guangzhou Electric Power Bureau extrahieren.

Da die spätere Tabelle auf früheren Zahlen basiert, ist es besser, die Zahlen zuerst zu überprüfen, um sicherzustellen, dass alles korrekt ist, bevor man fortfährt.

Der folgende Code hilft dabei, ein PDF aus dem Markdown zu generieren. Er hat einige spezielle Einstellungen, um die Darstellung chinesischer Zeichen in PDFs zu unterstützen.

```python
import os
import subprocess

# Konfiguration
CJK_FONT = "Heiti SC"
GEOMETRY = "margin=1in"
input_markdown_path = "mortgage.md"  # Ersetzen Sie dies durch Ihre Eingabe-Markdown-Datei
output_pdf_path = "mortgage.pdf"    # Ersetzen Sie dies durch Ihre gewünschte Ausgabe-PDF-Datei

# Überprüfen, ob die Eingabedatei existiert
if not os.path.exists(input_markdown_path):
    raise Exception(f"Eingabedatei existiert nicht: {input_markdown_path}")

# Pandoc-Befehl konstruieren
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]

# Pandoc-Befehl ausführen
try:
    subprocess.run(command, check=True)
    print(f"PDF erfolgreich generiert: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"Fehler beim Generieren des PDFs: {e}")
```