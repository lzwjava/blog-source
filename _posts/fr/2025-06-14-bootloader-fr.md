---
audio: false
generated: true
lang: fr
layout: post
title: Brûler un Bootloader
translated: true
type: note
---

Graver un bootloader sur un Arduino Uno R3 est nécessaire si le microcontrôleur (ATmega328P) est vierge, corrompu ou doit être remplacé. Ce processus programme la puce avec le firmware requis pour communiquer avec l'IDE Arduino et exécuter des sketches. Voici un guide étape par étape pour graver le bootloader en utilisant des méthodes courantes.

---

### **Matériel requis**
- **Arduino Uno R3** (la carte cible avec l'ATmega328P à programmer).
- **Programmeur** : L'un des éléments suivants :
  - Une autre carte Arduino fonctionnelle (par exemple, un autre Uno R3) comme "Arduino as ISP".
  - Un programmeur dédié comme **USBasp**, **AVRISP mkII** ou **Atmel-ICE**.
- **Arduino IDE** (téléchargeable sur [arduino.cc](https://www.arduino.cc/en/software)).
- **Câbles de liaison (jumper wires)** (si vous utilisez Arduino as ISP).
- **Câble USB** (pour connecter le programmeur ou l'Arduino à votre ordinateur).

---

### **Méthode 1 : Utiliser une autre Arduino (Arduino as ISP)**

Cette méthode utilise une seconde carte Arduino (par exemple, un autre Uno R3) comme programmeur In-System (ISP) pour graver le bootloader.

#### **Étapes**
1. **Préparer l'Arduino programmeur** :
   - Connectez la seconde Arduino (le programmeur) à votre ordinateur via USB.
   - Ouvrez l'IDE Arduino, allez dans **Fichier > Exemples > 11.ArduinoISP > ArduinoISP**, et téléversez ce sketch sur l'Arduino programmeur. Cela le transforme en ISP.

2. **Connecter les cartes** :
   - Câblez l'Arduino programmeur à l'Arduino Uno R3 cible (celui qui a besoin du bootloader) comme suit :
     - **Arduino programmeur** → **Arduino Uno R3 cible** :
       - 5V → 5V
       - GND → GND
       - Broche 10 → Reset
       - Broche 11 → Broche 11 (MOSI)
       - Broche 12 → Broche 12 (MISO)
       - Broche 13 → Broche 13 (SCK)
   - Alternativement, si l'Uno R3 cible possède un **connecteur ICSP**, connectez les broches ICSP correspondantes (MOSI, MISO, SCK, VCC, GND, Reset) directement en utilisant des câbles de liaison.

3. **Configurer l'IDE Arduino** :
   - Dans l'IDE Arduino, allez dans **Outils > Carte** et sélectionnez **Arduino Uno** (pour l'Uno R3 cible).
   - Allez dans **Outils > Programmeur** et sélectionnez **Arduino as ISP**.
   - Assurez-vous que le port correct pour l'Arduino programmeur est sélectionné sous **Outils > Port**.

4. **Graver le bootloader** :
   - Allez dans **Outils > Graver le bootloader**.
   - L'IDE utilisera l'Arduino programmeur pour flasher le bootloader sur l'ATmega328P de l'Uno R3 cible. Cela peut prendre une minute.
   - Si c'est réussi, vous verrez un message "Done burning bootloader". S'il y a une erreur, vérifiez les connexions et assurez-vous que l'Arduino programmeur exécute le sketch ArduinoISP.

5. **Tester la carte cible** :
   - Déconnectez l'Arduino programmeur et les câbles.
   - Connectez l'Uno R3 cible à votre ordinateur via USB.
   - Téléversez un sketch simple (par exemple, Blink depuis **Fichier > Exemples > 01.Basics > Blink**) pour confirmer que le bootloader fonctionne.

---

### **Méthode 2 : Utiliser un programmeur ISP dédié (par exemple, USBasp)**

Si vous avez un programmeur dédié comme un USBasp, le processus est plus simple et souvent plus fiable.

#### **Étapes**
1. **Connecter le programmeur** :
   - Connectez le USBasp (ou un programmeur similaire) à votre ordinateur via USB.
   - Connectez le programmeur au **connecteur ICSP** de l'Arduino Uno R3 cible en utilisant un câble ICSP 6 broches. Assurez-vous du bon sens d'orientation (la broche 1 est marquée d'un point ou d'une encoche sur le connecteur ICSP).

2. **Configurer l'IDE Arduino** :
   - Ouvrez l'IDE Arduino.
   - Allez dans **Outils > Carte** et sélectionnez **Arduino Uno**.
   - Allez dans **Outils > Programmeur** et sélectionnez votre programmeur (par exemple, **USBasp** ou **AVRISP mkII**).
   - Sélectionnez le port correct sous **Outils > Port** (le cas échéant, certains programmeurs ne nécessitent pas de sélection de port).

3. **Graver le bootloader** :
   - Allez dans **Outils > Graver le bootloader**.
   - L'IDE utilisera le programmeur pour flasher le bootloader. Cela prend environ 10 à 30 secondes.
   - Un message "Done burning bootloader" indique le succès. Si cela échoue, vérifiez les connexions et assurez-vous que le programmeur est reconnu par votre ordinateur.

4. **Tester la carte** :
   - Déconnectez le programmeur.
   - Connectez l'Uno R3 à votre ordinateur via USB et téléversez un sketch de test (par exemple, Blink) pour vérifier son fonctionnement.

---

### **Conseils de dépannage**
- **Messages d'erreur** : Si vous obtenez des erreurs comme "avrdude: stk500_getsync()" ou "not in sync", vérifiez :
  - Toutes les connexions (câbles ou câble ICSP).
  - Que l'Arduino programmeur exécute le sketch ArduinoISP (Méthode 1).
  - Que le bon programmeur est sélectionné dans l'IDE.
- **Problèmes de pilote** : Pour USBasp ou d'autres programmeurs, assurez-vous que les pilotes sont installés (par exemple, Zadig pour USBasp sous Windows).
- **Microcontrôleur vierge** : Si l'ATmega328P est neuf ou vierge, il peut avoir besoin d'un cristal externe 16 MHz et de deux condensateurs 22pF connectés aux broches 9 et 10 (XTAL1/XTAL2) s'ils ne sont pas déjà présents sur la carte Uno R3.
- **Alimentation** : Assurez-vous que la carte cible est alimentée (via USB ou VIN) pendant la programmation.

---

### **Notes supplémentaires**
- **Pourquoi graver un bootloader ?** : Le bootloader permet à l'Arduino Uno R3 de communiquer avec l'IDE Arduino via USB pour téléverser des sketches. Sans lui, la carte ne répondra pas aux téléversements USB.
- **Type de bootloader** : L'Uno R3 utilise le **bootloader Optiboot**, qui est compact et prend en charge des téléversements plus rapides par rapport aux anciens bootloaders.
- **Remplacer le microcontrôleur** : Si vous remplacez l'ATmega328P, assurez-vous qu'il s'agit d'un ATmega328P-PU (boîtier DIP) pour le socket de l'Uno R3. Les versions CMS nécessitent une soudure avancée.
- **Outils alternatifs** : Vous pouvez également utiliser **AVRDUDE** ou **PlatformIO** pour graver le bootloader, mais l'IDE Arduino est le plus simple pour les débutants.

Si vous avez besoin de précisions sur une étape ou d'aide avec un programmeur spécifique, faites-le moi savoir !