---
audio: false
generated: true
lang: fr
layout: post
title: Gestion des certificats non fiables dans IntelliJ IDEA
translated: true
type: note
---

La boîte de dialogue "Certificat du serveur non approuvé" dans IntelliJ IDEA apparaît souvent lorsque l'IDE rencontre des certificats SSL qui ne sont pas approuvés par son keystore, tels que des certificats auto-signés ou des certificats d'entreprise personnalisés. Étant donné que vous avez déjà importé le keystore de votre entreprise dans `/lib/cacerts` mais que l'invite persiste, le problème peut provenir du fait qu'IntelliJ n'utilise pas ce keystore ou que des certificats supplémentaires déclenchent la boîte de dialogue. Voici comment résoudre le problème et potentiellement arrêter les invites :

### Option 1 : Configurer IntelliJ pour accepter automatiquement les certificats non approuvés
Activer cette option demande à IntelliJ de contourner la boîte de dialogue pour les certificats non approuvés, mais soyez prudent car cela réduit la sécurité en acceptant tous les certificats, vous exposant potentiellement à des attaques de type man-in-the-middle.

- **Windows/Linux** :
  1. Allez dans `File > Settings > Tools > Server Certificates`.
  2. Cochez la case **"Accept non-trusted certificates automatically"**.
  3. Cliquez sur **Apply** puis **OK**.
- **macOS** :
  1. Allez dans `IntelliJ IDEA > Preferences > Tools > Server Certificates`.
  2. Cochez **"Accept non-trusted certificates automatically"**.
  3. Cliquez sur **Apply** puis **OK**.

**Remarque** : Cette option n'est pas recommandée, sauf si vous vous trouvez dans un réseau de confiance et isolé (par exemple, un environnement d'entreprise en air gap), car elle peut rendre votre IDE vulnérable à des connexions non vérifiées.

### Option 2 : Vérifier et corriger la configuration du Keystore
Étant donné que vous avez importé le keystore d'entreprise dans `/lib/cacerts`, assurez-vous qu'IntelliJ l'utilise correctement. Le problème peut être qu'IntelliJ référence toujours son propre truststore ou le mauvais fichier cacerts.

1. **Vérifier le chemin du Keystore** :
   - IntelliJ utilise souvent son propre truststore situé à `~/.IntelliJIdea<version>/system/tasks/cacerts` ou le truststore de JetBrains Runtime (JBR) à `<IntelliJ Installation>/jbr/lib/security/cacerts`.
   - Si vous avez modifié `/lib/cacerts` dans le répertoire d'IntelliJ, confirmez qu'il s'agit du bon chemin pour votre version de l'IDE. Pour les installations via JetBrains Toolbox, le chemin peut différer (par exemple, `~/AppData/Local/JetBrains/Toolbox/apps/IDEA-U/ch-0/<version>/jbr/lib/security/cacerts` sur Windows).
   - Utilisez la commande `keytool` pour vérifier que le certificat est bien dans le fichier cacerts :
     ```bash
     keytool -list -keystore <chemin-vers-cacerts> -storepass changeit
     ```
     Assurez-vous que votre certificat d'autorité de certification d'entreprise est listé.

2. **Pointer IntelliJ vers le Keystore personnalisé** :
   - Si le certificat est correctement importé mais qu'IntelliJ affiche toujours l'invite, il se peut qu'il n'utilise pas le cacerts modifié. Ajoutez une option VM personnalisée pour spécifier le truststore :
     1. Allez dans `Help > Edit Custom VM Options`.
     2. Ajoutez :
        ```
        -Djavax.net.ssl.trustStore=<chemin-vers-cacerts>
        -Djavax.net.ssl.trustStorePassword=changeit
        ```
        Remplacez `<chemin-vers-cacerts>` par le chemin complet vers votre fichier `cacerts` modifié.
     3. Redémarrez IntelliJ IDEA.

3. **Réimporter le certificat** :
   - Si l'importation du certificat était incomplète ou incorrecte, réimportez-le :
     ```bash
     keytool -import -trustcacerts -file <fichier-certificat>.cer -alias <alias> -keystore <chemin-vers-cacerts> -storepass changeit
     ```
     Remplacez `<fichier-certificat>.cer` par votre certificat d'autorité de certification d'entreprise et `<chemin-vers-cacerts>` par le chemin correct du fichier cacerts.

### Option 3 : Ajouter des certificats via les paramètres Server Certificates d'IntelliJ
Au lieu de modifier manuellement le fichier cacerts, vous pouvez ajouter des certificats via l'interface d'IntelliJ, qui les stocke dans son truststore interne :

1. Allez dans `File > Settings > Tools > Server Certificates` (ou `IntelliJ IDEA > Preferences` sur macOS).
2. Cliquez sur le bouton **"+"** pour ajouter un nouveau certificat.
3. Parcourez jusqu'à votre fichier de certificat d'autorité de certification d'entreprise (au format `.cer` ou `.pem`) et importez-le.
4. Redémarrez IntelliJ pour vous assurer que le certificat est reconnu.

### Option 4 : Vérifier les interférences de proxy ou d'antivirus
Les environnements d'entreprise utilisent souvent des proxys ou des logiciels antivirus (par exemple, Zscaler, Forcepoint) qui effectuent une inspection SSL de type man-in-the-middle, générant dynamiquement de nouveaux certificats. Cela peut provoquer des invites répétées si les certificats changent fréquemment (par exemple, quotidiennement, comme avec McAfee Endpoint Security).

- **Importer le certificat d'autorité de certification du proxy/antivirus** :
  - Obtenez le certificat racine de l'autorité de certification auprès de votre proxy ou logiciel antivirus (demandez à votre équipe informatique).
  - Importez-le dans le truststore d'IntelliJ via `Settings > Tools > Server Certificates` ou dans le fichier cacerts en utilisant la commande `keytool` ci-dessus.
- **Désactiver l'inspection SSL (si possible)** :
  - Si votre proxy le permet, configurez-le pour contourner l'inspection SSL pour les domaines liés à IntelliJ (par exemple, `plugins.jetbrains.com`, `repo.maven.apache.org`).

### Option 5 : Déboguer et identifier les certificats problématiques
Si le problème persiste, identifiez quel serveur ou certificat cause l'invite :

1. Activer la journalisation SSL verbose :
   - Allez dans `Help > Edit Custom VM Options` et ajoutez :
     ```
     -Djavax.net.debug=ssl:handshake:verbose
     ```
   - Redémarrez IntelliJ et vérifiez le fichier `idea.log` (situé dans `~/.IntelliJIdea<version>/system/log/`) pour les erreurs SSL, telles que `PKIX path building failed`. Cela indiquera le serveur ou le certificat problématique.

2. Vérifier les plugins ou intégrations spécifiques :
   - Les plugins comme Maven, Gradle ou les systèmes de contrôle de version (par exemple, Git, SVN) peuvent se connecter à des serveurs avec des certificats différents. Désactivez temporairement les plugins pour isoler le problème.
   - Pour Maven, assurez-vous que le JDK configuré dans `File > Settings > Build, Execution, Deployment > Build Tools > Maven > Runner` utilise le cacerts mis à jour.

### Notes supplémentaires
- **Avertissement de sécurité** : Accepter automatiquement les certificats non approuvés est pratique mais risqué dans les réseaux non isolés. Utilisez cette option uniquement dans des environnements de confiance.
- **Synchronisation de l'heure système** : Assurez-vous que l'horloge de votre système est synchronisée, car un décalage peut causer des problèmes de validation de certificat.
- **JetBrains Runtime (JBR)** : IntelliJ s'exécute sur son propre JBR, qui peut ne pas utiliser le truststore Java du système. Les modifications apportées au `$JAVA_HOME/lib/security/cacerts` du système n'affecteront pas IntelliJ, sauf configuration explicite.
- **Invites persistantes** : Si les invites persistent après l'importation du certificat, cela peut être dû à un plugin ou service (par exemple, JFrog, SonarQube) utilisant un truststore différent. Vérifiez les paramètres du plugin ou contactez votre équipe informatique pour obtenir la chaîne de certificats complète.

### Approche recommandée
1. Essayez d'abord l'**Option 3** (ajouter des certificats via l'interface d'IntelliJ), car c'est la plus sûre et la plus simple.
2. Si cela échoue, vérifiez le chemin et la configuration du keystore avec l'**Option 2**.
3. Utilisez l'**Option 1** (acceptation automatique) uniquement en dernier recours dans un environnement de confiance.
4. Si le problème implique un proxy ou un antivirus, travaillez avec votre équipe informatique pour obtenir et importer les certificats d'autorité de certification corrects.

Si vous rencontrez toujours des problèmes, partagez des détails sur le certificat (par exemple, émetteur, domaine) ou tout message d'erreur du fichier `idea.log`, et je pourrai vous aider à affiner le diagnostic.