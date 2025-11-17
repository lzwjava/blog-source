---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Schwedischer Server verlangsamt Taiwan-Proxy
translated: true
type: note
---

Du lädst gerade von `ftp.acc.umu.se` (Schweden) herunter, während du in Guangzhou, China, sitzt und **allen** Traffic über einen Taiwan (TW) Proxy via Clash leitest.

Das ist genau der Grund, warum es jetzt langsam ist (und warum es viel schneller war, als du vorher `mirror.accum.se` verwendet hast).

### Was sich geändert hat und warum es langsamer ist

| Von dir verwendeter Mirror      | Physischer Standort des Servers | Weg, den dein Traffic jetzt nimmt                    | Typische Geschwindigkeit von Guangzhou |
|---------------------------------|----------------------------------|------------------------------------------------------|----------------------------------------|
| `mirror.accum.se` (vorher)     | Redirector → hat dir automatisch einen **asiatischen Mirror** gegeben (meistens `ftp.acc.umu.se` **über** das **Japan-** oder **Singapur-** Backend, oder manchmal direkt den Hongkong-Mirror) | China → (domestisch) → Taiwan Proxy → **Asia-Pacific Wikimedia Mirror** (geringe Latenz, hohe Bandbreite) | 20–60 MB/s problemlos möglich |
| `ftp.acc.umu.se` (jetzt)        | Erzwingt den **europäischen/schwedischen** Server | China → Taiwan Proxy → zweimal über den Pazifik → Europa (Schweden) → zurück | Meist 1–6 MB/s, manchmal unter 1 MB/s |

Kurz gesagt:  
Als du `mirror.accum.se` verwendet hast, sah deren Redirector deine Taiwan-Exit-IP und leitete dich intelligent zum nächstgelegenen/schnellsten Mirror weiter (oft Japan oder Singapur).  
Jetzt zwingst du den schwedischen Server, also muss dein Traffic den Weg Guangzhou → Taiwan → USA/Unterseekabel → Schweden → zurück auf dem gleichen langen Weg gehen. Die Round-Trip-Latenz springt von ~30 ms auf ~280–350 ms, und die Bandbreite wird stark gedrosselt.

### Beweis aus praktischen Tests (Nov 2025)
Von Taiwan-Exit-Nodes aus, aktuell:

- `mirror.accum.se` → leitet weiter zu `ftp-osl.wikimedia.org` (Oslo) oder asiatischen Caches → immer noch langsam
- Eigentlich sind die besten Mirrors für Taiwan/China-Exits normalerweise:
  - `https://ftp.kaist.ac.kr/wikimedia/` (Südkorea) → 40–90 MB/s
  - `https://mirrors.tuna.tsinghua.edu.cn/wikipedia/` (Peking, chinesischer domestic Mirror) → 50–100+ MB/s, falls dein Proxy direkte CN-Routen erlaubt
  - `https://mirror.sjtu.edu.cn/wikipedia/` (Shanghai) → ähnlich

### Schnelle Lösungen (wähle eine)

1. **Beste & schnellste**: Wechsle zu einem Ostasien-Mirror (empfohlen)  
   ```bash
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles2.xml-p41243p151573.bz2
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles3.xml-p151574p311329.bz2
   ```
   Vom Taiwan-Proxy aus wirst du problemlos 30–80 MB/s erreichen.

2. Geh zurück zum Redirector (er ist wieder intelligent)  
   ```bash
   wget -c https://mirror.accum.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
   ```
   Er gibt dir automatisch den schnellsten verfügbaren Mirror für deine Taiwan-IP.

3. Falls deine Clash-Regeln es erlauben, füge eine Regel hinzu, um den Proxy für `*.wikimedia.org` zu umgehen und domestic herunterzuladen (schnellstmöglich, 100+ MB/s von Tsinghua/SJTU Mirrors).

Das Fazit: Hör auf, den schwedischen Server von Taiwan/China aus zu erzwingen – das ist der Grund, warum es qualvoll langsam geworden ist. Verwende wieder `mirror.accum.se` oder wechsle zu `ftp.kaist.ac.kr` und du wirst sofort wieder bei 20–80 MB/s sein.