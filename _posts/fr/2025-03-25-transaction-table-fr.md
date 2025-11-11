---
audio: false
generated: true
lang: fr
layout: post
title: Table des Transactions
translated: true
type: note
---

Une **table de transaction** dans un système bancaire stocke généralement les détails de toutes les transactions financières traitées par la banque. Cette table est essentielle pour suivre les transactions des clients, rapprocher les comptes et assurer la conformité réglementaire.

---

### **Champs Clés dans une Table de Transaction Bancaire**

| **Nom du Champ**           | **Type de Données** | **Description** |
|----------------------------|---------------------|-----------------|
| **Transaction_ID**         | `VARCHAR` / `BIGINT` | Identifiant unique pour chaque transaction |
| **Account_Number**         | `VARCHAR` / `BIGINT` | Numéro de compte bancaire du client impliqué dans la transaction |
| **Transaction_Type**       | `VARCHAR` | Type de transaction (ex: DEPOSIT, WITHDRAWAL, TRANSFER, PAYMENT) |
| **Transaction_Amount**     | `DECIMAL(15,2)` | Montant impliqué dans la transaction |
| **Currency_Code**          | `VARCHAR(3)` | Devise de la transaction (ex: USD, EUR, INR) |
| **Transaction_Date**       | `DATETIME` | Horodatage de la transaction |
| **Value_Date**             | `DATETIME` | Date où la transaction est réglée ou traitée |
| **Debit_Credit_Flag**      | `CHAR(1)` | Indicateur si la transaction est un **Débit ('D')** ou un **Crédit ('C')** |
| **Counterparty_Account**   | `VARCHAR` | Numéro de compte du bénéficiaire (le cas échéant) |
| **Transaction_Mode**       | `VARCHAR` | Moyen de paiement (SWIFT, RTGS, NEFT, ACH, UPI, Card, Wallet, etc.) |
| **Transaction_Status**     | `VARCHAR` | Statut de la transaction (PENDING, SUCCESS, FAILED, REVERSED) |
| **Reference_Number**       | `VARCHAR` | Identifiant unique pour les systèmes externes (ex: SWIFT Reference, UTR, UPI Transaction ID) |
| **Transaction_Description**| `TEXT` | Détails supplémentaires sur la transaction (ex: "Paiement de facture - Électricité", "Virement de salaire") |
| **Branch_Code**            | `VARCHAR(10)` | Identifiant de l'agence bancaire traitant la transaction |
| **Transaction_Fee**        | `DECIMAL(10,2)` | Frais éventuels déduits pour la transaction |
| **Exchange_Rate**          | `DECIMAL(10,6)` | Taux de change appliqué si une conversion de devise est impliquée |
| **Initiating_Channel**     | `VARCHAR` | Canal utilisé pour la transaction (ATM, Mobile Banking, Internet Banking, POS, Teller) |
| **Fraud_Check_Status**     | `VARCHAR` | Statut de la détection de fraude (ex: PASSED, FLAGGED, UNDER REVIEW) |
| **Reversal_Transaction_ID**| `VARCHAR` | Si annulée, lien vers l'ID de la transaction d'origine |

---

### **Exemples d'Enregistrements de Transaction**

| Transaction_ID | Account_Number | Type      | Montant  | Devise | Date                 | Débit/Crédit | Contrepartie | Mode   | Statut  |
|---------------|---------------|-----------|---------|----------|----------------------|--------------|--------------|--------|---------|
| 100001       | 123456789012   | DEPOSIT   | 1000.00 | USD      | 2025-03-25 10:15:00 | C            | -            | ATM    | SUCCESS |
| 100002       | 123456789012   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | D            | 987654321098 | SWIFT  | SUCCESS |
| 100003       | 987654321098   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | C            | 123456789012 | SWIFT  | SUCCESS |
| 100004       | 123456789012   | PAYMENT   | 50.00   | USD      | 2025-03-25 14:00:00 | D            | Utility Co.  | ACH    | PENDING |

---

### **Utilisation de Ces Champs dans le Secteur Bancaire**
1.  **Suivi des Transactions :** Chaque transaction possède un ID unique et peut être suivie via son statut.
2.  **Rapprochement de Comptes :** Aide à faire correspondre les débits et les crédits pour une comptabilité précise.
3.  **Détection de Fraude :** Les transactions suspectes peuvent être signalées en utilisant le statut de contrôle de fraude et en surveillant les modèles de transaction.
4.  **Reporting Réglementaire :** Assure la conformité avec les réglementations financières (AML, KYC, Bâle III).
5.  **Service Client :** Aide les banques à résoudre les litiges et les demandes concernant les transactions échouées ou en attente.

Souhaitez-vous un schéma plus détaillé avec des requêtes SQL ? 🚀