---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Prise en main d'AWS Lambda
translated: true
type: note
---

### Premiers pas avec AWS Lambda

AWS Lambda est un service de calcul serverless qui exécute votre code en réponse à des événements sans que vous ayez à gérer des serveurs. Voici un guide étape par étape, adapté aux débutants, pour créer, déployer et utiliser votre première fonction Lambda. Ce guide est basé sur la documentation officielle d'AWS.

#### Prérequis
- Un compte AWS actif. Inscrivez-vous sur [aws.amazon.com](https://aws.amazon.com/) si vous n'en avez pas.
- Une familiarité de base avec un langage de programmation comme Node.js ou Python (Lambda prend en charge de nombreux environnements d'exécution).

#### Étape 1 : Créer une fonction Lambda
1. Connectez-vous à la console de gestion AWS et accédez au service Lambda (recherchez "Lambda" dans le menu des services).
2. Sur la page Fonctions, cliquez sur **Créer une fonction**.
3. Choisissez **Créer à partir de zéro**.
4. Entrez un **Nom de fonction** (par exemple, `ma-premiere-fonction`).
5. Sélectionnez un **Environnement d'exécution** (par exemple, Node.js 22.x ou Python 3.13).
6. Laissez l'architecture par défaut (x86_64) et cliquez sur **Créer une fonction**.

Cela crée automatiquement un rôle d'exécution (un rôle IAM) avec des autorisations de base, comme l'écriture de journaux dans Amazon CloudWatch.

#### Étape 2 : Écrire votre code
Dans l'éditeur de code de la console Lambda (sous l'onglet **Code**), remplacez le code "Hello World" par défaut par quelque chose de simple. Voici un exemple qui calcule l'aire d'un rectangle à partir d'une entrée JSON avec les clés `length` et `width`.

- **Exemple Node.js** :
  ```javascript
  exports.handler = async (event) => {
    const length = event.length;
    const width = event.width;
    const area = length * width;
    console.log(`The area is ${area}`);
    console.log('Log group: /aws/lambda/' + process.env.AWS_LAMBDA_FUNCTION_NAME);
    return { area: area };
  };
  ```

- **Exemple Python** :
  ```python
  import json

  def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = length * width
    print(f"The area is {area}")
    print(f"Log group: /aws/lambda/{context.function_name}")
    return {
        'statusCode': 200,
        'body': json.dumps({'area': area})
    }
  ```

Enregistrez les modifications — le déploiement se fait automatiquement pour les langages interprétés.

Pour les langages compilés (par exemple, Java), créez un package de déploiement localement et téléchargez-le via la console ou AWS CLI.

#### Étape 3 : Tester votre fonction
1. Dans l'onglet **Test**, cliquez sur **Créer un nouvel événement de test**.
2. Nommez-le (par exemple, `test-calcul-aire`).
3. Collez un exemple d'entrée JSON :
   ```json
   {
     "length": 6,
     "width": 7
   }
   ```
4. Enregistrez et cliquez sur **Test**.

Consultez les résultats dans la section **Résultats de l'exécution** (par exemple, `{"area": 42}`). Vérifiez les journaux dans CloudWatch pour des détails comme la durée et l'utilisation de la mémoire.

#### Étape 4 : Invoquer et surveiller
- **Invocation manuelle** : Utilisez le bouton Test de la console ou AWS CLI : `aws lambda invoke --function-name ma-premiere-fonction output.json`.
- **Invocation par événement** : Connectez des déclencheurs comme API Gateway, les compartiments S3 ou les flux DynamoDB. Allez dans l'onglet **Configuration** > **Déclencheurs** pour les ajouter.
- **Journaux** : Envoyés automatiquement à CloudWatch Logs. Consultez-les sur [console.aws.amazon.com/cloudwatch/home#logsV2:log-groups](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) sous `/aws/lambda/votre-nom-de-fonction`.

Concepts clés :
- **Sources d'événements/Déclencheurs** : Services (par exemple, un téléchargement S3) qui invoquent votre fonction avec des données d'événement (charge utile JSON).
- **Gestionnaire (Handler)** : Le point d'entrée (par exemple, `index.handler` pour Node.js) qui traite l'événement.

#### Étape 5 : Nettoyer (Facultatif)
Supprimez la fonction via la console : Actions > Supprimer. Supprimez également les journaux et les rôles IAM associés pour éviter des frais.

#### Conseils
- Commencez avec le niveau gratuit (1 million de requêtes/mois).
- Utilisez AWS SAM ou Serverless Framework pour les déploiements avancés.
- Pour la production, configurez les variables d'environnement, les couches (layers) et les paramètres VPC dans l'onglet **Configuration**.

[Créez votre première fonction Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)