---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Protocole d’Infrastructure Interchaînes Union ZK
translated: true
type: note
---

### Aperçu
Le dépôt GitHub à l'adresse [https://github.com/unionlabs/union](https://github.com/unionlabs/union) est la base de code open-source officielle pour **Union**, un protocole d'infrastructure à connaissance zéro (ZK) développé par Union Labs. Union vise à permettre une interopérabilité transparente et sécurisée entre différentes blockchains, permettant aux actifs et aux données de circuler entre les chaînes sans ponts traditionnels, dépositaires ou intermédiaires de confiance. Il utilise des preuves ZK pour vérifier les transactions et les transitions d'état, en se concentrant sur l'évolutivité, la confidentialité et la composabilité dans l'écosystème multi-chaînes.

### Fonctionnalités principales
- **Client Léger ZK** : Utilise des preuves à connaissance zéro pour une vérification légère et minimisant la confiance des états et du consensus de la blockchain, réduisant la dépendance aux relais lourds.
- **Primitives d'Interopérabilité** : Prend en charge la messagerie inter-chaînes, les transferts d'actifs (par exemple, jetons, NFT) et le passage de données arbitraires entre les chaînes compatibles EVM et au-delà.
- **Architecture Modulaire** : Construit avec Cosmos SDK et Tendermint pour le consensus, mais extensible à d'autres frameworks. Il comprend des composants tels que le relais Union, les générateurs de preuves et les contrats de vérification.
- **Priorité à la Sécurité** : Met l'accent sur les primitives cryptographiques comme les preuves Groth16 et les signatures BLS pour prévenir les exploits courants des ponts.

### État du Développement (en novembre 2025)
- Le dépôt est activement maintenu, avec des commits récents se concentrant sur les intégrations de testnet (par exemple, Union Testnet v2 lancé mi-2025).
- Il compte plus de 500 étoiles, des contributions de plus de 50 développeurs, et est sous licence Apache-2.0.
- La documentation comprend des guides d'installation pour exécuter des nœuds, déployer des contrats et s'intégrer avec des portefeuilles comme MetaMask.

### Cas d'Utilisation
- Protocoles DeFi reliant la liquidité entre les écosystèmes Ethereum, Solana et Cosmos.
- Projets de jeux et NFT nécessitant une portabilité inter-chaînes.
- Applications d'entreprise nécessitant un partage de données privé et vérifiable entre registres.

Si vous êtes un développeur, vous pouvez cloner le dépôt et commencer par `make install` pour les dépendances, puis `make build` pour compiler. Pour plus d'informations, consultez le [dossier docs](https://github.com/unionlabs/union/tree/main/docs) ou le site d'Union Labs.

[Site Web d'Union Labs](https://union.build/)  
[Livre Blanc d'Union](https://union.build/whitepaper)  
[Dépôt GitHub](https://github.com/unionlabs/union)