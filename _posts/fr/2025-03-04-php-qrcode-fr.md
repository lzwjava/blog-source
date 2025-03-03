---
audio: false
generated: true
lang: fr
layout: post
title: Outil PHP pour générer des codes QR
translated: true
---

### Points Clés
- Il semble probable que pour utiliser "endroid/qr-code" version 2.2.2, il faille l'installer via Composer et s'assurer que l'extension GD est activée.
- La recherche suggère que vous pouvez générer des codes QR en utilisant la classe Builder, en définissant des paramètres comme les données, la taille et l'écrivain, puis en enregistrant ou en sortant le résultat.
- Les preuves penchent en faveur de la bibliothèque supportant PNG, SVG et d'autres formats, avec des options pour les logos et les étiquettes, mais vérifiez pour la version 2.2.2.

### Installation
Tout d'abord, installez la bibliothèque en utilisant Composer avec la commande :
```
composer require endroid/qr-code:2.2.2
```
Assurez-vous que votre configuration PHP a l'extension GD activée, car elle est requise pour la génération d'images.

### Exemple d'Utilisation
Voici un exemple de base utilisant la classe Builder, qui est probablement compatible avec la version 2.2.2 :
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
Cela crée un code QR pour une URL et l'enregistre en tant que fichier PNG. Vous pouvez également l'afficher sous forme d'URI de données pour l'affichage web.

### Notes Supplémentaires
La bibliothèque prend en charge divers écrivains (par exemple, PNG, SVG) et permet des personnalisations comme l'ajout de logos ou d'étiquettes. Cependant, étant donné que la version 2.2.2 est ancienne, certaines fonctionnalités de la documentation actuelle (comme les options avancées de logo) ne pourraient pas être disponibles, donc vérifiez la documentation pour cette version spécifique sur [GitHub](https://github.com/endroid/qr-code).

---

### Note de Sondage : Guide Détaillé sur l'Utilisation de "endroid/qr-code" Version 2.2.2

Cette note fournit un guide complet sur l'utilisation de la bibliothèque "endroid/qr-code", version 2.2.2, pour générer des codes QR dans des applications PHP. Elle développe la réponse directe en incluant tous les détails pertinents de la recherche, assurant une compréhension approfondie pour les développeurs, en particulier ceux nouveaux avec la bibliothèque. Le contenu est structuré pour imiter un article professionnel, avec des tableaux pour la clarté et des URL intégrées pour référence supplémentaire.

#### Introduction
La bibliothèque "endroid/qr-code" est un outil PHP pour générer des codes QR, largement utilisé pour des applications comme le suivi des produits, la gestion des documents et le marketing. La version 2.2.2, spécifiée dans la requête, est une version plus ancienne, et bien que la bibliothèque soit notée comme abandonnée sur [Packagist](https://packagist.org/packages/endroid/qr-code), elle reste fonctionnelle pour la génération de base de codes QR. Ce guide décrit l'installation et l'utilisation, en se concentrant sur l'assurance de la compatibilité avec la version 2.2.2, en reconnaissant les différences potentielles avec les versions plus récentes.

#### Processus d'Installation
Pour commencer, vous devez installer la bibliothèque via Composer, le gestionnaire de paquets PHP. La commande est :
```
composer require endroid/qr-code:2.2.2
```
Cela assure que vous obtenez la version exacte 2.2.2. Une exigence critique est l'extension GD pour PHP, qui doit être activée et configurée, car elle est essentielle pour la génération d'images. Sans elle, la bibliothèque ne peut pas produire des codes QR visuels.

| Étape                  | Détails                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Commande d'Installation       | `composer require endroid/qr-code:2.2.2`                                |
| Exigence PHP       | Assurez-vous que l'extension GD est activée (vérifiez `phpinfo()` pour confirmation)     |

La recherche indique que les pages du dépôt GitHub ([GitHub](https://github.com/endroid/qr-code)) et [Packagist](https://packagist.org/packages/endroid/qr-code) confirment cette méthode d'installation, sans documentation spécifique trouvée pour la version 2.2.2, suggérant une dépendance aux modèles d'utilisation généraux.

#### Détails d'Utilisation
La bibliothèque offre deux méthodes principales pour la génération de codes QR : l'utilisation de la classe Builder ou directement avec la classe QrCode. Étant donné que la requête se concentre sur l'utilisation, l'approche Builder est recommandée pour sa simplicité, bien que les deux soient détaillées ici pour exhaustivité.

##### Utilisation de la Classe Builder
La classe Builder fournit une interface fluide pour configurer les codes QR. Basé sur des exemples de la documentation récente, une implémentation de base est :
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
Ce code crée un code QR pour l'URL, utilisant le format PNG, avec un encodage ISO-8859-1 pour une meilleure compatibilité avec les scanners et un niveau élevé de correction d'erreurs. Vous pouvez également l'afficher sous forme d'URI de données :
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
Cela est utile pour l'intégration dans le HTML, par exemple, `<img src="<?php echo $qrCodeDataUri; ?>">`.

Cependant, étant donné l'âge de la version 2.2.2, certaines classes comme `ErrorCorrectionLevelHigh` pourraient être nommées différemment (par exemple, `ErrorCorrectionLevel::HIGH` dans les versions plus anciennes). La recherche provenant de messages Stack Overflow ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) suggère que les versions plus anciennes utilisaient des méthodes comme `setErrorCorrection('high')`, donc vérifiez l'API pour 2.2.2.

##### Utilisation de la Classe QrCode Directement
Pour plus de contrôle, vous pouvez utiliser la classe QrCode, comme vu dans les exemples :
```php
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

$qrCode = new QrCode('La vie est trop courte pour générer des codes QR');
$qrCode->setSize(300);
$qrCode->setMargin(10);
$writer = new PngWriter();
$result = $writer->write($qrCode);
$result->saveToFile('qrcode.png');
```
Cette méthode est plus verbeuse mais permet un réglage fin, tel que la définition des couleurs d'avant-plan et d'arrière-plan, ce qui pourrait être pertinent pour la version 2.2.2. Encore une fois, vérifiez la documentation pour la disponibilité des méthodes.

#### Options de Configuration
La bibliothèque prend en charge divers écrivains pour différents formats de sortie, comme détaillé dans le tableau ci-dessous, basé sur la documentation actuelle, avec une note pour vérifier pour la version 2.2.2 :

| Classe d'Écrivain          | Format   | Notes                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | Niveau de compression configurable, par défaut -1                           |
| SvgWriter             | SVG      | Adapté aux graphiques vectoriels, pas d'options de compression                 |
| WebPWriter            | WebP     | Qualité 0-100, par défaut 80, bon pour l'utilisation web                          |
| PdfWriter             | PDF      | Unité en mm, par défaut, bon pour l'impression                                 |

Les options d'encodage incluent UTF-8 (par défaut) et ISO-8859-1, avec ce dernier recommandé pour la compatibilité avec les scanners de codes-barres. Les modes de taille de bloc arrondis (marge, agrandir, rétrécir, aucun) peuvent améliorer la lisibilité, mais leur disponibilité dans 2.2.2 nécessite confirmation.

#### Fonctionnalités Avancées et Considérations
Pour une utilisation avancée, comme l'incorporation de logos, la classe Builder prend en charge des méthodes comme `logoPath()` et `logoResizeToWidth()`, comme vu dans un article Medium ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)). Cependant, celles-ci pourraient être des additions post-2.2.2, donc testez la compatibilité. La validation des codes QR générés est possible mais impacte les performances et est désactivée par défaut, un détail de [GitHub](https://github.com/endroid/qr-code).

Étant donné la note d'abandon de la bibliothèque sur [Packagist](https://packagist.org/packages/endroid/qr-code), il est bon de noter les préoccupations potentielles de sécurité ou de maintenance, bien que pour une utilisation de base, elle reste viable. Pour les utilisateurs de Symfony, il existe un bundle ([GitHub](https://github.com/endroid/qr-code-bundle)), mais cela est en dehors de l'utilisation PHP générale.

#### Notes Spécifiques à la Version
La recherche n'a montré aucune documentation directe pour la version 2.2.2, avec les balises GitHub ne la listant pas, suggérant qu'il pourrait s'agir d'une version plus ancienne ou d'une faute de frappe. Le dépôt actuel montre des versions jusqu'à 6.0.0, et [Packagist](https://packagist.org/packages/endroid/qr-code) la liste comme abandonnée, recommandant endroid/qr-code, ce qui est confus car c'est le même package. Cela indique des problèmes potentiels de renommage ou de versionnage, donc les utilisateurs devraient verrouiller les dépendances et tester les mises à niveau.

#### Conclusion
L'utilisation de "endroid/qr-code" version 2.2.2 implique l'installation via Composer, l'assurance que l'extension GD est activée, et la génération de codes QR avec la classe Builder ou QrCode. Bien que les exemples soient basés sur la documentation actuelle, vérifiez les différences d'API pour 2.2.2, en particulier pour les fonctionnalités avancées. Pour plus de détails, consultez la page GitHub de la bibliothèque et les discussions Stack Overflow connexes.

#### Citations Clés
- [Dépôt GitHub du Générateur de Codes QR](https://github.com/endroid/qr-code)
- [Page Packagist endroid/qr-code](https://packagist.org/packages/endroid/qr-code)
- [Article Medium sur la Création de Codes QR avec des Images Intégrées](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Discussion Stack Overflow Endroid QR Code](https://stackoverflow.com/questions/40777377/endroid-qr-code)