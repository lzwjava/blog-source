---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Configuration des délais d'attente HTTP et de Keep-Alive pour Liberty
translated: true
type: note
---

### Configuration des paramètres Keep-Alive

Le profil WebSphere Liberty gère les connexions HTTP keep-alive via l'élément `<httpEndpoint>` dans `server.xml`. Cet élément contrôle les connexions persistantes pour réduire la latence et la surcharge.

- **keepAlive** : Active ou désactive le keep-alive. Définissez sur `true` (par défaut) pour autoriser plusieurs requêtes sur une seule connexion.
- **keepAliveTimeout** : Définit le temps (en secondes) que le serveur attend avant de fermer une connexion keep-alive inactive. La valeur par défaut est de 30 secondes.

Pour configurer, ajoutez ou modifiez l'élément `<httpEndpoint>` sous la racine `<server>` dans `server.xml`. Exemple :

```xml
<server>
    <!-- Autres configurations -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        keepAlive="true"
        keepAliveTimeout="60"/>
</server>
```

Redémarrez le serveur pour que les modifications prennent effet. Les keep-alives au niveau TCP peuvent être ajustés via `<tcpOptions>` si nécessaire, mais le keep-alive HTTP est plus courant pour le trafic web.

### Configuration des paramètres de Timeout

Les timeouts dans `server.xml` de Liberty concernent principalement les timeouts de connexion sous `<httpEndpoint>`, contrôlant le temps que le serveur attend pour les opérations. Ceux-ci s'appliquent à la communication HTTP.

- **connectionTimeout** : Temps maximum (en secondes) pour établir une nouvelle connexion. La valeur par défaut est de 60 secondes.
- **readTimeout** : Temps maximum (en secondes) pour attendre les données entrantes pendant une requête. La valeur par défaut est de 60 secondes.
- **writeTimeout** : Temps maximum (en secondes) pour attendre l'envoi des données sortantes. La valeur par défaut est de 60 secondes.

Les timeouts spécifiques aux sessions (par exemple, pour les sessions d'application web) sont configurés dans `web.xml` ou via `<sessionManager>` dans `server.xml`, et non directement dans `<httpEndpoint>`.

Exemple de configuration `server.xml` :

```xml
<server>
    <!-- Autres configurations -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        connectionTimeout="30"
        readTimeout="120"
        writeTimeout="120"/>
</server>
```

Ajustez les valeurs en fonction des besoins de votre application, comme des timeouts plus élevés pour les réseaux lents ou les requêtes longues. Surveillez les journaux pour les erreurs liées aux timeouts et redémarrez le serveur après les modifications. Pour plus de détails, consultez la [documentation IBM Liberty sur les points de terminaison HTTP](https://www.ibm.com/docs/en/was-liberty/23.0.0?topic=configuration-http-endpoint-running-liberty).