---
audio: false
generated: true
lang: fr
layout: post
title: Problème avec l'API Hetzner
translated: true
type: note
---

Analysons l'erreur que vous rencontrez et expliquons ce qui se passe avec votre code :

### Erreur :
```
Error creating snapshot for server sg5: cannot perform operation because server is locked (locked, f21b9dc9d1535310)
```

Cette erreur provient de l'API Hetzner Cloud (via le SDK Python `hcloud`) et indique que l'opération de création d'un snapshot pour le serveur nommé `sg5` a échoué car le serveur est **verrouillé**. Un serveur verrouillé signifie qu'une autre opération (par exemple, un snapshot précédent, un redémarrage ou un redimensionnement) est actuellement en cours, et le serveur est temporairement restreint pour accepter de nouvelles opérations jusqu'à ce que ce processus se termine.

### Analyse du Code :
Voici votre script avec des explications et l'origine de l'erreur :

```python
from hcloud import Client
import os

# Récupère le jeton API depuis la variable d'environnement
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# Crée une instance du client
client = Client(token=api_token)

def create_snapshot(server):
    try:
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")

# Liste tous les serveurs
servers = client.servers.get_all()

# Affiche les détails des serveurs et crée des snapshots
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")
    create_snapshot(server)
```

1. **Configuration du Jeton API** :
   - Le script récupère la clé API Hetzner depuis une variable d'environnement (`HERTZNER_API_KEY`). Si elle n'est pas définie, il se termine avec une erreur.

2. **Initialisation du Client** :
   - Une instance `Client` est créée en utilisant le jeton API pour interagir avec l'API Hetzner Cloud.

3. **Fonction `create_snapshot`** :
   - Cette fonction tente de créer un snapshot d'un serveur donné en utilisant `client.servers.create_image()`.
   - Paramètres :
     - `server` : L'objet serveur à snapshotter.
     - `description` : Un nom pour le snapshot (par exemple, `sg5-snapshot`).
     - `type="snapshot"` : Spécifie que le type d'image est un snapshot (par opposition à une sauvegarde ou une ISO).
   - En cas de succès, elle imprime l'ID du snapshot ; sinon, elle capture et imprime toute exception (comme celle que vous voyez).

4. **Liste des Serveurs** :
   - `client.servers.get_all()` récupère une liste de tous les serveurs associés à votre compte Hetzner.
   - Le script les parcourt en boucle, imprime leurs détails (ID, nom, statut, IPs, etc.) et appelle `create_snapshot()` pour chacun.

5. **Où l'Erreur se Produit** :
   - À l'intérieur de la fonction `create_snapshot()`, l'appel `client.servers.create_image()` échoue pour le serveur `sg5` car il est verrouillé. Le message d'exception (`cannot perform operation because server is locked`) est levé par la bibliothèque `hcloud` basée sur la réponse de l'API.

### Pourquoi le Serveur est-il Verrouillé ?
Un serveur devient verrouillé lorsqu'une opération est déjà en cours. Les raisons courantes incluent :
- Un autre snapshot est en cours de création.
- Le serveur est en cours de redémarrage, de redimensionnement ou de reconstruction.
- Une opération précédente ne s'est pas encore terminée.

L'ID de verrou (`f21b9dc9d1535310`) dans le message d'erreur est un identifiant unique pour l'action en cours qui verrouille le serveur.

### Comment le Corriger :
Voici les étapes pour résoudre le problème et améliorer votre script :

#### 1. **Vérifier le Statut de Verrouillage Avant de Continuer**
Modifiez le script pour ignorer la création du snapshot si le serveur est verrouillé. Vous pouvez vérifier les actions actuelles du serveur en utilisant `client.actions.get_all()` ou attendre que le verrou soit levé.

Fonction `create_snapshot` mise à jour :
```python
def create_snapshot(server):
    try:
        # Vérifie si le serveur est verrouillé en regardant ses actions
        actions = client.actions.get_all(server=server)
        for action in actions:
            if action.status == "running":
                print(f"Skipping snapshot for {server.name}: Server is locked by action {action.id}")
                return
        # Si aucune action en cours, procède au snapshot
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 2. **Attendre que le Verrou soit Levé**
Si vous préférez attendre au lieu d'ignorer, vous pouvez interroger périodiquement les actions du serveur jusqu'à ce que le verrou disparaisse :
```python
import time

def wait_for_unlock(server):
    while True:
        actions = client.actions.get_all(server=server)
        running = any(action.status == "running" for action in actions)
        if not running:
            break
        print(f"Waiting for server {server.name} to unlock...")
        time.sleep(5)  # Attend 5 secondes avant de vérifier à nouveau

def create_snapshot(server):
    try:
        wait_for_unlock(server)
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 3. **Enquêter Manuellement sur le Verrou**
- Utilisez la Console Hetzner Cloud ou l'API pour vérifier le statut de l'action avec l'ID `f21b9dc9d1535310`.
- Exemple d'appel API (via Python) :
  ```python
  action = client.actions.get_by_id("f21b9dc9d1535310")
  print(f"Action Status: {action.status}, Command: {action.command}")
  ```
- Si elle est bloquée, vous devrez peut-être contacter le support Hetzner.

#### 4. **Relancer le Script**
Une fois que le serveur n'est plus verrouillé (l'action est terminée ou vous avez résolu le problème manuellement), relancez le script.

### Notes Supplémentaires :
- **Limites de Débit** : Créer des snapshots pour de nombreux serveurs dans une boucle peut atteindre les limites de débit de l'API Hetzner. Ajoutez un délai (par exemple, `time.sleep(1)`) entre les requêtes si nécessaire.
- **Gestion des Erreurs** : Le script actuel s'arrête à la première erreur. Si vous voulez qu'il continue pour les autres serveurs, assurez-vous que l'exception n'arrête pas la boucle (ce qui n'est pas le cas actuellement, ce qui est bien).

N'hésitez pas à me demander si vous avez besoin d'aide pour mettre en œuvre l'une de ces corrections ou pour un débogage plus poussé !