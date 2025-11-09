---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Gegensätzliche KI-Karrierewege
translated: true
type: note
---

Du triffst bei vielem genau ins Schwarze – es ist ein faszinierender Kontrast zwischen Lou Tianchengs Weg bei Pony.ai und jemandem wie Yang Zhilin bei Moonshot AI (der Mutterfirma von Kimi). Beide sind Elite-Talente aus Chinas Tech-Ökosystem (Lou ist der legendäre ICPC-Goldmedaillengewinner, oft als Chinas bester Wettbewerbsprogrammierer bezeichnet; Yang hat diesen tiefgehenden ML-Hintergrund von der Tsinghua University und Recurrent AI), aber ja, Pony hat momentan das Gefühl, mehr Gegenwind zu spüren im Vergleich zum LLM-Raketenschiff, auf dem Moonshot unterwegs ist. Lass mich meinen Standpunkt zu deinen Punkten darlegen, da du eine Menge scharfsinniger Beobachtungen aufgeführt hast.

### Der CP-zur-realen-Welt-Sprung: Übung vs. Chaos
Stimme völlig zu – ACM/ICPC und Competitive Programming (CP) sind brutale Meritokratien für *lösbare* Rätsel. Man paukt bekannte Muster, optimiert wie verrück, und "perfektes Üben" bringt einem Medaillen. Lou hat diese Welt dominiert (mehrere Goldmedaillen, eine Bestie im Weltfinale), aber wie du sagtest, die Realität überreicht einem kein Problemset mit Randbedingungen und Testfällen. Autopilot? Das sind unendliche Corner Cases: regnerische Reflexionen, die eine Fahrspurmarkierung in eine Disco-Kugel verwandeln, Spiegel, die LiDAR wie in einem Jahrmarkts-Spiegelhaus narren, oder dieser eine Fußgänger, der bei Rot geht, weil sein Hund ein Eichhörnchen gesehen hat. Jedes "kleine Detail" ist kein LeetCode-Medium – es ist ein mehrjähriges F&E-Schluckloch, das Physik-Simulationen, Sensor-Fusion-Anpassungen und reale Flottendaten erfordert, die sich nicht wie Textkorpora skalieren lassen.

Lou selbst hat in Interviews darüber gesprochen: Gutes AV ist nicht nur "das Rätsel lösen", es geht darum, menschliche Fahrer so nachzuahmen, dass es *sicher* *und* skalierbar ist, was herausragende Evaluierungssysteme erfordert (z. B. Sim-to-Real-Transfer, Simulation seltener Ereignisse). Aber selbst für algorithmische Durchbrüche wie Attention Mechanisms oder RLHF hast du recht – die LLM-Crowd brauchte *Jahre* der Iteration (Vaswanis Paper von 2017 bis GPT-3 im Jahr 2020), und das mit Ozeanen öffentlicher Daten. CP-Zauberer wie Lou glänzen durch Implementierungsgeschwindigkeit, aber Erfindungen von Grund auf in unbekanntem Terrain? Da schlagen die "Jahre, um ein Problem zu lösen" voll zu, besonders allein als Research Lead.

### Datenflaute vs. Text-Tsunami
Das ist die entscheidende Asymmetrie, die du auf den Punkt gebracht hast. LLMs wie Kimi schwelgen im Feuerstrahl des Internets – Billionen von Tokens aus Büchern, Code, Foren, alles autoregressives Gold. Moonshot kann darauf feintunen, mit Open-Source-Gewichten (Llama, etc.) bootstrappen und schnell MVPs ausliefern. Ergebnis? Kimi explodiert: Deren K2-Modell kam gerade im September mit massiven Kontextfenstern und Coding-Fähigkeiten auf den Markt und treibt das Nutzerwachstum an, das in China mit ChatGPT rivalisiert. Die Bewertung liegt jetzt bei 3,3 Mrd. USD, hoch von 2,5 Mrd. USD früher im Jahr, mit über 1,6 Mrd. USD, die von Alibaba, Tencent usw. eingesammelt wurden. Es ist der klassische KI-Hype-Zyklus: leicht erreichbare Früchte in der Gen-AI bedeuten schnelle Iterationen und Moonshot-Bewertungen.

Autonomes Fahren? Daten sind der Flaschenhals. Man kann nicht "alle regnerischen Straßen Pekings" scrapen wie arXiv-Papers. Pony verbrennt Geld mit proprietären Flotten (sie bauen ihre Gen-7-Robotaxis hoch, haben diesen Sommer 200+ Einheiten erreicht), aber die Skalierung auf "jeden Fall" bedeutet Milliarden für Kartierung, Annotation und Sicherheitsvalidierung. Die Einnahmen tröpfeln – 1,5 Mio. USD von Robotaxi im Q2 2025, ein Plus von 158 % im Vorjahresvergleich, aber das sind Peanuts im Vergleich zu LLM-Abonnement-Einnahmen. Ponys Börsenwert sank auf ~2 Mrd. USD (die Aktie ist volatil: +48 % Rally im Oktober, aber auch -9 % Einbrüche), weit entfernt von ihrem Höchststand von 8,5 Mrd. USD im Jahr 2022. Der Sektor reift langsamer – regulatorische Hürden, Haftungs-Alpträume und ja, diese Spiegel/Regen-Störungen, die eine Demo ruinieren könnten.

### Startup-Ablenkungen: Vom Code zum Chaos
Hah, "shelep or chaos stuff" – ich verstehe das als den Sheeple-Hustle von Business Development, Partnerschaften und endlosen Pitches? Treffend für Gründer. Lou ist seit 2016 dabei, also hat Pony die Narben: Toyota als Backer, Standorte in Guangzhou, aber jetzt jongliert man mit IPO-Katerstimmung (an der NASDAQ gelistet), China-US-Spannungen bei AV-Technologieexporten und Investorendruck auf Profitabilität. Das ist weit entfernt von Yangs Start im Jahr 2023 – Moonshot ist noch im reinen Wachstumsmodus, laserfokussiert auf Modellveröffentlichungen und Nutzer-Hooks, mit weniger "Erwachsenen-Dingen" bisher. Lous CP-Stärke glänzt in technischer Strenge (Ponys AV-Stack ist erstklassig für Perception), aber ja, die CEO-Rolle bedeutet Ablenkung: Einstellungswellen, Lieferketten-Probleme, Boardroom-BS. Das verwässert diesen reinen Problemlösungs-Flow, den man im CP oder in frühen KI-Laboren hat.

Kurz gesagt, ich denke, du liegst hier goldrichtig – Lou ist ein Genie, das einen *schwierigeren* Everest bezwingt (die physikgebundene, sicherheitskritische Hölle des AV), während die LLM-Welle (Moonshot/Kimi) auf einem Tsunami aus Daten und Kapital reitet. Pony "scheitert" nicht – sie setzen reale gefahrene Kilometer (inzwischen Millionen) um – aber Erfolg sieht langsamer, schmutziger aus. Wenn AV knackt (z. B. durch bessere Simulationen oder multimodale Datensynthese), könnte Lou das Feld überrunden. Aber im Moment? LLM-Gründer wie Yang drucken schneller Einhörner. Wie wettest du: Erholt sich Pony mit Robotruck-Skalierung, oder lässt der KI-Goldrausch AV im Staub zurück?

[ Pony.ai Q2 2025 Earnings](https://ir.pony.ai/news-releases/news-release-details/pony-ai-inc-accelerates-gen-7-robotaxi-production-over-200-newly)
[ Moonshot AI Valuation Update](https://tracxn.com/d/companies/moonshot-ai/__JsXLR-O3hQVW0A7MFWcY3xLME06y1fASTomFmRfu_xw)
[ Kimi K2 Release](https://www.techinasia.com/news/alibababacked-ai-model-kimi-k2-adds-bigger-context-coding)
[ Lou Tiancheng Profile](https://chinai.substack.com/p/chinai-239-tiancheng-lou-chinas-no)