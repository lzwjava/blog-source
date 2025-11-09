---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: AWS-Ausfall und das Yacht-Meme
translated: true
type: note
---

Ah, verstanden – du hast recht, das ist ein guter Hinweis. Der AWS-US-EAST-1-Ausfall am 19.-20. Oktober *hat* tatsächlich stattgefunden (DynamoDB-DNS-Auflösungsfehler, die zu stundenlangen Störungen bei 36+ Diensten eskalierten), aber der Teil mit James Hamiltons "Yachten-Heldentaten"? Das ist pures Internet-Meme-Gold, kein Fakt. Es stammt von einer frechen Zeile im offiziellen Status-Update von AWS ("At 2:57 PM PDT, James Hamilton's yacht made landfall"), die Teams während des Chaos scherzhaft aufgriffen. Hamilton *lebt* tatsächlich auf einer Yacht (der MV Dirona, die in der Nähe der Rechenzentren in Virginia liegt), und er ist eine echte Legende für schnelle Lösungen bei früheren Ausfällen, aber es gibt keine Beweise dafür, dass er tatsächlich anlandete und das DNS-Scaling in 4 Minuten debuggt hat. Es ist zu einer viralen Übertreibung geworden – eine Art Tech-Folklore – mit Memes von ihm als Cloud-Pirat, aber das AWS-Post-Mortem konzentrierte sich auf die technische Ursache (Retry-Storms, die Resolver überforderten), ohne ihn als alleinigen Retter zu nennen.

Die tatsächliche Lösung umfasste parallele Teamanstrengungen: Patchen von DynamoDB-Endpunkten, Stabilisieren von EC2-Starts und Umleiten von Datenverkehr. Hamilton hat wahrscheinlich remote oder durch Koordination beigetragen (er ist SVP of Engineering), aber das Anlegen der Yacht? Trockener AWS-Humor vom Feinsten, verstärkt durch X- und Blind-Threads.

Wenn du dich für den Ausfall beruflich oder aus Neugier interessierst, sollte das vollständige RCA bald erscheinen – AWS legt dies normalerweise innerhalb einer Woche vor.

[AWS Outage Post-Mortem Tease](https://aws.amazon.com/premiumsupport/technology/aws-service-health-dashboard/)
[TeamBlind Thread on the Meme](https://www.teamblind.com/post/distinguished-engineer-fixed-aws-outage-in-4-minutes-46jllgcs)
[X Thread with Status Screenshot](https://x.com/NotTuxedoSam/status/1980412758127775977)
[LinkedIn Breakdown of What Actually Broke](https://www.linkedin.com/posts/charlesmartin14_apparently-amazons-top-engineer-lives-on-activity-7386236616094203904-XoUz)