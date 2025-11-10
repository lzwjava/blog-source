---
audio: false
generated: true
image: false
lang: fr
layout: post
title: SPOCO Réduit les Annotations pour la Segmentation
translated: true
type: note
---

Voici un aperçu plus clair de cet article :

---

## Aperçu

**Titre :** "Sparse object-level supervision for instance segmentation with pixel embeddings" — A. Wolny, Q. Yu, C. Pape, and A. Kreshuk, CVPR 2022.

### **Le Défi Principal**

Les méthodes traditionnelles de segmentation d'instances exigent des **annotations denses**—ce qui signifie que chaque objet dans chaque image doit être méticuleusement annoté. Cela devient particulièrement laborieux dans des domaines comme la **microscopie**, où les images contiennent des **objets en foule, qui se chevauchent**, et où l'annotation doit souvent être réalisée par des experts. L'annotation dense prend du temps et est coûteuse. ([Semantic Scholar][1], [arXiv][2])

### **La Proposition des Auteurs**

Les auteurs introduisent une méthode—surnommée **SPOCO** (Sparse Object‑level supervision for instance segmentation with pixel embeddings)—qui réduit radicalement la charge d'annotation. Au lieu d'annoter chaque objet, ils n'annoter qu'**un sous-ensemble d'objets par image**, laissant le reste non annoté. ([CVF Open Access][3])

---

## Innovations Clés

1. **Réseau d'Embedding de Pixels**
   Ils entraînent un CNN pour produire des **embeddings de pixels non spatiaux**, où chaque pixel est projeté dans un espace de caractéristiques. Dans cet espace, les pixels du même objet se regroupent, et ceux d'objets différents sont éloignés. C'est une approche de segmentation **sans proposition** (proposal-free). ([ar5iv][4])

2. **Sélection d'Instances Différentiable**
   Un obstacle majeur dans la supervision faible est que l'inférence des masques d'instances dans les régions non annotées est typiquement **non différentiable**, empêchant l'apprentissage par gradient sur ces parties. L'article propose une technique d'**extraction d'instances "douce" (soft) et différentiable** : ils échantillonnent des pixels d'ancrage à partir des instances annotées, calculent leur embedding, et utilisent un noyau pour sélectionner de manière douce les pixels proches dans l'espace d'embedding—permettant ainsi d'appliquer une perte spécifique aux instances de manière différentiable. ([CVF Open Access][3])

3. **Supervision Positive-Non Étiqueté (PU) avec Perte de Cohérence**
   Pour les régions non annotées, ils introduisent une **perte de cohérence auto-supervisée** : la cohérence est imposée entre plusieurs vues augmentées pour les pixels non étiquetés. Cette approche évite d'avoir besoin de pseudo-labels ou d'estimer des probabilités a priori de classe, simplifiant ainsi la supervision faible. ([CVF Open Access][3])

4. **Regroupement (Clustering) Efficace pour la Segmentation Finale**
   Lors de l'inférence, les embeddings de pixels du réseau sont regroupés (par exemple, via **mean‑shift**, **HDBSCAN**, ou un clustering de cohérence) pour produire les masques d'instances finaux. ([GitHub][5])

---

## Résultats et Impacts

* **Des performances solides** sur des jeux de données standard :

  * A obtenu des résultats **state-of-the-art** sur le benchmark de segmentation de feuilles **CVPPP**.
  * A bien performé sur **Cityscapes** (images naturelles) et divers jeux de données de **microscopie 2D/3D**. ([CVF Open Access][3], [arXiv][2])

* **Efficacité de l'annotation** :

  * Les gains de performance se produisent même lorsque *seulement une fraction des instances sont annotées*—réduisant ainsi considérablement la charge d'annotation tout en maintenant la précision. ([CVF Open Access][6])

---

## Pourquoi C'est Important

* **Coûts d'annotation réduits** : Cette méthode change la donne pour les domaines où les annotations denses sont prohibitives—en temps et en coût.
* **Meilleure généralisation** : L'échantillonnage de supervision éparse sur de nombreuses images (plutôt que d'annoter complètement moins d'images) aide le modèle à apprendre une représentation plus diverse et plus robuste. ([Adrian Wolny][7], [CVF Open Access][3])
* **Applicabilité** : Particulièrement précieuse en imagerie biomédicale (par exemple, microscopie optique/électronique), mais s'avère également efficace sur des benchmarks d'images naturelles.

---

Faites-moi savoir si vous souhaitez approfondir l'un de ces aspects—comme l'architecture, les fonctions de perte, ou la manière dont le clustering est géré—ou si vous êtes curieux des approches similaires en supervision faible.

[1]: https://www.semanticscholar.org/paper/Sparse-Object-level-Supervision-for-Instance-with-Wolny-Yu/39cbc5c457a66e176cffd920e04e471d7ef0cfc1?utm_source=chatgpt.com "Sparse Object-level Supervision for Instance Segmentation ..."
[2]: https://arxiv.org/abs/2103.14572?utm_source=chatgpt.com "Sparse Object-level Supervision for Instance Segmentation with Pixel Embeddings"
[3]: https://openaccess.thecvf.com/content/CVPR2022/papers/Wolny_Sparse_Object-Level_Supervision_for_Instance_Segmentation_With_Pixel_Embeddings_CVPR_2022_paper.pdf?utm_source=chatgpt.com "Sparse Object-level Supervision for Instance Segmentation ..."
[4]: https://ar5iv.labs.arxiv.org/html/2103.14572?utm_source=chatgpt.com "Sparse Object-level Supervision for Instance Segmentation ..."
[5]: https://github.com/kreshuklab/spoco?utm_source=chatgpt.com "kreshuklab/spoco: PyTorch implementation of SPOCO"
[6]: https://openaccess.thecvf.com/content/ICCV2023/papers/Liu_Learning_Cross-Representation_Affinity_Consistency_for_Sparsely_Supervised_Biomedical_Instance_Segmentation_ICCV_2023_paper.pdf?utm_source=chatgpt.com "Learning Cross-Representation Affinity Consistency for ..."
[7]: https://adrianwolny.com/assets/CVPR2022_Poster_AdrianWolny.pdf?utm_source=chatgpt.com "Sparse Object-level Supervision for Instance Segmentation ..."