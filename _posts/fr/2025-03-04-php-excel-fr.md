---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque PHPExcel
translated: true
---

### Points Clés
- Il semble probable que pour utiliser "phpoffice/phpexcel": "^1.8", il faille l'installer via Composer et utiliser du code PHP pour lire et écrire des fichiers Excel.
- La recherche suggère que la bibliothèque est obsolète, il est donc conseillé d'utiliser PhpSpreadsheet pour les nouveaux projets.
- Les preuves penchent en faveur de la nécessité d'extensions PHP comme mbstring, XML et XMLWriter.

### Installation
Pour commencer, ajoutez `"phpoffice/phpexcel": "^1.8"` à votre fichier `composer.json` et exécutez `composer install`. Cela téléchargera la bibliothèque, essentielle pour travailler avec des fichiers Excel en PHP.

### Utilisation de Base
Pour écrire dans un fichier Excel :
- Incluez la bibliothèque avec `require 'vendor/autoload.php';`.
- Créez un nouvel objet PHPExcel : `$objPHPExcel = new PHPExcel();`.
- Définissez les valeurs des cellules, par exemple, `$sheet->setCellValue('A1', 'value');`.
- Enregistrez le fichier en utilisant un écrivain, comme `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` suivi de `$writer->save('filename.xlsx');`.

Pour lire à partir d'un fichier Excel :
- Chargez le fichier avec `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');`.
- Accédez aux valeurs des cellules, par exemple, `$cellValue = $sheet->getCell('A1')->getValue();`.

### Détail Inattendu
Un aspect inattendu est que PHPExcel prend en charge divers formats de fichiers comme .xls et .xlsx, et peut détecter automatiquement les types de fichiers lors de la lecture, ce qui simplifie l'utilisation.

---

### Note de Sondage : Guide Complet de l'Utilisation de "phpoffice/phpexcel": "^1.8"

Cette note fournit une exploration détaillée de l'utilisation de la bibliothèque PHPExcel, spécifiquement la version 1.8 ou supérieure, telle que spécifiée par la dépendance Composer "phpoffice/phpexcel": "^1.8". Étant donné son statut d'obsolescence, ce guide met également en avant des considérations pour les alternatives modernes et assure une compréhension approfondie pour les débutants et les utilisateurs avancés. Le contenu est structuré pour couvrir l'installation, l'utilisation, les dépendances et le contexte supplémentaire, en s'assurant que tous les détails pertinents de la recherche sont inclus.

#### Contexte et Contexte
PHPExcel est une bibliothèque PHP conçue pour lire et écrire des fichiers de tableur, notamment les formats Excel comme .xls et .xlsx. La spécification de version "^1.8" indique une plage de versionnement sémantique, ce qui signifie toute version à partir de 1.8 jusqu'à, mais sans inclure, 2.0, ce qui, étant donné l'historique de la bibliothèque, pointe vers la version 1.8.1 comme la dernière, publiée en 2015. Cependant, la recherche indique que PHPExcel a été officiellement obsolète en 2017 et archivée en 2019, avec la recommandation de migrer vers son successeur, PhpSpreadsheet, en raison d'un manque de maintenance et de problèmes de sécurité potentiels. Ce contexte est crucial pour les utilisateurs, car il suggère la prudence pour les nouveaux projets, bien que le guide se concentre sur l'utilisation de la version spécifiée comme demandé.

La fonctionnalité de la bibliothèque inclut la création, la lecture et la manipulation de fichiers Excel, en prenant en charge des formats au-delà d'Excel tels que CSV et HTML. Elle faisait partie du projet PHPOffice, qui a depuis déplacé son focus vers PhpSpreadsheet, offrant des fonctionnalités améliorées et une conformité aux normes PHP. Étant donné la date actuelle, le 3 mars 2025, et le statut d'archivage de la bibliothèque, les utilisateurs doivent être conscients de ses limitations, surtout avec les versions PHP plus récentes et les mises à jour de sécurité.

#### Processus d'Installation
Pour installer "phpoffice/phpexcel": "^1.8", le processus utilise Composer, le gestionnaire de dépendances PHP. Les étapes sont les suivantes :
- Ajoutez la dépendance à votre fichier `composer.json` sous la section "require" : `"phpoffice/phpexcel": "^1.8"`.
- Exécutez la commande `composer install` dans votre répertoire de projet. Cette commande télécharge la bibliothèque et met à jour le répertoire `vendor` avec les fichiers nécessaires.

La notation de caret (^) dans Composer suit le versionnement sémantique, en s'assurant que les versions 1.8, 1.8.1 ou toute mise à jour corrective sont installées, mais pas les versions qui pourraient rompre la compatibilité (c'est-à-dire pas 2.0 ou supérieur). Étant donné que la dernière version de la bibliothèque était 1.8.1 en 2015, cela se résout généralement à la version 1.8.1.

La recherche confirme que la page Packagist pour phpoffice/phpexcel la liste comme abandonnée, suggérant phpoffice/phpspreadsheet à la place, mais elle reste disponible pour l'installation, en s'alignant avec la demande de l'utilisateur.

#### Utilisation de Base : Écriture dans Excel
Une fois installé, l'utilisation de PHPExcel implique d'inclure le fichier autoload pour le chargement de classe, puis d'utiliser ses classes pour la manipulation de tableur. Voici un aperçu détaillé :

- **Inclure le Fichier Autoload :** Commencez votre script PHP avec `require 'vendor/autoload.php';`. Cette ligne assure que toutes les bibliothèques installées par Composer, y compris PHPExcel, sont chargées automatiquement, en utilisant le chargement automatique PSR-0 selon la structure de la bibliothèque de 2015.

- **Créer un Nouveau Objet PHPExcel :** Initialisez un nouveau classeur avec `$objPHPExcel = new PHPExcel();`. Cet objet représente l'ensemble du classeur, permettant plusieurs feuilles et propriétés.

- **Travaillez avec les Feuilles :** Accédez à la feuille active avec `$sheet = $objPHPExcel->getSheet(0);` pour la première feuille, ou créez-en une nouvelle avec `$sheet = $objPHPExcel->createSheet();`. Les feuilles sont indexées à partir de zéro, donc `getSheet(0)` cible la première feuille.

- **Définir les Valeurs des Cellules :** Remplissez les cellules en utilisant la méthode `setCellValue`, par exemple, `$sheet->setCellValue('A1', 'Hello');`. Cette méthode prend une référence de cellule (comme 'A1') et la valeur à insérer, qui peut être du texte, des nombres ou des formules.

- **Enregistrer le Fichier :** Pour enregistrer, créez un écrivain pour le format souhaité. Pour Excel 2007 et supérieur (.xlsx), utilisez `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`. Ensuite, enregistrez avec `$writer->save('filename.xlsx');`. D'autres formats incluent 'Excel5' pour .xls (Excel 95) ou 'CSV' pour les valeurs séparées par des virgules.

Un script d'exemple pour l'écriture pourrait ressembler à ceci :
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hello');
$sheet->setCellValue('B1', 'World');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hello_world.xlsx');
```
Cela crée un simple fichier Excel avec "Hello" en A1 et "World" en B1.

#### Utilisation de Base : Lecture à partir d'Excel
La lecture à partir d'un fichier Excel suit un schéma similaire mais commence par le chargement du fichier :
- **Charger le Fichier :** Utilisez `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` pour charger un fichier Excel existant. L'IOFactory peut détecter automatiquement le type de fichier, mais vous pouvez spécifier un lecteur, par exemple, `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` pour un type explicite.

- **Accéder aux Feuilles et aux Cellules :** Après le chargement, accédez aux feuilles comme avant, par exemple, `$sheet = $objPHPExcel->getSheet(0);`. Récupérez les valeurs des cellules avec `$cellValue = $sheet->getCell('A1')->getValue();`, qui retourne le contenu de la cellule spécifiée.

Un exemple pour la lecture :
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // Affiche "Hello"
```
Cela lit la valeur de A1, démontrant une récupération de base.

#### Dépendances et Exigences
PHPExcel a des exigences spécifiques en matière de version PHP et d'extensions nécessaires pour son fonctionnement :
- **Version PHP :** Nécessite PHP 5.2 ou 7.0 ou supérieur, selon les métadonnées Packagist. Étant donné la date actuelle, le 3 mars 2025, la plupart des installations PHP modernes devraient répondre à cette exigence, mais les configurations plus anciennes peuvent nécessiter des mises à jour.
- **Extensions :** La bibliothèque dépend de `ext-mbstring`, `ext-XML` et `ext-XMLWriter`, qui doivent être activés dans votre configuration PHP. Ces extensions gèrent le codage des chaînes, l'analyse XML et l'écriture XML, respectivement, essentielles pour les opérations de fichiers Excel.

Les utilisateurs doivent vérifier que ces extensions sont actives en utilisant `phpinfo()` ou en vérifiant le fichier `php.ini`, en s'assurant qu'aucun problème de compatibilité ne survienne.

#### Fonctionnalités Supplémentaires et Formats
Au-delà de la lecture/écriture de base, PHPExcel prend en charge divers formats de fichiers, ce qui est un détail inattendu pour les utilisateurs familiers uniquement avec Excel. La bibliothèque peut gérer :
- Excel 2007 (.xlsx) via l'écrivain/lecteur 'Excel2007'.
- Excel 95 (.xls) via 'Excel5'.
- Fichiers CSV via 'CSV'.
- HTML via 'HTML'.

Lors de l'enregistrement, spécifiez le type d'écrivain ; lors de la lecture, l'IOFactory détecte souvent automatiquement, mais des lecteurs explicites peuvent être utilisés pour la fiabilité. Par exemple, pour enregistrer en tant que .xls :
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
Cette flexibilité est utile pour les systèmes hérités ou des besoins spécifiques de format, bien que les utilisateurs doivent noter les limitations spécifiques au format, surtout avec les versions plus anciennes d'Excel.

#### Obsolescence et Conseils de Migration
Un point critique est l'obsolescence de PHPExcel. La recherche montre qu'elle a été archivée en 2019, avec la dernière mise à jour en 2015, et n'est plus maintenue. Cela soulève des préoccupations concernant les vulnérabilités de sécurité et la compatibilité avec les versions PHP au-delà de 7.0, surtout avec les normes modernes comme PHP 8.x. Le dépôt GitHub et la page Packagist recommandent tous deux de migrer vers PhpSpreadsheet, qui offre des espaces de noms, la conformité PSR et un développement actif.

Pour les utilisateurs, cela signifie :
- Pour les projets existants utilisant PHPExcel 1.8, continuez avec prudence, en vous assurant des tests de sécurité et de compatibilité.
- Pour les nouveaux projets, envisagez fortement PhpSpreadsheet, avec des outils de migration disponibles, comme noté dans la documentation PhpSpreadsheet ([Migration de PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)).

Ce conseil est particulièrement pertinent étant donné la date actuelle, en assurant que les utilisateurs s'alignent sur les bibliothèques modernes et supportées.

#### Documentation et Apprentissage Supplémentaire
Pour une exploration plus approfondie, la documentation officielle de PHPExcel est disponible dans son dépôt GitHub sous le dossier Documentation, bien que l'accès puisse nécessiter le téléchargement de fichiers comme la documentation du développeur DOC. En ligne, des tutoriels comme celui sur SitePoint ([Générer des fichiers Excel et des graphiques avec PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) fournissent des exemples pratiques, couvrant les graphiques et la mise en forme, qui vont au-delà de l'utilisation de base. Les fils de discussion Stack Overflow offrent également des informations de la communauté, bien que des précautions doivent être prises avec les réponses obsolètes étant donné le statut de la bibliothèque.

#### Tableau Comparatif : PHPExcel vs. PhpSpreadsheet
Pour aider à la prise de décision, voici un tableau de comparaison mettant en avant les différences clés, basé sur la recherche :

| Fonctionnalité                  | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| Dernière Mise à Jour              | 2015                              | Actif (jusqu'en 2025)             |
| Espaces de Noms               | Non, espace de noms racine                | Oui, conforme PSR-4            |
| Statut de Maintenance       | Obsolète, archivée 2019         | Activement maintenue             |
| Support des Versions PHP      | Jusqu'à 7.0                         | PHP 7.4+                        |
| Support des Formats de Fichiers      | Excel, CSV, HTML, etc.            | Amélioré, y compris ODS, PDF    |
| Performance              | Modérée, intensive en mémoire        | Optimisé, évolutif             |

Ce tableau souligne le passage à PhpSpreadsheet pour les besoins modernes, bien que PHPExcel reste fonctionnel pour des fins héritées.

#### Conclusion
L'utilisation de "phpoffice/phpexcel": "^1.8" implique l'installation via Composer, l'utilisation de ses classes pour les opérations Excel et l'assurance des extensions PHP requises. Bien que fonctionnelle, son obsolescence nécessite de la prudence, avec PhpSpreadsheet recommandé pour les futurs projets. Ce guide fournit un point de départ complet, avec des exemples, des dépendances et des ressources supplémentaires pour que les utilisateurs puissent explorer davantage.