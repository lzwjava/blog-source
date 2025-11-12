---
audio: false
generated: true
lang: fr
layout: post
title: Développement d'un client Shadowsocks avec Netty
translated: true
type: note
---

Construire un client Shadowsocks comme Clash ou le client Shadowsocks original en utilisant Netty implique de comprendre le protocole Shadowsocks et de tirer parti du framework d'application réseau asynchrone et orienté événements de Netty. Voici une décomposition des étapes et des concepts clés impliqués :

**1. Comprendre le protocole Shadowsocks**

Avant de plonger dans Netty, vous devez comprendre parfaitement le protocole Shadowsocks. Globalement, il implique :

* **Établissement de la connexion :** Un client initie une connexion vers un serveur Shadowsocks.
* **Authentification et Négociation de Méthode :** Le client envoie la méthode de chiffrement choisie et le mot de passe au serveur pour authentification.
* **Encodage d'Adresse :** Le client envoie l'adresse cible (adresse IP et port) du serveur de destination réel dans un format encodé spécifique.
* **Transfert de Données :** Après une authentification et un encodage d'adresse réussis, toutes les données échangées ultérieurement entre le client et le serveur Shadowsocks sont chiffrées/déchiffrées en utilisant la méthode convenue.

**Aspects clés du protocole que vous devrez implémenter :**

* **Gestion de la Méthode et du Mot de Passe :** Stocker et envoyer la méthode de chiffrement choisie (par exemple, `aes-256-cfb`, `chacha20-ietf-poly1305`) et le mot de passe.
* **Encodage d'Adresse :** Encoder l'adresse cible dans un format spécifique (octet de type, adresse, port). L'octet de type indique si l'adresse est une adresse IPv4 (0x01), une adresse IPv6 (0x04) ou un nom d'hôte (0x03).
* **Chiffrement et Déchiffrement :** Implémenter les algorithmes de chiffrement et de déchiffrement choisis. Des bibliothèques comme `PyCryptodome` (Python) ou `Bouncy Castle` (Java) peuvent être utiles pour cela.
* **Transfert TCP :** Établir un serveur TCP local qui écoute les connexions des applications et transfère le trafic via le tunnel Shadowsocks.

**2. Configuration d'un projet Netty**

Vous devrez d'abord inclure la dépendance Netty dans votre projet (par exemple, en utilisant Maven ou Gradle pour un projet Java).

**3. Composants Netty de base pour un client proxy**

Vous utiliserez principalement les composants Netty suivants :

* **`Bootstrap` :** Utilisé pour configurer et démarrer l'application côté client.
* **`EventLoopGroup` :** Gère les boucles d'événements qui traitent les opérations d'E/S pour le client. Vous utiliserez généralement `NioEventLoopGroup` pour les E/S non bloquantes.
* **`Channel` :** Représente une connexion réseau.
* **`ChannelPipeline` :** Une chaîne de `ChannelHandler`s qui traitent les événements et données entrants et sortants.
* **`ChannelHandler` :** Interfaces que vous implémentez pour gérer des événements et transformations de données spécifiques. Vous créerez des gestionnaires personnalisés pour le protocole Shadowsocks.
* **`ByteBuf` :** Le tampon de Netty pour gérer les données binaires.

**4. Implémentation du protocole Shadowsocks avec les gestionnaires Netty**

Vous devrez créer plusieurs `ChannelHandler`s personnalisés dans votre `ChannelPipeline` pour implémenter la logique Shadowsocks. Voici une structure possible :

* **Gestionnaire du Serveur Proxy Local (`ChannelInboundHandlerAdapter`) :**
    * Ce gestionnaire s'exécutera sur un socket serveur local auquel vos applications se connecteront (par exemple, `localhost:1080`).
    * Lorsqu'une nouvelle connexion arrive d'une application locale, ce gestionnaire :
        * Établit une connexion vers le serveur Shadowsocks distant.
        * Transfère la demande de connexion initiale (adresse cible) au serveur Shadowsocks après l'avoir encodée selon le protocole.
        * Gère le flux de données entre l'application locale et le serveur Shadowsocks.

* **Encodeur du Client Shadowsocks (`ChannelOutboundHandlerAdapter`) :**
    * Ce gestionnaire sera responsable de l'encodage des données envoyées au serveur Shadowsocks.
    * Il devra :
        * Encoder l'adresse cible selon le protocole Shadowsocks (type, adresse, port).
        * Chiffrer les données en utilisant la méthode de chiffrement choisie.

* **Décodeur du Client Shadowsocks (`ChannelInboundHandlerAdapter`) :**
    * Ce gestionnaire sera responsable du décodage des données reçues du serveur Shadowsocks.
    * Il devra :
        * Déchiffrer les données reçues.

* **Gestionnaire de Transfert vers le Serveur Distant (`ChannelInboundHandlerAdapter`) :**
    * Ce gestionnaire sera invoqué lorsque des données sont reçues du serveur Shadowsocks distant.
    * Il transférera les données déchiffrées vers l'application locale d'origine.

**5. Exemple de structure du pipeline Netty**

Voici un exemple simplifié de la façon dont votre `ChannelPipeline` pourrait ressembler pour la connexion au serveur Shadowsocks :

```java
public class ShadowsocksClientInitializer extends ChannelInitializer<SocketChannel> {

    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClientInitializer(String serverAddress, int serverPort, String method, String password) {
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // Gestionnaires sortants (données allant vers le serveur Shadowsocks)
        pipeline.addLast("encoder", new ShadowsocksClientEncoder(method, password));

        // Gestionnaires entrants (données provenant du serveur Shadowsocks)
        pipeline.addLast("decoder", new ShadowsocksClientDecoder(method, password));
        pipeline.addLast("remoteForwarder", new RemoteServerForwardingHandler());
    }
}
```

Et pour le serveur proxy local :

```java
public class LocalProxyInitializer extends ChannelInitializer<SocketChannel> {

    private final String shadowsocksServerAddress;
    private final int shadowsocksServerPort;
    private final String method;
    private final String password;

    public LocalProxyInitializer(String shadowsocksServerAddress, int shadowsocksServerPort, String method, String password) {
        this.shadowsocksServerAddress = shadowsocksServerAddress;
        this.shadowsocksServerPort = shadowsocksServerPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // Gestionnaire pour initier la connexion au serveur Shadowsocks et transférer les données
        pipeline.addLast("localProxyHandler",
                new LocalProxyHandler(shadowsocksServerAddress, shadowsocksServerPort, method, password));
    }
}
```

**6. Détails d'implémentation clés**

* **Implémentation du Chiffrement/Déchiffrement :** Vous devrez implémenter les algorithmes de chiffrement et de déchiffrement choisis dans votre `ShadowsocksClientEncoder` et `ShadowsocksClientDecoder`. Cela impliquera probablement l'utilisation de bibliothèques externes. Soyez prudent avec la dérivation de clé et les vecteurs d'initialisation si requis par la méthode choisie.
* **Encodage d'Adresse dans `LocalProxyHandler` :** Lorsque le `LocalProxyHandler` reçoit la demande de connexion initiale de l'application locale, il doit extraire l'adresse et le port cibles et les encoder dans le format Shadowsocks avant de les envoyer au serveur Shadowsocks.
* **Connexion au Serveur Shadowsocks dans `LocalProxyHandler` :** Le `LocalProxyHandler` utilisera un `Bootstrap` Netty séparé pour établir une connexion au serveur Shadowsocks configuré.
* **Transfert de Données :** Une fois la connexion au serveur Shadowsocks établie, les gestionnaires doivent transférer efficacement les données entre la connexion de l'application locale et la connexion du serveur Shadowsocks. Vous devrez probablement gérer les objets `Channel` pour les deux connexions.
* **Gestion des Erreurs :** Implémentez une gestion appropriée des erreurs pour les problèmes réseau, les erreurs de protocole et les échecs de chiffrement/déchiffrement.
* **Concurrence :** Netty gère la concurrence efficacement avec son modèle de boucle d'événements. Assurez-vous que vos gestionnaires sont conçus pour être thread-safe si vous devez partager un état.

**7. Démarrage du client proxy**

Vous devrez créer une classe principale pour démarrer le serveur proxy local (écoutant les connexions locales) et potentiellement gérer la configuration.

```java
public class ShadowsocksClient {

    private final int localPort;
    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClient(int localPort, String serverAddress, int serverPort, String method, String password) {
        this.localPort = localPort;
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    public void run() throws Exception {
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();

        try {
            ServerBootstrap b = new ServerBootstrap();
            b.group(bossGroup, workerGroup)
             .channel(NioServerSocketChannel.class)
             .childHandler(new LocalProxyInitializer(serverAddress, serverPort, method, password))
             .option(ChannelOption.SO_BACKLOG, 128)
             .childOption(ChannelOption.SO_KEEPALIVE, true);

            ChannelFuture f = b.bind(localPort).sync();
            System.out.println("Shadowsocks client started on port: " + localPort);
            f.channel().closeFuture().sync();
        } finally {
            workerGroup.shutdownGracefully();
            bossGroup.shutdownGracefully();
        }
    }

    public static void main(String[] args) throws Exception {
        // Remplacer par votre configuration
        int localPort = 1080;
        String serverAddress = "your_server_ip";
        int serverPort = 8388;
        String method = "aes-256-cfb";
        String password = "your_password";

        new ShadowsocksClient(localPort, serverAddress, serverPort, method, password).run();
    }
}
```

**8. Considérations avancées (comme Clash)**

Pour construire un client comme Clash, vous devriez considérer des fonctionnalités plus avancées :

* **Protocoles Proxy Multiples :** Clash prend en charge divers protocoles proxy (Shadowsocks, SOCKS5, HTTP). Vous devriez ajouter des gestionnaires pour chaque protocole.
* **Routage Basé sur des Règles :** Clash vous permet de définir des règles pour acheminer le trafic en fonction du domaine, de l'adresse IP, GEOIP, etc. Cela impliquerait d'implémenter un moteur de règles dans votre client.
* **Gestion de la Configuration :** Clash utilise des fichiers de configuration YAML. Vous devriez implémenter un moyen de charger et d'analyser de telles configurations.
* **Gestion DNS :** Clash intercepte souvent les requêtes DNS et les achemine via le proxy. Vous devriez implémenter l'interception et le transfert DNS.
* **Support UDP :** Shadowsocks prend également en charge le transfert UDP. Vous devriez implémenter la gestion UDP en utilisant les capacités UDP de Netty.
* **Plugins et Extensions :** Clash a un système de plugins. Implémenter un tel système ajouterait une complexité significative.

**En résumé, construire un client Shadowsocks basique avec Netty implique :**

1.  Comprendre le protocole Shadowsocks.
2.  Configurer un projet Netty.
3.  Créer des `ChannelHandler`s personnalisés pour l'encodage, le décodage et le transfert des données.
4.  Implémenter la logique de chiffrement et de déchiffrement.
5.  Démarrer un serveur local pour accepter les connexions des applications.
6.  Se connecter au serveur Shadowsocks distant.

Construire un client plus riche en fonctionnalités comme Clash nécessite une compréhension beaucoup plus profonde de la mise en réseau, des protocoles proxy et d'une architecture logicielle plus complexe. Commencez par une implémentation basique de Shadowsocks et ajoutez progressivement des fonctionnalités selon les besoins. N'oubliez pas de consulter la documentation officielle de Shadowsocks et les exemples Netty pour des informations plus détaillées.