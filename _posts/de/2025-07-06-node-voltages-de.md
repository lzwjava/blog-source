---
audio: false
generated: true
lang: de
layout: post
title: Knotenanalyse löst Knotenspannungen
translated: true
type: note
---

Die primäre unbekannte Variable, die in der Knotenanalyse gelöst wird, sind **Knotenspannungen**.

Hier ist eine Analyse jeder Option:

* **Zweigströme:** Obwohl Zweigströme *nach* dem Lösen der Knotenspannungen bestimmt werden können, sind sie nicht die primären Variablen, die in der Knotenanalyse direkt gelöst werden. Die Knotenanalyse konzentriert sich auf die Anwendung des Kirchhoffschen Stromgesetzes (KCL) an jedem Knoten, welches in Bezug auf Spannungen und Widerstände ausgedrückt wird, nicht direkt in Bezug auf Ströme.

* **Maschenströme:** Maschenströme sind die primären unbekannten Variablen, die in der **Maschenanalyse** (auch als Schleifenanalyse bekannt) gelöst werden, nicht in der Knotenanalyse. Die Maschenanalyse wendet das Kirchhoffsche Spannungsgesetz (KVL) um unabhängige Maschen an.

* **Knotenspannungen:** Dies ist die korrekte Antwort. In der Knotenanalyse definieren wir einen Referenzknoten (oft als Masseknoten bezeichnet) und weisen dann den anderen unabhängigen Knoten im Stromkreis unbekannte Spannungsvariablen zu. Durch die Anwendung des Kirchhoffschen Stromgesetzes (KCL) an jedem unabhängigen Knoten bilden wir ein System linearer Gleichungen, bei dem die Unbekannten genau diese Knotenspannungen sind. Sobald die Knotenspannungen bekannt sind, können alle anderen Stromkreisgrößen (wie Zweigströme, Leistungsverbrauch usw.) einfach berechnet werden.

* **Leistungsverbrauch:** Der Leistungsverbrauch ist eine Größe, die *nachdem* die Knotenspannungen (und anschließend die Zweigströme) bekannt sind, berechnet werden kann. Er ist ein Ergebnis der Analyse, keine primäre unbekannte Variable, die zur Aufstellung der Anfangsgleichungen in der Knotenanalyse verwendet wird.