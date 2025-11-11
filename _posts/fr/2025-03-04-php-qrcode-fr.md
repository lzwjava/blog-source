---
audio: false
generated: true
lang: fr
layout: post
title: Outil PHP de génération de codes QR
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser "endroid/qr-code" version 2.2.2, vous devez l'installer via Composer et vous assurer que l'extension GD est activée.
- Les recherches suggèrent que vous pouvez générer des codes QR en utilisant la classe Builder, en définissant des paramètres comme les données, la taille et le writer, puis en sauvegardant ou affichant le résultat.
- Les preuves tendent à indiquer que la bibliothèque prend en charge les formats PNG, SVG et autres, avec des options pour les logos et les étiquettes, mais il faut vérifier pour la version 2.2.2.

### Installation
Premièrement, installez la bibliothèque en utilisant Composer avec la commande :
```
composer require endroid/qr-code:2.2.2
```
Assurez-vous que votre configuration PHP a l'extension GD activée, car elle est requise pour la génération d'images.

### Exemple d'Utilisation
Voici un exemple basique utilisant la classe Builder, qui est probablement compatible avec la version 2.2.2 :
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Ceci crée un code QR pour une URL et le sauvegarde en tant que fichier PNG. Vous pouvez également l'afficher en tant que data URI pour un affichage web.

### Notes Additionnelles
La bibliothèque prend en charge divers writers (par exemple, PNG, SVG) et permet des personnalisations comme l'ajout de logos ou d'étiquettes. Cependant, étant donné que la version 2.2.2 est ancienne, certaines fonctionnalités présentes dans la documentation actuelle (comme les options avancées pour les logos) pourraient ne pas être disponibles, donc vérifiez la documentation pour cette version spécifique sur [GitHub](https://github.com/endroid/qr-code).

---

### Note d'Enquête : Guide Détaillé sur l'Utilisation de "endroid/qr-code" Version 2.2.2

Cette note fournit un guide complet sur l'utilisation de la bibliothèque "endroid/qr-code", version 2.2.2, pour générer des codes QR dans les applications PHP. Elle développe la réponse directe en incluant tous les détails pertinents de la recherche, assurant une compréhension approfondie pour les développeurs, en particulier ceux qui sont nouveaux avec cette bibliothèque. Le contenu est structuré pour imiter un article professionnel, avec des tableaux pour la clarté et des URL intégrées pour référence ultérieure.

#### Introduction
La bibliothèque "endroid/qr-code" est un outil PHP pour générer des codes QR, largement utilisé pour des applications comme le suivi de produits, la gestion de documents et le marketing. La version 2.2.2, spécifiée dans la requête, est une version ancienne, et bien que la bibliothèque soit notée comme abandonnée sur [Packagist](https://packagist.org/packages/endroid/qr-code), elle reste fonctionnelle pour la génération basique de codes QR. Ce guide décrit l'installation et l'utilisation, en se concentrant sur la garantie de compatibilité avec la version 2.2.2, en reconnaissant les différences potentielles avec les versions plus récentes.

#### Processus d'Installation
Pour commencer, vous devez installer la bibliothèque via Composer, le gestionnaire de paquets PHP. La commande est :
```
composer require endroid/qr-code:2.2.2
```
Ceci garantit que vous obtenez exactement la version 2.2.2. Une exigence critique est l'extension GD pour PHP, qui doit être activée et configurée, car elle est essentielle pour la génération d'images. Sans elle, la bibliothèque ne peut pas produire de codes QR visuels.

| Étape                  | Détails                                                                 |
|------------------------|-------------------------------------------------------------------------|
| Commande d'Installation| `composer require endroid/qr-code:2.2.2`                                |
| Exigence PHP           | Assurez-vous que l'extension GD est activée (vérifiez `phpinfo()` pour confirmation) |

Les recherches indiquent que le dépôt GitHub de la bibliothèque ([GitHub](https://github.com/endroid/qr-code)) et les pages [Packagist](https://packagist.org/packages/endroid/qr-code) confirment cette méthode d'installation, aucune documentation spécifique pour la version 2.2.2 n'ayant été trouvée, suggérant de s'appuyer sur les modèles d'utilisation généraux.

#### Détails d'Utilisation
La bibliothèque offre deux méthodes principales pour la génération de codes QR : utiliser la classe Builder ou directement avec la classe QrCode. Étant donné l'accent de la requête sur l'utilisation, l'approche Builder est recommandée pour sa simplicité, bien que les deux soient détaillées ici pour exhaustivité.

##### Utilisation de la Classe Builder
La classe Builder fournit une interface fluide pour configurer les codes QR. Basé sur des exemples de la documentation récente, une implémentation basique est :
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Ce code crée un code QR pour l'URL, en utilisant le format PNG, avec l'encodage ISO-8859-1 pour une meilleure compatibilité des scanners et une correction d'erreur élevée. Vous pouvez également l'afficher en tant que data URI :
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
Ceci est utile pour l'intégration en HTML, par exemple : `<img src="<?php echo $qrCodeDataUri; ?>">`.

Cependant, étant donné l'ancienneté de la version 2.2.2, certaines classes comme `ErrorCorrectionLevelHigh` pourraient être nommées différemment (par exemple, `ErrorCorrectionLevel::HIGH` dans les versions plus anciennes). Les recherches provenant de publications Stack Overflow ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) suggèrent que les versions plus anciennes utilisaient des méthodes comme `setErrorCorrection('high')`, donc vérifiez l'API pour la 2.2.2.

##### Utilisation Directe de la Classe QrCode
Pour plus de contrôle, vous pouvez utiliser la classe QrCode, comme vu dans les exemples :
```php
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

$qrCode = new QrCode('Life is too short to be generating QR codes');
$qrCode->setSize(300);
$qrCode->setMargin(10);
$writer = new PngWriter();
$result = $writer->write($qrCode);
$result->saveToFile('qrcode.png');
```
Cette méthode est plus verbeuse mais permet un réglage fin, tel que la définition des couleurs de premier plan et d'arrière-plan, ce qui pourrait être pertinent pour la version 2.2.2. Encore une fois, vérifiez la documentation pour la disponibilité des méthodes.

#### Options de Configuration
La bibliothèque prend en charge divers writers pour différents formats de sortie, comme détaillé dans le tableau ci-dessous, basé sur la documentation actuelle, avec une note pour vérifier pour la version 2.2.2 :

| Classe de Writer       | Format   | Notes                                                                 |
|------------------------|----------|----------------------------------------------------------------------|
| PngWriter              | PNG      | Niveau de compression configurable, défaut -1                           |
| SvgWriter              | SVG      | Adapté aux graphiques vectoriels, pas d'options de compression        |
| WebPWriter             | WebP     | Qualité 0-100, défaut 80, bon pour une utilisation web               |
| PdfWriter              | PDF      | Unité en mm, défaut, bon pour l'impression                           |

Les options d'encodage incluent UTF-8 (défaut) et ISO-8859-1, cette dernière étant recommandée pour la compatibilité avec les scanners de codes-barres. Les modes de taille de bloc rond (marge, agrandir, réduire, aucun) peuvent améliorer la lisibilité, mais leur disponibilité dans la 2.2.2 doit être confirmée.

#### Fonctionnalités Avancées et Considérations
Pour une utilisation avancée, telle que l'intégration de logos, la classe Builder prend en charge des méthodes comme `logoPath()` et `logoResizeToWidth()`, comme vu dans un article Medium ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)). Cependant, celles-ci pourraient être des ajouts postérieurs à la 2.2.2, donc testez la compatibilité. La validation des codes QR générés est possible mais impacte les performances et est désactivée par défaut, un détail provenant de [GitHub](https://github.com/endroid/qr-code).

Étant donné la note d'abandon de la bibliothèque sur [Packagist](https://packagist.org/packages/endroid/qr-code), il est important de noter les préoccupations potentielles de sécurité ou de maintenance, bien que pour une utilisation basique, elle reste viable. Pour les utilisateurs de Symfony, il existe un bundle ([GitHub](https://github.com/endroid/qr-code-bundle)), mais cela dépasse l'utilisation PHP générale.

#### Notes Spécifiques à la Version
La recherche n'a montré aucune documentation directe pour la version 2.2.2, les tags GitHub ne la listant pas, suggérant qu'il pourrait s'agir d'une version plus ancienne ou d'une faute de frappe. Le dépôt actuel montre des versions allant jusqu'à la 6.0.0, et [Packagist](https://packagist.org/packages/endroid/qr-code) la liste comme abandonnée, recommandant endroid/qr-code, ce qui est déroutant car c'est le même paquet. Ceci indique des problèmes potentiels de renommage ou de versionnage, donc les utilisateurs devraient verrouiller les dépendances et tester les mises à niveau.

#### Conclusion
Utiliser "endroid/qr-code" version 2.2.2 implique une installation via Composer, la garantie de l'extension GD, et la génération de codes QR avec la classe Builder ou QrCode. Bien que les exemples soient basés sur la documentation actuelle, vérifiez les différences d'API pour la 2.2.2, en particulier pour les fonctionnalités avancées. Pour plus de détails, consultez la page GitHub de la bibliothèque et les discussions Stack Overflow associées.

#### Citations Clés
- [Dépôt GitHub du Générateur de Code QR](https://github.com/endroid/qr-code)
- [Page Packagist de endroid/qr-code](https://packagist.org/packages/endroid/qr-code)
- [Article Medium sur la Création de Codes QR avec Images Intégrées](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Discussion Stack Overflow sur Endroid QR Code](https://stackoverflow.com/questions/40777377/endroid-qr-code)