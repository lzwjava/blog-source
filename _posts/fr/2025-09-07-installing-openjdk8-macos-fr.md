---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Installation d'OpenJDK 8 sur macOS
translated: true
type: note
---

Voici comment installer **OpenJDK 8** (Java SE 8) sur macOS en **2025**, avec des méthodes couvrant Homebrew, SDKMAN, les installateurs manuels et MacPorts. Pas de tableaux—juste des étapes claires et simples :

---

## 1. Utilisation de Homebrew (`openjdk@8`)

Cela reste l'une des façons les plus simples d'installer OpenJDK 8 sur macOS.

### Étapes :

1. Ouvrez le Terminal.

2. Exécutez :

   ```bash
   brew install openjdk@8
   ```

   ([Homebrew Formulae][1])

3. Après l'installation, liez le JDK pour que les outils macOS puissent le détecter :

   ```bash
   sudo ln -sfn $(brew --prefix)/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-8.jdk
   ```

   ([Homebrew Formulae][1])

4. Optionnellement, ajoutez OpenJDK 8 à votre PATH dans votre configuration de shell (par exemple, `.zshrc`) :

   ```bash
   export PATH="$(brew --prefix openjdk@8)/bin:$PATH"
   ```

**Note pour les utilisateurs Apple Silicon (série M) :**
Si vous rencontrez des problèmes d'architecture, vous devrez peut-être exécuter Homebrew sous Rosetta 2 :

```bash
env /usr/bin/arch -x86_64 /bin/zsh --login
brew install openjdk@8
```

Puis procédez à la création du lien symbolique et à la configuration du PATH ([Stack Overflow][2]).

---

## 2. Via SDKMAN (gestionnaire de versions Java)

SDKMAN est un outil flexible pour installer et alterner entre plusieurs versions de Java.

### Installation rapide :

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk list java
sdk install java 8.xxx-tem
```

Remplacez `8.xxx-tem` par l'identifiant affiché dans `sdk list java`. ([Stack Overflow][2])

---

## 3. Installation Manuelle (Oracle / Adoptium / AdoptOpenJDK)

### Option A : Installateur .dmg / .pkg d'Oracle

1. Téléchargez le bon installateur pour votre architecture depuis la page de téléchargement de Java SE 8 d'Oracle.
2. Ouvrez le `.dmg`, exécutez l'installateur `.pkg` et suivez les instructions. ([Documentation Oracle][3])
3. Une fois installé, utilisez des outils comme `java_home` pour choisir la version :

   ```bash
   /usr/libexec/java_home -v 1.8 --exec java -version
   ```

### Option B : Builds AdoptOpenJDK ou similaires

AdoptOpenJDK (maintenant sous Eclipse Adoptium) fournit des builds—avec des options d'installateur et d'archive.

* Par exemple, la documentation Salesforce en août 2025 suggère d'utiliser le site AdoptOpenJDK, de choisir OpenJDK 8 (LTS) avec la JVM HotSpot, et de procéder via son installateur. ([Salesforce][4])

Après l'installation, définissez votre JAVA\_HOME, par exemple :

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
export PATH=$JAVA_HOME/bin:$PATH
```

---

## 4. MacPorts

Si vous utilisez MacPorts au lieu de Homebrew, l'installation d'OpenJDK 8 est simple :

```bash
sudo port install openjdk8
```

Pour voir ce qui est installé :

```bash
port contents openjdk8
```

Pour mettre à jour plus tard :

```bash
sudo port selfupdate && sudo port upgrade openjdk8
```

([MacPorts][5])

---

## Choisir la Bonne Méthode pour Vous

| Intention                                          | Méthode Recommandée                             |
| -------------------------------------------------- | ----------------------------------------------- |
| Installation rapide et maintenance facile          | **Homebrew (`brew install openjdk@8`)**         |
| Gérer plusieurs versions Java simultanées          | **SDKMAN**                                      |
| Contrôle total et installateur officiel (GUI)      | **Installation manuelle `.dmg` ou `.pkg`** via Oracle/Adoptium |
| Préférence pour l'écosystème MacPorts              | **MacPorts**                                    |

---

## Vérification de l'Installation

Après l'installation, vérifiez avec :

```bash
java -version
```

Attendez-vous à quelque chose comme `"1.8.0_xxx"` pour confirmer que Java 8 est actif. Pour un contrôle précis :

```bash
/usr/libexec/java_home -v 1.8 --exec javac -version
```

---

## Dernières Réflexions

Pour résumer :

* **Homebrew** est la méthode la plus populaire en 2025—il suffit de `brew install openjdk@8`, puis de créer le lien et de configurer le PATH.
* **SDKMAN** vous offre de la flexibilité si vous changez fréquemment de version Java.
* **Les installateurs manuels** (Oracle, Adoptium) restent une solution de repli solide, basée sur une interface graphique.
* **MacPorts** fonctionne si c'est votre gestionnaire de paquets préféré.

Faites-moi savoir si vous avez besoin d'aide pour la configuration dans votre shell, pour alterner entre les versions de Java ou pour toute autre chose en cours de route !

[1]: https://formulae.brew.sh/formula/openjdk%408?utm_source=chatgpt.com "openjdk@8"
[2]: https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac?utm_source=chatgpt.com "How to install Java 8 on Mac"
[3]: https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html?utm_source=chatgpt.com "JDK 8 Installation for macOS"
[4]: https://help.salesforce.com/s/articleView?id=001117155&language=en_US&type=1&utm_source=chatgpt.com "How to Install OpenJDK 8 on macOS to Work with Anypoint ..."
[5]: https://ports.macports.org/port/openjdk8/?utm_source=chatgpt.com "Install openjdk8 on macOS with MacPorts"