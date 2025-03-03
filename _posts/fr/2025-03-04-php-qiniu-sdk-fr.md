---
audio: false
generated: true
lang: fr
layout: post
title: Qiniu PHP SDK
translated: true
---

Pour utiliser `"qiniu/php-sdk": "^7.0"` en PHP, vous devrez intégrer le SDK PHP de Qiniu dans votre projet. Ce SDK vous permet d'interagir avec les services de stockage cloud de Qiniu, tels que le téléchargement de fichiers, la gestion des buckets, et bien plus encore. Voici un guide étape par étape pour vous aider à démarrer :

---

### 1. Installer le SDK PHP de Qiniu
La méthode recommandée pour installer le SDK est via Composer, un gestionnaire de dépendances pour PHP. Assurez-vous que Composer est installé sur votre système.

#### Étapes :
- Ouvrez votre terminal et naviguez jusqu'à votre répertoire de projet.
- Exécutez la commande suivante pour ajouter le SDK PHP de Qiniu (version 7.x) à votre projet :
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer téléchargera le SDK et ses dépendances dans le répertoire `vendor/` et générera un fichier d'autochargement.

Si vous n'avez pas Composer installé, vous pouvez le télécharger depuis [getcomposer.org](https://getcomposer.org/).

---

### 2. Configurer votre projet
Après l'installation, vous devez inclure l'autoloader dans votre script PHP pour utiliser les classes du SDK.

#### Exemple :
Créez un fichier PHP (par exemple, `index.php`) dans votre répertoire de projet et ajoutez la ligne suivante en haut :
```php
require_once 'vendor/autoload.php';
```

Cela garantit que les classes du SDK sont automatiquement chargées lorsque nécessaire.

---

### 3. Configurer l'authentification
Pour utiliser le SDK de Qiniu, vous aurez besoin de votre `AccessKey` et `SecretKey` de Qiniu, que vous pouvez obtenir depuis votre tableau de bord Qiniu.

#### Exemple :
```php
use Qiniu\Auth;

$accessKey = 'VOTRE_ACCESS_KEY';
$secretKey = 'VOTRE_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

Remplacez `'VOTRE_ACCESS_KEY'` et `'VOTRE_SECRET_KEY'` par vos identifiants réels.

---

### 4. Utilisation de base : Télécharger un fichier
L'une des tâches les plus courantes avec le SDK de Qiniu est de télécharger des fichiers dans un bucket. Voici un exemple de la manière de télécharger un fichier local.

#### Exemple :
```php
use Qiniu\Storage\UploadManager;

$bucket = 'VOTRE_BUCKET_NAME'; // Remplacez par le nom de votre bucket Qiniu
$filePath = '/chemin/vers/votre/fichier.txt'; // Chemin vers le fichier que vous souhaitez télécharger
$key = 'fichier.txt'; // Le nom du fichier dans le stockage Qiniu (peut être null pour utiliser le nom de fichier original)

$token = $auth->uploadToken($bucket); // Générer un jeton de téléchargement
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Téléchargement échoué : " . $error->message();
} else {
    echo "Téléchargement réussi ! Hash du fichier : " . $ret['hash'];
}
```

- `$bucket` : Le nom de votre bucket Qiniu.
- `$filePath` : Le chemin local vers le fichier que vous souhaitez télécharger.
- `$key` : La clé du fichier (nom) sous laquelle il sera stocké dans Qiniu. Si défini à `null`, Qiniu générera une clé basée sur le hash du fichier.
- `$token` : Un jeton de téléchargement généré à l'aide de vos identifiants et du nom du bucket.
- La méthode `putFile` retourne un tableau : `$ret` (informations de succès) et `$error` (informations d'erreur, le cas échéant).

---

### 5. Fonctionnalités supplémentaires
Le SDK PHP de Qiniu fournit de nombreuses autres fonctionnalités, telles que :
- **Gestion des buckets** : Utilisez `Qiniu\Storage\BucketManager` pour lister les fichiers, supprimer les fichiers ou gérer les paramètres du bucket.
- **Opérations sur les fichiers** : Copier, déplacer ou supprimer des fichiers dans votre bucket.
- **Traitement des images** : Générer des URL pour des images redimensionnées ou formatées.

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
- Version PHP : La version du SDK `^7.0` prend en charge PHP 5.3.3 et supérieur (jusqu'à PHP 8.x dans les versions ultérieures).
- Extensions : Assurez-vous que les extensions `cURL` et `xml` PHP sont activées, car elles sont requises par le SDK.

Vous pouvez vérifier votre version PHP et vos extensions avec :
```bash
php -v
php -m
```

---

### 8. Où aller ensuite
- **Documentation** : Pour plus de détails, consultez la [documentation officielle du SDK PHP Qiniu](https://developer.qiniu.com/kodo/sdk/php) ou le [dépôt GitHub](https://github.com/qiniu/php-sdk).
- **Exemples** : Consultez le répertoire `examples/` dans le dépôt GitHub pour plus de cas d'utilisation.
- **Support** : Si vous rencontrez des problèmes, soumettez un ticket au support Qiniu (<support@qiniu.com>) ou posez des questions dans leurs forums communautaires.

---

### Exemple de code complet
Voici un script complet pour télécharger un fichier :
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'VOTRE_ACCESS_KEY';
$secretKey = 'VOTRE_SECRET_KEY';
$bucket = 'VOTRE_BUCKET_NAME';
$filePath = '/chemin/vers/votre/fichier.txt';
$key = 'fichier.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Téléchargement échoué : " . $error->message();
} else {
    echo "Téléchargement réussi ! Hash du fichier : " . $ret['hash'];
}
```

Remplacez les valeurs de substitution (`VOTRE_ACCESS_KEY`, `VOTRE_SECRET_KEY`, `VOTRE_BUCKET_NAME`, `/chemin/vers/votre/fichier.txt`) par vos données réelles, et vous êtes prêt à partir !

Faites-le moi savoir si vous avez besoin d'aide pour une fonctionnalité spécifique !