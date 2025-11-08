---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Programa del Curso de Desarrollo de Aplicaciones Móviles
translated: true
type: note
---

### Contenido del Curso: 14567 Tecnología de Desarrollo de Aplicaciones Móviles

**Información del Curso**
- **Código del Curso**: 14567
- **Nombre del Curso**: Tecnología de Desarrollo de Aplicaciones Móviles (移动应用开发技术)
- **Créditos**: 4
- **Nivel**: Especialista (专科)
- **Campo Profesional**: Tecnología de Aplicaciones Informáticas (计算机应用技术)
- **Tipo de Examen**: Escrito (笔试); Nota: Existe un examen práctico por separado bajo el código 14568 (1 crédito).
- **Autoridad Examinadora**: Examen de Autoevaluación de Educación Superior de la Provincia de Guangdong (广东省高等教育自学考试)
- **Libro de Texto**: *Android Mobile Development Basic Case Tutorial (2nd Edition)* por Heima Programmer (黑马程序员), People's Posts and Telecommunications Press (人民邮电出版社), ISBN: 9787115567680 (2022). El contenido del curso se alinea estrechamente con la estructura de este libro de texto, enfatizando el desarrollo para Android como ejemplo central para la programación de aplicaciones móviles.
- **Naturaleza y Objetivos del Curso**: Este es un curso práctico y orientado a la aplicación para las especialidades de ingeniería de software y tecnología de aplicaciones informáticas, centrado en las necesidades del mercado laboral. Enseña desarrollo de aplicaciones móviles utilizando Android como plataforma principal. Los estudiantes dominarán los fundamentos de Android y aprenderán a desarrollar aplicaciones móviles, combinando teoría con programación práctica. Se hace hincapié en construir un entorno de desarrollo, implementar interfaces de usuario (UI), manejo de datos y funciones avanzadas como redes y multimedia. Los estudiantes de autoevaluación deben combinar el estudio teórico con experimentos, utilizando herramientas como Android Studio para depuración y pruebas.

**Objetivos de Evaluación**:
Los exámenes evalúan el conocimiento integral del desarrollo para Android, incluyendo la implementación de código, resolución de problemas y diseño de aplicaciones. El enfoque está en comprender la sintaxis, la arquitectura y los escenarios prácticos. Los exámenes teóricos cubren temas amplios de manera sistemática; la práctica enfatiza habilidades clave (ej. a través del examen separado 14568). Se recomienda usar mapas mentales para la integración del conocimiento y ejercicios prácticos para la retención.

**Contenido del Curso y Requisitos de Evaluación**
El contenido está estructurado en torno a 12 capítulos, progresando desde lo básico hasta temas avanzados y un proyecto final. Cada capítulo incluye teoría, ejemplos de código, ejercicios prácticos y evaluaciones sobre conceptos clave (ej. identificación, aplicación, análisis). A continuación, el esquema jerárquico:

1.  **Introducción a los Fundamentos de Android**
    - Visión general de Android (tecnología de comunicación, historia, arquitectura, Dalvik VM).
    - Configuración del entorno de desarrollo (instalación de Android Studio, emulador, SDK).
    - Desarrollo y estructura del primer programa.
    - Gestión de recursos (imágenes, temas/estilos, diseños, cadenas de texto, colores, dimensiones).
    - Depuración (pruebas unitarias, Logcat).
    *Requisitos*: Comprender el ecosistema de Android; construir/ejecutar aplicaciones simples.

2.  **Diseños de Interfaz Comunes en Android**
    - Fundamentos de View y escritura de diseños (XML vs. código Java).
    - Atributos comunes.
    - LinearLayout (ej. interfaz de juego de emparejamiento de animales).
    - RelativeLayout (ej. interfaz de reproductor de música).
    - TableLayout (ej. interfaz de calculadora).
    - FrameLayout (ej. interfaz de luz de neón).
    *Requisitos*: Diseñar interfaces de usuario (UI) responsivas; aplicar diseños en proyectos.

3.  **Controles de Interfaz Comunes en Android**
    - Controles simples (TextView, EditText, Button, ImageView, RadioButton, CheckBox, Toast).
    - Controles de lista (ListView con adaptadores, RecyclerView; ej. centro comercial, feed de noticias).
    - Vistas personalizadas (Custom Views).
    *Requisitos*: Implementar elementos interactivos; manejar enlace de datos (data binding).

4.  **Unidad de Actividad del Programa: Activity**
    - Ciclo de vida (estados, métodos).
    - Creación, configuración, inicio/cierre.
    - Intent e IntentFilter.
    - Saltos entre Activities y paso/retorno de datos (ej. juego del mono recogiendo melocotones).
    - Pilas de tareas (Task stacks) y modos de lanzamiento (launch modes).
    - Uso de Fragmentos (Fragment) (ciclo de vida, creación, integración; ej. menú de Meituan).
    *Requisitos*: Gestionar el flujo de la aplicación; manejar fragmentos para UIs modulares.

5.  **Almacenamiento de Datos**
    - Descripción general de los métodos de almacenamiento.
    - Almacenamiento en archivos (escribir/leer; ej. guardar inicio de sesión de QQ).
    - SharedPreferences (almacenar/leer/eliminar; ej. inicio de sesión de QQ).
    - Base de datos SQLite (creación, operaciones CRUD, transacciones; ej. contactos de guisantes verdes).
    *Requisitos*: Persistir datos de forma segura; consultar/gestionar bases de datos.

6.  **Proveedor de Contenido (Content Provider)**
    - Descripción general.
    - Creación.
    - Acceso a otras aplicaciones (consultar datos; ej. leer contactos del teléfono).
    - Observadores de contenido (Content Observers) (monitorear cambios; ej. detección de cambios de datos).
    *Requisitos*: Compartir datos entre aplicaciones; implementar observadores.

7.  **Mecanismo de Emisión (Broadcast)**
    - Descripción general.
    - Receptores de emisiones (Broadcast Receivers) (creación).
    - Emisiones personalizadas (Custom Broadcasts) (ej. emisión de cafetería).
    - Tipos de emisión (ej. contando patos).
    *Requisitos*: Manejar eventos del sistema/aplicación a través de emisiones.

8.  **Servicios (Services)**
    - Descripción general y creación.
    - Ciclo de vida.
    - Métodos de inicio (startService, bindService).
    - Comunicación (local/remota; ej. reproductor de música NetEase).
    *Requisitos*: Ejecutar tareas en segundo plano; permitir la comunicación entre componentes.

9.  **Programación de Redes**
    - Acceso HTTP (HttpURLConnection).
    - Desarrollo con WebView (navegar HTML, soporte para JS).
    - Análisis de JSON (JSON parsing) (ej. interfaz de regateo de Pinduoduo).
    - Mecanismo de mensajes Handler.
    *Requisitos*: Obtener/analizar datos web; manejar operaciones asíncronas.

10. **Procesamiento de Gráficos e Imágenes**
    - Clases de dibujo (Bitmap, BitmapFactory, Paint, Canvas; ej. dibujar un cachorro).
    - Efectos de imagen.
    - Animaciones (tween, fotograma a fotograma, de propiedades; ej. mariposas/pájaros volando).
    *Requisitos*: Crear elementos visuales/animaciones; optimizar gráficos.

11. **Desarrollo de Aplicaciones Multimedia**
    - Reproducción de audio (MediaPlayer, SoundPool; ej. piano).
    - Reproducción de video (VideoView, SurfaceView+MediaPlayer; ej. reproductores de video).
    *Requisitos*: Integrar medios; controlar la reproducción.

12. **Proyecto Integral: Imitación de Meituan Takeout**
    - Análisis del proyecto (visión general, entorno, módulos).
    - Demostraciones de UI (tiendas, detalles, pedidos).
    - Preparación de datos del servidor.
    - Implementar listado de tiendas, detalles, menú/carrito de compras, pedidos/pago.
    *Requisitos*: Integrar todos los conceptos en una aplicación completa.

**Notas Adicionales y Requisitos de Implementación**
- **Consejos de Estudio**: Construir entornos de laboratorio pronto; programar junto con los ejemplos. Centrarse en 70% práctica, 30% teoría. Utilizar las sugerencias del IDE integrado durante los exámenes prácticos.
- **Formato del Examen**: Teórico: Opción múltiple, respuesta corta, análisis de código (80% de cobertura de los capítulos 1-11). Práctico (14568): Programación práctica para funciones centrales (ej. UI, almacenamiento, servicios).
- **Actualizaciones**: Los contenidos pueden ajustarse con revisiones del libro de texto; consultar la Autoridad de Exámenes Educativos de Guangdong (eea.gd.gov.cn) para la versión más reciente.

Para el PDF completo del plan de estudios oficial, visite los recursos de autoexamen de Guangdong o descargue de sitios autorizados como zikaosw.cn.

**Referencias**
- [Plan de Curso de Autoexamen de Guangdong](https://eea.gd.gov.cn/attachment/0/532/532589/4262692.pdf)
- [Tabla de Contenidos del Libro de Texto](https://resource.ityxb.com/book/android_case2.html)
- [Resumen del Plan de Estudios para Autoexamen de Guangdong](https://www.zikaosw.cn/news/22151554.html)