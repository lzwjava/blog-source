---
audio: false
generated: true
lang: es
layout: post
title: Tabla de Transacciones
translated: true
type: note
---

Una **tabla de transacciones** en un sistema bancario normalmente almacena los detalles de todas las transacciones financieras procesadas por el banco. Esta tabla es esencial para rastrear las transacciones de los clientes, conciliar cuentas y garantizar el cumplimiento normativo.

---

### **Campos Clave en una Tabla de Transacciones Bancaria**

| **Nombre del Campo**           | **Tipo de Dato** | **Descripción** |
|--------------------------------|------------------|-----------------|
| **Transaction_ID**             | `VARCHAR` / `BIGINT` | Identificador único para cada transacción |
| **Account_Number**             | `VARCHAR` / `BIGINT` | Número de cuenta bancaria del cliente involucrado en la transacción |
| **Transaction_Type**           | `VARCHAR` | Tipo de transacción (ej., DEPOSIT, WITHDRAWAL, TRANSFER, PAYMENT) |
| **Transaction_Amount**         | `DECIMAL(15,2)` | Monto involucrado en la transacción |
| **Currency_Code**              | `VARCHAR(3)` | Moneda de la transacción (ej., USD, EUR, INR) |
| **Transaction_Date**           | `DATETIME` | Marca de tiempo de cuándo ocurrió la transacción |
| **Value_Date**                 | `DATETIME` | Fecha en la que se liquida o procesa la transacción |
| **Debit_Credit_Flag**          | `CHAR(1)` | Indicador de si la transacción es un **Débito ('D')** o un **Crédito ('C')** |
| **Counterparty_Account**       | `VARCHAR` | Número de cuenta de destino (si aplica) |
| **Transaction_Mode**           | `VARCHAR` | Método de pago (SWIFT, RTGS, NEFT, ACH, UPI, Card, Wallet, etc.) |
| **Transaction_Status**         | `VARCHAR` | Estado de la transacción (PENDING, SUCCESS, FAILED, REVERSED) |
| **Reference_Number**           | `VARCHAR` | Identificador único para sistemas externos (ej., SWIFT Reference, UTR, UPI Transaction ID) |
| **Transaction_Description**    | `TEXT` | Detalles adicionales sobre la transacción (ej., "Pago de Factura - Electricidad", "Abono de Nómina") |
| **Branch_Code**                | `VARCHAR(10)` | Identificador de la sucursal bancaria que procesa la transacción |
| **Transaction_Fee**            | `DECIMAL(10,2)` | Cargos deducidos por la transacción |
| **Exchange_Rate**              | `DECIMAL(10,6)` | Tipo de cambio aplicado si hay conversión de moneda |
| **Initiating_Channel**         | `VARCHAR` | Canal utilizado para la transacción (ATM, Mobile Banking, Internet Banking, POS, Teller) |
| **Fraud_Check_Status**         | `VARCHAR` | Estado de la detección de fraude (ej., PASSED, FLAGGED, UNDER REVIEW) |
| **Reversal_Transaction_ID**    | `VARCHAR` | Si se revierte, enlaza al ID de la transacción original |

---

### **Ejemplo de Registros de Transacciones**

| Transaction_ID | Account_Number | Type      | Amount  | Currency | Date                 | Debit/Credit | Counterparty | Mode   | Status  |
|---------------|---------------|-----------|---------|----------|----------------------|--------------|--------------|--------|---------|
| 100001       | 123456789012   | DEPOSIT   | 1000.00 | USD      | 2025-03-25 10:15:00 | C            | -            | ATM    | SUCCESS |
| 100002       | 123456789012   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | D            | 987654321098 | SWIFT  | SUCCESS |
| 100003       | 987654321098   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | C            | 123456789012 | SWIFT  | SUCCESS |
| 100004       | 123456789012   | PAYMENT   | 50.00   | USD      | 2025-03-25 14:00:00 | D            | Utility Co.  | ACH    | PENDING |

---

### **Cómo se Usan Estos Campos en la Banca**
1.  **Seguimiento de Transacciones:** Cada transacción tiene un ID único y se puede rastrear a través de su estado.
2.  **Conciliación de Cuentas:** Ayuda a emparejar débitos y créditos para registros financieros precisos.
3.  **Detección de Fraude:** Las transacciones sospechosas se pueden marcar usando el estado de verificación de fraude y monitoreando patrones de transacción.
4.  **Informes Regulatorios:** Garantiza el cumplimiento de las regulaciones financieras (AML, KYC, Basilea III).
5.  **Servicio al Cliente:** Ayuda a los bancos a resolver disputas e inquietudes sobre transacciones fallidas o pendientes.

¿Te gustaría un esquema más detallado con consultas SQL? 🚀