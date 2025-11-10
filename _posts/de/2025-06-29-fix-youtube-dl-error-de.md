---
audio: false
generated: true
lang: de
layout: post
title: Behebung des YouTube-dl Bot-Verifizierungsfehlers
translated: true
type: note
---

Der Fehler "Sign in to confirm you’re not a bot" von youtube-dl tritt typischerweise auf, weil YouTube die Anfrage blockiert, oft aufgrund von IP-Beschränkungen, VPN-Nutzung oder fehlender Authentifizierung. Hier sind Schritte zur Lösung des Problems, beginnend mit den einfachsten Lösungen:

1. **youtube-dl aktualisieren**:
   - Der Fehler könnte von einer veralteten Version von youtube-dl stammen, da YouTube seine Systeme häufig aktualisiert. Aktualisieren Sie auf die neueste Version, indem Sie ausführen:
     ```bash
     sudo youtube-dl -U
     ```
     oder, falls Sie es via pip installiert haben:
     ```bash
     pip install --upgrade youtube-dl
     ```
   - Versuchen Sie nach der Aktualisierung den Befehl erneut:
     ```bash
     youtube-dl https://www.youtube.com/watch?v=st3mUEub99E
     ```

2. **Zu yt-dlp wechseln (Empfohlene Alternative)**:
   - youtube-dl wird nicht mehr aktiv gepflegt, und yt-dlp, ein Fork von youtube-dl, ist zuverlässiger für aktuelle YouTube-Änderungen. Installieren Sie yt-dlp:
     ```bash
     sudo pip install yt-dlp
     ```
     Verwenden Sie es dann:
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - yt-dlp handelt Authentifizierung und IP-Beschränkungen besser.

3. **VPN deaktivieren oder Server wechseln**:
   - Wenn Sie ein VPN verwenden, könnte YouTube Ihre IP als verdächtig einstufen. Versuchen Sie, Ihr VPN zu deaktivieren oder zu einem anderen Server zu wechseln:
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - Benutzer haben Erfolg gemeldet, nachdem sie sich von VPNs getrennt oder Server gewechselt haben.

4. **Cookies zur Authentifizierung verwenden**:
   - YouTube erfordert möglicherweise eine Authentifizierung, um die Bot-Überprüfung zu umgehen. Exportieren Sie Cookies aus einem Browser, in dem Sie bei YouTube angemeldet sind:
     - Installieren Sie eine Browser-Erweiterung wie "Export Cookies" für Firefox oder Chrome.
     - Melden Sie sich bei YouTube an, exportieren Sie die Cookies in eine `cookies.txt`-Datei und verwenden Sie sie mit:
       ```bash
       youtube-dl --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
       oder für yt-dlp:
       ```bash
       yt-dlp --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - Alternativ können Sie `--cookies-from-browser firefox` verwenden (oder `firefox` durch `chrome`, `edge` etc. ersetzen), um Cookies automatisch zu extrahieren:
       ```bash
       yt-dlp --cookies-from-browser firefox https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - Hinweis: Vermeiden Sie die Verwendung Ihres primären Google-Kontos, um eine mögliche Kennzeichnung zu verhindern. Verwenden Sie nach Möglichkeit ein Wegwerf-Konto.

5. **Einen Proxy verwenden**:
   - Wenn das Problem weiterhin besteht, könnte Ihre IP blockiert sein (z.B. bei Verwendung einer Data Center IP). Versuchen Sie, einen Residential Proxy zu verwenden, um Ihre IP zu verschleiern:
     ```bash
     youtube-dl --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
     oder für yt-dlp:
     ```bash
     yt-dlp --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - Residential Proxys werden seltener gekennzeichnet als Data Center Proxys.

6. **Cache leeren oder ein anderes Netzwerk versuchen**:
   - Wenn Sie kürzlich Logs oder Temp-Dateien gelöscht haben, stellen Sie sicher, dass youtube-dl/yt-dlp nicht auf einen beschädigten Cache angewiesen ist. Leeren Sie den Cache:
     ```bash
     rm -rf ~/.cache/youtube-dl
     rm -rf ~/.cache/yt-dlp
     ```
   - Wechseln Sie zu einem anderen Netzwerk (z.B. Mobile Hotspot), um zu testen, ob das Problem IP-bezogen ist.

7. **Ausführliche Ausgabe für die Fehlerdiagnose**:
   - Wenn die obigen Schritte fehlschlagen, führen Sie den Befehl mit ausführlicher Ausgabe aus, um weiter zu diagnostizieren:
     ```bash
     youtube-dl -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
     oder für yt-dlp:
     ```bash
     yt-dlp -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - Teilen Sie die Ausgabe in einem relevanten Forum (z.B. GitHub Issues für yt-dlp) mit, um Hilfe von der Community zu erhalten.

**Hinweise**:
- YouTubes Bot-Erkennung ist strenger geworden und zielt oft auf Data Center IPs oder nicht authentifizierte Anfragen ab.
- Die Verwendung von Cookies birgt ein geringes Risiko der Kontokennzeichnung, verwenden Sie daher ein Zweitkonto.
- Wenn das Video privat oder eingeschränkt ist, stellen Sie sicher, dass Ihr Konto Zugriff hat, bevor Sie Cookies verwenden.
- Wenn nichts davon funktioniert, ziehen Sie in Betracht, alternative Frontends wie Invidious oder NewPipe zu verwenden, obwohl diese Einschränkungen haben können.

Versuchen Sie diese Schritte in der angegebenen Reihenfolge, beginnend mit der Aktualisierung oder dem Wechsel zu yt-dlp, da dies die wahrscheinlichste Lösung ist. Wenn das Problem weiterhin besteht, teilen Sie mir die ausführliche Ausgabe oder spezifische Details mit (z.B. VPN-Nutzung, Betriebssystem).