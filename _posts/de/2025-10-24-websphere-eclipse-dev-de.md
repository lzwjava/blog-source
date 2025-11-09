---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: WebSphere-Entwicklung mit Eclipse
translated: true
type: note
---

### Entwicklung mit IBM WebSphere Application Server (WAS) in Eclipse

IBM WebSphere Application Server (WAS) ist ein Java EE Application Server, und Eclipse dient als eine hervorragende IDE, um Anwendungen dafür zu entwickeln, zusammenzustellen und bereitzustellen. Das Hauptwerkzeug für diese Integration sind die **IBM WebSphere Application Server Developer Tools for Eclipse** (oft als WDT abgekürzt). Dieses Plugin bietet Serververwaltung, Projekterstellung, Bereitstellung und Debugging-Funktionen direkt innerhalb von Eclipse. Es unterstützt sowohl das traditionelle WAS (z.B. v8.5 und v9.x) als auch das leichtgewichtige Liberty-Profil.

#### Erforderliches Plugin
- **IBM WebSphere Application Server Developer Tools for Eclipse**: Dies ist das wesentliche Plugin. Wählen Sie die Version, die Ihrer WAS-Laufzeitumgebung entspricht (z.B. V8.5x oder V9.x Tools). Es ist kostenlos im Eclipse Marketplace erhältlich und unterstützt aktuelle Eclipse-Versionen wie 2024-06 oder 2025-03.

Es sind keine weiteren Plugins zwingend erforderlich, aber für eine vollständige Java EE-Entwicklung sollte Ihre Eclipse-Installation die Web Tools Platform (WTP) enthalten, die im Paket "Eclipse IDE for Java EE Developers" standardmäßig enthalten ist.

#### Voraussetzungen
- Eclipse IDE for Java EE Developers (Version 2023-09 oder höher wird für die Kompatibilität empfohlen).
- IBM WAS-Laufzeitumgebung lokal installiert (traditionell oder Liberty) für Tests und Bereitstellung.
- Internetzugang für die Installation über den Marketplace (oder Herunterladen von Offline-Dateien).

#### Installationsschritte
Sie können WDT über den Eclipse Marketplace (einfachste Methode), einen Update-Site oder heruntergeladene Dateien installieren. Starten Sie Eclipse nach der Installation neu.

1. **Über den Eclipse Marketplace** (Empfohlen):
   - Öffnen Sie Eclipse und gehen Sie zu **Hilfe > Eclipse Marketplace**.
   - Suchen Sie nach "IBM WebSphere Application Server Developer Tools".
   - Wählen Sie die entsprechende Version (z.B. für V9.x oder V8.5x).
   - Klicken Sie auf **Installieren** und folgen Sie den Anweisungen. Akzeptieren Sie die Lizenzen und starten Sie Eclipse neu.

2. **Über eine Update-Site**:
   - Gehen Sie zu **Hilfe > Neue Software installieren**.
   - Klicken Sie auf **Hinzufügen** und geben Sie die Update-Site-URL ein (z.B. `https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/updates/wdt/2025-03_comp/` für aktuelle Versionen – prüfen Sie die IBM-Dokumentation auf die neueste URL).
   - Wählen Sie die WDT-Features aus (z.B. WebSphere Application Server V9.x Developer Tools) und installieren Sie sie.

3. **Aus heruntergeladenen Dateien** (Offline-Option):
   - Laden Sie das ZIP-Archiv von der [IBM Developer-Website](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools) herunter (z.B. `wdt-update-site_<version>.zip`).
   - Extrahieren Sie es in einen lokalen Ordner.
   - Gehen Sie in Eclipse zu **Hilfe > Neue Software installieren > Hinzufügen > Archiv** und wählen Sie die extrahierte `site.xml` aus.
   - Wählen Sie die gewünschten Features aus, installieren Sie sie und starten Sie Eclipse neu.

Überprüfen Sie nach der Installation die Installation, indem Sie **Fenster > Show View > Server** aufrufen – WAS sollte als Servertyp-Option erscheinen.

#### Grundlegende Schritte zur Entwicklung und Bereitstellung von WAS-Anwendungen
Sobald es installiert ist, können Sie Java EE-Anwendungen erstellen, bauen und ausführen, die für WAS bestimmt sind.

1. **Ein neues Projekt erstellen**:
   - Gehen Sie zu **Datei > Neu > Projekt**.
   - Wählen Sie **Web > Dynamisches Webprojekt** (für Web-Apps) oder **Java EE > Enterprise Application Project** (für vollständige EARs).
   - Legen Sie im Projekt-Assistenten die Ziel-Laufzeitumgebung auf Ihre lokale WAS-Installation fest (falls nicht aufgeführt, fügen Sie sie hinzu über **Fenster > Einstellungen > Server > Laufzeitumgebungen > Hinzufügen > WebSphere**).
   - Konfigurieren Sie Facets für die Java EE-Version (z.B. 7 oder 8), die zu Ihrer WAS-Version passt.

2. **Server einrichten**:
   - Öffnen Sie die **Server**-Ansicht (**Fenster > Show View > Server**).
   - Klicken Sie mit der rechten Maustaste in die Ansicht und wählen Sie **Neu > Server**.
   - Wählen Sie **WebSphere Application Server** (traditionell oder Liberty) und zeigen Sie auf Ihr lokales WAS-Installationsverzeichnis.
   - Schließen Sie den Vorgang ab und starten Sie den Server (Rechtsklick > Starten).

3. **Ihre Anwendung entwickeln**:
   - Fügen Sie Ihrem Projekt Java-Klassen, JSPs, Servlets, EJBs usw. hinzu.
   - Verwenden Sie die Editoren von Eclipse für XML-Konfigurationen (z.B. web.xml, ibm-web-bnd.xml für WAS-spezifische Bindungen).
   - Bauen Sie das Projekt (**Projekt > Projekt bauen**).

4. **Bereitstellen und Ausführen**:
   - Klicken Sie mit der rechten Maustaste auf Ihr Projekt > **Ausführen als > Auf Server ausführen** (wählen Sie Ihren WAS-Server).
   - Eclipse veröffentlicht die App (Auto-Publish für den Entwicklermodus) und startet den Server.
   - Debuggen Sie, indem Sie Haltepunkte setzen und im Debug-Modus ausführen.
   - Für Hot Deployment (schnelle Updates ohne Neustart) aktivieren Sie "Serveränderungen sofort veröffentlichen" in der Serverkonfiguration.

5. **Erweiterte Tipps**:
   - Verwenden Sie das Liberty-Profil für schnellere lokale Tests – es ist in WDT enthalten und imitiert das Verhalten des traditionellen WAS.
   - Für OSGi oder Microservices erstellen Sie OSGi Bundle Projects über das Plugin.
   - Überwachen Sie die Protokolle in der **Konsole**-Ansicht während der Laufzeit.

Wenn Sie auf Probleme stoßen (z.B. Kompatibilitätsfehler), prüfen Sie die bekannten Probleme bei IBM oder stellen Sie sicher, dass Ihre Eclipse- und WAS-Versionen zusammenpassen.

#### Referenzen
- [IBM WebSphere Application Server Developer Tools Overview](https://www.ibm.com/docs/en/wasdtfe?topic=websphere-developer-tools-overview)
- [Eclipse Marketplace: V9.x Tools](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v9x-developer-tools)
- [Eclipse Marketplace: V8.5x Tools](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v85x-developer-tools)
- [Installation Guide from IBM Docs](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools)