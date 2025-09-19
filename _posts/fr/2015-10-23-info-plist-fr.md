---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Décodage du fichier Info.plist
translated: true
---

Si vous avez travaillé avec le développement macOS ou iOS, vous avez probablement déjà rencontré un fichier `Info.plist`. Ce fichier basé sur XML est une partie clé de toute application ou plugin Apple, agissant comme un passeport qui indique au système qui il est, ce qu'il fait et comment il devrait se comporter. Aujourd'hui, nous explorons le `Info.plist` de "Reveal-In-GitHub", un plugin Xcode que nous avons introduit dans un précédent article. Plutôt que de disséquer chaque ligne, nous nous concentrerons sur les concepts et les schémas de base qui définissent son but et sa fonctionnalité.

---

#### Qu'est-ce qu'un fichier `Info.plist` ?

Le `Info.plist` (abréviation de "Information Property List") est un fichier structuré qui contient des métadonnées sur une application, un plugin ou un bundle. Écrit en XML (avec un schéma défini par Apple), il utilise des paires clé-valeur pour décrire des éléments essentiels comme le nom de l'application, sa version et sa compatibilité. Pour "Reveal-In-GitHub", ce fichier l'identifie comme un plugin Xcode et assure son intégration fluide avec l'IDE.

Contrairement au fichier `.pbxproj`, qui concerne *comment* construire quelque chose, le `Info.plist` concerne *ce que* c'est. C'est une déclaration d'identité et d'intention.

---

#### Concepts clés dans le fichier

1. **Bases du Bundle**
   Plusieurs clés définissent le plugin comme un bundle macOS :
   - **`CFBundleExecutable`** : défini sur `$(EXECUTABLE_NAME)`, un espace réservé pour le nom du binaire compilé (défini pendant le processus de construction).
   - **`CFBundleIdentifier`** : `$(PRODUCT_BUNDLE_IDENTIFIER)` se résout en `com.lzwjava.Reveal-In-GitHub`, un identifiant unique au format DNS inversé qui distingue ce plugin des autres.
   - **`CFBundlePackageType`** : `BNDL` marque ceci comme un bundle, un format courant pour les plugins et les bibliothèques sur macOS.
   - **`CFBundleName`** : `$(PRODUCT_NAME)` deviendra "Reveal-In-GitHub", le nom convivial.

2. **Versioning et Propriété**
   - **`CFBundleShortVersionString`** : "1.0" est la version visible par l'utilisateur.
   - **`CFBundleVersion`** : "1" est un numéro de build interne.
   - **`NSHumanReadableCopyright`** : "Copyright © 2015年 lzwjava. Tous droits réservés." crédite le créateur, `lzwjava`, et date le plugin à 2015.
   - **`CFBundleSignature`** : "????" est un espace réservé (généralement un code de quatre caractères), bien que ce soit moins critique pour les plugins.

3. **Localisation**
   - **`CFBundleDevelopmentRegion`** : "en" définit l'anglais comme langue par défaut, affectant la manière dont les ressources (le cas échéant) sont localisées.

4. **Compatibilité du Plugin Xcode**
   La caractéristique marquante ici est **`DVTPlugInCompatibilityUUIDs`**, un long tableau d'UUID. Ceux-ci correspondent à des versions spécifiques de Xcode (par exemple, Xcode 6, 7, etc.), assurant que le plugin ne se charge que dans les IDE compatibles. Cette liste est inhabituellement large, suggérant que "Reveal-In-GitHub" a été conçu pour fonctionner sur de nombreuses versions de Xcode — un signe de compatibilité avant et arrière réfléchie.

5. **Paramètres spécifiques au Plugin**
   - **`NSPrincipalClass`** : laissé vide (`<string></string>`), suggérant que le plugin pourrait définir dynamiquement son point d'entrée ou s'appuyer sur les conventions de Xcode.
   - **`XC4Compatible` et `XC5Compatible`** : tous deux `<true/>`, confirmant la compatibilité avec Xcode 4 et 5.
   - **`XCGCReady`** : `<true/>` indique la préparation pour la collecte des déchets, une ancienne fonction de gestion de la mémoire macOS (majoritairement obsolète en 2015 au profit d'ARC).
   - **`XCPluginHasUI`** : `<false/>` suggère qu'il n'y a pas d'interface utilisateur personnalisée au-delà de ce qui est intégré à Xcode — bien que cela semble entrer en conflit avec le fichier `.xib` dans le `.pbxproj`. Peut-être que l'interface utilisateur est minimale ou gérée différemment.

---

#### Schémas à remarquer

1. **Espaces réservés pour la flexibilité**
   Les clés comme `$(EXECUTABLE_NAME)` et `$(PRODUCT_BUNDLE_IDENTIFIER)` utilisent des variables liées au système de construction (définies dans le `.pbxproj`). Cela garde le `Info.plist` réutilisable à travers les configurations (par exemple, Debug vs. Release).

2. **Conception minimaliste**
   Le fichier est épuré, se concentrant sur les essentiels. Pas d'icônes sophistiquées, d'autorisations ou de paramètres spécifiques à l'application — juste ce dont un plugin Xcode a besoin pour fonctionner. Cette simplicité est typique pour les plugins qui étendent une application existante (Xcode) plutôt que des programmes autonomes.

3. **Focalisation sur la compatibilité**
   La longue liste de `DVTPlugInCompatibilityUUIDs` et les drapeaux comme `XC4Compatible` montrent un plugin conçu pour durer. Ce schéma est courant dans les outils de développement, où les utilisateurs pourraient s'accrocher à des versions plus anciennes de Xcode pour la stabilité.

4. **Métadonnées sur le comportement**
   Contrairement aux fichiers de code, le `Info.plist` ne *fait* rien — il décrit. Son rôle est passif, fournissant des informations que Xcode et macOS interprètent en temps d'exécution.

---

#### Que nous dit cela sur Reveal-In-GitHub ?

Ce `Info.plist` présente "Reveal-In-GitHub" comme un plugin Xcode léger et focalisé de 2015, probablement créé par un développeur solo (`lzwjava`). Sa large compatibilité suggère qu'il était destiné à être largement utilisable, tandis que l'absence d'un drapeau d'interface utilisateur (malgré un `.xib` dans le projet) laisse supposer une intégration subtile — peut-être un élément de menu ou une action contextuelle plutôt qu'une interface flashy. Étant donné le nom et le contexte du `.pbxproj`, il est probable qu'il optimise les flux de travail GitHub, comme le lien des fichiers Xcode à leurs dépôts en ligne.

---

#### Pourquoi cela importe

Le `Info.plist` est la poignée de main de votre application avec le système. Pour les développeurs, le comprendre signifie que vous pouvez ajuster la compatibilité, le versioning ou le comportement sans toucher au code. Pour "Reveal-In-GitHub", c'est la clé pour s'intégrer parfaitement dans Xcode. La prochaine fois que vous déboguez un plugin ou que vous en créez un, ce fichier sera votre point de départ — petit mais puissant.