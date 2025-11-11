---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Résoudre l'Incompatibilité Ruby de CocoaPod sur macOS
translated: true
type: note
---

Je vois ce qui se passe : votre configuration système Ruby et gems est un peu mélangée, donc la commande `pod deintegrate` ne trouve pas CocoaPods. Suivons cela étape par étape :

---

### Problème
- Vous êtes sur macOS (`arm64` probablement, M1/M2).
- Vous avez mis à jour Ruby (vers 3.4.1 via Homebrew).
- Votre exécutable `pod` appartient à l'ancienne version de Ruby (chemin des gems 3.3.0 : `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`).
- Mais maintenant Ruby 3.4.1 est actif, donc il ne trouve pas les gems `cocoapods` au bon endroit.

Ce décalage est la raison de l'échec.

---

### Solutions

#### 1. Réinstaller CocoaPods en utilisant la version de Ruby que vous exécutez réellement
```bash
gem install cocoapods
```

Puis vérifiez avec :
```bash
which pod
pod --version
```

---

#### 2. Si vous utilisez le Ruby de `brew`, il est préférable d'installer CocoaPods via Homebrew aussi
```bash
brew install cocoapods
```

Cela évite complètement les problèmes de version de Ruby.

---

#### 3. Si vous utilisez `rbenv` ou `rvm`, assurez-vous d'être dans l'environnement de la bonne version de Ruby
Par exemple, avec `rbenv` :
```bash
rbenv global 3.4.1
gem install cocoapods
```

---

#### 4. Nettoyer les anciens liens symboliques du binaire pod
Vérifiez d'où vient la commande `pod` orpheline :
```bash
which pod
```
Si elle pointe vers `/opt/homebrew/lib/ruby/gems/3.3.0/bin/pod`, supprimez-la ou mettez à jour votre `PATH` pour qu'il utilise la bonne.

---

✅ Recommandé (simple et stable) : Exécutez simplement
```bash
brew install cocoapods
```
puis réessayez :
```bash
pod deintegrate
```

---

Souhaitez-vous que je vous aide à **corriger le PATH pour qu'il sélectionne toujours le bon binaire pod**, ou simplement la réinstallation la plus rapide ?