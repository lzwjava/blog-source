---
audio: false
generated: true
lang: de
layout: post
title: Detaillierte Analyse von KI-Plattformen für API-Schlüsselintegration und Preisgestaltungsmodelle
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Portkey eine geeignete Plattform ist, um eigene KI-API-Schlüssel über eine einheitliche Oberfläche zu nutzen, allerdings erhebt es eine Abonnementgebühr, was möglicherweise nicht Ihrer Präferenz für nutzungsbasierte Bezahlung entspricht.
- Recherchen deuten darauf hin, dass OpenRouter eine nutzungsbasierte Bezahlung pro Token ohne Abonnement anbietet, erlaubt aber nicht das Anschließen eigener API-Schlüssel, was Ihren Anforderungen möglicherweise nicht gerecht wird.
- Die Erkenntnisse deuten darauf hin, dass es nur begrenzt Plattformen gibt, die Ihre Kriterien perfekt erfüllen: Nutzung eigener API-Schlüssel mit nutzungsbasierter Preisgestaltung auf Token-Basis und ohne Abonnementgebühr, was potenziell einen Kompromiss erfordert.

### Plattform-Empfehlung
Nach der Auswertung Ihrer Anforderungen scheint Portkey ([Portkey AI](https://portkey.ai/)) die passendste Lösung zu sein. Es erlaubt Ihnen, Ihre eigenen API-Schlüssel für verschiedene KI-Modelle anzuschließen und bietet eine einheitliche Oberfläche zur Verwaltung. Allerdings operiert es mit einem Abonnement-basierten Modell (z.B. 49 $/Monat für den Pro-Plan), was bedeutet, dass Sie eine feste Gebühr für die Plattformnutzung zahlen, zusätzlich zu den direkten Zahlungen an die KI-Anbieter über Ihre Schlüssel für die Token-Nutzung. Dies entspricht möglicherweise nicht vollständig Ihrem Wunsch, Abonnementgebühren wie 20 $/Monat zu vermeiden, aber es bietet erweiterte Funktionen wie Observability und Prompt-Management, die wertvoll sein könnten.

Falls die Vermeidung von Abonnementgebühren entscheidend ist und Sie bereit sind, auf die Nutzung eigener API-Schlüssel zu verzichten, ist OpenRouter ([OpenRouter](https://openrouter.ai)) eine weitere Option. Es berechnet 0,0001 $ pro Token nach einem kostenlosen Kontingent von 1000 Token pro Monat, ohne Abonnementgebühr, aber Sie würden deren API anstelle Ihrer eigenen Schlüssel verwenden, was bedeutet, dass Sie sie direkt für die Modellnutzung bezahlen.

### Unerwartetes Detail
Ein unerwarteter Befund ist, dass viele Plattformen, wie OpenRouter, ihren eigenen Zugang zu KI-Modellen bereitstellen und Nutzer dazu zwingen, über die Plattform zu bezahlen, anstatt persönliche API-Schlüssel zu verwenden. Dies könnte Ihre Kontrolle über Kosten und Daten einschränken.

---

### Untersuchungshinweis: Detaillierte Analyse von KI-Plattformen für API-Schlüssel-Integration und Preismodelle

Diese Analyse untersucht Plattformen, die es Nutzern erlauben, ihre eigenen KI-API-Schlüssel anzuschließen und nutzungsbasierte Preisgestaltung auf Token-Basis ohne Abonnementgebühr anbieten, als Alternative zu Plattformen wie ChatBoxAI und OpenWebUI. Die Recherche, durchgeführt um 02:42 AM PDT am Freitag, 14. März 2025, zielt darauf ab, die spezifischen Bedürfnisse des Nutzers zu adressieren und dabei die Komplexität von Plattform-Preisen und Funktionalität zu berücksichtigen.

#### Hintergrund und Nutzeranforderungen
Der Nutzer besitzt mehrere API-Schlüssel für verschiedene KI-Plattformen und sucht eine Plattform, die:
- Das Anschließen eigener API-Schlüssel für eine einheitliche Oberfläche erlaubt.
- Nutzungsbasierte Preisgestaltung auf Token-Basis bietet und Abonnementgebühren wie 20 $/Monat vermeidet.
- Eine bessere Benutzeroberfläche (UI) als ChatBoxAI bietet, die als schlecht empfunden wurde, und potenziell Mistral-Integration beinhaltet.

Angesichts dieser Anforderungen konzentriert sich die Analyse darauf, Plattformen zu identifizieren, die diese Kriterien erfüllen, ihre Preismodelle zu verstehen und ihre UI- und Integrationsfähigkeiten zu bewerten.

#### Plattform-Bewertung

##### Kontext zu ChatBoxAI und OpenWebUI
- **ChatBoxAI** ([ChatBox AI](https://chatboxai.app/en)) ist ein Desktop-Client für KI-Modelle wie ChatGPT, Claude und andere, der es Nutzern erlaubt, ihre eigenen API-Schlüssel anzuschließen. Es hat ein Abonnementmodell für seinen KI-Service, das eine Gebühr von 20 $/Monat beinhalten kann, und unterstützt Mistral über Integrationen, entgegen der Nutzeraussage, dass Mistral-Integration fehle. Dessen UI wurde vom Nutzer als schlecht bewertet.
- **OpenWebUI** ([Open WebUI](https://openwebui.com/)) ist eine quelloffene, selbst gehostete Oberfläche für KI-Modelle, die verschiedene LLM-Runner wie Ollama und OpenAI-kompatible APIs unterstützt. Es erlaubt Nutzern, ihre eigenen API-Schlüssel anzuschließen und ist kostenlos, ohne Abonnementgebühr, was dem nutzungsbasierten Modell durch Anbieterkosten entspricht. Der Nutzer sucht jedoch nach Alternativen hierzu.

##### Kandidaten-Plattformen
Mehrere Plattformen wurden bewertet, mit Fokus auf ihre Fähigkeit, nutzerbereitgestellte API-Schlüssel zu handhaben, und ihre Preismodelle. Die wichtigsten Erkenntnisse sind unten zusammengefasst:

| Plattform    | Eigene API-Schlüssel | Preismodell                       | Mistral-Integration | UI-Hinweise                       |
|--------------|----------------------|-----------------------------------|---------------------|-----------------------------------|
| Portkey      | Ja                   | Abonnement-basiert (z.B. 49 $/Mo) | Ja                  | Web-basiert, bekannt für Benutzerfreundlichkeit |
| OpenRouter   | Nein                 | Pay-per-token (0,0001 $/Token nach 1000 kostenlosen) | Ja | Web-basiert, einfache Oberfläche  |
| Unify.ai     | Möglicherweise (BYOM)| Unklar, wahrscheinlich Abonnement | Ja                  | Fokussiert auf Workflows, weniger UI-zentriert |
| LiteLLM      | Ja                   | Kostenlos (Open-Source)           | Ja                  | API-Schicht, keine nutzerorientierte UI |

- **Portkey** ([Portkey AI](https://portkey.ai/)): Diese Plattform erlaubt Nutzern, ihre eigenen API-Schlüssel für über 250 LLMs, inklusive Mistral, über dessen AI Gateway anzuschließen. Es bietet eine einheitliche Oberfläche mit Funktionen wie Observability, Prompt-Management und Model-Fallbacks. Die Preisgestaltung ist abonnementbasiert, mit Plänen wie einem kostenlosen Starter-Tarif, einem Pro-Tarif für 49 $/Monat und individuellen Business-Preisen. Nutzer zahlen Portkey für den Plattformzugang und die Anbieter direkt über ihre Schlüssel für die Modellnutzung, was möglicherweise nicht der Vermeidung von Abonnementgebühren entspricht. Nutzerbewertungen heben die Benutzerfreundlichkeit und umfassenden Funktionen hervor, was auf eine potenziell bessere UI als den ChatBoxAI-Desktop-Client hindeutet.

- **OpenRouter** ([OpenRouter](https://openrouter.ai)): Diese Plattform bietet eine einheitliche API für mehrere LLMs mit nutzungsbasierter Preisgestaltung pro Token (0,0001 $/Token nach 1000 kostenlosen Token monatlich, keine Abonnementgebühr). Allerdings erlaubt sie Nutzern nicht, ihre eigenen API-Schlüssel anzuschließen; stattdessen verwenden Nutzer die OpenRouter-API und zahlen sie direkt für die Modellnutzung. Sie unterstützt Mistral und hat eine web-basierte Oberfläche, die als einfach beschrieben wird, was potenziell eine bessere UI als ChatBoxAI bietet. Dies passt zum nutzungsbasierten Modell, erfüllt aber nicht die Anforderung der Nutzung persönlicher API-Schlüssel.

- **Unify.ai** ([Unify: Build AI Your Way](https://unify.ai/)): Diese Plattform konzentriert sich auf den Aufbau von KI-Workflows und erwähnt "Bring Your Own Model" (BYOM), was auf potenzielle Unterstützung für nutzerbereitgestellte Modelle hindeutet. Allerdings sind deren Preisgestaltung und UI weniger klar, und sie scheint eher entwicklerorientiert zu sein, möglicherweise mit abonnementbasierten Kosten. Sie unterstützt Mistral, aber ihre Eignung für eine nutzerorientierte Oberfläche ist unsicher, was sie weniger geeignet im Vergleich zu Portkey oder OpenRouter macht.

- **LiteLLM**: Ein quelloffener KI-API-Proxy, der es Nutzern erlaubt, ihre eigenen API-Schlüssel anzuschließen und über eine einheitliche API zu nutzen. Es ist kostenlos, ohne Abonnementgebühr, und Nutzer zahlen Anbieter direkt über ihre Schlüssel für die Token-Nutzung. Allerdings fehlt eine nutzerorientierte UI, was es eher für Entwickler geeignet macht, die es in Anwendungen integrieren, nicht für direkte Nutzerinteraktion wie ChatBoxAI oder OpenWebUI.

#### Analyse der Passung zu den Nutzeranforderungen
- **Nutzung eigener API-Schlüssel**: Portkey und LiteLLM erlauben dies explizit, während OpenRouter dies nicht tut und Nutzer zwingt, deren API zu verwenden. Die BYOM-Funktion von Unify.ai ist mehrdeutig und weniger nutzerfokussiert.
- **Nutzungsbasierte Preisgestaltung auf Token-Basis**: OpenRouter passt mit seiner Preisgestaltung pro Token, aber Nutzer verwenden nicht ihre eigenen Schlüssel. Portkey hat ein Abonnementmodell, was dem Wunsch des Nutzers widerspricht, Gebühren wie 20 $/Monat zu vermeiden. LiteLLM ist kostenlos, was zu keinem Abonnement passt, aber es fehlt eine UI. Keine Plattform kombiniert perfekt alle Anforderungen ohne Kompromisse.
- **UI und Mistral-Integration**: Sowohl Portkey als auch OpenRouter haben web-basierte UIs, potenziell besser als der ChatBoxAI-Desktop-Client, und beide unterstützen Mistral. Nutzerbewertungen deuten darauf hin, dass Portkeys UI benutzerfreundlich ist, während OpenRouters UI einfach ist. Das Fehlen einer UI bei LiteLLM macht es für UI-fokussierte Bedürfnisse ungeeignet.

#### Herausforderungen und Kompromisse
Die primäre Herausforderung ist der scheinbare Mangel an Plattformen, die es Nutzern erlauben, ihre eigenen API-Schlüssel anzuschließen, eine einheitliche nutzerorientierte Oberfläche bereitstellen und auf Token-Basis ohne Abonnementgebühr abrechnen. Die meisten Plattformen erheben entweder ein Abonnement (wie Portkey) oder erlauben keine persönlichen API-Schlüssel (wie OpenRouter). Dies deutet auf einen Kompromiss hin:
- Akzeptieren einer Abonnementgebühr für Plattformfunktionen (Portkey) während der Nutzung eigener Schlüssel.
- Verwenden eines Pay-per-Token-Modells ohne eigene Schlüssel (OpenRouter), was potenziell die Kostenkontrolle durch persönliche Schlüssel verliert.

#### Empfehlung und Überlegungen
Angesichts der Betonung des Nutzers auf die Verwendung eigener API-Schlüssel und die Vermeidung von Abonnementgebühren wurde keine perfekte Übereinstimmung gefunden. Dennoch wird **Portkey** als die passendste Lösung empfohlen, da es das Anschließen persönlicher API-Schlüssel erlaubt und eine einheitliche Oberfläche mit einer potenziell besseren UI als ChatBoxAI bietet. Trotz der Abonnementgebühr (z.B. 49 $/Monat für Pro) unterstützt es erweiterte Funktionen, die die Kosten für die Verwaltung mehrerer KI-Modelle rechtfertigen könnten. Nutzer sollten bewerten, ob die Funktionen die Abonnementkosten aufwiegen, besonders im Vergleich zur direkten Bezahlung von Anbietern über Schlüssel ohne Plattform.

Für diejenigen, die nutzungsbasierte Bezahlung ohne Abonnement priorisieren und bereit sind, auf persönliche Schlüssel zu verzichten, ist **OpenRouter** eine Alternative, die 0,0001 $ pro Token nach 1000 kostenlosen berechnet, mit einer einfachen Web-UI und Mistral-Unterstützung. Dies bedeutet jedoch, die Kontrolle über API-Schlüssel aufzugeben, was möglicherweise nicht zur Eigentümerschaft des Nutzers an mehreren Schlüsseln passt.

#### Fazit
Diese Analyse unterstreicht die Komplexität, eine Plattform zu finden, die alle Nutzerkriterien erfüllt. Portkey bietet die beste Passform für die Nutzung persönlicher API-Schlüssel mit einer einheitlichen Oberfläche, allerdings zu Abonnementkosten. OpenRouter bietet ein nutzungsbasiertes Modell ohne Abonnement, unterstützt aber keine persönlichen Schlüssel. Nutzer müssen möglicherweise entscheiden, ob Plattformfunktionen oder Kostenflexibilität kritischer sind, und potenziell quelloffene Optionen wie selbst gehostete OpenWebUI-Alternativen für die kostenlose Nutzung mit persönlichen Schlüsseln erkunden.

#### Wichtige Quellen
- [Portkey AI control panel for production AI](https://portkey.ai/)
- [OpenRouter unified interface for LLMs](https://openrouter.ai)
- [ChatBox AI your AI copilot](https://chatboxai.app/en)
- [Open WebUI extensible self-hosted interface for AI](https://openwebui.com/)