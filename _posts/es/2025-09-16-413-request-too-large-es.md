---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-oss-120b
title: Resolución de Errores 413 Solicitud Demasiado Grande
translated: true
type: note
---

## Qué significa el error  

- **413 Request Too Large** es un código de estado HTTP que indica que el servidor rechazó procesar la solicitud porque la carga útil excede el tamaño permitido. En el contexto del servicio de inferencia de OpenAI, la "carga útil" es el número total de tokens (entrada + salida) enviados en una sola solicitud. [1]  

- **Límite de tokens por minuto (TPM)**: El modelo `openai/gpt‑oss‑120b` está configurado con un máximo de **8,000 TPM** para el nivel de servicio bajo demanda. La solicitud que enviaste contenía **13,701 tokens**, que son **5,701 tokens por encima del límite**. [1]  

- **Por qué ocurre**:  
  1. **Prompt grande** – el texto de entrada (incluyendo instrucciones del sistema, mensajes del usuario y cualquier dato anexado) puede ser muy extenso.  
  2. **Configuración alta de `max_tokens`** – si la solicitud le pide al modelo que genere una respuesta larga, el número proyectado de tokens de salida se suma al de entrada.  
  3. **Llamadas sucesivas rápidas** – si se realizan muchas solicitudes en rápida sucesión, los tokens acumulados en el minuto actual pueden exceder la cuota de TPM, incluso si cada solicitud individual está por debajo del límite.  

## Cómo resolverlo  

| Opción | Qué hacer | Efecto |
|--------|------------|--------|
| **Recortar el prompt** | Eliminar texto innecesario, usar instrucciones concisas o comprimir datos (ej., resumir bloques grandes antes de enviarlos). | Reduce el recuento de tokens de entrada. |
| **Reducir `max_tokens`** | Solicitar una respuesta más corta (ej., establecer `max_tokens` en 500 en lugar de 2000). | Disminuye el recuento proyectado de tokens de salida. |
| **Dividir la solicitud** | Separar un documento muy grande en múltiples fragmentos más pequeños y llamar al modelo secuencialmente, uniendo los resultados después. | Mantiene cada llamada por debajo del límite de TPM. |
| **Mejorar el nivel** | Cambiar a un nivel de mayor capacidad (ej., Dev Tier) donde el límite de TPM es más grande o ilimitado. | Permite cargas útiles de solicitud individual más grandes sin error. |
| **Limitar las llamadas** | Añadir un breve retraso entre solicitudes o implementar limitación de tasa para mantener el total de tokens por minuto ≤ 8,000. | Previene el desbordamiento acumulativo de TPM. |

## Lista de verificación rápida antes de enviar una solicitud  

1. **Contar tokens** – usar la herramienta tokenizadora de OpenAI (o `tiktoken`) para estimar el total de tokens (prompt + max tokens).  
2. **Mantenerse ≤ 8,000 TPM** para el nivel bajo demanda.  
3. **Si está cerca del límite**, considerar uno de los pasos de mitigación anteriores.  

Al asegurarse de que la solicitud se mantenga dentro de la cuota de 8,000 tokens por minuto, se evitará el error 413 "Request Too Large". [1]

Citas:
[1] https://www.reddit.com/r/OpenAI/comments/1nbtl2p/wow_weve_been_burning_money_for_6_months/