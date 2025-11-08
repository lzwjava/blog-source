---
audio: false
generated: false
image: false
lang: de
layout: post
title: LeanChat iOS
translated: true
type: post
---

Dies ist die README.md von dem GitHub-Projekt [https://github.com/lzwjava/leanchat-ios](https://github.com/lzwjava/leanchat-ios).

---

![Lizenz MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/v/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/p/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![Support](https://img.shields.io/badge/support-iOS%207%2B%20-blue.svg?style=flat)](https://www.apple.com/nl/ios/)

![leanchat](https://cloud.githubusercontent.com/assets/5022872/8431636/4eff0aca-1f6d-11e5-8728-f8f450dac380.gif)

## App Store
LeanChat ist im App Store verfügbar. Sie können [https://itunes.apple.com/gb/app/leanchat/id943324553](https://itunes.apple.com/gb/app/leanchat/id943324553) besuchen oder nach LeanChat im App Store suchen.

## Einführung
Dieses Beispielprojekt zeigt umfassend die Anwendung des Echtzeit-Kommunikationsmerkmals von LeanCloud. Es enthält jedoch viel UI-Code und andere Funktionalitäten, wodurch es sich nicht für schnelles Lernen eignet. Wenn Sie neu bei LeanMessage sind, empfehlen wir das [LeanMessage-Demo](https://github.com/leancloud/LeanMessage-Demo)-Projekt. Sobald Sie sich auskennen, können Sie zu [LeanCloud-Demos](https://github.com/leancloud/leancloud-demos) gehen, um Ihr Lieblings-IM-Skin für die Integration auszuwählen. Wenn Sie während der Integration auf schwierige Probleme stoßen, können Sie auf das LeanChat-Projekt zurückgreifen.

## Struktur des LeanChat-Projekts

* [leanchat-android](https://github.com/leancloud/leanchat-android): Android-Client
* [leanchat-ios](https://github.com/leancloud/leanchat-ios): iOS-Client
* [leanchat-webapp](https://github.com/leancloud/leanchat-webapp): Web-Client
* [leanchat-cloud-code](https://github.com/leancloud/leanchat-cloudcode): Serverseitig

## Wertvolles Feedback

Wenn Sie Fragen haben, können Sie gerne einen [issue](https://github.com/leancloud/leanchat-ios/issues) eröffnen und mitteilen, was Sie nicht verstehen, und wir werden Ihnen so schnell wie möglich helfen.

## Download
Bitte klicken Sie direkt auf `Download Zip` auf GitHub, wie im Bild unten gezeigt, um die neueste Version herunterzuladen. Wenn Sie `git clone` verwenden, könnte es sehr langsam sein, da es einen großen Commit-Verlauf enthält. In einem Test betrug der Unterschied 1,5 M: 40 M.

![qq20150618-2 2x](https://cloud.githubusercontent.com/assets/5022872/8223520/4c25415a-15ab-11e5-912d-b5dab916ce86.png)

## Ausführung
```bash
  // LeanChat (Komplexes Beispiel)
  cd LeanChat
  pod install --verbose  // Wenn Sie eine lokale AVOSCloud-Abhängigkeitsbibliothek haben, können Sie die Option --no-repo-update hinzufügen, um den Prozess zu beschleunigen
  open LeanChat.workspace

  // LeanChatExample (Einfaches Beispiel)
  cd LeanChatExample
  pod install --verbose --no-repo-update
  open LeanChatExample.xcworkspace

  // LeanChatSwift (Swift-Beispiel)
  cd LeanChatSwift
  pod install --verbose --no-repo-update
  open LeanChatSwift.xcworkspace

  // LeanChatLib (Bibliothek, die LeanCloud-Kommunikationskomponenten und UI kapselt)
  cd LeanChatLib
  pod install --verbose --no-repo-update
  open LeanChatLib.xcworkspace
```

Wenn Sie Probleme wie `definition of 'AVUser' must be imported from module 'LeanChatLib.CDChatListVC' before it is required` haben, können Sie die Option in der Produktmenü drücken und auf [Clean Build Folder](http://stackoverflow.com/questions/8087065/xcode-4-clean-vs-clean-build-folder) klicken, um alle Build-Dateien zu löschen, und dann neu kompilieren. Dieses Problem scheint ein Fehler bei der komplexen Kompilierung von Cocoapods zu sein. Sie können dieses [Gif](https://cloud.githubusercontent.com/assets/5022872/9230256/cf822fe4-4153-11e5-876d-ed819babad89.gif) für weitere Details sehen.

Bitte beachten Sie, dass standardmäßig Produktionszertifikate verwendet werden, sodass während der Entwicklung keine Push-Benachrichtigungen für Offline-Nachrichten vorhanden sind. Push-Benachrichtigungen sind jedoch in der Online-Version verfügbar, die Sie aus dem [App Store](https://itunes.apple.com/gb/app/leanchat/id943324553) herunterladen können. Weitere Informationen finden Sie auch in diesem [issue](https://github.com/leancloud/leanchat-ios/issues/40).

Hier können Sie drei Projekte sehen, wie unten beschrieben.

## Einführung in das Subprojekt

* LeanChatLib: Die Kernlogik- und UI-Bibliothek zum Chatten. Mit ihr können Sie schnell die Chat-Funktionalität integrieren, die Text-, Audio-, Bild- und Emoji-Nachrichten sowie Nachrichtbenachrichtigungen unterstützt. Es gibt auch eine entsprechende [Android-Version](https://github.com/leancloud/leanchat-android).
* LeanChatExample: Das einfachste Anwendungsbeispiel von LeanChatLib. Es zeigt, wie man mit minimalem Code LeanChatLib aufrufen kann, um einem Chat beizutreten, unabhängig davon, ob Sie LeanClouds Benutzersystem oder Ihr eigenes Benutzersystem verwenden.
* LeanChat-ios: Die gesamte LeanChat-Anwendung. Sie umfasst Funktionen wie Freundesverwaltung, Gruppenverwaltung, standortbasierte Nachrichten, Benutzer in der Nähe, persönliche Seiten, Anmeldung und Registrierung, alles basierend auf LeanClouds Speicher- und Kommunikationsfähigkeiten. Es handelt sich um eine komplexere Anwendung von LeanChatLib.

## Einführung in LeanChatLib

Es kapselt die Seite für kürzliche Gespräche und die Chat-Seite. Sowohl das LeanChat- als auch das LeanChatExample-Projekt hängen davon ab. Sie können es wie folgt installieren,

```
    pod 'LeanChatLib'
```

Die meiste Zeit integrieren Sie LeanChatLib, indem Sie den Quellcode in Ihr Projekt ziehen. In diesem Fall müssen Sie `AVOSCloud.framework` und `AVOSCloudIM.framework` zuerst installieren. Wenn Sie `pod install 'AVOSCloud'`, `pod install 'AVOSCloudIM'` nicht verwendet haben, um zu installieren, können Sie die erforderlichen Frameworks gemäß der LeanCloud [Quick Start Guide](https://leancloud.cn/docs/start.html) konfigurieren. Installieren Sie auch zwei andere abhängige Bibliotheken `JSBadgeView` und `DateTools`. Wenn Sie `pod install` für diesen Demo ausführen, wird ein Pods-Verzeichnis erstellt, in dem Sie diese beiden Pods finden können. Alternativ können Sie online suchen. Sie können es auch durch die [.podspec-Datei](https://github.com/leancloud/leanchat-ios/blob/master/LeanChatLib.podspec#L9) konfigurieren, die beschreibt, welche Quelldateien integriert werden müssen und welche System-Frameworks eingeführt werden müssen usw. Oder, bitte beziehen Sie sich auf diesen [ticket](https://ticket.leancloud.cn/tickets/7666).

## So fügen Sie in drei Schritten IM hinzu

1. Erstellen Sie eine Anwendung in LeanCloud.
2. Fügen Sie die LeanChatLib-Pod-Abhängigkeit hinzu oder ziehen Sie die LeanChatLib-Code-Dateien in Ihr Projekt für eine einfachere UI-Anpassung und Funktionsanpassung.
3. Fügen Sie den folgenden Code an den entsprechenden Stellen hinzu,

Nach dem Start der Anwendung initialisieren und konfigurieren Sie den IM-Benutzer,
```objc
    [AVOSCloud setApplicationId:@"YourAppId" clientKey:@"YourAppKey"];
    [CDChatManager manager].userDelegate = [[CDUserFactory alloc] init];
```

Konfigurieren Sie eine UserFactory, die dem CDUserDelegate-Protokoll entspricht.

```objc
#import "CDUserFactory.h"

#import <LeanChatLib/LeanChatLib.h>

@interface CDUserFactory ()<CDUserDelegate>

@end

@implementation CDUserFactory

#pragma mark - CDUserDelegate
-(void)cacheUserByIds:(NSSet *)userIds block:(AVIMArrayResultBlock)block{
    block(nil,nil); // vergessen Sie es nicht
}

-(id<CDUserModel>)getUserById:(NSString *)userId{
    CDUser* user=[[CDUser alloc] init];
    user.userId=userId;
    user.username=userId;
    user.avatarUrl=@"http://ac-x3o016bx.clouddn.com/86O7RAPx2BtTW5zgZTPGNwH9RZD5vNDtPm1YbIcu";
    return user;
}

@end
```

Hier ist CDUser das Benutzerobjekt innerhalb der Anwendung, und Sie können das CDUserModel-Protokoll in Ihrem Benutzerobjekt implementieren.

CDUserModel,
```objc
@protocol CDUserModel <NSObject>

@required

-(NSString*)userId;

-(NSString*)avatarUrl;

-(NSString*)username;

@end
```

Rufen Sie beim Anmelden,
```objc
        [[CDChatManager manager] openWithClientId:selfId callback: ^(BOOL succeeded, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
               //go Main Controller
            }
        }];
```

Um mit jemandem zu chatten,
```objc
        [[CDChatManager manager] fetchConvWithOtherId : otherId callback : ^(AVIMConversation *conversation, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
                LCEChatRoomVC *chatRoomVC = [[LCEChatRoomVC alloc] initWithConv:conversation];
                [weakSelf.navigationController pushViewController:chatRoomVC animated:YES];
            }
        }];
```

Für Gruppenchat,
```objc
        NSMutableArray *memberIds = [NSMutableArray array];
        [memberIds addObject:groupId1];
        [memberIds addObject:groupId2];
        [memberIds addObject:[CDChatManager manager].selfId];
        [[CDChatManager manager] fetchConvWithMembers:memberIds callback: ^(AVIMConversation *conversation, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
                LCEChatRoomVC *chatRoomVC = [[LCEChatRoomVC alloc] initWithConv:conversation];
                [weakSelf.navigationController pushViewController:chatRoomVC animated:YES];
            }
        }];
```

Beim Abmelden,
```objc
    [[CDChatManager manager] closeWithCallback: ^(BOOL succeeded, NSError *error) {

    }];
```

Dann können Sie wie im obigen Screenshot gezeigt chatten. Beachten Sie, dass wir derzeit nicht empfehlen, die pod-Methode zu verwenden, um LeanChatLib direkt zu importieren, da einige Schnittstellen und Funktionen von Ihnen angepasst werden müssen. Daher empfehlen wir, den LeanChatLib-Code in das Projekt zu kopieren, um die Anpassung zu erleichtern.

## LeanChatLib ChangeLog

0.2.6

SDK auf 3.1.4 aktualisieren, um iOS 9 zu unterstützen

0.2.5

Verwenden Sie cachePolicy in AVIMConversationQuery, um den Datenverkehr zu sparen und die Offline-Unterstützung zu verbessern
Fehler behoben, bei dem der Aufruf von fetchConvWithConvid, wenn die Konversation nicht existiert, möglicherweise zu einem Absturz führen kann

0.2.4

Tuzki Emoji hinzugefügt

0.2.3

Parameterprüfung für die fetchConvWithMembers-Schnittstelle hinzugefügt, Fehler bei der Konversationsliste behoben, wenn es sich um einen Einzelchat handelt, aber nur ein Mitglied hat

0.2.2

AVOSCloud-Bibliothek auf 3.1.2.8 aktualisiert

0.2.1

ChatListDelegate addiert configureCell: und prepareConversaion: Schnittstellen für eine komplexere Konversationsanpassung.

Für Bildnachrichten AVFile für das Zwischenspeichern von Bildern verwenden, sodass Ihre eigenen gesendeten Fotos nicht erneut heruntergeladen werden müssen.

0.2.0

Kommentare hinzufügen, Nachricht neu senden, fehlgeschlagene Nachrichten anzeigen, Soundeffekte und Vibration hinzufügen

0.1.3

Fehler behoben, bei dem die App möglicherweise abstürzt, wenn historische Nachrichten durch Herunterziehen schnell geladen werden

0.1.2

Verwenden Sie den Chat-Cache des SDK, entfernen Sie die FMDB-Abhängigkeit. Sie können historische Nachrichten auf dem Server und historische Chat-Dateien auch nach der Neuinstallation sehen. Die Klasse CDNotify entfernt.

0.1.1

Neu strukturiert

0.1.0

Erste Veröffentlichung

## Bereitstellungshinweise für LeanChat

Wenn Sie die gesamte LeanChat bereitstellen möchten, da die Anwendung eine Funktion zum Hinzufügen von Freunden hat, gehen Sie bitte zu Einstellungen -> Anwendungseinstellungen und aktivieren Sie die Option "Gegenseitiges Folgen", damit beide Parteien, wenn eine Partei zugestimmt hat, sich gegenseitig hinzufügen können.

![qq20150407-5](https://cloud.githubusercontent.com/assets/5022872/7016645/53f91bb8-dd1b-11e4-8ce0-72312c655094.png)

## Entwicklungsleitung

[Echtzeit-Nachrichten-Dienst Entwicklungsleitung](https://leancloud.cn/docs/realtime_v2.html)

[Weitere Informationen](https://github.com/leancloud/leanchat-android)

## Danksagungen

Vielen Dank für die großartige [MessageDisplayKit](https://github.com/xhzengAIB/MessageDisplayKit) Open-Source-Bibliothek von Xian-Hua Han.