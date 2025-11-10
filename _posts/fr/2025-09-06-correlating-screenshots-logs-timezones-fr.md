---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Corréler les captures d'écran et les journaux serveur sur plusieurs fuseaux
  horaires
translated: true
type: note
---

Compris 👍 – vous voulez **corréler les captures d'écran (que les testeurs téléversent dans Confluence) avec les journaux du serveur UAT** (générés par Java + log4j/slf4j), et la difficulté réside dans les multiples fuseaux horaires et horodatages.

Décomposons cela soigneusement :

---

## 1. Quels horodatages avez-vous ?

**Depuis la capture d'écran (Windows) :**
- L'horloge **visible dans la barre des tâches de la capture d'écran** = heure **locale** de la machine cliente (heure système, dans son fuseau horaire).
- Les métadonnées du fichier (si vous les avez encore en dehors de Confluence) peuvent afficher les horodatages `Créé` / `Modifié` = également dans le fuseau horaire du client.

**Depuis Confluence :**
- L'horodatage de téléversement = moment où la pièce jointe a atteint le serveur Confluence.
- Généralement stocké/affiché en *heure du serveur* ou converti en *fuseau horaire du profil utilisateur Confluence*.  
(Vous pouvez vérifier votre profil Confluence → Paramètres → Fuseau horaire pour confirmer ce que vous voyez.)

**Depuis les journaux UAT (log4j/slf4j) :**
- Les horodatages sont générés par le **fuseau horaire du processus JVM Java** (généralement défini par le système d'exploitation du serveur par défaut, sauf s'il est écrasé).
- Le format est déterminé par votre modèle de journal (par exemple `yyyy-MM-dd HH:mm:ss,SSS [thread] ...`). Typiquement, il s'agit de l'heure locale de la JVM, pas UTC, sauf configuration explicite.

---

## 2. Pourquoi les choses ne s'alignent pas directement
- La capture d'écran montre l'heure **locale de l'ordinateur portable** du testeur.
- Confluence stocke **l'heure de téléversement dans le fuseau horaire du serveur/BDD**.
- Les journaux affichent le **fuseau horaire du serveur Java**.  
Ces trois éléments ne sont pas garantis d'être identiques.

---

## 3. Méthode pour les réconcilier
Voici comment comparer de manière cohérente une capture d'écran d'un testeur avec les journaux du serveur :

1. **Choisissez une norme de temps commune – généralement UTC**  
   - Convertissez tous les horodatages pertinents en UTC (Excel, script ou manuellement).
   - Cela évite la confusion entre les fuseaux horaires.

2. **Vérifiez le fuseau horaire JVM / journal**  
   - Confirmez sur le serveur UAT : `java -Duser.timezone` ou vérifiez une entrée de journal connue par rapport à `date` sous Linux.  
   - Si les journaux ne sont pas en UTC, notez le décalage.

3. **Vérifiez le fuseau horaire du serveur/Profil Confluence**  
   - Vérifiez si l'horodatage de téléversement que vous voyez est déjà ajusté pour votre fuseau horaire de profil.
   - Reconvertissez-le en UTC brut.

4. **Alignez avec l'horloge de la capture d'écran**  
   - Si la capture d'écran montre `2024-02-10 13:45` et que vous savez que le testeur était dans `Asia/Kolkata (UTC+5:30)`, alors cela équivaut à `2024-02-10 08:15 UTC`.
   - Si les journaux montrent un événement à `2024-02-10 08:15:23 UTC`, vous pouvez les faire correspondre.

---

## 4. Processus recommandé

- **Étape 1 :** Demandez aux testeurs (ou imposez-le dans les instructions UAT) d'inclure leur **fuseau horaire/lieu** lors du téléversement des captures d'écran, ou mieux encore, demandez-leur de régler correctement l'horloge système.  
- **Étape 2 :** Lors de la vérification des journaux, convertissez d'abord l'horodatage de la capture d'écran (horloge locale du testeur) → UTC.  
- **Étape 3 :** Convertissez l'horodatage du journal → UTC (en appliquant le fuseau horaire de la JVM).  
- **Étape 4 :** Comparez.

---

## 5. Exemple de correspondance

- Capture d'écran : montre `2024-06-01 14:05` (testeur à Berlin, UTC+2).  
  → UTC = `2024-06-01 12:05`.  

- Confluence montre le téléversement = `2024-06-01 12:07 UTC`.  
  (logique – téléversé dans les ~2 minutes).  

- Journal UAT :  
  ```
  2024-06-01 12:05:20,456 INFO UAT-Service [thread-19] ...
  ```
  Fuseau horaire JVM = UTC.  
  → Correspondance parfaite.

---

✅ **Point clé :** Vous devez normaliser tous les horodatages dans le même fuseau horaire (généralement UTC). Les captures d'écran Windows affichent l'heure locale. Les journaux Java utilisent le fuseau horaire de la JVM. Confluence affiche l'heure de téléversement dans le fuseau horaire du serveur ou du profil utilisateur. Sans cette normalisation, vous ne pourrez jamais les aligner.

---

Souhaitez-vous que je rédige un **mini guide** pour votre équipe UAT, afin que les testeurs sachent quoi capturer (comme "toujours noter votre fuseau horaire lors du téléversement des captures d'écran") pour faciliter la corrélation avec les journaux ?