---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 快速支付系統整合指南
translated: true
type: note
---

香港的快速支付系統（FPS）由香港銀行同業結算有限公司（HKICL）在金管局（HKMA）監管下運作，並未向銀行提供公開的軟體開發套件（SDK）進行整合。整合需透過直接連接FPS基礎設施實現，技術規格會在參與銀行（稱為結算參與者）加入過程中私下分享。這些規格指引銀行提升系統以實現接入，但官方文件中並未提及現成的SD件或開發套件。

關於應用程式介面（API），FPS目前並未提供專供外部或第三方整合的專用API。然而，它與金管局更廣泛的「香港銀行業開放API框架」（於2018年推出並分階段更新至2025年）保持一致，該框架鼓勵銀行透過API向第三方服務供應商開放某些功能（例如帳戶資訊或支付發起）。FPS交易可間接利用此框架實現如支付發起等功能，但目前尚未提供FPS專屬API——基於安全及監管原因，存取權限仍按需限制。金管局持續監察情況，未來或會擴展API支援。

### 銀行整合關鍵細節
- **連接方式**：銀行透過IBM MQ訊息傳遞實時連接以實現即時處理，或透過檔案傳輸（例如經HKICL安全的ICLNET網絡）以批次模式連接。系統全天候運作。
- **訊息標準**：所有通訊均採用ISO 20022格式，支援豐富數據、中文字元及互通性。
- **加入流程**：銀行向金管局（港元）或中國銀行（香港）（人民幣）登記，簽署FPS規則協議，根據提供的規格調整系統，通過HKICL測試後正式運作。所有持牌銀行必須以直接結算者身份參與。
- **其他功能**：支援代理識別碼（如電話/電郵）、二維碼（EMV標準）及多幣種（港元/人民幣）轉帳。認證遵循金管局的雙重因素指引，銀行可自設交易限額。

有關詳細技術規格，銀行必須在加入時直接聯絡HKICL，因這些規格不提供公開下載。

[快速支付系統（FPS） - 金管局](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/financial-market-infrastructure/faster-payment-system-fps/)  
[計劃文件 - HKICL FPS](https://fps.hkicl.com.hk/eng/fps/about_fps/scheme_documentation.php)  
[世界銀行FPS案例研究：香港](https://fastpayments.worldbank.org/sites/default/files/2021-09/World_Bank_FPS_Hong_Kong_SAR_China_FPS_Case_Study.pdf)  
[銀行業開放API框架 - 金管局](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/fintech/open-application-programming-interface-api-for-the-banking-sector/)