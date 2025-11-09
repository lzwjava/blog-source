---
audio: false
generated: true
image: false
lang: es
layout: post
model: deepseek/deepseek-v3.2-exp
title: Celda de Tabla de Conversación de Chat Personalizada
translated: true
type: note
---

Esta es una implementación en Objective-C de una celda de tabla personalizada para mostrar elementos de conversación en una aplicación de chat (como iMessage o WhatsApp). Permíteme desglosar los componentes clave:

## Descripción general
La clase `LZConversationCell` crea una celda personalizada que muestra:
- Avatar/imagen del usuario
- Nombre del contacto
- Vista previa del último mensaje
- Marca de tiempo
- Indicadores de insignia para mensajes no leídos

## Componentes clave

### 1. Constantes de diseño
```objc
static CGFloat kLZImageSize = 45;           // Tamaño del avatar
static CGFloat kLZVerticalSpacing = 8;      // Relleno vertical
static CGFloat kLZHorizontalSpacing = 10;   // Relleno horizontal
static CGFloat kLZTimestampeLabelWidth = 100; // Ancho para la marca de tiempo
```

### 2. Elementos de UI
- **`avatarImageView`**: Foto de perfil del usuario (45x45 puntos)
- **`nameLabel`**: Visualización del nombre del contacto
- **`messageTextLabel`**: Vista previa del último mensaje
- **`timestampLabel`**: Hora/fecha del mensaje
- **`litteBadgeView`**: Pequeño punto rojo para mensajes nuevos
- **`badgeView`**: Insignia numérica para el conteo de no leídos

### 3. Métodos de gestión de celdas
- **`+dequeueOrCreateCellByTableView:`**: Patrón estándar de reutilización de celdas de tabla
- **`+registerCellToTableView:`**: Registra la clase de celda con la tabla
- **`+heightOfCell`**: Cálculo de altura fija (61 puntos)

### 4. Configuración del diseño
El método `setup`:
- Calcula las alturas de las etiquetas basándose en proporciones
- Crea y posiciona todas las subvistas
- Utiliza diseño basado en frames (sin Auto Layout)

### 5. Cálculos de frames
Cada subvista se posiciona en relación con las demás:
- Avatar a la izquierda con espaciado fijo
- Etiquetas de nombre y mensaje a la derecha del avatar
- Marca de tiempo alineada al borde derecho
- Vistas de insignia posicionadas sobre el avatar

### 6. Gestión de memoria
- **`prepareForReuse`**: Limpia todo el contenido cuando la celda se recicla
- Inicialización diferida para todas las subvistas (creadas solo cuando se necesitan)

## Patrón de uso
Esta celda se usaría en una vista de tabla de lista de conversaciones para mostrar cada conversación de chat con:
- Información del contacto
- Vista previa del mensaje
- Indicadores de estado leído/no leído
- Marca de tiempo del último mensaje

La celda sigue los patrones de diseño de iOS y proporciona indicadores visuales comunes en aplicaciones de mensajería.