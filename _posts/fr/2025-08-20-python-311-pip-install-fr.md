---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Installer Python 3.11 et pip3.11
translated: true
type: note
---

Il semble que vous ayez plusieurs versions de Python et pip installées sur votre système Ubuntu, et vous souhaitez installer **Python 3.11** et son **pip (pip3.11)** correspondant. Voici comment procéder :

---

### **1. Installer Python 3.11**
Commencez par mettre à jour votre liste de paquets et installez Python 3.11 :

```bash
sudo apt update
sudo apt install python3.11
```

Vérifiez l'installation :

```bash
python3.11 --version
```

---

### **2. Installer pip pour Python 3.11**
Les dépôts par défaut d'Ubuntu peuvent ne pas inclure `pip` pour Python 3.11. Vous pouvez l'installer en suivant ces étapes :

#### **Option A : Installer pip via apt (si disponible)**
```bash
sudo apt install python3.11-venv python3.11-dev python3-pip
```
Si `python3-pip` installe pip pour une version différente, passez à l'**Option B**.

#### **Option B : Installer pip en utilisant ensurepip**
```bash
python3.11 -m ensurepip --upgrade
```
Cela installera pip spécifiquement pour Python 3.11.

#### **Option C : Installer pip en utilisant get-pip.py**
Si les méthodes ci-dessus ne fonctionnent pas, utilisez le script officiel `get-pip.py` :

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
```

---

### **3. Vérifier l'installation de pip3.11**
Vérifiez si `pip3.11` est maintenant disponible :

```bash
pip3.11 --version
```
Vous devriez voir un résultat similaire à :
```
pip 23.x.x from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
```

---

### **4. (Optionnel) Créer un environnement virtuel**
Pour éviter les conflits entre les versions de Python, vous pouvez créer un environnement virtuel :

```bash
python3.11 -m venv myenv
source myenv/bin/activate
```
Maintenant, `pip` à l'intérieur de l'environnement virtuel utilisera Python 3.11.

---

### **Tableau récapitulatif**

| Commande | Objectif |
|---------|---------|
| `sudo apt update` | Mettre à jour la liste des paquets |
| `sudo apt install python3.11` | Installer Python 3.11 |
| `python3.11 -m ensurepip --upgrade` | Installer pip pour Python 3.11 |
| `pip3.11 --version` | Vérifier l'installation de pip |
| `python3.11 -m venv myenv` | Créer un environnement virtuel |

---