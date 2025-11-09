---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Présentation du gestionnaire d'accès réseau Cisco AnyConnect
translated: true
type: note
---

Cisco AnyConnect Secure Mobility Client est une suite de modules logiciels qui fournissent un accès VPN sécurisé, une sécurité réseau et des fonctionnalités de poste de travail basées sur des stratégies. L'un des modules optionnels de cette suite est **Cisco Network Access Manager (NAM).**

### Fonctionnalités de Cisco AnyConnect NAM
- **Gestion des connexions réseau** : NAM remplace les gestionnaires de réseau natifs de Windows (sans fil et filaire). Il gère la configuration, la connexion et la sécurisation des réseaux filaires et sans fil.
- **Prise en charge avancée du 802.1X** : Fournit une **authentification 802.1X** complète pour les connexions réseau filaires et sans fil (EAP-TLS, PEAP, EAP-FAST, etc.), souvent utilisée dans les environnements d'entreprise où une authentification par certificat ou une vérification de la posture du poste est requise.
- **Application des stratégies** : Les administrateurs peuvent définir des stratégies qui déterminent comment les appareils des utilisateurs finaux se connectent aux réseaux, en priorisant les exigences de sécurité, en définissant les SSID autorisés ou en restreignant les connexions non sécurisées.
- **Comportement cohérent sur toutes les plateformes** : Il offre un contrôle centralisé afin que les utilisateurs bénéficient de la même expérience d'accès au réseau, quel que soit l'ordinateur utilisé.

### Points clés à noter
- **Plateformes prises en charge** : Historiquement, NAM n'était pris en charge que sur Windows. Cisco a abandonné la prise en charge de NAM à partir des versions ultérieures d'AnyConnect (à partir de la v4.9 et suivantes), car les gestionnaires de réseau natifs des systèmes d'exploitation (Windows Native Wi-Fi, le supplicant macOS, etc.) sont devenus plus robustes.
- **Utilisation typique** : Principalement déployé dans les entreprises, les universités ou les réseaux gouvernementaux qui nécessitent une connexion sécurisée par certificat au Wi-Fi ou au LAN filaire avant ou pendant la connexion au système.

👉 En bref : **Cisco AnyConnect NAM (Network Access Manager)** est un gestionnaire de connexion réseau avancé qui remplace le supplicant natif de Windows pour gérer les connexions filaires/sans fil sécurisées en utilisant l'authentification 802.1X et des stratégies définies par l'entreprise.

---

Souhaitez-vous que j'explique également **comment NAM se positionne par rapport au module VPN AnyConnect plus couramment utilisé** (étant donné que la plupart des gens ne connaissent aujourd'hui que la partie VPN) ?