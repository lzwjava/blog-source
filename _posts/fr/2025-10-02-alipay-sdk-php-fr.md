---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide d'intégration PHP du SDK Alipay
translated: true
type: note
---

### Prérequis
Pour intégrer le SDK Alipay en PHP, vous aurez besoin de :
- Un compte marchand Alipay valide (inscrivez-vous sur https://open.alipay.com).
- Des paires de clés RSA : Générez une clé privée pour votre serveur et téléchargez la clé publique sur Alipay pour signer les transactions.
- PHP 5.6+ (de préférence 7.x pour une meilleure sécurité), avec des extensions comme cURL et OpenSSL activées.
- Téléchargez le SDK Alipay depuis leur GitHub officiel (par exemple, https://github.com/alipay/alipay-sdk-php) – notez que l'extrait de code fourni semble être pour une version plus ancienne (~2016) ; le dernier SDK utilise des API plus récentes comme les API Alipay Trade. Si vous utilisez l'ancien paiement mobile de sécurité, il peut encore fonctionner mais est déprécié.

### Configuration du SDK
1. **Téléchargement et Inclusion** : Téléchargez le ZIP du SDK depuis le portail développeur d'Alipay ou GitHub. Extrayez-le dans votre répertoire de projet (par exemple, `vendor/alipay-sdk`).
2. **Inclusion des Fichiers** : Dans votre script PHP, incluez le fichier SDK principal, par exemple :
   ```php
   require_once 'chemin/vers/alipay-sdk/AopClient.php'; // Pour le SDK moderne
   ```
   Pour la version héritée dans votre extrait, vous pourriez avoir besoin d'inclusions personnalisées comme `AopSdk.php`.

3. **Configuration des Clés et du Compte** :
   - Générez les clés RSA (2048 bits) en utilisant des commandes OpenSSL ou des outils en ligne. Exemple :
     ```bash
     openssl genrsa -out private_key.pem 2048
     openssl rsa -in private_key.pem -pubout -out public_key.pem
     ```
   - Remplissez le tableau `$config` comme indiqué dans votre extrait :
     - `partner` : Votre identifiant partenaire Alipay (16 chiffres commençant par 2088).
     - `private_key` : Votre clé privée encodée PEM (brute, sans en-têtes comme -----BEGIN PRIVATE KEY-----).
     - `alipay_public_key` : La clé publique d'Alipay (copiez-la depuis votre console Alipay).
     - Autres champs : Utilisez HTTPS pour `transport`, et placez `cacert.pem` (téléchargeable depuis la documentation Alipay) dans le répertoire du script pour la vérification SSL.

### Initialisation du SDK
Créez une instance AopClient et transmettez la configuration :
```php
use Orvibo\AopSdk\AopClient; // Ajustez le namespace pour votre version du SDK

$aopClient = new AopClient();
$aopClient->gatewayUrl = 'https://openapi.alipay.com/gateway.do'; // URL de production
$aopClient->appId = 'your_app_id'; // Le SDK plus récent utilise appId au lieu de partner
$aopClient->rsaPrivateKey = $config['private_key'];
$aopClient->alipayrsaPublicKey = $config['alipay_public_key'];
$aopClient->apiVersion = '1.0';
$aopClient->signType = 'RSA2'; // Le SDK moderne préfère RSA2
$aopClient->postCharset = $config['input_charset'];
$aopClient->format = 'json';
```

Pour l'ancien paiement mobile comme dans votre extrait, vous utiliseriez des classes plus anciennes comme `AlipaySign`.

### Création d'une Demande de Paiement
1. **Construction des Paramètres de la Demande** :
   ```php
   $request = new AlipayTradeAppPayRequest(); // Ou similaire pour votre version du SDK
   $request->setBizContent("{" .
       "\"body\":\"Test transaction\"," .
       "\"subject\":\"Test Subject\"," .
       "\"out_trade_no\":\"123456789\"," .
       "\"timeout_express\":\"30m\"," .
       "\"total_amount\":\"0.01\"," .
       "\"product_code\":\"QUICK_MSECURITY_PAY\"" .
       "}");
   $request->setNotifyUrl($config['service']); // Votre URL de notification
   ```

2. **Exécution de la Demande** :
   ```php
   $response = $aopClient->sdkExecute($request);
   echo $response; // Cette chaîne signée est utilisée dans le SDK Alipay de votre application
   ```

3. **Dans Votre Application Mobile (si intégration avec une app)** : Transmettez la réponse au SDK Alipay natif de votre application (par exemple, Android/iOS) pour finaliser le paiement.

### Gestion des Notifications et Réponses
- **Notifications Asynchrones** : Configurez un script PHP de rappel à l'`notify_url` pour vérifier les notifications d'Alipay.
  ```php
  $aopClient->rsaCheckV1($_POST, $alipayPublicKey, 'RSA2'); // Vérifier la signature
  // Traiter le statut du paiement (par exemple, mettre à jour la base de données)
  ```
- **Retour Synchrone** : Après le paiement, Alipay redirige vers votre `return_url` (si défini).

### Tests et Déploiement
- Utilisez l'environnement sandbox d'Alipay pour les tests : https://openhome.alipay.com/platform/devEnv.htm.
- Problèmes courants : Assurez-vous que les clés sont correctement formatées (pas de lignes supplémentaires). Utilisez RSA2 pour une meilleure sécurité.
- Conseils de Sécurité : Stockez les clés de manière sécurisée (pas dans le contrôle de version). Vérifiez toujours les signatures pour empêcher la falsification.

S'il s'agit de l'ancien SDK, envisagez de passer à la dernière version du SDK PHP d'Alipay (par exemple, via Composer : `composer require alipay/openapisdk`) pour de meilleures fonctionnalités et une sécurité accrue. Pour la documentation détaillée, visitez https://docs.open.alipay.com/. Si vous rencontrez des erreurs, partagez votre code et vos journaux pour le dépannage.