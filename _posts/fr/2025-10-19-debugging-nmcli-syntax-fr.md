---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Pièges de syntaxe de nmcli pour le débogage
translated: true
type: note
---

Oui, tu as parfaitement raison — la programmation (surtout quand on manipule des commandes shell, des sous-processus ou des outils comme `nmcli`) est absolument pleine de ce genre de pièges de syntaxe pointilleux. Ce ne sont pas des "erreurs" au sens d'un système cassé ou d'un bug insoluble ; ce sont juste des particularités spécifiques à une version ou des préférences non documentées dans les interfaces en ligne de commande qui finissent par piéger tout le monde à un moment ou un autre. Les outils évoluent, la documentation prend du retard, et une lettre de différence (comme `iface` vs `ifname`) peut tout arrêter. C'est frustrant mais très courant, et la solution est généralement simple une fois qu'on l'a repérée.

D'après la sortie que tu as partagée, on dirait que le script a rencontré exactement ce problème sur plusieurs réseaux : `nmcli` rejetant `iface` comme argument invalide (ce qui est logique, car l'option officielle a toujours été `ifname` pour spécifier le nom de l'interface dans les commandes de connexion). La modification que tu as appliquée — remplacer par `ifname {interface}` à la ligne 113 — devrait résoudre le problème proprement. Cette diff est précise et minimale, donc aucun risque d'introduire de nouveaux effets secondaires.

### Suggestion de Test Rapide
Pour vérifier le correctif sans avoir à re-scanner les 35 réseaux, tu pourrais temporairement ajouter un debug print juste après l'appel `subprocess.run` dans `test_wifi_connection` (autour de la ligne 114) :

```python
result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
print(f"Debug: Ran '{cmd}' -> returncode: {result.returncode}, stdout: '{result.stdout}', stderr: '{result.stderr}'")  # Ajouter cette ligne
```

Exécute-le sur seulement un ou deux SSID (par exemple en tronchant la liste temporairement), et il devrait maintenant afficher une tentative de connexion réussie ou une erreur plus révélatrice (comme un échec d'authentification) au lieu de la plainte sur l'argument.

Si tu rencontres encore des problèmes après cela (par exemple sur des réseaux spécifiques comme "HONG GOR 1" ou ceux sans nom avec `--`), colle la nouvelle sortie ici — cela pourrait être des problèmes d'encodage du mot de passe, des caractères cachés dans les SSID, ou même des particularités du pilote sur ton matériel. Nous pouvons itérer à partir de là. À quoi ressemble la prochaine exécution ?