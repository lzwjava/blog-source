---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: DJI Mini 3 Tracking-Einschränkungen und Lösungsansätze
translated: true
type: note
---

Das DJI Mini 3 (das Basismodell) verfügt nicht über integrierte Funktionen wie ActiveTrack (visuelles Objektverfolgung) oder Follow-Me-Modus (GPS-basierte Verfolgung), um automatisch einem fahrenden Auto für Fotos oder Videos zu folgen oder darüber zu schweben. Dies ist eine wesentliche Einschränkung im Vergleich zu höherwertigen DJI-Drohnen. Allerdings unterstützt der DJI Mini 3 Pro ActiveTrack, welches die Kamera der Drohne nutzt, um Objekte wie Autos, Personen oder Fahrzeuge visuell zu verfolgen – von hinten, oben oder anderen Positionen aus. Dies ermöglicht das Aufnehmen dynamischer Aufnahmen, während die Drohne einen festgelegten Abstand und eine Höhe beibehält.

Zu APIs für individuelle Entwicklung:
- DJIs Mobile SDK (für Android/iOS Apps) unterstützt die Mini-3-Serie, einschließlich grundlegender Flugsteuerung wie virtuelle Stick-Befehle (z.B. zur manuellen Anpassung von Position/Geschwindigkeit) und Waypoint-Missionen. Man könnte eine eigene App entwickeln, um die Drohne einem Auto auf dessen Weg folgen zu lassen, wenn man Echtzeit-GPS-Daten des Autos integriert (via Bluetooth, eine Begleit-App oder einen externen Sender). Dies wäre keine "Plug-and-Play"-visuelle Verfolgung, könnte aber ein Verfolgen von oben oder hinten annähern, indem man Versätze berechnet (z.B. 10-20 Meter zurück und 50 Meter hoch).
- Allerdings werden die ActiveTrack-Missions-APIs des SDK (für automatisierte visuelle Verfolgung) **nicht unterstützt** auf dem Mini 3 oder Mini 3 Pro – sie sind auf ältere Modelle wie die Mavic Air 2 oder Air 2S beschränkt.
- Für die Fotoaufnahme während des Flugs kann man die Kamera-APIs des SDK nutzen, um Aufnahmen automatisch basierend auf Timern, Entfernung oder eigener Logik auszulösen.

Falls Drittanbieter-Apps in Frage kommen (die das SDK intern nutzen):
- Apps wie Dronelink oder Litchi können einen grundlegenden "Follow-Me"-Modus auf dem Mini 3 ermöglichen, indem sie das GPS des Telefons (oder eines externen Geräts) nutzen. Um speziell ein Auto zu verfolgen, müsste man dieses mit einem GPS-Beacon am Fahrzeug koppeln (z.B. via Smartphone-Hotspot oder einem dedizierten Tracker wie einer Tile- oder AirTag-Alternative, die Daten an die App liefert). Dieses Setup hat bei Nutzern funktioniert, die Autos auf Straßen oder Wegen verfolgten, wobei die Drohne über Kopf oder mit Abstand hinterher flog, um Aufnahmen zu machen.

Zu beachten sind rechtliche/sicherheitstechnische Hinweise: Das Verfolgen von fahrenden Fahrzeugen mit Drohnen muss lokalen Vorschriften entsprechen (z.B. erfordern FAA-Regeln in den USA Sichtkontakt, keine Operationen außerhalb der Sichtweite). Tests in offenen Gebieten durchführen, um Hindernisse zu vermeiden, und das Leichtbaudesign des Mini 3 begrenzt die Windbeständigkeit bei Hochgeschwindigkeitsverfolgungen.

### Referenzen
- [DJI Mini 3 Active Track HACK DJI Mini 3 Follow Me](https://www.youtube.com/watch?v=UYzSdd3iJwA)
- [Does the mini 3 have ai tracking to follow objects like cars](https://www.facebook.com/groups/djimini3ukowners/posts/2726498670890510/)
- [Can someone explain follow me mode? And if it's on mini 3?](https://www.reddit.com/r/dji/comments/13pqbw7/can_someone_explain_follow_me_mode_and_if_its_on/)
- [DJI Mini 3 / Mini 3 Pro - Follow Me Mode With Dronelink](https://www.youtube.com/watch?v=Rhneo8QoXV0)
- [DJI Product SDK Compatibility](https://support.dji.com/help/content?customId=01700000763&spaceId=17&re=US&lang=en&documentType=&paperDocType=ARTICLE)
- [DJI has released MSDK 5.3.0 with support for Mini 3 Pro and Mini 3](https://forum.flylitchi.com/t/dji-has-released-msdk-5-3-0-with-support-for-mini-3-pro-and-mini-3/9512)
- [class ActiveTrackOperator - DJI Mobile SDK Documentation](https://developer.dji.com/api-reference/android-api/Components/Missions/DJIActiveTrackMissionOperator.html)