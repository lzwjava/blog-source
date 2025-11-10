---
audio: false
generated: true
lang: de
layout: post
title: Die wichtigsten Mitwirkenden und Gründer von Rust
translated: true
type: note
---

Das Rust-Ökosystem ist lebendig und wächst, wobei viele Einzelpersonen und Organisationen bedeutende Beiträge leisten. Hier ist eine Aufschlüsselung der wichtigsten Mitwirkenden, Programmierer, einflussreichen Projekte und Gründer:

### Rust-Gründer

Der Hauptgründer der Programmiersprache Rust ist:

*   **Graydon Hoare:** Er startete Rust als persönliches Projekt während seiner Arbeit bei Mozilla im Jahr 2006, angetrieben von dem Wunsch nach einer Systemprogrammiersprache, die die Speichersicherheitsprobleme in C und C++ anspricht. Er legte die grundlegenden Prinzipien der Sprache fest.

Weitere Schlüsselfiguren, die in der frühen Entwicklung und Evolution von Rust bei Mozilla entscheidend waren, sind:

*   **Niko Matsakis:** Ein langjähriger Mitwirkender am Rust-Compiler und am Sprachdesign, insbesondere am Borrow Checker.
*   **Patrick Walton**
*   **Felix Klock**
*   **Manish Goregaokar**

### Top-Mitwirkende & Programmierer im Rust-Ökosystem (Hoch anerkannt, Open-Source-Arbeit)

Es ist schwierig, eine definitive "Top 30" zu erstellen, da die Beiträge vielfältig sind und auf viele Einzelpersonen und Teams verteilt sind. Hier sind jedoch einige hoch anerkannte Programmierer und wichtige Mitwirkende, die für ihre Open-Source-Arbeit und ihren Einfluss auf die Rust-Community bekannt sind:

*   **Steve Klabnik:** Ein produktiver Autor, Pädagoge und Core-Team-Mitglied. Er ist bekannt für seine Beiträge zur Rust-Dokumentation (z.B. "The Rust Programming Language Book") und seine Advocacy-Arbeit für Rust. Er arbeitet jetzt bei Oxide Computer Company und wendet Rust auf Hardware/Software-Systeme an.
*   **Nicholas Matsakis (nikomatsakis):** Entscheidend am Design und der Implementierung des Rust-Compilers beteiligt, insbesondere am Borrow Checker, der zentral für Rusts Speichersicherheitsgarantien ist. Er arbeitet bei AWS an Rust.
*   **Mara Bos:** Ein prominentes Mitglied des Rust Libraries Team und aktiv in der Rust-Community, das zu verschiedenen Aspekten der Standardbibliothek und der Sprachentwicklung beiträgt. Sie ist auch Mitbegründerin von Fusion Engineering.
*   **Carol Nichols:** Eine weitere Schlüsselfigur in der Rust-Community, Co-Autorin von "The Rust Programming Language Book" und Mitglied im Vorstand der Rust Foundation. Sie setzt sich aktiv für die Verbreitung und Nachhaltigkeit von Rust ein.
*   **Jon Gjengset (jonhoo):** Bekannt für seine tiefgehenden Einblicke in die Interna von Rust, insbesondere Nebenläufigkeit, und für seinen exzellenten Bildungscontent und Streams, die vielen helfen, fortgeschrittene Rust-Konzepte zu lernen.
*   **Alex Crichton:** Ein bedeutender Mitwirkender an verschiedenen Rust-Projekten, einschließlich `rust-lang/rust` und `crates.io-index`, der eine entscheidende Rolle für die Infrastruktur des Ökosystems spielt.
*   **Ralf Jung:** Bekannt für seine Arbeit an Miri, einem UBM (Undefined Behavior Machine) Interpreter für Rust, der bei der Identifizierung von undefiniertem Verhalten in Rust-Code hilft.
*   **Bryan Cantrill:** CTO und Mitbegründer der Oxide Computer Company, ein starker Befürworter von Rust in der Systemprogrammierung und Industrie.
*   **Josh Triplett:** Ein langjähriger Rust-Mitwirkender und Core-Team-Mitglied, beteiligt an vielen Aspekten der Sprachentwicklung.
*   **Armin Ronacher (mitsuhiko):** Schöpfer des Python Flask-Frameworks, er wurde zu einer bedeutenden treibenden Kraft für die Rust-Adaption, insbesondere bei Sentry.
*   **Andrew Gallant (BurntSushi):** Bekannt für hochoptimierte und weit verbreitete Rust-Crates wie `ripgrep` (eine schnelle grep-Alternative) und `regex`.
*   **Syrus Akbary:** Schöpfer von Wasmer, einer WebAssembly-Laufzeitumgebung, die mit Rust betrieben wird.
*   **Frank McSherry:** Bekannt für seine Arbeit an Differential Dataflow und anderen Projekten, die fortgeschrittene Nebenläufigkeit und Datenverarbeitung in Rust erforschen.
*   **Jeremy Soller:** Seine Arbeit bei System76 und jetzt bei Oxide Computer Company demonstriert die Tauglichkeit von Rust bis hinunter auf die Betriebssystemebene.
*   **Guillaume Gomez:** Ein produktiver Mitwirkender am Rust-Compiler und am GTK-RS-Projekt (Rust-Bindings für GTK).
*   **Pietro Albini:** Trägt wesentlich zur entscheidenden Rust-Infrastruktur bei und ist Mitglied des Rust Core Teams.
*   **Dirkjan Ochtman:** Für die Wartung von `rustls` und `quinn`, wichtige Bibliotheken für sichere Kommunikation in Rust.
*   **Gary Guo:** Für die Wartung von Rust for Linux, einer kritischen Bemühung, Rust in den Linux-Kernel zu integrieren.
*   **Manish Goregaokar:** Ein Google Senior Software Engineer, trägt zu verschiedenen Rust-Projekten bei, einschließlich Unicode-bezogener Arbeit.

### Top Open-Source Rust-Projekte (Hoch einflussreich)

Viele Open-Source-Projekte zeigen Rusts Stärken und haben einen bedeutenden Einfluss:

1.  **Rust Lang/Rust (der Rust-Compiler und die Standardbibliothek):** Das Kernprojekt selbst, das alle befähigt, zuverlässige und effiziente Software zu bauen.
2.  **Tauri Apps/Tauri:** Ein Framework zum Erstellen kleinerer, schnellerer und sicherer Desktop- und Mobil-Anwendungen mit einem Web-Frontend, ähnlich wie Electron, aber effizienter.
3.  **RustDesk/RustDesk:** Eine Open-Source-Remote-Desktop-Anwendung, eine beliebte Alternative zu TeamViewer.
4.  **Alacritty/Alacritty:** Ein plattformübergreifender OpenGL-Terminalemulator, bekannt für seine hohe Leistung.
5.  **Tokio/Tokio:** Die grundlegende asynchrone Laufzeitumgebung für Rust, weit verbreitet für den Bau hochperformanter Netzwerkanwendungen.
6.  **Hyper/Hyper:** Eine schnelle und korrekte HTTP-Bibliothek für Rust, oft in Verbindung mit Tokio verwendet.
7.  **Actix/Actix-web:** Ein leistungsstarkes, schnelles und hochgradig nebenläufiges Web-Framework für Rust.
8.  **Axum/Axum:** Ein Webanwendungs-Framework, das mit Tokio und Hyper gebaut wurde und Ergonomie und starke Typisierung betont.
9.  **Ripgrep (BurntSushi/ripgrep):** Ein zeilenorientiertes Suchtool, das Verzeichnisse rekursiv nach einem Regex-Muster durchsucht und deutlich schneller als `grep` ist.
10. **Bat (sharkdp/bat):** Ein `cat(1)`-Klon mit Flügeln, der Syntax-Hervorhebung, Git-Integration und mehr bietet.
11. **Fd (sharkdp/fd):** Eine einfache, schnelle und benutzerfreundliche Alternative zu `find`.
12. **Meilisearch/Meilisearch:** Eine leistungsstarke, schnelle und relevante Suchmaschine.
13. **Polars/Polars:** Eine blitzschnelle DataFrame-Bibliothek, oft als Rust-Alternative zu Pandas für Datenmanipulation gesehen.
14. **BevyEngine/Bevy:** Ein erfrischend einfacher datengesteuerter Game Engine, gebaut in Rust.
15. **Helix Editor/Helix:** Ein moderner modaler Texteditor, inspiriert von Neovim und Kakoune, geschrieben in Rust.
16. **Nushell/Nushell (oder Nu):** Eine moderne Shell, die darauf abzielt, Programmierkonzepte in die Kommandozeile zu bringen.
17. **Deno/Deno:** Eine sichere Laufzeitumgebung für JavaScript und TypeScript, gebaut mit Rust und V8.
18. **Firecracker MicroVM/Firecracker:** Entwickelt von AWS, eine leichtgewichtige Virtualisierungstechnologie, die für Serverless Computing verwendet wird.
19. **Crates.io:** Das offizielle Paket-Registry für die Programmiersprache Rust, essentiell für das Ökosystem.
20. **Rustlings (rust-lang/rustlings):** Kleine Übungen, um Benutzer daran zu gewöhnen, Rust-Code zu lesen und zu schreiben, unglaublich wertvoll für Anfänger.
21. **Yewstack/Yew:** Ein modernes Rust-Framework zum Erstellen clientseitiger Webanwendungen mit WebAssembly.
22. **DioxusLabs/Dioxus:** Eine weitere beliebte deklarative UI-Bibliothek für Rust zum Erstellen plattformübergreifender Anwendungen.
23. **Servo/Servo:** Ein hochperformanter, paralleler Browser-Engine, geschrieben in Rust, entwickelt von Mozilla und später an die Linux Foundation übertragen.
24. **Rocket/Rocket:** Ein Web-Framework für Rust, bekannt für seine Typsicherheit und Entwicklererfahrung.
25. **Solana/Solana:** Eine hochperformante Blockchain-Plattform, mit einem signifikanten Teil ihrer Kernkomponenten, die in Rust geschrieben sind.
26. **Substrate/Substrate:** Ein Framework zum Bauen benutzerdefinierter Blockchains, das ebenfalls stark Rust nutzt.
27. **Wasmtime/Wasmtime:** Eine eigenständige JIT-artige Laufzeitumgebung für WebAssembly und WASI (WebAssembly System Interface).
28. **Delta (dandavison/delta):** Ein Syntax-hervorhebender Pager für `diff`-, `git`- und `merge`-Ausgaben.
29. **Spotify TUI (Rigellute/spotify-tui):** Eine Terminal-Benutzeroberfläche für Spotify.
30. **mdBook (rust-lang/mdBook):** Ein Kommandozeilen-Tool zum Erstellen von Büchern aus Markdown-Dateien, verwendet für viele Rust-Projekte, einschließlich "The Rust Programming Language Book."

Diese Liste ist nicht vollständig, und das Rust-Ökosystem entwickelt sich ständig weiter, wobei regelmäßig neue und einflussreiche Projekte entstehen. Die Stärke der Community liegt in ihrer kollaborativen Natur und der hohen Qualität ihrer Open-Source-Beiträge.