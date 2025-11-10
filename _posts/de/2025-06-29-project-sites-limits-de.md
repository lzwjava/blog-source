---
audio: false
generated: true
lang: de
layout: post
title: GitHub Pages Projekt-Website URL-Regeln
translated: true
type: note
---

Mit GitHub Pages können Sie zusätzlich zu Ihrer Benutzerwebsite (`username.github.io`) auch **Projekt-Websites** unter Ihrem persönlichen Konto erstellen. Allerdings ist das Format der URL für Projekt-Websites auf bestimmte Muster beschränkt, und nicht alle Subdomain- oder Unterpfad-Konfigurationen werden nativ unterstützt. Beantworten wir Ihre Frage, ob Sie `username.github.io/projekt1` oder `projekt1.username.github.io` für Projekt-Websites verwenden können.

### Wichtige Punkte
- **Benutzerwebsite**: Ein einzelnes Repository namens `username.github.io` stellt Inhalte unter `https://username.github.io` bereit.
- **Projekt-Websites**: Jedes andere Repository in Ihrem persönlichen Konto kann als Projekt-Website konfiguriert werden, die unter `https://username.github.io/repository-name` (ein Unterpfad, keine Subdomain) bereitgestellt wird.
- **Subdomain-Einschränkung**: GitHub Pages unterstützt nativ keine Subdomains wie `projekt1.username.github.io` unter der `github.io`-Domain. Die `github.io`-Domain wird von GitHub verwaltet, und nur `username.github.io` (für Benutzer) oder `organization.github.io` (für Organisationen) werden als Top-Level-Subdomains unterstützt. Benutzerdefinierte Subdomains wie `projekt1.username.github.io` erfordern eine benutzerdefinierte Domain und DNS-Konfiguration.

### Können Sie `username.github.io/projekt1` verwenden?
**Ja**, Sie können `username.github.io/projekt1` für eine Projekt-Website verwenden. Dies ist die Standardmethode, mit der GitHub Pages Projekt-Websites behandelt:
- Erstellen Sie ein Repository in Ihrem persönlichen Konto (z. B. `username/projekt1`).
- Aktivieren Sie GitHub Pages für dieses Repository:
  - Gehen Sie zum Tab **Einstellungen** des Repositorys.
  - Scrollen Sie zum Abschnitt **Pages**.
  - Wählen Sie unter **Quelle** den zu veröffentlichenden Branch aus (z. B. `main` oder `gh-pages`) und speichern Sie.
- Nach der Konfiguration ist die Website unter `https://username.github.io/projekt1` erreichbar.
- Sie können mehrere Projekt-Websites erstellen (z. B. `username.github.io/projekt2`, `username.github.io/projekt3`), indem Sie GitHub Pages für weitere Repositorys aktivieren (`username/projekt2`, `username/projekt3`, usw.).
- **Inhalt**: Fügen Sie eine `index.html` hinzu oder verwenden Sie einen Static Site Generator wie Jekyll im Publishing-Branch jedes Repositorys.

### Können Sie `projekt1.username.github.io` verwenden?
**Nein**, GitHub Pages unterstützt nativ keine Subdomains wie `projekt1.username.github.io` unter der `github.io`-Domain. Die `github.io`-Domain erlaubt nur:
- `username.github.io` für Benutzerwebsites.
- `organization.github.io` für Organisations-Websites.
- Unterpfade wie `username.github.io/repository-name` für Projekt-Websites.

Um eine URL wie `projekt1.username.github.io` zu erreichen, benötigen Sie:
1. **Eine benutzerdefinierte Domain**: Kaufen Sie eine Domain (z. B. `beispiel.com`) bei einem Registrar wie Namecheap oder GoDaddy.
2. **DNS-Konfiguration**: Richten Sie einen CNAME-Record ein, um eine Subdomain (z. B. `projekt1.beispiel.com`) auf Ihre GitHub Pages-Website (z. B. `username.github.io` oder `username.github.io/projekt1`) zu verweisen.
3. **GitHub Pages Einstellungen**:
   - Konfigurieren Sie in den **Pages**-Einstellungen des Repositorys die benutzerdefinierte Domain (z. B. `projekt1.beispiel.com`).
   - Aktivieren Sie optional "Enforce HTTPS" für mehr Sicherheit.
4. **Ergebnis**: Sie können `projekt1.beispiel.com` auf den Inhalt des `projekt1`-Repositorys abbilden, aber nicht `projekt1.username.github.io`, da GitHub die `github.io`-Domain kontrolliert und keine benutzerdefinierten Subdomains darunter zulässt.

### Beispielaufbau für `username.github.io/projekt1`
1. Erstellen Sie ein Repository namens `projekt1` unter Ihrem Konto (`username/projekt1`).
2. Fügen Sie Inhalte hinzu (z. B. `index.html`):
   ```bash
   git clone https://github.com/username/projekt1
   cd projekt1
   echo "Hallo von Projekt 1" > index.html
   git add --all
   git commit -m "Initialer Commit"
   git push origin main
   ```
3. Aktivieren Sie GitHub Pages:
   - Gehen Sie zu `username/projekt1` → **Einstellungen** → **Pages**.
   - Setzen Sie die Quelle auf `main` (oder einen anderen Branch) und speichern Sie.
4. Besuchen Sie `https://username.github.io/projekt1`, um die live Website zu sehen (kann einige Minuten dauern, bis sie verteilt ist).

### Beispiel für benutzerdefinierte Subdomain mit einer benutzerdefinierten Domain
Wenn Sie `projekt1.beispiel.com` möchten:
1. Besitzen Sie eine Domain (z. B. `beispiel.com`).
2. Fügen Sie in den Einstellungen Ihres DNS-Anbieters einen CNAME-Record hinzu:
   - Name: `projekt1`
   - Wert: `username.github.io`
3. Setzen Sie in den **Pages**-Einstellungen des `projekt1`-Repositorys die benutzerdefinierte Domain auf `projekt1.beispiel.com`.
4. Pushen Sie Inhalte zum `projekt1`-Repository, und sie werden unter `projekt1.beispiel.com` bereitgestellt.

### Einschränkungen
- **Nur Unterpfade für `github.io`**: Ohne eine benutzerdefinierte Domain werden Projekt-Websites immer als Unterpfade (`username.github.io/projekt1`) bereitgestellt, nicht als Subdomains (`projekt1.username.github.io`).
- **Eine Benutzerwebsite**: Ihr `username.github.io`-Repository ist für Ihre Benutzerwebsite reserviert. Projekt-Websites verwenden andere Repositorys und erscheinen als Unterpfade.
- **Benutzerdefinierte Subdomains erfordern benutzerdefinierte Domain**: Um `projekt1.etwas` zu erhalten, müssen Sie `etwas` besitzen (z. B. `beispiel.com`) und DNS konfigurieren.
- **Private Repositorys**: Projekt-Websites in privaten Repositorys erfordern GitHub Pro, Team oder Enterprise. Für kostenlose Konten müssen Repositorys öffentlich sein.

### Zusammenfassung
- **Verwenden Sie `username.github.io/projekt1`**: Ja, dies wird nativ unterstützt, indem Sie ein Repository (`username/projekt1`) erstellen und GitHub Pages aktivieren. Sie können auf diese Weise mehrere Projekt-Websites erstellen (z. B. `username.github.io/projekt2`, usw.).
- **Verwenden Sie `projekt1.username.github.io`**: Nein, dies wird unter `github.io` nicht unterstützt. Sie benötigen eine benutzerdefinierte Domain (z. B. `projekt1.beispiel.com`) und einen DNS-Setup, um einen ähnlichen Effekt zu erzielen.
- **Mehrere Subdomains**: Um mehrere `*.github.io`-Subdomains zu erhalten, erstellen Sie GitHub-Organisationen (wie zuvor besprochen) für `org1.github.io`, `org2.github.io`, usw., oder verwenden Sie eine benutzerdefinierte Domain für Subdomains wie `projekt1.beispiel.com`.

Wenn Sie Hilfe beim Einrichten einer bestimmten Projekt-Website, beim Konfigurieren einer benutzerdefinierten Domain oder beim Verwalten mehrerer Websites benötigen, lassen Sie es mich wissen!