---
audio: false
generated: false
lang: de
layout: post
title: Mesh-Router
translated: true
---

## TP-Link AX3000 - TL-XDR 3050

Ich habe 2023 begonnen, ein Mesh-Router-System zu verwenden. Ich habe ein TP-Link AX3000-System gekauft, das aus zwei Mesh-Routern besteht: einer Haupteinheit und einer Satelliteneinheit. Es hat mich damals etwa 484 CNY gekostet, aber jetzt kostet es auf JD.com nur noch 395 CNY.

Ursprünglich habe ich dieses System in meinem großen Haus verwendet, aber später habe ich es in das Haus meiner Eltern verlegt.

## ZTE AC1200

Während einiger Tage des Frühlingsfestes 2025 blieb meine Familie in meinem großen Haus und erlebte erneut eine schlechte WiFi-Netzqualität. Um dies zu beheben, kaufte ich einen weiteren Mesh-Router, den ZTE AC1200, der etwa 108 CNY kostet.

Ähnliche Produkte, die bei Walmart erhältlich sind, umfassen den TP-Link WiFi Mesh Router, den Eero Dual Band Mesh Router und den NetGear Nighthawk AX3000. Die Preise für die meisten dieser Produkte liegen zwischen 50 USD und 200 USD.

Für den ZTE AC1200 Mesh-Router konnte ich einfach einen kaufen und den Bridge-Modus verwenden, wodurch er ein WiFi-Signal empfängt und dann sein eigenes WiFi-Signal aussendet. Es funktioniert einwandfrei. Ursprünglich war die Domain-Adresse des Routers 192.168.5.1. Nach der Aktivierung des Bridge-Modus ist diese IP-Adresse nicht mehr erreichbar. Stattdessen leitet 192.168.1.1 Sie zum Hauptrouter in Ihrem Heimnetzwerk weiter. An diesem Punkt können Sie das Kontrollzentrum des Routers aufrufen, indem Sie zu http://zte.home navigieren.

Wenn Sie auf den Hauptrouter zugreifen können, können Sie die verbundenen Geräte und ihre IP-Adressen sehen. Dann können Sie versuchen, auf jedes Gerät zuzugreifen, um festzustellen, welches der Sub-Router ist. In meinem Fall war es 192.168.1.23, die Adresse des ZTE AC1200 Mesh-Routers.

Für Mobiltelefone, die wir im Haus herumbewegen, ist es besser, den 2,4 GHz-Kanal zu verwenden, da er stabiler ist. Für Laptops oder Desktop-Computer, die wir normalerweise in unseren Schlafzimmern oder Arbeitszimmern verwenden, ist der 5 GHz-Kanal besser geeignet, da er schneller ist.

Nach einigen Tagen der Nutzung stelle ich fest, dass er etwas schlechter ist. Die Geschwindigkeit oder das Signal ist schlechter als beim TL-XDR 3050.

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*Quelle: JD.com*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*Quelle: Walmart.com*{: .caption }

## 12V-Stromversorgung für Router

Ein USB-Spannungswandler-Kabel kann verwendet werden, um Router mit einer Powerbank zu betreiben.

In einigen Fällen kann das Wandlerkabel von einer Powerbank den Router jedoch nicht korrekt einrichten. Der Router startet möglicherweise kontinuierlich neu.

{: .centered }
![](assets/images/cable-tester/12v.jpg){: .responsive }
*Quelle: JD.com*{: .caption }

## Zwei Möglichkeiten, einem Sub-Router zu helfen, den Hauptrouter zu finden

Manchmal kann ein Sub-Router den Hauptrouter nicht leicht finden, wenn das Signal schwach ist.

Wenn wir den Sub-Router weit vom Hauptrouter entfernt platzieren müssen, frage ich mich, ob es schneller ist, ihn zunächst in der Nähe zu verbinden und ihn dann weiter weg zu bewegen, anstatt zu versuchen, ihn zu verbinden, wenn er bereits an der entfernten Position ist.

Die Aufrechterhaltung einer Verbindung in der Nähe ermöglicht es ihnen, miteinander zu kommunizieren. Ich habe festgestellt, dass diese Methode effektiver ist.