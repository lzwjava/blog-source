---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: API Rentable de Markdown a PDF
translated: true
type: note
---

### Opción Barata Recomendada: Google Cloud Run

Para una API simple basada en Java que convierta Markdown a PDF (por ejemplo, usando una librería como Flying Saucer o iText), con solo ~100 peticiones por semana para uso personal de un blog, **Google Cloud Run** es la opción más rentable. Es una plataforma serverless que ejecuta aplicaciones en contenedores, escala a cero cuando está inactiva y solo cobra por el uso real. No es necesario gestionar máquinas virtuales ni preocuparse por costos de ejecución continua, perfecto para escenarios de bajo tráfico como el tuyo.

#### ¿Por qué Cloud Run sobre Otras Opciones?
- **Frente a Compute Engine (Máquinas Virtuales)**: Las máquinas virtuales tienen costos fijos por hora incluso cuando están inactivas, lo cual sería excesivo y más caro (~$5–10/mes mínimo para una instancia pequeña).
- **Frente a App Engine**: Beneficios serverless similares, pero Cloud Run es más flexible para contenedores Java y a menudo más barato para uso esporádico.
- Tu carga de trabajo encaja completamente dentro del nivel gratuito, así que en la práctica espera **$0/mes**.

#### Costos Estimados
Con 100 peticiones/semana (~400/mes):
- Supongamos que cada petición usa 1 vCPU y 0.5 GiB de memoria durante 10 segundos (una estimación conservadora para una conversión rápida de Markdown a PDF).
- Uso total: ~4,000 segundos-vCPU y ~2,000 segundos-GiB/mes.
- **El nivel gratuito lo cubre todo**: 180,000 segundos-vCPU, 360,000 segundos-GiB y 2 millones de peticiones por mes (en la mayoría de las regiones).
- Si lo excedes (poco probable), las tarifas de pago son ~$0.000024/segundo-vCPU + $0.0000025/segundo-GiB + $0.40/millón de peticiones después de los límites gratuitos—aún así sería menos de $0.10/mes.

No hay tarifas de salida de datos (egress) para tu caso de uso (las llamadas internas a la API dentro de la misma región son gratuitas).

#### Región Recomendada: us-central1 (Iowa)
- Esta es la región de Nivel 1 más barata para Cloud Run, con las tarifas más bajas para cómputo y sin recargo por latencia en Norteamérica.
- Los precios son similares en todas las regiones de Nivel 1 (EE. UU./Europa), pero us-central1 tiene una ligera ventaja en los costos promedio de instancia.
- Si estás fuera de Norteamérica (por ejemplo, Europa o Asia), cambia a la región de Nivel 1 más cercana, como europe-west1 (Bélgica), para una mejor latencia—los costos difieren en menos del 10%.
- Evita las regiones de Nivel 2 (por ejemplo, asia-southeast1), ya que son entre un 20 y 50% más caras.

#### Guía Rápida de Configuración para Tu Servidor Java
1. **Construye tu aplicación**: Usa Spring Boot para una API REST simple. Ejemplo de endpoint: POST `/convert` con el cuerpo en Markdown, devuelve PDF.
   - Añade la dependencia: `implementation 'org.xhtmlrenderer:flying-saucer-pdf:9.1.22'` (o similar).
   - Fragmento de código de ejemplo:
     ```java:disable-run
     @RestController
     public class MarkdownController {
         @PostMapping("/convert")
         public ResponseEntity<byte[]> convert(@RequestBody String markdown) {
             // Lógica de conversión aquí (ej., markdown a HTML, luego a PDF)
             byte[] pdfBytes = // tu resultado de la conversión;
             return ResponseEntity.ok()
                 .header("Content-Type", "application/pdf")
                 .body(pdfBytes);
         }
     }
     ```
2. **Empaqueta en contenedor**: Crea un `Dockerfile`:
   ```
   FROM openjdk:17-jdk-slim
   COPY target/your-app.jar app.jar
   ENTRYPOINT ["java", "-jar", "/app.jar"]
   ```
   Construye: `docker build -t gcr.io/your-project/markdown-api .`
3. **Despliega en Cloud Run**:
   - Habilita la API de Cloud Run en la consola de GCP.
   - `gcloud run deploy markdown-api --image gcr.io/your-project/markdown-api --platform managed --region us-central1 --allow-unauthenticated --memory 512Mi --cpu 1 --max-instances 1`
   - Obtén la URL: `https://markdown-api-abc.run.app/convert`
4. **Prueba**: Envía una petición POST con Markdown; escalará automáticamente.

Regístrate para la prueba gratuita de $300 si eres nuevo en GCP. Monitorea los costos en el panel de Facturación.

[Precios de Cloud Run](https://cloud.google.com/run/pricing)  
[Guía de Regiones de GCP](https://www.cloudzero.com/blog/gcp-regions/)  
[Inicio Rápido de Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)