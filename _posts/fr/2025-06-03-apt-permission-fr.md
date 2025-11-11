---
audio: false
generated: true
lang: fr
layout: post
title: Installation de paquets Linux
translated: true
type: note
---

Le message d'erreur que vous voyez indique que le gestionnaire de paquets (`apt`) a rencontré un problème de permissions en essayant d'accéder au fichier de paquet téléchargé. Plus précisément, il tente d'accéder au paquet en tant qu'utilisateur root, mais il ne peut pas le faire car il est exécuté avec des permissions élevées d'une manière qui restreint l'accès au fichier.

Pour résoudre ce problème, vous avez plusieurs options :

### Option 1 : Utiliser un répertoire différent
Déplacez le paquet `.deb` vers un répertoire différent et essayez de l'installer à partir de là. Par exemple :

```bash
sudo mv /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb /tmp/
sudo apt install /tmp/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
```

### Option 2 : Ajuster les permissions temporairement
Changez temporairement le propriétaire du fichier de paquet `.deb` pour permettre à la commande `apt` d'y accéder :

```bash
sudo chown root:root /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
sudo apt install /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
```

### Option 3 : Télécharger à nouveau le paquet
Si vous préférez, vous pouvez aussi essayer de télécharger à nouveau le paquet et vous assurer d'avoir les permissions correctes :

1. Supprimez le paquet `.deb` existant s'il existe :
   ```bash
   rm /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
   ```

2. Téléchargez à nouveau le paquet depuis le site web officiel ou la source et réessayez l'installation.

### Exemple :
```bash
sudo apt install /chemin/vers/le/paquet/telecharge.package.deb
```

### Conseils supplémentaires :
- Assurez-vous que votre répertoire de travail actuel a les permissions nécessaires pour accéder au paquet téléchargé.
- Vérifiez que le paquet que vous avez téléchargé est bien un paquet `.deb` valide et non corrompu.

Suivre ces étapes devrait permettre à `apt` de décompresser et d'installer avec succès le paquet Tencent Meeting.