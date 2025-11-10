---
audio: false
generated: true
lang: de
layout: post
title: iPhone Hotspot-Verhalten bei ausgeschaltetem Bildschirm
translated: true
type: note
---

### Verhalten des iPhone-Personal Hotspots bei ausgeschaltetem Bildschirm

Basierend auf zuverlässigen Quellen finden Sie hier eine klare Erklärung, wie ein iPhone mit dem Personal Hotspot (Teilen von Mobilfunkdaten) umgeht, wenn der Bildschirm ausgeschaltet ist (d.h., das Gerät sich sperrt oder in den Ruhemodus geht). Ich werde es Schritt für Schritt aufschlüsseln und Ihre Fragen beantworten, ob er sofort stoppt, nach einiger Zeit, bis zum Ausschalten weiterläuft usw. Beachten Sie, dass dies für Standard-iOS-Versionen gilt (wie iOS 18 Stand 2025); das Verhalten kann in Beta-Versionen oder mit bestimmten Carrier-Einstellungen leicht variieren.

#### 1. **Stoppt der Personal Hotspot die Freigabe, wenn der Bildschirm ausgeht?**
   - Nein, er stoppt nicht sofort, nur weil der Bildschirm ausgeht oder sich das iPhone sperrt.
   - Der Hotspot funktioniert im Hintergrund weiter und teilt Ihre Mobilfunkdaten via Wi-Fi, Bluetooth oder USB, selbst wenn der Bildschirm aus ist. Dies ist dafür ausgelegt, eine ununterbrochene Nutzung für verbundene Geräte (z.B. Laptops, Tablets) zu ermöglichen, ohne dass der Bildschirm des iPhones aktiv bleiben muss.[1][2]
   - Es gibt jedoch Bedingungen, die indirekt dazu führen können, dass er sich ausschaltet oder die Verbindung trennt (siehe unten).

#### 2. **Wann stoppt er die Freigabe (Automatisches Ausschalten oder Trennen)?**
   - **Wenn keine Geräte verbunden sind**: Der Personal Hotspot schaltet sich automatisch nach etwa 90 Sekunden ohne Verbindungen ab. Dies ist eine Akku-sparende Funktion, um unnötigen Daten- und Stromverbrauch zu verhindern, wenn nichts den Hotspot nutzt.[3][4]
   - **Wenn Geräte verbunden, aber inaktiv sind**: Verbundene Geräte (insbesondere Drittanbieter- oder Nicht-Apple-Geräte) können die Verbindung trennen, wenn sie innerhalb von 90 Sekunden keinen IP-Datenverkehr (Datenaktivität) senden. Der Hotspot selbst könnte sich dann ausschalten, wenn alle Verbindungen aufgrund von Inaktivität abbrechen.[5]
   - **Energiesparmodus oder Akkusparmodus**: Wenn sich Ihr iPhone im Energiesparmodus befindet (manuell aktiviert oder bei niedrigem Akkustand), kann dies Hintergrundprozesse einschränken und dazu führen, dass sich der Hotspot häufiger ausschaltet oder die Verbindung trennt.[6]
   - **Andere Auslöser**: Es könnte zu Verbindungstrennungen aufgrund von Netzwerkproblemen, Carrier-Beschränkungen, Interferenzen (z.B. Entfernung zu verbundenen Geräten oder elektromagnetische Quellen) kommen, oder wenn Sie Ihr Datenvolumen überschritten haben. Er schaltet sich nicht allein wegen des ausgeschalteten Bildschirms ab, aber längere Inaktivität oder ein niedriger Akkustand können dazu führen.

#### 3. **Wie lange kann die Freigabe andauern?**
   - **Bei aktiven Verbindungen**: Er kann theoretisch unbegrenzt weiterlaufen, bis Sie ihn manuell ausschalten, der Akku des iPhones leer ist oder Sie das Gerät vollständig ausschalten. Es gibt keine eingebaute Zeitbegrenzung, solange Geräte verbunden sind und gelegentlich Datenverkehr senden.[2]
   - **Dauer des ausgeschalteten Bildschirms**: Selbst wenn der Bildschirm stundenlang (oder tagelang) aus bleibt, bleibt der Hotspot aktiv, sofern die Bedingungen erfüllt sind. Wenn beispielsweise die automatische Sperre auf eine kurze Zeit (z.B. 30 Sekunden) eingestellt ist, geht der Bildschirm schnell aus, aber die Freigabe läuft weiter.[7]
   - **Bis zum Ausschalten**: Ja, er teilt weiter, bis das iPhone vollständig ausgeschaltet ist (Seitentaste gedrückt halten und Herunterfahren bestätigen) oder neu startet.

#### 4. **Tipps, um automatisches Ausschalten oder Verbindungstrennungen zu verhindern**
   - **Automatische Sperre auf "Nie" stellen**: Gehen Sie zu Einstellungen > Display & Helligkeit > Automatische Sperre > Nie. Dies hält das iPhone länger "wach" und hilft, den Hotspot auch in Phasen geringer Aktivität aktiv zu halten (verbraucht jedoch schneller Akku – wenn möglich, anschließen).[2][7]
   - **Energiesparmodus deaktivieren**: Einstellungen > Batterie > Energiesparmodus ausschalten.[6]
   - **Daten sparen-Modus deaktivieren**: Einstellungen > Mobilfunk > Mobildaten-Optionen > Daten sparen-Modus ausschalten.[3]
   - **Siri-Trick nutzen**: Sperren Sie Ihren Bildschirm und bitten Sie Siri dann, "Personal Hotspot einzuschalten". Dies kann ihn dauerhaft aktiv halten, bis Sie ihn ausschalten, und umgeht einige automatische Abschaltungen.[8]
   - **Aktivität sicherstellen**: Führen Sie auf verbundenen Geräten eine Hintergrundaufgabe aus (wie das Pingen einer Website), um etwa jede Minute Datenverkehr zu senden und das 90-Sekunden-Inaktivitäts-Timeout zu verhindern.
   - **Netzwerkeinstellungen zurücksetzen**: Wenn die Probleme bestehen bleiben, gehen Sie zu Einstellungen > Allgemein > iPhone übertragen oder zurücksetzen > Zurücksetzen > Netzwerkeinstellungen zurücksetzen. Dies behebt Fehler, löscht jedoch gespeicherte Wi-Fi-Passwörter.[9]
   - **iOS und Carrier-Einstellungen aktualisieren**: Prüfen Sie auf Updates in Einstellungen > Allgemein > Softwareupdate und Einstellungen > Allgemein > Info (für Carrier-Updates).[3]

Wenn Sie häufige Verbindungstrennungen erleben, die über diese Gründe hinausgehen, könnte es sich um einen Fehler handeln – versuchen Sie, Ihr iPhone neu zu starten, oder wenden Sie sich an den Apple Support/Ihren Carrier. Das Verhalten kann je nach iPhone-Modell (z.B. iPhone-16-Serie) oder iOS-Version leicht variieren.

#### Referenzen (Markdown-Zitate)
[1]: Apple Discussions (web:0)  
[2]: Ask Different (web:2, web:13, web:25)  
[3]: Alphr Article (web:23, web:31)  
[4]: Quora (web:15, web:29)  
[5]: Apple Training Snippet (web:26)  
[6]: Wondershare (web:6, web:24) and Alphr (web:31)  
[7]: Reddit (web:1, web:11)  
[8]: Reddit (web:1)  
[9]: Apple Support (web:4) and Alphr (web:31)