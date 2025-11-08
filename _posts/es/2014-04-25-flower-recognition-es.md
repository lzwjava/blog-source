---
audio: false
generated: false
image: false
lang: es
layout: post
title: App de Reconocimiento de Flores
translated: true
type: post
---

Este es el README.md del proyecto de github [https://github.com/lzwjava/flower-recognition](https://github.com/lzwjava/flower-recognition).

---

### Aplicación de Reconocimiento de Flores

Esta es una aplicación Android de reconocimiento de flores diseñada para ayudar a los usuarios a identificar flores capturando fotos y dibujando círculos para asistir en el reconocimiento.

#### Características:
- **Captura de Fotos**: Los usuarios pueden tomar fotos de flores directamente dentro de la aplicación.
- **Funcionalidad de Dibujo**: Capacidad para dibujar círculos y anotaciones en imágenes de flores para asistir en el reconocimiento.
- **Autenticación**: Autenticación de usuario segura con una pantalla de inicio de sesión.
- **Mostrar Resultados**: Mostrar resultados de reconocimiento en una interfaz amigable para el usuario.
- **Diseño Material**: Implementación de los principios de diseño material para una experiencia de usuario moderna e intuitiva.

#### Estructura de Archivos:
```
└── com
    └── lzw
        └── flower
            ├── activity
            │   ├── LoginActivity.java
            │   └── PhotoActivity.java
            ├── adapter
            │   └── PhotoAdapter.java
            ├── avobject
            │   └── Photo.java
            ├── base
            │   ├── App.java
            │   ├── ImageLoader.java
            │   └── SplashActivity.java
            ├── deprecated
            │   ├── CameraActivity.java
            │   └── Deprecated.java
            ├── draw
            │   ├── Draw.java
            │   ├── DrawActivity.java
            │   ├── DrawFragment.java
            │   ├── DrawView.java
            │   ├── HelpBtn.java
            │   ├── History.java
            │   ├── Tooltip.java
            │   └── ZoomImageView.java
            ├── fragment
            │   ├── RecogFragment.java
            │   └── WaitFragment.java
            ├── material
            │   └── MaterialActivity.java
            ├── result
            │   ├── FlowerAdapter.java
            │   ├── FlowerData.java
            │   ├── Image.java
            │   ├── ResultActivity.java
            │   └── ResultFragment.java
            ├── service
            │   └── PhotoService.java
            ├── utils
            │   ├── BitmapUtils.java
            │   ├── Crop.java
            │   ├── ImageListDialogBuilder.java
            │   ├── Logger.java
            │   ├── PathUtils.java
            │   └── Utils.java
            └── web
                ├── Upload.java
                ├── UploadImage.java
                └── Web.java
```

#### Componentes:
- **Activities**: Contiene clases para manejar diferentes actividades de la aplicación como el inicio de sesión, la captura de fotos y la pantalla de inicio.
- **Adapters**: Maneja la visualización de fotos y resultados de reconocimiento.
- **AVObject**: Representa objetos de fotos con metadatos asociados.
- **Drawing**: Clases relacionadas con el dibujo de círculos y anotaciones en imágenes de flores.
- **Fragments**: Proporciona componentes de interfaz de usuario para mostrar resultados de reconocimiento e indicadores de espera.
- **Material**: Posiblemente relacionado con la implementación de las directrices de diseño material.
- **Services**: Maneja tareas en segundo plano y manipulación de datos relacionados con fotos.
- **Utils**: Contiene clases utilitarias para diversas tareas como la manipulación de imágenes y el registro.

#### Uso:
1. Clona el repositorio.
2. Abre el proyecto en Android Studio.
3. Compila y ejecuta la aplicación en un dispositivo Android o emulador.

#### Licencia:
Este proyecto está protegido bajo la [Licencia MIT](LICENSE).