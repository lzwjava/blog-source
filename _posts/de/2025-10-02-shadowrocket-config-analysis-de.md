---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Analyse der Shadowrocket-Konfigurationsdatei
translated: true
type: note
---

Dies scheint eine Konfigurationsdatei für Shadowrocket zu sein, eine regelbasierte Proxy-App für iOS (ähnlich Tools wie Surge oder Quantumult). Sie ist als textbasierte Konfigurationsdatei strukturiert, die definiert, wie die App Datenverkehr routet, DNS behandelt, Regeln anwendet und Rewrites oder MITM-Abfänge (Man-in-the-Middle) durchführt. Die Datei ist mit "2025-10-02 20:25:43" datiert, was ein Zeitstempel oder Platzhalter sein könnte.

Ich werde sie Abschnitt für Abschnitt erklären, jeden Teil aufschlüsseln, was er tut und warum er so konfiguriert sein könnte. Diese Konfiguration scheint für Nutzer in Regionen mit Internetbeschränkungen (z.B. China) optimiert zu sein, indem bestimmte globale/blockierte Dienste über einen Proxy-Server geleitet werden, während lokaler/inländischer Traffic direkt für bessere Geschwindigkeit und zur Vermeidung unnötiger Umleitung bleibt. Es ist kein komplettes Setup – man müsste einen Proxy-Server (z.B. via Shadowsocks, V2Ray, etc.) separat in der App konfigurieren, und diese Konfiguration verweist auf externe Regelsätze, die sich automatisch von GitHub aktualisieren.

### Wichtige Annahmen und Hinweise
- **Proxy-Setup**: Diese Konfiguration setzt voraus, dass man einen funktionierenden Proxy-Server in Shadowrocket konfiguriert hat (z.B. SOCKS5, HTTP oder verschlüsselte Protokolle). Ohne diesen funktionieren "PROXY"-Regeln nicht.
- **Zweck**: Sie scheint zur Umgehung von Zensur (z.B. Great Firewall in China) gedacht zu sein. KI-Dienste (wie OpenAI/ChatGPT) werden über den Proxy geleitet, während chinesische Domains/IPs direkt gehen, um Drosselung zu vermeiden.
- **TUN-Modus**: Verweise auf "tun" (Tunnel-Modus) für das Routen des gesamten Datenverkehrs durch das Gerät.
- **Externe Abhängigkeiten**: Einige Regeln laden von GitHub-URLs (z.B. Regel-Listen). Stelle sicher, dass du diesen Quellen vertraust, da sie sich automatisch aktualisieren können.
- Falls etwas unklar ist oder du Hilfe bei der Anwendung brauchst, teile mir Details zu deinem Setup mit.

### Abschnittsaufschlüsselung

#### **[General]**
Dies legt globale App-Verhalten, DNS-Auflösung und Netzwerk-Routing fest. Es ist wie die "Einstellungen" oder "Systemeinstellungen" für Shadowrocket.

- `bypass-system = true`: Ignoriere die System-Proxy-Einstellungen von iOS. Shadowrocket handhabt das gesamte Proxying selbst, anstatt sich auf systemweite Konfigurationen zu verlassen.

- `skip-proxy = 192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,captive.apple.com,*.ccb.com,*.abchina.com.cn,*.psbc.com,www.baidu.com`: Eine kommagetrennte Liste von Domains/IP-Bereichen, die **immer direkt** geroutet werden (kein Proxy). Dies beinhaltet:
  - Private Netzwerke (z.B. Heim-WLAN-IPs wie 192.168.x.x).
  - Lokale Domains (*.local) und localhost.
  - Apples Captive Portal Check.
  - Chinesische Bankdomains (*.ccb.com für China Construction Bank, *.abchina.com.cn für Agricultural Bank of China, *.psbc.com für Postal Savings Bank).
  - Baidu (www.baidu.com), eine große chinesische Suchmaschine.
  - *Warum?* Inländische chinesische Seiten (besonders Banken und Suchmaschinen) sind ohne Proxy erreichbar und könnten gedrosselt oder markiert werden, wenn sie über einen Proxy geleitet werden.

- `tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32, 239.255.255.250/32`: Im Tunnel-(TUN)-Modus sind diese IP-Bereiche **vom Proxy-Tunnel ausgeschlossen**. Dies verhindert Störungen mit lokalem/Routing-Datenverkehr wie Loopback-IPs, Multicast und Testbereichen.

- `dns-server = https://doh.pub/dns-query,https://dns.alidns.com/dns-query,223.5.5.5,119.29.29.29`: Priorisierte Liste von DNS-Resolvern für Proxy-Datenverkehr. Dies sind DoH-Server (DNS over HTTPS) und Plain-DNS (Tencent's 119.29.29.29 und Aliyun's 223.5.5.5). Es beginnt mit verschlüsselten/öffentlichen Servern (doh.pub und alidns.com) für Privatsphäre/Sicherheit.

- `fallback-dns-server = system`: Wenn der primäre DNS fehlschlägt, falle auf den iOS-System-DNS zurück.

- `ipv6 = true`: Aktiviere IPv6-Unterstützung. `prefer-ipv6 = false`: Bevorzuge IPv4 gegenüber IPv6 für Verbindungen (z.B. Stabilität oder Kompatibilität).

- `dns-direct-system = false`: Verwende den System-DNS nicht für Direktverbindungen – verwende stattdessen den konfigurierten DNS.

- `icmp-auto-reply = true`: Antworte automatisch auf ICMP-Anfragen (Ping). Nützlich für Konnektivitätsprüfungen.

- `always-reject-url-rewrite = false`: Erlaube URL-Rewrites (später in der Konfiguration verwendet).

- `private-ip-answer = true`: Erlaube DNS-Antworten mit privaten IPs (z.B. dein Router).

- `dns-direct-fallback-proxy = true`: Wenn eine direkte DNS-Abfrage fehlschlägt, versuche es erneut über den Proxy.

- `tun-included-routes = `: (Leer) Keine benutzerdefinierten Routen im TUN-Modus enthalten – verwende Standardwerte.

- `always-real-ip = `: (Leer) Keine erzwungene Offenlegung der echten IP – Standardverhalten.

- `hijack-dns = 8.8.8.8:53,8.8.4.4:53`: Fange DNS-Datenverkehr von Googles öffentlichem DNS (8.8.8.8/8.8.4.4 auf Port 53) ab und leite ihn über den Proxy. Dies erzwingt die Verwendung des konfigurierten DNS anstelle öffentlicher Server, die blockiert oder überwacht sein könnten.

- `udp-policy-not-supported-behaviour = REJECT`: Wenn UDP-Datenverkehr nicht von einer Richtlinie unterstützt wird, lehne ihn ab, anstatt ihn zuzulassen.

- `include = `: (Leer) Keine zusätzlichen Konfigurationsdateien eingebunden.

- `update-url = `: (Leer) Keine automatischen Konfigurations-Updates von einer URL.

#### **[Rule]**
Dies definiert Datenverkehrs-Routing-Regeln, die in Reihenfolge verarbeitet werden. Es ist wie eine ACL (Access Control List), die Shadowrocket mitteilt, was zu proxyn ist, was direkt gesendet werden soll, basierend auf Domains, Keywords, GEOIP, etc. Wenn keine Regel zutrifft, fällt es auf `FINAL,DIRECT`.

- `DOMAIN-SUFFIX,anthropic.com,PROXY`: Leite alle Subdomains von anthropic.com über den Proxy (z.B. api.anthropic.com). Anthropic ist ein KI-Unternehmen – wahrscheinlich zur Umgehung von Blocks.

- `DOMAIN-SUFFIX,chatgpt.com,PROXY`: Leite ChatGPT-Domains über den Proxy. ChatGPT ist oft in bestimmten Regionen eingeschränkt.

- `DOMAIN-SUFFIX,openai.com,PROXY`: Leite OpenAI-Domains über den Proxy (ähnlicher Grund).

- `DOMAIN-SUFFIX,googleapis.com,PROXY`: Leite Googles API-Dienste über den Proxy (könnte für den indirekten Zugriff auf Google-Dienste sein).

- `DOMAIN-SUFFIX,zhs.futbol,DIRECT`: Leite diese spezifische Domain (wahrscheinlich eine Sportseite auf Spanisch/Chinesisch) direkt.

- `RULE-SET,https://github.com/lzwjava/lzwjava.github.io/raw/refs/heads/main/scripts/auto-ss-config/AI.list,PROXY`: Lade einen externen Regelsatz von GitHub (eine Liste von KI-bezogenen Domains) und proxy sie. Dies aktualisiert und erweitert die KI-Proxy-Regeln automatisch.

- `RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Lan/Lan.list,DIRECT`: Lade einen Regelsatz für lokale Netzwerk-(LAN)-Domains und leite sie direkt. Vermeidet das Proxying von Heim-/internem Datenverkehr.

- `DOMAIN-KEYWORD,cn,DIRECT`: Jede Domain, die das Keyword "cn" enthält (z.B. irgendetwas.cn), geht direkt. Nützlich für chinesische Seiten.

- `GEOIP,CN,DIRECT`: Jede IP, die nach China (CN) geolokalisiert ist, geht direkt. Verhindert das Proxying von inländischem Datenverkehr, der schnell und uneingeschränkt ist.

- `FINAL,DIRECT`: Standardaktion – wenn keine Regel zutrifft, route direkt. Hält den meisten Datenverkehr für Effizienz ungeproxyt.

*Gesamteffekt*: Dies ist ein "Proxy für blockierte Globals"-Setup. KI/ChatGPT/OpenAI-Datenverkehr wird gezwungen, über VPN/Proxy zu gehen, um regionale Beschränkungen zu umgehen, während chinesisches/lokales Zeug direkt bleibt.

#### **[Host]**
Manuelle Host-Zuordnungen (wie eine lokale Hosts-Datei).

- `localhost = 127.0.0.1`: Mappe "localhost" auf die Loopback-IP. Standard – stellt sicher, dass die App auf lokale Dienste verbinden kann.

#### **[URL Rewrite]**
Schreibt eingehende URLs um, bevor Anfragen gemacht werden. Verwendet Regex-Matching.

- `^https?://(www.)?g.cn https://www.google.com 302`: Schreibe jede HTTP/HTTPS-URL für g.cn (oder www.g.cn) um, um auf google.com mit einem 302-Status (temporäre Weiterleitung) umzuleiten. g.cn ist Googles China-Domain – dies umgeht sie.

- `^https?://(www.)?google.cn https://www.google.com 302`: Dasselbe für google.cn zu google.com. China blockiert oder leitet google.com oft um, daher erzwingt dies eine saubere Weiterleitung.

*Warum?* In zensierten Regionen könnte google.cn veränderte/gesperrte Ergebnisse liefern. Dies stellt sicher, dass man die globale Google-Seite direkt erreicht.

#### **[MITM]**
Man-in-the-Middle-Einstellungen zum Abfangen und Modifizieren von HTTPS-Datenverkehr (erfordert ein Root-CA-Zertifikat in Shadowrocket).

- `hostname = *.google.cn`: Fange Datenverkehr für jede Subdomain von google.cn ab. Kombiniert mit dem URL-Rewrite könnte dies Datenverkehr für Google-CN-Domains entschlüsseln/umleiten.

*Warum?* Dies könnte sein, um die Rewrites durchzusetzen oder Zertifikat-Pinning-Probleme in China zu handhaben, wo google.cn andere Zertifikate verwendet.

### Wie man diese Konfiguration verwendet
1. **Importieren**: Importiere dies in Shadowrocket als Konfigurationsdatei.
2. **Proxy-Server**: Füge deinen tatsächlichen Proxy (z.B. Shadowsocks-Server) unter dem Abschnitt "Servers" hinzu – Regeln wie "PROXY" hängen davon ab.
3. **Aktivieren**: Wechsle zu dieser Konfiguration und aktiviere den Tunnel-Modus (VPN), falls nötig.
4. **CA-Zertifikat**: Für MITM installiere und vertraue dem CA von Shadowrocket, falls noch nicht geschehen.
5. **Testen**: Überprüfe Seiten wie whatismyipaddress.com, um zu sehen, ob IPs/Routing wie erwartet funktionieren. Überwache langsame chinesische Seiten.
6. **Fehlerbehebung**: Wenn Regelsätze nicht laden, könnten sie rate-limited oder geändert sein. IPv6-Präferenzen müssen möglicherweise für Konnektivität getoggelt werden.

### Mögliche Probleme/Sicherheitshinweise
- **Privatsphäre**: Offengelegte Regelsätze (GitHub-Links) könnten preisgeben, was du routest. MITM kann sensiblen Datenverkehr abfangen – verwende nur vertrauenswürdige CAs.
- **Updates**: Regelsätze laden automatisch; wenn GitHub blockiert ist, verwende einen Proxy für sie.
- **Zukünftiges Datum**: Die Konfiguration ist mit Okt 2025 beschriftet – könnte ein Tippfehler oder Zukunftssicherung sein, aber keine Funktionen hängen davon ab.
- **Legalität**: Proxying zur Zensurumgehung ist an manchen Orten in Ordnung, an anderen eingeschränkt – verwende auf eigenes Risiko.
- Wenn du Fehlerprotokolle teilst oder was du erreichen möchtest, kann ich Ratschläge verfeinern!