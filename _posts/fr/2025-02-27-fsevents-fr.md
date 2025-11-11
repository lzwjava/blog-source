---
audio: false
generated: true
lang: fr
layout: post
title: Surveillance des changements de répertoire avec l'API FSEvents
translated: true
type: note
---

J'utilisais un blog Jekyll, et lorsque j'ai exécuté `bundle exec jekyll serve --incremental`, le terminal a affiché `fsevent_watch`. Par conséquent, j'ai posé des questions à une IA à ce sujet.

---

Il semble que vous fassiez référence à `fsevent_watch`, qui n'est pas un outil ou une fonction standard autonome dans la plupart des contextes de programmation. Sur la base de votre question et des conventions courantes, je suppose que vous vous interrogez sur l'utilisation de l'**API FSEvents** sur macOS pour surveiller les événements du système de fichiers—peut-être vouliez-vous parler de `fsevents` ou d'un utilitaire similaire. Si j'ai mal compris, n'hésitez pas à clarifier !

L'API FSEvents est un framework spécifique à macOS qui permet aux applications de recevoir des notifications concernant les modifications apportées à une arborescence de répertoires. Elle est couramment utilisée en programmation C, Objective-C ou Swift pour surveiller les événements du système de fichiers tels que la création, la suppression ou la modification de fichiers. Comme `fsevent_watch` n'est pas une commande ou une fonction reconnue (cela pourrait être une faute de frappe ou un outil tiers), je vais expliquer comment utiliser directement l'API FSEvents, ce qui est probablement ce que vous recherchez.

Voici un guide pratique pour utiliser FSEvents afin de surveiller un répertoire :

### Utilisation de FSEvents en C/Objective-C
L'API FSEvents fait partie du framework CoreServices sur macOS. Voici un exemple basique en C pour surveiller un répertoire afin de détecter les modifications :

1. **Inclure les en-têtes nécessaires** :
   Vous devrez inclure l'en-tête FSEvents du framework CoreServices.

2. **Configurer le flux d'événements** :
   Créez un flux d'événements pour surveiller un répertoire spécifique, définissez une fonction de rappel pour gérer les événements et planifiez-le avec une boucle d'exécution (run loop).

3. **Traiter les événements** :
   La fonction de rappel traite les événements (par exemple, fichier modifié, supprimé) et fournit les chemins et les indicateurs.

Voici un exemple minimal :

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// Fonction de rappel pour gérer les événements du système de fichiers
void callback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[])
{
    char **paths = (char **)eventPaths;
    for (size_t i = 0; i < numEvents; i++) {
        printf("Changement détecté à : %s (Indicateurs : 0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // Chemin à surveiller (par exemple, votre répertoire personnel)
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // Créer le flux d'événements
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // Allocateur
        &callback,      // Fonction de rappel
        NULL,           // Info de rappel (contexte)
        pathsToWatch,   // Chemins à surveiller
        kFSEventStreamEventIdSinceNow, // Commencer avec les événements à partir de maintenant
        1.0,            // Latence en secondes (délai de regroupement)
        kFSEventStreamCreateFlagNone // Indicateurs (peut utiliser kFSEventStreamCreateFlagFileEvents pour les événements au niveau fichier)
    );

    // Planifier le flux sur la boucle d'exécution actuelle
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // Démarrer le flux
    FSEventStreamStart(stream);

    // Exécuter la boucle pour écouter les événements
    printf("Surveillance de /Users/yourusername... Appuyez sur Ctrl+C pour arrêter.\n");
    CFRunLoopRun();

    // Nettoyage (inaccessible dans cet exemple sauf si arrêté)
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### Étapes expliquées :
- **Chemins à surveiller** : Vous spécifiez un ou plusieurs répertoires (par exemple, `/Users/yourusername`) dans un `CFArray`.
- **Fonction de rappel** : La fonction `callback` est déclenchée lorsque des changements se produisent. Elle reçoit un tableau des chemins affectés et des indicateurs (par exemple, `kFSEventStreamEventFlagItemCreated`).
- **Création du flux** : `FSEventStreamCreate` configure le surveillant. La latence (par exemple, `1.0` seconde) regroupe les événements pour éviter de submerger la fonction de rappel.
- **Boucle d'exécution** : Le flux s'intègre avec une boucle d'exécution (comme `CFRunLoopRun`) pour maintenir le programme actif et réactif.
- **Nettoyage** : Arrêtez et libérez le flux une fois terminé (non montré dans cet exemple de boucle infinie).

#### Compilation :
Compilez avec le framework CoreServices :
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

Exécutez-le :
```bash
./fsevents_example
```

### Points clés :
- **Granularité** : Par défaut, FSEvents surveille les changements au niveau du répertoire. Pour les événements au niveau fichier (par exemple, modifications de fichiers spécifiques), ajoutez l'indicateur `kFSEventStreamCreateFlagFileEvents`.
- **Latence** : Le paramètre de latence (par exemple, `1.0`) contrôle la fréquence à laquelle la fonction de rappel est appelée. Des valeurs plus faibles donnent des mises à jour plus rapides mais plus d'appels.
- **Portée** : FSEvents surveille récursivement l'intégralité de l'arborescence du répertoire—il n'est pas nécessaire de spécifier les sous-répertoires.

### Alternative : Utiliser un outil
Si vous recherchez un outil en ligne de commande plutôt que de le coder vous-même, il n'y a pas de `fsevent_watch` dans la boîte à outils standard de macOS. Cependant, des outils tiers comme `fswatch` utilisent FSEvents. Pour utiliser `fswatch` :

1. **Installer fswatch** (par exemple, via Homebrew) :
   ```bash
   brew install fswatch
   ```

2. **Exécutez-le** :
   ```bash
   fswatch /chemin/à/surveiller
   ```
   Cela affiche les chemins lorsque des changements se produisent. Par exemple :
   ```bash
   fswatch ~/Documents
   ```
   Vous verrez des lignes comme `/Users/yourusername/Documents/file.txt` lorsque les fichiers changent.

3. **Avec un script** :
   Redirigez la sortie vers un script pour des actions personnalisées :
   ```bash
   fswatch ~/Documents | while read -r file; do echo "Modifié : $file"; done
   ```

### Si vous vouliez dire autre chose
Si `fsevent_watch` fait référence à une bibliothèque, un outil ou une faute de frappe spécifique (par exemple, `fsevents-watch`), veuillez fournir plus de contexte—comme le langage de programmation ou l'environnement dans lequel vous travaillez—et j'adapterai la réponse en conséquence.

Faites-moi savoir comment je peux affiner cela pour vous !