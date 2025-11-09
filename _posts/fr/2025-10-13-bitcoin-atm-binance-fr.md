---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide de Transfert d'un Distributeur de Bitcoin vers Binance
translated: true
type: note
---

### Comprendre votre demande
Il semble que vous vous interrogiez sur l'utilisation de CoinUnit.io (un service de distributeurs automatiques de Bitcoin) pour « recharger » ou déposer du BTC, sur la sélection du réseau approprié, puis sur l'envoi (retrait) de ce BTC vers votre compte Binance — en particulier, sur le choix entre le réseau standard « Bitcoin » ou « BTC SegWit » sur Binance. Je vais décomposer cela étape par étape, en me basant sur le fonctionnement de ces services, pour vous aider à éviter tout risque tel que la perte de fonds.

### Étape 1 : « Recharger » du BTC sur CoinUnit.io
- CoinUnit.io opère des distributeurs automatiques de Bitcoin où vous pouvez **acheter du BTC en déposant des espèces** (c'est probablement ce que signifie « recharger » dans ce contexte — approvisionner votre portefeuille avec du BTC).
- Le processus est simple à leurs distributeurs (principalement situés à Hong Kong, avec quelques emplacements internationaux) :
  1. Localisez un distributeur via leur site ou leur application.
  2. Sélectionnez « Acheter du Bitcoin ».
  3. Scannez le code QR de votre portefeuille Bitcoin (utilisez un portefeuille mobile comme Electrum, Trust Wallet ou l'application de portefeuille de Binance).
  4. Insérez les espèces (supporte diverses dénominations ; les frais sont généralement de 5 à 10 %, vérifiez sur place).
  5. Le distributeur envoie le BTC directement **à l'adresse Bitcoin de votre portefeuille**.
- **Important** : Les distributeurs CoinUnit.io envoient le BTC exclusivement sur la **blockchain native Bitcoin**. Il n'y a pas de « choix de réseau » ici comme sur les exchanges — c'est toujours le réseau BTC standard. Votre portefeuille le reçoit comme une transaction Bitcoin standard (compatible avec tous les types d'adresses : Legacy commençant par "1", P2SH-SegWit avec "3", ou Native SegWit avec "bc1").
- Aucun guide sur leur site pour l'envoi vers Binance, mais une fois que vous avez le BTC dans votre portefeuille, vous pouvez le transférer.

Si vous vouliez dire vendre du BTC contre des espèces à leurs distributeurs, c'est l'inverse (option « Vendre du Bitcoin »), mais votre demande semble se concentrer sur l'acquisition et l'envoi vers Binance.

### Étape 2 : Envoyer du BTC de votre portefeuille vers Binance
- Après avoir acheté sur CoinUnit.io, vous aurez du BTC dans votre portefeuille personnel. Pour le transférer vers Binance :
  1. Connectez-vous à Binance > Portefeuille > Dépôt > Sélectionnez « BTC » (Bitcoin).
  2. Binance générera une adresse de dépôt et vous demandera de **choisir un réseau**. C'est là que votre question intervient.
- **Avertissement clé** : Le réseau que vous sélectionnez sur Binance **doit correspondre** au réseau que votre portefeuille utilise pour envoyer le BTC. Les incohérences peuvent entraîner une perte permanente de fonds (Binance ne peut pas les récupérer). Étant donné que CoinUnit.io utilise le réseau Bitcoin natif, restez sur les options basées sur Bitcoin sur Binance.

### Étape 3 : Choisir « Bitcoin » ou « BTC SegWit » sur Binance ?
- Binance prend en charge plusieurs réseaux pour les dépôts BTC, mais seuls **les réseaux natifs Bitcoin** sont sûrs pour les transferts depuis un portefeuille standard comme celui que vous utiliseriez à un distributeur CoinUnit.io. Voici une comparaison rapide :

| Option de réseau sur Binance | Description | Adresse Commence Par | Recommandé ? | Pourquoi ? |
|---------------------------|-------------|---------------------|--------------|------|
| **Bitcoin (BTC)** | Réseau Bitcoin standard (souvent Legacy ou P2SH). | "1" ou "3" | ✅ **Oui, option la plus sûre par défaut** | Correspond exactement à ce qu'envoie CoinUnit.io. Risque d'erreur le plus faible ; largement compatible. Les frais sont les frais Bitcoin standard. |
| **BTC (SegWit)** | Native SegWit (bech32) sur le réseau Bitcoin. | "bc1" | ✅ Oui, si votre portefeuille le supporte | Également sur la blockchain Bitcoin — entièrement compatible. Frais légèrement inférieurs et confirmations plus rapides grâce à l'efficacité de SegWit. À utiliser si votre portefeuille génère des adresses "bc1" (par exemple, les portefeuilles modernes comme Electrum). |
| **BEP20 (BSC)** | Binance Smart Chain (BTC wrappé). | Divers (BEP20) | ❌ Non | Mauvaise blockchain — vos BTC seraient perdus. |
| **BEP2** | Binance Chain (BTC wrappé). | "bnb" | ❌ Non | Mauvaise blockchain — fonds perdus. |
| **ERC20** | Réseau Ethereum (BTC wrappé comme WBTC). | "0x" | ❌ Non | Mauvaise blockchain — fonds perdus. |

- **Recommandation** : Optez pour **Bitcoin (BTC)** à moins que votre portefeuille n'utilise spécifiquement des adresses Native SegWit (vérifiez en générant une adresse de réception dans votre application de portefeuille). Les deux sont sûrs pour ce transfert, mais « Bitcoin » est le plus simple et le plus indulgent pour les débutants.
  - Les dépôts sur ces réseaux se confirment en 1-3 blocs (généralement 10-30 minutes), selon l'encombrement du réseau.
  - Dépôt minimum : Généralement 0,0005 BTC (vérifiez les limites actuelles sur Binance).
- Conseil Pro : Effectuez toujours d'abord un petit test de transaction (par exemple, 0,001 BTC) pour confirmer que tout fonctionne avant d'envoyer le montant total.

### Conseils supplémentaires
- **Frais** : CoinUnit.io facture ~5-8 % pour les achats (varie selon l'emplacement). Les frais de réseau Bitcoin pour le transfert vers Binance sont d'environ 1-5 USD (payés depuis votre portefeuille). Les dépôts sur Binance sont gratuits.
- **Sécurité** : Activez l'authentification à deux facteurs (2FA) sur Binance. Utilisez un portefeuille réputé pour le scan au distributeur. Évitez les Wi-Fi publics.
- **En cas de problème** : Contactez le support CoinUnit.io (email/téléphone via leur FAQ) pour l'aide relative aux distributeurs, ou le support Binance pour les questions de dépôt.
- Pour plus de détails, consultez le guide de dépôt officiel de Binance.

Si cela ne correspond pas à ce que vous vouliez dire (par exemple, si « recharger » fait référence à autre chose), fournissez plus de détails pour une meilleure aide !