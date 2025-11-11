---
audio: false
generated: true
lang: fr
layout: post
title: Gestionnaire d'identification Git Diagnostiquer
translated: true
type: note
---

La sortie de `git credential-manager diagnose` indique désormais clairement un **échec réseau**, en plus de l'avertissement de vérification du certificat TLS. Décomposons l'erreur et comment la résoudre :

**Principales Constatations :**

*   **Échec Réseau :**
    * Le test de diagnostic a échoué avec l'erreur : `System.Net.Http.HttpRequestException: nodename nor servname provided, or not known (example.com:443)`.
    * Cette erreur signifie que le Gestionnaire d'Informations d'Identification Git n'a pas pu résoudre le nom d'hôte `example.com` en une adresse IP, ou qu'il n'a pas pu se connecter au port 443 sur cet hôte.
    * Le journal de diagnostic montre que la requête HEAD vers `https://example.com` a échoué.
*   **Interférence du Proxy (Cause Probable) :**
    * La présence de `HTTP_PROXY: http://127.0.0.1:7890` et `HTTPS_PROXY: http://127.0.0.1:7890` suggère fortement que le proxy est la cause racine de l'échec réseau.
    * Le fait que le diagnostic puisse accéder à [http://httpforever.com](http://httpforever.com), mais pas à [https://example.com](https://example.com), indique que le proxy rencontre des problèmes avec les requêtes https.
*   **Vérification du Certificat TLS Désactivée (Risque de Sécurité) :**
    * Comme précédemment, la vérification du certificat TLS est désactivée, ce qui est un problème de sécurité majeur.

**Étapes de Dépannage :**

1.  **Vérification du Proxy :**
    * **Tester le Proxy :** Ouvrez un navigateur web et essayez d'accéder directement à `https://example.com`. Si vous rencontrez une erreur "impossible de se connecter" ou "nom d'hôte non trouvé", votre proxy est probablement mal configuré.
    * **Problèmes Logiciels de Proxy :**
        * Redémarrez votre logiciel proxy (Shadowsocks, Clash, etc.).
        * Vérifiez les journaux du logiciel proxy pour des messages d'erreur.
        * Assurez-vous que le proxy est configuré pour gérer correctement le trafic HTTPS.
        * Assurez-vous que le logiciel proxy est en cours d'exécution.
    * **Configuration du Proxy :**
        * Vérifiez doublement les paramètres de proxy dans les préférences réseau de votre système d'exploitation et dans tous les fichiers de configuration Git.
        * Vérifiez que l'adresse du proxy (`127.0.0.1`) et le port (`7890`) sont corrects.
        * Désactivez temporairement le proxy dans les paramètres réseau de votre système d'exploitation, et relancez la commande `git credential-manager diagnose`.
2.  **Résolution DNS :**
    * Bien que le message d'erreur suggère un problème de résolution de nom d'hôte, le proxy est le coupable le plus probable. Cependant, il vaut toujours la peine de vérifier vos paramètres DNS.
    * Essayez d'utiliser un serveur DNS public (par exemple, 8.8.8.8, 1.1.1.1).
3.  **Vérification du Certificat TLS :**
    * **Réactiver la Vérification du Certificat :** Ceci est crucial pour la sécurité. Suivez les instructions fournies dans le lien `https://aka.ms/gcm/tlsverify`.
    * Si votre logiciel proxy est conçu pour intercepter le trafic HTTPS, assurez-vous d'installer le certificat racine du proxy dans le magasin de certificats racines de confiance de votre système d'exploitation. C'est la méthode sécurisée pour permettre au proxy de fonctionner.
4.  **Configuration Git :**
    * Exécutez `git config --global --list` pour examiner votre configuration Git.
    * Supprimez temporairement les paramètres de proxy de Git pour isoler le problème :
        ```bash
        git config --global --unset http.proxy
        git config --global --unset https.proxy
        ```
    * Après avoir supprimé les paramètres du proxy, relancez la commande `git credential-manager diagnose`.
5.  **Pare-feu :**
    * Désactivez temporairement tous les pare-feux sur votre ordinateur, pour éliminer toute interférence de pare-feu.
6.  **Connexion Réseau :**
    * Testez votre connexion réseau en utilisant d'autres applications réseau, pour vous assurer que le réseau lui-même est stable.
    * Si vous utilisez un point d'accès mobile, déplacez-vous vers un endroit avec une meilleure force du signal.

**Conclusion Principale :** Le proxy cause presque certainement les échecs réseau. Configurer correctement le proxy et réactiver la vérification du certificat TLS sont les étapes les plus importantes.