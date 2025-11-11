---
audio: false
generated: true
lang: fr
layout: post
title: Circuits intégrés TTL et CMOS
translated: true
type: note
---

## TTL (Transistor-Transistor Logic)

Le TTL a été développé au début des années 1960 par Texas Instruments, la série 7400 introduite en 1964 devenant une norme industrielle. Le TTL représentait une avancée significative par rapport aux technologies antérieures comme le DTL (Diode-Transistor Logic).

Développements clés dans l'histoire du TTL :
- Créé à l'origine par James L. Buie chez TRW en 1961
- Commercialisé par Texas Instruments avec leurs séries 5400/7400
- Le TTL standard a évolué vers des variantes améliorées :
  - TTL haute vitesse (série 74H)
  - TTL basse consommation (série 74L)
  - TTL Schottky (série 74S) qui réduisait le délai de propagation
  - Schottky basse consommation (série 74LS)
  - Schottky basse consommation avancée (série 74ALS)
  - Rapide (série 74F)

Le TTL a dominé la logique numérique de la fin des années 1960 jusqu'aux années 1970 et a été utilisé dans les premiers micro-ordinateurs, les calculatrices et divers équipements industriels. Son adoption généralisée était due à sa standardisation, sa fiabilité et son coût relativement faible.

## CMOS (Complementary Metal-Oxide-Semiconductor)

La technologie CMOS a été inventée en 1963 par Frank Wanlass chez Fairchild Semiconductor. La technologie est devenue commercialement significative dans les années 1970 et a finalement dépassé le TTL.

Développements clés dans l'histoire du CMOS :
- Brevet déposé par Frank Wanlass en 1963
- RCA a développé la famille logique CMOS série 4000 au début des années 1970
- Initialement plus lent que le TTL mais offrait une consommation d'énergie significativement plus faible
- La série CMOS haute densité (HC/HCT) introduite dans les années 1980 a amélioré la vitesse
- Le CMOS avancé (AC/ACT) a encore amélioré les performances à la fin des années 1980

Le CMOS est finalement devenu la technologie dominante pour plusieurs raisons :
- Consommation d'énergie beaucoup plus faible, particulièrement à l'arrêt
- Meilleure immunité au bruit
- Plage de tension de fonctionnement plus large
- Plus grande densité d'intégration
- Évolutivité de fabrication qui a permis à la loi de Moore de se poursuivre

Dans les années 1990, le CMOS était devenu la base de pratiquement tous les circuits intégrés numériques, des simples portes logiques aux microprocesseurs complexes. Les processeurs avancés, les puces mémoire et les ASIC d'aujourd'hui sont presque exclusivement basés sur le CMOS, bien qu'avec des améliorations significatives de la technologie de base.

Souhaitez-vous des informations plus spécifiques sur un aspect particulier de l'histoire du TTL ou du CMOS ?

---

# Fonctionnement des Circuits Intégrés TTL et CMOS

## TTL (Transistor-Transistor Logic)

Le TTL fonctionne en utilisant des transistors bipolaires à jonction (BJT) et opère grâce à un agencement spécifique de ces transistors :

1. **Étage d'entrée** : Utilise un transistor à émetteurs multiples où chaque émetteur sert d'entrée.

2. **Principe de fonctionnement** :
   - Lorsque toutes les entrées sont HAUTES (~5V), la jonction base-collecteur du transistor d'entrée est polarisée en direct, et sa jonction collecteur-émetteur est polarisée en inverse, ce qui éteint le transistor de sortie.
   - Lorsqu'une entrée passe à BASSE (~0V), le transistor d'entrée sature, allumant le transistor de sortie.

3. **Étage de sortie** : Utilise typiquement un agencement "totem pole" avec deux transistors. Le transistor supérieur agit comme un pull-up (source de courant), et le transistor inférieur agit comme un pull-down (puits de courant).

4. **Caractéristiques** :
   - Fonctionne avec une alimentation de 5V
   - Immunité au bruit robuste (typiquement 0,8V pour BAS, 2,0V pour HAUT)
   - Capable de couler plus de courant que d'en fournir
   - Composants pull-up et pull-down actifs

## CMOS (Complementary Metal-Oxide-Semiconductor)

Le CMOS fonctionne en utilisant des paires complémentaires de MOSFET (Transistors à Effet de Champ Métal-Oxyde-Semiconducteur) :

1. **Structure de base** : Chaque porte logique contient des paires complémentaires de transistors à canal P (PMOS) et à canal N (NMOS).

2. **Principe de fonctionnement** :
   - Lorsque l'entrée est BASSE (0V), le transistor PMOS s'allume tandis que le transistor NMOS s'éteint.
   - Lorsque l'entrée est HAUTE (tension d'alimentation), le transistor PMOS s'éteint tandis que le transistor NMOS s'allume.
   - Cela crée une action de commutation complémentaire où un seul transistor est allumé à la fois.

3. **Caractéristiques de puissance** :
   - Consommation d'énergie statique quasi nulle (l'énergie n'est utilisée que pendant la commutation)
   - Le courant ne circule que momentanément pendant les changements d'état lorsque les deux transistors sont partiellement conducteurs
   - La consommation d'énergie augmente avec la fréquence de commutation

4. **Fonctionnalités clés** :
   - Large plage de tension de fonctionnement (typiquement 3-15V pour les CMOS anciens, 1,8-5V pour les variantes modernes)
   - Haute immunité au bruit (typiquement 30-40% de la tension d'alimentation)
   - Capacités de source et de puits presque égales
   - Très haute impédance d'entrée

La différence fondamentale entre le TTL et le CMOS est que le TTL utilise des transistors bipolaires contrôlés en courant, tandis que le CMOS utilise des transistors à effet de champ contrôlés en tension, ce qui se traduit par une consommation d'énergie significativement plus faible pour le CMOS, mais traditionnellement des vitesses de commutation plus lentes (bien que le CMOS moderne ait surmonté cette limitation).