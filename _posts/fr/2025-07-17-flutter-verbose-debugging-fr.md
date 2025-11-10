---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide de débogage en mode verbeux de Flutter
translated: true
type: note
---

Ahh compris 👍 — Oui, Flutter a un **mode verbeux** qui affiche *tout* ce qu'il fait en arrière-plan, ce qui te permet de voir où il bloque.

---

### ✅ Exécuter les commandes `flutter` avec la journalisation verbeuse

Il suffit d'ajouter le drapeau `-v` (ou `--verbose`) :

- Pour `flutter clean` :
  ```bash
  flutter clean -v
  ```

- Pour récupérer les dépendances :
  ```bash
  flutter pub get -v
  ```

- Pour exécuter ton application :
  ```bash
  flutter run -v
  ```

Cela déversera des journaux détaillés (appels réseau, suppressions de fichiers, commandes pod, etc.) dans le terminal.

---

### 📌 Conseils pour lire les journaux verbeux
- Regarde les **quelques dernières lignes** affichées avant qu'il ne cesse de répondre → cela te dit à quelle étape il bloque.
- Les blocages se produisent souvent pendant :
  - La résolution **CocoaPods** (réseau lent / dépôt obsolète).
  - La synchronisation **Gradle** (sur la build Android).
  - Les permissions (si Flutter n'a pas accès à certains répertoires).

---

👉 Si `flutter clean -v` semble toujours bloqué, colle ici les ~20 dernières lignes qu'il affiche ⬇️, et je peux t'aider à analyser exactement où il bloque.

Veux-tu que je t'écrive **un script de nettoyage rapide avec verbosité** pour que tu puisses exécuter `./super_clean.sh` au lieu de taper chaque commande ?