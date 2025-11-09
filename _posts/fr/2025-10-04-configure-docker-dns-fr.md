---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configurer les serveurs DNS du démon Docker
translated: true
type: note
---

Pour configurer les serveurs DNS du démon Docker (qui seront utilisés par les conteneurs sauf s'ils sont remplacés au niveau du conteneur), vous pouvez éditer le fichier `/etc/docker/daemon.json`. Ce fichier vous permet de personnaliser le comportement d'exécution de Docker.

### Étapes pour configurer le DNS

1. **Éditez le fichier daemon.json** :
   - Si le fichier n'existe pas, créez-le avec les privilèges root (par exemple, en utilisant `sudo nano /etc/docker/daemon.json` ou votre éditeur préféré).
   - Ajoutez ou mettez à jour la clé `dns` en tant que tableau d'adresses IP pour les serveurs DNS. Par exemple, pour utiliser le DNS public de Google (8.8.8.8 et 8.8.4.4) :

     ```json
     {
       "dns": ["8.8.8.8", "8.8.4.4"]
     }
     ```

     - Vous pouvez ajouter plus de serveurs si nécessaire (par exemple, Cloudflare 1.1.1.1).
     - Ce paramètre s'applique à tous les conteneurs créés avec le réseau par défaut, sauf indication contraire.

2. **Validez le JSON** :
   - Assurez-vous que le fichier est un JSON valide. Vous pouvez utiliser un outil comme `jq` pour vérifier : `jq . /etc/docker/daemon.json`. S'il y a une erreur, corrigez la syntaxe.

3. **Redémarrez le service Docker** :
   - Appliquez les changements en redémarrant Docker :
     ```
     sudo systemctl restart docker
     ```
     - Sur les systèmes non systemd (par exemple, les anciennes distributions Linux), utilisez `sudo service docker restart`.
   - Vérifiez le statut : `sudo systemctl status docker`.

4. **Testez la configuration** :
   - Exécutez un conteneur de test et vérifiez sa résolution DNS :
     ```
     docker run --rm busybox nslookup google.com
     ```
     - Il devrait résoudre en utilisant vos serveurs DNS configurés.

### Notes
- **Portée** : Ceci configure le DNS pour le démon Docker sur l'hôte, affectant la résolution de noms sortante pour les conteneurs. Cela ne modifie pas le DNS système de l'hôte.
- **Remplacements** : Si un conteneur a besoin d'un DNS différent (par exemple, via le drapeau `--dns` dans `docker run`), cela remplacera le paramètre au niveau du démon.
- **Sécurité** : Utiliser un DNS public comme 8.8.8.8 convient pour la plupart des cas, mais envisagez un DNS interne pour les environnements d'entreprise.
- **Documentation** : Pour plus d'options (par exemple, les domaines de recherche DNS), consultez la [documentation officielle Docker sur daemon.json](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file).

Si vous rencontrez des erreurs (par exemple, des problèmes de permissions ou d'analyse JSON), partagez les détails pour un dépannage plus approfondi.