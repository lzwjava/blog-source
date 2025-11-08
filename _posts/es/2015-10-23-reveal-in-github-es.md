---
audio: false
generated: false
image: false
lang: es
layout: post
title: 'Un complemento de Xcode: Reveal-In-GitHub'
translated: true
type: post
---

Esto es el README.md del proyecto de GitHub [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub).

---

# Reveal-In-GitHub

Un complemento de Xcode diseñado para una navegación fluida a las funcionalidades clave de GitHub dentro de tu repositorio actual. Con solo un clic, accede sin esfuerzo al historial de GitHub, a la funcionalidad Blame, a las solicitudes de extracción, a los problemas y a las notificaciones, todo en cuestión de segundos.

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

Mi empresa trabaja en GitHub. Abro GitHub con frecuencia. A veces, mientras edito en Xcode, no entiendo algunos códigos, así que voy a GitHub para investigar. A veces, busco los últimos compromisos sobre un archivo para ayudarme a entender cómo evoluciona el código. Entonces me pregunté si hay una herramienta que me ayude a abrir rápidamente GitHub desde Xcode. Así que escribí este complemento. Cuando estás editando algún archivo de origen en Xcode, es fácil saber en qué repositorio de GitHub estás trabajando y saber qué archivo estás editando. Así que tiene sentido saltar rápidamente al archivo en GitHub, saltar rápidamente a la responsabilidad de la línea actual que estás editando en GitHub, saltar rápidamente a los problemas o a las solicitudes de extracción del repositorio actual en el que estás trabajando en Xcode.

## Elementos del Menú

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

Tiene seis elementos de menú:

 Menu Title     | Shortcut              | Patrón de URL de GitHub (Cuando estoy editando LZAlbumManager.m Línea 40)                |
----------------|-----------------------|----------------------------------
 Setting	    |⌃⇧⌘S |
 Repo           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 Quick File     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 List History   |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blame          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Notifications  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

Los atajos de teclado están cuidadosamente diseñados. No entrarán en conflicto con los atajos predeterminados de Xcode. El patrón de atajo es ⌃⇧⌘ (Ctrl+Shift+Command), más la primera letra del título del menú.

## Personalizar

A veces, puede que quieras saltar rápidamente a la Wiki. Aquí está el método, abre la configuración:

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

Por ejemplo,

Archivo rápido, el patrón y la URL real:

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

El {commit} es el hash del compromiso más reciente de la rama actual. Es mejor que usar la rama. Porque el HEAD de la rama puede cambiar. Así que el código en #L40-L43 también puede cambiar.

Entonces, si quieres agregar un atajo al wiki del repositorio actual, solo agrega un elemento del menú y establece el patrón en `{git_remote_url}/wiki`.

En la configuración, `Clear Default Repos` dice que si tienes múltiples remotos de git, cuando se active por primera vez, te pedirá que elijas uno de ellos:

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

Luego, el complemento recordará cuál elegiste. Así que cuando vuelvas a activar el menú, abrirá ese repositorio remoto como predeterminado. El botón `Clear Default Repos` borrará esta configuración y te pedirá seleccionar de nuevo.

## Instalación

Se recomienda instalar con [Alcatraz](http://alcatraz.io/),

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

O

1. Clona este repositorio.
2. Abre `Reveal-In-GitHub.xcodeproj` y compílalo.
3. `Reveal-In-GitHub.xcplugin` debe estar en `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`
4. Reinicia Xcode
5. Abre cualquier proyecto de GitHub y presiona ⌃⇧⌘B (Ctrl+Shift+Command+B) para investigar el código.

## 安装

推荐使用 [Alcatraz](http://alcatraz.io/)，可参考巧神的一遍[博客](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)。安装好后，按照上图搜索 `Reveal In GitHub`，点击 `Install` 即可。

如果不使用这个工具的话，那么也只需三步：

* 克隆该项目到本地。
* 打开 xcodeproj，点击 Build 构建。这会在目录`~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` 生成 Reveal-In-GitHub.xcplugin 文件。
* 重启 Xcode，打开任意一个放在 GitHub 上的项目。按下 `Ctrl+Shift+Command+B` 即可。

## Créditos

Durante el curso de su desarrollo, encontré otro complemento [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) que hace algo similar. Aprendí algunas técnicas de él. Gracias por eso.

## Licencia

MIT