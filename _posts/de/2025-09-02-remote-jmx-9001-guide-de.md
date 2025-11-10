---
audio: false
generated: true
image: false
lang: de
layout: post
title: Leitfaden zum Remote-JMX-Port 9001
translated: true
type: note
---

Ein **JMX-Remote-Agent** ist Teil der Java Management Extensions (JMX). Er ermöglicht es Ihnen, eine laufende Java-Anwendung remote zu überwachen und zu verwalten. Wenn Sie die JMX-Fernverwaltung aktivieren, startet die JVM einen Agenten, der MBeans (Managed Beans) über einen TCP-Port verfügbar macht. Tools wie **jconsole**, **VisualVM** oder benutzerdefinierte Monitoring-Software können sich mit diesem Port verbinden, um Speichernutzung, Thread-Zustände, GC-Aktivität zu inspizieren und sogar Operationen aufzurufen.

Über den **Port 9001**:

* Die tatsächliche Portnummer hängt davon ab, wie die Anwendung konfiguriert ist. Üblicherweise sieht man 9001, 9090, 9091, etc.
* Wenn Sie sehen, dass etwas auf `9001` lauscht und es sich um einen **JMX-Remote-Agent** handelt, bedeutet das, dass ein Java-Prozess mit Systemeigenschaften wie diesen gestartet wurde:

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9001
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```

Dies öffnet JMX auf Port `9001` ohne Authentifizierung/SSL (oft nur für interne oder Entwicklungszwecke, da es unsicher ist, wenn es öffentlich exponiert wird).

---

### So überprüfen Sie, welches Programm den JMX-Port 9001 unter Windows verwendet

1. Öffnen Sie die **Eingabeaufforderung (als Administrator)**.
2. Führen Sie aus:

   ```cmd
   netstat -ano | findstr :9001
   ```

   Dies zeigt die PID (Process ID), die an diesen Port gebunden ist.
3. Um das Programm zu identifizieren:

   ```cmd
   tasklist /FI "PID eq <PID>"
   ```

   Ersetzen Sie `<PID>` durch die Nummer aus Schritt 2.

---

### So stoppen / beenden Sie es

* Wenn Sie bestätigen, dass es sich um einen unerwünschten Java-Prozess handelt, beenden Sie ihn mit:

  ```cmd
   taskkill /PID <PID> /F
   ```
* Wenn es jedoch Teil Ihres Application Servers (Tomcat, WebSphere, Spring Boot App, etc.) ist, ist es besser, ihn über seinen Service/die Konsole zu stoppen, anstatt den Prozess zu killen, damit er sich sauber herunterfährt.

---

👉 Möchten Sie, dass ich Ihnen auch zeige, wie man den **JMX-Remote-Agent** in einer Java-Anwendung **deaktiviert**, damit er den Port 9001 überhaupt nicht öffnet?