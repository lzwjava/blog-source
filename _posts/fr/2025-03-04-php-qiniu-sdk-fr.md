---
audio: false
generated: true
lang: fr
layout: post
title: Kit de Développement PHP Qiniu
translated: true
type: note
---

Pour utiliser `"qiniu/php-sdk": "^7.0"` en PHP, vous devez intégrer le SDK PHP Qiniu dans votre projet. Ce SDK vous permet d'interagir avec les services de stockage cloud Qiniu, tels que le téléchargement de fichiers, la gestion des buckets, et plus encore. Voici un guide étape par étape pour commencer :

---

### 1. Installer le SDK PHP Qiniu
La méthode recommandée pour installer le SDK est via Composer, un gestionnaire de dépendances pour PHP. Assurez-vous d'avoir Composer installé sur votre système.

#### Étapes :
- Ouvrez votre terminal et naviguez vers votre répertoire de projet.
- Exécutez la commande suivante pour ajouter le SDK PHP Qiniu (version 7.x) à votre projet :
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer téléchargera le SDK et ses dépendances dans le répertoire `vendor/` et générera un fichier d'autoload.

Si vous n'avez pas Composer installé, vous pouvez le télécharger depuis [getcomposer.org](https://getcomposer.org/).

---

### 2. Configurer votre projet
Après l'installation, vous devez inclure l'autoloader dans votre script PHP pour utiliser les classes du SDK.

#### Exemple :
Créez un fichier PHP (par exemple, `index.php`) dans votre répertoire de projet et ajoutez la ligne suivante au début :
```php
require_once 'vendor/autoload.php';
```

Cela garantit que les classes du SDK sont automatiquement chargées lorsque nécessaire.

---

### 3. Configurer l'authentification
Pour utiliser le SDK Qiniu, vous aurez besoin de votre `AccessKey` et `SecretKey` Qiniu, que vous pouvez obtenir depuis le tableau de bord de votre compte Qiniu.

#### Exemple :
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

Remplacez `'YOUR_ACCESS_KEY'` et `'YOUR_SECRET_KEY'` par vos véritables identifiants.

---

### 4. Utilisation de base : Télécharger un fichier
L'une des tâches les plus courantes avec le SDK Qiniu est le téléchargement de fichiers vers un bucket. Voici un exemple montrant comment télécharger un fichier local.

#### Exemple :
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // Remplacez par le nom de votre bucket Qiniu
$filePath = '/path/to/your/file.txt'; // Chemin vers le fichier que vous souhaitez télécharger
$key = 'file.txt'; // Le nom du fichier dans le stockage Qiniu (peut être null pour utiliser le nom de fichier original)

$token = $auth->uploadToken($bucket); // Génère un token de téléchargement
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Échec du téléchargement : " . $error->message();
} else {
    echo "Téléchargement réussi ! Hachage du fichier : " . $ret['hash'];
}
```

- `$bucket` : Le nom de votre bucket Qiniu.
- `$filePath` : Le chemin local vers le fichier que vous souhaitez télécharger.
- `$key` : La clé du fichier (nom) sous laquelle il sera stocké dans Qiniu. Si défini sur `null`, Qiniu générera une clé basée sur le hachage du fichier.
- `$token` : Un token de téléchargement généré à l'aide de vos identifiants et du nom du bucket.
- La méthode `putFile` retourne un tableau : `$ret` (informations de succès) et `$error` (informations d'erreur, le cas échéant).

---

### 5. Fonctionnalités supplémentaires
Le SDK PHP Qiniu fournit de nombreuses autres fonctionnalités, telles que :
- **Gestion des Buckets** : Utilisez `Qiniu\Storage\BucketManager` pour lister les fichiers, supprimer des fichiers ou gérer les paramètres du bucket.
- **Opérations sur les fichiers** : Copier, déplacer ou supprimer des fichiers dans votre bucket.
- **Traitement d'image** : Générer des URL pour des images redimensionnées ou formatées.

#### Exemple : Lister les fichiers dans un bucket
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "Erreur : " . $error->message();
} else {
    echo "Fichiers dans le bucket :\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. Gestion des erreurs
Vérifiez toujours la variable `$error` après les opérations du SDK. Si une opération échoue, `$error` contiendra des détails sur ce qui s'est mal passé.

#### Exemple :
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. Prérequis
- Version de PHP : La version du SDK `^7.0` prend en charge PHP 5.3.3 et supérieur (jusqu'à PHP 8.x dans les versions ultérieures).
- Extensions : Assurez-vous que les extensions PHP `cURL` et `xml` sont activées, car elles sont requises par le SDK.

Vous pouvez vérifier votre version de PHP et vos extensions avec :
```bash
php -v
php -m
```

---

### 8. Pour aller plus loin
- **Documentation** : Pour plus de détails, reportez-vous à la [documentation officielle du SDK PHP Qiniu](https://developer.qiniu.com/kodo/sdk/php) ou au [dépôt GitHub](https://github.com/qiniu/php-sdk).
- **Exemples** : Consultez le répertoire `examples/` dans le repo GitHub pour plus de cas d'utilisation.
- **Support** : Si vous rencontrez des problèmes, soumettez un ticket au support Qiniu (<support@qiniu.com>) ou demandez dans leurs forums communautaires.

---

### Exemple de code complet
Voici un script complet pour télécharger un fichier :
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';
$bucket = 'YOUR_BUCKET_NAME';
$filePath = '/path/to/your/file.txt';
$key = 'file.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Échec du téléchargement : " . $error->message();
} else {
    echo "Téléchargement réussi ! Hachage du fichier : " . $ret['hash'];
}
```

Remplacez les valeurs factices (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/path/to/your/file.txt`) par vos données réelles, et vous êtes prêt !

Faites-moi savoir si vous avez besoin d'aide pour une fonctionnalité spécifique !