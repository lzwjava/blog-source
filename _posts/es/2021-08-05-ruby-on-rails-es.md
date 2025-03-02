---
audio: false
generated: false
lang: es
layout: post
title: Usando Ruby on Rails
translated: true
---

Durante mi tiempo en ShowMeBug, contribuí al proyecto de integración de Enterprise WeChat. Esto implicó integrar ShowMeBug con Enterprise WeChat, proporcionando acceso sin problemas a las herramientas de entrevistas técnicas dentro del ecosistema de Enterprise WeChat. Utilicé tecnologías como Ruby, Ruby on Rails, PostgreSQL y el SDK de WeChat para crear una experiencia de usuario fluida tanto para entrevistadores como para candidatos.

Este artículo de blog fue compuesto con la asistencia de IA alrededor de febrero de 2025.

---

Ruby on Rails (a menudo simplemente "Rails") es un potente marco de desarrollo web construido sobre el lenguaje de programación Ruby. Está diseñado para hacer que la construcción de aplicaciones web sea rápida y agradable, enfatizando las convenciones sobre la configuración y los principios DRY (Don’t Repeat Yourself). Vamos a pasar por su configuración y la creación de una aplicación simple.

#### Paso 1: Instalar Ruby y Rails
Primero, necesitarás tener Ruby instalado, ya que Rails es una gema (biblioteca) de Ruby. La mayoría de los sistemas no vienen con Ruby preinstalado, así que aquí tienes cómo configurarlo:

- **En macOS/Linux:**
  - Usa un gestor de versiones como `rbenv` o `rvm` para flexibilidad. Instálalo a través de Homebrew (`brew install rbenv`), luego ejecuta:
    ```bash
    rbenv install 3.2.2  # Una versión estable de Ruby según 2025
    rbenv global 3.2.2
    ```
  - Instalar Rails:
    ```bash
    gem install rails
    ```

- **En Windows:**
  - Usa RubyInstaller (descárgalo desde rubyinstaller.org). Elige una versión como 3.2.2 con DevKit.
  - Después de instalar Ruby, abre una ventana de comandos y ejecuta:
    ```bash
    gem install rails
    ```

Verifica la instalación:
```bash
ruby -v  # Debería mostrar algo como ruby 3.2.2
rails -v # Debería mostrar la última versión de Rails, por ejemplo, 7.1.x
```

#### Paso 2: Crear un Nuevo Proyecto de Rails
Una vez instalado Rails, genera una nueva aplicación:
```bash
rails new myapp --database=sqlite3
cd myapp
```
Esto crea una carpeta llamada `myapp` con una estructura completa de Rails, utilizando SQLite como base de datos predeterminada (ideal para desarrollo).

#### Paso 3: Iniciar el Servidor
Ejecuta el servidor integrado de Rails:
```bash
rails server
```
Abre tu navegador en `http://localhost:3000`. Verás una página de bienvenida. ¡Enhorabuena, tu aplicación de Rails está en funcionamiento!

#### Paso 4: Construir Algo Simple
Vamos a crear una característica básica de "Publicaciones" para entender el patrón MVC (Modelo-Vista-Controlador) de Rails.

- **Generar un Modelo y Controlador:**
  ```bash
  rails generate scaffold Post title:string body:text
  ```
  Esto crea un modelo `Post`, una migración de base de datos, un controlador y vistas—todo conectado.

- **Ejecutar la Migración:**
  ```bash
  rails db:migrate
  ```
  Esto configura la tabla de base de datos para las publicaciones.

- **Revisarlo:**
  Reinicia el servidor (`rails server`) y visita `http://localhost:3000/posts`. Verás una interfaz CRUD para crear, leer, actualizar y eliminar publicaciones.

#### Paso 5: Explorar Conceptos Clave
- **Rutas:** Abre `config/routes.rb`. Verás `resources :posts`, que genera automáticamente rutas RESTful como `/posts/new` o `/posts/1/edit`.
- **Controladores:** Mira `app/controllers/posts_controller.rb`. Maneja las solicitudes y respuestas.
- **Vistas:** Revisa `app/views/posts/`. Son plantillas ERB (HTML con Ruby incrustado).
- **Modelos:** Mira `app/models/post.rb`. Se conecta a la base de datos y puede incluir validaciones (por ejemplo, `validates :title, presence: true`).

#### Paso 6: Personalizar y Desplegar
- Añade algo de estilo con CSS en `app/assets/stylesheets/`.
- Para producción, cambia a una base de datos como PostgreSQL (`rails new myapp --database=postgresql`) y despliega en una plataforma como Render o Heroku. Actualiza `Gemfile` con `gem "pg"` y ejecuta `bundle install`.

#### Consejos Pro
- Usa `rails console` para experimentar con tus modelos en tiempo real.
- Ejecuta `rails generate --help` para ver todos los atajos que ofrece Rails.
- Aprovecha las gemas como `devise` para autenticación o `pundit` para autorización—añádelas a tu `Gemfile` y configúralas según sea necesario.

¡Y eso es todo! Tienes una aplicación básica de Rails en funcionamiento. Desde aquí, explora las Guías Oficiales de Rails (guides.rubyonrails.org) o construye algo real para consolidar tus habilidades. ¿Qué tipo de proyecto tienes en mente?