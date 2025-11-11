---
audio: false
generated: true
lang: de
layout: post
title: Transaktionstabelle
translated: true
type: note
---

Eine **Transaktionstabelle** in einem Bankensystem speichert typischerweise Details aller finanziellen Transaktionen, die von der Bank verarbeitet werden. Diese Tabelle ist entscheidend für die Nachverfolgung von Kundentransaktionen, den Kontenabgleich und die Einhaltung gesetzlicher Vorschriften.

---

### **Wichtige Felder in einer Bank-Transaktionstabelle**

| **Feldname**                | **Datentyp**     | **Beschreibung**                                                                                             |
|-----------------------------|------------------|-------------------------------------------------------------------------------------------------------------|
| **Transaction_ID**          | `VARCHAR` / `BIGINT` | Eindeutiger Identifikator für jede Transaktion                                                              |
| **Account_Number**          | `VARCHAR` / `BIGINT` | Kontonummer des Kunden, der an der Transaktion beteiligt ist                                                |
| **Transaction_Type**        | `VARCHAR`        | Art der Transaktion (z.B. DEPOSIT, WITHDRAWAL, TRANSFER, PAYMENT)                                           |
| **Transaction_Amount**      | `DECIMAL(15,2)`  | Betrag der Transaktion                                                                                      |
| **Currency_Code**           | `VARCHAR(3)`     | Währung der Transaktion (z.B. USD, EUR, INR)                                                                |
| **Transaction_Date**        | `DATETIME`       | Zeitstempel, wann die Transaktion stattgefunden hat                                                         |
| **Value_Date**              | `DATETIME`       | Datum, an dem die Transaktion abgewickelt oder verarbeitet wird                                             |
| **Debit_Credit_Flag**       | `CHAR(1)`        | Kennzeichen, ob es sich um eine **Lastschrift ('D')** oder **Gutschrift ('C')** handelt                     |
| **Counterparty_Account**    | `VARCHAR`        | Zielkontonummer (falls zutreffend)                                                                          |
| **Transaction_Mode**        | `VARCHAR`        | Zahlungsmethode (SWIFT, RTGS, NEFT, ACH, UPI, Card, Wallet, etc.)                                           |
| **Transaction_Status**      | `VARCHAR`        | Status der Transaktion (PENDING, SUCCESS, FAILED, REVERSED)                                                 |
| **Reference_Number**        | `VARCHAR`        | Eindeutiger Identifikator für externe Systeme (z.B. SWIFT Reference, UTR, UPI Transaction ID)               |
| **Transaction_Description** | `TEXT`           | Zusätzliche Details zur Transaktion (z.B. "Rechnungszahlung - Strom", "Gehaltseingang")                     |
| **Branch_Code**             | `VARCHAR(10)`    | Kennung für die Bankfiliale, die die Transaktion bearbeitet                                                 |
| **Transaction_Fee**         | `DECIMAL(10,2)`  | Etwaige für die Transaktion abgezogene Gebühren                                                             |
| **Exchange_Rate**           | `DECIMAL(10,6)`  | Wechselkurs, der bei einer Währungsumrechnung angewendet wurde                                              |
| **Initiating_Channel**      | `VARCHAR`        | Genutzter Kanal für die Transaktion (ATM, Mobile Banking, Internet Banking, POS, Teller)                    |
| **Fraud_Check_Status**      | `VARCHAR`        | Status der Betrugserkennung (z.B. PASSED, FLAGGED, UNDER REVIEW)                                            |
| **Reversal_Transaction_ID** | `VARCHAR`        | Bei Stornotransaktionen: Verweis auf die ursprüngliche Transaktions-ID                                      |

---

### **Beispielhafte Transaktionsdatensätze**

| Transaction_ID | Account_Number | Type      | Amount  | Currency | Date                 | Debit/Credit | Counterparty      | Mode   | Status  |
|---------------|---------------|-----------|---------|----------|----------------------|--------------|-------------------|--------|---------|
| 100001       | 123456789012   | DEPOSIT   | 1000.00 | USD      | 2025-03-25 10:15:00 | C            | -                 | ATM    | SUCCESS |
| 100002       | 123456789012   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | D            | 987654321098      | SWIFT  | SUCCESS |
| 100003       | 987654321098   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | C            | 123456789012      | SWIFT  | SUCCESS |
| 100004       | 123456789012   | PAYMENT   | 50.00   | USD      | 2025-03-25 14:00:00 | D            | Utility Co.       | ACH    | PENDING |

---

### **Wie diese Felder im Bankwesen verwendet werden**
1.  **Transaktionsverfolgung:** Jede Transaktion hat eine eindeutige ID und kann über ihren Status verfolgt werden.
2.  **Kontenabstimmung:** Hilft beim Abgleichen von Lastschriften und Gutschriften für genaue Finanzaufzeichnungen.
3.  **Betrugserkennung:** Verdächtige Transaktionen können mithilfe des Betrugsprüfstatus und der Überwachung von Transaktionsmustern gekennzeichnet werden.
4.  **Meldepflichten:** Stellt die Einhaltung finanzieller Vorschriften sicher (AML, KYC, Basel III).
5.  **Kundenservice:** Hilft Banken, Streitigkeiten und Anfragen zu fehlgeschlagenen oder ausstehenden Transaktionen zu klären.

Möchten Sie ein detaillierteres Schema mit SQL-Abfragen? 🚀