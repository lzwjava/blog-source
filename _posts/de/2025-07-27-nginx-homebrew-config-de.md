---
audio: false
generated: true
image: false
lang: de
layout: post
title: Nginx-Konfiguration unter macOS Homebrew
translated: true
type: note
---

Für Nginx, das über Homebrew auf macOS installiert wurde (wie durch den Binärpfad `/opt/homebrew/bin/nginx` angegeben), befindet sich die Hauptkonfigurationsdatei typischerweise unter:

```
/opt/homebrew/etc/nginx/nginx.conf
```

Dieses Verzeichnis enthält auch andere zugehörige Dateien, wie Server-Blöcke in einem `servers/` Unterverzeichnis (z.B. `/opt/homebrew/etc/nginx/servers/`).

Um den exakten Pfad der Konfigurationsdatei zu bestätigen, die von Ihrer Nginx-Instanz verwendet wird, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```
nginx -t
```

Dies testet die Konfiguration und gibt den Pfad zur verwendeten `nginx.conf`-Datei aus. Alternativ können Sie `nginx -V` verwenden, um Compile-Time-Details, inklusive des Konfigurationspfad-Präfixes, einzusehen.

Falls Sie sich auf einem älteren Intel-basierten Mac befinden, wo Homebrew unter `/usr/local` installiert, wäre der Pfad `/usr/local/etc/nginx/nginx.conf`. Ihr angegebener Binärpfad bestätigt jedoch den Standort `/opt/homebrew`.

**Referenzen**  
[Locate the nginx.conf file my nginx is actually using - Stack Overflow](https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using)  
[Installing nginx in macOS using homebrew | by Ram - Medium](https://medium.com/@rprprasath05/installing-nginx-in-macos-ventura-using-homebrew-12b87a900a03)  
[Simple Configuration of NGINX on Mac - DEV Community](https://dev.to/arjavdave/simple-configuration-of-nginx-on-mac-3cg3)