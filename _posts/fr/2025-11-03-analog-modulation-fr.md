---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'Techniques de modulation analogique : AM, FM, PM'
translated: true
type: note
---

### Techniques de modulation : AM, FM et PM

Dans le contexte des systèmes de communication et du traitement du signal, **AM**, **FM** et **PM** désignent des **techniques de modulation analogique** fondamentales. Ces méthodes sont utilisées pour encoder (ou "moduler") un signal porteur d'information (comme l'audio ou des données) sur une onde porteuse de plus haute fréquence pour une transmission efficace via des supports comme les ondes radio, les câbles ou les canaux sans fil. Bien qu'elles soient principalement associées à la communication analogique, elles peuvent interférer avec les conversions analogique-numérique (A/N) et numérique-analogique (N/A) dans les systèmes hybrides—par exemple, lorsque des signaux échantillonnés numériquement sont modulés pour la transmission ou lorsque des signaux modulés reçus sont numérisés.

Voici une description de chacune :

- **AM (Modulation d'Amplitude)** :  
  L'amplitude (la force ou la hauteur) de l'onde porteuse est variée proportionnellement à l'amplitude du signal modulant, tandis que la fréquence de la porteuse reste constante. C'est une technique simple et largement utilisée dans la radiodiffusion AM. Elle est sensible au bruit car les interférences affectent directement l'amplitude.  
  *Exemple* : Dans la transmission vocale, les sons plus forts augmentent les pics d'amplitude de la porteuse.

- **FM (Modulation de Fréquence)** :  
  La fréquence de l'onde porteuse est variée en fonction de l'amplitude et de la fréquence du signal modulant, tandis que l'amplitude de la porteuse reste constante. La FM offre une meilleure résistance au bruit et est courante dans la radio FM, le son de la télévision et les radios bidirectionnelles.  
  *Exemple* : Un audio plus aigu décale la fréquence de la porteuse vers le haut ou vers le bas proportionnellement.

- **PM (Modulation de Phase)** :  
  La phase (le timing ou le décalage) de l'onde porteuse est modifiée en fonction des variations du signal modulant, avec une amplitude et une fréquence constantes. La PM est similaire à la FM (elles sont mathématiquement liées via la différenciation) et est souvent utilisée dans les systèmes numériques comme la modulation par déplacement de phase (PSK), mais sous forme analogique, elle est appliquée dans certaines communications satellitaires et mobiles.  
  *Exemple* : Un changement dans le signal modulant avance ou retarde le cycle de la forme d'onde de la porteuse.

#### Relation avec les conversions A/N et N/A
Ces techniques sont plus directement liées à la transmission analogique, mais dans les systèmes modernes :
- Lors d'une **conversion N/A**, un signal numérique peut être reconstruit en une forme d'onde analogique modulante avant d'appliquer l'AM/FM/PM pour le préparer à une transmission RF (radiofréquence).
- Dans une **conversion A/N**, un signal modulé analogique reçu (par exemple, une radio FM) est d'abord démodulé, puis échantillonné et quantifié en forme numérique.

Pour des approfondissements, consultez les ressources sur la modulation analogique dans le traitement du signal.

[Techniques de modulation analogique](https://en.wikipedia.org/wiki/Modulation#Analog_modulation_methods)  
[Comparaison FM vs AM](https://www.electronics-tutorials.ws/accircuits/amplitude-modulator.html)