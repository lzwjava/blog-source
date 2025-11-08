---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Union ZK Interchain-Infrastrukturprotokoll
translated: true
type: note
---

### Übersicht
Das GitHub-Repository unter [https://github.com/unionlabs/union](https://github.com/unionlabs/union) ist die offizielle Open-Source-Codebasis für **Union**, ein Zero-Knowledge (ZK) Infrastrukturprotokoll, entwickelt von Union Labs. Union zielt darauf ab, nahtlose, sichere Interoperabilität zwischen verschiedenen Blockchains zu ermöglichen, sodass Assets und Daten kettenübergreifend bewegt werden können, ohne traditionelle Bridges, Verwahrer oder vertrauenswürdige Vermittler. Es nutzt ZK-Beweise, um Transaktionen und Zustandsübergänge zu verifizieren, und konzentriert sich auf Skalierbarkeit, Privatsphäre und Komponierbarkeit im Multi-Chain-Ökosystem.

### Wichtige Funktionen
- **ZK-Light Client**: Verwendet Zero-Knowledge-Beweise für eine leichtgewichtige, vertrauensminimierte Verifizierung von Blockchain-Zuständen und Konsens, um die Abhängigkeit von schweren Relayers zu verringern.
- **Interoperabilitäts-Primitive**: Unterstützt Cross-Chain-Messaging, Asset-Transfers (z.B. Token, NFTs) und die Übertragung beliebiger Daten zwischen EVM-kompatiblen Chains und darüber hinaus.
- **Modulare Architektur**: Erbaut mit Cosmos SDK und Tendermint für den Konsens, aber erweiterbar für andere Frameworks. Es beinhaltet Komponenten wie den Union Relayer, Proof-Generatoren und Verifizierer-Verträge.
- **Sicherheitsfokus**: Legt Wert auf kryptografische Primitive wie Groth16-Beweise und BLS-Signaturen, um häufige Bridge-Exploits zu verhindern.

### Entwicklungsstatus (Stand November 2025)
- Das Repo wird aktiv gepflegt, mit kürzlichen Commits, die sich auf Testnet-Integrationen konzentrieren (z.B. Union Testnet v2, Mitte 2025 gestartet).
- Es hat über 500 Sterne, Beiträge von 50+ Entwicklern und ist unter der Apache-2.0-Lizenz lizenziert.
- Die Dokumentation enthält Setup-Anleitungen zum Betreiben von Nodes, zum Bereitstellen von Verträgen und zur Integration mit Wallets wie MetaMask.

### Anwendungsfälle
- DeFi-Protokolle, die Liquidität über die Ethereum-, Solana- und Cosmos-Ökosysteme hinweg bridgen.
- Gaming- und NFT-Projekte, die kettenübergreifende Übertragbarkeit benötigen.
- Enterprise-Anwendungen, die private, verifizierbare Datenaustausch zwischen Ledgern erfordern.

Wenn Sie ein Entwickler sind, können Sie das Repo klonen und mit `make install` für die Abhängigkeiten beginnen, dann `make build` zum Kompilieren. Für mehr Informationen, lesen Sie den [docs-Ordner](https://github.com/unionlabs/union/tree/main/docs) oder die Website von Union Labs.

[Union Labs Website](https://union.build/)  
[Union Whitepaper](https://union.build/whitepaper)  
[GitHub Repo](https://github.com/unionlabs/union)