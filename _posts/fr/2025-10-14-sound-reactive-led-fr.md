---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Circuit à LED Réactif au Son
translated: true
type: note
---

### Circuit simple de LED réactives à la musique sur plaque d’essai

On dirait que tu te souviens d’un projet sympa de LED réactives au son datant de 2021 — en gros, un circuit où les LED pulsent ou « dansent » sur le rythme de la musique, détecté via un microphone ou une entrée audio. Les « lumières bulles » sont probablement juste des LED colorées sur la plaque d’essai, et la partie « volume baissé » pourrait faire référence au réglage de la sensibilité ou à l’utilisation d’un potentiomètre pour contrôler la luminosité/réponse des LED.

Pour une version très simple (pas besoin de microcontrôleur, juste des composants basiques), tu peux en construire une qui allume plusieurs LED en rythme avec la musique ou un son proche. Cela utilise un microphone électret (souvent listé comme un « haut-parleur » dans les tutoriels basiques, mais il agit ici comme un micro) pour capter l’audio, quelques diodes pour le traitement du signal, et des transistors implicitement via les zener pour piloter les LED. C’est compatible plaque d’essai et coûte moins de 10 $ en pièces.

#### Composants matériels nécessaires
Voici une liste minimale pour 6 LED (réduis si tu en veux moins) :

| Composant      | Valeur/Spécification | Quantité |
|----------------|----------------------|----------|
| Résistance     | 56Ω                  | 6        |
| Condensateur   | 470µF                | 2        |
| Diode          | 1N4007 (ou similaire)| 2        |
| Diode Zener    | 1N4148               | 5        |
| Microphone électret (petit haut-parleur/micro) | 8Ω, 0.5W | 1 |
| LED            | Couleur au choix, 5mm | 6       |
| Plaque d’essai | Taille standard      | 1        |
| Fils de liaison | Mâle-mâle           | ~20      |
| Alimentation   | Pile 9V ou adaptateur 5-12V | 1 |

Optionnel pour le « contrôle du volume » : Ajoute un potentiomètre 10kΩ en série avec le micro pour ajuster la sensibilité (comme baisser le « volume » du signal d’entrée).

#### Aperçu rapide de la construction
1. **Configurer l’entrée micro** : Connecte le microphone entre l’alimentation et la masse via un condensateur (pour le signal audio AC). Cela capte les vibrations sonores et les convertit en impulsions électriques.
2. **Traitement du signal** : Utilise les diodes et les diodes zener dans une configuration redresseur/filtre pour convertir la forme d’onde audio en impulsions qui déclenchent les LED à différentes intensités selon le volume/la force du beat. Les zener protègent contre les pics de tension.
3. **Pilotage des LED** : Câble chaque LED en parallèle avec une résistance de 56Ω pour limiter le courant. Connecte le signal traité aux anodes des LED — les basses ou beats plus forts les feront clignoter plus brillamment/rapidement.
4. **Alimente le tout** : Branche sur 9V. Joue de la musique à proximité (le haut-parleur d’un téléphone fonctionne), et les LED devraient se synchroniser avec le rythme. Les condensateurs lissent le signal pour un effet « dansant ».
5. **Conseils plaque d’essai** : Place le micro d’un côté, les diodes/condensateurs au milieu, les LED en rangée de l’autre côté. Teste avec un multimètre pour la continuité avant de mettre sous tension.

Cela crée ce spectacle lumineux hypnotique sans pièces sophistiquées. Si tu veux ajouter un potentiomètre pour ajuster le volume, mets-le simplement en ligne sur le signal du micro — cela réduira la réponse des LED comme tu l’as mentionné.

Pour les schémas complets et les étapes, consulte ceux-ci :

[Simple Sound Reactive LEDs Circuit](https://www.circuits-diy.com/simple-sound-reactive-leds-circuit/)  
[Creating an Audio-Reactive LED Circuit (even simpler single-LED version)](https://www.instructables.com/Creating-An-Audio-Reactive-LED-Circuit/)