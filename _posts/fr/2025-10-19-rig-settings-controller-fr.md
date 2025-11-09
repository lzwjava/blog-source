---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Vue d'ensemble du contrôleur de la fenêtre des paramètres RIG
translated: true
type: note
---

### Aperçu

Ce code Objective-C implémente la classe `RIGSettingWindowController`, qui gère une fenêtre de paramètres pour l'application macOS "Reveal-In-GitHub" (RIG) (probablement un plugin Xcode permettant de révéler rapidement le code sélectionné dans les dépôts GitHub). La fenêtre permet aux utilisateurs de configurer des éléments de menu personnalisés, des raccourcis clavier et des motifs regex pour différents dépôts GitHub. Elle utilise une vue de type tableau (`RIGConfigCellsView`) pour afficher et modifier jusqu'à 10 emplacements de configuration (remplis avec des vides pour assurer la cohérence de l'interface utilisateur).

La classe se conforme aux protocoles `NSTableViewDataSource` et `NSTableViewDelegate`, suggérant qu'elle gère les données et les événements pour une vue tableau à l'intérieur de la vue personnalisée des cellules. Elle s'intègre avec des singletons applicatifs comme `RIGSetting` pour la persistance et `RIGUtils` pour le retour d'information dans l'interface utilisateur.

Responsabilités principales :
- Charger et afficher les éléments configurables (par exemple, titres des menus, touches de raccourci, motifs regex).
- Valider et sauvegarder les modifications.
- Fournir des boutons pour sauvegarder, effacer les paramètres du dépôt par défaut et réinitialiser aux valeurs par défaut.

### Imports et Définitions

```objectivec
#import "RIGSettingWindowController.h"
#import "RIGConfigCellsView.h"
#import "RIGConfig.h"
#import "RIGPlugin.h"
#import "RIGUtils.h"
#import "RIGSetting.h"

#define kOutterXMargin 0
#define kOutterYMargin 0
```

- Les imports incluent l'en-tête de cette classe, une vue personnalisée pour le rendu des lignes de configuration (`RIGConfigCellsView`), des objets modèle (`RIGConfig` pour les paramètres individuels, `RIGSetting` pour le stockage applicatif) et des utilitaires (`RIGUtils` pour les alertes, `RIGPlugin` probablement pour le cycle de vie du plugin).
- Les définitions fixent des marges nulles pour une mise en page en pleine largeur de la vue de configuration à l'intérieur de la fenêtre.

### Interface Privée

```objectivec
@interface RIGSettingWindowController ()<NSTableViewDataSource, NSTableViewDelegate>

@property (nonatomic, strong) NSArray *configs;
@property (nonatomic, strong) RIGConfigCellsView *configCellsView;
@property (weak) IBOutlet NSView *mainView;
@property (weak) IBOutlet NSView *configsView;

@end
```

- Déclare une extension privée pour les propriétés internes et la conformité aux protocoles.
- `configs` : Tableau d'objets `RIGConfig` contenant les paramètres de l'utilisateur (par exemple, titre du menu, dernière touche pressée, motif regex).
- `configCellsView` : Vue personnalisée qui affiche les configurations sous forme de lignes modifiables (probablement un tableau ou une pile de cellules défilables).
- `mainView` et `configsView` : IBOutlets vers les vues conteneurs dans le fichier storyboard/nib ; `configsView` héberge les cellules dynamiques.

### Implémentation

#### Méthodes d'Initialisation

```objectivec
- (void)awakeFromNib {
    [super awakeFromNib];
}

- (void)windowDidLoad {
    [super windowDidLoad];
    
    self.configs = [self displayConfigs];
    
    self.configCellsView = [[RIGConfigCellsView alloc] initWithFrame:CGRectMake(kOutterXMargin, kOutterYMargin, CGRectGetWidth(self.configsView.frame) - 2 * kOutterXMargin, [RIGConfigCellsView heightForConfigs:self.configs])];
    self.configCellsView.configs = self.configs;
    [self.configsView addSubview:self.configCellsView];
    [self.configCellsView reloadData];
}
```

- `awakeFromNib` : Surcharge vide ; appelée lorsque la fenêtre est chargée depuis le nib (storyboard). Se contente d'appeler la superclasse.
- `windowDidLoad` : Configuration principale après que la fenêtre est entièrement chargée.
  - Charge `configs` via `displayConfigs` (expliqué ci-dessous).
  - Crée `configCellsView` avec un cadre qui remplit `configsView` horizontalement (en utilisant les marges) et verticalement en fonction de la hauteur totale nécessaire pour toutes les configurations (calculée par la méthode de classe `RIGConfigCellsView`).
  - Assigne les configurations à la vue, l'ajoute comme sous-vue et déclenche un rechargement des données (rafraîchit probablement les cellules du tableau).

Il y a un appel commenté à `updateConfigsViewHeight`, ce qui suggère qu'un redimensionnement dynamique a été envisagé mais désactivé—peut-être parce que la vue des cellules se redimensionne automatiquement ou que la fenêtre est de taille fixe.

```objectivec
- (void)updateConfigsViewHeight {
    CGRect frame = self.configsView.frame;
    frame.size.height = CGRectGetHeight(self.configCellsView.frame);
    self.configsView.frame = frame;
}
```

- Utilitaire pour redimensionner `configsView` afin qu'elle corresponde à la hauteur de la vue des cellules. Non utilisé actuellement, mais pourrait servir pour agrandir automatiquement la fenêtre si d'autres configurations sont ajoutées.

#### Gestion des Configurations

```objectivec
- (NSMutableArray *)displayConfigs {
    NSMutableArray *configs = [NSMutableArray arrayWithArray:[RIGSetting setting].configs];
    while (configs.count < 10) {
        RIGConfig *config = [[RIGConfig alloc] init];
        config.menuTitle = @"";
        config.lastKey = @"";
        config.pattern = @"";
        [configs addObject:config];
    }
    return configs;
}
```

- Charge les configurations existantes depuis le singleton applicatif `RIGSetting`.
- Complète le tableau avec exactement 10 éléments en utilisant des instances `RIGConfig` vides. Cela garantit une interface utilisateur cohérente (par exemple, 10 lignes modifiables), même si l'utilisateur a moins de configurations sauvegardées. Les configurations vides sont filtrées lors de la sauvegarde.

```objectivec
- (void)reloadConfigs {
    self.configs = [self displayConfigs];
    self.configCellsView.configs = self.configs;
    [self.configCellsView reloadData];
}
```

- Rafraîchit les configurations affichées depuis le stockage et met à jour la vue. Utilisé après les réinitialisations.

```objectivec
- (BOOL)isValidConfigs:(NSArray *)configs {
    for (RIGConfig *config in configs) {
        if (![config isValid]) {
            return NO;
        }
    }
    return YES;
}
```

- Itère sur les configurations et appelle `isValid` sur chacune (vérifie probablement que `menuTitle` et `pattern` ne sont pas vides). Retourne `YES` seulement si toutes sont valides ou vides (mais voir le filtrage ci-dessous).

```objectivec
- (NSArray *)filteredConfigs {
    NSMutableArray *filtered = [NSMutableArray array];
    NSArray *configs = self.configCellsView.configs;
    for (RIGConfig *config in configs) {
        if (config.menuTitle.length > 0 || config.lastKey.length > 0 || config.pattern.length > 0) {
            [filtered addObject:config];
        }
    }
    return filtered;
}
```

- Filtre le tableau des 10 emplacements pour n'inclure que les configurations non vides (basé sur la présence de contenu dans n'importe quel champ). Cela supprime les entrées vides avant la validation/la sauvegarde, donc `isValidConfigs` ne vérifie que les entrées réelles.

#### Gestionnaires d'Actions (IBActions)

Ceux-ci sont connectés aux boutons de l'interface utilisateur via Interface Builder.

```objectivec
- (IBAction)saveButtonClcked:(id)sender {
    NSArray *configs = [self filteredConfigs];
    if (![self isValidConfigs:configs]) {
        [RIGUtils showMessage:@"Please complete the config, should at least have menuTitle and pattern."];
        return;
    }
    [RIGSetting setting].configs = self.configCellsView.configs;
    [RIGUtils showMessage:@"Save succeed. Will Take effect when reopen Xcode."];
}
```

- **Bouton Sauvegarder** : Filtre les configurations, les valide (alerte d'erreur si invalides), puis sauvegarde le tableau complet (complété) dans `RIGSetting`. Note : Il sauvegarde les 10 emplacements, mais les vides sont ignorés lors du chargement/du filtrage. Affiche un message de succès notant qu'un redémarrage de Xcode est nécessaire (rechargement du plugin).

Faute de frappe dans le nom de la méthode : "Clcked" devrait être "Clicked".

```objectivec
- (IBAction)clearButtonClicked:(id)sender {
    RIGSetting *setting = [RIGSetting settingForGitPath:self.gitRepo.localPath];
    NSString *defaultRepo = setting.defaultRepo;
    if (defaultRepo == nil) {
        [RIGUtils showMessage:@"There's no default repo setting."];
    } else {
        setting.defaultRepo = nil;
        [RIGUtils showMessage:[NSString stringWithFormat:@"Succeed to clear current default repo(%@) setting. In the next time to open github, will ask you to select new default repo.", defaultRepo]];
    }
}
```

- **Bouton Effacer** : Cible un paramètre spécifique au projet via `settingForGitPath` (suppose que `self.gitRepo` est disponible, probablement défini ailleurs). Efface le `defaultRepo` (par exemple, une URL GitHub de secours). Alerte si aucun n'est défini, ou confirme l'effacement avec des détails.

Note : `self.gitRepo` n'est pas déclaré ici—probablement une propriété d'une superclasse ou d'une catégorie.

```objectivec
- (IBAction)resetMenusButtonClicked:(id)sender {
    [[RIGSetting setting] setConfigs:[RIGSetting defaultConfigs]];
    [self reloadConfigs];
}
```

- **Bouton Réinitialiser** : Remplace les configurations par les valeurs par défaut de l'application (depuis `RIGSetting`), puis recharge l'interface utilisateur. Aucune boîte de dialogue de confirmation—action directe.

### Améliorations Potentielles / Notes

- **Flux de l'Interface Utilisateur** : La fenêtre est non modale (aucun appel explicite pour l'afficher ici), donc elle est probablement présentée via `[controller showWindow:sender]`. Les modifications nécessitent un redémarrage de Xcode en raison de la nature du plugin.
- **Validation** : Repose sur `RIGConfig.isValid`, qui n'est pas montré—vérifie probablement que les champs requis comme le titre et le motif ne sont pas vides.
- **Cas Limites** : Le remplissage à 10 suppose une interface utilisateur fixe ; un redimensionnement dynamique pourrait utiliser la fonction `updateConfigsViewHeight` commentée. Aucune annulation/confirmation pour la réinitialisation/l'effacement.
- **Dépendances** : Fortement lié aux modèles de l'application (`RIGConfig`, `RIGSetting`)—une compréhension complète nécessite ces en-têtes.

Ce code date de 2015, il utilise donc des modèles Cocoa plus anciens (par exemple, configuration manuelle des cadres plutôt qu'Auto Layout). Pour SwiftUI moderne, ce serait une `View` avec `@State` pour les configurations.