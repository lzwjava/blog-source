---
audio: false
generated: true
lang: es
layout: post
title: Cómo Funciona AlphaFold
translated: true
type: note
---

Adentrémonos en cómo funciona **AlphaFold**, desarrollado por DeepMind: un sistema de IA revolucionario que predice estructuras de proteínas con una precisión notable. Desglosaré sus conceptos centrales, el problema que resuelve, su arquitectura y los pasos que sigue para pasar de la secuencia de aminoácidos de una proteína a una estructura 3D. Esto será exhaustivo pero digerible, con suficiente detalle para satisfacer la curiosidad sin ahogarnos en jerga técnica.

---

### El Problema: El Plegamiento de Proteínas

Las proteínas son los caballos de batalla de la vida, formadas por cadenas de aminoácidos que se pliegan en formas 3D específicas para realizar sus funciones (por ejemplo, enzimas, anticuerpos). El **problema del plegamiento de proteínas** consiste en descifrar cómo una secuencia de aminoácidos (por ejemplo, "AGHKL...") se pliega en su estructura 3D única, determinada por interacciones físicas y químicas. Tradicionalmente, esto se resolvía experimentalmente (por ejemplo, con cristalografía de rayos X), un proceso lento y costoso, o computacionalmente, lo que era impreciso para proteínas complejas. AlphaFold cambia esto prediciendo estructuras únicamente a partir de secuencias, rivalizando con la precisión experimental.

---

### La Evolución de AlphaFold

- **AlphaFold 1 (2018)**: Debutó en CASP13 (Critical Assessment of Structure Prediction), usando una combinación de machine learning y modelado basado en física. Era bueno pero limitado.
- **AlphaFold 2 (2020)**: Un salto adelante en CASP14, logrando una precisión casi experimental (puntuación GDT_TS media ~90). Prescindió de gran parte del enfoque basado en física por un sistema completamente impulsado por IA.
- **AlphaFold 3 (2024)**: Se expande para predecir interacciones proteína-ligando y otras biomoléculas, pero nos centraremos en AlphaFold 2, ya que es el más documentado y fundamental.

---

### Cómo Funciona AlphaFold (2): El Panorama General

AlphaFold 2 toma una secuencia de aminoácidos y genera una estructura 3D mediante:
1. Aprovechar **datos