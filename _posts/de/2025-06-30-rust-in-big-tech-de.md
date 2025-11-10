---
audio: false
generated: true
lang: de
layout: post
title: Rusts Aufstieg in der Big-Tech-Branche
translated: true
type: note
---

Rust gewinnt in der Tech-Branche erheblich an Bedeutung, da es einen starken Fokus auf Speichersicherheit, Leistung und Parallelität legt. Viele große Technologieunternehmen setzen Rust für verschiedene kritische Projekte ein. Hier ist eine Aufschlüsselung einiger prominenter Beispiele:

**1. Amazon (AWS)**
* **Firecracker:** Ein MicroVM, der entwickelt wurde, um Container-Workloads sicher und in großem Maßstab auszuführen; er treibt AWS Lambda und Fargate an.
* **AWS Nitro System:** Wird für die Entwicklung neuer Komponenten verwendet, einschließlich sicherer und isolierter EC2-Umgebungen.
* **Andere Dienste:** Rust wird in Komponenten von Amazon S3, Amazon EC2, Amazon CloudFront und Amazon Route 53 verwendet.
* **Bottlerocket:** Ein Linux-basiertes Container-Betriebssystem, das in Rust geschrieben ist.

**2. Microsoft**
* **Windows-Komponenten:** Microsoft schreibt aktiv Teile von Windows, einschließlich Kernel-Komponenten, in Rust um, um die Sicherheit und Wartbarkeit zu verbessern.
* **Azure-Dienste:** Rust ist in Azure IoT Edge und Kusto (die Kern-Abfrage- und Speicher-Engine für Azure Data Explorer) integriert.
* **`windows-rs`:** Ein Projekt, das das Aufrufen von Windows-APIs mit Rust ermöglicht.

**3. Meta (Facebook)**
* **Interne Source-Control-Tools:** Meta hat Teile ihres internen Source-Control-Systems (Mononoke) in Rust neu aufgebaut, um ihre große Monorepo mit besserer Parallelität und Geschwindigkeit zu verwalten.
* **Diem (ehemals Libra) Blockchain:** Die Blockchain für dieses Kryptowährungsprojekt wurde primär in Rust geschrieben.

**4. Google**
* **Android Open Source Project (AOSP):** Rust wird zunehmend verwendet, um sichere Systemkomponenten in Android zu schreiben, was Speicherfehler in kritischen Funktionen wie Medienverarbeitung und Dateisystemzugriff reduziert.
* **Fuchsia OS:** Ein erheblicher Teil des internen Codes von Fuchsia OS ist in Rust geschrieben.
* **Chromium:** Experimentelle Unterstützung für Rust existiert in Chromium.

**5. Dropbox**
* **Sync Engine:** Rust ersetzte älteren Python- und C++-Code in der Dateisynchronisierungs-Engine von Dropbox, was zu reduzierter CPU-Auslastung, besserer Parallelität und flüssigerer Synchronisation führte.
* **Kern-Dateispeichersystem:** Mehrere Komponenten ihres Kern-Dateispeichersystems sind in Rust geschrieben.

**6. Discord**
* **Backend-Dienste:** Discord verwendet Rust für kritische Backend-Dienste wie Nachrichtenrouting und Presence-Tracking, was die Leistung und Zuverlässigkeit verbessert. Sie wechselten für ihren "Read States"-Service von Go zu Rust, um Latenzspitzen zu vermeiden.
* **Client- und Serverseiten:** Sowohl die Client- als auch die Serverseite von Discords Codebasis haben Rust-Komponenten.

**7. Cloudflare**
* **Pingora:** Ein hochleistungsfähiger Web-Proxy, geschrieben in Rust, um NGINX zu ersetzen, was zu reduzierter CPU-Auslastung und verbessertem Verbindungsmanagement führte.
* **Kern-Edge-Logik:** Rust wird in der Kern-Edge-Logik von Cloudflare als Ersatz für speicherunsichere Sprachen wie C verwendet.
* **Cloudflare Workers:** Unterstützt die serverlose Codebereitstellung mit Rust.

**8. Mozilla**
* **Firefox (Stylo):** Mozilla, der ursprüngliche Schöpfer von Rust, verwendete die Sprache, um Stylo, die CSS-Engine in Firefox, zu bauen, was die Leistung und Sicherheit erheblich verbesserte.
* **Servo:** Eine Prototyp-Webbrowser-Engine, die vollständig in Rust gebaut ist.

**9. npm (Node Package Manager)**
* **Authentifizierungsdienste:** npm verwendete Rust, um Teile seiner Authentifizierungsdienste neu zu schreiben, um die Sicherheit zu verbessern, Last zu bewältigen und Verzögerungen zu reduzieren.

**Weitere bemerkenswerte Anwender und Projekte:**
* **Linux-Kernel:** Rust ist jetzt die zweite offizielle Sprache für die Linux-Kernel-Entwicklung, was sicherere Gerätetreiber und andere Module ermöglicht.
* **Figma:** Ihre Multiplayer-Synchronisierungs-Engine wurde von TypeScript auf Rust umgeschrieben, um die Leistung zu verbessern.
* **1Password:** Bietet ihre neuesten Desktop- und Mobile-Apps mit einer einzigen gemeinsamen Rust-Codebasis.
* **Hugging Face:** Viele Komponenten in ihrem AI-Ökosystem, einschließlich `safetensors`, `tokenizer` und `candle`, sind mit Rust implementiert.
* **Polkadot:** Diese Blockchain-Plattform ist vollständig in Rust für Sicherheit und Geschwindigkeit gebaut.
* **Solana:** Eine weitere hochleistungsfähige Blockchain-Plattform, die Rust nutzt.
* **Brave Browser:** Verwendet Rust in einigen seiner Komponenten.
* **Atlassian:** Verwendet Rust in einem Dienst zur Analyse von Petabytes an Quellcode.
* **Huawei:** Migrierte Teile seiner Codebasis zu Rust für Telekommunikationsgeräte und Infrastruktur-Tools.

Die Übernahme von Rust durch diese großen Technologieunternehmen unterstreicht seine wachsende Bedeutung für den Aufbau zuverlässiger, effizienter und sicherer Software, insbesondere für Systemprogrammierung, Infrastruktur und Hochleistungsanwendungen.