---
audio: false
generated: true
lang: fr
layout: post
title: Méthodes d'extraction de sous-titres de vidéos YouTube
translated: true
type: note
---

Pour obtenir tous les sous-titres d'une vidéo YouTube, suivez ces étapes, en fonction de vos besoins et selon que vous préférez une approche manuelle ou automatisée. Notez que les sous-titres doivent être disponibles pour la vidéo (soit générés automatiquement, soit téléchargés par le créateur).

### Méthode manuelle (Utilisation de la fonction de transcription intégrée à YouTube)
1. **Ouvrir la vidéo** : Allez sur YouTube dans un navigateur web et accédez à la vidéo souhaitée.
2. **Vérifier la présence de sous-titres** : Cliquez sur la vidéo pour la mettre en pause. Cherchez l'icône "CC" (Sous-titres codés) en bas à droite du lecteur. Si elle est visible, les sous-titres sont disponibles.
3. **Accéder à la transcription** :
   - Descendez dans la description de la vidéo et cliquez sur "Afficher plus".
   - Trouvez et cliquez sur "Afficher la transcription" (si disponible). Cela ouvre un panneau de transcription sur le côté droit de la vidéo avec les horodatages et le texte.
4. **Activer/Désactiver les horodatages** : Cliquez sur les trois points verticaux en haut à droite du panneau de transcription et sélectionnez "Activer/désactiver les horodatages" pour les afficher ou les masquer, selon votre préférence.
5. **Copier la transcription** :
   - Descendez au bas de la transcription, cliquez et maintenez le bouton de la souris après le dernier mot, puis remontez jusqu'en haut pour surligner tout le texte.
   - Appuyez sur `Ctrl + C` (Windows) ou `Command + C` (Mac) pour copier.
6. **Coller et enregistrer** : Ouvrez un éditeur de texte (par exemple, Bloc-notes, TextEdit ou Word), collez le texte avec `Ctrl + V` ou `Command + V`, et enregistrez-le sous forme de fichier `.txt` ou dans le format de votre choix.

**Remarque** : Cette méthode ne fonctionne que sur le site web de YouTube, pas sur l'application mobile.[](https://www.wikihow.com/Download-YouTube-Video-Subtitles)

### Pour les créateurs de contenu (Téléchargement des sous-titres de votre propre vidéo)
Si vous êtes propriétaire de la vidéo, vous pouvez télécharger les sous-titres directement depuis YouTube Studio :
1. **Se connecter à YouTube Studio** : Allez sur [studio.youtube.com](https://studio.youtube.com).
2. **Sélectionner la vidéo** : Cliquez sur "Contenu" dans le menu de gauche, puis choisissez la vidéo.
3. **Accéder aux sous-titres** : Cliquez sur "Sous-titres" dans le menu de gauche, puis sélectionnez la langue.
4. **Télécharger les sous-titres** : Cliquez sur le menu à trois points à côté de la piste de sous-titres et sélectionnez "Télécharger". Choisissez un format comme `.srt`, `.vtt` ou `.sbv`.
5. **Modifier ou utiliser** : Ouvrez le fichier téléchargé dans un éditeur de texte ou un éditeur de sous-titres (par exemple, Aegisub) pour une utilisation ultérieure.

**Remarque** : Vous ne pouvez télécharger les fichiers de sous-titres que pour les vidéos des chaînes que vous gérez.[](https://ito-engineering.screenstepslive.com/s/ito_fase/a/1639680-how-do-i-download-a-caption-file-from-youtube)

### Méthode automatisée (Utilisation d'outils tiers)
Si vous avez besoin de sous-titres dans un format spécifique (par exemple, `.srt`) ou pour des vidéos dont vous n'êtes pas propriétaire, utilisez un outil tiers de confiance :
1. **Choisir un outil** : Les options populaires incluent :
   - **DownSub** : Un outil en ligne gratuit pour télécharger les sous-titres.
   - **Notta** : Offre la transcription et le téléchargement de sous-titres avec une grande précision.[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)
   - **4K Download** : Une application de bureau pour l'extraction de sous-titres.[](https://verbit.ai/captioning/a-guide-to-downloading-subtitles-and-captions-from-youtube-enhancing-accessibility-and-user-experience/)
2. **Copier l'URL de la vidéo** : Ouvrez la vidéo YouTube, cliquez sur "Partager" sous la vidéo et copiez l'URL.
3. **Utiliser l'outil** :
   - Collez l'URL dans le champ de saisie de l'outil.
   - Sélectionnez la langue et le format souhaités (par exemple, `.srt`, `.txt`).
   - Cliquez sur "Télécharger" ou "Extraire" et enregistrez le fichier.
4. **Vérifier** : Ouvrez le fichier pour vous assurer de son exactitude, car les sous-titres générés automatiquement peuvent contenir des erreurs.

**Attention** : Utilisez des outils de confiance pour éviter les risques de sécurité. Certains outils peuvent contenir des publicités ou nécessiter un paiement pour les fonctionnalités avancées.[](https://gotranscript.com/blog/how-to-download-subtitles-from-youtube)

### Utilisation de l'API YouTube (Pour les développeurs)
Pour l'extraction en masse de sous-titres ou l'intégration dans une application, utilisez l'API YouTube Data :
1. **Configurer l'accès à l'API** : Créez un projet dans la [Google Cloud Console](https://console.cloud.google.com), activez l'API YouTube Data v3 et obtenez une clé API.
2. **Lister les pistes de sous-titres** : Utilisez le point de terminaison `captions.list` pour récupérer les pistes de sous-titres disponibles pour une vidéo. Exemple :
   ```
   GET https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId=VIDEO_ID&key=API_KEY
   ```
3. **Télécharger les sous-titres** : Utilisez le point de terminaison `captions.download` pour récupérer une piste de sous-titres spécifique. Exemple :
   ```
   GET https://www.googleapis.com/youtube/v3/captions/CAPTION_ID?tfmt=srt&key=API_KEY
   ```
4. **Limitations** :
   - Vous ne pouvez télécharger les sous-titres que pour vos propres vidéos, à moins que le propriétaire de la vidéo ne les ait rendus accessibles au public.
   - L'utilisation de l'API est soumise à des limites de quota (environ 200 unités par téléchargement de sous-titres).[](https://developers.google.com/youtube/v3/docs/captions)[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)
5. **Alternative** : Certains développeurs extraient l'URL du texte synchronisé (par exemple, `https://www.youtube.com/api/timedtext?...`) depuis le code source de la page de la vidéo, mais cette méthode n'est pas fiable, peut violer les conditions d'utilisation de YouTube et risque un blocage d'adresse IP.[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)

### Conseils supplémentaires
- **Sélection de la langue** : Si les sous-titres sont disponibles en plusieurs langues, sélectionnez votre langue préférée dans les paramètres "Sous-titres/CC" ou le menu déroulant de la transcription.[](https://riverside.fm/blog/youtube-transcription)
- **Sous-titres générés automatiquement** : Ils peuvent contenir des erreurs dues aux accents, au bruit de fond ou à un audio complexe. Relisez-les et modifiez-les si l'exactitude est critique.[](https://support.google.com/youtube/answer/6373554?hl=en)
- **Accessibilité** : Les sous-titres améliorent l'accessibilité pour les spectateurs sourds ou malentendants et améliorent le référencement (SEO) en rendant le contenu consultable.[](https://www.descript.com/blog/article/transcript-of-youtube-videos)
- **Aucun sous-titre disponible ?** : Si la vidéo n'a pas de sous-titres, envisagez d'utiliser des services de transcription comme Rev ou Notta pour générer une transcription à partir de l'audio.[](https://www.rev.com/resources/how-to-download-youtube-subtitles-as-text-files)[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)

### Limitations
- Toutes les vidéos n'ont pas de sous-titres, surtout si le créateur les a désactivés ou si le sous-titrage automatique de YouTube n'est pas pris en charge pour la langue ou la qualité audio.[](https://support.google.com/youtube/answer/6373554?hl=en)
- L'application mobile YouTube ne prend pas en charge l'affichage de la transcription, mais vous pouvez activer les sous-titres via le bouton "CC".[](https://riverside.fm/blog/youtube-transcription)
- Certains outils tiers ou méthodes d'API peuvent ne pas fonctionner pour les sous-titres générés automatiquement ou les vidéos restreintes.[](https://stackoverflow.com/questions/9611397/how-to-extract-closed-caption-transcript-from-youtube-video)

Si vous avez besoin de sous-titres pour une vidéo spécifique ou dans un format particulier, faites-le-moi savoir et je pourrai vous guider davantage !