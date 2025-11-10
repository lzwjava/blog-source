---
audio: false
generated: true
image: false
lang: de
layout: post
title: Unterbrechungen brechen Cloud-Inferenz nicht ab
translated: true
type: note
---

Wenn Sie Ihr Python-Skript unterbrechen (z.B. mit Strg+C), während es auf den `generate_images()`-Aufruf wartet, passiert in etwa Folgendes:

1. **Client-seitiges Verhalten**
   – Sobald Sie den Python-Prozess beenden, wird die zugrundeliegende HTTP/gRPC-Verbindung abgebaut.
   – Die GenAI-Client-Bibliothek fängt typischerweise die unterbrochene Verbindung oder den Verbindungsrücksturz ab und löst eine Exception aus (die Sie in Ihrem Skript sehen werden).

2. **Was auf der Seite von Google passiert**
   – Wenn Sie abbrechen, hat Ihre Anfrage bereits den Inferenzdienst von Google erreicht und wurde in die Warteschlange gestellt (oder läuft bereits).
   – Die meisten Cloud-Inferenz-Endpunkte brechen Arbeiten **nicht** automatisch ab, nur weil der Client verschwunden ist. Sie führen Ihren Bildgenerierungsauftrag bis zum Abschluss weiter aus (verbrauchen GPU/TPU und verursachen Kosten), auch wenn keine lebende Verbindung mehr besteht, um das Ergebnis zurückzugeben.
   – Sobald der Auftrag beendet ist, werden die generierten Bilder verworfen – es gibt keinen Rückruf an Sie, es sei denn, Sie haben einen langlebigen Vorgang oder Webhook eingerichtet.

3. **Wie Nginx (oder ein anderer Proxy) sich auswirkt**
   – Wenn sich ein Nginx-Reverse-Proxy vor dem Inferenzdienst befindet, ist sein Standardverhalten, die Client-Verbindung zu überwachen. Sobald der Client abbricht, schließt Nginx seine Upstream-Verbindung zum Inferenzprozess (sendet ein FIN/RST).
   – Der Upstream-Prozess sieht dann eine unterbrochene Socket-Verbindung, wenn er schließlich versucht, die Antwort zu schreiben. Zu diesem Zeitpunkt protokolliert er möglicherweise einen E/A-Fehler, aber – entscheidend – er setzt die von Ihnen angeforderte Berechnung **nicht** zurück und stoppt sie nicht; er kann die Bytes einfach nicht liefern.
   – Sie können die Nginx-Direktive `proxy_ignore_client_abort` anpassen – wenn Sie sie auf `on` setzen, hält Nginx die Upstream-Verbindung auch dann aufrecht, wenn der Client die Verbindung trennt (was Ihnen ermöglichen kann, das Schreiben von Protokollen oder andere Bereinigungen vollständig abzuschließen).

4. **Wichtige Erkenntnisse für Ihr Skript**

   * **Unterbrechungen “stellen keine Bereitstellung zurück”** oder brechen das Modell auf den Servern von Google nicht ab – Ihnen werden weiterhin die vollen Inferenzkosten berechnet.
   * Wenn Sie abbrechbare Inferenz benötigen, müssten Sie ein anderes Muster verwenden, zum Beispiel:

     1. Einen nicht-blockierenden Stapelauftrag oder langlebigen Vorgang übermitteln,
     2. Dessen Status abfragen oder ihn explizit über einen separaten API-Aufruf abbrechen.

Kurz gesagt: Das Abbrechen Ihres Skripts bei 5 s stoppt Ihr lokales Warten und schließt den Socket, aber die Google-Inferenz läuft auf ihrer Hardware trotzdem bis zum Abschluss weiter (und Nginx oder Ähnliches verwirft die Antwort einfach ins Nichts, sobald sie fertig ist).