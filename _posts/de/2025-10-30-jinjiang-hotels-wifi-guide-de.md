---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Jinjiang Hotels WLAN-Portal-Anleitung
translated: true
type: note
---

Das Jinjiang Hotels WiFi-Portal (https://portal.jinjianghotels.com.cn/) ist ein Captive Portal, das nur für den Zugang vor Ort konzipiert ist – es ist nicht vollständig öffentlich außerhalb des Hotelnetzwerks crawlbare, weshalb das direkte Aufrufen im Browser oft leere oder Fehlerseiten zurückgibt. Basierend auf Benutzerberichten und Anleitungen finden Sie hier eine Aufschlüsselung der typischen "Route"-Struktur (d.h. der Haupt-URL-Pfade/Endpunkte) und wie man auf sie zugreift. Dies ist üblich für Vienna Hotels (eine Jinjiang-Marke) und ähnliche Ketten in China.

### Hauptroute und Zugriffsmethode
- **Primäre Route**: Der Stammpfad `/` (d.h. https://portal.jinjianghotels.com.cn/ oder http://portal.jinjianghotels.com.cn/).
  - Dies ist die Landing Page, die automatisch geladen wird, wenn Sie versuchen, auf eine nicht-HTTPS-Website zuzugreifen, während Sie mit dem Hotel-WLAN verbunden sind.
  - **Zugriff**:
    1. Verbinden Sie Ihr Gerät mit der WLAN-SSID des Hotels (z.B. "ViennaHotel", "Jinjiang_Free" oder "Vienna_Free_WiFi" – zunächst ohne Passwort).
    2. Öffnen Sie einen Webbrowser und rufen Sie eine beliebige HTTP-Seite auf (z.B. http://neverssl.com oder http://172.16.16.1 – die lokale Gateway-IP aus Ihrer ersten Anfrage).
    3. Sie werden auf die Stammseite `/` des Portals weitergeleitet. Falls keine automatische Weiterleitung erfolgt, geben Sie manuell `http://172.16.16.1` oder die Portal-URL ein (verwenden Sie HTTP, nicht HTTPS, da Captive Portals HTTPS oft blockieren oder ignorieren).
  - Die Seite ist auf Chinesisch, aber einfach: Sie zeigt Hotel-Branding, Nutzungsbedingungen und Login-Schaltflächen an. Verwenden Sie die Browser-Übersetzung (z.B. die eingebaute von Chrome) für Englisch.

### Bekannte Unterrouten/Pfade
Das Portal verwendet eine minimale Struktur – meist eine Single-Page-App mit Formularübermittlungen anstelle tiefer Unterpfade. Es gibt keine öffentliche Dokumentation, die alle Endpunkte auflistet, aber aus Benutzervideos und Fehlerberichten sind folgende gängige Pfade bekannt:
- **SMS-Login-Pfad**: Wird über ein Formular auf der Stammseite `/` abgewickelt (kein separater `/sms`-Unterpfad; es ist eine POST-Anfrage an einen internen Endpunkt wie `/auth/sms` oder ähnlich).
  - **Zugriff/Verwendung**: Klicken Sie auf der Hauptseite auf die SMS-Schaltfläche (短信验证). Geben Sie Ihre Telefonnummer ein (+86 für China oder im internationalen Format). Ein Code wird per SMS gesendet; geben Sie ihn zur Authentifizierung ein. Der Zugang läuft nach 24 Stunden ab.
- **Social-Login-Pfade**: Links oder Iframes zu Drittanbieter-Endpunkten, z.B.:
  - Weibo/QQ-Login: Leitet weiter zu `/oauth/weibo` oder `/oauth/qq` (temporäre Unterrouten für Auth-Callback).
  - **Zugriff**: Klicken Sie auf der Stammseite auf die jeweilige Social-Media-Schaltfläche; es öffnet sich ein Popup oder es erfolgt eine kurze Weiterleitung.
- **Andere potenzielle Unterrouten** (abgeleitet aus ähnlichen Systemen; nicht für Jinjiang bestätigt):
  - `/terms` oder `/agreement`: Zum Anzeigen der vollständigen Nutzungsbedingungen (verlinkt aus der Fußzeile der Hauptseite).
  - `/logout`: Zum manuellen Trennen der Verbindung (selten verwendet).
  - Fehlerpfade wie `/error` oder 404 für ungültige Zugriffe.

Wenn Sie vor Ort sind und Unterrouten untersuchen möchten (z.B. für Dev-Tools), öffnen Sie die Browser-Entwicklerkonsole (F12) auf der Portalseite – dies kann AJAX-Aufrufe an Endpunkte wie `/api/verify` für die SMS-Übermittlung aufdecken.

### Fehlerbehebung beim Zugriff
- **Keine Weiterleitung?** Löschen Sie den Browser-Cache, vergessen Sie das WLAN und verbinden Sie sich erneut, oder schalten Sie die Mobilfunkdaten kurz an und aus.
- **Internationale Telefonnummer?** Funktioniert für die meisten, aber Codes können sich verzögern – fragen Sie an der Rezeption nach einem gemeinsamen Code.
- **Sicherheitshinweis**: Der gesamte Datenverkehr wird über das Gateway des Hotels geleitet (172.16.16.x-Bereich), verwenden Sie daher nach dem Login ein VPN.

Für visuelle Eindrücke sehen Sie sich kurze Douyin-Videos zum Thema "维也纳酒店 WiFi 登录" an, die den genauen Seitenablauf zeigen.

Referenzen:  
[Reddit: Issues with WiFi in China Hotels](https://www.reddit.com/r/travelchina/comments/1kjdngn/issues_with_wifi_connection/)  
[Douyin: Vienna Hotel WiFi Steps](https://www.douyin.com/search/%E7%BB%B4%E4%B9%9F%E7%BA%B3%E9%85%92%E5%BA%97Wi-Fi%E8%BF%9E%E6%8E%A5%E6%AD%A5%E9%AA%A4)  
[Douyin: Hotel WiFi Connection Guide](https://www.douyin.com/search/%E9%85%92%E5%BA%97%E6%97%A0%E7%BA%BF%E7%BD%91%E6%80%8E%E4%B9%88%E8%BF%9E%E6%8E%A5)