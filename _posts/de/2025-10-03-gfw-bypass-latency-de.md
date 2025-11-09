---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Optimierung von GFW-Umgehung und Latenz
translated: true
type: note
---

Danke, dass du dein Setup und deine Erfahrungen teilst – klingt nach einer durchdachten Entwicklung von deinem anfänglichen Proxy-Skript und der VPN-Kombination hin zum Macau-SIM-Ansatz für den direkten Mobilfunkzugang. Es ist toll zu hören, dass es seit ein paar Monaten gut funktioniert, besonders mit dem Python-Skript, das die Proxy-Auswahl automatisiert (Priorisierung von Singapur für KI-Tools) und dass du bei zhs.cloud für das VPN auf deinem Laptop geblieben bist. Das SIM-Datenpaket (Macau-Karte für 150 CNY/Monat für 20GB plus Extras) scheint eine solide mobile Lösung zu sein, um GFW-Beschränkungen zu umgehen, ohne ständigen App-Overhead.

Deine Erkenntnisse, dass die Macau-SIM für GFW-gesperrte Seiten am schnellsten ist, machen Sinn – direkte Mobilfunk-IPs aus Macau umgehen geopolitische Blöcke oft besser als Optionen aus HK oder dem Festland, besonders für Dienste wie ChatGPT oder Claude, die regionale Beschränkungen haben. Das Routing spezifischer Enabler (z.B. ChatGPT zu USA-Proxys) in Shadowrocket ist eine clevere Anpassung, aber ja, die pauschale Proxy-Verzögerung bei jeder Netzwerkanfrage ist ein häufiger Schmerzpunkt auf iOS. Shadowrocket (oder Surge) kann träge werden, wenn es zu viel Verkehr abfängt, was zu höherer Latenz bei Apps wie Twitter/X führt, selbst wenn sie nicht vollständig blockiert sind.

Hier ist etwas Feedback und einige Vorschläge basierend auf deinen Notizen – mit Fokus auf Optimierungen, während es praktisch bleibt:

### Shadowrocket-Optimierungen
- **Regelverfeinerung für weniger Verzögerung**: Versuche anstelle eines breiten Proxy-für-alles-Setups, deine Regeln zu straffen, um die Abfangrate zu minimieren. Verwende zum Beispiel den folgenden Ablauf in der Shadowrocket-Konfiguration:
  - **DIRECT**: Standard für lokalen/regionalen Verkehr (z.B. WeChat, Baidu).
  - **Proxy/Reject**: Whitelist nur die hochpriorisierten, GFW-gesperrten Domains (z.B. erlaube ChatGPT, Claude, Google und ein paar andere, die über USA-Proxys geroutet werden).
  - Beispielregeln (in einer `.conf`-Datei):
    ```
    [Rule]
    DOMAIN-KEYWORD,chatgpt.com,PROXY
    DOMAIN-KEYWORD,claude.ai,PROXY
    DOMAIN-KEYWORD,google.com,PROXY
    DOMAIN-KEYWORD,twitter.com,PROXY  # Nur falls ChatGPT/etc. darauf zugreifen
    MATCH,DIRECT  # Catch-all, um nicht blockierten Verkehr vom Proxy wegzuleiten
    ```
    Auf diese Weise gehen nur ausgewählte Seiten/Apps durch die USA-Proxy-Kette, was die Gesamtverzögerung reduziert. Du kannst diese in Clash oder Shadowrocket-Managern wie Stash oder Quantumult X generieren oder bearbeiten, um die Anpassung zu erleichtern.
- **Latenz testen**: Führe nach dem Hinzufügen der Regeln Geschwindigkeitstests (z.B. via Fast.com oder Ookla) mit Shadowrocket ein-/ausgeschaltet durch. Wenn Verzögerungen bestehen bleiben, ziehe in Betracht, die Proxy-Kettenlänge zu reduzieren – ein Hop (z.B. ein US-abhängiger Proxy) könnte gegenüber Multi-Tier-Setups ausreichen.

### Alternative Tools für einfacheren iOS-Zugang
Falls der Overhead von Shadowrocket zu hoch ist (besonders, da du erwähnt hast, es nach einem Tag fallengelassen zu haben), hier sind Optionen mit geringer Reibung, die deine direkte Macau-SIM-Nutzung widerspiegeln:
- **VPN-Apps mit On-Demand-Regeln**: Etwas wie ExpressVPN oder NordVPN hat iOS-Funktionen für app-spezifisches Routing (aktiviere VPN nur für ChatGPT, Mistral, etc.), ohne alles zu proxyn. Es integriert sich nahtlos mit Mobilfunkdaten.
- **Clash für iOS (via Apps wie Surge oder Stash)**: Wenn dir die Logik deines Desktop-Python-Skripts gefällt, portiere eine vereinfachte Clash-Konfiguration auf iOS. Verwende einen Regelsatz, der mit "DIRECT" beginnt und nur ausgewählte Domains proxyt – weniger Verzögerung als Full-Proxy, und du kannst Macau-IPs priorisieren, falls dein Anbieter dies unterstützt.
- **Direkte Mobilfunk-Proxys via SIM**: Da du für Mistral und Grok auf die Macau-SIM setzt, ist das schlau für reine Geschwindigkeit. Wenn du KI-Tools auf dem Handy brauchst, prüfe, ob Mistral/Grok Macau-freundliche IPs haben, oder versuche den Zugriff über Inkognito-Modi, um app-basiertes Routing ganz zu vermeiden.

### Allgemeinere Tipps
- **Akku/Latenz auf iOS**: Längerer Proxy-Gebrauch kann den Akku schneller entleeren. Überwache es mit Bordmitteln und ziehe geplantes Ein-/Ausschalten in Betracht (z.B. Proxy nur zu Stoßzeiten).
- **Anbieterstabilität**: zhs.cloud scheint zuverlässig für deine VPN-Bedürfnisse zu sein – bleib dabei für den Laptop, aber prüfe auch auf iOS-VPN-Apps, falls du erweiterst. Für die SIM sind Macau-Anbieter wie CTM solide, aber behalte die Datenvolumengrenzen im Auge.
- **Langfristige Tragfähigkeit**: Die Vorsicht für den Fall, dass du China verlässt, ist gut – kombiniere dies mit einem globalen eSIM oder Roaming-Tarif als Backup. Behalte politische Veränderungen im Auge, da Zugangstools vergänglich sein können.

Falls du auf spezifische Konfigurationsprobleme stößt (z.B. beim Teilen deiner Shadowrocket-Regeldatei) oder Skript-Anpassungen für Clash möchtest, kannst du gerne mehr Details dalassen – ich kann helfen, ohne es zu kompliziert zu machen. Bleib sicher da draußen! 🚀