---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Fenêtre des paramètres Révéler dans GitHub
translated: true
type: note
---

### Aperçu
Ce fichier XML est un document Interface Builder XIB (XML Interface Builder) pour une application macOS. Les fichiers XIB sont utilisés dans Xcode pour définir les interfaces utilisateur de manière déclarative, en particulier pour les fenêtres, les vues et les contrôles dans les applications Cocoa. Ce fichier spécifique définit l'interface utilisateur pour une fenêtre de paramètres dans une application appelée **Reveal-In-GitHub** (probablement un utilitaire pour ouvrir rapidement des fichiers de code source ou des dépôts dans GitHub depuis votre IDE ou votre système de fichiers).

Le fichier cible macOS (runtime Cocoa) et utilise Auto Layout (`useAutolayout="YES"`). Il est structuré autour d'un objet fenêtre principal, avec des connexions vers une classe de contrôleur personnalisée (`RIGSettingWindowController`), des outlets pour les vues principales, et diverses sous-vues d'interface utilisateur comme des boutons, des étiquettes et un conteneur personnalisé.

Métadonnées clés :
- **Version des outils** : Xcode 9.0.1 (toolsVersion="9059"), construit sur macOS 10.12.6 (systemVersion="14F27").
- **Comportement de la fenêtre** : Avec titre, pouvant être fermée, réduite et redimensionnée. Elle ne recalcule pas automatiquement la boucle de vue clé et utilise les animations par défaut.
- **Position/Taille initiale** : S'ouvre à la position d'écran (527, 176) avec les dimensions 651x497 pixels (sur un écran de 1440x877).

La racine du fichier est un `<document>` contenant `<dependencies>` (pour le plugin Cocoa) et `<objects>` (la hiérarchie réelle de l'interface utilisateur).

### Composants principaux

#### 1. **Propriétaire du fichier (Contrôleur personnalisé)**
   - **Classe** : `RIGSettingWindowController`
   - Celui-ci agit comme le contrôleur pour la fenêtre, gérant la logique telle que le chargement/la sauvegarde des paramètres.
   - **Outlets** (connexions aux éléments de l'interface utilisateur) :
     - `configsView` → Une vue personnalisée pour afficher les options de configuration (ID : `IKd-Ev-B9V`).
     - `mainView` → La vue contenu de la fenêtre (ID : `se5-gp-TjO`).
     - `window` → La fenêtre de paramètres elle-même (ID : `F0z-JX-Cv5`).
   - Le `delegate` de la fenêtre est également connecté à ce contrôleur.

#### 2. **Objets standards**
   - **First Responder** (`-1`) : Espace réservé pour la gestion des événements clavier.
   - **Application** (`-3`) : Représente l'instance NSApplication (non utilisée directement ici).

#### 3. **La fenêtre de paramètres**
   - **ID** : `F0z-JX-Cv5`
   - **Titre** : "Reveal-In-GitHub Settings"
   - **Vue contenu** (ID : `se5-gp-TjO`) : Une vue pleine taille (651x497) qui se redimensionne automatiquement avec la fenêtre. Elle contient toutes les sous-vues, positionnées avec des cadres fixes (bien qu'Auto Layout soit activé, suggérant que les contraintes pourraient être ajoutées par programmation ou dans un fichier .storyboard compagnon).

   **Disposition des sous-vues** (toutes utilisent des cadres fixes pour le positionnement ; les coordonnées y augmentent vers le bas depuis le haut) :

   | Élément | Type | Position (x, y) | Taille (l x h) | Description |
   |---------|------|-----------------|--------------|-------------|
   | **Bouton Sauvegarder** | `NSButton` (ID : `EuN-9g-Vcg`) | (14, 13) | 137x32 | Bouton "Save" en bas à gauche (bordure arrondie). Déclenche l'action `saveButtonClcked:` sur le contrôleur. Utilise la petite police système (13pt). |
   | **Bouton Réinitialiser les menus par défaut** | `NSButton` (ID : `KvN-fn-w7m`) | (151, 12) | 169x32 | Bouton "Reset Default Menus" à proximité. Déclenche l'action `resetMenusButtonClicked:`. Petite police système (13pt). |
   | **Vue de configuration** | `NSView` (Personnalisée, ID : `IKd-Ev-B9V`) | (20, 54) | 611x330 | Grande vue personnalisée centrale étiquetée "Config View". Probablement un conteneur pour du contenu dynamique comme des tableaux, des listes ou des boutons à bascule pour les configurations de dépôt GitHub (par exemple, chemins de dépôt, jetons d'authentification). Elle est connectée à l'outlet `configsView`. |
   | **Étiquette Éléments de menu personnalisés** | `NSTextField` (ID : `G1C-Td-n9Y`) | (18, 425) | 187x17 | Étiquette statique "Custom Menu Items" près du bas. Helvetica Neue (17pt), couleur d'étiquette. |
   | **Bouton Effacer les dépôts par défaut** | `NSButton` (ID : `KvN-fn-w7m`) | (14, 449) | 164x32 | Bouton "Clear Default Repos" en bas à gauche. Déclenche l'action `clearButtonClicked:`. Petite police système (13pt). |
   | **Étiquette Titre du menu** | `NSTextField` (ID : `UUf-Cr-5zs`) | (20, 392) | 77x18 | Étiquette statique "Menu Title". Helvetica Neue (14pt), couleur d'étiquette. |
   | **Étiquette Raccourci clavier** | `NSTextField` (ID : `rMv-by-SKS`) | (112, 391) | 63x19 | Étiquette statique "⌃⇧⌘ +" (Contrôle+Maj+Commande +). Lucida Grande UI (15pt), couleur d'étiquette. Indique un raccourci global personnalisable pour le menu de l'application. |
   | **Étiquette Modèle d'URL** | `NSTextField` (ID : `zW4-cw-Rhb`) | (410, 392) | 94x18 | Étiquette statique "URL Pattern ". Police système (15pt), couleur d'étiquette. Probablement pour configurer les modèles d'URL GitHub (par exemple, pour les liens profonds vers les fichiers/les vues blame). |

   - **Notes de disposition** :
     - Les éléments sont principalement alignés à gauche (x=14-20) pour un design compact, semblable à un formulaire.
     - Haut : Boutons d'action (Sauvegarder/Réinitialiser).
     - Milieu : Grande Vue de configuration (la majeure partie de l'espace pour la gestion des dépôts/paramètres).
     - Bas : Étiquettes pour la personnalisation du menu et un bouton d'effacement.
     - Tous les champs de texte sont non modifiables (étiquettes statiques), suggérant que la saisie utilisateur se produit à l'intérieur de la Vue de configuration ou via des champs séparés non définis ici.
     - Couleurs : Valeurs par défaut du système (couleurs d'étiquette/contrôle pour l'accessibilité).
     - Polices : Mélange de polices système, Helvetica Neue et Lucida Grande pour une sensation macOS native.

### Objectif et fonctionnalité
Cette fenêtre de paramètres permet aux utilisateurs de :
- **Gérer les dépôts/Configurations** : Via la "Config View" centrale (par exemple, ajouter/supprimer des dépôts GitHub par défaut).
- **Personnaliser les menus** : Définir un titre de menu, un raccourci clavier global (⌃⇧⌘+) et des modèles d'URL pour révéler des fichiers dans GitHub.
- **Persister les modifications** : Sauvegarder les paramètres ou réinitialiser/effacer les valeurs par défaut avec des boutons dédiés.

Le contrôleur (`RIGSettingWindowController`) gère les actions des boutons :
- `saveButtonClcked:` – Sauvegarde les modifications de l'utilisateur (par exemple, dans UserDefaults ou un fichier plist).
- `resetMenusButtonClicked:` – Restaure les paramètres d'usine des menus.
- `clearButtonClicked:` – Supprime les entrées de dépôt par défaut.

Ce XIB est probablement chargé par programmation dans le code de l'application (par exemple, `NSNib(nibNamed: "Settings", bundle: nil)`), la vue personnalisée étant remplie dynamiquement (par exemple, avec un NSTableView pour les listes de dépôts).

Si vous construisez ou modifiez cette application, vous pouvez ouvrir le XIB dans l'Interface Builder de Xcode pour visualiser/modifier la disposition visuellement. Pour l'intégration du code, recherchez les méthodes IBAction dans la classe du contrôleur correspondant aux sélecteurs d'action.