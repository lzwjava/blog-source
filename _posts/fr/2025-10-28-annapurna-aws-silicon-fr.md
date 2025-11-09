---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Annapurna Labs : Les Puce Sur Mesure d'AWS
translated: true
type: note
---

### Qu’est-ce qu’Annapurna Labs ?

**Annapurna Labs** est une société israélienne de semi-conducteurs spécialisée dans les **processeurs hautes performances et écoénergétiques** pour le cloud computing, la mise en réseau, le stockage et les charges de travail d'IA. Elle a été **acquise par Amazon en janvier 2015** pour un montant estimé à environ 350–370 millions de dollars et opère désormais comme une filiale à part entière d'**Amazon Web Services (AWS)**.

Annapurna Labs conçoit des **silicon personnalisé** qui alimente une grande partie de l'infrastructure AWS, permettant à Amazon de réduire sa dépendance à l'égard de fournisseurs de puces tiers comme Intel, Broadcom et NVIDIA pour certaines charges de travail.

---

### Principales puces conçues par Annapurna Labs (utilisées dans AWS)

| Famille de puces | Type | Caractéristiques principales | Cas d'utilisation principal AWS |
|-------------|------|--------------|-----------------------|
| **Alpine** | SoC basé sur ARM | Processeurs ARMv8 multi-cœurs, faible consommation, mise en réseau/stockage intégrés | Premières instances EC2, contrôleurs de stockage |
| **Graviton** | Processeur basé sur ARM | Cœurs 64-bit ARM Neoverse (conçus par AWS), nombre de cœurs élevé, DDR5, PCIe Gen4/5 | **Instances EC2 Graviton** (calcul à usage général) |
| **Nitro** | SmartNIC / Décharge | Processeurs ARM + accélérateurs personnalisés pour virtualisation, sécurité, stockage, mise en réseau | **Système EC2 Nitro**, EBS, VPC, décharge de sécurité |
| **Inferentia** | Inférence IA | Traitement tensoriel haut débit, faible latence, cœurs neuronaux | **Instances EC2 Inf1/Inf2** pour l'inférence ML |
| **Trainium** | Entraînement IA | Évolutif pour les grands modèles de langage, bande passante mémoire élevée, interconnect NeuronLink | **Instances EC2 Trn1/Trn2** pour l'entraînement des LLM |

---

### Familles de puces phares (Actualisé en 2025)

#### 1. **AWS Graviton (Processeur)**
- **Architecture** : Cœurs personnalisés basés sur ARM Neoverse (pas des modèles standard)
- **Générations** :
  - **Graviton1** (2018) : 16 cœurs ARMv8, utilisé dans les instances A1
  - **Graviton2** (2020) : 64 cœurs Neoverse N1, ~40 % de perf/prix en plus par rapport au x86
  - **Graviton3** (2022) : Neoverse V1, DDR5, bfloat16, jusqu'à 60 % de perf en plus que Graviton2
  - **Graviton4** (2024) : Neoverse V2, 96 cœurs, 2,7x de perf/W par rapport à Graviton3
- **Utilisation** : Alimente **~30–40 % des charges de travail EC2 AWS** (en particulier les conteneurs, microservices, bases de données)

#### 2. **AWS Inferentia (Inférence IA)**
- **Inferentia2** (2023) : Performances 4x supérieures à Inferentia1, supporte FP16/BF16/INT8
- Optimisé pour l'**inférence en temps réel** (moteurs de recommandation, reconnaissance vocale, vision par ordinateur)
- Utilisé dans **SageMaker**, **EC2 Inf2**

#### 3. **AWS Trainium (Entraînement IA)**
- **Trainium2** (annoncé 2024, livraison 2025) : Performances d'entraînement 4x supérieures à Trainium1
- Conçu pour concurrencer le **NVIDIA H100** pour l'entraînement des LLM
- Prend en charge les **modèles à billions de paramètres**, mémoire à haute bande passante (HBM)

#### 4. **Système Nitro (SmartNIC / DPU)**
- SoC ARM personnalisés avec accélérateurs matériels
- Décharge l'hyperviseur, la mise en réseau, le stockage, le chiffrement
- Permet des **performances bare-metal dans des environnements virtualisés**

---

### Pourquoi Annapurna est important

- **Coût et Efficacité** : AWS revendique **jusqu'à 40 % de perf/prix en plus** par rapport au x86
- **Intégration Verticale** : Amazon contrôle le silicon → innovation plus rapide, coûts réduits
- **Poussée de l'IA** : Trainium/Inferentia concurrencent directement la domination de NVIDIA dans l'IA cloud
- **Résilience de la Chaîne d'Approvisionnement** : Réduit la dépendance à une chaîne d'approvisionnement exclusivement Intel/TSMC

---

### Résumé

> **Annapurna Labs = L'arme secrète en silicon d'AWS.**  
> Ils construisent les **processeurs Graviton basés sur ARM**, **Inferentia (inférence)**, **Trainium (entraînement)** et les **puces de décharge Nitro** — tous optimisés pour le cloud.  
> Ceux-ci alimentent des services AWS **moins chers, plus rapides et plus écologiques** et sont une raison clé pour laquelle AWS peut proposer des prix inférieurs à ceux de ses concurrents tout en développant l'IA.