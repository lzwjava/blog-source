---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque PHPExcel
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser "phpoffice/phpexcel": "^1.8", vous devez l'installer via Composer et utiliser du code PHP pour lire et écrire des fichiers Excel.
- Les recherches suggèrent que la bibliothèque est obsolète, donc envisagez d'utiliser PhpSpreadsheet pour les nouveaux projets.
- Les preuves indiquent qu'il est probable de nécessiter des extensions PHP comme mbstring, XML et XMLWriter.

### Installation
Pour commencer, ajoutez `"phpoffice/phpexcel": "^1.8"` à votre fichier `composer.json` et exécutez `composer install`. Cela téléchargera la bibliothèque, essentielle pour travailler avec des fichiers Excel en PHP.

### Utilisation de Base
Pour écrire dans un fichier Excel :
- Incluez la bibliothèque avec `require 'vendor/autoload.php';`.
- Créez un nouvel objet PHPExcel : `$objPHPExcel = new PHPExcel();`.
- Définissez les valeurs des cellules, par ex. `$sheet->setCellValue('A1', 'valeur');`.
- Sauvegardez le fichier en utilisant un writer, comme `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` suivi de `$writer->save('nom_du_fichier.xlsx');`.

Pour lire à partir d'un fichier Excel :
- Chargez le fichier avec `$objPHPExcel = PHPExcel_IOFactory::load('nom_du_fichier.xlsx');`.
- Accédez aux valeurs des cellules, par ex. `$cellValue = $sheet->getCell('A1')->getValue();`.

### Détail Inattendu
Un aspect inattendu est que PHPExcel prend en charge divers formats de fichiers comme .xls et .xlsx, et peut détecter automatiquement les types de fichiers lors de la lecture, ce qui simplifie l'utilisation.

---

### Note d'Enquête : Guide Complet pour Utiliser "phpoffice/phpexcel": "^1.8"

Cette note fournit une exploration détaillée de l'utilisation de la bibliothèque PHPExcel, spécifiquement la version 1.8 ou supérieure, comme spécifié par la dépendance Composer "phpoffice/phpexcel": "^1.8". Étant donné son statut d'obsolescence, ce guide met également en lumière les considérations pour les alternatives modernes et assure une compréhension approfondie pour les utilisateurs débutants et avancés. Le contenu est structuré pour couvrir l'installation, l'utilisation, les dépendances et le contexte supplémentaire, en s'assurant que tous les détails pertinents de la recherche sont inclus.

#### Contexte
PHPExcel est une bibliothèque PHP conçue pour lire et écrire des fichiers de feuille de calcul, en particulier les formats Excel comme .xls et .xlsx. La spécification de version "^1.8" indique une plage de version sémantique, signifiant toute version à partir de 1.8 jusqu'à, mais n'incluant pas, la version 2.0, ce qui, étant donné l'historique de la bibliothèque, pointe vers la version 1.8.1 comme la plus récente, publiée en 2015. Cependant, les recherches indiquent que PHPExcel a été officiellement déprécié en 2017 et archivé en 2019, avec la recommandation de migrer vers son successeur, PhpSpreadsheet, en raison du manque de maintenance et de problèmes de sécurité potentiels. Ce contexte est crucial pour les utilisateurs, car il suggère la prudence pour les nouveaux projets, bien que le guide se concentre sur l'utilisation de la version spécifiée comme demandé.

La fonctionnalité de la bibliothèque inclut la création, la lecture et la manipulation de fichiers Excel, prenant en charge des formats au-delà d'Excel tels que CSV et HTML. Elle faisait partie du projet PHPOffice, qui a depuis déplacé son focus vers PhpSpreadsheet, offrant des fonctionnalités améliorées et une conformité aux standards PHP. Étant donné la date actuelle, le 3 mars 2025, et le statut d'archivage de la bibliothèque, les utilisateurs doivent être conscients de ses limitations, en particulier avec les versions PHP plus récentes et les mises à jour de sécurité.

#### Processus d'Installation
Pour installer "phpoffice/phpexcel": "^1.8", le processus utilise Composer, le gestionnaire de dépendances PHP. Les étapes sont les suivantes :
- Ajoutez la dépendance à votre fichier `composer.json` dans la section "require" : `"phpoffice/phpexcel": "^1.8"`.
- Exécutez la commande `composer install` dans votre répertoire de projet. Cette commande télécharge la bibliothèque et met à jour le répertoire `vendor` avec les fichiers nécessaires.

La notation du caret (^) dans Composer suit le versionnage sémantique, garantissant que les versions 1.8, 1.8.1, ou toute mise à jour de correctif sont installées, mais pas les versions qui casseraient la compatibilité (c'est-à-dire pas la version 2.0 ou supérieure). Étant donné que la dernière version de la bibliothèque était la 1.8.1 en 2015, cela se résout généralement à la version 1.8.1.

Les recherches confirment que la page Packagist pour phpoffice/phpexcel la liste comme abandonnée, suggérant phpoffice/phpspreadsheet à la place, mais elle reste disponible pour l'installation, ce qui correspond à la demande de l'utilisateur.

#### Utilisation de Base : Écriture dans Excel
Une fois installé, utiliser PHPExcel implique d'inclure le fichier d'autoload pour le chargement des classes puis d'utiliser ses classes pour la manipulation des feuilles de calcul. Voici une ventilation détaillée :

- **Inclure le Fichier d'Autoload :** Commencez votre script PHP avec `require 'vendor/autoload.php';`. Cette ligne assure que toutes les bibliothèques installées par Composer, y compris PHPExcel, sont chargées automatiquement, en tirant parti de l'autoloading PSR-0 selon la structure de la bibliothèque de 2015.

- **Créer un Nouvel Objet PHPExcel :** Initialisez une nouvelle feuille de calcul avec `$objPHPExcel = new PHPExcel();`. Cet objet représente l'ensemble du classeur, permettant plusieurs feuilles et propriétés.

- **Travailler avec les Feuilles :** Accédez à la feuille active en utilisant `$sheet = $objPHPExcel->getSheet(0);` pour la première feuille, ou créez-en une nouvelle avec `$sheet = $objPHPExcel->createSheet();`. Les feuilles sont indexées à partir de zéro, donc `getSheet(0)` cible la première feuille.

- **Définir les Valeurs des Cellules :** Remplissez les cellules en utilisant la méthode `setCellValue`, par ex. `$sheet->setCellValue('A1', 'Bonjour');`. Cette méthode prend une référence de cellule (comme 'A1') et la valeur à insérer, qui peut être du texte, des nombres ou des formules.

- **Sauvegarder le Fichier :** Pour sauvegarder, créez un writer pour le format souhaité. Pour Excel 2007 et supérieur (.xlsx), utilisez `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`. Puis sauvegardez avec `$writer->save('nom_du_fichier.xlsx');`. D'autres formats incluent 'Excel5' pour .xls (Excel 95) ou 'CSV' pour les valeurs séparées par des virgules.

Un exemple de script pour l'écriture pourrait ressembler à :
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Bonjour');
$sheet->setCellValue('B1', 'Monde');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('bonjour_monde.xlsx');
```
Cela crée un simple fichier Excel avec "Bonjour" en A1 et "Monde" en B1.

#### Utilisation de Base : Lecture d'Excel
La lecture d'un fichier Excel suit un schéma similaire mais commence par le chargement du fichier :
- **Charger le Fichier :** Utilisez `$objPHPExcel = PHPExcel_IOFactory::load('nom_du_fichier.xlsx');` pour charger un fichier Excel existant. L'IOFactory peut détecter automatiquement le type de fichier, mais vous pouvez spécifier un reader, par ex. `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('nom_du_fichier.xlsx');` pour un type explicite.

- **Accéder aux Feuilles et Cellules :** Après le chargement, accédez aux feuilles comme auparavant, par ex. `$sheet = $objPHPExcel->getSheet(0);`. Récupérez les valeurs des cellules avec `$cellValue = $sheet->getCell('A1')->getValue();`, qui renvoie le contenu de la cellule spécifiée.

Un exemple pour la lecture :
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('bonjour_monde.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // Affiche "Bonjour"
```
Cela lit la valeur de A1, démontrant la récupération de base.

#### Dépendances et Prérequis
PHPExcel a des prérequis PHP spécifiques et des extensions nécessaires pour son fonctionnement :
- **Version PHP :** Requiert PHP 5.2 ou 7.0 ou supérieur, selon les métadonnées Packagist. Étant donné la date actuelle, le 3 mars 2025, la plupart des installations PHP modernes devraient répondre à cette exigence, mais les configurations plus anciennes peuvent nécessiter des mises à jour.
- **Extensions :** La bibliothèque dépend de `ext-mbstring`, `ext-XML` et `ext-XMLWriter`, qui doivent être activées dans votre configuration PHP. Ces extensions gèrent l'encodage des chaînes, l'analyse XML et l'écriture XML, respectivement, essentielles pour les opérations sur les fichiers Excel.

Les utilisateurs doivent vérifier que ces extensions sont actives en utilisant `phpinfo()` ou en vérifiant le fichier `php.ini`, pour s'assurer qu'aucun problème de compatibilité ne survient.

#### Fonctionnalités Supplémentaires et Formats
Au-delà de la lecture/écriture de base, PHPExcel prend en charge divers formats de fichiers, ce qui est un détail inattendu pour les utilisateurs familiers uniquement avec Excel. La bibliothèque peut gérer :
- Excel 2007 (.xlsx) via le writer/reader 'Excel2007'.
- Excel 95 (.xls) via 'Excel5'.
- Fichiers CSV via 'CSV'.
- HTML via 'HTML'.

Lors de la sauvegarde, spécifiez le type de writer ; lors de la lecture, l'IOFactory détecte souvent automatiquement, mais des readers explicites peuvent être utilisés pour la fiabilité. Par exemple, pour sauvegarder en .xls :
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('nom_du_fichier.xls');
```
Cette flexibilité est utile pour les systèmes hérités ou les besoins de format spécifiques, bien que les utilisateurs doivent noter les limitations potentielles spécifiques au format, en particulier avec les versions Excel plus anciennes.

#### Obsolescence et Conseil de Migration
Un point critique est l'obsolescence de PHPExcel. Les recherches montrent qu'il a été archivé en 2019, avec la dernière mise à jour en 2015, et n'est plus maintenu. Cela soulève des inquiétudes concernant les vulnérabilités de sécurité et la compatibilité avec les versions PHP au-delà de 7.0, en particulier avec les standards modernes comme PHP 8.x. Le dépôt GitHub et la page Packagist recommandent tous deux de migrer vers PhpSpreadsheet, qui offre des namespaces, une conformité PSR et un développement actif.

Pour les utilisateurs, cela signifie :
- Pour les projets existants utilisant PHPExcel 1.8, continuez avec prudence, en assurant des tests pour la sécurité et la compatibilité.
- Pour les nouveaux projets, envisagez fortement PhpSpreadsheet, avec des outils de migration disponibles, comme indiqué dans la documentation de PhpSpreadsheet ([Migration from PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)).

Ce conseil est particulièrement pertinent étant donné la date actuelle, assurant que les utilisateurs s'alignent sur des bibliothèques modernes et supportées.

#### Documentation et Apprentissage Complémentaire
Pour une exploration plus approfondie, la documentation officielle pour PHPExcel est disponible dans son dépôt GitHub sous le dossier Documentation, bien que l'accès puisse nécessiter le téléchargement de fichiers comme la documentation développeur DOC. En ligne, des tutoriels comme celui sur SitePoint ([Generate Excel Files and Charts with PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) fournissent des exemples pratiques, couvrant les graphiques et le formatage, qui vont au-delà de l'utilisation de base. Les fils de discussion Stack Overflow offrent également des insights de la communauté, bien qu'il faille faire attention avec les réponses obsolètes étant donné le statut de la bibliothèque.

#### Tableau Comparatif : PHPExcel vs. PhpSpreadsheet
Pour aider à la prise de décision, voici un tableau comparatif mettant en lumière les différences clés, basé sur les recherches :

| Fonctionnalité           | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| Dernière Mise à Jour     | 2015                              | Actif (en 2025)                 |
| Namespaces               | Non, namespace racine             | Oui, conforme PSR-4             |
| Statut de Maintenance    | Obsolète, archivé 2019            | Activement maintenu             |
| Support des Versions PHP | Jusqu'à 7.0                       | PHP 7.4+                        |
| Support des Formats      | Excel, CSV, HTML, etc.            | Amélioré, incluant ODS, PDF     |
| Performance              | Modérée, gourmande en mémoire     | Optimisée, évolutive           |

Ce tableau souligne le passage à PhpSpreadsheet pour les besoins modernes, bien que PHPExcel reste fonctionnel pour les besoins hérités.

#### Conclusion
Utiliser "phpoffice/phpexcel": "^1.8" implique une installation via Composer, l'utilisation de ses classes pour les opérations Excel et la garantie des extensions PHP requises. Bien que fonctionnelle, son obsolescence nécessite de la prudence, avec PhpSpreadsheet recommandé pour les projets futurs. Ce guide fournit un point de départ complet, avec des exemples, des dépendances et des ressources supplémentaires pour que les utilisateurs puissent explorer plus avant.

### Citations Clés
- [Page Packagist phpoffice/phpexcel avec les détails d'installation](https://packagist.org/packages/phpoffice/phpexcel)
- [Tutoriel SitePoint sur la génération de fichiers Excel avec PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [Statut d'archivage du dépôt GitHub PHPExcel](https://github.com/PHPOffice/PHPExcel)
- [Guide de migration de PhpSpreadsheet depuis PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)