---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Leistungsleitfaden für Black Myth Wukong auf dem PC
translated: true
type: note
---

### Black Myth: Wukong auf deinem PC-Setup

Dein PC ist eine absolute Bestie – i9-13900KF, RTX 4070, 64 GB DDR5-RAM und schneller NVMe-Speicher bedeuten, dass du dieses Spiel bei 4K Ultra-Einstellungen mit aktiviertem Raytracing meistern wirst und problemlos 60+ FPS erreichst. Hier gibt es keine Engpässe; er liegt weit über den empfohlenen Specs (die eine RTX 2060 und einen i7-9700 fordern). Die Gesamtbaukosten (~14.000 CNY) sind ein solider Preis für ein High-End-System wie dieses.

Black Myth: Wukong ist ein Singleplayer-Action-RPG, inspiriert von *Die Reise nach dem Westen*, in dem du als der "Destined One" (ein Affenkrieger) spielst und in einem alten China gegen mythische Bosse kämpfst. Der Kampf ist souls-like (Ausweichen, Parieren, Ausdauermanagement), aber zugänglicher, mit flüssigen Kombos, Verwandlungen und Zauber-Upgrades. Erwarte 30-40 Stunden für die Hauptgeschichte, plus Exploration und NG+.

#### Brauchst du Windows? (Kurze Antwort: Nein)
- **Steam auf Ubuntu 22.04**: Steam läuft nativ unter Linux. Falls du es noch nicht installiert hast:
  1. Öffne ein Terminal und führe aus: `sudo apt update && sudo apt install steam`.
  2. Starte Steam, melde dich an und lass es Updates herunterladen.
- **Spielkompatibilität**: Black Myth: Wukong hat keine native Linux-Version (es ist nur für Windows), aber es läuft *einwandfrei* unter Linux via Proton (Valves Kompatibilitätsschicht, die in Steam integriert ist). Es hat eine **Platinum**-Bewertung auf ProtonDB, was "perfekte" Leistung ohne Anpassungen bedeutet. Nutzer berichten in einigen Fällen von besseren Bildraten und mehr Stabilität unter Linux als unter Windows, dank optimierter Proton-Versionen.
- **Mögliche Probleme**:
  - Es verwendet Denuvo DRM, was Proton-Versionswechsel als "neue Installation" flaggen könnte (was Aktivierungen limitiert). Bleibe bei einer Proton-Version, um dies zu vermeiden.
  - Seltene Abstürze beim Start? Erzwinge Proton Experimental in Steam (Rechtsklick auf Spiel > Eigenschaften > Kompatibilität > "Nutzung eines bestimmten Steam Play Kompatibilitätstools erzwingen" aktivieren > Proton Experimental auswählen).
- **Benchmark-Test**: Lade vor dem Kauf das kostenlose Black Myth: Wukong Benchmark Tool von Steam herunter – es läuft gut auf Proton und lässt dich dein Setup Stresstesten.
- Fazit: Bleib bei Ubuntu. Ein Windows-Dual-Boot ist übertrieben, es sei denn, du spielst andere Multiplayer-Spiele mit schwerem Anti-Cheat (dieses hier ist ein Singleplayer, also keine Probleme).

Wenn du *unbedingt* Windows für die absolute Spitzenoptimierung willst (z.B. 5-10 % bessere Leistung in Randfällen), ist ein Dual-Boot einfach einzurichten, aber hier unnötig.

#### So bekommst und spielst du es
1. **Kaufen & Installieren**:
   - Suche nach "Black Myth: Wukong" in Steam (App-ID: 2358720). Es kostet ~60 $ / ~430 CNY und ist oft im Sale.
   - Installationsgröße: ~130 GB, deine 1 TB SSD ist also mehr als ausreichend (HDD für Überlauf, falls nötig).
   - In Steam: Rechtsklick auf das Spiel > Eigenschaften > Kompatibilität > "Steam Play für alle anderen Titel aktivieren" > Proton Experimental auswählen.

2. **Steuerung (Tastatur/Maus Standard)**:
   - Verwende deine vorhandene Maus/Tastatur – sie ist reaktionsschnell, aber ein Controller (Xbox/PS) fühlt sich für Kombos natürlicher an.
   - **Bewegung**: WASD zum Bewegen, Leertaste zum Ausweichen/Springen, Umschalttaste zum Sprinten.
   - **Kampf**: Linksklick (Leichter Angriff), Rechtsklick (Schwerer Angriff), R (Parieren – Timing ist entscheidend!), Q/E (Zauber), F (Gegner für Finalschläge bewegungsunfähig machen).
   - **Ausdauer**: Angriffe/Ausweichen lassen einen blauen Balken schrumpfen – verwalte ihn wie in Dark Souls.
   - **Upgrades**: Sammle Will (Equivalent zu Seelen), um Fähigkeiten an Schreinen zu verbessern. Konzentriere dich auf Stäbe, Verwandlungen (z.B. werde ein Vogel für Luftangriffe) und Relikte.
   - Tasten in Einstellungen > Steuerung bei Bedarf neu belegen.

3. **Schnelle Tipps für einen starken Start**:
   - **Frühes Spiel**: Priorisiere Ausweichen vor Blockieren – Parieren kommt später. Erkunde die Umgebung nach versteckten Töpfen (sie lassen Beute fallen).
   - **Bosse**: Lerne Angriffsmuster; nutze Säulen als Deckung. Funken (Upgrades) sind versteckt – durchsuche höher und tiefer gelegene Bereiche.
   - **Leistung**: Stelle im Spiel die Voreinstellung auf "Sehr Hoch", DLSS auf Qualität (deine 4070 glänzt hier) und begrenze die FPS auf 60 für flüssiges Spielen.
   - **Audio/Untertitel**: Die englische Synchronisation ist solide, aber Chinesisch mit Untertiteln fängt den Mythos-Vibe besser ein.
   - Speichere oft an Hüter-Schreinen (Checkpoints).

Wenn du auf Probleme stößt (z.B. Controller-Einrichtung), sind Lutris oder Heroic Launcher Alternativen, aber Steam Proton ist die einfachste Lösung. Genieße die epischen Kämpfe – es ist eines der besten Spiele von 2024!

#### Referenzen
- [Black Myth: Wukong on Steam](https://store.steampowered.com/app/2358720/Black_Myth_Wukong/)
- [ProtonDB: Black Myth: Wukong](https://www.protondb.com/app/2358720)
- [Reddit: Wukong Benchmark on Proton](https://www.reddit.com/r/linux_gaming/comments/1er0biq/black_myth_wukong_has_a_free_benchmark_and_it/)
- [SteamDB: App Details](https://steamdb.info/app/2358720/)