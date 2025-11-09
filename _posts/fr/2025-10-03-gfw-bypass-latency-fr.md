---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Optimisation du contournement de la GFW et de la latence
translated: true
type: note
---

Merci d'avoir partagé votre configuration et vos expériences—on dirait une évolution bien pensée depuis votre combinaison initiale de script proxy et VPN vers l'approche par carte SIM de Macao pour un accès cellulaire direct. C'est super d'entendre que cela fonctionne bien depuis deux mois, surtout avec le script Python automatisant la sélection du proxy (en priorisant Singapour pour les outils d'IA) et en restant sur zhs.cloud pour le VPN sur votre ordinateur portable. Le forfait de données de la carte SIM (carte de Macao à 150 CNY/mois pour 20GB plus des extras) semble être une bonne solution de contournement mobile pour bypasser les restrictions du GFW sans la surcharge constante des applications.

Vos observations sur la carte SIM de Macao étant la plus rapide pour les sites bannis par le GFW sont logiques—l'IP cellulaire directe de Macao contourne souvent mieux les blocages géopolitiques que les options de Hong Kong ou de la Chine continentale, surtout pour des services comme ChatGPT ou Claude qui ont des restrictions régionales. Router des activateurs spécifiques (par exemple, ChatGPT vers des proxies USA) dans Shadowrocket est un ajustement astucieux, mais effectivement, le délai du proxy global sur chaque requête réseau est un point faible commun sur iOS. Shadowrocket (ou Surge) peut devenir lent s'il intercepte trop de trafic, entraînant une latence plus élevée sur des apps comme Twitter/X même si elles ne sont pas complètement bloquées.

Voici quelques retours et suggestions basés sur vos notes—en se concentrant sur les optimisations tout en restant pratique :

### Optimisations Shadowrocket
- **Affinement des Règles pour Moins de Délai** : Au lieu d'une configuration proxy généralisée, essayez de resserrer vos règles pour minimiser l'interception. Par exemple, utilisez le flux suivant dans la config de Shadowrocket :
  - **DIRECT** : Par défaut pour le trafic local/régional (ex: WeChat, Baidu).
  - **Proxy/Reject** : Liste blanche uniquement des domaines prioritaires bannis par le GFW (ex : autoriser ChatGPT, Claude, Google, et quelques autres à transiter par les proxies USA).
  - Exemple de règles (dans un fichier `.conf`) :
    ```
    [Rule]
    DOMAIN-KEYWORD,chatgpt.com,PROXY
    DOMAIN-KEYWORD,claude.ai,PROXY
    DOMAIN-KEYWORD,google.com,PROXY
    DOMAIN-KEYWORD,twitter.com,PROXY  # Seulement si ChatGPT/etc. en dépendent
    MATCH,DIRECT  # Règle fourre-tout pour diriger le trafic non bloqué hors du proxy
    ```
    De cette façon, seuls certains sites/apps passent par la chaîne de proxies USA, réduisant le délai global. Vous pouvez générer ou éditer ces règles dans Clash ou des gestionnaires comme Stash ou Quantumult X pour une personnalisation plus facile.
- **Tester la Latence** : Après avoir ajouté les règles, effectuez des tests de vitesse (par ex. via Fast.com ou Ookla) avec Shadowrocket activé/désactivé. Si les délais persistent, envisagez de réduire la longueur de la chaîne de proxy—un saut (ex: un proxy dépendant des USA) pourrait suffire par rapport aux configurations multi-niveaux.

### Outils Alternatifs pour un Accès iOS Plus Simple
Si la surcharge de Shadowrocket est trop importante (surtout puisque vous avez mentionné l'avoir abandonné après un jour), voici des options à faible friction qui reflètent votre utilisation directe de la carte SIM de Macao :
- **Apps VPN avec Règles à la Demande** : Quelque chose comme ExpressVPN ou NordVPN a des fonctionnalités iOS pour le routage spécifique aux applications (activer le VPN seulement pour ChatGPT, Mistral, etc.), sans tout proxyfier. Cela s'intègre parfaitement avec les données cellulaires.
- **Clash pour iOS (via des Apps comme Surge ou Stash)** : Si vous aimez la logique de votre script Python sur desktop, portez une configuration Clash simplifiée sur iOS. Utilisez un ensemble de règles qui commence par "DIRECT" et ne proxyfie que certains domaines—moins de délai qu'un proxy complet, et vous pouvez prioriser les IP de Singapour/Macao si votre fournisseur le supporte.
- **Proxies Cellulaires Directs via la SIM** : Puisque vous misez sur la carte SIM de Macao pour Mistral et Grok, c'est intelligent pour la vitesse pure. Si vous avez besoin des outils d'IA sur mobile, vérifiez si Mistral/Grok ont des IP compatibles avec Macao ou essayez d'y accéder via les modes navigation privée pour éviter entièrement le routage basé sur l'application.

### Conseils Plus Généraux
- **Batterie/Latence sur iOS** : Une utilisation prolongée du proxy peut vider la batterie plus vite. Surveillez avec les outils intégrés, et envisagez des basculements programmés (ex: proxy seulement pendant les heures de pointe).
- **Stabilité du Fournisseur** : zhs.cloud semble fiable pour vos besoins VPN—restez-y pour l'ordinateur portable, mais vérifiez aussi les apps VPN pour iOS si vous étendez. Pour la SIM, les opérateurs de Macao comme CTM sont solides, mais attention aux plafonds de données.
- **Viabilité à Long Terme** : J'apprécie la prudence pour quand vous quitterez la Chine—combinez cela avec une eSIM globale ou un forfait roaming en backup. Gardez un œil sur les changements de politiques, car les outils d'accès peuvent être éphémères.

Si vous rencontrez des problèmes de configuration spécifiques (ex: partager votre fichier de règles Shadowrocket) ou souhaitez des ajustements de script pour Clash, n'hésitez pas à donner plus de détails—je peux aider à dépanner sans compliquer les choses. Restez en sécurité là-bas ! 🚀