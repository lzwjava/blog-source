---
audio: false
lang: de
layout: post
title: Gängige HTTP-Statuscodes
translated: true
---

Hast du dich jemals über einen "404 Not Found" Fehler gestolpert, während du im Internet surfst, und dich gefragt, was es damit auf sich hat? Oder hast du vielleicht einen "500 Internal Server Error" erlebt und dich gefragt, warum er aufgetaucht ist. Diese Zahlen sind **HTTP-Statuscodes**, und sie sind Schlüsselspieler in der Kommunikation im Internet. In diesem Blog werden wir erklären, was diese Codes sind, einige der häufigsten Codes erkunden und erklären, warum sie es wert sind, verstanden zu werden – ob du Entwickler bist oder einfach nur ein neugieriger Webnutzer.

---

## Was ist HTTP?

Lass uns mit den Grundlagen beginnen. **HTTP**, oder *Hypertext Transfer Protocol*, ist das System, das den Datenaustausch im World Wide Web antreibt. Wenn du eine URL in deinen Browser eingibst und Enter drückst, sendet dein Browser eine **HTTP-Anfrage** an den Server, der diese Website hostet. Der Server antwortet dann mit einer **HTTP-Antwort**, die einen dreistelligen **Statuscode** enthält. Dieser Code sagt dir, ob deine Anfrage funktioniert hat und, wenn nicht, was schiefgelaufen ist.

---

## Die fünf Klassen von HTTP-Statuscodes

HTTP-Statuscodes sind in fünf Kategorien unterteilt, jede mit einem spezifischen Zweck:

- **1xx (Informativ)**: Der Server hat deine Anfrage erhalten und arbeitet noch daran.
- **2xx (Erfolgreich)**: Deine Anfrage wurde empfangen, verstanden und erfolgreich abgeschlossen.
- **3xx (Weiterleitung)**: Du musst einen zusätzlichen Schritt unternehmen – wie das Folgen einer neuen URL – um das zu bekommen, was du möchtest.
- **4xx (Client-Fehler)**: Etwas ist auf deiner Seite schiefgelaufen, wie ein Tippfehler oder fehlende Anmeldeinformationen.
- **5xx (Server-Fehler)**: Der Server ist auf ein Problem gestoßen und konnte deine gültige Anfrage nicht verarbeiten.

Jetzt tauchen wir in die Codes ein, die du am wahrscheinlichsten treffen wirst.

---

## Gängige HTTP-Statuscodes erklärt

Hier ist eine Übersicht der bekanntesten HTTP-Statuscodes, mit Beispielen, um sie klar zu machen:

### 200 OK
- **Was es bedeutet**: Die Anfrage hat perfekt funktioniert. Der Server hat sie verarbeitet und die angeforderten Daten zurückgesendet.
- **Beispiel**: Eine Webseite wie `www.example.com` wird ohne Probleme geladen? Das ist ein 200 OK.

### 201 Created
- **Was es bedeutet**: Deine Anfrage war erfolgreich und eine neue Ressource wurde als Ergebnis erstellt.
- **Beispiel**: Ein Formular ausfüllen, um sich für einen Newsletter anzumelden, und der Server bestätigt, dass dein Konto erstellt wurde.

### 301 Moved Permanently
- **Was es bedeutet**: Die gewünschte Ressource hat sich dauerhaft zu einer neuen URL verschoben, und du solltest diese neue Adresse in Zukunft verwenden.
- **Beispiel**: Ein Blogbeitrag verschiebt sich von `oldblog.com/post1` zu `newblog.com/post1`, und der Server leitet dich weiter.

### 302 Found
- **Was es bedeutet**: Die Ressource befindet sich vorübergehend an einer anderen URL, aber du solltest die ursprüngliche URL für zukünftige Anfragen weiterhin verwenden.
- **Beispiel**: Eine Website-Homepage wird vorübergehend zu einer Seite mit einem Sonderangebot weitergeleitet.

### 404 Not Found
- **Was es bedeutet**: Der Server kann das Gesuchte nicht finden – möglicherweise ist die Seite verschwunden oder die URL ist falsch.
- **Beispiel**: Eingabe von `www.example.com/oops` und Landen auf einer Fehlermeldung, weil „oops“ nicht existiert.

### 403 Forbidden
- **Was es bedeutet**: Der Server kennt, was du möchtest, lässt dich es aber nicht haben, weil dir die Berechtigung fehlt.
- **Beispiel**: Versuch, ein privates Admin-Panel ohne Anmeldung zu betreten.

### 401 Unauthorized
- **Was es bedeutet**: Du musst dich authentifizieren (wie Anmeldung), bevor du fortfahren kannst.
- **Beispiel**: Besuch eines Mitglieder-Forums ohne vorherige Anmeldung.

### 400 Bad Request
- **Was es bedeutet**: Der Server kann deine Anfrage aufgrund schlechter Syntax oder ungültiger Daten nicht verstehen.
- **Beispiel**: Ein Formular mit einem E-Mail-Feld, das nur Unsinn enthält, wie „@#$%“.

### 500 Internal Server Error
- **Was es bedeutet**: Etwas ist auf der Serverseite kaputtgegangen, aber es wird dir nicht gesagt, was.
- **Beispiel**: Eine Website stürzt wegen eines Fehlers ab, den die Entwickler nicht entdeckt haben.

### 503 Service Unavailable
- **Was es bedeutet**: Der Server ist offline – möglicherweise für Wartungsarbeiten oder weil er überlastet ist.
- **Beispiel**: Versuch, während eines großen Verkaufs online einzukaufen, nur um eine „später wieder versuchen“ Nachricht zu sehen.

---

## Ein paar weitere Codes, die es wert sind, bekannt zu sein

Diese Codes sind nicht so häufig, tauchen aber oft genug auf, um erwähnt zu werden:

- **100 Continue**: Der Server ist einverstanden, dass du eine große Anfrage sendest, also mach weiter.
- **204 No Content**: Die Anfrage hat funktioniert, aber es gibt nichts zurückzusenden (z.B. nach dem Löschen von etwas).
- **304 Not Modified**: Die Ressource hat sich nicht geändert, also verwende die Version, die du bereits im Cache hast.
- **429 Too Many Requests**: Du hast den Server zu oft kontaktiert, und er sagt dir, dass du dich beruhigen sollst (häufig bei APIs).
- **502 Bad Gateway**: Ein Zwischenserver hat eine schlechte Antwort vom Hauptserver erhalten, den er erreichen möchte.

---

## Alltagsvergleiche für HTTP-Codes

Lass uns diese Codes mit einigen realen Vergleichen nachvollziehbar machen:

- **200 OK**: Du bestellst einen Kaffee, und er wird dir genau so serviert, wie du ihn magst.
- **201 Created**: Du bestellst ein maßgeschneidertes T-Shirt, und der Laden sagt: „Es wird erstellt!“
- **301 Moved Permanently**: Dein Lieblingsdiner zieht um und gibt dir die neue Adresse.
- **302 Found**: Das Diner ist wegen Reparaturen geschlossen, aber sie zeigen dir ihren Foodtruck in der Nähe.
- **404 Not Found**: Du fragst nach einem Buch in der Bibliothek, aber es ist nicht in ihrem Katalog.
- **403 Forbidden**: Du versuchst, eine private Party ohne Einladung zu stürmen.
- **401 Unauthorized**: Du versuchst, ein Fitnessstudio zu nutzen, aber du hast deine Mitgliedskarte vergessen.
- **400 Bad Request**: Du bestellst Essen in einer Sprache, die der Kellner nicht versteht.
- **500 Internal Server Error**: Du fragst einen Koch nach Suppe, und die Küche fängt Feuer.
- **503 Service Unavailable**: Du rufst eine Hotline an, aber alle Leitungen sind besetzt.

---

## Warum sollten dich HTTP-Codes interessieren?

Für **Entwickler** sind diese Codes Gold wert. Sie helfen dir, Probleme zu beheben, Fehler elegant zu behandeln und Apps zu erstellen, die Benutzer nicht im Stich lassen. Zum Beispiel kann das Wissen, ob ein 400- oder 500-Fehler aufgetreten ist, darauf hinweisen, ob das Problem beim Benutzer oder beim Server liegt.

Für **normale Benutzer** kann ein grundlegendes Verständnis dieser Codes Web-Hickups entmystifizieren. Ein 404 bedeutet, dass die Seite fehlt, während ein 503 darauf hinweist, dass man es später noch einmal versuchen sollte. Es ist wie ein Cheat-Sheet für das Internet.

Außerdem **Suchmaschinen** nutzen diese Codes für SEO. Eine 301-Weiterleitung kann das Ranking deiner Seite bewahren, wenn du Inhalte verschiebst, während ein 404 Google signalisieren könnte, dass es sich um eine Sackgasse handelt.

---

## Zusammenfassung

HTTP-Statuscodes sind die Art und Weise, wie das Web mit uns spricht, uns mitteilt, ob unsere Anfragen ins Schwarze getroffen haben oder danebengegangen sind. Vom triumphalen **200 OK** bis zum gefürchteten **500 Internal Server Error** erzählt jeder Code eine Geschichte. Ob du eine Seite codest oder einfach nur surfst, das Verständnis dieser gängigen Codes kann dein Online-Leben glatter und weniger mysteriös machen. Also beim nächsten Mal, wenn du einen 404 siehst, weißt du, dass es nicht du bist – es ist nur das Web, das sagt: „Ich kann diese Seite nicht finden!“