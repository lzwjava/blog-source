---
audio: false
generated: false
lang: de
layout: post
title: Workflow ist BFS, Agent ist DFS
translated: true
---

Laut Anthropic [^1]:

- **Workflows** sind Systeme, in denen LLMs und Tools über vordefinierte Code-Pfade orchestriert werden.
- **Agents** hingegen sind Systeme, in denen LLMs ihre eigenen Prozesse und die Nutzung von Tools dynamisch steuern, wodurch die Flexibilität bei der Aufgabenbewältigung erhalten bleibt.

Was ich daraus verstehe, ist:

- Die Verwendung von **Workflows** zur Verbesserung einer App oder Plattform ähnelt **BFS (Breitensuche)**, bei der Aufgaben systematisch und Ebene für Ebene abgeschlossen werden.
- Die Verwendung von **Agenten** ist eher wie **DFS (Tiefensuche)**, bei der Aufgaben auf eine explorativere, schrittweise Art und Weise angegangen werden.

Manchmal können **BFS** und **DFS** kombiniert werden. DFS kann in einen anderen DFS eingebettet sein, und dasselbe gilt für BFS.

Zum Beispiel ist **o1 (chain-of-thought)** wie die Breitensuche (BFS). Zunächst werden die Hauptaufgaben in separate Schritte unterteilt, und jeder Schritt wird in detailliertere Erklärungen erweitert. Dann wird basierend auf all diesen Überlegungen das Endergebnis geliefert.

Für sehr komplexe Aufgaben, wie die Aufforderung an eine KI, eine YouTube-App zu erstellen oder ein Betriebssystem zu entwickeln, könnte sie BFS (Breitensuche), DFS (Tiefensuche) oder eine Kombination aus beidem verwenden. Es hängt wirklich davon ab, wie wir BFS und DFS einsetzen – manchmal muss die KI tief graben (DFS), und manchmal muss sie ihren Ansatz erweitern (BFS).

Eine weitere Überlegung ist, dass die KI bei jedem Schritt bewerten sollte, was als Nächstes zu tun ist, um ihre Ziele zu erreichen.

**Ziele** sind ein interessanter Aspekt. Es kann viele Ziele geben, wie zum Beispiel die Erstellung einer YouTube-App, bei der die KI sicherstellen muss, dass der gesamte Code gut funktioniert, alle Funktionen implementiert sind und alle Tests bestanden werden. Die Art und Weise, wie diese Ziele erreicht werden, ist faszinierend. Sollte die KI ein Ziel nach dem anderen angehen, oder sollte sie gleichzeitig Fortschritte bei allen Zielen machen und dann iterativ an jedem arbeiten?

---

[^1]: Effektive Agenten entwickeln, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

