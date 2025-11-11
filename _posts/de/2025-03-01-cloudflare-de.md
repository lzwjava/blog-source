---
audio: false
generated: true
lang: de
layout: post
title: Erste Schritte mit Cloudflare
translated: true
type: note
---

Cloudflare ist ein beliebter Dienst, der eine Reihe von Tools bietet, um die Leistung, Sicherheit und Zuverlässigkeit Ihrer Website zu verbessern. Egal, ob Sie einen kleinen Blog oder eine große E-Commerce-Website betreiben – Funktionen von Cloudflare wie DNS-Management, Content Delivery Network (CDN) und Sicherheitsschutz können einen erheblichen Unterschied machen. In diesem Blogbeitrag gehen wir drei wichtige Aufgaben durch: Konfiguration des DNS, Verwaltung von A-Records und das Sperren von IP-Regionen. Diese sind entscheidend, um das Beste aus Cloudflare herauszuholen, und sie sind einfacher einzurichten, als Sie vielleicht denken!

### **Warum Cloudflare verwenden?**

Bevor wir uns mit der Anleitung befassen, wollen wir kurz zusammenfassen, was Cloudflare so wertvoll macht:
-   **DNS-Management**: Cloudflare bietet schnelle und zuverlässige DNS-Dienste und stellt sicher, dass Ihre Website immer erreichbar ist.
-   **CDN**: Es beschleunigt Ihre Website, indem Inhalte näher an Ihre Besucher:innen herangeführt werden (Caching).
-   **Sicherheit**: Cloudflare bietet DDoS-Schutz, SSL/TLS-Verschlüsselung und Tools, um bösartigen Datenverkehr zu blockieren.
-   **Benutzerfreundlichkeit**: Noch besser: Cloudflare hat einen kostenlosen Plan, der perfekt für kleine Websites und Blogs ist.

Kommen wir nun zu den Details.

---

### **Schritt 1: DNS auf Cloudflare konfigurieren**

DNS (Domain Name System) ist so etwas wie das Telefonbuch des Internets – es übersetzt Ihren Domainnamen (z. B. `example.com`) in eine IP-Adresse, die Server verstehen können. Wenn Sie Cloudflare verwenden, verwalten Sie Ihre DNS-Einträge über deren Plattform, was zusätzliche Geschwindigkeit und Sicherheit bietet.

#### **So richten Sie Cloudflare DNS ein:**
1.  **Registrieren Sie sich bei Cloudflare**: Wenn Sie noch kein Konto haben, gehen Sie zur [Website von Cloudflare](https://www.cloudflare.com/) und registrieren Sie sich für ein kostenloses Konto.
2.  **Fügen Sie Ihre Domain hinzu**: Sobald Sie eingeloggt sind, klicken Sie auf „Add a Site“ (Website hinzufügen) und geben Sie Ihren Domainnamen ein (z. B. `example.com`). Cloudflare scannt Ihre vorhandenen DNS-Einträge.
3.  **Überprüfen Sie die DNS-Einträge**: Nach dem Scan zeigt Cloudflare eine Liste Ihrer aktuellen DNS-Einträge an. Sie können sie überprüfen, um sicherzustellen, dass alles korrekt aussieht.
4.  **Ändern Sie Ihre Nameserver**: Um Cloudflare DNS zu verwenden, müssen Sie die Nameserver Ihrer Domain bei Ihrem Domain-Registrar (z. B. GoDaddy, Namecheap) aktualisieren. Cloudflare stellt Ihnen zwei Nameserver zur Verfügung (z. B. `ns1.cloudflare.com` und `ns2.cloudflare.com`). Melden Sie sich im Dashboard Ihres Registrars an, suchen Sie die Nameserver-Einstellungen für Ihre Domain und ersetzen Sie die vorhandenen Nameserver durch die von Cloudflare.
5.  **Warten Sie auf die Verbreitung (Propagation)**: DNS-Änderungen können bis zu 24 Stunden dauern, bis sie vollständig verteilt sind, aber in der Regel geht es viel schneller. Sobald dies abgeschlossen ist, verwendet Ihre Domain Cloudflare DNS.

**Wichtiger Hinweis**: Stellen Sie sicher, dass Sie die Nameserver genau so kopieren, wie sie von Cloudflare bereitgestellt werden. Falsche Nameserver können dazu führen, dass Ihre Website offline geht.

---

### **Schritt 2: Verwalten von A-Records auf Cloudflare**

Ein A-Record ist eine Art von DNS-Eintrag, der Ihre Domain (oder Subdomain) einer IPv4-Adresse zuordnet. Er teilt dem Internet beispielsweise mit, dass `example.com` auf `192.0.2.1` verweisen soll. Cloudflare macht es einfach, A-Records hinzuzufügen, zu bearbeiten oder zu löschen.

#### **So verwalten Sie A-Records:**
1.  **Melden Sie sich bei Cloudflare an**: Gehen Sie zu Ihrem Cloudflare-Dashboard und wählen Sie die Domain aus, die Sie verwalten möchten.
2.  **Navigieren Sie zu DNS**: Klicken Sie auf den Tab „DNS“ im oberen Menü.
3.  **Einen A-Record hinzufügen**:
    -   Klicken Sie auf „Add Record“.
    -   Wählen Sie „A“ aus dem Dropdown-Menü für den Typ.
    -   Geben Sie den Namen ein (z. B. `www` für `www.example.com` oder lassen Sie ihn für die Root-Domain leer).
    -   Geben Sie die IPv4-Adresse ein, auf die verwiesen werden soll.
    -   Wählen Sie, ob der Datensatz über Cloudflare geproxyt werden soll (mehr dazu weiter unten).
    -   Legen Sie die TTL (Time to Live) fest. Für geproxyte Einträge beträgt der Standardwert 300 Sekunden.
    -   Klicken Sie auf „Save“.
4.  **Einen A-Record bearbeiten**: Suchen Sie den vorhandenen A-Record in der Liste, klicken Sie auf „Edit“, nehmen Sie Ihre Änderungen vor und klicken Sie auf „Save“.
5.  **Einen A-Record löschen**: Klicken Sie neben dem Eintrag auf „Edit“ und dann auf „Delete“. Bestätigen Sie die Löschung.

**Geproxyt vs. Nur DNS**:
-   **Geproxyt (Orange Wolke)**: Der Datenverkehr läuft über Cloudflare und ermöglicht so CDN-, Sicherheits- und Leistungsfunktionen.
-   **Nur DNS (Graue Wolke)**: Der Datenverkehr geht direkt zu Ihrem Server und umgeht die Schutzfunktionen von Cloudflare. Verwenden Sie dies für Einträge, die Cloudflare-Funktionen nicht benötigen (z. B. Mailserver).

**Kurzer Tipp**: Cloudflare unterstützt auch AAAA-Records für IPv6-Adressen. Der Vorgang zu deren Verwaltung ist derselbe wie für A-Records.

---

### **Schritt 3: Sperren von IP-Regionen auf Cloudflare**

Mit Cloudflare können Sie Datenverkehr aus bestimmten Ländern oder Regionen blockieren, was helfen kann, Spam, Bots und bösartige Angriffe zu reduzieren. Diese Funktion ist besonders nützlich, wenn Sie unerwünschten Datenverkehr aus bestimmten Gebieten feststellen.

#### **So sperren Sie IP-Regionen:**
1.  **Melden Sie sich bei Cloudflare an**: Gehen Sie zu Ihrem Cloudflare-Dashboard und wählen Sie Ihre Domain aus.
2.  **Navigieren Sie zu Sicherheit**: Klicken Sie auf den Tab „Security“ und wählen Sie dann „WAF“ (Web Application Firewall) aus.
3.  **Erstellen Sie eine Regel**:
    -   Klicken Sie auf „Create Firewall Rule“.
    -   Geben Sie Ihrer Regel einen Namen (z. B. „Bestimmte Länder blockieren“).
    -   Legen Sie die Regel so fest, dass sie Datenverkehr basierend auf dem Land der Besucher:in blockiert. Zum Beispiel:
        -   Feld: „Country“
        -   Operator: „is in“ (ist in)
        -   Wert: Wählen Sie die Länder aus, die Sie blockieren möchten.
    -   Wählen Sie die Aktion: „Block“.
    -   Klicken Sie auf „Deploy“.
4.  **Überwachen Sie blockierten Datenverkehr**: Sie können blockierte Anfragen im Tab „Security“ unter „Events“ einsehen.

**Wichtiger Hinweis**: Verwenden Sie diese Funktion mit Vorsicht. Das Sperren ganzer Regionen kann versehentlich legitime Nutzer:innen daran hindern, auf Ihre Website zuzugreifen. Es ist am besten, Ihren Datenverkehr zu überwachen und Regionen nur zu blockieren, wenn Sie sicher sind, dass es notwendig ist.

---

### **Zusätzliche Tipps und Best Practices**

-   **Verwenden Sie Cloudflares kostenlosen Plan**: Er ist perfekt für kleine Websites und enthält wesentliche Funktionen wie DNS-Management, CDN und grundlegende Sicherheit.
-   **Proxyen Sie Ihre Einträge**: Für optimale Leistung und Sicherheit sollten Sie Ihre A- und AAAA-Records whenever möglich über Cloudflare proxyen.
-   **Richten Sie SSL/TLS ein**: Cloudflare bietet kostenlose SSL-Zertifikate an, um den Datenverkehr zwischen Ihren Besucher:innen und Ihrer Website zu verschlüsseln. Sie können dies im Tab „SSL/TLS“ aktivieren.
-   **Erkunden Sie das Caching**: Das Caching von Cloudflare kann Ihre Website erheblich beschleunigen. Sehen Sie sich den Tab „Caching“ an, um es zu konfigurieren.
-   **Überwachen Sie Ihre Website**: Verwenden Sie die Analysen von Cloudflare, um Datenverkehr, Bedrohungen und Leistung im Auge zu behalten.

---

### **Fazit**

Cloudflare ist ein leistungsstarkes Tool, das die Geschwindigkeit, Sicherheit und Zuverlässigkeit Ihrer Website verbessern kann. Indem Sie die Schritte in dieser Anleitung befolgen, können Sie einfach DNS konfigurieren, A-Records verwalten und IP-Regionen sperren, um Ihre Website zu schützen. Denken Sie daran:
-   **DNS-Konfiguration**: Aktualisieren Sie Ihre Nameserver korrekt, um Ausfallzeiten zu vermeiden.
-   **A-Records**: Verwenden Sie sie, um Ihre Domain der IP-Adresse Ihres Servers zuzuordnen, und erwägen Sie, sie zu proxyen, um zusätzliche Vorteile zu nutzen.
-   **IP-Regionssperre**: Verwenden Sie diese Funktion sparsam, um das Blockieren legitimer Nutzer:innen zu vermeiden.

Cloudflare bietet viele weitere Funktionen wie SSL/TLS-Verschlüsselung, Caching und erweiterte Sicherheitstools. Sobald Sie mit den Grundlagen vertraut sind, erkunden Sie diese Optionen, um noch mehr aus der Plattform herauszuholen.