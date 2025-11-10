---
audio: false
generated: true
image: false
lang: fr
layout: post
title: ETH et non ERC-20 pour les transferts Binance
translated: true
type: note
---

Non, vous ne pouvez pas envoyer directement des ETH de Binance en utilisant le réseau ERC-20 vers une adresse Ethereum mainnet de MetaMask.

Voici pourquoi :

* **Ethereum (ETH)** : Ethereum (ETH) lui-même est transféré sur le réseau principal Ethereum. C'est une cryptomonnaie native de la blockchain Ethereum.
* **ERC-20** : ERC-20 est un standard pour les jetons, et non une blockchain spécifique. Les jetons ERC-20 (comme USDT, DAI, etc.) sont des jetons créés sur la blockchain Ethereum, mais ils sont distincts de l'ETH, qui est la monnaie principale du réseau.

Pour clarifier :

* Les transactions **ETH** sur le réseau Ethereum ont lieu sur le mainnet Ethereum, et non en tant que jeton ERC-20.
* Si vous retirez des ETH de Binance, ils seront transférés via le **mainnet Ethereum**, et non via le standard de jeton ERC-20.
* L'**adresse ETH MetaMask** est sur le réseau principal Ethereum, qui est compatible avec l'ETH et les jetons ERC-20, mais vous devez vous assurer de sélectionner le **réseau principal Ethereum** (et non un retrait de jeton ERC-20) lorsque vous retirez des ETH de Binance vers MetaMask.

### Les étapes correctes seraient :

1.  **Retirer des ETH de Binance** : Choisissez le **mainnet Ethereum (ETH)** comme méthode de retrait.
2.  **Recevoir sur MetaMask** : Votre adresse ETH MetaMask est sur le réseau principal Ethereum, et vous recevrez les ETH directement.

### Pour résumer :

* **L'ETH n'est pas un jeton ERC-20** ; c'est la monnaie principale du mainnet Ethereum.
* Lorsque vous retirez des ETH, utilisez l'option **réseau principal Ethereum** à la fois sur Binance et MetaMask.