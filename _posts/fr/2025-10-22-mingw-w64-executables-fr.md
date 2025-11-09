---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exécutables inclus avec MinGW-w64
translated: true
type: note
---

### Exécutables inclus dans MinGW-w64

MinGW-w64 est principalement une toolchain minimale pour la compilation croisée d'applications Windows natives en utilisant GCC et les outils associés. Il se concentre sur les utilitaires de développement plutôt que sur une suite complète de commandes de type Unix (par exemple, il n'inclut **pas** `gpg` ou GnuPG par défaut — ceux-ci sont disponibles sous forme de paquets séparés dans des environnements comme MSYS2). Le répertoire `bin` de l'installation principale contient généralement les exécutables suivants (basés sur un téléchargement autonome standard, comme celui des versions officielles de SourceForge). Cette liste peut varier légèrement selon la version et la compilation, mais voici les plus courants :

| Exécutable | Description |
|------------|-------------|
| `gcc.exe` | Compilateur C GNU |
| `g++.exe` | Compilateur C++ GNU |
| `cpp.exe` | Préprocesseur C |
| `gfortran.exe` | Compilateur Fortran GNU (s'il est inclus dans la compilation) |
| `ld.exe` | Éditeur de liens GNU |
| `as.exe` | Assembleur GNU |
| `ar.exe` | Archivage pour créer des bibliothèques |
| `ranlib.exe` | Génère un index pour les bibliothèques d'archives |
| `nm.exe` | Liste les symboles des fichiers objets |
| `objdump.exe` | Affiche les informations des fichiers objets |
| `objcopy.exe` | Copie et traduit les fichiers objets |
| `strip.exe` | Supprime les symboles des exécutables |
| `size.exe` | Liste la taille des sections des fichiers objets |
| `strings.exe` | Affiche les chaînes de caractères imprimables dans les fichiers |
| `readelf.exe` | Affiche les informations des fichiers ELF (pour les outils de compilation croisée) |
| `dlltool.exe` | Crée les fichiers d'import/export des DLL |
| `windres.exe` | Compile les fichiers de ressources Windows |
| `gendef.exe` | Génère les fichiers .def à partir des DLL |
| `genidl.exe` | Génère les fichiers .idl à partir des DLL |
| `widl.exe` | Compile les fichiers IDL pour Wine/Winelib |
| `gcc-ar.exe` | Wrapper GCC pour ar |
| `gcc-nm.exe` | Wrapper GCC pour nm |
| `gcc-ranlib.exe` | Wrapper GCC pour ranlib |

Il s'agit principalement d'outils de compilation, d'édition de liens et de manipulation de binaires provenant de GCC et Binutils. Pour un environnement plus complet de type Unix avec des outils comme `gpg`, `make`, `bash`, etc., envisagez d'installer MSYS2 (qui inclut MinGW-w64 en tant que composant) et d'ajouter des paquets via `pacman`.

[Site officiel de MinGW-w64](https://www.mingw-w64.org/)  
[Paquets MSYS2 (pour les extensions comme GnuPG)](https://packages.msys2.org/package/mingw-w64-x86_64-gnupg)  
[Téléchargements MinGW-w64 sur SourceForge](https://sourceforge.net/projects/mingw-w64/files/)