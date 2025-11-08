---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Création de comptes utilisateur Ubuntu
translated: true
type: note
---

### Créer un nouvel utilisateur dans Ubuntu Linux

Ubuntu propose des méthodes en ligne de commande et graphique pour créer un utilisateur. L'approche en ligne de commande est simple et fonctionne sur toutes les éditions (y compris les serveurs), tandis que l'interface graphique est disponible sur les versions de bureau.

#### Méthode en ligne de commande (Recommandée)
1. Ouvrez un terminal (Ctrl+Alt+T).
2. Exécutez la commande suivante, en remplaçant `username` par le nom d'utilisateur de votre choix :
   ```
   sudo adduser username
   ```
   - Vous serez invité à définir un mot de passe fort pour le nouvel utilisateur.
   - Des informations facultatives telles que le nom complet, le numéro de bureau, le téléphone professionnel, etc., vous seront également demandées. Appuyez sur Entrée pour ignorer ces champs ou renseignez-les si nécessaire.
3. (Optionnel) Pour accorder des privilèges administratifs (sudo) au nouvel utilisateur :
   ```
   sudo usermod -aG sudo username
   ```
   - Cela ajoute l'utilisateur au groupe `sudo`, lui permettant d'exécuter des commandes avec des permissions élevées.

Le nouvel utilisateur aura un répertoire personnel situé à `/home/username` et pourra se connecter immédiatement.

#### Méthode graphique (Bureau uniquement)
1. Ouvrez l'application **Paramètres** (recherchez-la dans l'aperçu des Activités).
2. Accédez à **Utilisateurs** dans la barre latérale.
3. Cliquez sur **Déverrouiller** dans le coin supérieur droit et entrez votre mot de passe administrateur.
4. Cliquez sur **Ajouter un utilisateur**.
5. Remplissez le type de compte (Standard ou Administrateur), le nom complet, le nom d'utilisateur et le mot de passe.
6. Cliquez sur **Ajouter**.

#### Vérification
- Passez au nouvel utilisateur avec `su - username` ou déconnectez-vous et reconnectez-vous.
- Vérifiez les utilisateurs avec `cat /etc/passwd | grep username`.

Ce processus fonctionne sur Ubuntu 24.04 LTS et les versions ultérieures.

[Gestion des utilisateurs - Documentation Ubuntu Server](https://documentation.ubuntu.com/server/how-to/security/user-management/)  
[Ajouter un nouveau compte utilisateur - Documentation Ubuntu](https://help.ubuntu.com/stable/ubuntu-help/user-add.html.en)