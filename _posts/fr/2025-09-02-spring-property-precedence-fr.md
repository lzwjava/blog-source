---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Règles de préséance des propriétés de Spring expliquées
translated: true
type: note
---

Au printemps, lorsque vous avez **des clés de propriété en double** dans vos sources de configuration (par exemple, `application.properties`, `application.yml`, variables d'environnement, arguments de ligne de commande, etc.), **la dernière ayant la priorité la plus élevée l'emporte**.

Voici comment cela fonctionne en détail :

### 1. Ordre des sources de propriétés

Spring Boot applique un **ordre des sources de propriétés** bien défini. Par exemple :

* Les arguments de ligne de commande
* `application.properties` / `application.yml` (d'abord ceux spécifiques au profil, puis ceux par défaut)
* Les variables d'environnement
* Les propriétés système
* Les valeurs par défaut dans le code (`@Value("${...:default}")`)

Si la même clé de propriété apparaît dans plusieurs sources, Spring choisit celle de la **source ayant la priorité la plus élevée**.

### 2. Dans le même fichier

Si vous avez la même clé de propriété **répétée dans un seul fichier** (comme `application.properties`), Spring utilise **la dernière occurrence déclarée**.
Exemple (`application.properties`) :

```properties
server.port=8080
server.port=9090
```

Ici, `server.port=9090` prend effet.

### 3. À travers plusieurs fichiers

Si vous définissez la même propriété dans `application.properties` et `application-dev.properties`, et que vous activez le profil `dev`, alors la valeur de `application-dev.properties` remplacera celle par défaut.

### 4. Avec `@PropertySource`

Si vous chargez plusieurs fichiers de propriétés via `@PropertySource`, l'ordre de déclaration est important. Le dernier peut remplacer les valeurs précédentes, sauf si vous le marquez avec `ignoreResourceNotFound` ou si vous contrôlez explicitement la priorité.

---

✅ **Résumé :**

* Spring résout les propriétés par **priorité des sources**.
* Dans **le même fichier**, la **dernière définition de clé** l'emporte.
* À travers les fichiers/profils, la **propriété du profil actif ou du fichier chargé plus tard** remplace les précédentes.

Voulez-vous que je vous montre également **la hiérarchie exacte de priorité des propriétés de Spring Boot (de la plus haute à la plus basse)** ? Cela donne une image très claire de l'endroit où les remplacements se produisent.