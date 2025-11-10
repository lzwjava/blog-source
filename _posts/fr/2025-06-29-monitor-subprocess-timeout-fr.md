---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Surveillance de la sortie d'un sous-processus avec délai d'attente
translated: true
type: note
---

```python
import subprocess
import threading
import queue
import time
import sys

def read_output(proc, output_queue):
    """Fonction de thread pour lire stdout et stderr, les mettre dans la file."""
    try:
        for line in iter(proc.stdout.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
        # Vérifie aussi stderr si nécessaire
        for line in iter(proc.stderr.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
    except Exception as e:
        output_queue.put(f"Erreur de lecture de sortie: {e}")

def main():
    # Commande à exécuter (ex: 'mvn clean compile' sur Windows)
    cmd = ['mvn', 'clean', 'compile']  # Ajuster si nécessaire, ex: ['cmd', '/c', 'mvn build']
    timeout_seconds = 10

    # Démarrer le sous-processus
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # Tamponné par ligne
        universal_newlines=False,  # Gérer les octets
        cwd=None  # Définir le répertoire de travail si nécessaire
    )

    # File pour la sortie
    output_queue = queue.Queue()

    # Démarrer le thread pour lire la sortie
    output_thread = threading.Thread(target=read_output, args=(proc, output_queue))
    output_thread.daemon = True
    output_thread.start()

    print("Commande démarrée. Surveillance de la sortie toutes les 10 secondes...")

    while proc.poll() is None:
        try:
            # Attendre la sortie avec timeout
            output = output_queue.get(timeout=timeout_seconds)
            print(f"Sortie: {output}")  # Optionnel: afficher ou traiter la sortie
        except queue.Empty:
            print(f"Aucune sortie depuis {timeout_seconds} secondes. Arrêt de la commande et sortie.")
            proc.terminate()  # ou proc.kill() pour un arrêt forcé
            try:
                proc.wait(timeout=5)  # Attendre un peu pour un arrêt gracieux
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

    # Le processus s'est terminé normalement
    print("Commande terminée.")
    output_thread.join()  # Attendre que le thread de sortie se termine

if __name__ == "__main__":
    main()
```

### Explication
- **Sous-processus**: Utilise `subprocess.Popen` pour exécuter `mvn clean compile` (ajuster la commande si nécessaire; pour un simple `mvn build`, cela pourrait être `['mvn', 'build']` ou encapsulé dans `cmd /c` si nécessaire). Il est exécuté de manière asynchrone avec des pipes pour stdout et stderr.
- **File et Threads**: Un thread séparé lit depuis stdout et stderr ligne par ligne (pour éviter de lire toute la sortie en une fois), la décode et place les lignes dans une `queue.Queue`. Cela permet des lectures non bloquantes.
- **Surveillance du Timeout**: Dans le thread principal, vérifier la file pour une nouvelle sortie avec `get(timeout=10)`. Si aucune sortie n'arrive dans les 10 secondes, terminer le sous-processus et quitter.
- **Compatibilité Windows**: `subprocess` fonctionne sur Windows. Si la commande nécessite un shell (ex: pour `mvn` si pas dans le PATH), vous pourriez définir `shell=True` et passer la commande comme chaîne: `proc = subprocess.Popen("mvn clean compile", shell=True, ...)`.
- **Cas particuliers**: Si le processus se termine normalement pendant l'attente, la boucle s'arrête et on joint le thread. Le thread est démon pour éviter un blocage à la sortie.
- **Personnalisation**: Vous pouvez modifier pour traiter les sorties différemment (ex: journaliser dans un fichier au lieu d'afficher). Pour stderr, c'est combiné dans la même file; vous pourriez séparer si nécessaire. Si les sorties sont binaires, ajuster le décodage.