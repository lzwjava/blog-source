---
audio: false
generated: true
lang: de
layout: post
title: Leitfaden für datenschutzorientierte Webanalyse
translated: true
type: note
---

Cloudflare Web Analytics ist ein datenschutzorientiertes, kostenloses Tool, das Website-Betreibern dabei helfen soll, die Leistung ihrer Website und das Besucherverhalten zu verfolgen und zu verstehen, ohne die Privatsphäre der Nutzer zu beeinträchtigen. Im Folgenden finden Sie eine umfassende Anleitung zur Einrichtung und Verwendung von Cloudflare Web Analytics, basierend auf den neuesten verfügbaren Informationen.

### Überblick über Cloudflare Web Analytics
Cloudflare Web Analytics bietet Einblicke in Website-Traffic, Seitenaufrufe und Leistungsmetriken und priorisiert dabei die Privatsphäre der Nutzer. Im Gegensatz zu traditionellen Analysetools, die personenbezogene Daten erfassen oder Cookies verwenden könnten, vermeidet Cloudflares Lösung invasive Tracking-Methoden wie Fingerprinting, Cookies oder lokalen Speicher für Analysezwecke. Es eignet sich für Websites aller Größen und kann mit oder ohne Cloudflares Proxy-Dienste verwendet werden.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)

### Wichtige Funktionen
- **Datenschutz-First**: Erfasst keine personenbezogenen Daten, verwendet keine Cookies und verfolgt Nutzer nicht über IP-Adressen oder User Agents, um die Einhaltung von Datenschutzvorschriften wie der DSGVO zu gewährleisten.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Zwei Datenerfassungsmethoden**:
  - **JavaScript Beacon**: Ein schlankes JavaScript-Snippet erfasst clientseitige Metriken unter Verwendung der Performance API des Browsers. Ideal für detaillierte Real User Monitoring (RUM)-Daten, wie Seitenladezeiten und Core Web Vitals.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
  - **Edge Analytics**: Erfasst serverseitige Daten von den Edge-Servern von Cloudflare für Websites, die über Cloudflare geproxyt werden. Es sind keine Code-Änderungen erforderlich, und es erfasst alle Anfragen, einschließlich derer von Bots oder Nutzern mit deaktiviertem JavaScript.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **Bereitgestellte Metriken**: Verfolgt Seitenaufrufe, Besuche, Top-Seiten, Verweise, Länder, Gerätetypen, Statuscodes und Leistungsmetriken wie Seitenladezeiten.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Adaptive Bit Rate (ABR)**: Passt die Datenauflösung automatisch basierend auf Datengröße, Zeitraum und Netzwerkbedingungen für optimale Leistung an.[](https://developers.cloudflare.com/web-analytics/about/)
- **Kostenlos zu verwenden**: Verfügbar für jeden mit einem Cloudflare-Konto, auch ohne DNS-Änderung oder die Verwendung des Cloudflare-Proxys.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Dashboard und Filter**: Bietet ein intuitives Dashboard zum Anzeigen und Filtern von Daten nach Hostname, URL, Land und Zeitraum. Sie können in bestimmte Zeiträume zoomen oder Daten für tiefere Analysen gruppieren.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)
- **Unterstützung für Single Page Applications (SPA)**: Verfolgt Routenänderungen in SPAs automatisch durch Überschreiben der `pushState`-Funktion der History API (hash-basierte Router werden nicht unterstützt).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### Einschränkungen
- **Datenaufbewahrung**: Beschränkt auf 30 Tage historischer Daten, was für Benutzer, die Langzeitanalysen benötigen, möglicherweise nicht geeignet ist.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Daten-Stichproben**: Metriken basieren auf einer 10 %-Stichprobe von Seitenlade-Ereignissen, was zu Ungenauigkeiten im Vergleich zu Tools wie Plausible oder Fathom Analytics führen kann.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Ungenauigkeitsprobleme**: Serverseitige Analysen (Edge Analytics) können Bot-Traffic enthalten, was die Zahlen im Vergleich zu clientseitigen Analysen wie Google Analytics aufbläht. Clientseitige Analysen können Daten von Nutzern mit deaktiviertem JavaScript oder Ad-Blockern verpassen.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
- **Keine UTM-Parameter-Unterstützung**: Derzeit werden Query-Strings wie UTM-Parameter nicht protokolliert, um die Erfassung sensibler Daten zu vermeiden.[](https://developers.cloudflare.com/web-analytics/faq/)
- **Export-Einschränkungen**: Keine direkte Möglichkeit, Daten (z. B. nach CSV) zu exportieren, anders als bei einigen Mitbewerbern wie Fathom Analytics.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Grundlegende Analysen**: Es fehlen erweiterte Funktionen wie Conversion-Tracking oder detaillierte Analyse des Nutzerwegs im Vergleich zu Google Analytics.[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)

### Einrichtung von Cloudflare Web Analytics
#### Voraussetzungen
- Ein Cloudflare-Konto (kostenlos zu erstellen unter cloudflare.com).
- Zugriff auf den Code Ihrer Website (für JavaScript Beacon) oder die DNS-Einstellungen (für Edge Analytics, wenn der Cloudflare-Proxy verwendet wird).

#### Einrichtungsschritte
1. **Melden Sie sich beim Cloudflare Dashboard an**:
   - Gehen Sie zu [cloudflare.com](https://www.cloudflare.com) und melden Sie sich an oder erstellen Sie ein Konto.
   - Gehen Sie vom Account Home zu **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/web-analytics/get-started/)

2. **Fügen Sie eine Website hinzu**:
   - Klicken Sie im Bereich Web Analytics auf **Add a site**.
   - Geben Sie den Hostnamen Ihrer Website ein (z. B. `example.com`) und wählen Sie **Done**.[](https://developers.cloudflare.com/web-analytics/get-started/)

3. **Wählen Sie die Datenerfassungsmethode**:
   - **JavaScript Beacon (Empfohlen für nicht-geproxte Websites)**:
     - Kopieren Sie das bereitgestellte JavaScript-Snippet aus dem Abschnitt **Manage site**.
     - Fügen Sie es in das HTML Ihrer Website vor dem schließenden `</body>`-Tag ein. Stellen Sie sicher, dass Ihre Website gültiges HTML hat, damit das Snippet funktioniert.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
     - Für Single Page Applications stellen Sie sicher, dass `spa: true` in der Konfiguration für die automatische Routenverfolgung steht (hash-basierte Router werden nicht unterstützt).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
     - Beispiel für Nuxt-Apps: Verwenden Sie den `useScriptCloudflareWebAnalytics` Composable oder fügen Sie den Token zu Ihrer Nuxt-Konfiguration für globales Laden hinzu.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
   - **Edge Analytics (Für geproxte Websites)**:
     - Proxyn Sie Ihre Website über Cloudflare, indem Sie Ihre DNS-Einstellungen so aktualisieren, dass sie auf die Nameserver von Cloudflare verweisen. Dies kann in Minuten erledigt werden und erfordert keine Code-Änderungen.[](https://www.cloudflare.com/en-in/web-analytics/)
     - Metriken erscheinen im Cloudflare-Dashboard unter **Analytics & Logs**.[](https://developers.cloudflare.com/web-analytics/faq/)
   - **Cloudflare Pages**:
     - Für Pages-Projekte aktivieren Sie Web Analytics mit einem Klick: Wählen Sie unter **Workers & Pages** Ihr Projekt aus, gehen Sie zu **Metrics** und klicken Sie auf **Enable** unter Web Analytics.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/get-started/)

4. **Überprüfen Sie die Einrichtung**:
   - Es kann einige Minuten dauern, bis Daten im Dashboard erscheinen. Überprüfen Sie den Abschnitt **Web Analytics Sites**, um zu bestätigen, dass die Website hinzugefügt wurde.[](https://developers.cloudflare.com/web-analytics/get-started/)
   - Wenn Sie Edge Analytics verwenden, stellen Sie sicher, dass die DNS-Verteilung abgeschlossen ist (kann 24–72 Stunden dauern).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)

5. **Konfigurieren Sie Regeln (Optional)**:
   - Richten Sie Regeln ein, um bestimmte Websites oder Pfade zu verfolgen. Verwenden Sie Dimensionen, um Metriken zu kategorisieren (z. B. nach Hostname oder URL).[](https://developers.cloudflare.com/web-analytics/)

#### Hinweise
- Wenn Ihre Website einen `Cache-Control: public, no-transform`-Header hat, wird der JavaScript Beacon nicht automatisch injiziert und Web Analytics funktioniert möglicherweise nicht. Passen Sie Ihre Cache-Einstellungen an oder fügen Sie das Snippet manuell hinzu.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
- Einige Ad-Blocker können den JavaScript Beacon blockieren, aber Edge Analytics sind davon nicht betroffen, da sie auf Server-Logs angewiesen sind.[](https://developers.cloudflare.com/web-analytics/faq/)
- Für die manuelle Einrichtung meldet der Beacon an `cloudflareinsights.com/cdn-cgi/rum`; für geproxte Websites verwendet er den `/cdn-cgi/rum`-Endpunkt Ihrer Domain.[](https://developers.cloudflare.com/web-analytics/faq/)

### Verwendung von Cloudflare Web Analytics
1. **Zugriff auf das Dashboard**:
   - Melden Sie sich im Cloudflare-Dashboard an, wählen Sie Ihr Konto und Ihre Domain aus und gehen Sie zu **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/analytics/types-of-analytics/)
   - Sehen Sie sich Metriken wie Seitenaufrufe, Besuche, Top-Seiten, Verweise, Länder, Gerätetypen und Leistungsdaten (z. B. Seitenladezeiten, Core Web Vitals) an.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)

2. **Filtern und Analysieren von Daten**:
   - Verwenden Sie Filter, um sich auf bestimmte Metriken zu konzentrieren (z. B. nach Hostname, URL oder Land).
   - Zoomen Sie in Zeiträume hinein, um Traffic-Spitzen zu untersuchen, oder gruppieren Sie Daten nach Metriken wie Verweisen oder Seiten.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - Für fortgeschrittene Benutzer: Fragen Sie Daten über die **GraphQL Analytics API** ab, um benutzerdefinierte Dashboards zu erstellen.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)

3. **Verstehen Sie die wichtigsten Metriken**:
   - **Seitenaufrufe**: Die Gesamtzahl, wie oft eine Seite geladen wird (HTML Content-Type mit erfolgreicher HTTP-Antwort).[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)
   - **Besuche**: Seitenaufrufe von einem anderen Verweis (der nicht dem Hostname entspricht) oder von direkten Links.[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - **Eindeutige Besucher**: Basierend auf IP-Adressen, aber aus Datenschutzgründen nicht gespeichert. Kann aufgrund von Bot-Traffic oder fehlender JavaScript-basierter Deduplizierung höher sein als bei anderen Tools.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)
   - **Leistungsmetriken**: Einschließlich Seitenladezeiten, First Paint und Core Web Vitals (nur clientseitig).[](https://usefathom.com/features/vs-cloudflare-web-analytics)

4. **Vergleichen Sie mit anderen Tools**:
   - Im Gegensatz zu Google Analytics verfolgt Cloudflare keine Nutzerwege oder Conversion, schließt aber Bot- und Bedrohungs-Traffic ein, was die Zahlen aufblähen kann (20–50 % des Traffics für die meisten Websites).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.cloudflare.com/insights/)
   - Im Vergleich zu Plausible oder Fathom Analytics sind Cloudflares Daten aufgrund von Stichproben und begrenzter Aufbewahrung weniger granular.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
   - Edge Analytics können höhere Zahlen anzeigen als clientseitige Tools wie Google Analytics, die Bots und Nicht-JavaScript-Anfragen ausschließen.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/CloudFlare/comments/1alzkwm/why_are_my_cloudflare_traffic_stats_so_different/)

### Best Practices
- **Wählen Sie die richtige Methode**: Verwenden Sie den JavaScript Beacon für datenschutzorientierte, clientseitige Metriken oder Edge Analytics für umfassende serverseitige Daten, wenn Ihre Website geproxyt wird.[](https://www.cloudflare.com/web-analytics/)
- **Kombinieren Sie mit anderen Tools**: Kombinieren Sie es mit Google Analytics oder datenschutzorientierten Alternativen wie Plausible oder Fathom für tiefere Einblicke, da Cloudflares Analysen grundlegend sind.[](https://www.cloudflare.com/insights/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Überwachen Sie die Leistung**: Verwenden Sie Leistungsmetriken, um langsam ladende Seiten zu identifizieren, und nutzen Sie die Empfehlungen von Cloudflare (z. B. Cache-Optimierungen).[](https://developers.cloudflare.com/web-analytics/)
- **Prüfen Sie auf Ad-Blocker-Probleme**: Wenn Sie den JavaScript Beacon verwenden, informieren Sie die Benutzer, dass sie `cloudflare.com` erlauben oder Ad-Blocker deaktivieren müssen, um die Datenerfassung zu gewährleisten.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
- **Überprüfen Sie Daten regelmäßig**: Prüfen Sie das Dashboard häufig, um Trends oder Anomalien zu erkennen, da Daten nur 30 Tage lang aufbewahrt werden.[](https://plausible.io/vs-cloudflare-web-analytics)

### Problembehandlung
- **Es werden keine Daten angezeigt**:
  - Vergewissern Sie sich, dass das JavaScript-Snippet korrekt platziert ist und die Website gültiges HTML hat.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
  - Für Edge Analytics stellen Sie sicher, dass der DNS auf Cloudflare zeigt (die Verteilung kann 24–72 Stunden dauern).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
  - Prüfen Sie, ob `Cache-Control: no-transform`-Header die automatische Beacon-Injektion blockieren.[](https://developers.cloudflare.com/web-analytics/get-started/)
- **Ungenau Statistiken**:
  - Edge Analytics schließen Bot-Traffic ein, was die Zahlen aufbläht. Verwenden Sie clientseitige Analysen für genauere Besucherzahlen.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
  - Daten-Stichproben (10 %) können zu Diskrepanzen führen. Berücksichtigen Sie dies beim Vergleich mit anderen Tools.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Ad-Blocker-Probleme**: Einige Browser-Erweiterungen blockieren den JavaScript Beacon. Edge Analytics sind immun dagegen.[](https://developers.cloudflare.com/web-analytics/faq/)
- **Fehlende SPA-Metriken**: Stellen Sie sicher, dass die SPA-Unterstützung aktiviert ist (`spa: true`) und vermeiden Sie hash-basierte Router.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### Erweiterte Verwendung
- **GraphQL Analytics API**: Für benutzerdefinierte Analysen, fragen Sie die Cloudflare-API ab, um maßgeschneiderte Dashboards zu erstellen oder mit anderen Systemen zu integrieren. Erfordert technisches Know-how.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)
- **Cloudflare Workers**: Senden Sie Analysedaten an eine Time-Series-Datenbank zur benutzerdefinierten Verarbeitung oder verwenden Sie Workers für erweiterte serverlose Analysen.[](https://developers.cloudflare.com/analytics/)
- **Sicherheitseinblicke**: Kombinieren Sie es mit Cloudflares Security Analytics, um Bedrohungen und Bots parallel zu Besucherdaten zu überwachen.[](https://www.cloudflare.com/insights/)[](https://developers.cloudflare.com/waf/analytics/security-analytics/)

### Vergleich mit Alternativen
- **Google Analytics**: Bietet detailliertes Tracking von Nutzerwegen und Conversion, verlässt sich aber auf Cookies und JavaScript, die blockiert werden können. Cloudflare ist einfacher und datenschutzorientiert, aber weniger funktionsreich.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Plausible Analytics**: Open-Source, datenschutzorientiert, mit unbegrenzter Datenaufbewahrung und ohne Stichproben. Genauer für eindeutige Besucher, erfordert aber einen kostenpflichtigen Plan.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Fathom Analytics**: Ähnlich wie Plausible, mit exportierbaren Daten und erweiterten Funktionen wie Kampagnen-Tracking. Cloudflares kostenloses Angebot ist weniger robust, aber einfacher für grundlegende Bedürfnisse einzurichten.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Jetpack Stats**: WordPress-spezifisch, mit begrenzter Datenaufbewahrung (28 Tage) und keinem Tracking auf Benutzerebene. Ähnlicher Datenschutzfokus, aber weniger flexibel als Cloudflare.[](https://wordpress.com/support/stats/)

### Zusätzliche Ressourcen
- **Offizielle Dokumentation**: [Cloudflare Web Analytics Docs](https://developers.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
- **Einrichtungsanleitung**: [Enabling Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/get-started/)
- **FAQ**: [Cloudflare Web Analytics FAQs](https://developers.cloudflare.com/web-analytics/faq/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **Blog-Beitrag**: [Cloudflare’s Privacy-First Web Analytics](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Community-Support**: Besuchen Sie die Community-Foren von Cloudflare für zusätzliche Hilfe.[](https://developers.cloudflare.com/web-analytics/faq/)

### Fazit
Cloudflare Web Analytics ist eine ausgezeichnete Wahl für Website-Betreiber, die ein kostenloses, datenschutzorientiertes Analysetool mit minimalem Einrichtungsaufwand suchen. Es ist ideal für die grundlegende Überwachung von Traffic und Leistung, kann aber für fortgeschrittene Anforderungen aufgrund von Daten-Stichproben, begrenzter Aufbewahrung und dem Fehlen von Funktionen wie Conversion-Tracking zu kurz greifen. Für tiefere Einblicke sollten Sie es mit Tools wie Plausible oder Fathom Analytics kombinieren. Überprüfen Sie immer die Genauigkeit der Einrichtung und seien Sie sich der Einschränkungen bei der Dateninterpretation bewusst.

Wenn Sie spezielle Hilfe bei der Einrichtung benötigen oder Fragen zur Integration von Cloudflare Web Analytics in Ihre Website haben, lassen Sie es mich wissen!