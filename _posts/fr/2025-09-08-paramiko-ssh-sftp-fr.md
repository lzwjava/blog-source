---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide SSH et SFTP avec Paramiko
translated: true
type: note
---

### Installation
Paramiko est une bibliothèque Python pour SSH et SFTP. Installez-la via pip :

```bash
pip install paramiko
```

### Utilisation de base
Paramiko vous permet de vous connecter à des serveurs SSH, d'exécuter des commandes et de transférer des fichiers. Manipulez toujours les clés privées de manière sécurisée et utilisez des mots de passe robustes—Paramiko prend en charge l'authentification par clé et par mot de passe.

Concepts clés :
- **Client** : Utilisez `paramiko.SSHClient()` pour établir une connexion.
- **Transport** : Pour un contrôle de bas niveau, utilisez `paramiko.Transport()`.
- Authentifiez-vous via `client.connect()` avec le nom d'hôte, le nom d'utilisateur et soit un mot de passe, soit une clé (par exemple, via `paramiko.RSAKey.from_private_key_file()`).

### Exemple : Connexion et exécution d'une commande
Voici un script complet pour se connecter à un serveur SSH, exécuter une commande et afficher la sortie. Remplacez les espaces réservés par vos informations.

```python
import paramiko

# Créer un client SSH
client = paramiko.SSHClient()

# Ajouter automatiquement la clé d'hôte (soyez prudent en production ; chargez known_hosts à la place)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Se connecter (utiliser un mot de passe ou un fichier de clé)
    client.connect(
        hostname='your.server.com',
        port=22,  # Port SSH par défaut
        username='your_username',
        password='your_password',  # Ou key_filename='chemin/vers/private_key.pem'
    )

    # Exécuter une commande
    stdin, stdout, stderr = client.exec_command('echo "Hello from SSH!"')

    # Lire la sortie
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    print("Sortie :", output)
    print("Erreur :", error)

except paramiko.SSHException as e:
    print(f"Erreur SSH : {e}")
finally:
    client.close()
```

### Exemple avancé : Utilisation de l'authentification par clé et transfert de fichiers
Pour l'authentification par clé, générez une paire de clés si nécessaire (par exemple, avec `ssh-keygen`), ajoutez la clé publique à `~/.ssh/authorized_keys` sur le serveur, puis utilisez :

```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connexion par clé
    client.connect(
        hostname='your.server.com',
        username='your_username',
        key_filename='~/.ssh/id_rsa',  # Chemin vers la clé privée
    )

    # Exécuter une commande
    stdin, stdout, stderr = client.exec_command('ls -la')
    print(stdout.read().decode('utf-8'))

    # Exemple SFTP : transfert de fichier
    sftp = client.open_sftp()
    sftp.put('fichier_local.txt', 'fichier_distant.txt')  # Téléversement
    sftp.get('fichier_distant.txt', 'copie_locale.txt')  # Téléchargement
    sftp.close()

except Exception as e:
    print(f"Erreur : {e}")
finally:
    client.close()
```

### Conseils et bonnes pratiques
- **Sécurité** : Préférez l'authentification par clé aux mots de passe. Désactivez `AutoAddPolicy` en production et vérifiez les clés d'hôte via `client.load_host_keys()`.
- **Gestion des erreurs** : Interceptez toujours `paramiko.SSHException` et vérifiez les codes de sortie avec `exit_status = stdout.channel.recv_exit_status()`.
- **Threads** : Paramiko n'est pas thread-safe par défaut ; utilisez des verrous si nécessaire.
- **Documentation** : Pour en savoir plus, consultez la [documentation officielle de Paramiko](https://docs.paramiko.org/). Testez avec des outils comme `sshd` d'OpenSSH ou des machines virtuelles locales.

Ceci devrait vous aider à démarrer ; adaptez en fonction de vos besoins !