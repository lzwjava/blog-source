---
audio: false
generated: false
lang: de
layout: post
title: So greift man auf Google zu
translated: true
---

Dieser Beitrag wurde ursprünglich auf Chinesisch verfasst.

---

Diese Lektion behandelt Folgendes:

1. Zugriff auf die offizielle Website eines VPN-Dienstes.
2. Verwendung eines VPN unter Windows.
3. Einführung in die Clash-Software.
4. Versuch, Google, Twitter, YouTube und TikTok zu öffnen.

Beginnen wir. Hier ist eine schriftliche Beschreibung, wie ich Xiao Wang beigebracht habe, auf Google zuzugreifen.

Wir verwenden eine Plattform namens "Summoner". Die Website lautet `https://zhshi.gitlab.io`.

<img src="/assets/images/google/zhs.png" alt="zhs" />

Sie ist jedoch möglicherweise nicht zugänglich, da sie von der Great Firewall blockiert wird.

![zhs_user](/assets/images/google/zhs_user.png)

So sieht es aus, wenn Sie sich anmelden.

Es gibt eigentlich zwei Möglichkeiten, die Firewall zu umgehen. Eine ist, unseren eigenen Server in Übersee zu kaufen. Die andere ist die Verwendung einer VPN-Plattform, die viele Serveradressen in Übersee bereitstellt.

"Firewall umgehen" bedeutet, zuerst von innerhalb des Landes auf einen Server in Übersee zuzugreifen. Dieser Server in Übersee kann dann auf Websites zugreifen, die blockiert sind.

Eine solche Plattform heißt "Summoner". Aber wenn die offizielle Website nicht zugänglich ist, wie erhalten wir dann die von ihr bereitgestellten Serveradressen in Übersee? Xiao Wang verwendet zum ersten Mal ein VPN, und ich unterrichte ihn aus der Ferne. Wie soll ich ihn unterrichten?

An diesem Punkt dachte ich daran, Xiao Wangs Windows-Computer so zu konfigurieren, dass er die Firewall umgeht. Ich werde Xiao Wang eine Adresse geben. Dann kann Xiao Wang die "Summoner"-Website öffnen, ein Konto registrieren und die Serveradressen in Übersee unter seinem eigenen Konto verwenden.

![clash_win](/assets/images/google/clash_win.png)

![win_version](/assets/images/google/win_version.png)

Überprüfen Sie als Nächstes, ob Ihr Computer 64-Bit oder 32-Bit ist. Wenn es 64-Bit ist, laden Sie `Clash.for.Windows.Setup.0.14.8.exe` herunter. Wenn es 32-Bit ist, laden Sie `Clash.for.Windows.Setup.0.14.8.ia32.exe` herunter.

Xiao Wangs Computer ist 64-Bit. Der Download ist bei ihm jedoch sehr langsam. Daher habe ich ihn auf meinem Computer heruntergeladen und ihm per QQ-E-Mail geschickt.

Er hat es von der QQ-E-Mail heruntergeladen, installiert und geöffnet.

![clash_win_exe](/assets/images/google/clash_win_exe.png)

Ich habe ihm zuerst meine Summoner-Konfigurationsadresse gegeben. Diese Konfigurationsadresse lädt eine Datei herunter, die viele VPN-Serveradressen enthält. Fügen Sie unter `Profile` die Adresse ein und klicken Sie auf `Download`.

![zhs_url](/assets/images/google/zhs_url.png)

Sehen Sie, es ist heruntergeladen. Beachten Sie die zweite Konfiguration oben. Davor befindet sich ein grünes Häkchen, das anzeigt, dass wir diese Konfiguration verwenden.

![zhs_proxy](/assets/images/google/zhs_proxy.png)

Öffnen Sie als Nächstes die Registerkarte `Proxies`. Sie werden hier einige Dinge sehen. Dies sind einige der Konfigurationen von `Clash`. Einfach ausgedrückt bedeutet dies, dass inländische Websites das VPN nicht verwenden, ausländische Websites jedoch schon.

Beachten Sie, dass der aktuelle Wert von `Proxy` `DIRECT` ist, was bedeutet, dass es sich um eine direkte Verbindung handelt. Wir ändern es in einen Knoten.

![zhs_node](/assets/images/google/zhs_node.png)

Wir haben den Knoten `US Rose` ausgewählt.

![clash_system](/assets/images/google/clash_system.png)

Schalten Sie als Nächstes die Einstellung `System Proxy` um, um sie zu aktivieren. Dies bedeutet, die `Clash`-Software als Proxy-Ebene des Systems einzurichten. Dann wird der Datenverkehr des Systems zuerst an die `Clash`-Software gehen und dann auf das externe Netzwerk zugreifen.

<img src="/assets/images/google/google.png" alt="google" style="zoom:40%;" />

Xiao Wang öffnete Google. Als Nächstes probierte er TikTok, YouTube und Twitter aus.

Okay, also verwendet Xiao Wang mein Summoner-Konto. Wie registriert er sich? Er muss die offizielle Summoner-Website öffnen.

<img src="/assets/images/google/zhs_register.png" alt="zhs_register" style="zoom:50%;" />

Nach der Registrierung stellte er fest, dass das Aufladen zum Kauf von Diensten einige Schritte erfordert. Hier ist ein Screenshot meines Kontos.

![zeng](/assets/images/google/zeng.png)

Es heißt, dass es mit Telegram verknüpft werden muss.

<img src="/assets/images/google/zhs_telegram.png" alt="zhs_telegram" style="zoom:50%;" />

Xiao Wang ging auf die Telegram-Website und lud die Telegram Windows-Desktopversion herunter.

![telegram](/assets/images/google/telegram.png)

Achten Sie nach dem Herunterladen und Installieren auf den obigen Text.

> Nach der Installation von Telegram und der Registrierung klicken Sie, um mit `小兔` oder `城主` zu chatten, kopieren Sie den folgenden QR-Code und senden Sie ihn an sie, oder `klicken Sie hier, um den Code automatisch zu kopieren und an den Bot zu senden, um ihn zu binden`.

Wenn Sie auf `小兔` klicken, springt die Software automatisch zu `Telegram` und öffnet ein Chatfenster mit `小兔`. Senden Sie ihnen dann den Code.

![telegram_username](/assets/images/google/telegram_username.png)

Xiao Wangs `Telegram`-Konto ist jedoch neu registriert und hat keinen `Benutzernamen`. Es ist, als würde man WeChat verwenden, ohne eine WeChat-ID einzurichten.

Suchen Sie das Telegram-Menü und legen Sie es fest. Senden Sie dann den Code erneut zum Binden.

<img src="/assets/images/google/zhs_set.png" alt="zhs_set" style="zoom:50%;" />

Als Nächstes können Sie spenden, um es zu unterstützen. Sie können mit einer Aufladung von 30 Yuan für zwei Monate beginnen.

Gehen Sie zurück zur Summoner-Homepage. Suchen Sie hier nach der Schaltfläche "Klicken zum Kopieren", erhalten Sie die Adresse und laden Sie dann die Konfiguration in der `Clash`-Software herunter.

Dann kann Xiao Wang die Adresse, die ich ihm gegeben habe, löschen. Xiao Wang hat jetzt sein eigenes Summoner-Konto.
