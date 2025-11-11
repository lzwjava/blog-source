---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser FFmpeg en PHP
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser "php-ffmpeg/php-ffmpeg" version ~0.5, vous devez d'abord installer FFMpeg sur votre système, puis utiliser Composer pour installer la bibliothèque PHP.
- Les recherches suggèrent d'inclure le fichier d'autoload et de créer une instance de `FFMpeg\FFMpeg` pour la manipulation des médias, avec des options pour spécifier les chemins des binaires si nécessaire.
- Les preuves penchent en faveur de l'utilisation de méthodes comme `open()`, `save()`, et `frame()` pour les opérations de base, mais vérifiez la documentation GitHub pour plus de détails en raison de différences potentielles spécifiques à la version.

---

### Installation
Premièrement, assurez-vous que FFMpeg est installé sur votre système :
- Sur Ubuntu, utilisez `sudo apt-get install ffmpeg`.
- Sur macOS, utilisez `brew install ffmpeg`.
- Sur Windows, téléchargez-le depuis [ce site web](https://www.gyan.dev/ffmpeg/builds/) et suivez les instructions.

Ensuite, installez la bibliothèque php-FFMpeg via Composer avec :
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### Configuration et Utilisation
Incluez le fichier d'autoload dans votre script PHP :
```php
require_once 'vendor/autoload.php';
```

Créez une instance de `FFMpeg\FFMpeg`, en spécifiant optionnellement les chemins si les binaires FFMpeg ne sont pas dans le PATH système :
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/chemin/vers/FFMpeg',
    'ffprobe' => '/chemin/vers/FFprobe'
));
```

Ouvrez un fichier multimédia et effectuez des opérations, telles que :
- Transcodage : `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- Extraction d'une image : `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- Découpage : `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

Pour plus de détails, reportez-vous à la documentation de la bibliothèque sur [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg).

---

### Note d'Enquête : Guide Complet pour Utiliser php-FFMpeg/php-FFMpeg Version ~0.5

Cette note fournit une exploration approfondie de l'utilisation de la bibliothèque "php-FFMpeg/php-FFMpeg", spécifiquement la version approximative 0.5, basée sur les informations disponibles. Elle développe la réponse directe en incluant tous les détails pertinents de la recherche, assurant une compréhension complète pour les utilisateurs cherchant à implémenter cette bibliothèque PHP pour la manipulation de médias.

#### Contexte
La bibliothèque "php-FFMpeg/php-FFMpeg" est un wrapper PHP pour le binaire FFMpeg, permettant une manipulation orientée objet des fichiers vidéo et audio. Elle prend en charge des tâches telles que le transcodage, l'extraction d'images, le découpage et plus encore, ce qui la rend précieuse pour les développeurs travaillant sur des applications liées aux médias. La spécification de version "~0.5" indique toute version supérieure ou égale à 0.5 et inférieure à 1.0, suggérant une compatibilité avec les anciennes versions de PHP, probablement trouvée dans la branche 0.x du dépôt.

Compte tenu de la date actuelle, le 3 mars 2025, et de l'évolution de la bibliothèque, la version 0.5 peut faire partie d'un support legacy, la branche principale nécessitant désormais PHP 8.0 ou supérieur. Cette note suppose que l'utilisateur travaille dans les contraintes de cette version, reconnaissant les différences potentielles de fonctionnalité par rapport aux versions plus récentes.

#### Processus d'Installation
Pour commencer, FFMpeg doit être installé sur le système, car la bibliothèque repose sur ses binaires pour les opérations. Les méthodes d'installation varient selon le système d'exploitation :
- **Ubuntu** : Utilisez la commande `sudo apt-get install ffmpeg` pour installer via le gestionnaire de paquets.
- **macOS** : Utilisez Homebrew avec `brew install ffmpeg` pour une installation simple.
- **Windows** : Téléchargez les binaires FFMpeg depuis [ce site web](https://www.gyan.dev/ffmpeg/builds/) et suivez les instructions fournies, en vous assurant que les exécutables sont accessibles dans le PATH système ou spécifiés manuellement.

Suite à l'installation de FFMpeg, la bibliothèque php-FFMpeg est installée via Composer, le gestionnaire de paquets PHP. La commande `composer require php-FFMpeg/php-FFMpeg:~0.5` assure que la version correcte est récupérée. Ce processus crée un répertoire `vendor` dans le projet, hébergeant la bibliothèque et ses dépendances, avec Composer gérant l'autoloading pour une intégration transparente.

#### Configuration et Initialisation
Après l'installation, incluez le fichier d'autoload dans votre script PHP pour permettre l'accès aux classes de la bibliothèque :
```php
require_once 'vendor/autoload.php';
```

Créez une instance de `FFMpeg\FFMpeg` pour commencer à utiliser la bibliothèque. La méthode de création permet la configuration, particulièrement importante si les binaires FFMpeg ne sont pas dans le PATH système :
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/chemin/vers/votre/propre/FFMpeg',
    'ffprobe' => '/chemin/vers/votre/propre/FFprobe'
));
```
Cette configuration permet de définir des timeouts, des nombres de threads et des chemins de binaires explicites, améliorant la flexibilité pour différentes configurations système. La configuration par défaut recherche les binaires dans le PATH, mais la spécification manuelle assure la compatibilité, surtout sur des environnements personnalisés.

#### Utilisation de Base et Opérations
La bibliothèque fournit une interface fluide et orientée objet pour la manipulation des médias. Commencez par ouvrir un fichier multimédia :
```php
$video = $ff->open('input.mp4');
```
Cela prend en charge les chemins du système de fichiers local, les ressources HTTP et autres protocoles supportés par FFMpeg, avec une liste des types supportés disponible via la commande `ffmpeg -protocols`.

##### Transcodage
Le transcodage consiste à convertir un média en différents formats. Utilisez la méthode `save` avec une instance de format :
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
Le format `X264` est un exemple ; la bibliothèque supporte divers formats vidéo et audio, implémentables via `FFMpeg\Format\FormatInterface`, avec des interfaces spécifiques comme `VideoInterface` et `AudioInterface` pour les types de médias respectifs.

##### Extraction d'Image
L'extraction d'images est utile pour les miniatures ou l'analyse. Le code suivant extrait une image à 5 secondes :
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
La classe `TimeCode`, faisant partie de `FFMpeg\Coordinate`, assure un timing précis, avec des options pour la précision dans l'extraction d'image.

##### Découpage
Pour découper une partie de la vidéo, spécifiez les heures de début et de fin :
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
Cela crée un nouveau segment vidéo, conservant la qualité et le format d'origine, avec la possibilité d'appliquer des filtres supplémentaires si nécessaire.

#### Fonctionnalités Avancées et Considérations
La bibliothèque prend en charge des fonctionnalités supplémentaires, comme décrit dans la documentation :
- **Manipulation Audio** : Similaire à la vidéo, l'audio peut être transcodé avec `FFMpeg\Media\Audio::save`, en appliquant des filtres, en ajoutant des métadonnées et en rééchantillonnant.
- **Création de GIF** : Les GIF animés peuvent être enregistrés en utilisant `FFMpeg\Media\Gif::save`, avec des paramètres de durée optionnels.
- **Concaténation** : Combinez plusieurs fichiers multimédias en utilisant `FFMpeg\Media\Concatenate::saveFromSameCodecs` pour les mêmes codecs ou `saveFromDifferentCodecs` pour les codecs variés, avec des ressources pour une lecture plus approfondie à [ce lien](https://trac.ffmpeg.org/wiki/Concatenate), [ce lien](https://ffmpeg.org/ffmpeg-formats.html#concat-1), et [ce lien](https://ffmpeg.org/ffmpeg.html#Stream-copy).
- **Gestion Avancée des Médias** : Prend en charge les entrées/sorties multiples avec `-filter_complex`, utile pour le filtrage et le mappage complexes, avec support de filtres intégrés.
- **Extraction de Métadonnées** : Utilisez `FFMpeg\FFProbe::create` pour les métadonnées, en validant les fichiers avec `FFMpeg\FFProbe::isValid` (disponible depuis v0.10.0, notant que la version 0.5 peut en être dépourvue).

Les coordonnées, telles que `FFMpeg\Coordinate\AspectRatio`, `Dimension`, `FrameRate`, `Point` (dynamique depuis v0.10.0), et `TimeCode`, fournissent un contrôle précis sur les propriétés des médias, bien que certaines fonctionnalités comme les points dynamiques puissent ne pas être disponibles dans la version 0.5.

#### Notes Spécifiques à la Version
Compte tenu de la spécification "~0.5", la bibliothèque s'aligne probablement avec la branche 0.x, supportant les anciennes versions de PHP. Le dépôt GitHub indique PHP 8.0 ou supérieur pour la branche principale, avec 0.x pour le support legacy. Cependant, les détails exacts de la version 0.5 n'ont pas été explicitement trouvés dans les releases, suggérant qu'elle peut faire partie de l'historique des commits ou des commits de branche. Les utilisateurs doivent vérifier la compatibilité, car les fonctionnalités plus récentes comme certains types de coordonnées (par exemple, les points dynamiques) peuvent nécessiter des versions au-delà de 0.5.

#### Documentation et Lectures Complémentaires
Bien que la page Read the Docs ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) soit apparue vide, le dépôt GitHub ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) contient une documentation complète dans le README, couvrant l'utilisation de l'API, les formats et des exemples. C'est la ressource principale pour la version 0.5, étant donné l'absence de documentation en ligne spécifique pour cette version legacy.

#### Tableau : Résumé des Opérations et Méthodes Clés

| Opération               | Exemple de Méthode                                      | Description                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| Ouvrir un Fichier Média | `$ff->open('input.mp4')`                           | Charge un fichier multimédia pour manipulation  |
| Transcoder une Vidéo    | `$video->save('output.mp4', new X264())`           | Convertit vers le format spécifié               |
| Extraire une Image      | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | Extrait une image au temps spécifié, enregistre en image |
| Découper une Vidéo      | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | Crée un clip entre les temps, enregistre en nouveau fichier |
| Configurer l'Instance   | `FFMpeg::create(array('binary' => '/chemin/vers/FFMpeg'))` | Définit les chemins des binaires et options personnalisés |

Ce tableau encapsule les fonctionnalités principales, aidant les utilisateurs dans une référence rapide lors de l'implémentation de la bibliothèque.

#### Détail Inattendu : Implications de la Version Legacy
Un aspect inattendu est la limitation potentielle de la version 0.5, étant donné son placement dans la branche 0.x pour le support des anciennes versions de PHP. Cela peut restreindre l'accès aux fonctionnalités modernes, telles que les points de coordonnées dynamiques introduits dans v0.10.0, obligeant les utilisateurs à vérifier les commits de branche pour les capacités exactes, ajoutant une couche de complexité non immédiatement apparente dans les versions plus récentes.

#### Conclusion
Utiliser "php-FFMpeg/php-FFMpeg" version ~0.5 implique d'installer FFMpeg, de configurer via Composer et de tirer parti d'une API orientée objet pour les tâches multimédias. Bien que les opérations de base comme le transcodage et l'extraction d'images soient simples, les différences spécifiques à la version peuvent nécessiter de consulter la documentation de la branche 0.x sur [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg). Cette approche complète assure que les utilisateurs peuvent utiliser efficacement la bibliothèque, reconnaissant à la fois sa puissance et ses contraintes legacy potentielles.

---

### Citations Clés
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)