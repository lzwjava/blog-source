---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Chronométrage informatique avant Unix
translated: true
type: note
---

Oui, vous avez parfaitement raison — bien avant les horodatages Unix dans les années 1970, nous avions ces machines massives des débuts comme l'ENIAC (je pense que vous vouliez dire ça au lieu de ANNIC ; c'était l'Electronic Numerical Integrator and Computer de 1945), l'Altair 8800 (le kit de 1975 qui a lancé la révolution de l'ordinateur personnel, où Bill Gates et Paul Allen ont bricolé ce fameux interpréteur BASIC via télétype), et les idées fondatrices de John von Neumann (comme son rapport de 1945 sur l'EDVAC qui a donné naissance au concept de programme enregistré influençant tout ce qui a suivi).

Mais "gérer le temps" à cette époque ? Rien à voir avec notre élégance des secondes-depuis-l'époque. Ces bêtes n'avaient pas d'horloges temps réel (RTC) intégrées pour les dates ou l'heure civile — elles étaient conçues pour le calcul brut, pas pour planifier votre rendez-vous chez le dentiste. Le temps était très basique : principalement des horloges internes pour synchroniser les opérations, ou des astuces logicielles comme des compteurs de boucle pour les délais. Pas de mémoire persistante pour "maintenant nous sommes le 15 octobre 2025". Décomposons cela rapidement pour chacun, sous l'angle du traitement numérique.

### ENIAC (1945) : Trains d'impulsions et horloge maîtresse
Ce monstre de 30 tonnes était programmé en branchant des câbles et en actionnant des interrupteurs — pas de stockage de code, juste du câblage pour des problèmes mathématiques comme les tables de balistique. La gestion du temps était entièrement matérielle :
- **Bases de l'horloge** : Un oscillateur "cycling unit" central émettait des impulsions à 100 000 par seconde (toutes les 10 microsecondes). Tout se synchronisait sur celles-ci — comme un battement de cœur pour les tubes à vide.
- **Chronométrage des opérations** : Une addition prenait 20 impulsions (200 microsecondes, ou 1/5000e de seconde). Les boucles ou les délais ? Vous câbliez manuellement des répéteurs ou des compteurs ; pas de minuteries logicielles.
- **Temps réel ?** Nada. Elle exécutait des calculs de balistique en 30 secondes là où les machines analogiques mettaient 15 minutes, mais le "temps" signifiait des décomptes de cycles, pas des calendriers. Von Neumann a été consultant dessus mais a poussé pour les programmes enregistrés pour rendre le chronométrage plus flexible.

D'un point de vue numérique : Voyez cela comme des ticks à débit fixe (100 kHz), où vous additionniez les impulsions pour savoir "combien de temps" un calcul durait — un peu comme des secondes rudimentaires, mais il fallait les compter manuellement pour le débogage.

### Altair 8800 (1975) : Horloge à cristal et délais DIY
L'Altair fut le premier ordinateur "personnel" — une boîte clignotante avec une puce Intel 8080, pas de clavier ni d'écran au début (juste des interrupteurs et des LED). Le BASIC 4K de Gates se chargeait via bande, permettant aux amateurs de bidouiller.
- **Bases de l'horloge** : Un oscillateur à cristal de 2 MHz pilotait le CPU — des ticks réguliers à 2 millions de cycles/seconde pour le fetch/décodage/exécution des instructions.
- **Astuces de chronométrage** : Pas d'horloge intégrée pour les dates ; vous ajoutiez une carte accessoire "Time Clock" (88-ACC) pour des interruptions ou compteurs basiques. Sinon, des boucles logicielles : par exemple, une boucle FOR-NEXT en BASIC pour brûler des cycles et créer des délais (comme `FOR I=1 TO 1000: NEXT I` pour une "pause" approximative).
- **L'approche de BASIC** : Le premier Altair BASIC n'avait pas de fonction TIME$ (c'est venu plus tard dans Microsoft BASIC). Le temps était relatif — comptez les instructions ou connectez un matériel externe comme une puce d'horloge temps réel (un add-on rare).

En termes de nombres : À 2 MHz, une instruction pouvait prendre 4-20 cycles, donc un délai d'1 seconde ? Bouclez ~2 millions de fois. Brutal, mais cela nous a appris l'efficacité.

### L'Architecture de Von Neumann (1945+) : Les cycles comme tick universel
Von Neumann n'a pas construit de matériel (c'était la machine IAS en 1952), mais son plan — CPU, mémoire, E/S communiquant tous via un bus — a préparé le terrain. Le temps ? Entièrement question de cycles synchronisés.
- **Rôle de l'horloge** : Une horloge maîtresse (à cristal ou autre) émet des impulsions pour fetch-décoder-exécuter les instructions. Chaque cycle (front montant/descendant) fait avancer l'état — pas de chevauchement, du pur série.
- **Représentation du temps** : Les instructions prenaient un nombre fixe de cycles (par exemple, addition en 1-4 ticks), donc le "temps" était le décompte de cycles. Pour les délais, on utilisait des branchements conditionnels sur des compteurs ; les horloges réelles étaient externes (comme des prises murales ou des réinitialisations manuelles).
- **Héritage** : Ce goulot d'étranglement (données/instructions partageant le bus) nous hante toujours — l'IA le déteste car déplacer les données prend bien plus de cycles que les traiter.

En termes d'équation : Temps total = (instructions × cycles/instr) / fréquence horloge. Pour l'IAS (inspirée de von Neumann) : ~1 MHz d'horloge, donc 1 million d'opérations/seconde max — vos 1,76 milliard de secondes ? Cela représenterait ~55 ans de fonctionnement non-stop de l'IAS, mais elle aurait fondu avant.

Ces configurations étaient de folles précurseures de l'époque Unix — le temps comme compteur, mais il fallait le construire soi-même. Si vous voulez approfondir (comme des extraits de code pour les délais Altair), dites-le-moi !

[ENIAC Wikipedia](https://en.wikipedia.org/wiki/ENIAC)
[A Report on the ENIAC](https://ftp.arl.army.mil/mike/comphist/46eniac-report/chap1.html)
[Electronic Computing Circuits of the ENIAC](https://archive.computerhistory.org/resources/text/Knuth_Don_X4100/PDF_index/k-8-pdf/k-8-r5367-1-ENIAC-circuits.pdf)
[Organization of the Altair 8800](https://ubuntourist.codeberg.page/Altair-8800/part-2.html)
[MITS Altair 8800 Brochure](https://vtda.org/docs/computing/MITS/MITS_Altair8800ComputerSystem_Brochure.pdf)
[Von Neumann Architecture - Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_architecture)
[In a simple Von Neumann architecture, what exactly is a clock cycle?](https://www.quora.com/In-a-simple-Von-Neumann-architecture-what-exactly-is-a-clock-cycle)