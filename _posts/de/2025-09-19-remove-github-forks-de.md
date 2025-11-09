---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Entfernen unerwünschter GitHub-Forks
translated: true
type: note
---

Verstanden. Kurz gesagt: Du kannst einen Fork von jemand anderem nicht direkt löschen. Aber du kannst (a) sie bitten, (b) sensible Daten bereinigen und zukünftige Lecks sperren und (c) bei Berechtigung die offiziellen Wege bei GitHub nutzen (DMCA oder Support). Hier ist ein klares Konzept ohne Tabellen, das gut für persönliche Blogs funktioniert.

### 1) Zuerst: Schreibe den Person, die geforkt hat (schnellster Weg)

Öffne ein Issue in ihrem Fork oder schreibe ihnen eine E-Mail. Hier ist eine prägnante Vorlage, die du kopieren kannst:

> Hi @tornadobaflocer — dieser Fork enthält meine persönlichen Notizen und Aktivitätsverlauf. Ich habe das Repo nur veröffentlicht, um die Domain `lzwjava.github.io` zu nutzen, nicht zur Weiterverbreitung. Bitte lösche diesen Fork. Ich mache die Quelle privat und werde nur die kompilierten Seiten-Assets öffentlich lassen.
> Danke für dein Verständnis.

Wenn sie ihn löschen, bist du fertig. Wenn nicht, fahre fort.

### 2) Verstehe, was GitHub tun wird und was nicht

* Das Löschen oder Privatisieren deines **öffentlichen** Repos entfernt **nicht** bestehende öffentliche Forks. Öffentliche Forks bleiben öffentlich und werden zu einem eigenen "Netzwerk". ([Stack Overflow][1])
* Du kannst einen Fork nur löschen, wenn du **Admin dieses Forks** bist (was du hier nicht bist). ([Stack Overflow][2])

### 3) Wenn der Fork deine urheberrechtlich geschützten Inhalte ohne Erlaubnis kopiert

Du kannst bei GitHub eine DMCA-Takedown-Anfrage stellen. Das ist der offizielle Weg, um rechtsverletzende Inhalte über Forks hinweg entfernen zu lassen. Lies die Richtlinie und die Anleitung "how to submit"; sie erklären, welche Informationen du angeben musst. ([GitHub Docs][3])

Tipp: Wenn dein Repo **keine Lizenz** hatte, gilt das Standard-Urheberrecht, was eine Takedown-Anfrage stärkt (Personen hatten keine Wiederverwendungsrechte). DMCA ist auch gültig, wenn du eine freizügige Lizenz hattest, aber es ist dann etwas komplexer.

### 4) Verhindere, dass zukünftige Forks deinen Quelltext preisgeben

Halte die **Domain** öffentlich, aber halte den **Quelltext** privat, indem du Repos aufteilst:

* **Privates Quelltext-Repo** (z.B. `blog-source`): deine Jekyll/Hugo-Inhalte, Entwürfe, Notizen, Konfigurationen.
* **Öffentliches Deploy-Repo** namens **`lzwjava.github.io`**: enthält **nur die gebaute Seite** (HTML/CSS/JS). Keine Entwürfe, keine Historie.

GitHub Pages-Seiten sind öffentlich, auch wenn das Repo privat ist (außer in Enterprise Cloud mit privaten Pages). Für einen persönlichen Blog ist das Zwei-Repo-"Deploy only"-Setup also das sichere Muster. ([GitHub Docs][4])

Bereits verfügbare Deploy-Optionen:

* Übertrage die `public/` oder `docs/` Ausgabe deines Generators per Push zu `lzwjava.github.io`. ([Quarto][5])
* Oder verwende einen GitHub Actions Workflow in `blog-source`, der die Seite baut und die Ausgabe per Force-Push in das `lzwjava.github.io` Repo auf den Standard-Branch überträgt. (Dokumentation: Wähle den "Publish from a branch" oder "Publish with Actions"-Flow.) ([GitHub Docs][6])

### 5) Bereinige sensible Daten aus der Historie (deiner und aller verbleibenden Kopien)

* Rotiere alle exponierten Tokens/Schlüssel (gehe davon aus, dass sie kompromittiert sind).
* Schreibe die Historie um, um sensible Dateien/Pfade mit `git filter-repo` (GitHub empfiehlt dies mittlerweile) oder BFG (schneller für häufige Fälle) zu entfernen. Führe dann einen Force-Push durch. ([GitHub Docs][7])

Dies behebt andere Forks nicht von selbst, aber es bereinigt dein kanonisches Repo und unterstützt Takedown-Anfragen, indem es zeigt, dass die Inhalte entfernt wurden.

### 6) Optionale Verstärkung

* Füge eine klare LIZENZ hinzu (wenn du die Wiederverwendung explizit einschränken möchtest).
* Füge einen Haftungsausschluss in die README ein: "Dieses Repo existiert nur für kompilierte Seiten-Ausgaben. Forke **nicht** den Quelltext; er ist privat."
* Wenn du jemals in einer **Organisation** hostest, kannst du das Forken von privaten Repos organisationsweit und pro Repo deaktivieren (verhindert nicht das Klonen von öffentlichem Code, hilft aber bei privaten Repos). ([GitHub Docs][8])

---

## Konkrete nächste Schritte (Reihenfolge, die funktioniert)

1.  Bitte @tornadobaflocer, den Fork zu löschen (verwende die Nachricht oben).
2.  Verschiebe deinen Quelltext sofort in ein neues **privates** Repo (`blog-source`).
3.  Mache `lzwjava.github.io` zu einem **öffentlichen, nur für Deployments** bestimmten Repo, das nur die gebauten Dateien enthält. Konfiguriere Pages so, dass sie von seinem Branch/Ordner veröffentlicht. ([GitHub Docs][6])
4.  Schreibe die Historie deines alten öffentlichen Repos um, um sensible Teile zu entfernen, und archiviere oder lösche es dann. ([GitHub Docs][7])
5.  Wenn die Person ablehnt und du es entfernt haben möchtest, reiche eine **DMCA-Takedown**-Anfrage bei GitHub ein. ([GitHub Docs][9])

Falls du möchtest, kann ich die DMCA-Mitteilung im exakten Format, das GitHub verlangt, entwerfen, sowie einen minimalen GitHub Actions Workflow, der deine Seite aus `blog-source` baut und nur die kompilierten Dateien zu `lzwjava.github.io` überträgt.

[1]: https://stackoverflow.com/questions/53052745/what-happens-to-the-forks-when-deleting-the-original-repository?utm_source=chatgpt.com "What happens to the forks when deleting the original repository?"
[2]: https://stackoverflow.com/questions/50280412/github-delete-a-fork-that-was-created-from-my-repo?utm_source=chatgpt.com "Github - Delete a fork that was created from my repo"
[3]: https://docs.github.com/articles/dmca-takedown-policy?utm_source=chatgpt.com "DMCA Takedown Policy"
[4]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "Creating a GitHub Pages site"
[5]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[6]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site?utm_source=chatgpt.com "Configuring a publishing source for your GitHub Pages site"
[7]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository?utm_source=chatgpt.com "Removing sensitive data from a repository"
[8]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository?utm_source=chatgpt.com "Managing the forking policy for your repository"
[9]: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice?utm_source=chatgpt.com "Guide to Submitting a DMCA Takedown Notice"