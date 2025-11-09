---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Rendimiento de Black Myth Wukong para PC
translated: true
type: note
---

### Black Myth: Wukong en tu Configuración de PC

Tu PC es una bestia absoluta: el i9-13900KF, la RTX 4070, 64 GB de RAM DDR5 y el almacenamiento NVMe rápido significan que aplastarás este juego en 4K con configuración ultra y trazado de rayos habilitado, alcanzando fácilmente más de 60 FPS. No hay cuellos de botella aquí; está muy por encima de los requisitos recomendados (que piden una RTX 2060 y un i7-9700). El coste total del equipo (~14.000 CNY) es una buena relación calidad-precio para un equipo de gama alta como este.

Black Myth: Wukong es un juego de acción RPG para un jugador inspirado en *Viaje al Oeste*, donde encarnas al Elegido (un guerrero mono) que lucha contra jefes míticos en la antigua China. Su combate es al estilo souls (esquiva, parada, gestión de aguante) pero más accesible, con combos fluidos, transformaciones y mejoras de hechizos. Espera entre 30 y 40 horas para la historia principal, más la exploración y el NG+.

#### ¿Necesitas Windows? (Respuesta Corta: No)
- **Steam en Ubuntu 22.04**: Steam funciona de forma nativa en Linux. Si aún no lo tienes instalado:
  1. Abre una terminal y ejecuta: `sudo apt update && sudo apt install steam`.
  2. Inicia Steam, inicia sesión y deja que descargue las actualizaciones.
- **Compatibilidad del Juego**: Black Myth: Wukong no tiene versión nativa para Linux (solo está para Windows), pero se ejecuta *a la perfección* en Linux mediante Proton (la capa de compatibilidad de Valve integrada en Steam). Tiene una calificación **Platino** en ProtonDB, lo que significa un rendimiento "perfecto" listo para usar: no se necesitan ajustes importantes. Los usuarios reportan mejores tasas de fotogramas y estabilidad en Linux que en Windows en algunos casos, gracias a las versiones optimizadas de Proton.
- **Posibles Problemas**:
  - Utiliza DRM Denuvo, que podría marcar los cambios de versión de Proton como "nuevas instalaciones" (limitando las activaciones). Mantente en una versión de Proton para evitarlo.
  - ¿Bloqueos raros al iniciar? Fuerza el uso de Proton Experimental en Steam (clic derecho en el juego > Propiedades > Compatibilidad > marcar "Forzar el uso de una herramienta de compatibilidad de Steam Play concreta" > seleccionar Proton Experimental).
- **Prueba de Rendimiento**: Antes de comprar, descarga la herramienta de evaluación gratuita Black Myth: Wukong Benchmark Tool desde Steam: funciona muy bien con Proton y te permite someter tu configuración a una prueba de estrés.
- Conclusión: Quédate en Ubuntu. Hacer un arranque dual con Windows es excesivo a menos que juegues a otros juegos multijugador con mucho anti-cheat (este es para un jugador, así que no hay problema).

Si *realmente* quieres Windows para una optimización máxima (por ejemplo, un 5-10% mejor rendimiento en casos muy específicos), es fácil hacer un arranque dual, pero no es necesario aquí.

#### Cómo Conseguirlo y Jugarlo
1. **Compra e Instalación**:
   - Busca "Black Myth: Wukong" en Steam (ID de la aplicación: 2358720). Cuesta ~$60 USD / ~430 CNY, y a menudo está en oferta.
   - Tamaño de instalación: ~130 GB, así que tu SSD de 1 TB es más que suficiente (usa el HDD para desbordamiento si es necesario).
   - En Steam: Clic derecho en el juego > Propiedades > Compatibilidad > Habilitar Steam Play para todos los títulos > Seleccionar Proton Experimental.

2. **Controles (Por Defecto Teclado/Ratón)**:
   - Usa tu ratón y teclado actuales: es receptivo, pero un mando (Xbox/PS) se siente más natural para los combos.
   - **Movimiento**: WASD para moverte, Espacio para esquivar/saltar, Mayús para correr.
   - **Combate**: Clic izquierdo (ataque ligero), Clic derecho (ataque pesado), R (parada: ¡el momento es clave!), Q/E (hechizos), F (inmovilizar enemigos para remates).
   - **Aguante**: Los ataques y esquivados consumen una barra azul: gestiónala como en Dark Souls.
   - **Mejoras**: Recoge Voluntad (equivalente a las almas) para subir de nivel las habilidades en los santuarios. Enfócate en bastones, transformaciones (por ejemplo, conviértete en un pájaro para ataques aéreos) y reliquias.
   - Reasigna las teclas en Configuración > Controles si es necesario.

3. **Consejos Rápidos para Empezar con Fuerza**:
   - **Principios del Juego**: Prioriza esquivar sobre bloquear: las paradas vendrán después. Explora para encontrar vasijas ocultas (suelen soltar botín).
   - **Jefes**: Aprende sus patrones; usa pilares para cubrirte. Las Chispas (mejoras) están ocultas: busca en zonas altas y bajas.
   - **Rendimiento**: En el juego, establece el ajuste preestablecido en Muy Alto, DLSS en Calidad (tu 4070 brilla aquí) y limita los FPS a 60 para mayor fluidez.
   - **Audio/Subtítulos**: el doblaje en inglés es sólido, pero el chino con subtítulos captura mejor la vibra del mito.
   - Guarda a menudo en los Santuarios del Guardián (puntos de control).

Si encuentras problemas (por ejemplo, con la configuración del mando), Lutris o Heroic Launcher son alternativas, pero Steam Proton es lo más simple. ¡Disfruta de las batallas épicas: es uno de los mejores juegos de 2024!

#### Referencias
- [Black Myth: Wukong en Steam](https://store.steampowered.com/app/2358720/Black_Myth_Wukong/)
- [ProtonDB: Black Myth: Wukong](https://www.protondb.com/app/2358720)
- [Reddit: Evaluación de Wukong en Proton](https://www.reddit.com/r/linux_gaming/comments/1er0biq/black_myth_wukong_has_a_free_benchmark_and_it/)
- [SteamDB: Detalles de la Aplicación](https://steamdb.info/app/2358720/)