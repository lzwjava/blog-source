---
audio: false
generated: false
lang: fr
layout: post
title: 'LeanChat iOS


  ChatMince iOS'
translated: true
---

Voici le README.md du projet github [https://github.com/lzwjava/leanchat-ios](https://github.com/lzwjava/leanchat-ios).

---

![Licence MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/v/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/p/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![Support](https://img.shields.io/badge/support-iOS%207%2B%20-blue.svg?style=flat)](https://www.apple.com/nl/ios/)

![leanchat](https://cloud.githubusercontent.com/assets/5022872/8431636/4eff0aca-1f6d-11e5-8728-f8f450dac380.gif)

## App Store
LeanChat est disponible sur l'App Store. Vous pouvez visiter [https://itunes.apple.com/gb/app/leanchat/id943324553](https://itunes.apple.com/gb/app/leanchat/id943324553) ou rechercher LeanChat sur l'App Store.

## Introduction
Ce projet d'exemple montre de manière exhaustive l'application de la fonction de communication en temps réel de LeanCloud. Cependant, il contient beaucoup de code UI et d'autres fonctionnalités, ce qui le rend peu adapté à un apprentissage rapide. Si vous êtes nouveau sur LeanMessage, nous recommandons le projet [LeanMessage-Demo](https://github.com/leancloud/LeanMessage-Demo). Une fois que vous êtes familiarisé, vous pouvez aller sur [LeanCloud-Demos](https://github.com/leancloud/leancloud-demos) pour sélectionner votre peau IM préférée pour l'intégration. Pendant l'intégration, si vous rencontrez des problèmes difficiles, vous pouvez vous référer au projet LeanChat.

## Structure du projet LeanChat

* [leanchat-android](https://github.com/leancloud/leanchat-android) : client Android
* [leanchat-ios](https://github.com/leancloud/leanchat-ios) : client iOS
* [leanchat-webapp](https://github.com/leancloud/leanchat-webapp) : client Web
* [leanchat-cloud-code](https://github.com/leancloud/leanchat-cloudcode) : côté serveur

## Retours précieux

Si vous avez des questions, n'hésitez pas à créer un [issue](https://github.com/leancloud/leanchat-ios/issues), en indiquant ce que vous ne comprenez pas, et nous vous fournirons de l'aide dès que possible.

## Téléchargement
Veuillez cliquer directement sur `Download Zip` sur Github comme indiqué sur l'image ci-dessous pour télécharger uniquement la dernière version. Si vous utilisez `git clone`, cela peut être très lent car il inclut un grand historique de commits. Lors d'un test, la différence était de 1,5M:40M.

![qq20150618-2 2x](https://cloud.githubusercontent.com/assets/5022872/8223520/4c25415a-15ab-11e5-912d-b5dab916ce86.png)

## Exécution
```bash
  // LeanChat (Exemple complexe)
  cd LeanChat
  pod install --verbose  // Si vous avez la bibliothèque de dépendance AVOSCloud localement, vous pouvez ajouter l'option --no-repo-update pour accélérer le processus
  open LeanChat.workspace

  // LeanChatExample (Exemple simple)
  cd LeanChatExample
  pod install --verbose --no-repo-update
  open LeanChatExample.xcworkspace

  // LeanChatSwift (Exemple Swift)
  cd LeanChatSwift
  pod install --verbose --no-repo-update
  open LeanChatSwift.xcworkspace

  // LeanChatLib (Bibliothèque encapsulant les composants de communication LeanCloud et l'UI)
  cd LeanChatLib
  pod install --verbose --no-repo-update
  open LeanChatLib.xcworkspace
```

Si vous rencontrez des problèmes comme `definition of 'AVUser' must be imported from module 'LeanChatLib.CDChatListVC' before it is required`, vous pouvez maintenir la touche Option dans le menu Produit et cliquer sur [Clean Build Folder](http://stackoverflow.com/questions/8087065/xcode-4-clean-vs-clean-build-folder) pour effacer tous les fichiers de Build, puis recompiler. Ce problème semble être un bug lorsque Cocoapods effectue une compilation complexe. Vous pouvez voir ce [Gif](https://cloud.githubusercontent.com/assets/5022872/9230256/cf822fe4-4153-11e5-876d-ed819babad89.gif) pour plus de détails.

Veuillez noter que, en raison de l'utilisation par défaut des certificats de production, il n'y a pas de notifications push pour les messages hors ligne pendant le développement. Cependant, les notifications push sont disponibles dans la version en ligne, que vous pouvez télécharger depuis l'[App Store](https://itunes.apple.com/gb/app/leanchat/id943324553). Pour plus de détails, vous pouvez également vous référer à ce [issue](https://github.com/leancloud/leanchat-ios/issues/40).

Vous pouvez voir trois projets, comme décrit ci-dessous.

## Introduction aux sous-projets
* LeanChatLib : la bibliothèque de logique et d'interface utilisateur principale pour la discussion. Avec elle, vous pouvez rapidement intégrer la fonctionnalité de discussion, prenant en charge les messages texte, audio, image et emoji, ainsi que les notifications de messages. Il existe également une version [Android correspondante](https://github.com/leancloud/leanchat-android).
* LeanChatExample : l'exemple d'utilisation le plus simple de LeanChatLib. Il montre comment utiliser un minimum de code pour appeler LeanChatLib et rejoindre une discussion, que vous utilisiez le système d'utilisateurs de LeanCloud ou votre propre système d'utilisateurs.
* LeanChat-ios : l'application LeanChat complète. Elle inclut des fonctionnalités telles que la gestion des amis, la gestion des groupes, la messagerie basée sur la localisation, les utilisateurs à proximité, les pages personnelles, la connexion et l'inscription, toutes basées sur les capacités de stockage et de communication de LeanCloud. C'est une application plus complexe de LeanChatLib.

## Introduction à LeanChatLib

Il encapsule la page des conversations récentes et la page de discussion. Les projets LeanChat et LeanChatExample en dépendent. Vous pouvez l'installer comme suit,

```
    pod 'LeanChatLib'
```

La plupart du temps, vous intégrerez LeanChatLib en faisant glisser le code source dans votre projet. Dans ce cas, vous devez d'abord installer `AVOSCloud.framework` et `AVOSCloudIM.framework`. Si vous n'avez pas utilisé `pod install 'AVOSCloud'`, `pod install 'AVOSCloudIM'` pour installer, vous pouvez configurer les Frameworks nécessaires selon le [Guide de démarrage rapide de LeanCloud](https://leancloud.cn/docs/start.html). Installez également deux autres bibliothèques dépendantes `JSBadgeView` et `DateTools`. Lors de l'exécution de `pod install` pour cette Démonstration, un répertoire Pods sera généré, à partir duquel vous pouvez trouver ces deux Pods. Sinon, vous pouvez rechercher en ligne. Vous pouvez également le configurer via le fichier [.podspec](https://github.com/leancloud/leanchat-ios/blob/master/LeanChatLib.podspec#L9), qui décrit quels fichiers sources doivent être intégrés et quels frameworks système doivent être introduits, etc. Ou, veuillez vous référer à ce [ticket](https://ticket.leancloud.cn/tickets/7666).

## Comment ajouter IM en trois étapes
1. Créez une application dans LeanCloud.
2. Ajoutez la dépendance du pod LeanChatLib, ou faites glisser les fichiers de code LeanChatLib dans votre projet pour une personnalisation UI plus facile et un ajustement des fonctionnalités.
3. Ajoutez le code suivant aux endroits appropriés,

À l'ouverture de l'application, initialisez et configurez l'utilisateur IM,
```objc
    [AVOSCloud setApplicationId:@"YourAppId" clientKey:@"YourAppKey"];
    [CDChatManager manager].userDelegate = [[CDUserFactory alloc] init];
```

Configurez une UserFactory, qui se conforme au protocole CDUserDelegate.

```objc
#import "CDUserFactory.h"

#import <LeanChatLib/LeanChatLib.h>

@interface CDUserFactory ()<CDUserDelegate>

@end


@implementation CDUserFactory

#pragma mark - CDUserDelegate
-(void)cacheUserByIds:(NSSet *)userIds block:(AVIMArrayResultBlock)block{
    block(nil,nil); // n'oubliez pas cela
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

Ici, CDUser est l'objet Utilisateur au sein de l'application et vous pouvez mettre en œuvre le protocole CDUserModel dans votre objet Utilisateur.

CDUserModel,
```objc
@protocol CDUserModel <NSObject>

@required

-(NSString*)userId;

-(NSString*)avatarUrl;

-(NSString*)username;

@end
```

Appelez lors de la connexion,
```objc
        [[CDChatManager manager] openWithClientId:selfId callback: ^(BOOL succeeded, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
               // allez au Contrôleur Principal
            }
        }];
```

Pour discuter avec quelqu'un,
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

Pour une discussion de groupe,
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

Lors de la déconnexion,
```objc
    [[CDChatManager manager] closeWithCallback: ^(BOOL succeeded, NSError *error) {

    }];
```

Ensuite, vous pouvez discuter comme montré dans la capture d'écran ci-dessus. Notez que nous ne recommandons actuellement pas d'utiliser la méthode pod pour importer directement LeanChatLib car certaines interfaces et fonctionnalités doivent être personnalisées par vous. Par conséquent, nous recommandons de copier le code LeanChatLib dans le projet pour une personnalisation plus facile.

## LeanChatLib ChangeLog

0.2.6

Mise à jour du SDK vers 3.1.4 pour s'adapter à iOS 9

0.2.5

Utilisation de cachePolicy dans AVIMConversationQuery pour économiser le trafic et mieux supporter le hors ligne
Correction d'un bug où l'appel de fetchConvWithConvid lorsque la conversation n'existe pas peut provoquer un plantage

0.2.4

Ajout de l'icône Tuzki

0.2.3

Ajout d'une vérification des paramètres pour l'interface fetchConvWithMembers:, correction d'un potentiel plantage dans la liste des conversations lorsqu'il s'agit d'une discussion individuelle mais qu'elle n'a qu'un seul membre

0.2.2

Mise à jour de la bibliothèque AVOSCloud vers 3.1.2.8

0.2.1

ChatListDelegate ajoute les interfaces configureCell: et prepareConversaion: pour une personnalisation plus complexe des conversations.

Pour les messages d'images, utilisez AVFile pour mettre en cache les images, de sorte que vos propres photos envoyées n'aient pas besoin d'être téléchargées à nouveau.

0.2.0

Ajout de commentaires, support du réenvoi des messages, affichage des messages échoués, ajout d'effets sonores et de vibrations

0.1.3

Correction d'un bug où l'application pouvait planter lors du chargement rapide des messages historiques en tirant vers le bas

0.1.2

Utilisation du cache de discussion SDK, suppression de la dépendance FMDB. Vous pouvez voir les messages historiques sur le serveur et les enregistrements de discussion historiques même après réinstallation. Suppression de la classe CDNotify.

0.1.1

Refonte

0.1.0

Version initiale

## Notes de déploiement pour LeanChat

Si vous souhaitez déployer LeanChat complète, puisque l'application a une fonctionnalité d'ajout d'amis, veuillez allez dans Paramètres->Options de l'application et cochez l'option Suivi mutuel afin que lorsque l'une des parties accepte, elles puissent s'ajouter mutuellement en amis.

![qq20150407-5](https://cloud.githubusercontent.com/assets/5022872/7016645/53f91bb8-dd1b-11e4-8ce0-72312c655094.png)

## Guide de développement

[Guide de développement du service de messagerie en temps réel](https://leancloud.cn/docs/realtime_v2.html)

[Plus d'informations](https://github.com/leancloud/leanchat-android)

## Remerciements

Merci à la grande bibliothèque open-source [MessageDisplayKit](https://github.com/xhzengAIB/MessageDisplayKit) par Xian-Hua Han.