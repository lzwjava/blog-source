---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Hexadécimal ASCII et UTF-8 expliqués simplement
translated: true
type: note
---

Décortiquons-les clairement :

---

### ASCII

* **Définition** : ASCII (American Standard Code for Information Interchange) est l'un des premiers encodages de caractères.
* **Plage** : Utilise **7 bits** (valeurs 0–127).
* **Signification** : Chaque nombre correspond à un caractère.
  Par exemple :

  * `65` → `"A"`
  * `97` → `"a"`
  * `48` → `"0"`
* **Limitation** : Ne couvre que les lettres anglaises, les chiffres, la ponctuation et les codes de contrôle (comme le saut de ligne).

---

### Hex (Représentation Hexadécimale)

* **Définition** : L'hexadécimal n'est pas un jeu de caractères en soi, mais une **représentation numérique** (base-16) des données.
* **Utilisation** : Couramment utilisé pour afficher les octets de manière compacte et lisible pour un humain.
* **Exemple** :

  * ASCII `"A"` = décimal `65` = hex `41`.
  * ASCII `"B"` = décimal `66` = hex `42`.
  * Donc le texte `"AB"` s'affiche comme `41 42` en hexadécimal.

---

### UTF-8

* **Définition** : UTF-8 est un standard **d'encodage Unicode**.
* **Caractéristiques** :

  * Longueur variable : encode chaque caractère sur **1 à 4 octets**.
  * Rétrocompatible avec ASCII : les caractères `0–127` sont identiques à l'ASCII (1 octet).
  * Peut représenter tous les caractères Unicode (lettres, symboles, émojis, caractères chinois, etc.).
* **Exemples** :

  * `"A"` → `41` (identique à l'ASCII).
  * `"中"` → `E4 B8 AD` (trois octets en hexadécimal).
  * `"😊"` → `F0 9F 98 8A` (quatre octets en hexadécimal).

---

✅ **En bref** :

* ASCII = ancien code 7 bits pour les caractères anglais.
* Hex = une façon d'écrire les nombres/octets (base-16).
* UTF-8 = encodage moderne qui inclut l'ASCII mais prend également en charge toutes les langues et symboles.

---

Souhaitez-vous que je vous montre également un **exemple côte à côte du même texte** (`"Hello 世界😊"`) en ASCII (si possible), en hexadécimal et en UTF-8 pour que vous puissiez voir la différence directement ?