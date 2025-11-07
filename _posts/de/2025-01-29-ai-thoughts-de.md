---
audio: false
generated: false
image: false
lang: de
layout: post
title: KI-Workflows, Code-Editoren und Plattformdisruption
translated: true
type: post
---

### Inhaltsverzeichnis

1. [Gedanken über KI](#ai-thoughts)
   - KI fehlt echte Intelligenz oder Tiefe
   - Maschinelles Lernen ist fortgeschrittene angewandte Analysis
   - LLMs kämpfen mit strukturierten Dateiformaten
   - Open Source beseitigt technologische Geheimhaltung
   - Textbasierte Tools werden zuerst von KI disruptiert

2. [Neue Plattformen mit KI-Workflows](#new-platforms-powered-by-ai-workflows)
   - KI-Workflows automatisieren mehrsprachige Inhaltsgenerierung
   - Nutzer übermitteln Prompts zur Formatkonvertierung
   - Plattformen ermöglichen Inhaltsverfeinerung und Zusammenfassung
   - Anpassbare KI-Workflows durch Schlüsselworteinstellungen
   - KI übernimmt Inhaltsumwandlung end-to-end

3. [Die nächste Richtung von KI-Code-Editoren](#the-next-direction-of-ai-code-editors)
   - Cloud-Integration entscheidend für CI/CD-Workflows
   - A/B-Tests verbessern KI-generierte Inhalte
   - RLHF erweitert auf Feedback aus der realen Welt
   - Menschliches Feedback verfeinert unvollkommene KI-Outputs
   - Prompt-Optimierung schlägt Output-Korrektur


## Gedanken über KI

*Zuletzt aktualisiert im August 2025*

- Satya Nadella erwähnte das Jevons-Paradox. Es lohnt sich, darüber zu lernen.

- Yin Wang: Es gibt keine "Intelligenz" in künstlicher Intelligenz, kein "Neurales" in neuronalem Netzwerk, kein "Lernen" in maschinellem Lernen und keine "Tiefe" in Deep Learning. Was in diesem Bereich wirklich funktioniert, heißt "Analysis". Daher bevorzuge ich die Bezeichnung "differenzierbare Berechnung", und der Prozess des Modellbaus wird "differenzierbare Programmierung" genannt.

- Yin Wang: Maschinelles Lernen ist wirklich nützlich, man könnte sogar sagen, eine schöne Theorie, denn es ist einfach Analysis in neuem Gewand! Es ist die alte und großartige Theorie von Newton, Leibniz, in einer einfacheren, eleganten und mächtigeren Form. Maschinelles Lernen ist im Grunde die Anwendung von Analysis, um Funktionen abzuleiten und anzupassen, und Deep Learning ist die Anpassung komplexerer Funktionen.

- Derzeit können große Sprachmodelle nicht nach Dateisprachen wie YAML oder Python filtern. Ein erheblicher Teil der Informationen in der realen Welt ist jedoch so organisiert. Das bedeutet, dass wir große Sprachmodelle mit Dateien trainieren könnten.

- Für das Training großer Sprachmodelle könnten wir ein System entwickeln, das exakte Übereinstimmungen findet. Vielleicht können wir den KMP (Knuth-Morris-Pratt)-Suchalgorithmus mit der Transformer-Architektur kombinieren, um die Suchfähigkeiten zu verbessern.

- Es gibt keine technologischen Geheimnisse. Open Source wird alle gut gehüteten Geheimnisse enthüllen.

- KI wird viele Tools beeinflussen, auch indirekt. Die Leute sagen, sie werden Figma nicht mehr brauchen, um Prototypen zu zeichnen, sie werden direkt zum Code greifen. Ich denke, Postman wird ähnlich sein; die Leute werden direkt Python oder andere Skripte verwenden, um APIs aufzurufen oder zu testen.

- Ein Grund, warum wir Postman oder Figma im KI-Zeitalter nicht verwenden, ist, dass ihre Funktionen nicht über Text generiert werden können. Ihnen fehlt auch eine Befehlstaste + K, um Komponentenersetzung auszulösen.

- Benutzeroberflächen werden im KI-Zeitalter zu einer Barriere. Warum Postman aufrüsten, um KI-gestützte Anwendungstests zu ermöglichen, wenn wir direkt die Requests-Bibliothek von Python oder andere Programmiersprachen nutzen können, um Code zu testen, da Letztere von KI unterstützt werden?

- Warum Figma aufrüsten, um KI-gestützte UI-Erstellung zu ermöglichen, wenn codebasierte UI-Generierung, verstärkt durch KI, einen direkteren und potenziell mächtigeren Ansatz bietet?

- LLMs werden zuerst textbezogene Anwendungen verändern, wie Google, Suchmaschinen, Texteditoren und Schreibwerkzeuge, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo und Feedly.

- Umgekehrt werden LLMs kaum Technologien wie Git, Linux, ffmpeg, Handys, Hardware, Browser, Betriebssysteme oder Sprach- und Videoanrufe revolutionieren. Diese Technologien sind codezentriert, und ihr Code wird nicht so einfach von KI generiert wie API-Testtools wie Postman.

- Technologien mit mehr Code sind schwer durch KI zu revolutionieren, wie OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC Media Player, Qt Framework, LLVM/Clang und GNOME. Wenn KI helfen könnte, diese Technologien zu verbessern, würden sie nicht ersetzt werden. KI sollte helfen, bessere Technologien zu entwickeln, und dafür wird KI mehr Rechenleistung benötigen, um denselben Umfang an Code zu generieren.

- Es gibt zwei Arten, wie LLMs Veränderungen bringen können: erstens durch die Veränderung von Inhalten oder Daten innerhalb einer Plattform oder Software, wie z.B. Inhaltsübersetzung in Apps wie TikTok; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, wie Postman oder Google Search, einschließlich Google Translate.

- Es gibt zwei Arten, wie KI-Audio-Tools Veränderungen bringen können: erstens durch die Veränderung von Inhalte oder Daten innerhalb einer Plattform oder Software, wie z.B. die Erzeugung von Hörbüchern für Audible; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, zum Beispiel die Sing-Songs-App, da KI jetzt die gleichen Aufgaben wie Menschen erfüllen kann, was es einfacher macht, das Singen als Hobby zu betreiben.

- Es gibt mehrere Möglichkeiten, zu messen, wie KI aktuelle Software oder Plattformen beeinflusst. Eine Möglichkeit ist, zu messen, wie viele Daten oder Inhalte durch KI teilweise oder vollständig generiert oder verbessert werden können. Eine andere Möglichkeit ist, zu messen, wie viel Code durch KI teilweise oder vollständig geschrieben oder verbessert werden kann. Das bedeutet, wir nutzen das, was KI generiert, um aktuelle Plattformen zu verbessern. Zusätzlich kann KI helfen, neue Software und Plattformen zu erfinden.

- Es gibt drei Arten von Produkten: Generative-KI-Produkte, Produkte, die APIs von Generative-KI-Produkten nutzen, und andere Produkte.

- Eine Produktidee ist, KI zu nutzen, um Echtzeitinformationen, Nachrichten oder Updates von sozialen Plattformen wie Reddit, GitHub Trending, Twitter Trending, Quora Trending und Zhihu Trending zu sammeln. Nutzer können mit Prompts den Feed anpassen oder sogar bestimmte Social-Media-Accounts hinzufügen.

- Es gibt fünf wichtige Arten von Daten: Text, Bild, Audio, Video und Code.

- Andere wichtige Arten von Daten sind numerische, georäumliche, biometrische, Sensoren-, Transaktions-, Metadaten-, Zeitreihen-, strukturierte, unstrukturierte, teilstrukturierte, Gesundheits-, Umwelt-, Log-, Netzwerk- und Verhaltensdaten.

- Google ist immer noch besser für die Website-Indizierung, besonders wenn man Software oder ein Dokument von einer bestimmten Seite herunterladen möchte. Es funktioniert wie eine Domain-Suche. Man nutzt es nicht, um Informationen zu finden, sondern um auf andere Seiten zu navigieren, um Aufgaben zu erledigen. Ein LLM hat möglicherweise nicht die neuesten Download-Links.

- Google funktioniert wie eine Domain-Suche; wenn man eine Maven-Repository-Seite aufrufen möchte, um die neueste Version zu prüfen, kann man es nutzen.

- Google bleibt nützlich für die Bildersuche, während LLMs in der Texterzeugung hervorragen. Dennoch bevorzugen Menschen oft echte Bilder, um Hardwaredetails, Abmessungen, Objektformen oder das Aussehen einer Person zu überprüfen.

- KI-Chatbots sind beliebt, weil Text schwerer zu verarbeiten ist als Bilder. Menschen bevorzugen echte Bilder gegenüber KI-generierten, da Bilder auf einen Blick leichter zu verstehen sind. Allerdings hat die KI-Bildgenerierung ungenutztes Potenzial – Nutzer könnten die KI auffordern, verschiedene Blickwinkel zu zeigen, Gesichter heranzuzoomen oder Details von Leiterplatten zu vergrößern. Da Menschen hauptsächlich mit Text arbeiten und nicht mit Bildern, gibt es enormes Wachstumspotenzial für KI-Bildtools.

- KI ist hervorragend darin, Konzepte zu erklären und Verständnis zu vermitteln. Darüber hinaus können Nutzer Fragen zu jedem spezifischen Detail stellen. Dies ist wahrscheinlich der bedeutendste Nutzen von KI-Tools.

- Ich habe KI genutzt, um über große Sprachmodelle zu lernen. Der Moment, in dem es mir half, K, Q und V zu verstehen, war wunderbar.

- Der Grund, warum ich seit der Veröffentlichung von LLM lieber Ubuntu verwende, ist, dass die bunten und vielfältigen Apps von macOS mich weniger ansprechen. Ich bevorzuge es, meine Programme zu schreiben und alles über das Terminal und Text zu erledigen.

- KI kann daran gemessen werden, wie gut sie eine pom.xml oder requirements.txt-Datei auf die neueste Version aktualisieren, Bibliotheken updaten und Prüfungen durchführen kann. Dieser Prozess kann einen erheblichen Arbeitsaufwand bedeuten und manchmal komplex sein.

- Im KI-Zeitalter sind Programmiersprachen mit besserer Leistung und Robustheit wichtiger und werden beliebter sein, während die Syntax weniger wichtig ist. Dies liegt daran, dass LLM hilft, Code zu generieren, was weniger Aufwand bedeutet, solange das Programm gut ausgeführt wird.

- Menschen neigen dazu, alles von KI-Chatbots zu lesen, weil es leicht zu lernen ist, sie Fragen zu jedem Aspekt stellen können, das Format konsistent ist und die Qualität oft zu den besten im Internet gehört.

- Aber Informationen beschränken sich nicht nur auf Text. Man kann die meisten Textinformationen von KI-Chatbots lesen, verliert jedoch die Original-Website, ihr Layout und ihre Form, ihre Erklärungsbilder und das Webdesign.

- Websites mit viel Interaktion werden wahrscheinlich nicht wesentlich durch KI verändert, wie Webspiele, Google Docs, Google Sheets und Kollaborationstools wie Zoom oder Slack. Sie sind codezentriert und nicht nur auf Text fokussiert.

 [Wie ich gut in der KI- und Blockchain-Ära lebe](./ai-blockchain-en)


---

## Neue Plattformen mit KI-Workflows

*08.01.2025*

- Workflows sind Systeme, in denen große Sprachmodelle (LLMs) und Tools durch vordefinierte Codepfade orchestriert werden.[^1]

- Stell dir eine neue Plattform vor, wie TikTok oder Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit oder YouTube, vollständig betrieben durch KI-Übersetzung.

- Jeder Beitrag oder jede Antwort, die von Nutzern erstellt wird, kann in einer einzigen Sprache gespeichert werden. Die Plattform übersetzt Inhalte automatisch in 20 Sprachen, sodass Nutzer sie in ihrer bevorzugten Sprache ansehen können.

- Neben der Übersetzung werden andere KI-gestützte Funktionen wie Zusammenfassung, Audioerzeugung und Videogenerierung eine Schlüsselrolle spielen. Im Grunde übermittelt der Nutzer den Prompt-Kontext, und die Plattform übernimmt den Rest.

- Nutzer können Text, Bilder, Audio oder Videos hochladen, und die Plattform wird den Inhalt automatisch in andere Formate umwandeln. Nutzer können entscheiden, wie sie den Inhalt erhalten möchten (z.B. als Text, Bilder, Audio oder Video).

- Plattformen können automatisch Zusammenfassungen generieren, wobei verschiedene Arten der Zusammenfassung in mehreren Sprachen verfügbar sind.

- In jedem Text, Bild, Audio oder Video auf der Plattform kann KI helfen, Inhalte zu generieren, zu verfeinern, zu verbessern, zu reparieren, zusammenzufassen, zu erweitern, in andere Formate umzuwandeln oder neue Formen des Inhalts zu imaginieren.

- Nutzer können die Plattform mit Schlüsselwörtern wie "Englisch" oder "lustig" anpassen, um den Stil der KI-Workflows auf Plattformen wie TikTok anzupassen. Einmal festgelegt, passt die KI den Inhalt entsprechend an.


---

[^1]: Building Effective Agents, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

---

## Die nächste Richtung von KI-Code-Editoren

*08.01.2025*

Kürzlich habe ich daran gearbeitet, eine `xelatex`-Pipeline zu GitHub Actions hinzuzufügen.

Ich stieß auf ein Problem mit dem `fontawesome5`-Paket im GitHub-Flow. Die von 4o-mini vorgeschlagene Lösung (Installation von TeX Live 2021 und Verwendung von `tlmgr install fontawesome5`) funktionierte bei mir nicht. Allerdings schlug 4o einen besseren Ansatz vor: ein Upgrade auf TeX Live 2023 und weiterhin die Verwendung von `tlmgr` zur Installation von `fontawesome5`. Dies löste das Problem nicht vollständig, aber der Wechsel zu TeX Live 2023 verbesserte die Situation erheblich.

Ich habe ChatGPT genutzt, um das Problem zu lösen. Für weitere Details siehe [What ChatGPT O1 Can Do That 4o-mini Cannot](./o1-en).

Zu diesem Zeitpunkt habe ich keine Editoren wie Cursor oder Windsurf verwendet, obwohl ich sie in einem anderen Projekt ausprobiert habe. Das Problem mit diesen Code-Editoren ist, dass sie nur lokale Testausgaben erfassen, was ihre Funktionalität in Cloud-Umgebungen einschränkt.

In Workflows wie GitHub Actions, Jenkins-Jobs oder jedem Code-Deployment- oder Testflow müssen Code-Editoren besser integriert sein. Sie sollten nahtlose Interaktion mit der Cloud und CI/CD-Prozessen bieten.

Diese Integration gilt auch für andere Inhaltserstellungstools – ob für Text, Bilder, Audio oder Video. Diese Tools sollten mit A/B-Test-Systemen integriert sein. KI-Tools könnten Inhalte generieren, und A/B-Test-Tools könnten Feedback liefern. Diese Dynamik ähnelt dem Reinforcement Learning from Human Feedback (RLHF), bei dem KI-Modelle sich basierend auf Feedback aus der realen Welt mit der Zeit verbessern.

Dieses Konzept, RLHF über reine Modell-Outputs hinaus auf reale Test- und Deployment-Umgebungen auszudehnen, scheint eine vielversprechende Richtung für die Verbesserung von sowohl Code-Editoren als auch KI-gestützten Inhaltserstellungstools zu sein.

Der Test kann entweder sofort oder langfristig sein und entweder automatisiert oder mit menschlicher Unterstützung erfolgen. Wenn die Tests automatisiert sind, wie z.B. A/B-Tests für ein KI-Tool, beinhaltet dies immer noch menschliches Feedback, aber der Prozess ist automatisiert. Zum Beispiel können wir den Computer täglich oder stündlich basierend auf A/B-Test-Ergebnissen prüfen lassen, um den Erstellungsprozess zu verbessern. Ähnlich können wir für Jenkins- oder GitHub-Actions-Jobs den Computer nach Abschluss der Aufgaben prüfen lassen.

Wenn menschliche Unterstützung involviert ist, kann das Feedback nicht vollständig von der Maschine verstanden werden und ist oft etwas vage. Zum Beispiel, wenn KI-Tools Inhalte wie Bilder oder Videos erstellen, könnten Menschen anmerken, dass der Inhalt nicht lustig genug ist oder dass ein bestimmtes Detail verbessert werden sollte. Maschinen haben noch einen langen Weg vor sich, um alles perfekt zu machen, und ob etwas "perfekt" ist, hängt oft vom individuellen Geschmack ab. Es ist menschliches Feedback, das Dinge besser macht.

Theoretisch können alle vom Menschen definierten Regeln als Prompts geschrieben werden. Es gibt Nutzer-Prompts und System-Prompts. Wir sollten uns darauf konzentrieren, die Prompts zu verbessern, anstatt jedes Mal den Output zu korrigieren.