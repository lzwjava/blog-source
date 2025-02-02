---
audio: false
lang: es
layout: post
title: 'Un Plugin de Xcode: Revelar-en-GitHub'
translated: true
---

Este es el README.md del proyecto de GitHub [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub).

---

# Reveal-In-GitHub

Un plugin de Xcode diseñado para una navegación fluida a las funcionalidades clave de GitHub dentro de tu repositorio actual. Con solo un clic, accede sin esfuerzo al historial de GitHub, Blame, Pull Requests, Issues y Notificaciones, todo en cuestión de segundos.

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

Mi empresa trabaja en GitHub. Abro GitHub a menudo. A veces, estoy editando en Xcode y no entiendo algún código, así que voy a GitHub a buscar la culpa. A veces, busco los últimos commit de un archivo para ayudarme a entender cómo evoluciona el código. Así que me pregunto si hay una herramienta que me permita abrir rápidamente GitHub desde Xcode. Entonces escribí este plugin. Cuando estás editando algún archivo de origen en Xcode, es fácil saber en qué repositorio de GitHub estás trabajando y saber qué archivo estás editando. Entonces tiene sentido saltar rápidamente al archivo en GitHub, saltar rápidamente a la culpa de la línea actual que estás editando en GitHub, saltar rápidamente a los issues o prs del repositorio actual en el que estás trabajando en Xcode.

## Elementos del Menú

![2015-11-01 12 56 35](https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png)

Tiene seis elementos de menú:

 Menú Title    | Ataj                          | Patrón de URL de GitHub (cuando estoy editando LZAlbumManager.m Línea 40)
----------------|-----------------------------|---------------------------------------------------------------
 Configuración  |⌃⇧⌘S |                          |
 Repo           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 Archivo Rápido  |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Historial       |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blame          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Notificaciones  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

Los atajos están cuidadosamente diseñados. No entrarán en conflicto con los atajos predeterminados de Xcode. El patrón de atajos es ⌃⇧⌘ (Ctrl+Shift+Command), más la primera letra del título del menú.

## Personalizar

A veces, puede que quieras saltar rápidamente a la Wiki. Aquí está la forma, abre la configuración:

![2015-11-01 12 56 35](https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png)

Por ejemplo,

Archivo rápido, el patrón y la URL real:

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

El {commit} es el hash del último commit de la rama actual. Es mejor usarlo en lugar de la rama. Porque la HEAD de la rama puede cambiar. Entonces el código en #L40-L43 también puede cambiar.

Entonces, si quieres agregar un acceso directo a la wiki del repositorio actual, solo agrega un elemento de menú y establece el patrón en `{git_remote_url}/wiki`.

En la configuración, `Clear Default Repos` dice si tienes múltiples remotos git, al primer intento, te pedirá que elijas uno de ellos:

![5794994a-803c-11e5-9527-965f7e617e8f](https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png)

Luego, el plugin recuerda cuál elegiste. Entonces, cuando vuelvas a activar el menú, abrirá ese repositorio remoto como predeterminado. El botón `Clear Default Repos` borrará esta configuración y te pedirá que selecciones nuevamente.

## Instalar

Recomiendo instalar con [Alcatraz](http://alcatraz.io/),

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

O

1. Clona este repositorio.
2. Abre `Reveal-In-GitHub.xcodeproj` y compíralo.
3. Reveal-In-GitHub.xcplugin debe estar ubicado en `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`
4. Reinicia Xcode
5. Abre cualquier proyecto de GitHub y presiona ⌃⇧⌘B (Ctrl+Shift+Command+B) para buscar la culpa del código.

## 安装

推荐使用 [Alcatraz](http://alcatraz.io/)，可参考巧神的一遍[博客](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)。安装好后，按照上图搜索 `Reveal In GitHub`，点击 `Install` 即可。

如果不使用这个工具的话，那么也只需三步：

* 克隆该项目到本地。
* 打开 xcodeproj，点击 Build 构建。这会在目录`~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` 生成 Reveal-In-GitHub.xcplugin 文件。
* 重启 Xcode，打开任意一个放在 GitHub 上的项目。按下 `Ctrl+Shift+Command+B` 即可。

## Créditos

Cuando estaba desarrollando, encontré otro plugin [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) que hace algo similar. Aprendí algunas técnicas de él. Gracias por eso.

## Licencia

MIT