---
audio: true
generated: false
lang: fr
layout: post
title: Sortie Verbose
translated: true
---

- Pour activer la sortie verbale dans Homebrew, utilisez `export HOMEBREW_CURL_VERBOSE=1` en conjunction avec `brew upgrade --verbose`.

- Pour augmenter la verbosité dans SSH, utilisez `ssh -vvv user@host`.

- Pour une sortie plus verbale avec `git`, utilisez `git -v` ou `git --verbose`.

- Pour obtenir plus de sortie de `rsync`, utilisez `rsync -vv source destination`.

- écrire une configuration verbale dans ssh config, comme avoir LogLevel VERBOSE dans .ssh/config.

- Pour activer la sortie verbale avec `npm`, utilisez `npm install --verbose` ou `npm run <script> --verbose`.

- Pour la journalisation verbale dans Node.js, utilisez la variable d'environnement `NODE_DEBUG` : `NODE_DEBUG=http,net node your_script.js`.

- Pour obtenir une sortie verbale de `curl`, utilisez `curl -v <url>`.

- Pour activer la sortie verbale avec `pip`, utilisez `pip install -v <package>` ou `pip install --verbose <package>`.

- Pour une sortie verbale avec `wget`, utilisez `wget --verbose <url>`.

- Pour obtenir une sortie verbale de `yum`, utilisez `yum -v install <package>`.

- Pour activer la sortie verbale avec `apt-get`, utilisez `apt-get -o Debug::pkgProblemResolver=yes install <package>`.

- Pour la journalisation verbale avec `adb`, utilisez `adb logcat -v verbose`.

- Pour exécuter Python en mode verbeux, utilisez `python -v your_script.py`.

- Pour compiler du code Java avec une sortie verbale, utilisez `javac -verbose YourClass.java`.

- Pour démarrer VSCode en mode verbeux : `code --verbose`. Pour la journalisation, définissez `"trace": true` dans `settings.json` et consultez les journaux via "Developer: Open View..." -> "Log (Window)" ou "Log (Extension Host)".

- Pour la journalisation verbale avec IntelliJ IDEA : "Help" -> "Diagnostic Tools" -> "Debug Log Settings..." ou ajoutez `-Didea.logging.level=DEBUG` à `idea.vmoptions`. Les journaux se trouvent dans le répertoire "log" sous le répertoire de configuration d'IntelliJ IDEA.

- Pour activer la sortie verbale dans Eclipse, modifiez `eclipse.ini` avec `-debug` ou `-consoleLog`. Pour une journalisation détaillée, configurez Log4j ou java.util.logging. L'emplacement du journal dépend de la configuration de la journalisation.

- Pour obtenir une sortie verbale de Maven, utilisez `mvn -X <command>`. Par exemple, `mvn -X clean install`.

- Pour activer la journalisation verbale dans WebSphere Liberty Server, configurez le fichier `server.xml` pour inclure `<logging traceSpecification="*=info:com.ibm.ws.*=all:"/>`. Vous pouvez également utiliser les fichiers `console.log` et `messages.log` pour des journaux détaillés.

- Pour une sortie verbale avec l'AWS CLI, utilisez le drapeau `--debug` : `aws <command> --debug`.

- Pour obtenir une sortie verbale de `gcloud`, utilisez le drapeau `--verbosity` : `gcloud <command> --verbosity=debug`.

- Pour activer la sortie verbale dans Gradle, utilisez le drapeau `-v` ou `--verbose` : `gradle <task> -v`. Pour une journalisation plus détaillée, utilisez `--debug` : `gradle <task> --debug`.

- Pour une sortie verbale avec Docker, utilisez le drapeau `--verbose` (si disponible pour la commande spécifique) ou consultez les journaux du démon Docker. Vous pouvez configurer le niveau de journalisation du démon Docker dans le fichier `daemon.json`.

- Pour obtenir une sortie verbale de Terraform, définissez la variable d'environnement `TF_LOG` sur `DEBUG` ou `TRACE` : `export TF_LOG=DEBUG` ou `export TF_LOG=TRACE`.

- Pour activer la sortie verbale avec Ansible, utilisez les drapeaux `-v`, `-vv`, `-vvv`, ou `-vvvv` pour augmenter la verbosité : `ansible-playbook playbook.yml -vvv`.

- Pour une sortie verbale avec Kubernetes `kubectl`, utilisez le drapeau `--v` suivi d'un nombre indiquant le niveau de verbosité (par exemple, `--v=6` ou `--v=9`) : `kubectl get pods --v=6`.

- Pour obtenir une sortie verbale de systemd, utilisez `journalctl -b -x` pour afficher les journaux avec des explications ou `systemctl --full --all status <service>`.