---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Lignes directrices pour l'intégration du système de paiement accéléré
translated: true
type: note
---

Le système de paiement rapide (FPS) de Hong Kong, exploité par Hong Kong Interbank Clearing Limited (HKICL) sous la supervision de l'Autorité monétaire de Hong Kong (HKMA), ne fournit pas de SDK public pour l'intégration par les banques. L'intégration s'effectue via une connectivité directe à l'infrastructure FPS, les spécifications techniques étant partagées de manière privée avec les banques participantes (appelées Settlement Participants) durant le processus d'onboarding. Ces spécifications guident les banques pour l'adaptation de leurs systèmes afin d'obtenir l'accès, mais il n'existe pas de SDK prêts à l'emploi ou de kits de développement mentionnés dans la documentation officielle.

Concernant les API, le FPS lui-même ne propose pas actuellement d'API dédiées pour une intégration externe ou tierce. Cependant, il s'aligne sur le cadre plus large de l'Open API Framework de la HKMA pour le secteur bancaire de Hong Kong (introduit en 2018 et mis à jour par phases jusqu'en 2025), qui encourage les banques à exposer certaines fonctions via des API pour les fournisseurs de services tiers (par exemple, pour les informations de compte ou l'initiation de paiement). Les transactions FPS peuvent utiliser ce cadre indirectement pour des fonctionnalités comme l'initiation de paiement, mais aucune API spécifique au FPS n'est encore disponible — l'accès reste restreint sur une base de besoin de connaître pour des raisons de sécurité et de réglementation. La HKMA continue de surveiller la situation et pourrait étendre le support des API à l'avenir.

### Détails clés de l'intégration pour les banques
- **Méthodes de connectivité** : Les banques se connectent en mode temps réel via la messagerie IBM MQ pour un traitement instantané, ou en mode batch via des transferts de fichiers (par exemple, sur le réseau sécurisé ICLNET de HKICL). Le système fonctionne 24h/24 et 7j/7.
- **Normes de messagerie** : Toutes les communications utilisent le format ISO 20022, prenant en charge les données riches, les caractères chinois et l'interopérabilité.
- **Processus d'onboarding** : Les banques s'inscrivent auprès de la HKMA (pour le HKD) ou de la Bank of China (Hong Kong) pour le RMB, signent les accords FPS Rules, adaptent leurs systèmes aux spécifications fournies, subissent les tests de HKICL et deviennent opérationnelles. Toutes les banques agréées doivent participer en tant que Settlement Participants directs.
- **Autres fonctionnalités** : Prend en charge les proxy IDs (par exemple, téléphone/email), les codes QR (norme EMV) et les transferts multi-devises (HKD/RMB). L'authentification suit les directives à deux facteurs de la HKMA, les banques fixant leurs propres limites de transaction.

Pour les spécifications techniques détaillées, les banques doivent contacter directement HKICL lors de leur inscription, car elles ne sont pas téléchargeables publiquement.

[Système de paiement rapide (FPS) - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/financial-market-infrastructure/faster-payment-system-fps/)  
[Documentation du système - HKICL FPS](https://fps.hkicl.com.hk/eng/fps/about_fps/scheme_documentation.php)  
[Étude de cas Banque Mondiale sur le FPS : Hong Kong](https://fastpayments.worldbank.org/sites/default/files/2021-09/World_Bank_FPS_Hong_Kong_SAR_China_FPS_Case_Study.pdf)  
[Open API Framework pour le secteur bancaire - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/fintech/open-application-programming-interface-api-for-the-banking-sector/)