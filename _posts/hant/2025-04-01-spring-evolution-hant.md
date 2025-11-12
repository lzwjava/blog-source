---
audio: false
generated: true
lang: hant
layout: post
title: Spring Framework 演進歷程
translated: true
type: note
---

Spring Framework 與 Spring Boot 自問世以來已歷經重大演進。以下是它們的發展歷程、主要更新版本以及如何塑造現代 Java 開發的歷史概述。

---

## **Spring Framework 演進歷程**
**Spring Framework** 由 **Rod Johnson** 於 2003 年創建，作為 Java EE 中繁重的 **Enterprise JavaBeans (EJB)** 模型替代方案。它引入了輕量級的 **控制反轉 (IoC)** 與 **依賴注入 (DI)** 模型，使 Java 開發更具模組化與可測試性。

### **Spring Framework 重要里程碑**
1. **Spring Framework 1.x (2004 年)**
   - 引入 **IoC（依賴注入）** 與 **AOP（面向切面程式設計）**
   - 為繁重的 Java EE 應用提供替代方案

2. **Spring Framework 2.x (2006 年)**
   - 增加 **基於 Java 的配置支援**（初期仍以 XML 配置為主）
   - 透過與 Hibernate 等 ORM 框架更好整合，引入更模組化的開發方式

3. **Spring Framework 3.x (2009 年)**
   - 引入 **基於 Java 的配置**（減少大量 XML 配置）
   - 新增 **RESTful Web 服務** 支援
   - 首個支援 **Java 6 與 7** 的版本

4. **Spring Framework 4.x (2013 年)**
   - 完整 **Java 8 支援**（Lambda、Streams）
   - 強化 **Spring WebSocket 支援**
   - 推出 **Spring Boot**（作為獨立專案）

5. **Spring Framework 5.x (2017 年)**
   - 引入 **響應式程式設計（Spring WebFlux）**
   - 完整 **Java 8+ 相容性**（支援 Java 11）
   - 改進 **Kotlin 支援**

6. **Spring Framework 6.x (2022 年)**
   - 完整 **Jakarta EE 支援**（取代 Java EE）
   - 要求 **Java 17+** 環境
   - 引入 **虛擬執行緒支援** 以提升並行處理效能

---

## **Spring Boot 演進歷程**
Spring Boot 最初於 **2014 年** 推出，透過消除繁瑣配置來簡化 Spring 應用的設定與開發流程。

### **Spring Boot 重要里程碑**
1. **Spring Boot 1.x (2014 年)**
   - 引入 **自動配置** 與 **Spring Initializr**
   - 內嵌伺服器如 **Tomcat、Jetty**（無需 WAR 部署）
   - 透過約定優於配置原則減少手動設定

2. **Spring Boot 2.x (2018 年)**
   - 支援 **Spring Framework 5**
   - 引入 **Spring WebFlux** 實現響應式程式設計
   - 支援 **Java 9-11**

3. **Spring Boot 3.x (2022 年)**
   - 完整支援 **Jakarta EE 10**
   - 要求 **Java 17+** 環境
   - 引入 **GraalVM 原生映像支援** 實現快速啟動

---

## **Spring 未來發展**
- **Spring AI**：整合人工智慧功能的新模組
- **強化虛擬執行緒與 GraalVM 支援** 以支援雲原生應用
- **提升 Kubernetes 與無伺服器架構能力**

Spring 已從 **繁重的企業級框架** 轉型為 **輕量級、響應式且雲原生的解決方案**，使其成為當今 Java 開發領域的主導力量。

需要我深入說明任何特定版本或功能嗎？🚀