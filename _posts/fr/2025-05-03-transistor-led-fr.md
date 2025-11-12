---
audio: false
generated: true
lang: fr
layout: post
title: Circuit à DEL avec un transistor
translated: true
type: note
---

Voici un tutoriel basé sur la vidéo YouTube que vous avez fournie, expliquant comment utiliser un transistor pour contrôler un circuit à LED.

**Objectif :** Apprendre à utiliser un transistor comme interrupteur pour allumer et éteindre une LED à l'aide d'un signal de faible courant.

**Informations de base :**

* Les transistors permettent à un courant plus important de circuler entre leur collecteur et leur émetteur, contrôlé par un plus petit courant circulant de la base vers l'émetteur.
* Le courant du collecteur peut être considérablement plus important que le courant de base (par exemple, 100 fois).
* Les LED nécessitent généralement une quantité de courant spécifique (par exemple, 20 mA) pour s'illuminer correctement.

**Étapes :**

1.  **Configurer le circuit de base de la LED :** Connectez une alimentation de 5V, une LED, une résistance (comme 220 ohms) et le transistor en série. La résistance est cruciale pour limiter le courant circulant vers la LED. Le transistor fonctionnera comme l'interrupteur dans ce circuit.
2.  **Connecter le transistor :** Identifiez les broches émetteur, base et collecteur de votre transistor. Connectez la broche émetteur à la masse. Connectez la broche collecteur dans le circuit entre la résistance (et la LED) et l'émetteur.
3.  **Connecter le signal de contrôle :** Connectez la borne positive de votre signal de contrôle à la broche de base du transistor. Connectez la masse du signal de contrôle à la broche émetteur (qui est également connectée à la masse du circuit principal).
4.  **Observer le résultat :** Lorsque le signal de contrôle est actif (allumé), un petit courant circulera de la base vers l'émetteur. Ce petit courant de base permet à un courant beaucoup plus important de circuler du collecteur vers l'émetteur, ce qui fait que la LED s'allume brillamment. Lorsque le signal de contrôle est inactif (éteint), aucun courant ne circule de la base vers l'émetteur, le transistor s'éteint et la LED s'éteint.

**Concepts clés :**

* **Amplification du courant :** Les transistors peuvent amplifier un petit courant de base pour contrôler un courant de collecteur beaucoup plus important.
* **Interrupteur contrôlé par le courant :** Les transistors fonctionnent comme des interrupteurs où un petit courant d'entrée dicte l'écoulement d'un courant plus important.

En mettant en œuvre ce circuit, vous pouvez utiliser efficacement un petit signal de contrôle pour gérer un circuit qui nécessite un courant plus élevé, comme celui alimentant une LED.
http://googleusercontent.com/youtube_content/0