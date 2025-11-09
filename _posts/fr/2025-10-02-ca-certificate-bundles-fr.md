---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Comprendre les lots de certificats d'autorité de certification
translated: true
type: note
---

### Qu'est-ce que cacert.pem ?

`cacert.pem` (ou des fichiers au nom similaire comme `ca-bundle.crt`, `ca-bundle.pem`, ou `ca-certificates.pem`) fait référence à un fichier contenant un ou plusieurs certificats racines d'Autorité de Certification (CA) au format PEM. PEM signifie Privacy Enhanced Mail, un standard d'encodage textuel (utilisant Base64) qui encapsule les données du certificat entre des en-têtes comme `-----BEGIN CERTIFICATE-----` et `-----END CERTIFICATE-----`.

- **Objectif** : Ces fichiers sont des regroupements de certificats racines de confiance provenant de grandes Autorités de Certification (par exemple, Let's Encrypt, DigiCert, GlobalSign). Ils permettent aux logiciels (comme les navigateurs web, les serveurs ou les outils) de vérifier l'authenticité des certificats SSL/TLS présentés par des sites web ou des serveurs lors de connexions sécurisées (HTTPS).
- **Dans votre exemple** : Le contenu collé est un fichier `ca-bundle.crt` obsolète (datant d'octobre 2012) extrait du navigateur Firefox de Mozilla. Il inclut des certificats racines comme "GTE CyberTrust Global Root" et "Thawte Server CA", qui étaient approuvés à l'époque mais ont depuis expiré ou ont été remplacés. Les regroupements de CA modernes sont mis à jour régulièrement (par exemple, via les mises à jour du système d'exploitation ou les paquets).

De nombreux systèmes et outils utilisent des fichiers similaires :
- Sur Linux : Souvent trouvés à `/etc/ssl/certs/ca-certificates.crt` (Debian/Ubuntu) ou `/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem` (Red Hat).
- Sur macOS : Faisant partie du trousseau du système.
- Sur Windows : Stockés dans le magasin de certificats.

Preuve de leur fiabilité : Les certificats d'AC sont signés par des entités de confiance, et les regroupements comme celui-ci assurent une navigation web sécurisée. Sans eux, la vérification SSL échouerait, risquant des attaques de type man-in-the-middle. Pour les mises à jour, Mozilla publie les données actuelles sur https://wiki.mozilla.org/CA.

### Pourquoi en avons-nous besoin ?

Les regroupements de certificats d'AC sont essentiels pour le chiffrement SSL/TLS (utilisé dans HTTPS, les emails sécurisés, etc.) car ils :
- **Vérifient l'authenticité** : Lorsque vous vous connectez à un site comme https://example.com, le serveur envoie son certificat. Votre client (navigateur, curl, etc.) utilise le regroupement de CA pour vérifier si le certificat est signé par une racine de confiance. Sinon, il avertit ou bloque la connexion.
- **Préviennent les attaques** : Sans vérification, n'importe qui pourrait falsifier des certificats, conduisant à des vulnérabilités comme le hameçonnage ou l'interception de données.
- **Permettent une communication sécurisée** : Ils assurent un chiffrement de bout en bout et la confiance dans les certificats numériques, essentiels pour le commerce électronique, les services bancaires et tout service en ligne.
- **Contexte historique** : Au début des années 1990, SSL a été développé, et les regroupements de CA sont devenus un standard (par exemple, approuvés par les normes IETF comme le RFC 5280 pour les certificats X.509).

Si votre système manque d'un regroupement à jour, les sites sécurisés peuvent afficher des erreurs (par exemple, "certificat non approuvé"). La plupart des systèmes d'exploitation les maintiennent et les mettent à jour automatiquement.

### Comment l'utiliser ?

L'utilisation dépend de l'outil ou du logiciel. Voici des exemples courants :

#### 1. **Avec Curl (Outil en ligne de commande)**
   - Curl utilise les regroupements de CA par défaut (depuis le magasin de votre système), mais vous pouvez spécifier un fichier personnalisé pour la vérification.
   - Exemple : Téléchargez un regroupement personnalisé et utilisez-le pour les requêtes HTTPS.
     ```
     wget https://curl.se/ca/cacert.pem  # Obtenir un regroupement de CA à jour depuis le site de curl
     curl --cacert cacert.pem https://api.github.com  # Vérifier par rapport à ce regroupement
     ```
     - Sans `--cacert`, curl peut charger depuis `/etc/ssl/certs/ca-certificates.crt` sur Linux.

#### 2. **Avec Apache/Nginx (Serveurs Web)**
   - Configurez pour l'authentification par certificat client ou la vérification SSL.
   - Dans le `httpd.conf` d'Apache ou l'hôte virtuel :
     ```
     SSLCACertificateFile /chemin/vers/ca-bundle.crt
     ```
     - Cela indique à Apache d'utiliser le regroupement pour approuver les certificats clients ou vérifier les connexions en amont.

#### 3. **En PHP ou d'autres langages**
   - Pour cURL en PHP :
     ```
     $ch = curl_init();
     curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);  // Activer la vérification
     curl_setopt($ch, CURLOPT_CAINFO, '/chemin/vers/cacert.pem');  // Spécifier le regroupement
     // Faire la requête...
     ```
   - Node.js ou Python (bibliothèque requests) ont des options similaires pour définir des chemins d'AC personnalisés.

#### 4. **Utilisation dans le navigateur**
   - Les navigateurs (Chrome, Firefox) incluent des regroupements de CA intégrés et ne nécessitent généralement pas de configuration manuelle. Vous pouvez ajouter des AC personnalisées via les paramètres si nécessaire (par exemple, pour des sites de développement auto-signés).

#### 5. **Conseils généraux**
   - **Maintenez-le à jour** : Les certificats d'AC expirent ou sont révoqués. Téléchargez des regroupements frais depuis des sources comme https://mkcert.dev (pour le développement) ou votre gestionnaire de paquets (par exemple, `sudo apt-get update ca-certificates` sur Ubuntu).
   - **Note de sécurité** : Utilisez uniquement des regroupements de confiance pour éviter d'accepter des certificats invalides. Pour les tests, vous pouvez créer des certificats auto-signés avec OpenSSL (par exemple, `openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365`).
   - **Vérifiez la validité** : Utilisez `openssl x509 -in cacert.pem -text -noout` pour inspecter les détails d'un certificat.

Si c'est pour une application spécifique, fournissez plus de détails pour un conseil personnalisé ! Si vous voyez des erreurs (par exemple, "SSL certificate verify failed"), cela peut signifier que votre regroupement est obsolète ou manquant.