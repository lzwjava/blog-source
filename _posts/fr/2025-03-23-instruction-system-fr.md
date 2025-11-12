---
audio: false
generated: true
lang: fr
layout: post
title: Système d'instruction – Un guide complet
translated: true
type: note
---

## **1. Introduction au système d'instructions**  
Une **Architecture de Jeu d'Instructions (ISA)** définit l'interface entre le logiciel et le matériel. Elle spécifie les instructions qu'un processeur peut exécuter, leurs formats et la façon dont elles interagissent avec la mémoire et les registres. Comprendre l'ISA est crucial à la fois pour la programmation (en particulier en langage d'assemblage) et pour la conception du matériel informatique.

---

## **2. Architecture de Jeu d'Instructions (ISA)**  
### **2.1 Qu'est-ce que l'ISA ?**  
L'**Architecture de Jeu d'Instructions (ISA)** est la partie de la conception du processeur qui gère l'exécution des instructions, y compris :  
- **Les types de données** (par exemple, les entiers, les nombres à virgule flottante, les caractères)  
- **Les registres** (emplacements de stockage temporaires à l'intérieur du CPU)  
- **Les méthodes d'accès à la mémoire** (comment les données sont récupérées et stockées)  
- **Les types d'instructions** (arithmétiques, logiques, de contrôle, E/S)  

### **2.2 Types d'ISA**  
1. **CISC (Complex Instruction Set Computing)**  
   - Une seule instruction peut effectuer plusieurs opérations.  
   - Exemple : l'architecture x86 (Intel, AMD).  
   - **Avantages :** Moins d'instructions par programme, plus facile à programmer en assembleur.  
   - **Inconvénients :** Exécution des instructions plus lente en raison de la complexité.  

2. **RISC (Reduced Instruction Set Computing)**  
   - Chaque instruction effectue une opération simple et s'exécute en un seul cycle.  
   - Exemple : ARM, MIPS, RISC-V.  
   - **Avantages :** Exécution plus rapide, matériel plus simple.  
   - **Inconvénients :** Plus d'instructions nécessaires pour les tâches complexes.  

---

## **3. Formats d'instructions**  
### **3.1 Qu'est-ce qu'un format d'instruction ?**  
Un **format d'instruction** définit la structure d'une instruction en mémoire. Il se compose des champs suivants :  
1. **Opcode (Code d'Opération) :** Spécifie l'opération (par exemple, ADD, LOAD, STORE).  
2. **Opérandes :** Spécifie les données (registres, adresses mémoire).  
3. **Mode d'adressage :** Spécifie comment accéder aux opérandes.  

### **3.2 Formats d'instructions courants**  
1. **Format Fixe :**  
   - Toutes les instructions ont la même taille (par exemple, 32 bits dans MIPS).  
   - Facile à décoder mais peut gaspiller de l'espace.  

2. **Format Variable :**  
   - Les instructions varient en taille (par exemple, x86, ARM).  
   - Utilisation efficace de la mémoire mais plus difficile à décoder.  

3. **Format Hybride :**  
   - Combinaison de formats fixes et variables (par exemple, les instructions ARM Thumb).  

### **3.3 Exemple de format d'instruction (Architecture MIPS)**  
Dans **MIPS**, une instruction a une longueur de 32 bits et possède trois formats principaux :  

1. **Type R (Type Registre)**
   ```
   | Opcode (6) | Rs (5) | Rt (5) | Rd (5) | Shamt (5) | Funct (6) |
   ```
   - Exemple : `add $t1, $t2, $t3`  
   - Signification : `$t1 = $t2 + $t3`  

2. **Type I (Type Immédiat)**
   ```
   | Opcode (6) | Rs (5) | Rt (5) | Immédiat (16) |
   ```
   - Exemple : `addi $t1, $t2, 10`  
   - Signification : `$t1 = $t2 + 10`  

3. **Type J (Type Saut)**
   ```
   | Opcode (6) | Adresse (26) |
   ```
   - Exemple : `j 10000` (Saut à l'adresse mémoire 10000)  

---

## **4. Modes d'adressage**  
Les **modes d'adressage** déterminent comment les opérandes sont accédés dans une instruction.  

### **4.1 Modes d'adressage courants**  
1. **Adressage Immédiat :** L'opérande est directement spécifié dans l'instruction.  
   - Exemple : `addi $t1, $t2, 10` (10 est une valeur immédiate)  

2. **Adressage par Registre :** L'opérande est stocké dans un registre.  
   - Exemple : `add $t1, $t2, $t3` (tous les opérandes sont dans des registres)  

3. **Adressage Direct :** L'instruction contient l'adresse mémoire de l'opérande.  
   - Exemple : `load $t1, 1000` (charge la valeur depuis l'adresse mémoire 1000)  

4. **Adressage Indirect :** L'adresse de l'opérande est stockée dans un registre.  
   - Exemple : `load $t1, ($t2)` (récupère la valeur à partir de l'adresse stockée dans `$t2`)  

5. **Adressage Indexé :** L'adresse est calculée en ajoutant un décalage à un registre.  
   - Exemple : `load $t1, 10($t2)` (récupère la valeur à partir de `$t2 + 10`)  

6. **Adressage Base+Décalage :** Un registre de base et un décalage déterminent l'adresse.  
   - Exemple : `lw $t1, 4($sp)` (récupère depuis `$sp + 4`)  

### **4.2 Importance des modes d'adressage**  
- **Utilisation Efficace de la Mémoire :** Différents modes d'adressage optimisent l'accès à la mémoire.  
- **Optimisation des Performances :** Certains modes sont plus rapides que d'autres.  
- **Flexibilité :** Prend en charge différents styles de programmation (par exemple, l'arithmétique des pointeurs).  

---

## **5. Programmation en langage d'assemblage**  
### **5.1 Qu'est-ce que le langage d'assemblage ?**  
Le **langage d'assemblage** est un langage de programmation de bas niveau qui correspond directement au code machine.  

### **5.2 Structure d'un programme assembleur**  
Un programme assembleur de base se compose de :  
- **Directives :** Instructions pour l'assembleur (par exemple, `.data`, `.text`).  
- **Instructions :** Opérations réelles exécutées par le CPU.  

### **5.3 Programme assembleur MIPS basique**  
```assembly
.data
msg: .asciiz "Hello, World!"

.text
.globl main
main:
    li $v0, 4       # Charger le code du syscall pour print_string
    la $a0, msg     # Charger l'adresse de la chaîne
    syscall         # Afficher la chaîne

    li $v0, 10      # Syscall de sortie
    syscall
```
- La section `.data` stocke les variables et les chaînes de caractères.  
- La section `.text` contient les instructions exécutables.  
- `syscall` est utilisé pour interagir avec le système d'exploitation.  

### **5.4 Instructions assembleur clés**

| Instruction | Signification | Exemple |
|------------|---------|---------|
| `add` | Additionner deux registres | `add $t1, $t2, $t3` |
| `sub` | Soustraire deux registres | `sub $t1, $t2, $t3` |
| `lw` | Charger un mot depuis la mémoire | `lw $t1, 0($t2)` |
| `sw` | Stocker un mot en mémoire | `sw $t1, 0($t2)` |
| `beq` | Branchement si égal | `beq $t1, $t2, label` |
| `j` | Sauter à une adresse | `j label` |

### **5.5 Assembleur vs Langages de Haut Niveau**

| Caractéristique | Assembleur | Langage de Haut Niveau (C, Python) |
|---------|---------|------------------------------|
| **Vitesse** | Plus rapide | Plus lent (plus de surcharge) |
| **Contrôle** | Contrôle total du matériel | Abstrait du matériel |
| **Difficulté** | Syntaxe complexe | Syntaxe plus facile |
| **Portabilité** | Spécifique au CPU | Fonctionne sur différents CPU |

---

## **6. Résumé**  
### **Points clés à retenir**
- **L'ISA définit comment le logiciel interagit avec le matériel.**
- **Les formats d'instructions déterminent la structure d'une instruction.**
- **Les modes d'adressage spécifient comment les opérandes sont accédés.**
- **Le langage d'assemblage contrôle directement le CPU et la mémoire.**

### **Exercices pratiques**
1. Convertissez l'instruction MIPS `addi $t1, $t2, 5` en format binaire.  
2. Écrivez un programme assembleur pour additionner deux nombres stockés dans des registres.  
3. Expliquez la différence entre l'adressage direct et indirect avec des exemples.  

---

Comprendre le **système d'instructions** est essentiel pour apprendre **l'organisation et l'architecture des ordinateurs**, surtout si vous visez à travailler avec **la programmation de bas niveau, les systèmes embarqués ou la conception de processeurs**. Faites-moi savoir si vous avez besoin de plus d'exemples ou d'explications ! 🚀