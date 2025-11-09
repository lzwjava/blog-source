---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Clash-Proxy-Nachfolger und Linux-Unterstützung
translated: true
type: note
---

Clash, ein regelbasiertes Proxy-Tool ähnlich wie Shadowsocks, hatte sein ursprüngliches Repository, das 2023 vom Autor aufgrund regulatorischer Druck in China gelöscht wurde. Die Community hat die Entwicklung durch Forks und Nachfolger wie Clash.Meta (jetzt offiziell Mihomo genannt) fortgesetzt, welches weithin als der zuverlässigste und aktiv gepflegte Ersatz angesehen wird. Es unterstützt Linux-Binärdateien, auch für Ubuntu, und beinhaltet Funktionen wie DNS over HTTPS (DoH), Tunneling und regelbasiertes Routing.

Für ein zuverlässiges GitHub-Repository für Linux/Ubuntu empfehle ich das Hauptfortführungsprojekt. Hier ist eine Zusammenfassung der besten Optionen basierend auf Community-Akzeptanz, Updates und Linux-Unterstützung:

### Empfohlene Repositories
- **MetaCubeX/mihomo (Clash.Meta Core)**: Dies ist der primäre Nachfolger von Clash, der nach der ursprünglichen Löschung von der Community geforkt und gepflegt wird. Es bietet vollständige Proxy-Funktionalität, häufige Updates und vorgefertigte Binärdateien für Linux (x86_64 und arm64). Die Ubuntu-Kompatibilität ist exzellent, wobei Binärdateien über Version 18.04+ getestet wurden. Es ist Open-Source, werbefrei und hochgradig anpassbar über YAML-Konfigurationsdateien.
  - GitHub: https://github.com/MetaCubeX/mihomo
  - Warum zuverlässig: Über 14k Sterne, aktive Community, und Binärdateien beinhalten GeoIP-Datenbanken für das Routing. Direkte Download-Links für Linux-CLI-Binärdateien im Releases-Bereich.
  - Installation für Ubuntu: Laden Sie die neueste "mihomo-linux-amd64"-Binärdatei aus den Releases herunter, machen Sie sie ausführbar (`chmod +x mihomo`) und führen Sie sie aus. Erfordert eine config.yaml-Datei mit Proxy-Regeln. [1][2]
  - Alternativen, falls der Core nicht geeignet ist:
    - **CarlDegio/verge**: Ein Tauri-basierter GUI-Wrapper für Clash.Meta, der ein intuitives Dashboard für Linux (einschließlich Ubuntu) bereitstellt. Baut stabil auf Mihomo auf.
      - GitHub: https://github.com/CarlDegio/verge
      - Warum zuverlässig: GUI-Unterstützung für den Desktop, über 2k Sterne, einfacher Profilwechsel und System-Tray-Symbol. Laden Sie das AppImage für Ubuntu herunter. [3]
    - **chen08209/FlClash**: Multi-Plattform-Client (einschließlich Linux-Binärdateien) basierend auf Clash.Meta. Konzentriert sich auf Einfachheit und werbefreies Design, mit einer einfachen Schnittstelle für die Konfiguration.
      - GitHub: https://github.com/chen08209/FlClash
      - Warum zuverlässig: Leichtgewichtig, unterstützt Ubuntu via deb/AppImage-Builds und integriert Mihomo-Bindings. [4]
  - Für Legacy-Backups: Kuingsmile/clash-core bietet archivierte Builds des Pre-Deletion-Cores, mit Releases für Linux-Downloads, falls Sie eine ungepflegte, aber historische Version bevorzugen. [5]

### Zusätzliche Hinweise
- **Installationstipps**: Stellen Sie sicher, dass Sie libc (glibc 2.17+) für Ubuntu haben. Verwenden Sie Tools wie `systemd` oder `screen`, um es als Hintergrunddienst auszuführen. Überprüfen Sie Downloads gegen SHA256-Hashes für die Sicherheit.
- **Zuverlässigkeitskriterien**: Diese Repos haben aktive Beiträge, große Nutzerbasen (hohe Sterne/Forks) und vermeiden die Risiken verwaister Projekte nach 2023. Clash.Premin (wahrscheinlich ein Tippfehler für Premium) ist ein bezahlter Fork, aber nicht so Open-Source-lastig.
- **Rechtliche/Nutzungshinweise**: Clash dient zur Umgehung von Zensur; stellen Sie die Einhaltung lokaler Gesetze sicher, da seine Nutzung in eingeschränkten Regionen Aufmerksamkeit erregen kann.
- Wenn Sie eine UI oder spezifische Funktionen benötigen (z.B. Multi-Plattform), sind verge oder FlClash benutzerfreundlicher als der Mihomo-Core-CLI. Für Details lesen Sie die README jedes Repos. Bei Problemen hat das Mihomo-Repo eine umfangreiche Dokumentation. [6][7][1][8]

Wenn nichts passt oder Sie eine Schritt-für-Schritt-Anleitung für Ubuntu benötigen, geben Sie bitte mehr Details an!

Zitate:
[1] https://github.com/djoeni/Clash.Meta
[2] https://discussion.fedoraproject.org/t/rhbz-2305079-review-request-clash-meta-a-rule-based-network-proxy-tool-aka-mihomo/146312
[3] https://github.com/CarlDegio/verge
[4] https://github.com/chen08209/FlClash
[5] https://github.com/Kuingsmile/clash-core/releases
[6] https://github.com/fengwz17/Clash-For-Ubuntu
[7] https://news.ycombinator.com/item?id=38126160
[8] https://github.com/hiddify/Clash.Meta