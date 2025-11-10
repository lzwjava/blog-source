---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Résoudre l'Erreur de Signature GPG d'APT
translated: true
type: note
---

L'erreur que vous voyez signifie qu'APT refuse de se mettre à jour depuis le dépôt ShiftKey car il ne peut pas vérifier sa signature GPG. Vous avez deux solutions simples pour corriger ceci :

---

## 1. **Supprimer ou désactiver le dépôt défectueux**

Si vous n'avez pas réellement besoin de `https://apt.packages.shiftkey.dev/ubuntu`, désactivez-le simplement :

```bash
# Trouvez le fichier définissant ce dépôt (il se trouvera dans /etc/apt/sources.list.d/)
ls /etc/apt/sources.list.d/shiftkey*

# Supprimez-le (remplacez par le nom de fichier actuel)
sudo rm /etc/apt/sources.list.d/shiftkey.packages.shiftkey.dev.list

# Puis mettez à jour et installez
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

## 2. **Importer la clé de signature du dépôt**

Si vous souhaitez continuer à utiliser les paquets de ShiftKey, vous devez récupérer et installer sa clé publique :

```bash
# Téléchargez et dé-armurez leur clé GPG dans le trousseau de clés d'APT
curl -fsSL https://apt.packages.shiftkey.dev/ubuntu/pubkey.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-archive-keyring.gpg > /dev/null

# Modifiez le fichier du dépôt pour qu'il référence ce trousseau de clés.
# Ouvrez /etc/apt/sources.list.d/shiftkey*.list dans votre éditeur, et changez la ligne deb par :
#   deb [signed-by=/usr/share/keyrings/shiftkey-archive-keyring.gpg] https://apt.packages.shiftkey.dev/ubuntu any main

# Puis mettez à jour et installez
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

Une fois qu'APT pourra se mettre à jour sans erreurs GPG, vous pourrez installer `pkg-config` et `libssl-dev`, puis recompiler :

```bash
cargo clean
cargo run
```