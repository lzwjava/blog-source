---
audio: false
generated: true
lang: fr
layout: post
title: Programmation en langage d'assemblage
translated: true
type: note
---

Voici un tutoriel complet pour **Partie 2 : Programmation en langage d'assemblage**, couvrant les sujets décrits : *Jeu d'instructions 8086 (Instructions de transfert de données, arithmétiques, logiques et de contrôle de flux), Programmation en langage d'assemblage (Structures séquentielles, de branchement et de boucle), et Routines de service d'interruption*. Ce tutoriel est conçu pour être approfondi, accessible et pratique, s'appuyant sur les fondamentaux des micro-ordinateurs (par exemple, l'architecture 8086/8088). Il suppose une connaissance de base des registres du CPU et de l'adressage mémoire.

---

## Partie 2 : Programmation en langage d'assemblage

Le langage d'assemblage est un langage de programmation de bas niveau qui offre un contrôle direct sur les opérations d'un microprocesseur. Pour l'Intel 8086/8088, le langage d'assemblage permet aux programmeurs d'écrire des instructions qui correspondent étroitement au code machine, offrant un contrôle granulaire sur les ressources matérielles comme les registres, la mémoire et les périphériques d'E/S.

### 1. Jeu d'instructions 8086

Le jeu d'instructions 8086 est une collection de commandes que le CPU comprend, catégorisées par leur fonction : **transfert de données**, **arithmétique**, **logique** et **contrôle de flux**. Chaque instruction opère sur des registres, de la mémoire ou des valeurs immédiates, en utilisant les modes d'adressage du 8086 (par exemple, registre, direct, indirect).

#### a. Instructions de transfert de données
Ces instructions déplacent des données entre les registres, la mémoire et les valeurs immédiates.

- **MOV (Déplacer)** :
  - Syntaxe : `MOV destination, source`
  - Fonction : Copie les données de la source vers la destination.
  - Exemple : `MOV AX, BX` (copie BX dans AX) ; `MOV AX, [1234h]` (copie les données de l'adresse mémoire DS:1234h vers AX).
  - Notes : N'affecte pas les drapeaux ; la source et la destination doivent être de même taille (8 bits ou 16 bits).
- **XCHG (Échanger)** :
  - Syntaxe : `XCHG destination, source`
  - Fonction : Échange le contenu de la source et de la destination.
  - Exemple : `XCHG AX, BX` (échange AX et BX).
- **PUSH (Empiler)** :
  - Syntaxe : `PUSH source`
  - Fonction : Pousse des données 16 bits sur la pile, décrémente SP de 2.
  - Exemple : `PUSH AX` (sauvegarde AX sur la pile).
- **POP (Dépiler)** :
  - Syntaxe : `POP destination`
  - Fonction : Dépile des données 16 bits de la pile vers la destination, incrémente SP de 2.
  - Exemple : `POP BX` (restaure BX à partir de la pile).
- **LEA (Charger l'adresse effective)** :
  - Syntaxe : `LEA destination, source`
  - Fonction : Charge l'adresse d'un opérande mémoire dans un registre.
  - Exemple : `LEA BX, [SI+4]` (charge l'adresse de DS:SI+4 dans BX).
- **IN/OUT** :
  - Syntaxe : `IN destination, port` ; `OUT port, source`
  - Fonction : Transfère des données vers/depuis les ports d'E/S.
  - Exemple : `IN AL, 60h` (lit le port du clavier) ; `OUT 61h, AL` (écrit sur le port du haut-parleur).

#### b. Instructions arithmétiques
Elles effectuent des opérations mathématiques, mettant à jour les drapeaux (par exemple, ZF, CF, SF, OF) en fonction des résultats.

- **ADD (Additionner)** :
  - Syntaxe : `ADD destination, source`
  - Fonction : Additionne la source à la destination, stocke le résultat dans la destination.
  - Exemple : `ADD AX, BX` (AX = AX + BX).
- **SUB (Soustraire)** :
  - Syntaxe : `SUB destination, source`
  - Fonction : Soustrait la source de la destination.
  - Exemple : `SUB CX, 10` (CX = CX - 10).
- **INC (Incrémenter)** :
  - Syntaxe : `INC destination`
  - Fonction : Incrémente la destination de 1.
  - Exemple : `INC BX` (BX = BX + 1).
- **DEC (Décrémenter)** :
  - Syntaxe : `DEC destination`
  - Fonction : Décrémente la destination de 1.
  - Exemple : `DEC CX` (CX = CX - 1).
- **MUL (Multiplier, non signé)** :
  - Syntaxe : `MUL source`
  - Fonction : Multiplie AL (8 bits) ou AX (16 bits) par la source, stocke le résultat dans AX ou DX:AX.
  - Exemple : `MUL BX` (DX:AX = AX * BX).
- **DIV (Diviser, non signé)** :
  - Syntaxe : `DIV source`
  - Fonction : Divise AX (8 bits) ou DX:AX (16 bits) par la source, stocke le quotient dans AL/AX, le reste dans AH/DX.
  - Exemple : `DIV BX` (AX = DX:AX / BX, DX = reste).
- **ADC (Additionner avec retenue)** et **SBB (Soustraire avec emprunt)** :
  - Fonction : Gèrent l'arithmétique multi-mot en utilisant le drapeau de retenue.
  - Exemple : `ADC AX, BX` (AX = AX + BX + CF).

#### c. Instructions logiques
Elles effectuent des opérations bit à bit et manipulent les données binaires.

- **AND (ET bit à bit)** :
  - Syntaxe : `AND destination, source`
  - Fonction : Effectue un ET bit à bit, stocke le résultat dans la destination.
  - Exemple : `AND AX, 0FFh` (efface l'octet supérieur de AX).
- **OR (OU bit à bit)** :
  - Syntaxe : `OR destination, source`
  - Fonction : Effectue un OU bit à bit.
  - Exemple : `OR BX, 1000h` (définit le bit 12 dans BX).
- **XOR (OU exclusif bit à bit)** :
  - Syntaxe : `XOR destination, source`
  - Fonction : Effectue un OU exclusif bit à bit.
  - Exemple : `XOR AX, AX` (met AX à 0).
- **NOT (NON bit à bit)** :
  - Syntaxe : `NOT destination`
  - Fonction : Inverse tous les bits de la destination.
  - Exemple : `NOT BX` (BX = ~BX).
- **SHL/SHR (Décalage à gauche/droite)** :
  - Syntaxe : `SHL destination, count` ; `SHR destination, count`
  - Fonction : Décale les bits vers la gauche/droite, remplit avec 0 (SHR) ou le bit de signe (SAL/SAR).
  - Exemple : `SHL AX, 1` (AX = AX * 2).
- **ROL/ROR (Rotation à gauche/droite)** :
  - Fonction : Fait tourner les bits, en bouclant à travers le drapeau de retenue.
  - Exemple : `ROL BX, 1` (fait tourner BX à gauche de 1 bit).

#### d. Instructions de contrôle de flux
Elles modifient la séquence d'exécution du programme, permettant les sauts, les boucles et les sous-routines.

- **JMP (Saut)** :
  - Syntaxe : `JMP label`
  - Fonction : Saute inconditionnellement vers un label.
  - Exemple : `JMP start` (aller au label `start`).
  - Variantes :
    - Saut court (±127 octets).
    - Saut proche (dans le segment).
    - Saut loin (segment différent).
- **Sauts conditionnels** :
  - Syntaxe : `Jcc label` (par exemple, JZ, JNZ, JC, JNC)
  - Fonction : Saute en fonction de l'état des drapeaux.
  - Exemples :
    - `JZ loop_end` (saute si le drapeau zéro est défini).
    - `JC error` (saute si le drapeau de retenue est défini).
    - Conditions courantes : JZ (zéro), JNZ (non zéro), JS (signe), JO (dépassement).
- **LOOP (Boucle)** :
  - Syntaxe : `LOOP label`
  - Fonction : Décrémente CX, saute au label si CX ≠ 0.
  - Exemple : `LOOP process` (répète jusqu'à ce que CX = 0).
  - Variantes :
    - `LOOPE/LOOPZ` : Boucle si CX ≠ 0 et ZF = 1.
    - `LOOPNE/LOOPNZ` : Boucle si CX ≠ 0 et ZF = 0.
- **CALL (Appeler une sous-routine)** :
  - Syntaxe : `CALL label`
  - Fonction : Pousse l'adresse de retour sur la pile, saute vers la sous-routine.
  - Exemple : `CALL compute_sum` (appelle la sous-routine).
- **RET (Retour)** :
  - Syntaxe : `RET`
  - Fonction : Dépile l'adresse de retour de la pile, reprend l'exécution.
  - Exemple : `RET` (retourne de la sous-routine).
- **INT (Interruption)** :
  - Syntaxe : `INT number`
  - Fonction : Déclenche une interruption logicielle, appelant une routine de service d'interruption (ISR).
  - Exemple : `INT 21h` (appel système DOS).
- **IRET (Retour d'interruption)** :
  - Fonction : Retourne d'une ISR, restaurant les drapeaux et l'adresse de retour.

---

### 2. Programmation en langage d'assemblage

Les programmes en langage d'assemblage sont écrits sous forme d'instructions lisibles par l'homme qui sont assemblées en code machine. Le 8086 utilise un **modèle de mémoire segmenté**, avec des segments de code, de données et de pile définis explicitement.

#### a. Structure d'un programme
Un programme assembleur 8086 typique comprend :
- **Directives** : Instructions pour l'assembleur (par exemple, NASM, MASM).
  - `SEGMENT` : Définit les segments de code, de données ou de pile.
  - `ORG` : Définit l'adresse d'origine.
  - `DB/DW` : Définit des données octet/mot.
- **Instructions** : Opérations du CPU (par exemple, MOV, ADD).
- **Labels** : Marquent des emplacements pour les sauts ou les données.
- **Commentaires** : Expliquent le code (par exemple, `; commentaire`).

**Exemple de structure de programme (syntaxe MASM)** :
```asm
.model small
.stack 100h
.data
    message db 'Hello, World!$'
.code
main proc
    mov ax, @data    ; Initialiser DS
    mov ds, ax
    mov dx, offset message ; Charger l'adresse du message
    mov ah, 09h      ; Fonction DOS d'impression de chaîne
    int 21h          ; Appeler l'interruption DOS
    mov ah, 4Ch      ; Quitter le programme
    int 21h
main endp
end main
```

#### b. Structures séquentielles
Le code séquentiel exécute les instructions dans l'ordre, sans sauts ni boucles.

**Exemple : Additionner deux nombres**
```asm
mov ax, 5        ; AX = 5
mov bx, 10       ; BX = 10
add ax, bx       ; AX = AX + BX (15)
mov [result], ax ; Stocke le résultat en mémoire
```
- Les instructions s'exécutent les unes après les autres.
- Courant pour les calculs simples ou l'initialisation de données.

#### c. Structures de branchement
Le branchement utilise des sauts conditionnels/inconditionnels pour modifier le flux du programme en fonction de conditions.

**Exemple : Comparer et brancher**
```asm
mov ax, 10       ; AX = 10
cmp ax, 15       ; Compare AX avec 15
je equal         ; Saute si AX == 15
mov bx, 1        ; Sinon, BX = 1
jmp done
equal:
    mov bx, 0    ; BX = 0 si égal
done:
    ; Continuer le programme
```
- **CMP** : Définit les drapeaux basés sur la soustraction (AX - 15).
- **JE** : Saute si ZF = 1 (égal).
- Utile pour la logique si-alors-sinon.

#### d. Structures de boucle
Les boucles répètent les instructions jusqu'à ce qu'une condition soit remplie, utilisant souvent `LOOP` ou des sauts conditionnels.

**Exemple : Somme des nombres de 1 à 10**
```asm
mov cx, 10       ; Compteur de boucle = 10
mov ax, 0        ; Somme = 0
sum_loop:
    add ax, cx   ; Ajoute CX à la somme
    loop sum_loop ; Décrémente CX, boucle si CX ≠ 0
    ; AX = 55 (1 + 2 + ... + 10)
```
- `LOOP` simplifie l'itération basée sur un compteur.
- Alternative : Utiliser `CMP` et `JNZ` pour des conditions personnalisées.

**Exemple avec boucle conditionnelle**
```asm
mov ax, 0        ; Compteur
mov bx, 100      ; Limite
count_up:
    inc ax       ; AX++
    cmp ax, bx   ; Compare avec 100
    jle count_up ; Saute si AX <= 100
```
- Flexible pour les boucles non basées sur un compteur.

#### e. Sous-routines
Les sous-routines modularisent le code, permettant la réutilisation via `CALL` et `RET`.

**Exemple : Mettre un nombre au carré**
```asm
main:
    mov ax, 4    ; Entrée
    call square  ; Appeler la sous-routine
    ; AX = 16
    jmp exit
square:
    push bx      ; Sauvegarder BX
    mov bx, ax   ; Copier AX
    mul bx       ; AX = AX * BX
    pop bx       ; Restaurer BX
    ret          ; Retourner
exit:
    ; Fin du programme
```
- **PUSH/POP** : Sauvegardent/restaurent les registres pour éviter les effets de bord.
- La pile gère automatiquement les adresses de retour.

---

### 3. Routines de service d'interruption (ISR)

Les interruptions permettent au CPU de répondre à des événements externes ou internes (par exemple, entrée clavier, ticks d'horloge) en mettant en pause le programme en cours et en exécutant une ISR.

#### Mécanisme d'interruption
- **Table des vecteurs d'interruption (IVT)** :
  - Située en mémoire 0000:0000h–0000:03FFh.
  - Stocke les adresses des ISR pour 256 types d'interruption (0–255).
  - Chaque entrée : Segment:Offset (4 octets).
- **Types** :
  - **Interruptions matérielles** : Déclenchées par des périphériques (par exemple, IRQ).
  - **Interruptions logicielles** : Déclenchées par l'instruction `INT` (par exemple, INT 21h pour DOS).
  - **Exceptions** : Erreurs du CPU (par exemple, division par zéro).
- **Processus** :
  1. Une interruption se produit.
  2. Le CPU sauvegarde les drapeaux, CS et IP sur la pile.
  3. Saute vers l'ISR via l'IVT.
  4. L'ISR s'exécute, se termine par `IRET` pour restaurer l'état.

#### Écrire une ISR
Les ISR doivent :
- Préserver les registres (PUSH/POP).
- Gérer l'interruption rapidement.
- Se terminer par `IRET`.

**Exemple : ISR d'horloge personnalisée**
```asm
.data
old_vec dw 2 dup(0) ; Stocker l'ancien vecteur d'interruption
.code
install_isr:
    cli             ; Désactiver les interruptions
    mov ax, 0
    mov es, ax      ; ES = 0 (segment IVT)
    mov bx, 1Ch*4   ; Interruption d'horloge (1Ch)
    mov ax, es:[bx] ; Sauvegarder l'ancien vecteur
    mov old_vec, ax
    mov ax, es:[bx+2]
    mov old_vec+2, ax
    mov ax, offset my_isr ; Définir le nouveau vecteur
    mov es:[bx], ax
    mov ax, cs
    mov es:[bx+2], ax
    sti             ; Activer les interruptions
    ret
my_isr:
    push ax
    inc word ptr [counter] ; Incrémenter le compteur
    pop ax
    iret            ; Retourner de l'interruption
```
- Accroche l'interruption d'horloge (1Ch, ~18,2 Hz).
- Incrémente une variable compteur.
- Préserve les registres et utilise `IRET`.

**Exemple : Interruption DOS (INT 21h)**
```asm
mov ah, 09h      ; Fonction d'impression de chaîne
mov dx, offset msg ; Adresse de la chaîne terminée par '$'
int 21h          ; Appeler DOS
```
- INT 21h fournit des services du système d'exploitation (par exemple, E/S, gestion de fichiers).
- AH spécifie le code de la fonction.

#### Notes pratiques
- **Sauvegarde de l'état** : Les ISR doivent préserver tous les registres pour éviter de corrompre le programme principal.
- **Priorité** : Les interruptions matérielles peuvent en interrompre d'autres (gérées par le PIC).
- **Débogage** : Utiliser des outils comme DEBUG.COM ou des émulateurs modernes (par exemple, DOSBox, Bochs).

---

### Exemple de programme : Calcul de factorielle
Ce programme calcule la factorielle d'un nombre (par exemple, 5! = 120) en utilisant une boucle et une sous-routine.

```asm
.model small
.stack 100h
.data
    num dw 5        ; Nombre d'entrée
    result dw ?     ; Stocker le résultat
.code
main proc
    mov ax, @data
    mov ds, ax      ; Initialiser DS
    mov ax, num     ; Charger le nombre
    call factorial  ; Calculer la factorielle
    mov result, ax  ; Stocker le résultat
    mov ah, 4Ch     ; Quitter
    int 21h
main endp
factorial proc
    push bx
    mov bx, ax      ; BX = n
    mov ax, 1       ; AX = résultat
fact_loop:
    cmp bx, 1
    jle done        ; Si BX <= 1, sortir
    mul bx          ; AX = AX * BX
    dec bx          ; BX--
    jmp fact_loop
done:
    pop bx
    ret
factorial endp
end main
```
- **Logique** :
  - Entrée : num = 5.
  - Boucle : AX = AX * BX, BX-- jusqu'à BX = 1.
  - Résultat : AX = 5 * 4 * 3 * 2 * 1 = 120.
- **Caractéristiques** :
  - Sous-routine pour la modularité.
  - Pile pour la préservation des registres.
  - Structures séquentielles et de boucle.

---

### Bonnes pratiques
1. **Commenter le code** : L'assembleur est cryptique ; expliquez chaque étape.
2. **Minimiser l'utilisation des registres** : Évitez les écrasements inutiles.
3. **Tester de manière incrémentielle** : Utilisez des débogueurs pour tracer l'exécution.
4. **Gérer les cas limites** : Vérifiez les dépassements, zéro ou entrées négatives.
5. **Optimiser** : Réduisez les instructions (par exemple, utilisez XOR AX, AX au lieu de MOV AX, 0).

---

### Résumé
- **Jeu d'instructions 8086** :
  - **Transfert de données** : MOV, PUSH, POP pour déplacer les données.
  - **Arithmétique** : ADD, SUB, MUL pour les calculs.
  - **Logique** : AND, OR, XOR pour la manipulation des bits.
  - **Contrôle de flux** : JMP, LOOP, CALL pour le flux du programme.
- **Structures de programmation** :
  - **Séquentielle** : Exécution linéaire pour les tâches simples.
  - **Branchement** : Sauts conditionnels pour les décisions.
  - **Boucle** : LOOP ou Jcc pour la répétition.
  - **Sous-routines** : CALL/RET pour le code modulaire.
- **Interruptions** :
  - Les ISR gèrent les événements via l'IVT.
  - Préservent l'état, se terminent par IRET.
  - Utilisées pour les interruptions matérielles (par exemple, horloge) et logicielles (par exemple, DOS).

---

### Questions pratiques
1. Écrivez un programme pour inverser une chaîne en mémoire.
2. Implémentez une sous-routine pour vérifier si un nombre est premier.
3. Créez une ISR pour l'interruption clavier (INT 09h) pour compter les appuis sur les touches.
4. Expliquez la différence entre `JMP` et `CALL`.
5. Optimisez ce code : `MOV AX, 0; MOV BX, AX; ADD BX, 5`.

---

Ce tutoriel couvre les bases essentielles de la programmation assembleur 8086, avec des exemples et des explications pour développer des compétences pratiques. Si vous souhaitez explorer des instructions spécifiques, des techniques avancées (par exemple, les opérations sur les chaînes) ou des outils d'émulation, faites-le moi savoir !