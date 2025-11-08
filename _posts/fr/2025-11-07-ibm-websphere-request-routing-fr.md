---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-4.5-sonnet
title: Routage des requêtes IBM WebSphere expliqué
translated: true
type: note
---

Permettez-moi d'expliquer comment IBM WebSphere Application Server (WAS) gère les requêtes entrantes et le routage :

## Flux de requête dans IBM WAS

Lorsqu'une requête arrive dans IBM WAS, voici le flux typique :

**1. Couche Serveur Web (Optionnelle)**
- La requête atteint d'abord IBM HTTP Server (IHS) ou un autre serveur web
- Le plugin du serveur web route vers l'instance WAS appropriée

**2. Point d'entrée du Conteneur Web**
La requête entre dans WAS via le **Conteneur Web**, qui fait partie du moteur de servlet principal. La structure de package clé est :

```
com.ibm.ws.webcontainer.*
```

**3. Chaîne de traitement des requêtes**

Le routage se fait via plusieurs composants :

**Framework de Canal de Transport**
- `com.ibm.ws.channel.*` - gère la communication réseau
- Les canaux de transport HTTP reçoivent la requête

**Traitement du Conteneur Web**
```
com.ibm.ws.webcontainer.servlet.ServletWrapper
com.ibm.ws.webcontainer.filter.WebAppFilterManager
```

**4. Exécution de la Chaîne de Filtres**

Les filtres fonctionnent exactement comme les filtres de servlet Java standard mais sont gérés par WAS :

- **Définis dans web.xml** de votre application
- Les filtres sont enchaînés dans l'ordre spécifié
- Chaque filtre peut inspecter/modifier la requête et la réponse
- Utilise l'interface standard `javax.servlet.Filter`

```xml
<filter>
    <filter-name>MyFilter</filter-name>
    <filter-class>com.example.MyFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>MyFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

**Ordre d'exécution des filtres :**
1. WAS charge les configurations de filtre au démarrage de l'application
2. WebAppFilterManager crée la chaîne de filtres
3. À chaque requête : Requête → Filtre1 → Filtre2 → ... → Servlet

## Principaux Packages dans IBM WAS

**Packages de base :**
- `com.ibm.ws.webcontainer.*` - Implémentation du conteneur web
- `com.ibm.ws.runtime.*` - Services d'exécution
- `com.ibm.websphere.servlet.*` - Extensions de servlet spécifiques à WAS
- `com.ibm.ws.channel.*` - Couche de transport
- `com.ibm.ejs.*` - Services de conteneur EJB
- `com.ibm.ws.naming.*` - Implémentation JNDI

## Mécanisme de Routage

**Routage par Hôte Virtuel :**
- Configuré dans la console d'administration WAS
- Mappe les combinaisons `nom d'hôte:port` vers les applications
- Configuration : `VirtualHost → Host Aliases → Applications`

**Routage par Racine de Contexte :**
- Chaque application a une racine de contexte (ex: `/myapp`)
- WAS maintient un registre des applications déployées
- Mappage d'URI : `http://server:port/racineContexte/cheminServlet`

**Mappage de Servlet :**
- Défini dans web.xml ou via annotations
- Correspondance de motifs (exact, chemin, extension, par défaut)

## Séquence de Démarrage d'Application

Lorsqu'une application démarre :
1. **Initialisation du ClassLoader** - L'application obtient son propre chargeur de classe
2. **Analyse de web.xml** - Filtres, servlets, écouteurs chargés
3. **Déclenchement des ServletContextListeners** - `contextInitialized()`
4. **Instanciation des Filtres** - Méthode `init()` appelée
5. **Servlets à chargement au démarrage** - Initialise les servlets précoces
6. **Application marquée DÉMARRÉE** - Prête à accepter des requêtes

Le registre de routage est mis à jour, et l'application est maintenant disponible à sa racine de contexte.

Cela clarifie-t-il comment WAS gère le routage des requêtes et le filtrage ?