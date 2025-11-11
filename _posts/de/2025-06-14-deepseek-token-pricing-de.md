---
audio: false
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: TiefenSuche Tokenpreisgestaltung im Detail erklärt
translated: true
type: note
---

Um Ihre Beobachtung direkt anzusprechen: DeepSeek v3.2 hat zwar einen signifikanten Preisrückgang angekündigt – in einigen Fällen bis zu 50 % oder mehr – aber die tatsächliche Kostensenkung, die Nutzer erfahren, kann aufgrund mehrerer Faktoren variieren:

- **Angekündigter Preis vs. Effektive Kosten:** DeepSeek kündigte eine Preissenkung von 1,68 $ auf 0,42 $ pro Million Tokens an (in manchen Kontexten eine Reduzierung um 75 %), dies gilt jedoch für die Roh-Token-Preisgestaltung. Ihre tatsächlichen Kosten hängen von Ihrem spezifischen Nutzungsmuster ab: dem Verhältnis von Input- zu Output-Tokens, Cache-Treffer-/Fehlraten und davon, ob Sie Rabatte für Nebenzeiten nutzen (die in bestimmten Stunden bis zu 50–75 % betragen können) ue202turn0search1,[1],[2].
- **Cache-Effizienz:** Wenn Ihre Workload vom Caching profitiert (z. B. wiederholte Prompts oder Wiederverwendung von Kontext), können die effektiven Kosten niedriger sein als der angekündigte Preis vermuten lässt. Die beworbene Preissenkung gilt jedoch nur für den Basistarif, nicht unbedingt für zwischengespeicherte Tokens.
- **Input/Output-Asymmetrie:** Einige Modelle berechnen unterschiedliche Sätze für Input- und Output-Tokens. Wenn die Preissenkung nur für Input-Tokens gilt, Ihre Aufgabe jedoch output-lastig ist, wird die gesamte Kostensenkung geringer als 50 % ausfallen.
- **Rabatte für Nebenzeiten:** DeepSeek bietet zusätzliche Rabatte während der Nebenzeiten (16:30–00:30 UTC), die die Kosten weiter senken können, wenn Ihre Nutzung in diese Zeiten fällt ue202turn0search2.

**Warum Sie keinen sofortigen Kostenrückgang von 50 % gesehen haben:**
- Die Preissenkung wurde möglicherweise nicht einheitlich auf alle Tokentypen oder Nutzungsszenarien angewendet.
- Die spezifische Token-Verteilung Ihrer Aufgabe (Input/Output, Cache-Treffer/Fehlschläge) stimmt möglicherweise nicht mit der beworbenen Preissenkung überein.
- Es kann eine Verzögerung zwischen der Ankündigung und der Umsetzung der Preisänderung in allen Abrechnungssystemen oder APIs geben.

Zusammenfassend lässt sich sagen, dass der Preisrückgang bei DeepSeek v3.2 zwar real und erheblich ist, die tatsächlichen Kosteneinsparungen jedoch von Ihrem Nutzungsmuster abhängen und möglicherweise nicht genau der angekündigten Prozentzahl entsprechen ue202turn0search1,[1],[2].

Zitate:
[1] https://x.com/deepseek_ai
[2] https://www.facebook.com/groups/developerkaki/posts/2615893198756577/