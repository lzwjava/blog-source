---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht der BrowserStack-Testplattform
translated: true
type: note
---

BrowserStack ist eine führende cloud-basierte Software-Testplattform, die Entwicklern, QA-Teams und Testern die Validierung von Websites und mobilen Anwendungen auf Tausenden von echten Browsern, Betriebssystemen und Geräten ermöglicht. Das 2011 gestartete Produkt beseitigt die Notwendigkeit, physische Hardware-Labore zu unterhalten, indem es sofortigen Zugriff auf über 3.500 Browser-Geräte-Kombinationen bietet, einschließlich der neuesten Versionen von Chrome, Firefox, Safari, Edge und mobilen Umgebungen auf iOS und Android. Es wird besonders für Cross-Browser-Kompatibilitätstests, automatisiertes Scripting und manuelle interaktive Sitzungen geschätzt und unterstützt sowohl Web- als auch Native/Hybrid-Apps.

## Warum BrowserStack verwenden?

Das Testen über verschiedene Umgebungen hinweg ist entscheidend, um die konsistente Leistung von Anwendungen sicherzustellen, aber es ist ressourcenintensiv. BrowserStack adressiert dies durch:
- Bereitstellung echter Geräte und Browser (keine Emulatoren) für genaue Ergebnisse.
- Ermöglichen von parallelem Testen, um Testzyklen zu beschleunigen.
- Integration mit beliebten Tools wie Selenium, Appium, Cypress und CI/CD-Pipelines (z.B. Jenkins, GitHub Actions).
- Bereitstellung KI-gestützter Funktionen wie selbstheilender Tests und Fehleranalysen, um den Wartungsaufwand zu reduzieren.
- Unterstützung von Teams mit kollaborativem Debugging, Bug-Reporting und Analysen.

Es wird von über 50.000 Teams weltweit genutzt, einschließlich Fortune-500-Unternehmen, für schnellere Releases und höhere Abdeckung ohne Einrichtungsaufwand.

## Registrierung und erste Schritte

1.  **Konto erstellen**: Besuchen Sie die BrowserStack-Website und registrieren Sie sich mit Ihrer E-Mail, Google oder GitHub. Eine kostenlose Testversion ist verfügbar, einschließlich eingeschränktem Zugang zu Live-Testing und Automatisierungsfunktionen.
2.  **Dashboard-Zugang**: Melden Sie sich an, um Ihren Benutzernamen und Zugangsschlüssel (zu finden unter Automate > Account Settings) einzusehen. Diese sind für das Scripting entscheidend.
3.  **Produkte erkunden**: Wählen Sie im oberen Menü aus Live (manuelles Testen), Automate (script-basiertes Web/Mobile), App Live/Automate (App-fokussiert), Percy (visuell) und mehr.
4.  **Local Testing einrichten**: Für private Apps installieren Sie das BrowserStack Local Tool (Binary für Windows/Mac/Linux), um Localhost-Datenverkehr sicher zu tunneln.
5.  **Team-Einrichtung**: Laden Sie Benutzer per E-Mail ein und konfigurieren Sie Rollen für kollaborativen Zugriff.

Über den lokalen Agenten hinaus ist keine Installation erforderlich – Tests laufen in der Cloud.

## Live Testing (Manuelles interaktives Testen)

Live Testing ermöglicht es Ihnen, in Echtzeit mit Apps auf Remote-Geräten zu interagieren, ideal für exploratives QA.

### Webanwendungen testen
1.  Wählen Sie **Live** aus dem Produkt-Dropdown-Menü.
2.  Wählen Sie ein Betriebssystem (z.B. Windows 10, macOS, Android).
3.  Wählen Sie einen Browser/eine Version (z.B. Chrome 120, Safari 17).
4.  Geben Sie die URL Ihrer App ein – die Sitzung startet in einem neuen Tab.
5.  Verwenden Sie die integrierten Tools: DevTools, Konsole, Netzwerk-Inspector, Screenshots und Responsiveness-Checker.
6.  Wechseln Sie Browser während der Sitzung über die Dashboard-Seitenleiste.
7.  Bugs melden: Heben Sie Probleme hervor, kommentieren Sie sie und integrieren Sie mit Jira, Slack oder E-Mail.

Sitzungen unterstützen Geopositionierung (100+ Länder), Netzwerk-Drosselung und bis zu 25-minütige Leerlauf-Timeouts bei Pro-Plänen.

### Mobiles Web testen (Browser auf Geräten)
1.  Wählen Sie in Live ein mobiles Betriebssystem (Android/iOS).
2.  Wählen Sie ein Gerät (z.B. Samsung Galaxy S24, iPhone 15) und einen Browser (z.B. Chrome auf Android).
3.  Laden Sie die URL und interagieren Sie – unterstützt Gesten wie Pinch-to-Zoom.
4.  Debuggen Sie mit mobil-spezifischen Tools: Touch-Simulation, Orientierungswechsel und Leistungsmetriken.

### Native/Hybrid Mobile Apps testen
1.  Gehen Sie zu **App Live**.
2.  Laden Sie Ihre App hoch (.apk für Android, .ipa für iOS; bis zu 500 MB) oder synchronisieren Sie sie von App Center/HockeyApp.
3.  Wählen Sie ein Gerät aus über 30.000 echten Optionen (z.B. iPad Pro auf iOS 18).
4.  Starten Sie die App und testen Sie: Wischen, Tippen, Schütteln oder verwenden Sie Hardware wie GPS/Kamera.
5.  Erweitert: QR-Codes injizieren, Biometrie simulieren, Apple Pay/Google Pay testen oder Zeitzonen/Dunkelmodus ändern.
6.  Beenden Sie die Sitzung und sehen Sie sich Videoaufzeichnungen/Logs an.

| Funktion | Web Live | App Live |
|---------|----------|----------|
| Geräte | 3.000+ Browser | 30.000+ echte Mobilgeräte |
| Upload | Nur URL | App-Binary |
| Tools | DevTools, Auflösungen | Gesten, Biometrie, Audioeingabe |
| Limits | Unbegrenzte Minuten (bezahlt) | 10-25 min Leerlauf-Timeout |

## Automatisierte Tests

Automatisieren Sie repetitive Tests mit Scripts auf echten Umgebungen, skalierbar auf Tausende parallele Durchläufe.

### Einrichtung
1.  Wählen Sie ein Framework: Selenium (Java/Python/JS), Cypress, Playwright oder Appium für mobil.
2.  Beschaffen Sie Anmeldedaten: Benutzername und Zugangsschlüssel aus dem Automate-Dashboard.
3.  Konfigurieren Sie Capabilities: Verwenden Sie JSON, um Browser, Betriebssystem und Gerät anzugeben (z.B. `{"browser": "Chrome", "os": "Windows", "os_version": "10", "real_mobile": true}`).

### Ausführung
1.  Richten Sie Ihr Script auf BrowserStacks Hub aus: `https://username:accesskey@hub-cloud.browserstack.com/wd/hub`.
2.  Führen Sie es lokal oder via CI/CD aus – Tests werden parallel ausgeführt.
3.  Ergebnisse ansehen: Das Dashboard zeigt Videos, Screenshots, Konsolen-/Netzwerk-Logs und KI-analysierte Fehler an.
4.  Für mobil: Laden Sie die App zuerst per API hoch und geben Sie sie dann in den Capabilities an.

#### Beispiel-Selenium-Script (Java, Test von Google auf iPhone)
```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.By;
import java.net.URL;

public class BrowserStackSample {
    public static final String USERNAME = "your_username";
    public static final String AUTOMATE_KEY = "your_access_key";
    public static final String URL = "https://" + USERNAME + ":" + AUTOMATE_KEY + "@hub-cloud.browserstack.com/wd/hub";

    public static void main(String[] args) throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("browserName", "iPhone");
        caps.setCapability("device", "iPhone 15");
        caps.setCapability("realMobile", "true");
        caps.setCapability("os_version", "17");
        caps.setCapability("name", "Sample Test");

        WebDriver driver = new RemoteWebDriver(new URL(URL), caps);
        driver.get("https://www.google.com");
        WebElement searchBox = driver.findElement(By.name("q"));
        searchBox.sendKeys("BrowserStack");
        searchBox.submit();
        System.out.println("Page title: " + driver.getTitle());
        driver.quit();
    }
}
```
Anpassung für Python/JS ähnlich. Fügen Sie Waits (z.B. WebDriverWait) für Stabilität hinzu.

## Testautomatisierungs-Workflow

Erstellen Sie eine effiziente Pipeline mit diesen Schritten:
1.  **Planen**: Identifizieren Sie hochwertige Tests (z.B. Kernabläufe); stimmen Sie sie mit Agile ab.
2.  **Tools auswählen**: Verwenden Sie BrowserStack Automate für Cloud-Ausführung; fügen Sie Low Code für scriptloses Testen hinzu.
3.  **Designen**: Erstellen Sie modulare Scripts mit wiederverwendbaren Komponenten; nutzen Sie KI für die Erstellung in natürlicher Sprache.
4.  **Ausführen**: Auslösen via CI/CD; führen Sie parallele Tests auf echten Geräten mit benutzerdefinierten Netzwerken/Standorten durch.
5.  **Analysieren**: Überprüfen Sie KI-Erkenntnisse, Logs und Trends; protokollieren Sie Fehler in Jira.
6.  **Warten**: Wenden Sie Self-Healing für UI-Änderungen an; optimieren Sie flaky Tests.

Dies reduziert den Wartungsaufwand um 40 % und beschleunigt Releases.

## Wichtige Funktionen und Integrationen

-   **KI-Agenten**: Selbstheilung, Fehlerkategorisierung, Testgenerierung.
-   **Visuell/Barrierefreiheit**: Percy für UI-Diffs; Scans auf WCAG-Compliance.
-   **Berichterstattung**: Benutzerdefinierte Dashboards, Warnungen, 1-Jahres-Aufbewahrung.
-   **Integrationen**: CI/CD (Jenkins, Travis), Bug-Tracker (Jira, Trello), Versionskontrolle (GitHub) und Low-Code-Tools.
-   **Sicherheit**: SOC2-konform, Datenverschlüsselung, RBAC.

Unterstützt 21 Rechenzentren für niedrige Latenz.

## Preispläne (Stand Oktober 2025)

Pläne sind jährlich (sparen Sie 25 %) und skalieren nach Benutzern/parallelen Tests. Kostenlose Tarife/begrenzte Testversionen verfügbar; Open-Source unbegrenzt.

| Produkt | Starter Plan | Pro/Team | Wichtige Funktionen |
|---------|--------------|----------|--------------|
| **Live (Desktop/Mobile)** | 29 $/User/Monat (Desktop) | 39 $/User/Monat (Mobile) | Unbegrenzte Minuten, 3.000+ Browser, Geopositionierung. Team: 30 $+/User. |
| **Automate (Web/Mobile)** | 99 $/Monat (1 parallel) | 225 $/Monat (Pro, 1 parallel) | Selenium/Appium, KI-Selbstheilung, Videos/Logs. Skaliert auf 25+ Parallele. |
| **App Live/Automate** | 39 $/Monat (Individual) | 199 $/Monat (1 parallel) | 30.000+ Geräte, Gesten, Biometrie. Pro: 249 $/Monat. |
| **Percy (Visuell)** | Kostenlos (5K Screenshots) | 199 $/Monat (10K) | KI-Reviews, Figma-Integration. Mobile: 599 $/Monat. |
| **Barrierefreiheit** | Kostenlos (5 Seiten/Scan) | 199 $/Monat (Monitor) | Screen Reader, tägliche Scans. Automate: 459 $/Monat. |
| **Testmanagement** | Kostenlos (5 Benutzer) | 99 $/Monat (Team) | Repos, CI-Integrationen. Pro: 199 $/Monat. |

Enterprise: Benutzerdefiniert, mit SSO und privaten Geräten. Mengenrabatte bis zu 90 %.

## Vor- und Nachteile

**Vorteile**:
-   Große Abdeckung mit echten Geräten ohne Hardwarekosten.
-   Schnelle Einrichtung und parallele Skalierung.
-   Robustes Debugging und KI-Effizienzen.
-   Starke Integrationen für DevOps.

**Nachteile**:
-   Abhängig vom Internet; gelegentliche Latenz im Vergleich zu lokal.
-   Vollzugriff nur kostenpflichtig (keine vollständige kostenlose Stufe).
-   Komplex für absolute Anfänger ohne Tutorials.

## Best Practices

-   Beginnen Sie mit Tests mit großer Wirkung; automatisieren Sie 70 % der Regressionstests.
-   Verwenden Sie Local Tunneling für Staging-Apps.
-   Überwachen Sie Flakiness mit KI-Berichten; testen Sie zuerst auf neuesten OS/Browsern.
-   Kombinieren Sie manuelle und automatisierte Tests für umfassende Abdeckung.
-   Nutzen Sie Videos/Screenshots für schnelles Triaging.
-   Für mobil: Testen Sie früh auf verschiedenen Netzwerken und Ausrichtungen.

Dieser Leitfaden stattet Sie aus, um BrowserStack effektiv zu nutzen. Für praktische Erfahrungen erkunden Sie deren kostenlose Testversion.

## Referenzen

-   [BrowserStack Offizielle Website](https://www.browserstack.com/)
-   [BrowserStack Preisgestaltung](https://www.browserstack.com/pricing)
-   [BrowserStack Tutorial: App und Browser Testing](https://www.softwaretestinghelp.com/browserstack-tutorial/)
-   [Testautomatisierungs-Workflow-Leitfaden](https://www.browserstack.com/guide/test-automation-workflow)
-   [BrowserStack Funktionsübersicht](https://www.browserstack.com/guide)