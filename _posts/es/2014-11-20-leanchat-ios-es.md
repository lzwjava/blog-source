---
audio: false
generated: false
image: false
lang: es
layout: post
title: 'LeanChat iOS


  Chat en Línea iOS'
translated: true
type: post
---

Este es el archivo README.md del proyecto de GitHub [https://github.com/lzwjava/leanchat-ios](https://github.com/lzwjava/leanchat-ios).

---

![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/v/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![CocoaPods](http://img.shields.io/cocoapods/p/LeanChatLib.svg?style=flat)](http://cocoapods.org/?q=LeanChatLib)&nbsp;
[![Support](https://img.shields.io/badge/support-iOS%207%2B%20-blue.svg?style=flat)](https://www.apple.com/nl/ios/)

![leanchat](https://cloud.githubusercontent.com/assets/5022872/8431636/4eff0aca-1f6d-11e5-8728-f8f450dac380.gif)

## App Store
LeanChat está disponible en la App Store. Puedes visitar [https://itunes.apple.com/gb/app/leanchat/id943324553](https://itunes.apple.com/gb/app/leanchat/id943324553) o buscar LeanChat en la App Store.

## Introducción
Este proyecto de ejemplo demuestra de manera exhaustiva la aplicación de la característica de comunicación en tiempo real de LeanCloud. Sin embargo, contiene mucha lógica de la interfaz de usuario y otras funcionalidades, lo que lo hace no adecuado para aprender rápidamente. Si eres nuevo en LeanMessage, te recomendamos el proyecto [LeanMessage-Demo](https://github.com/leancloud/LeanMessage-Demo). Una vez que te familiarices, puedes ir a [LeanCloud-Demos](https://github.com/leancloud/leancloud-demos) para seleccionar tu piel de IM favorita para la integración. Durante la integración, si encuentras problemas difíciles, puedes volver a referirte al proyecto LeanChat.

## Estructura del Proyecto LeanChat

* [leanchat-android](https://github.com/leancloud/leanchat-android): Cliente de Android
* [leanchat-ios](https://github.com/leancloud/leanchat-ios): Cliente de iOS
* [leanchat-webapp](https://github.com/leancloud/leanchat-webapp): Cliente web
* [leanchat-cloud-code](https://github.com/leancloud/leanchat-cloudcode): Servidor

## Retroalimentación Valiosa

Si tienes alguna pregunta, no dudes en abrir un [issue](https://github.com/leancloud/leanchat-ios/issues), mencionando lo que no entiendes, y te proporcionaremos asistencia lo antes posible.

## Descarga
Haz clic directamente en `Descargar ZIP` en GitHub, como se muestra en la imagen a continuación, para descargar solo la última versión. Si usas `git clone`, puede ser muy lento porque incluye un gran historial de commits. En una prueba, la diferencia fue de 1.5M:40M.

![qq20150618-2 2x](https://cloud.githubusercontent.com/assets/5022872/8223520/4c25415a-15ab-11e5-912d-b5dab916ce86.png)

## Ejecución
```bash
  // LeanChat (Ejemplo Complejo)
  cd LeanChat
  pod install --verbose  // Si tienes una biblioteca de dependencias de AVOSCloud localmente, puedes agregar la opción --no-repo-update para acelerar el proceso
  open LeanChat.workspace

  // LeanChatExample (Ejemplo Simple)
  cd LeanChatExample
  pod install --verbose --no-repo-update
  open LeanChatExample.xcworkspace

  // LeanChatSwift (Ejemplo en Swift)
  cd LeanChatSwift
  pod install --verbose --no-repo-update
  open LeanChatSwift.xcworkspace

  // LeanChatLib (Librería que encapsula los componentes de comunicación y la interfaz de usuario de LeanCloud)
  cd LeanChatLib
  pod install --verbose --no-repo-update
  open LeanChatLib.xcworkspace
```

Si encuentras problemas como `la definición de 'AVUser' debe importarse del módulo 'LeanChatLib.CDChatListVC' antes de que se requiera`, puedes mantener presionada la tecla Option en el menú Product y hacer clic en [Clean Build Folder](http://stackoverflow.com/questions/8087065/xcode-4-clean-vs-clean-build-folder) para limpiar todos los archivos de compilación, luego recompilar. Este problema parece ser un error cuando Cocoapods realiza la compilación compleja. Puedes ver este [Gif](https://cloud.githubusercontent.com/assets/5022872/9230256/cf822fe4-4153-11e5-876d-ed819babad89.gif) para más detalles.

Ten en cuenta que, debido a que se utilizan certificados de producción por defecto, no se reciben notificaciones push para mensajes fuera de línea durante el desarrollo. Sin embargo, las notificaciones push están disponibles en la versión en línea, que se puede descargar desde la [App Store](https://itunes.apple.com/gb/app/leanchat/id943324553). Para más detalles, también puedes referirte a este [issue](https://github.com/leancloud/leanchat-ios/issues/40).

Aquí puedes ver tres proyectos, como se describe a continuación.

## Introducción del Subproyecto
* LeanChatLib: La lógica principal y la biblioteca de interfaz de usuario para el chat. Con ella, puedes integrar rápidamente la funcionalidad de chat, que soporta mensajes de texto, audio, imágenes y emojis, así como notificaciones de mensajes. También hay una versión correspondiente [para Android](https://github.com/leancloud/leanchat-android).
* LeanChatExample: El ejemplo de uso más sencillo de LeanChatLib. Muestra cómo usar la cantidad mínima de código para llamar a LeanChatLib para unirse a un chat, independientemente de si usas el sistema de usuarios de LeanCloud o el tuyo propio.
* LeanChat-ios: La aplicación LeanChat completa. Incluye características como la gestión de amigos, la gestión de grupos, el envío de mensajes basados en la ubicación, usuarios cercanos, páginas personales, inicio de sesión y registro, todas basadas en las capacidades de almacenamiento y comunicación de LeanCloud. Es una aplicación más compleja de LeanChatLib.

## Introducción a LeanChatLib

Encapsula la página de conversación reciente y la página de chat. Tanto el proyecto LeanChat como LeanChatExample dependen de él. Puedes instalarlo de la siguiente manera,

```
    pod 'LeanChatLib'
```

La mayoría de las veces, integrarás LeanChatLib arrastrando el código fuente a tu proyecto. En este caso, necesitarás instalar `AVOSCloud.framework` y `AVOSCloudIM.framework` primero. Si no usaste `pod install 'AVOSCloud'`, `pod install 'AVOSCloudIM'` para instalar, puedes configurar los marcos necesarios según la [Guía de Inicio Rápido](https://leancloud.cn/docs/start.html) de LeanCloud. También instala dos otras bibliotecas dependientes, `JSBadgeView` y `DateTools`. Al ejecutar `pod install` para este Demo, se generará un directorio Pods, del cual puedes encontrar estos dos Pods. Alternativamente, puedes buscarlos en línea. También puedes configurarlo a través del [.podspec file](https://github.com/leancloud/leanchat-ios/blob/master/LeanChatLib.podspec#L9), que describe qué archivos fuente deben integrarse y qué marcos del sistema deben introducirse, etc. O, por favor, refiérrete a este [ticket](https://ticket.leancloud.cn/tickets/7666).

## Cómo agregar IM en tres pasos
1. Crea una aplicación en LeanCloud.
2. Agrega la dependencia del pod LeanChatLib, o arrastra los archivos de código de LeanChatLib a tu proyecto para una personalización de interfaz de usuario más fácil y un ajuste de funcionalidad.
3. Agrega el siguiente código en los lugares apropiados,

Al iniciar la aplicación, inicializa y configura IM User,
```objc
    [AVOSCloud setApplicationId:@"YourAppId" clientKey:@"YourAppKey"];
    [CDChatManager manager].userDelegate = [[CDUserFactory alloc] init];
```

Configura una UserFactory, que cumple con el protocolo CDUserDelegate.

```objc
#import "CDUserFactory.h"

#import <LeanChatLib/LeanChatLib.h>

@interface CDUserFactory ()<CDUserDelegate>

@end


@implementation CDUserFactory

#pragma mark - CDUserDelegate
-(void)cacheUserByIds:(NSSet *)userIds block:(AVIMArrayResultBlock)block{
    block(nil,nil); // no lo olvides
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

Aquí, CDUser es el objeto de usuario dentro de la aplicación, y puedes implementar el protocolo CDUserModel en tu objeto de usuario.

CDUserModel,
```objc
@protocol CDUserModel <NSObject>

@required

-(NSString*)userId;

-(NSString*)avatarUrl;

-(NSString*)username;

@end
```

Llama al iniciar sesión,
```objc
        [[CDChatManager manager] openWithClientId:selfId callback: ^(BOOL succeeded, NSError *error) {
            if (error) {
                DLog(@"%@", error);
            }
            else {
               // Ir al Controlador Principal
            }
        }];
```

Para chatear con alguien,
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

Para chatear en grupo,
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

Al cerrar la sesión,
```objc
    [[CDChatManager manager] closeWithCallback: ^(BOOL succeeded, NSError *error) {

    }];
```

Luego, puedes chatear como se muestra en la captura de pantalla anterior. Ten en cuenta que actualmente no recomendamos usar el método pod para importar LeanChatLib directamente porque algunas interfaces y funcionalidades necesitan ser personalizadas por ti. Por lo tanto, recomendamos copiar el código de LeanChatLib en el proyecto para una personalización más fácil.

## Registro de cambios de LeanChatLib

0.2.6

Actualiza el SDK a 3.1.4 para adaptarse a iOS 9

0.2.5

Usa cachePolicy en AVIMConversationQuery para ahorrar tráfico y soportar mejor el modo fuera de línea
Corregido un error donde llamar a fetchConvWithConvid cuando la conversación no existe podría causar un bloqueo

0.2.4

Añadido emoji de Tuzki

0.2.3

Añadida verificación de parámetros para la interfaz fetchConvWithMembers, corregido un posible bloqueo en la lista de conversaciones cuando es una conversación de uno a uno pero solo tiene un miembro

0.2.2

Actualizada la biblioteca AVOSCloud a 3.1.2.8

0.2.1

ChatListDelegate añade las interfaces configureCell: y prepareConversaion: para una personalización de conversación más compleja.

Para mensajes de imágenes, usa AVFile para almacenar en caché imágenes, de modo que tus propias fotos enviadas no necesiten volver a descargarse.

0.2.0

Añade comentarios, soporta reenvío de mensajes, muestra mensajes fallidos, añade efectos de sonido y vibración

0.1.3

Corregido un error donde la aplicación podría bloquearse al cargar rápidamente mensajes históricos tirando hacia abajo

0.1.2

Usa la caché de chat del SDK, eliminada la dependencia de FMDB. Puedes ver mensajes históricos en el servidor y registros de chat históricos incluso después de la reinstalación. Eliminada la clase CDNotify.

0.1.1

Refactorización

0.1.0

Versión inicial

## Notas de Despliegue para LeanChat

Si deseas desplegar LeanChat completo, ya que la aplicación tiene una función de adición de amigos, ve a Configuración->Opciones de la Aplicación y marca la opción Seguidores Mutuos para que, cuando ambas partes acepten, puedan añadirse como amigos.

![qq20150407-5](https://cloud.githubusercontent.com/assets/5022872/7016645/53f91bb8-dd1b-11e4-8ce0-72312c655094.png)

## Guía de Desarrollo

[Guía de Desarrollo de Servicio de Mensajería en Tiempo Real](https://leancloud.cn/docs/realtime_v2.html)

[Más Información](https://github.com/leancloud/leanchat-android)

## Agradecimientos

Gracias a la excelente biblioteca de código abierto [MessageDisplayKit](https://github.com/xhzengAIB/MessageDisplayKit) de Xian-Hua Han.