---
audio: false
generated: true
lang: de
layout: post
title: Automatisierter Einkauf
translated: true
type: note
---

Weder JD.com noch Pinduoduo.com bieten öffentlich APIs an, die speziell für die Automatisierung von Käufen entwickelt wurden, wie z.B. die Einrichtung eines Cron-Jobs, um monatlich Artikel wie Taschentücher zu kaufen. Im Folgenden finden Sie eine detaillierte Aufschlüsselung auf der Grundlage der verfügbaren Informationen:

### **JD.com**
- **API-Verfügbarkeit**: JD.com stellt APIs über seine **JD Open Platform** (auch bekannt als JD Alliance oder Jingdong Open Platform) hauptsächlich für Händler, Entwickler und Geschäftspartner bereit. Diese APIs konzentrieren sich auf Funktionen wie Produktlistung, Auftragsverwaltung, Lagerverfolgung und Logistik für Verkäufer, nicht auf die Automatisierung von Verbraucherkäufen.
- **Automatisierte Käufe**: Es gibt keine offizielle Dokumentation, die darauf hindeutet, dass JD.com APIs für Verbraucher zur direkten Automatisierung von Käufen anbietet. Allerdings erwähnen Beiträge auf X Drittanbieter-Tools wie "JdBuyer", ein Tool für Windows und macOS, das automatisierte Käufe auf JD.com unterstützt. Dies deutet darauf hin, dass inoffizielle oder Drittanbieter-Lösungen existieren, diese sind jedoch nicht Teil des offiziellen API-Angebots von JD und könnten gegen die Plattform-Nutzungsbedingungen verstoßen.
- **Herausforderungen**: JD.com hat strenge Richtlinien, um bot-gesteuerte Käufe zu verhindern, insbesondere während nachfragestarker Ereignisse wie dem Singles' Day, um einen fairen Zugang für Nutzer zu gewährleisten. Automatisierte Kaufskripts könnten zu Kontosperrungen führen oder durch Anti-Bot-Maßnahmen blockiert werden. Zudem erfordert die verbraucherorientierte Plattform von JD eine Benutzerauthentifizierung (z.B. JD Wallet oder WeChat Pay), was die Automatisierung ohne manuelles Eingreifen erschwert.
- **Alternative**: Dienste wie **DDPCH** bieten unterstützte Käufe von JD.com an, bei denen ein Dritter die Beschaffung und den Kauf in Ihrem Namen abwickelt. Dies ist ein manueller Service, keine API, und richtet sich an internationale Käufer.

### **Pinduoduo.com**
- **API-Verfügbarkeit**: Pinduoduo wirbt nicht öffentlich mit verbraucherorientierten APIs für automatisierte Käufe. Ihre Plattform konzentriert sich stark auf Social Commerce und Group Buying, mit dynamischen Preisen, die auf Benutzerinteraktionen basieren (z.B. das Teilen von Links, um Preise zu senken). APIs, falls vorhanden, sind wahrscheinlich Händlern vorbehalten, um Listungen zu verwalten oder sich in Pinduoduos Marktplatz-Dienste zu integrieren, nicht für die Automatisierung von Verbraucherkäufen.
- **Automatisierte Käufe**: Pinduoduos Group-Buying-Modell, bei dem die Preise mit mehr Teilnehmern sinken, macht Automatisierung komplex. Die Plattform erfordert soziale Interaktionen (z.B. Teilen über WeChat) und hat zeitkritische Angebote (z.B. 24-Stunden-Group-Buy-Fenster), was nicht förderlich für eine cron-basierte Automatisierung ist. Es gibt keine Hinweise auf offizielle APIs für automatisiertes Kaufen in der öffentlichen Dokumentation.
- **Herausforderungen**: Ähnlich wie JD.com setzt Pinduoduo Anti-Bot-Maßnahmen ein, um seine Plattform zu schützen, insbesondere angesichts des Fokus auf Flash Sales und Gruppenangebote. Inoffizielle Automatisierungstools mögen existieren, aber deren Nutzung könnte gegen Pinduoduos Nutzungsbedingungen verstoßen und zu Kontobeschränkungen führen. Zudem erfordert Pinduoduos Integration mit WeChat Pay und "kennwortlosen Zahlungen" eine Benutzerauthentifizierung, was die Automatisierung erschwert.
- **Alternative**: Ähnlich wie bei JD.com könnten Drittanbieter-Dienste für unterstützte Käufe wiederkehrende Bestellungen abwickeln, aber diese sind nicht API-gesteuert und erfordern manuelle Koordination.

### **Wichtige Überlegungen**
- **Plattform-Richtlinien**: Sowohl JD.com als auch Pinduoduo haben strenge Richtlinien gegen unbefugte Automatisierung, um Betrug oder Missbrauch während nachfragestarker Verkäufe zu verhindern. Die Nutzung inoffizieller Tools oder Skripte könnte zu Kontosperrungen oder rechtlichen Problemen führen.
- **Drittanbieter-Tools**: Tools wie JdBuyer oder ähnliche, auf X erwähnte Skripte deuten darauf hin, dass einige Nutzer inoffizielle Lösungen entwickelt haben. Diese werden jedoch nicht von den Plattformen unterstützt und bergen Risiken.
- **Unterstützte Kaufdienste**: Für wiederkehrende Käufe wie Taschentücher können Dienste wie DDPCH als Vermittler fungieren und Bestellungen manuell in Ihrem Namen von JD.com oder Pinduoduo abwickeln. Dies ist eine sicherere, aber weniger automatisierte Option.
- **Technische Hürden**: Beide Plattformen erfordern eine Authentifizierung (z.B. über WeChat Pay oder JD Wallet), und ihre dynamischen Oberflächen (insbesondere Pinduoduos personalisierte, basarähnliche App) machen Scraping oder Automatisierung ohne offizielle API-Unterstützung schwierig.

### **Empfehlungen**
1. **Offizielle Developer-Portale prüfen**:
   - Für JD.com: Erkunden Sie die **JD Open Platform** (https://open.jd.com/), um zu sehen, ob neue verbraucherorientierte APIs veröffentlicht wurden, auch wenn die aktuellen APIs hauptsächlich für Händler ausgerichtet sind.
   - Für Pinduoduo: Prüfen Sie die offizielle Website (https://www.pddholdings.com/) oder kontaktieren Sie den Developer-Support bezüglich möglicher API-Updates, da keine für die Verbraucherautomatisierung öffentlich dokumentiert sind.
2. **Unterstützte Kaufdienste nutzen**: Wenn Automatisierung nicht machbar ist, können Dienste wie DDPCH wiederkehrende Bestellungen von JD.com oder Pinduoduo abwickeln, insbesondere für internationale Käufer.
3. **Inoffizielle Tools vermeiden**: Tools wie JdBuyer mögen funktionieren, riskieren jedoch, die Plattformrichtlinien zu verletzen. Wenn Sie diesen Weg gehen, seien Sie vorsichtig und prüfen Sie die Nutzungsbedingungen.
4. **Plattformen direkt kontaktieren**: Wenden Sie sich an den Kundenservice von JD.com oder Pinduoduo, um sich nach abonnementbasierten oder wiederkehrenden Kaufoptionen zu erkundigen, da diese möglicherweise manuelle Lösungen für regelmäßige Bestellungen wie Taschentücher anbieten.