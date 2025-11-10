---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Problème de luminosité du ZBook non résolu
translated: true
type: note
---

Sur un **poste de travail HP ZBook**, la luminosité de l'écran peut généralement être ajustée de plusieurs façons, mais elle peut parfois ne pas fonctionner en raison de conflits de pilotes, de matériel ou de paramètres. Voici un guide structuré :

---

### Méthodes pour ajuster la luminosité

1. **Raccourcis clavier**

   * La plupart des ordinateurs portables ZBook utilisent **Fn + F3/F4** (ou les touches avec une icône de soleil) pour diminuer/augmenter la luminosité.
   * Assurez-vous que le **verrouillage Fn** n'est pas inversé (certains modèles nécessitent d'appuyer simplement sur F3/F4 si le verrouillage Fn est activé).

2. **Paramètres Windows**

   * Allez dans **Démarrer → Paramètres → Système → Affichage**.
   * Sous *Luminosité et couleur*, faites glisser le **curseur de luminosité**.

3. **Centre de maintenance**

   * Appuyez sur **Win + A** pour ouvrir les paramètres rapides.
   * Utilisez le curseur de luminosité en bas.

4. **Prise en charge des touches de raccourci HP / HP Command Center**

   * Certains ZBook ont besoin du pilote **Prise en charge des touches de raccourci HP** ou de l'application HP Command Center pour que les touches de fonction fonctionnent correctement.

---

### Pourquoi le contrôle de la luminosité ne fonctionne parfois pas

1. **Différences de type d'affichage**

   * Si votre ZBook est connecté à un **moniteur externe**, la luminosité est contrôlée via les boutons matériels/le menu OSD du moniteur, et non par Windows.
   * Certains écrans de workstation (panneaux DreamColor) utilisent des **pilotes spéciaux** qui peuvent remplacer les contrôles par défaut de Windows.

2. **Problèmes de pilotes**

   * Des pilotes **Intel Graphics** ou **NVIDIA/AMD** obsolètes ou manquants peuvent bloquer le contrôle de la luminosité.
   * Le pilote de secours "Pilote d'affichage de base Microsoft" supprimera les options de luminosité.

3. **Paramètres du mode de gestion de l'alimentation**

   * Dans de rares cas, la gestion de l'alimentation ou les paramètres de luminosité adaptative peuvent interférer.
   * Vérifiez : **Panneau de configuration → Options d'alimentation → Modifier les paramètres du mode → Paramètres avancés → Affichage → Activer la luminosité adaptative**.

4. **BIOS/microprogramme**

   * Certains ZBook ont besoin de mises à jour du BIOS pour que les touches de raccourci de luminosité fonctionnent de manière cohérente.
   * Dans le BIOS, vérifiez que le **Mode touches d'action** est activé (pour que la luminosité fonctionne sans appuyer sur Fn).

---

### Liste de vérification pour la résolution

* Mettez à jour le pilote **Prise en charge des touches de raccourci HP** depuis le site du Support HP.
* Mettez à jour les **pilotes graphiques Intel/NVIDIA/AMD**.
* Assurez-vous que vous ajustez la luminosité sur l'**écran intégré**, et non sur un moniteur externe.
* Vérifiez les paramètres du BIOS pour le **Mode touches d'action**.
* Désactivez ou activez la **luminosité adaptative** si la luminosité se comporte étrangement.
* Redémarrez après les mises à jour des pilotes — les contrôles de luminosité réapparaissent parfois après un redémarrage.

---

👉 Souhaitez-vous que je vous donne des **instructions détaillées pour la mise à jour des pilotes pour HP ZBook** (Intel/NVIDIA/AMD + pilote HP Hotkey), afin que vous puissiez résoudre le problème définitivement ?