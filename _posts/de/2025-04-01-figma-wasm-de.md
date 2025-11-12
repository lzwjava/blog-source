---
audio: false
generated: true
lang: de
layout: post
title: Figma Nutzt WebAssembly
translated: true
type: note
---

Figma nutzt WebAssembly (Wasm), um seine Leistung zu steigern, und ist damit ein herausragendes Beispiel dafür, wie diese Technologie webbasierte Anwendungen transformieren kann. Im Kern ist Figma ein kollaboratives Designtool, das hauptsächlich im Browser läuft, und es verwendet WebAssembly, um kritische, leistungsintensive Aufgaben mit nahezu nativer Geschwindigkeit auszuführen. So funktioniert es:

Figma's Engine ist in C++ geschrieben, einer Sprache, die für ihre Geschwindigkeit und Effizienz bekannt ist, aber nicht nativ von Browsern unterstützt wird. Um diese Lücke zu schließen, kompiliert Figma seine C++-Codebasis mit Emscripten, einer Toolchain, die C/C++ in Wasm-Binärdateien umwandelt, in WebAssembly. Diese `.wasm`-Dateien werden dann in den Browser geladen, wo sie die rechenintensiven Aufgaben übernehmen – Dinge wie das Rendern komplexer Vektorgrafiken, das Verwalten großer Designdokumente und das Verarbeiten von Echtzeit-Updates über mehrere Benutzer hinweg.

Ein großer Vorteil dieses Ansatzes ist die **Ladezeit**. Figma hat berichtet, dass der Wechsel zu WebAssembly die Ladezeit im Vergleich zur früheren Verwendung von asm.js (einem JavaScript-Subset für die Ausführung von C++-Code) um mehr als das Dreifache verkürzt hat. Das Binärformat von WebAssembly ist kompakter und schneller zu parsen als JavaScript, und sobald es geladen ist, cached der Browser den kompilierten Maschinencode, sodass nachfolgende Ladevorgänge noch schneller sind. Dies ist entscheidend für Figma, wo Benutzer oft mit riesigen Dateien arbeiten und sofortige Reaktionsfähigkeit erwarten.

Die **Rendering-Engine** ist ein weiterer Schlüsselbereich, in dem WebAssembly glänzt. Figma verwendet WebGL für GPU-beschleunigte Grafiken, aber die Logik dahinter – denken Sie an Kurvenrendering, Maskierung, Unschärfen und Mischmodi – wird vom C++-Code verwaltet, der zu Wasm kompiliert wurde. Dieser Setup umgeht den HTML-Rendering-Pipeline des Browsers und gibt Figma eine fein abgestimmte Kontrolle über Leistung und Konsistenz über verschiedene Plattformen hinweg. Deshalb fühlen sich Zoomen und Schwenken in Figma so flüssig an, selbst bei Tausenden von Ebenen.

**Echtzeit-Kollaboration** profitiert ebenfalls. Figmas Multiplayer-Funktionen basieren auf Conflict-Free Replicated Data Types (CRDTs), um Änderungen sofort zwischen Benutzern zu synchronisieren. Während die CRDT-Logik selbst möglicherweise nicht vollständig in Wasm läuft, verwaltet die C++-gesteuerte Engine den Dokumentstatus und Updates effizient und stellt sicher, dass kollaborative Bearbeitungen das System nicht ausbremsen. Die Geschwindigkeit von WebAssembly trägt dazu bei, dies nahtlos zu halten, selbst bei Dutzenden von Mitwirkenden.

Hier kommt eine hybride Architektur zum Tragen: Die Kern-Engine (C++/Wasm) verwaltet das Dokument und die Leinwand, während die umgebende UI – wie Symbolleisten und Menüs – mit JavaScript (heute TypeScript + React) erstellt wurde. Die beiden kommunizieren über eine Bridge, wobei Wasm Funktionen exportiert, die JavaScript aufrufen kann, und umgekehrt. Diese Aufteilung ermöglicht es Figma, die Leistung dort zu optimieren, wo es am wichtigsten ist, und gleichzeitig die web-native Flexibilität von JavaScript für weniger rechenintensive Aufgaben beizubehalten.

Ein Haken: Figma verwendet WebAssembly nicht einheitlich in allen Browsern. In der Vergangenheit setzte es stärker auf Wasm in Firefox aufgrund früherer Chrome-Bugs (z.B. fehlendes Caching für übersetzten Wasm-Code), obwohl moderne Implementierungen dies wahrscheinlich geglättet haben. Dennoch bleibt die C++-zu-Wasm-Pipeline zentral für seine Architektur.

Kurz gesagt, Figma verwendet WebAssembly, um Desktop-Leistung in den Browser zu bringen, indem es seinen C++-Kern in effiziente Binärdateien kompiliert, die Rendering, Dokumentenverwaltung und Echtzeit-Synchronisierung übernehmen. Es ist ein Lehrbuchbeispiel dafür, wie Wasm einer Web-App ermöglicht, weit über die Leistungsklasse von JavaScript hinaus zu agieren. Möchten Sie mehr über die technischen Details erfahren oder sehen, wie sich dies mit anderen Tools vergleicht?