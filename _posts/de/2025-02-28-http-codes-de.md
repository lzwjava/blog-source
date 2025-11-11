---
audio: false
generated: true
lang: de
layout: post
title: Häufige HTTP-Antwortcodes
translated: true
type: note
---

Bist du schon einmal über einen "404 Not Found"-Fehler gestolpert, während du im Internet gesurft hast, und hast dich gefragt, was es damit auf sich hat? Oder vielleicht ist dir ein "500 Internal Server Error" begegnet und du hast dir den Kopf darüber zerbrochen, warum er aufgetaucht ist. Diese Zahlen sind **HTTP-Antwortcodes**, und sie sind Schlüsselfiguren in der Kommunikation des Internets. In diesem Blog werden wir erklären, was diese Codes sind, einige der häufigsten unter die Lupe nehmen und erläutern, warum es sich lohnt, sie zu verstehen – egal, ob du ein Entwickler oder einfach ein neugieriger Internetnutzer bist.

---

## Was ist HTTP?

Fangen wir mit den Grundlagen an. **HTTP**, oder *Hypertext Transfer Protocol*, ist das System, das den Datenaustausch im World Wide Web ermöglicht. Wenn du eine URL in deinen Browser eingibst und die Eingabetaste drückst, sendet dein Browser eine **HTTP-Anfrage** an den Server, der diese Website hostet. Der Server antwortet dann mit einer **HTTP-Antwort**, die einen dreistelligen **Statuscode** enthält. Dieser Code teilt dir mit, ob deine Anfrage funktioniert hat und, falls nicht, was schiefgelaufen ist.

---

## Die fünf Klassen von HTTP-Antwortcodes

HTTP-Antwortcodes sind in fünf Kategorien unterteilt, jede mit einer bestimmten Aufgabe:

- **1xx (Informationell)**: Der Server hat deine Anfrage erhalten und arbeitet noch daran.
- **2xx (Erfolgreich)**: Deine Anfrage wurde empfangen, verstanden und erfolgreich bearbeitet.
- **3xx (Weiterleitung)**: Du musst einen zusätzlichen Schritt unternehmen – wie einer neuen URL zu folgen – um das Gewünschte zu erhalten.
- **4xx (Client-Fehler)**: Irgendetwas stimmt auf deiner Seite nicht, zum Beispiel ein Tippfehler oder fehlende Berechtigungen.
- **5xx (Server-Fehler)**: Der Server ist auf ein Problem gestoßen und konnte deine gültige Anfrage nicht bearbeiten.

Lass uns nun in die Codes eintauchen, denen du höchstwahrscheinlich begegnen wirst.

---

## Häufige HTTP-Antwortcodes erklärt

Hier ist eine Übersicht der gängigsten HTTP-Antwortcodes, mit Beispielen, um sie ganz klar zu verstehen:

### 200 OK
- **Was es bedeutet**: Die Anfrage hat perfekt funktioniert. Der Server hat sie bearbeitet und die angeforderten Daten zurückgeschickt.
- **Beispiel**: Lädt eine Webseite wie `www.example.com` ohne Probleme? Das ist ein 200 OK.

### 201 Created
- **Was es bedeutet**: Deine Anfrage war erfolgreich und eine neue Ressource wurde als Ergebnis erstellt.
- **Beispiel**: Du übermittelst ein Formular, um dich für einen Newsletter anzumelden, und der Server bestätigt, dass dein Konto erstellt wurde.

### 301 Moved Permanently
- **Was es bedeutet**: Die gewünschte Ressource ist dauerhaft an eine neue URL umgezogen, und du solltest diese neue Adresse zukünftig verwenden.
- **Beispiel**: Ein Blogbeitrag wechselt von `oldblog.com/post1` zu `newblog.com/post1`, und der Server leitet dich weiter.

### 302 Found
- **Was es bedeutet**: Die Ressource ist vorübergehend unter einer anderen URL erreichbar, aber verwende weiterhin die ursprüngliche für zukünftige Anfragen.
- **Beispiel**: Die Homepage einer Website wird kurzzeitig auf eine Sonderangebotsseite umgeleitet.

### 404 Not Found
- **Was es bedeutet**: Der Server kann das, was du suchst, nicht finden – vielleicht ist die Seite nicht mehr da oder die URL ist falsch.
- **Beispiel**: Du gibst `www.example.com/oops` ein und landest auf einer Fehlerseite, weil "oops" nicht existiert.

### 403 Forbidden
- **Was es bedeutet**: Der Server weiß, was du willst, wird es dir aber nicht geben, weil dir die Berechtigung fehlt.
- **Beispiel**: Du versuchst, auf ein privates Admin-Panel zuzugreifen, ohne dich anzumelden.

### 401 Unauthorized
- **Was es bedeutet**: Du musst dich authentifizieren (z. B. durch Anmelden), bevor du fortfahren kannst.
- **Beispiel**: Du besuchst ein nur für Mitglieder zugängliches Forum, ohne dich vorher anzumelden.

### 400 Bad Request
- **Was es bedeutet**: Der Server kann deine Anfrage aufgrund fehlerhafter Syntax oder ungültiger Daten nicht verstehen.
- **Beispiel**: Du übermittelst ein Formular mit einem E-Mail-Feld, das nur Kauderwelsch wie "@#$%" enthält.

### 500 Internal Server Error
- **Was es bedeutet**: Auf Serverseite ist etwas schiefgelaufen, aber es wird dir nicht mitgeteilt, was.
- **Beispiel**: Eine Website stürzt ab, weil die Entwickler einen Bug nicht erkannt haben.

### 503 Service Unavailable
- **Was es bedeutet**: Der Server ist nicht erreichbar – vielleicht wegen Wartungsarbeiten oder weil er überlastet ist.
- **Beispiel**: Du versuchst, während eines Massenandrangs online einzukaufen, und siehst nur eine "Versuche es später noch einmal"-Nachricht.

---

## Ein paar weitere Codes, die es zu kennen lohnt

Diese Codes sind nicht so häufig, tauchen aber oft genug auf, um eine Erwähnung zu verdienen:

- **100 Continue**: Der Server hat kein Problem damit, dass du eine große Anfrage sendest, also leg los.
- **204 No Content**: Die Anfrage war erfolgreich, aber es gibt keine Daten zum Zurückschicken (z. B. nach dem Löschen einer Ressource).
- **304 Not Modified**: Die Ressource hat sich nicht geändert, verwende also die Version, die du bereits im Cache hast.
- **429 Too Many Requests**: Du hast den Server zu oft angefragt, und er sagt dir, dass du dich etwas zurückhalten sollst (häufig bei APIs).
- **502 Bad Gateway**: Ein zwischengeschalteter Server hat eine fehlerhafte Antwort vom Hauptserver erhalten, den er erreichen will.

---

## Alltagsanalogien für HTTP-Codes

Machen wir diese Codes mit einigen Analogien aus der realen Welt greifbar:

- **200 OK**: Du bestellst einen Kaffee, und er wird dir genau so überreicht, wie du ihn magst.
- **201 Created**: Du bestellst ein individuelles T-Shirt, und der Laden sagt: "Es ist in Arbeit!"
- **301 Moved Permanently**: Dein Stamm-Imbiss zieht auf die andere Seite der Stadt und gibt dir die neue Adresse.
- **302 Found**: Der Imbiss ist wegen Renovierungsarbeiten geschlossen, weist dich aber auf seinen Food-Truck in der Nähe hin.
- **404 Not Found**: Du fragst in der Bibliothek nach einem Buch, aber es ist nicht in ihrem Katalog.
- **403 Forbidden**: Du versuchst, eine private Party zu stürmen, ohne eingeladen zu sein.
- **401 Unauthorized**: Du versuchst, ein Fitnessstudio zu benutzen, hast aber deine Mitgliedskarte vergessen.
- **400 Bad Request**: Du bestellst Essen in einer Sprache, die der Kellner nicht versteht.
- **500 Internal Server Error**: Du bittest einen Koch um Suppe, und die Küche fängt Feuer.
- **503 Service Unavailable**: Du rufst eine Hotline an, aber alle Leitungen sind besetzt.

---

## Warum solltest du dich für HTTP-Codes interessieren?

Für **Entwickler** sind diese Codes Gold wert. Sie helfen dir, Probleme zu debuggen, Fehler elegant zu behandeln und Apps zu bauen, die die Nutzer nicht im Regen stehen lassen. Wenn du zum Beispiel weißt, ob ein 400- oder 500-Fehler aufgetreten ist, kannst du eingrenzen, ob der Fehler beim Nutzer oder beim Server liegt.

Für **reguläre Nutzer** kann ein grundlegendes Verständnis dieser Codes Web-Pannen entmystifizieren. Eine 404 bedeutet, dass die Seite fehlt, während eine 503 nahelegt, es später noch einmal zu versuchen. Es ist, als hättest du einen Spickzettel für das Internet.

Zudem verlassen sich **Suchmaschinen** auf diese Codes für die SEO. Eine 301-Weiterleitung kann das Ranking deiner Website erhalten, wenn du Inhalte verschiebst, während eine 404 für Google eine Sackgasse signalisieren könnte.

---

## Zusammenfassung

HTTP-Antwortcodes sind die Art und Weise des Webs, mit uns zu kommunizieren. Sie teilen uns mit, ob unsere Anfragen ins Schwarze getroffen haben oder daneben gegangen sind. Vom triumphierenden **200 OK** bis zum gefürchteten **500 Internal Server Error** erzählt jeder Code eine Geschichte. Egal, ob du eine Website programmierst oder einfach nur surfst – ein Verständnis dieser gängigen Codes kann dein Online-Leben reibungsloser und weniger rätselhaft machen. Wenn du also das nächste Mal eine 404 siehst, weißt du, dass nicht du es bist – es ist nur das Web, das sagt: "Diese Seite kann ich nicht finden!"