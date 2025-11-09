---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Azure Log Analytics im Vergleich zu Azure Insights
translated: true
type: note
---

Gute Frage – sie sind **eng miteinander verbunden**, aber **nicht dasselbe**. Lassen Sie uns das klar darlegen.

---

### **1. Azure Log Analytics**

**Azure Log Analytics** ist ein **Tool/Dienst** innerhalb von **Azure Monitor**, mit dem Sie **Protokolle** aus Ihren Cloud- und lokalen Ressourcen **sammeln, abfragen und analysieren** können.

* Es speichert Protokolle in einem **Log Analytics-Arbeitsbereich**.
* Sie können Abfragen mit der **Kusto Query Language (KQL)** ausführen, um Daten zu analysieren.
* Es wird verwendet für:

  * Fehlerbehebung
  * Leistungsuntersuchungen
  * Sicherheitsüberwachung
  * Erstellen benutzerdefinierter Dashboards und Warnungen

Stellen Sie sich Log Analytics als den **Data Lake und die Abfrage-Engine** für all Ihre Protokolldaten in Azure vor.

---

### **2. Azure Insights**

**Azure Insights** (oft als **Application Insights** oder **Azure Monitor Insights** zu sehen) ist Teil derselben Monitoring-Ökosphäre, konzentriert sich aber mehr auf **Anwendungsmonitoring** als auf Rohprotokolle.

Es gibt verschiedene Arten von "Insights":

* **Application Insights** – überwacht Anwendungen (APM): Leistung, Ausnahmen, Abhängigkeiten, Benutzerverhalten usw.
* **VM Insights**, **Container Insights**, **Network Insights** – bieten vorgefertigte Monitoring-Ansichten für bestimmte Ressourcentypen.

Alle diese Insights **speichern ihre Telemetriedaten und Metriken in Log Analytics-Arbeitsbereichen**, sie **bauen also unter der Haube auf Log Analytics auf**.

---

### **3. Beziehung**

* **Azure Insights = Visualisierungs- & intelligente Monitoring-Schicht**
* **Log Analytics = Protokollspeicher & Abfrage-Engine darunter**

Kurz gesagt:

> Log Analytics ist, *wo* die Daten leben und analysiert werden.
> Insights sind, *wie* Sie diese Daten für bestimmte Ressourcentypen betrachten und interpretieren.

---

### **Beispiel**

Wenn Sie **Application Insights** für eine Web-App aktivieren:

* Es sammelt Telemetriedaten (Anfragen, Abhängigkeiten, Ablaufverfolgungen, Ausnahmen).
* Diese Daten werden in **einem Log Analytics-Arbeitsbereich** gespeichert.
* Sie können **Log Analytics** verwenden, um KQL-Abfragen über dieselben Daten für tiefgreifendere benutzerdefinierte Analysen auszuführen.

---

Möchten Sie, dass ich ein einfaches **KQL-Beispiel** zeige, wie Log Analytics Application Insights-Daten abfragt?