---
audio: false
generated: false
image: false
lang: de
layout: post
title: Überlegen Sie Upgrades bei der Verwendung von Bibliotheken
translated: true
type: post
---

Ich habe CodeIgniter in meinem Startup-Projekt [Fun Live](https://github.com/lzwjava/live-server) verwendet. Obwohl das Projekt beendet wurde, wollte ich es nach einigen Jahren wiederbeleben, um es zu würdigen. Damals im Jahr 2016 habe ich CodeIgniter 3 verwendet, während die neueste Version jetzt CodeIgniter 4 ist.

Das Upgrade hat sich als problematisch erwiesen, da mein Code eng mit dem CodeIgniter-Framework verknüpft ist. Wenn man dem Upgrade-Leitfaden unter [https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html) folgt, wird deutlich, dass erhebliche Anstrengungen erforderlich sind, um die Codebasis zu aktualisieren.

Diese Erfahrung hat mir eine wichtige Lektion beigebracht: Beim Schreiben von Code sollten wir sorgfältig überlegen, wie wir zukünftige Updates handhaben. Es ist entscheidend, darüber nachzudenken, welche Teile des Codes wir kontrollieren und welche Teile von Drittanbieter-Abhängigkeiten gesteuert werden.