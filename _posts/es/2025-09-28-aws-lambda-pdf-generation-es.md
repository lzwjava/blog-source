---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-sonnet-4
title: AWS Lambda para la Generación de PDF
translated: true
type: note
---

¡Sí, AWS Lambda (o funciones serverless similares) es perfecto para tu caso de uso! Este es exactamente el escenario para el que fue diseñado el cómputo serverless: cargas de trabajo esporádicas e infrecuentes donde no quieres tener infraestructura inactiva.

Aquí te explico por qué Lambda tiene sentido para tu generación de PDFs:

**Beneficios de Costo:**
- Solo pagas cuando la función se ejecuta (por solicitud + tiempo de ejecución)
- Sin cargos cuando está inactiva - crucial para tu uso de 1-2 veces por día
- El nivel gratuito de Lambda incluye 1 millón de solicitudes/mes y 400,000 GB-segundos
- Para cientos de usuarios con bajo uso de PDFs, es probable que te mantengas dentro del nivel gratuito

**Enfoque Técnico:**
```
Blog → API Gateway → Función Lambda → Generación de PDF → Almacenamiento S3 → Retornar URL
```

**Opciones de Arquitectura:**

1. **Lambda Simple + Puppeteer/Playwright:**
   - Función Lambda con navegador headless para convertir HTML a PDF
   - Bueno para contenido de blog con estilos
   - Arranque en frío ~2-3 segundos, pero aceptable para tu uso

2. **Lambda + librerías PDF:**
   - Usa librerías como jsPDF, PDFKit o wkhtmltopdf
   - Ejecución más rápida, tamaño de paquete más pequeño
   - Mejor para contenido principalmente textual

3. **Enfoque híbrido:**
   - Lambda genera el PDF y lo almacena en S3
   - CloudFront para la distribución de PDFs
   - Opcional: SQS si quieres procesamiento asíncrono

**Opciones Serverless Alternativas:**
- **Vercel Functions** - si tu blog está en Vercel
- **Netlify Functions** - concepto similar
- **Google Cloud Functions** - precios comparables
- **Railway/Render** - contenedores serverless

Para tu escala (cientos de usuarios, 1-2 solicitudes de PDF/día), Lambda te costaría prácticamente nada mientras elimina por completo el mantenimiento del servidor. Mucho mejor que mantener un servidor ejecutándose 24/7 para una generación ocasional de PDFs.

¿Te gustaría que profundice en algún enfoque de implementación específico?