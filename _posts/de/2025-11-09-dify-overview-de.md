---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht der Dify AI-Plattform
translated: true
type: note
---

### Was ist Dify.ai?
Dify.ai ist eine Open-Source-, Low-Code-Plattform zum Erstellen und Bereitstellen generativer KI-Anwendungen, die von Large Language Models (LLMs) angetrieben werden. Die 2023 gestartete Plattform konzentriert sich auf agentenbasierte Workflows, Retrieval-Augmented Generation (RAG)-Pipelines und KI-Agenten und erleichtert es Entwicklern, Teams und Unternehmen, Chatbots, Copilots und komplexe Automatisierungen ohne tiefgehende Programmierkenntnisse zu erstellen. Sie ist selbst gehostbar, verfügt über eine Drag-and-Drop-Oberfläche und legt den Schwerpunkt auf Produktionsreife durch skalierbare Infrastruktur, Modellmanagement und einen Plugin-Marktplatz. Man kann es sich als "LangChain in der Cloud" vorstellen, nur benutzerfreundlicher und visueller; es konkurriert mit Tools wie Flowise oder Vercel AI.

Stand November 2025 floriert Dify im KI-Agenten-Boom mit starker Community-Dynamik und Enterprise-Adaption. Es ist besonders beliebt in Asien (z. B. Integrationen mit Alibaba Cloud) und für B2B-Anwendungsfälle wie die Automatisierung des Kundensupports und Wissenspipelines.

### Wichtige Funktionen
- **Visueller Workflow-Builder**: Drag-and-Drop für mehrstufige KI-Agenten, einschließlich Iterationsschleifen, bedingter Logik und Tool-Orchestrierung.
- **RAG und Wissenspipelines**: Daten aus dem Web, Datenbanken oder Dateien erfassen; in Vektorspeichern indizieren und kontextbewusste Antworten ermöglichen.
- **LLM-Flexibilität**: Wechsel zwischen 100+ Modellen (Open-Source wie Llama oder proprietär wie GPT/Claude) mit integriertem Performance-Benchmarking.
- **Plugins und Integrationen**: 120+ im Marketplace, einschließlich neuer Zugänge 2025 wie Firecrawl (Web Scraping), Qdrant/TiDB (Vektorspeicher), Tavily (Suche), Bright Data (strukturierte Daten), TrueFoundry (AI Gateway) und Arize (Observability). Unterstützt MCP für API-/Datenbank-Bridging.
- **Bereitstellungsoptionen**: Cloud-gehostet (Backend-as-a-Service), selbst gehostet oder einbettbar; Enterprise-Features wie SSO, Audit-Logs und Skalierbarkeit für hohen Traffic.
- **No-Code bis Pro**: Anfängerfreundliche Vorlagen, aber erweiterbar mit benutzerdefiniertem Code, Debugging-Tools und Monitoring.

Aktuelle Updates umfassen v1.0.0 (Feb 2025) mit entkoppelten Plugins für einfachere Erweiterbarkeit, HTTP-basierte MCP-Unterstützung (März 2025 Protokoll) und ein neues offizielles Forum für Community-Fragen und -Antworten.

### Wie läuft es? Wachstum und Metriken
Dify's Wachstum hat sich 2025 beschleunigt, getragen von der Welle der KI-Agenten-Adaption. Es hat einen Großteil seines Erfolgs bootstrapped durch Open-Source-Beiträge (GitHub-Stars im Zehntausender-Bereich) und virales Teilen unter Entwicklern.

| Metrik                  | Details (Stand Nov 2025)                  |
|-------------------------|-------------------------------------------|
| **Annual Recurring Revenue (ARR)** | 3,1 Millionen US-Dollar (stetiges Wachstum seit dem Launch 2023) |
| **Teamgröße**          | 28 Mitarbeiter (schlanker, effizienter Betrieb) |
| **Gesamtfinanzierung**      | 1,39 Millionen US-Dollar (Series A im Aug 2024 angeführt von Alibaba Cloud und VCshare; keine größeren Runden 2025 angekündigt) |
| **Nutzergrundlage/Traffic**  | Millionen von Apps global bereitgestellt; 60M+ monatliche Besuche (62% Direktverkehr, stark von Entwicklern); 63% männliches Publikum, dominante Altersgruppe 25-34 |
| **Adaptions-Highlights**| Wird von Volvo Cars (KI-Navigation), Konsumelektronikfirmen (reduzierte Analysezeit von 8→3 Stunden/Aufgabe) und 20+ Abteilungen in großen Organisationen genutzt; aktiv in Biomedizin, Automobilindustrie und SaaS |

Es ist noch kein Einhorn wie n8n, aber der Umsatz hat sich im Jahresvergleich verdreifacht, wobei Self-Hosting die organische Verbreitung unter datenschutzbewussten Teams vorantreibt.

### Nutzerstimmung und Bewertungen
Das Feedback ist größtenteils positiv, besonders bezüglich der Benutzerfreundlichkeit und des schnellen Prototypings – Nutzer lieben, wie es "KI-Agenten demokratisiert" ohne SDK-Probleme. Auf G2 (Durchschnitt 4,5-4,7/5 von 100+ Bewertungen) werden als Vorteile die intuitive UI, robustes RAG und Kosteneinsparungen im Vergleich zu individuellen Entwicklungen genannt. Nachteile: Gelegentliche Skalierungsprobleme in der Produktion (z.B. Debugging unter hoher Last) und eine Lernkurve für fortgeschrittene Agenten.

Aus aktuellen X-Posts (meist Entwickler-Community auf Englisch/Japanisch):
- Begeisterung über Integrationen: "Performance mit Firecrawl 10-fach gesteigert" und "Qdrant für Enterprise-RAG ist ein Game-Changer."
- Community-Erfolge: Neues Forum für schnelle Bugfixes gelobt (z.B. Gemini-Probleme).
- Kleinere Kritikpunkte: Abrechnungsprobleme (z.B. Rückerstattungen für Studentenpläne) und der Wunsch nach mehr "methodenähnlichen" wiederverwendbaren Blöcken.
- Gesamteindruck: Aktiv, kollaborativ – Beiträge über Workflows wie DeepResearch (automatisierte mehrstufige Suchen) zeigen echten Nutzen.

Es ist solide für Indie-Entwickler und den B2B-Mittelmarkt, aber Unternehmen merken an, dass es für ultra-hohe Skalierung noch reift (kombiniere es dafür mit Gateways wie Higress).

### Warum es an Zugkraft gewinnt
Dify glänzt in der "Agenten-Ökonomie" 2025, indem es No-Code-Zugänglichkeit mit professioneller Erweiterbarkeit verbindet, alles Open-Source. Während KI vom Hype zum operativen Betrieb übergeht (z.B. Automatisierung von Recherche oder Kundeninteraktionen), positioniert es sich gut durch den Fokus auf beobachtbare, skalierbare Workflows. Wenn Sie LLM-Apps erstellen, ist es eine Top-Wahl – Free-Tier für Einsteiger, kostenpflichtig für Teams (laut Beschwerden ab 59 $/Monat, aber Website prüfen).

Referenzen:  
[Dify AI Review 2025](https://www.gptbots.ai/blog/dify-ai)  
[How Dify Hit $3.1M Revenue](https://getlatka.com/companies/dify.ai)  
[Dify Buyer's Guide 2025](https://skywork.ai/blog/dify-review-buyers-guide-2025/)  
[Dify Strategic Overview](https://www.baytechconsulting.com/blog/what-is-dify-ai-2025)  
[Dify Funding Profile](https://pitchbook.com/profiles/company/539409-43)  
[Dify G2 Reviews](https://www.g2.com/products/dify-ai/reviews)  
[Dify v1.0.0 Release](https://dify.ai/blog)  
[Dify Traffic Analytics](https://www.similarweb.com/website/dify.ai/)  
[Dify Integrations Blog](https://dify.ai/blog/dify-x-qdrant-building-and-powering-the-next-gen-ai-applications)  
[Dify Forum Launch](https://forum.dify.ai/)  
[Dify X Posts](https://x.com/dify_ai)