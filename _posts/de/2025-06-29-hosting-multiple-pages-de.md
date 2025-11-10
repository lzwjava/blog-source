---
audio: false
generated: true
lang: de
layout: post
title: Mehrere GitHub Pages mit Organisationen hosten
translated: true
type: note
---

Ja, das Erstellen einer GitHub-Organisation ist eine praktikable Methode, um zusätzliche GitHub Pages-Seiten mit eindeutigen `*.github.io`-Subdomains zu hosten, da jede Organisation ihre eigene `organization.github.io`-Seite haben kann, getrennt von Ihrer persönlichen `username.github.io`-Seite. So können Sie vorgehen und das sollten Sie wissen:

### Wichtige Punkte
- **Beschränkung persönlicher Accounts**: Jeder GitHub-Benutzeraccount kann nur eine User Site hosten, die unter `username.github.io` erreichbar ist und an ein Repository namens `username.github.io` gebunden ist. Wenn Sie dies bereits für Ihren persönlichen Account genutzt haben, können Sie kein weiteres `*.github.io`-Subdomain unter demselben Account erstellen.
- **Organisations-Seiten**: Jede GitHub-Organisation kann ebenfalls ihre eigene Organization Site hosten, die unter `organization.github.io` erreichbar ist, indem ein Repository namens `organization.github.io` erstellt wird. Dies ermöglicht es Ihnen, zusätzliche `*.github.io`-Subdomains durch das Einrichten mehrerer Organisationen zu erstellen.
- **Projekt-Seiten**: Sowohl Benutzer- als auch Organisationsaccounts können mehrere Project Sites hosten (z.B. `username.github.io/project` oder `organization.github.io/project`) aus anderen Repositories, aber dies sind Unterpfade, keine Subdomains. Wenn Sie ausdrücklich eindeutige Subdomains (z.B. `sub.example.github.io`) möchten, können Sie dies nicht direkt mit GitHub Pages ohne eine eigene Domain erreichen, da GitHub keine benutzerdefinierten Subdomains wie `sub.example.github.io` unter der `github.io`-Domain unterstützt.

### Schritte zum Erstellen einer GitHub-Organisation für zusätzliche `*.github.io`-Subdomains
1. **GitHub-Organisation erstellen**:
   - Gehen Sie zu GitHub und melden Sie sich mit Ihrem Account an.
   - Klicken Sie auf das "+"-Symbol in der oberen rechten Ecke und wählen Sie **New organization**.
   - Befolgen Sie die Anweisungen, um die Organisation einzurichten, und wählen Sie einen eindeutigen Namen (z.B. `myorg`). Dieser Name bestimmt das Subdomain (z.B. `myorg.github.io`).
   - Hinweis: Organisationen können kostenlos erstellt werden, aber einige Funktionen (wie private Repositories) erfordern möglicherweise einen kostenpflichtigen Plan, je nach Ihren Anforderungen. GitHub Pages für öffentliche Repositories ist mit GitHub Free verfügbar.

2. **Das GitHub Pages-Repository der Organisation erstellen**:
   - Erstellen Sie in der neuen Organisation ein Repository mit dem exakten Namen `myorg.github.io` (ersetzen Sie `myorg` durch den Namen Ihrer Organisation).
   - Dieses Repository hostet die Organization Site, die unter `https://myorg.github.io` erreichbar ist.

3. **GitHub Pages einrichten**:
   - Gehen Sie zur Registerkarte **Settings** des `myorg.github.io`-Repositorys.
   - Scrollen Sie zum Abschnitt **Pages**.
   - Wählen Sie unter **Source** den Branch aus, den Sie veröffentlichen möchten (z.B. `main` oder `gh-pages`), und speichern Sie.
   - Sobald konfiguriert, ist die Seite nach wenigen Minuten unter `https://myorg.github.io` live.

4. **Inhalt hinzufügen**:
   - Fügen Sie eine `index.html`-Datei hinzu oder verwenden Sie einen Static Site Generator wie Jekyll im Publishing-Branch des Repositorys.
   - Committen und pushen Sie Ihre Änderungen. Zum Beispiel:
     ```bash
     git clone https://github.com/myorg/myorg.github.io
     cd myorg.github.io
     echo "Hello World" > index.html
     git add --all
     git commit -m "Initial commit"
     git push origin main
     ```
   - Besuchen Sie `https://myorg.github.io`, um zu überprüfen, ob die Seite live ist.

5. **Für zusätzliche Subdomains wiederholen**:
   - Erstellen Sie zusätzliche Organisationen (z.B. `myorg2`, `myorg3`) und wiederholen Sie den Prozess, um `myorg2.github.io`, `myorg3.github.io` usw. zu erhalten.
   - Jede Organisation kann ein `*.github.io`-Subdomain haben, sodass Sie so viele Subdomains erstellen können, wie Sie Organisationen haben.

### Einschränkungen und Überlegungen
- **Benutzerdefinierte Subdomains auf `github.io`**: Sie können keine Subdomains wie `sub.myorg.github.io` direkt mit GitHub Pages erstellen. Die `github.io`-Domain wird von GitHub verwaltet, und nur `username.github.io` oder `organization.github.io` werden unterstützt. Um benutzerdefinierte Subdomains (z.B. `blog.example.com`) zu verwenden, müssen Sie eine eigene Domain besitzen und die DNS-Einstellungen (CNAME-Records) so konfigurieren, dass sie auf `myorg.github.io` zeigen.
- **Einzelnes Repository pro Subdomain**: Jedes `*.github.io`-Subdomain ist an ein einzelnes Repository (`username.github.io` oder `organization.github.io`) gebunden. Sie können nicht mehrere Subdomains von einem einzigen Repository aus bereitstellen, ohne eine eigene Domain und zusätzliche Hosting- oder Proxying-Dienste.
- **Management-Overhead**: Jede Organisation erfordert separates Management (z.B. Mitglieder, Berechtigungen, Abrechnung). Stellen Sie sicher, dass Sie mit der Verwaltung mehrerer Organisationen vertraut sind.
- **DNS und benutzerdefinierte Domains**: Wenn Sie eine eigene Domain (z.B. `example.com` oder `sub.example.com`) anstelle von `*.github.io` verwenden möchten, können Sie diese in den **Pages**-Einstellungen des Repositorys konfigurieren und einen CNAME-Record bei Ihrem DNS-Provider hinzufügen. Zeigen Sie zum Beispiel `sub.example.com` auf `myorg.github.io`. Vergewissern Sie sich, dass Sie die Domain verifizieren, um Übernahmerisiken zu vermeiden.
- **Private Repositories**: GitHub Pages für private Repositories erfordert GitHub Pro, Team oder Enterprise Pläne. Wenn Sie kostenlose Pläne verwenden, stellen Sie sicher, dass Ihr `myorg.github.io`-Repository öffentlich ist.

### Alternative für mehrere Subdomains
Wenn Ihr Ziel ist, mehrere Subdomains (z.B. `blog.example.com`, `shop.example.com`) unter einer einzelnen eigenen Domain zu haben, können Sie:
1. Eine eigene Domain (z.B. `example.com`) bei einem Registrar wie Namecheap oder GoDaddy kaufen.
2. Mehrere Repositories in Ihrer Organisation erstellen (z.B. `myorg/blog`, `myorg/shop`).
3. GitHub Pages für jedes Repository aktivieren und benutzerdefinierte Domains wie `blog.example.com` und `shop.example.com` in ihren jeweiligen **Pages**-Einstellungen festlegen.
4. CNAME-Records bei Ihrem DNS-Provider konfigurieren, um `blog.example.com` auf `myorg.github.io` und `shop.example.com` auf `myorg.github.io` zeigen zu lassen. Beachten Sie, dass alle Repositories ohne ihre eigene benutzerdefinierte Domain unter der benutzerdefinierten Domain der Organisation als Unterpfade erscheinen (z.B. `example.com/blog`).
5. Beachten Sie, dass das Bereitstellen mehrerer Subdomains von einem einzigen Repository aus von GitHub Pages nicht nativ unterstützt wird und möglicherweise externe Dienste wie ein CDN oder Reverse Proxy erfordert.

### Beispielszenario
- Sie haben `username.github.io` für Ihre persönliche Seite verwendet.
- Erstellen Sie eine Organisation namens `myorg` und ein Repository `myorg.github.io`, um `myorg.github.io` zu erhalten.
- Erstellen Sie eine weitere Organisation namens `myorg2` und ein Repository `myorg2.github.io`, um `myorg2.github.io` zu erhalten.
- Für benutzerdefinierte Subdomains besitzen Sie `example.com` und richten `blog.example.com` (zeigt auf `myorg.github.io`) und `shop.example.com` (zeigt auf `myorg2.github.io`) über CNAME-Records ein.

### Abschließende Hinweise
- Das Erstellen mehrerer Organisationen ist eine unkomplizierte Methode, um zusätzliche `*.github.io`-Subdomains zu erhalten, ohne eine eigene Domain zu benötigen.
- Wenn Sie echte Subdomains (z.B. `sub.myorg.github.io`) möchten, benötigen Sie eine eigene Domain und DNS-Konfiguration, da GitHub's `github.io` dies nicht nativ unterstützt.
- Verifizieren Sie immer benutzerdefinierte Domains, um Sicherheitsrisiken wie Domain-Übernahmen zu vermeiden.
- DNS-Änderungen können bis zu 24 Stunden dauern, um zu propagieren.

Wenn Sie weitere Fragen haben oder Hilfe bei spezifischen Konfigurationen benötigen, lassen Sie es mich wissen!