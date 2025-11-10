---
audio: false
generated: true
lang: fr
layout: post
title: Simulation de bascules en Python
translated: true
type: note
---

Créons un programme Python simple pour simuler le comportement des différents types de bascules (RS, D, JK et T) décrits précédemment. Comme les bascules sont des composants matériels, nous modéliserons leur logique dans des classes Python pour imiter leur comportement, y compris les entrées, les sorties et les changements d'état. Le programme nous permettra de saisir des valeurs pour les commandes de la bascule (comme S, R, D, J, K, T et l'horloge) et d'afficher la sortie (Q) en fonction de leurs règles. Nous le garderons simple et basé sur du texte, adapté à un débutant pour comprendre, avec une interface en ligne de commande pour tester chaque bascule.

Voici le plan :
- Créer une classe de base `FlipFlop` pour gérer les attributs communs comme l'état actuel (Q).
- Créer des classes spécifiques pour `RSFlipFlop`, `DFlipFlop`, `JKFlipFlop` et `TFlipFlop`, chacune implémentant son comportement unique.
- Simuler l'horloge en exigeant un "tick" pour mettre à jour l'état, imitant ainsi le fonctionnement des bascules sur les impulsions d'horloge.
- Fournir une boucle interactive simple pour tester chaque bascule en entrant les valeurs d'entrée et en voyant la sortie.
- Utiliser des instructions d'impression pour montrer les changements d'état, en restant clair et pédagogique.

Le code n'utilisera pas de bibliothèques externes (comme pygame) puisque nous simulons seulement la logique, et il s'exécutera dans un environnement Python standard. L'artefact sera un script Python que vous pourrez exécuter pour expérimenter avec les bascules.

```python
# Classe de base pour toutes les bascules
class FlipFlop:
    def __init__(self):
        self.Q = 0  # État actuel (sortie)
        self.Q_next = 0  # État suivant (à mettre à jour sur le tick d'horloge)

    def get_output(self):
        return self.Q

    def tick(self):
        self.Q = self.Q_next  # Mettre à jour l'état sur le tick d'horloge

# Bascule RS
class RSFlipFlop(FlipFlop):
    def update(self, S, R):
        if S == 1 and R == 1:
            print("Avertissement : État invalide (S=1, R=1) - Aucun changement")
            return
        elif S == 1 and R == 0:
            self.Q_next = 1  # Set (Mise à 1)
        elif S == 0 and R == 1:
            self.Q_next = 0  # Reset (Remise à 0)
        # Si S=0, R=0, maintient l'état précédent (aucun changement pour Q_next)

# Bascule D
class DFlipFlop(FlipFlop):
    def update(self, D):
        self.Q_next = D  # La sortie deviendra D au prochain tick d'horloge

# Bascule JK
class JKFlipFlop(FlipFlop):
    def update(self, J, K):
        if J == 0 and K == 0:
            pass  # Aucun changement
        elif J == 0 and K == 1:
            self.Q_next = 0  # Reset (Remise à 0)
        elif J == 1 and K == 0:
            self.Q_next = 1  # Set (Mise à 1)
        elif J == 1 and K == 1:
            self.Q_next = 1 - self.Q  # Bascule (Toggle)

# Bascule T
class TFlipFlop(FlipFlop):
    def update(self, T):
        if T == 0:
            pass  # Aucun changement
        elif T == 1:
            self.Q_next = 1 - self.Q  # Bascule (Toggle)

# Fonction pour obtenir une entrée binaire valide (0 ou 1)
def get_binary_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1]:
                return value
            print("Veuillez entrer 0 ou 1.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer 0 ou 1.")

# Fonction principale de simulation
def simulate_flip_flop():
    print("Bienvenue dans le simulateur de bascules !")
    print("Choisissez une bascule à tester :")
    print("1. Bascule RS")
    print("2. Bascule D")
    print("3. Bascule JK")
    print("4. Bascule T")
    print("5. Quitter")

    choice = input("Entrez votre choix (1-5): ")

    if choice == "5":
        print("Au revoir !")
        return

    if choice == "1":
        ff = RSFlipFlop()
        print("\nBascule RS : Entrez S et R (0 ou 1).")
        while True:
            S = get_binary_input("Entrez S: ")
            R = get_binary_input("Entrez R: ")
            ff.update(S, R)
            ff.tick()
            print(f"Sortie Q: {ff.get_output()}")
            if input("Continuer? (o/n): ").lower() != 'o':
                break

    elif choice == "2":
        ff = DFlipFlop()
        print("\nBascule D : Entrez D (0 ou 1).")
        while True:
            D = get_binary_input("Entrez D: ")
            ff.update(D)
            ff.tick()
            print(f"Sortie Q: {ff.get_output()}")
            if input("Continuer? (o/n): ").lower() != 'o':
                break

    elif choice == "3":
        ff = JKFlipFlop()
        print("\nBascule JK : Entrez J et K (0 ou 1).")
        while True:
            J = get_binary_input("Entrez J: ")
            K = get_binary_input("Entrez K: ")
            ff.update(J, K)
            ff.tick()
            print(f"Sortie Q: {ff.get_output()}")
            if input("Continuer? (o/n): ").lower() != 'o':
                break

    elif choice == "4":
        ff = TFlipFlop()
        print("\nBascule T : Entrez T (0 ou 1).")
        while True:
            T = get_binary_input("Entrez T: ")
            ff.update(T)
            ff.tick()
            print(f"Sortie Q: {ff.get_output()}")
            if input("Continuer? (o/n): ").lower() != 'o':
                break

    else:
        print("Choix invalide. Veuillez réessayer.")
    
    simulate_flip_flop()  # Redémarre le menu

# Exécuter le simulateur
if __name__ == "__main__":
    simulate_flip_flop()
```

**Comment exécuter le code :**
1. Enregistrez le code dans un fichier nommé `flip_flop_simulator.py`.
2. Exécutez-le en utilisant Python (par exemple, `python flip_flop_simulator.py`).
3. Suivez les invites pour choisir une bascule (1-4) ou quitter (5).
4. Entrez les valeurs d'entrée (0 ou 1) pour les entrées de la bascule sélectionnée (par exemple, S et R pour RS, D pour D, etc.).
5. Le programme affichera la sortie Q après chaque tick d'horloge.
6. Choisissez de continuer à tester la même bascule ou de revenir au menu.

**Ce qu'il fait :**
- Le programme simule le comportement de chaque type de bascule comme décrit (RS, D, JK, T).
- Par exemple, dans la bascule RS, entrer S=1, R=0 définit Q à 1 ; entrer S=1, R=1 avertit de l'état invalide.
- La bascule D copie l'entrée D vers Q à chaque tick.
- La bascule JK gère la mise à 1, la remise à 0 et la bascule en fonction de J et K.
- La bascule T bascule Q lorsque T=1.
- C'est interactif et boucle pour que vous puissiez continuer à tester différentes entrées.

Faites-moi savoir si vous souhaitez modifier le code, ajouter des fonctionnalités (comme un compteur utilisant des bascules T) ou si vous avez des questions !