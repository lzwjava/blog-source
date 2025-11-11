---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Tuer le processus sur le port avec Psutil
translated: true
type: note
---

### Utilisation de psutil pour détecter et tuer un processus sur un port spécifique (Windows)

Psutil est une bibliothèque Python multiplateforme pour récupérer des informations sur les processus en cours d'exécution et l'utilisation du système. Vous pouvez l'utiliser pour trouver les processus écoutant sur un port spécifique (par exemple, identifier si quelque chose comme un serveur de développement npm est en cours d'exécution sur ce port), puis terminer le processus. Cela fonctionne sur Windows, mais gardez à l'esprit :

- **Permissions** : Sur Windows, la termination des processus nécessite souvent des privilèges d'administrateur (exécutez votre script Python en tant qu'administrateur). Si vous ne le faites pas, une exception `AccessDenied` peut être levée.
- **Détection de port** : Nous nous concentrerons sur les connexions TCP de type 'inet' (qui couvre IPv4 et IPv6). C'est courant pour les serveurs web comme ceux démarrés par `npm run dev` ou similaires.
- **Hypothèses** : Nous supposons que vous souhaitez vérifier un port en écoute (serveur) (par exemple, quelque chose lié localement). Si vous parlez de connexions sortantes vers un port, l'approche est légèrement différente — faites-le moi savoir pour clarification.

#### Étape 1 : Installer psutil
Si vous ne l'avez pas déjà fait :
```bash
pip install psutil
```

#### Étape 2 : Exemple de code pour détecter et tuer
Voici un script Python complet. Il définit une fonction pour trouver le PID du processus écoutant sur un port donné (en utilisant `kind='inet'` comme vous l'avez spécifié), puis le termine. Sur Windows, `terminate()` est préféré à `kill()` car il permet un arrêt gracieux (équivalent à SIGTERM sur Unix).

```python
import psutil
import time  # Pour un délai optionnel

def get_pid_listening_on_port(port, kind='inet'):
    """
    Scanne les connexions réseau pour les processus écoutant sur le port spécifié.
    Retourne une liste de PIDs (généralement un seul, mais pourrait être plusieurs dans de rares cas).
    """
    pids = []
    for conn in psutil.net_connections(kind=kind):
        # Vérifie si c'est une connexion en écoute (status='LISTEN') et si le port de l'adresse locale correspond
        if conn.status == 'LISTEN' and conn.laddr and conn.laddr.port == port:
            if conn.pid:
                pids.append(conn.pid)
    return pids

def kill_process_on_port(port, kind='inet'):
    """
    Trouve et termine le processus écoutant sur le port spécifié.
    Si plusieurs processus, les tue tous (avec un avertissement).
    """
    pids = get_pid_listening_on_port(port, kind)
    if not pids:
        print(f"Aucun processus trouvé en écoute sur le port {port}.")
        return
    
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            print(f"Terminaison du processus {proc.name()} (PID {pid}) sur le port {port}...")
            # Utilise terminate() pour un arrêt gracieux ; cela envoie un signal similaire à SIGTERM
            proc.terminate()
            # Optionnel : Attendre un peu et forcer l'arrêt s'il ne se termine pas
            gone, still_alive = psutil.wait_procs([proc], timeout=3)
            if still_alive:
                print(f"Arrêt forcé du PID {pid}...")
                still_alive[0].kill()
        except psutil.AccessDenied:
            print(f"Accès refusé : Impossible de terminer le PID {pid}. Exécuter en tant qu'administrateur ?")
        except psutil.NoSuchProcess:
            print(f"Le processus {pid} n'existe plus.")

# Exemple d'utilisation : Remplacez 3000 par votre port cible (par exemple, les serveurs de développement npm utilisent souvent le port 3000)
if __name__ == "__main__":
    kill_process_on_port(3000)  # Ajustez kind si nécessaire (par exemple, 'inet4' pour IPv4 uniquement)
```

#### Explications clés
- **`psutil.net_connections(kind='inet')`** : Cela récupère les connexions réseau de type 'inet' (comprenant IPv4 et IPv6). Chaque connexion est un namedtuple avec des champs comme :
  - `laddr` : Adresse locale (par exemple, ('0.0.0.0', 8080) – IP et port).
  - `status` : 'LISTEN' pour les serveurs en attente de connexions.
  - `pid` : ID du processus propriétaire.
  - Nous filtrons pour `status == 'LISTEN'` pour trouver les serveurs (comme le port de développement npm), pas les connexions client.
- **Récupération du PID** : Le script obtient directement le PID à partir du tuple de connexion. Si vous voulez seulement détecter sans tuer, utilisez `get_pid_listening_on_port(port)` qui retourne le(s) PID(s).
- **Terminaison du processus** :
  - `psutil.Process(pid).terminate()` : Envoie un signal de terminaison. Sur Windows, c'est comme CTRL+C.
  - S'il ne se termine pas, nous forçons optionnellement l'arrêt avec `kill()` (équivalent à SIGKILL).
  - `wait_procs()` de Psutil attend que le processus meure.
- **Spécificité du type 'inet'** : 'inet' inclut à la fois IPv4 et IPv6. Si vous savez que c'est IPv4, changez pour `kind='inet4'`. CET NOM répond directement à votre demande concernant le type "inet".
- **Notes spécifiques à Windows** :
  - Psutil gère bien les internals de Windows, mais les informations réseau peuvent nécessiter des privilèges élevés dans certains cas.
  - Pour les ports en dessous de 1024 (privilégiés), seuls les services système peuvent se lier, mais la détection devrait toujours fonctionner.
- **Gestion des erreurs** : Des vérifications de base ont été ajoutées pour l'absence de processus ou les problèmes d'accès.
- **Test** : Exécutez quelque chose comme `npm run dev` pour occuper le port 3000, puis exécutez ce script.

Si cela ne correspond pas exactement à votre besoin (par exemple, si "npm run port" signifie autre chose ou si vous voulez détecter des connexions non en écoute), fournissez plus de détails pour un ajustement ! Pour la sécurité, assurez-vous de ne tuer que les processus souhaités.