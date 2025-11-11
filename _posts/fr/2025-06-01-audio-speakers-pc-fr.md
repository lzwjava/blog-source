---
audio: false
generated: true
lang: fr
layout: post
title: Branchement de haut-parleurs audio sur un PC
translated: true
type: note
---

Pour connecter des enceintes audio à votre ordinateur en utilisant la sortie RCA (ou "RS out") de la carte mère, suivez ces étapes. Notez que la carte mère MSI MAG B760M Mortar WiFi n'a généralement pas de sorties RCA directement, car la plupart des cartes mères modernes utilisent des prises audio 3.5mm ou HDMI pour la sortie audio. Cependant, je suppose que vous faites référence à la sortie audio de la carte mère (probablement une prise 3.5mm étiquetée pour les enceintes arrière ou line-out) ou à un adaptateur/convertisseur RCA.

### Étapes pour connecter des enceintes audio avec une entrée RCA :

1. **Identifier la sortie audio sur la carte mère** :
   - Vérifiez le panneau I/O arrière de votre carte mère MSI MAG B760M Mortar WiFi. Il a généralement plusieurs prises audio 3.5mm, dont une verte (line-out) pour les enceintes stéréo ou une sortie pour le caisson de basses/centre (orange) pour les configurations surround.
   - Si vos enceintes ont des entrées RCA (connecteurs rouge et blanc), vous aurez probablement besoin d'un adaptateur ou d'un convertisseur.

2. **Vérifier les besoins des enceintes** :
   - Confirmez si vos enceintes sont **amplifiées** (actives, avec un amplificateur intégré) ou **passives** (nécessitant un amplificateur externe).
     - **Enceintes amplifiées** : Peuvent se connecter directement à la sortie audio de la carte mère avec le bon câble ou adaptateur.
     - **Enceintes passives** : Nécessitent un amplificateur ou un récepteur externe avec des entrées RCA.

3. **Obtenir le bon câble/adaptateur** :
   - Si vos enceintes ont des entrées RCA, vous aurez besoin d'un **câble 3.5mm vers RCA** ou d'un adaptateur :
     - **Câble mâle 3.5mm vers RCA mâle** : Connecte la prise line-out verte 3.5mm de la carte mère (ou une autre sortie audio désignée) aux entrées RCA de vos enceintes ou amplificateur.
     - **Adaptateur femelle 3.5mm vers RCA mâle** : Si vous avez déjà un câble RCA, vous pouvez utiliser un adaptateur femelle 3.5mm vers RCA mâle.
   - Exemple de produit : Un câble 3.5mm vers RCA (similaire au câble SATA Cable Matters que vous avez listé, mais pour l'audio). Ils sont largement disponibles pour 10-50 CNY sur JD.com.

4. **Connecter les enceintes** :
   - **Pour les enceintes amplifiées** :
     - Branchez l'extrémité 3.5mm du câble dans la prise line-out verte du panneau I/O arrière de la carte mère.
     - Connectez les extrémités RCA (rouge et blanc) aux entrées RCA correspondantes sur vos enceintes.
     - Allumez les enceintes et assurez-vous que leur volume est augmenté.
   - **Pour les enceintes passives** :
     - Connectez l'extrémité 3.5mm à la prise line-out de la carte mère.
     - Branchez les extrémités RCA dans les entrées RCA d'un amplificateur ou récepteur externe.
     - Connectez les enceintes passives aux borniers haut-parleurs de l'amplificateur (généralement via un câble haut-parleur, pas un RCA).
     - Allumez l'amplificateur et ajustez ses paramètres.

5. **Configurer les paramètres audio** :
   - Démarrez votre ordinateur et assurez-vous que les enceintes sont allumées.
   - Sous Windows :
     - Faites un clic droit sur l'icône du haut-parleur dans la barre des tâches et sélectionnez **Sons** ou **Paramètres audio**.
     - Dans l'onglet **Lecture**, sélectionnez le périphérique de sortie (par exemple, "Haut-parleurs" ou "Realtek Audio") et définissez-le comme périphérique par défaut.
     - Si vous utilisez le son surround, allez dans **Propriétés > Avancé** et configurez la configuration des enceintes (par exemple, stéréo ou 5.1 surround).
   - Installez les derniers **pilotes Realtek Audio** pour votre carte mère MSI depuis le site web officiel de MSI ou JD.com s'ils ne sont pas déjà installés, pour garantir des performances audio optimales.

6. **Tester l'audio** :
   - Jouez un fichier audio (par exemple, de la musique ou une vidéo) pour vérifier la sortie son.
   - Ajustez les niveaux de volume sur les enceintes, l'amplificateur (si utilisé) et dans Windows.
   - S'il n'y a pas de son, vérifiez :
     - Les connexions des câbles sont sécurisées.
     - Le bon périphérique de lecture est sélectionné dans Windows.
     - La sortie audio de la carte mère est activée dans le BIOS (rarement désactivée, mais vérifiez les paramètres du BIOS MSI sous **Advanced > Integrated Peripherals** si nécessaire).

### Notes :
- **Audio de la carte mère** : La MSI MAG B760M Mortar WiFi utilise une puce audio Realtek, qui prend en charge une sortie audio de haute qualité via les prises 3.5mm. Les sorties RCA ne sont pas standard, donc vous utilisez probablement un adaptateur ou faites référence à la prise line-out.
- **Sorties alternatives** :
  - Si vos enceintes prennent en charge HDMI ou optique (S/PDIF), votre carte mère a également une sortie S/PDIF optique ou HDMI (via le GPU pour la vidéo+audio). Vérifiez si vos enceintes ou amplificateur les prennent en charge pour une qualité audio potentiellement meilleure.
  - Les sorties HDMI/DisplayPort du GPU RTX 4070 peuvent transmettre l'audio vers un moniteur ou un récepteur avec des enceintes, si vous préférez.
- **Coût** : Un câble ou adaptateur 3.5mm vers RCA est peu coûteux (10-50 CNY sur JD.com). Assurez-vous qu'il prend en charge l'audio (pas seulement les données, comme votre câble SATA).
- **Son surround** : Si vos enceintes font partie d'une configuration 5.1 ou 7.1, utilisez les prises 3.5mm supplémentaires (par exemple, orange pour le centre/caisson de basses, noir pour l'arrière) et configurez-les dans Windows.

Si vous précisez le modèle des enceintes ou si vous utilisez un amplificateur, je peux fournir des conseils plus spécifiques. Si vous vouliez dire une autre "RS out" (par exemple, un port ou un appareil spécifique), veuillez fournir des détails, et j'adapterai les instructions.