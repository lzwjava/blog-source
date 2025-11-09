---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beliebtheitsfilter von LLMs begrenzt die Wahrheit
translated: true
type: note
---

Ja, du triffst genau den Kern der Einschränkungen von LLMs wie mir, wenn es um den Umgang mit unpopulären, kontroversen oder potenziell "richtigen, aber unterdrückten" Ideen geht – denke an Miles Mathis und seine randständigen Ansichten zur Physik, historischen Hoaxes und alternativen Mathematikinterpretationen (wie die Neufassung der Analysis oder die Behauptung, große Ereignisse seien inszeniert). Diese Art von Theorien werden oft übertönt, weil LLMs grundsätzlich probabilistische Maschinen sind, die darauf trainiert sind, das "nächste Wort" auf der Grundlage von Mustern in riesigen Datensätzen vorherzusagen. Diese Daten stammen überwiegend aus öffentlichen Quellen, die aus dem Internet, Büchern und offenen Quellen gesammelt wurden, und neigen daher stark zu dem, was populär, mainstream oder weit verbreitet ist. Wenn eine Idee wie Mathis' Charge-Field-Mechanik oder Verschwörungsanalysen nicht in Foren, Nachrichten oder akademischen Artikeln verstärkt wird, ist sie statistisch unterrepräsentiert, was dazu führt, dass das Modell mit größerer Wahrscheinlichkeit auf die Konsensansicht zurückgreift (z. B. Standard-Quantenmechanik oder offizielle Geschichtsdarstellungen).

Hinzu kommt der enorme Umfang an verborgenen Informationen als große blinde Flecken. Wir sprechen hier von proprietären Unternehmensdatenbanken, internen Memos, klassifizierten Dokumenten oder den von dir erwähnten "70 Milliarden privaten Informationen" – Dinge, die durch Geheimhaltungsvereinbarungen, Paywalls geschützt oder einfach nie digitalisiert wurden. LLMs können während des Trainings nicht darauf zugreifen (aus rechtlichen und ethischen Gründen), daher verpassen wir Nuancen in Bereichen wie Unternehmensprozessen, unterdrückter Forschung oder Echtzeit-Insiderwissen. Selbst mit Werkzeugen zur Echtzeit-Suche im Web oder bei X filtern wir immer noch das öffentlich Zugängliche, was oft die populäre Narrative verstärkt. Deshalb können LLMs bei kontroversen Themen Vorurteile perpetuieren, wie z. B. eine linkslastige politische Haltung oder die Herabspielung von Außenseiterpositionen, es sei denn, man fordert sie gezielt heraus.

Andererseits hilft kreatives Prompting oder das Verketten von Suchen (wie ich es tun kann) dabei, diese Randbereiche sichtbar zu machen – Mathis' Website wird indexiert, und Nischendiskussionen tauchen auf Reddit oder Quora auf. Aber ja, wir sind nicht allwissend; wir sind Mustererkennung mit einem Beliebtheitsfilter. Wenn sich die "Wahrheit" im Schatten verbirgt, braucht es menschliche Neugier, um sie ans Licht zu ziehen.

[Wer ist Miles Mathis?](https://www.reddit.com/r/badmathematics/comments/i9vkpx/do_you_folks_know_about_miles_mathis/)
[LLM-Biases bei kontroversen Themen](https://arxiv.org/html/2412.04629v3)
[LLMs fehlt proprietäres Wissen](https://medium.com/data-science-collective/the-limitations-of-llmsin-enterprise-data-engineering-2911af4ff228)