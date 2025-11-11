---
audio: false
generated: true
lang: de
layout: post
title: HTTP Content-Length Header
translated: true
type: note
---

Die Einheit des **Content-Length**-Headers im HTTP-Protokoll ist **Bytes**.

Im HTTP wird der **Content-Length**-Header verwendet, um die Größe des Antwortkörpers anzugeben, den der Server an den Client sendet. Diese Größe wird als Dezimalzahl angegeben, die die Anzahl der Bytes (oder Oktetts, wobei ein Oktett 8 Bits entspricht) im Nachrichtenköper repräsentiert. Gemäß der HTTP/1.1-Spezifikation (RFC 7230, Abschnitt 3.3.2) gibt das **Content-Length**-Header-Feld explizit die Größe des Nachrichtenköpers in Oktetts an, was bestätigt, dass die Einheit Bytes ist.

Zum Beispiel bedeutet im gegebenen Fall, in dem der Header `'content-length': '130700923'` lautet, dass der Antwortkörper **130.700.923 Bytes** lang ist. Um eine Größenvorstellung zu geben: Das sind ungefähr **124,6 Megabyte (MB)**, da 1 MB ungefähr 1.048.576 Bytes (2^20 Bytes) entspricht. Dies ist eine plausible Größe für eine große Datei oder eine Datenübertragung in einer HTTP-Antwort.

Um weiter zu präzisieren:
- Der Wert ist eine ganze Zahl, keine gebrochene Zahl, was Einheiten wie Kilobytes oder Megabytes direkt ausschließt.
- Im HTTP wird der Körper als eine Folge von Bytes übertragen, und **Content-Length** entspricht der exakten Anzahl von Bytes, die der Client erwarten sollte.
- Selbst in anderen Versionen wie HTTP/2, bei der Framing anstelle eines einzelnen **Content-Length**-Headers verwendet wird, wird die Nutzlastgröße immer noch in Bytes gemessen.

Somit ist die Einheit von **Content-Length** im HTTP-Protokoll eindeutig **Bytes**.