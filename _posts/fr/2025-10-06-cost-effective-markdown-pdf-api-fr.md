---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: API Économique de Conversion de Markdown en PDF
translated: true
type: note
---

### Option Économique Recommandée : Google Cloud Run

Pour une API Java simple qui convertit Markdown en PDF (par exemple, en utilisant une bibliothèque comme Flying Saucer ou iText), avec seulement ~100 requêtes par semaine pour un usage de blog personnel, **Google Cloud Run** est le choix le plus économique. C'est une plateforme serverless qui exécute des applications conteneurisées, qui peut passer à zéro instance lorsqu'elle est inactive, et qui ne facture que l'utilisation réelle. Aucune gestion de VM ni de souci de coûts pour une instance toujours allumée—parfait pour des scénarios à faible trafic comme le vôtre.

#### Pourquoi Cloud Run Plutôt que les Autres Options ?
- **Vs. Compute Engine (VMs)** : Les VM ont des coûts horaires fixes même lorsqu'elles sont inactives, ce qui serait excessif et plus coûteux (~5–10 $/mois minimum pour une petite instance).
- **Vs. App Engine** : Bénéfices serverless similaires, mais Cloud Run est plus flexible pour les conteneurs Java et souvent moins cher pour une utilisation sporadique.
- Votre charge de travail entre entièrement dans le niveau gratuit, donc attendez-vous à **0 $/mois** en pratique.

#### Coûts Estimés
Avec 100 requêtes/semaine (~400/mois) :
- Supposez que chaque requête utilise 1 vCPU et 0,5 Gio de mémoire pendant 10 secondes (estimation prudente pour une conversion rapide Markdown-vers-PDF).
- Utilisation totale : ~4 000 secondes-vCPU et ~2 000 secondes-Gio/mois.
- **Le niveau gratuit couvre tout** : 180 000 secondes-vCPU, 360 000 secondes-Gio et 2 millions de requêtes par mois (dans la plupart des régions).
- Si vous dépassez (peu probable), les tarifs payants sont ~0,000024 $/seconde-vCPU + 0,0000025 $/seconde-Gio + 0,40 $/million de requêtes après les limites gratuites—toujours moins de 0,10 $/mois.

Aucuns frais d'egress pour votre cas d'usage (les appels d'API internes restent gratuits dans la même région).

#### Région Recommandée : us-central1 (Iowa)
- C'est la région de Niveau 1 la moins chère pour Cloud Run, avec les tarifs de calcul les plus bas et aucune majoration pour la latence en Amérique du Nord.
- La tarification est similaire dans toutes les régions de Niveau 1 (États-Unis/Europe), mais us-central1 est en moyenne légèrement meilleure sur les coûts d'instance.
- Si vous êtes hors Amérique du Nord (par exemple, en Europe ou en Asie), choisissez la région de Niveau 1 la plus proche comme europe-west1 (Belgique) pour une meilleure latence—la différence de coût est inférieure à 10 %.
- Évitez les régions de Niveau 2 (par exemple, asia-southeast1) car elles sont 20 à 50 % plus chères.

#### Guide de Configuration Rapide pour Votre Serveur Java
1.  **Construisez votre application** : Utilisez Spring Boot pour une API REST simple. Exemple de point de terminaison : POST `/convert` avec un corps Markdown, retourne un PDF.
    - Ajoutez la dépendance : `implementation 'org.xhtmlrenderer:flying-saucer-pdf:9.1.22'` (ou similaire).
    - Exemple de snippet de code :
      ```java:disable-run
      @RestController
      public class MarkdownController {
          @PostMapping("/convert")
          public ResponseEntity<byte[]> convert(@RequestBody String markdown) {
              // Logique de conversion ici (par exemple, markdown vers HTML, puis vers PDF)
              byte[] pdfBytes = // votre résultat de conversion;
              return ResponseEntity.ok()
                  .header("Content-Type", "application/pdf")
                  .body(pdfBytes);
          }
      }
      ```
2.  **Conteneurisez** : Créez un `Dockerfile` :
    ```
    FROM openjdk:17-jdk-slim
    COPY target/your-app.jar app.jar
    ENTRYPOINT ["java", "-jar", "/app.jar"]
    ```
    Construction : `docker build -t gcr.io/your-project/markdown-api .`
3.  **Déployez sur Cloud Run** :
    - Activez l'API Cloud Run dans la Console GCP.
    - `gcloud run deploy markdown-api --image gcr.io/your-project/markdown-api --platform managed --region us-central1 --allow-unauthenticated --memory 512Mi --cpu 1 --max-instances 1`
    - Obtenez l'URL : `https://markdown-api-abc.run.app/convert`
4.  **Testez** : Envoyez une requête POST avec du Markdown ; l'application scale automatiquement.

Inscrivez-vous à l'essai gratuit de 300 $ si vous êtes nouveau sur GCP. Surveillez les coûts dans le tableau de bord de facturation.

[Tarification Cloud Run](https://cloud.google.com/run/pricing)
[Guide des Régions GCP](https://www.cloudzero.com/blog/gcp-regions/)
[Démarrage Rapide Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)