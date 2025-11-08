---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Examen sur les fondamentaux de la technologie électronique
translated: true
type: note
---

### Exemples de questions d'examen : Fondamentaux de la technologie électronique (III)  
*(Basé sur l'édition de Wen Xidong, Examen national d'auto-enseignement supérieur)*  

Ce jeu de questions s'inspire des anciennes épreuves de l'examen d'auto-enseignement pour le cours 电子技术基础（三）. Les sujets abordés incluent l'analyse des circuits AC, les semi-conducteurs, les transistors et les amplificateurs opérationnels. Les questions sont en anglais (traduites des originaux chinois) pour plus de clarté. Chaque question à choix unique vaut 1 point ; la question d'analyse vaut 5 points.

#### Section I : Questions à choix unique  
Sélectionnez l'option correcte (A, B, C ou D) pour chaque question.

1. **Parmi les descriptions suivantes des caractéristiques d'une source de tension idéale, la correcte est :**  
   A. La résistance interne de la source de signal de tension idéale tend vers l'infini.  
   B. Les sources de tension idéales peuvent être connectées en parallèle à tout moment.  
   C. La tension de sortie de la source de tension idéale est liée à la charge.  
   D. Le courant traversant la source de tension idéale est lié à la charge.

2. **Étant donné le courant phasor traversant la réactance inductive \\( \omega L = 2 \, \Omega \\) est \\( I = 10 \angle 30^\circ \\) mA, alors la tension phasor à ses bornes est :**  
   A. \\( U = 20 \angle 0^\circ \\) mV  
   B. \\( U = 20 \angle 120^\circ \\) mV  
   C. \\( U = 20 \angle 30^\circ \\) mV  
   D. \\( U = 20 \angle -60^\circ \\) mV

3. **Supposons qu'un condensateur \\( C = 1 \, \mu \mathrm{F} \\), la tension aux bornes du condensateur est \\( \cos(100 \pi t) \\) mV, alors le courant traversant le condensateur est :**  
   A. \\( i_c(t) = -0.1 \times 10^{-6} \pi \sin(100 \pi t) \\) A  
   B. \\( i_c(t) = 0.1 \times 10^{-6} \pi \sin(100 \pi t) \\) A  
   C. \\( i_c(t) = -0.1 \times 10^{-6} \sin(100 \pi t) \\) A  
   D. \\( i_c(t) = 0.1 \times 10^{-6} \sin(100 \pi t) \\) A

4. **Le porteur majoritaire dans un semi-conducteur de type P est :**  
   A. Les électrons libres  
   B. Les trous  
   C. Les atomes d'impuretés trivalents  
   D. Les ions d'impuretés trivalents

5. **Étant donné les potentiels des trois électrodes d'un certain transistor à cristal comme indiqué sur la figure (tensions émetteur-base-collecteur indiquant les caractéristiques d'un transistor NPN au silicium), le type de ce transistor est :**  
   *(Description de la figure : Émetteur à 0V, base à 0.7V, collecteur à 5V – caractéristique typique d'une jonction NPN au silicium en polarisation directe.)*  
   A. Tube au germanium de type PNP  
   B. Tube au germanium de type NPN  
   C. Tube au silicium de type PNP  
   D. Tube au silicium de type NPN

#### Section II : Question d'analyse  
**Question 31 (5 points) :** Dans le circuit illustré par la Figure 31 (une configuration basique d'amplificateur opérationnel inverseur avec une résistance d'entrée \\( R_i = 10 \, \mathrm{k} \Omega \\), une résistance de rétroaction \\( R_f = 20 \, \mathrm{k} \Omega \\), une tension d'entrée \\( U_i = 10 \\) V), calculez la tension de sortie \\( U_o \\).

*(Description de la figure : Amplificateur opérationnel inverseur standard ; entrée non inverseuse mise à la masse. Utilisez la formule de gain : \\( U_o = - \frac{R_f}{R_i} \times U_i \\).)*

**Indice de solution :** Appliquez le principe de la masse virtuelle (l'entrée inverseuse est au potentiel 0V). La chute de tension aux bornes de \\( R_i \\) est égale à \\( U_i \\), donc le courant \\( I = \frac{U_i}{R_i} \\). Ensuite, \\( U_o = -I \times R_f \\). Résultat attendu : \\( U_o = -20 \\) V.

Ces questions correspondent à des chapitres tels que les phaseurs AC (Ch. 2), les semi-conducteurs (Ch. 3–4) et les amplificateurs opérationnels (Ch. 5). Conseil de pratique : révisez l'arithmétique des phaseurs, le transport des porteurs et les règles des amplificateurs opérationnels idéaux.

**Références :**  
- [04730 电子技术基础(三) 2010.07 自考 历年真题 试题](https://wenku.baidu.com/view/a2a96333b90d6c85ec3ac6bf.html)  
- [自考电子技术基础（三）04730真题及答案免费分享](http://www.s9w.cn/zkzt408/)