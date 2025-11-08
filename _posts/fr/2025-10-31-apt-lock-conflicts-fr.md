---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre les conflits de verrouillage APT
translated: true
type: note
---

### Comprendre le problème
Vous rencontrez un conflit de verrouillage APT courant sur les systèmes Ubuntu/Debian. Le fichier de verrou `/var/lib/dpkg/lock-frontend` est détenu par un autre processus `apt` (PID 6761), empêchant votre commande `--fix-broken install` de s'exécuter. Cela se produit souvent si une mise à jour, une installation ou une mise à niveau est bloquée ou s'exécute en arrière-plan. La suspension avec `Ctrl+Z` (qui l'a placée dans le job [1]) ne libère pas le verrou.

### Étapes pour résoudre le problème
Suivez ces étapes dans l'ordre—**commencez par vérifier, pas par tuer**, pour éviter d'interrompre une opération légitime.

1. **Vérifier le processus en cours d'exécution**  
   Voyez ce qui utilise le PID 6761 :  
   ```
   ps aux | grep 6761
   ```  
   Ou plus largement :  
   ```
   ps aux | grep -E "(apt|dpkg)"
   ```  
   - S'il s'agit d'une mise à jour active (par exemple, via `apt upgrade` ou le Logiciel de mise à jour), attendez qu'elle se termine ou laissez-la se terminer.  
   - Si elle est bloquée (aucune sortie ou le processus est suspendu), passez à l'étape suivante pour le tuer.

2. **Tuer le processus bloquant (s'il est bloqué)**  
   Terminez-le doucement :  
   ```
   sudo kill 6761
   ```  
   Si cela ne fonctionne pas (le processus ignore SIGTERM) :  
   ```
   sudo kill -9 6761
   ```  
   - Vérifiez qu'il a disparu : `ps aux | grep 6761` (ne devrait rien retourner de pertinent).

3. **Supprimer les fichiers de verrouillage**  
   Une fois le processus terminé, supprimez les verrous :  
   ```
   sudo rm /var/lib/dpkg/lock-frontend
   sudo rm /var/lib/dpkg/lock
   sudo rm /var/lib/apt/lists/lock
   ```  
   - Il est sûr de les supprimer si aucun processus APT n'est en cours d'exécution.

4. **Mettre à jour les listes de paquets**  
   Actualisez le cache :  
   ```
   sudo dpkg --configure -a
   sudo apt update
   ```

5. **Reprendre ou relancer votre commande**  
   - Pour reprendre le job suspendu : `fg` (ramène le job [1]).  
   - Ou simplement relancer : `sudo apt --fix-broken install`.  
   Si cela échoue encore, essayez `sudo apt install -f` (identique à `--fix-broken`).

### Conseils de prévention
- Évitez d'exécuter plusieurs commandes APT simultanément.  
- Si vous utilisez un logiciel de mise à jour graphique, fermez-le avant les opérations en ligne de commande.  
- Pour les problèmes persistants, vérifiez l'espace disque (`df -h`) ou les journaux (`sudo journalctl -u apt`).

Si cela ne résout pas le problème ou si vous voyez des erreurs, collez la sortie de l'étape 1 pour obtenir plus d'aide.

[Résolution des problèmes de verrouillage APT sur Ubuntu](https://askubuntu.com/questions/248748/could-not-get-lock-var-lib-dpkg-lock)  
[Guide de gestion des paquets Debian](https://wiki.debian.org/AptConfiguration)