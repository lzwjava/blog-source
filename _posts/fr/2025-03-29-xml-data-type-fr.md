---
audio: false
generated: true
lang: fr
layout: post
title: Types de données de schéma XML
translated: true
type: note
---

XML Schema définit un riche ensemble de types de données intégrés qui peuvent être utilisés pour spécifier le type de données autorisé dans les éléments et les attributs. Ces types de données garantissent que le contenu XML respecte le format et les contraintes prévus.

Les types de données intégrés dans XML Schema sont globalement classés en types **primitifs** et **dérivés**. Les types dérivés sont basés sur des types primitifs et sont créés en appliquant des restrictions ou d'autres modifications.

**Types de données primitifs (19 intégrés) :**

Ce sont les types de données fondamentaux et indivisibles à partir desquels tous les autres types simples intégrés et définis par l'utilisateur sont dérivés.

* **String :** Représente des chaînes de caractères.
* **Boolean :** Représente des valeurs logiques (true ou false, peut aussi être représenté par 1 ou 0).
* **Decimal :** Représente des nombres décimaux de précision arbitraire.
* **Float :** Représente des nombres à virgule flottante simple précision 32 bits.
* **Double :** Représente des nombres à virgule flottante double précision 64 bits.
* **Duration :** Représente un intervalle de temps.
* **DateTime :** Représente un point spécifique dans le temps, incluant la date et l'heure.
* **Time :** Représente un point spécifique dans le temps au cours d'une période de 24 heures.
* **Date :** Représente une date calendaire.
* **gYearMonth :** Représente une année et un mois spécifiques.
* **gYear :** Représente une année spécifique.
* **gMonthDay :** Représente un mois et un jour spécifiques.
* **gDay :** Représente un jour spécifique du mois.
* **gMonth :** Représente un mois spécifique de l'année.
* **HexBinary :** Représente des données binaires sous forme de valeurs hexadécimales.
* **Base64Binary :** Représente des données binaires encodées en Base64.
* **AnyURI :** Représente un Uniform Resource Identifier (URI).
* **QName :** Représente un nom qualifié (un nom avec un préfixe d'espace de noms).
* **NOTATION :** Représente le nom d'une notation déclarée dans le schéma.

**Types de données dérivés (environ 25 intégrés) :**

Ces types de données sont dérivés des types primitifs en appliquant des contraintes (facettes) telles que la longueur, la plage, les motifs, etc.

**Dérivés de `string` :**

* `normalizedString` : Représente des chaînes de caractères où les sauts de ligne, les tabulations et les retours chariot sont remplacés par des espaces, et sans espaces de début ou de fin.
* `token` : Représente des chaînes normalisées sans espace blanc de début ou de fin, et sans séquences internes de deux espaces blancs ou plus.
* `language` : Représente un identifiant de langue tel que défini par la RFC 3066.
* `NMTOKEN` : Représente un jeton de nom (peut contenir des lettres, des chiffres, des points, des traits d'union et des underscores).
* `NMTOKENS` : Représente une liste séparée par des espaces de `NMTOKEN`s.
* `Name` : Représente un nom XML (doit commencer par une lettre ou un underscore, suivi de lettres, chiffres, points, traits d'union ou underscores).
* `NCName` : Représente un nom non colonisé (comme `Name` mais ne peut pas contenir de deux-points).
* `ID` : Représente un identifiant unique dans un document XML.
* `IDREF` : Représente une référence à une valeur `ID` dans le même document.
* `IDREFS` : Représente une liste séparée par des espaces de valeurs `IDREF`.
* `ENTITY` : Représente une référence à une entité non analysée déclarée dans un DTD (moins courant en XML Schema).
* `ENTITIES` : Représente une liste séparée par des espaces de valeurs `ENTITY` (moins courant en XML Schema).

**Dérivés de `decimal` :**

* `integer` : Représente des nombres entiers (sans partie fractionnaire).
* `nonPositiveInteger` : Représente des entiers inférieurs ou égaux à 0.
* `negativeInteger` : Représente des entiers strictement inférieurs à 0.
* `long` : Représente des entiers signés 64 bits.
* `int` : Représente des entiers signés 32 bits.
* `short` : Représente des entiers signés 16 bits.
* `byte` : Représente des entiers signés 8 bits.
* `nonNegativeInteger` : Représente des entiers supérieurs ou égaux à 0.
* `unsignedLong` : Représente des entiers non signés 64 bits.
* `unsignedInt` : Représente des entiers non signés 32 bits.
* `unsignedShort` : Représente des entiers non signés 16 bits.
* `unsignedByte` : Représente des entiers non signés 8 bits.
* `positiveInteger` : Représente des entiers strictement supérieurs à 0.

**Autres types dérivés :**

* `dateTimeStamp` (dans XML Schema 1.1) : Similaire à `dateTime` mais inclut également des informations de fuseau horaire.
* `yearMonthDuration` (dans XML Schema 1.1) : Représente une durée en années et mois.
* `dayTimeDuration` (dans XML Schema 1.1) : Représente une durée en jours, heures, minutes et secondes.
* `precisionDecimal` (dans XML Schema 1.1) : Représente des nombres décimaux avec une précision préservée.

**Types de données définis par l'utilisateur :**

En plus des types intégrés, XML Schema vous permet de définir vos propres types de données simples et complexes en utilisant des mécanismes tels que :

* **Restriction :** Créer un nouveau type en limitant la plage ou le format d'un type existant (soit intégré, soit défini par l'utilisateur).
* **List :** Définir un type dont les valeurs sont des séquences de valeurs d'un autre type simple.
* **Union :** Définir un type dont les valeurs peuvent provenir des espaces de valeur de deux types simples ou plus.

Lors de la définition d'éléments et d'attributs dans un schéma XML, vous utilisez l'attribut `type` pour spécifier à quel type de données le contenu doit se conformer. Cela garantit la validité des données et facilite leur traitement.

Par exemple :

```xml
<xs:element name="age" type="xs:positiveInteger"/>
<xs:element name="name" type="xs:string"/>
<xs:attribute name="status" type="xs:token"/>
```

Dans cet extrait, l'élément `age` est défini pour contenir un entier positif, l'élément `name` une chaîne de caractères, et l'attribut `status` un jeton (une chaîne normalisée avec une gestion spécifique des espaces blancs).

Comprendre ces types de données est fondamental pour créer des schémas XML efficaces et bien définis. Vous pouvez trouver les détails complets et les définitions formelles dans la spécification W3C XML Schema Part 2: Datatypes.