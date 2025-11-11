---
audio: false
generated: true
lang: es
layout: post
title: Desencadena tu flujo de trabajo de GitHub
translated: true
type: note
---

Tienes razón, incrustar directamente un token de GitHub en tu código frontend es un riesgo de seguridad. Cualquier persona que vea el código fuente de tu página podría acceder y hacer un uso indebido de tu token.

Aquí tienes un desglose de enfoques seguros que puedes tomar para activar tu workflow de GitHub desde un botón en el frontend, junto con explicaciones y ejemplos de código:

**Idea Central: Introducir un Backend Seguro**

La forma más segura de manejar esto es introducir un componente backend (un endpoint de API) que:

1.  **Reciba la solicitud de activación desde tu frontend.**
2.  **Almacene de forma segura y use tu token de GitHub.**
3.  **Realice la llamada autenticada a la API de GitHub para despachar tu workflow.**

De esta manera, tu token sensible de GitHub nunca abandona tu entorno del lado del servidor.

Aquí tienes algunas opciones para tu backend:

**1. Funciones Serverless (por ejemplo, AWS Lambda, Google Cloud Functions, Netlify Functions, Vercel Functions)**

Esta es a menudo una solución ligera y rentable para endpoints de API simples como este.

*   **Cómo funciona:** Escribes una pequeña función que se despliega en una plataforma serverless. Esta función contend