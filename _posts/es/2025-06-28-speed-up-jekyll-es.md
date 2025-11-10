---
audio: false
generated: true
lang: es
layout: post
title: 'Acelerando las compilaciones de Jekyll: Explorando enfoques de multiprocesamiento'
translated: true
type: note
---

El proceso de compilación de Jekyll es de un solo hilo por defecto, lo que puede ser lento para sitios grandes. Si bien no existe una opción de configuración incorporada en Jekyll para habilitar compilaciones multihilo, puedes explorar algunos enfoques para lograr paralelismo. A continuación, describo las posibilidades, los desafíos y los pasos prácticos basados en la información disponible y consideraciones técnicas.

### Por qué las compilaciones de Jekyll son de un solo hilo
Jekyll procesa las páginas de forma secuencial para garantizar que las dependencias (como `site.related_posts` o las plantillas Liquid) se manejen correctamente. Algunos componentes, como Liquid y ciertos plugins, pueden no ser seguros para hilos, lo que complica el multihilo (). Este diseño prioriza la corrección sobre la velocidad, pero para sitios grandes, esto puede generar tiempos de compilación de varios minutos (,).[](https://github.com/jekyll/jekyll/issues/9485)[](https://github.com/jekyll/jekyll/issues/1855)[](https://github.com/jekyll/jekyll/issues/4297)

### Enfoques para compilaciones multihilo de Jekyll
Aquí hay formas potenciales de introducir paralelismo en las compilaciones de Jekyll, particularmente en el contexto de un flujo de trabajo de GitHub Actions como el que proporcionaste:

#### 1. **Usar un Plugin Personalizado para Renderizado Multihilo**
Se ha propuesto un plugin de prueba de concepto para el renderizado multihilo (). Redujo el tiempo de compilación de 45 segundos a 10 segundos en un caso de prueba, pero tuvo problemas de seguridad de hilos, lo que llevó a contenido de página incorrecto. El plugin también entró en conflicto con plugins como `jekyll-feed`, que dependen del renderizado secuencial.[](https://github.com/jekyll/jekyll/issues/9485)

**Pasos para probar un plugin personalizado:**
- **Crear un Plugin**: Implementa un plugin Ruby que extienda la clase `Site` de Jekyll para paralelizar el renderizado de páginas. Por ejemplo, podrías modificar el método `render_pages` para usar la clase `Thread` de Ruby o un grupo de hilos ().[](https://github.com/jekyll/jekyll/issues/9485)
  ```ruby
  module Jekyll
    module UlyssesZhan::MultithreadRendering
      def render_pages(*args)
        @rendering_threads = []
        super # Llamar al método original
        @rendering_threads.each(&:join) # Esperar a que los hilos terminen
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::UlyssesZhan::MultithreadRendering)
  ```
- **Agregar al Gemfile**: Coloca el plugin en tu directorio `_plugins` y asegúrate de que Jekyll lo cargue.
- **Probar la Seguridad de Hilos**: Dado que Liquid y algunos plugins (por ejemplo, `jekyll-feed`) pueden romperse, prueba exhaustivamente. Es posible que necesites parchear Liquid o evitar el multihilo para ciertas funciones ().[](https://github.com/jekyll/jekyll/issues/9485)
- **Integrar con GitHub Actions**: Actualiza tu flujo de trabajo para incluir el plugin en tu repositorio. Asegúrate de que la acción `jekyll-build-pages` use tu configuración personalizada de Jekyll:
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
    env:
      BUNDLE_GEMFILE: ./Gemfile # Asegúrate de que se use tu Gemfile personalizado con el plugin
  ```

**Desafíos**:
- Problemas de seguridad de hilos con Liquid y plugins como `jekyll-feed` ().[](https://github.com/jekyll/jekyll/issues/9485)
- Potencial de renderizado incorrecto de páginas (por ejemplo, el contenido de una página apareciendo en otra).
- Requiere experiencia en Ruby para depurar y mantener.

#### 2. **Paralelizar compilaciones con múltiples configuraciones**
En lugar de multihilo en una sola compilación, puedes dividir tu sitio en partes más pequeñas (por ejemplo, por colección o directorio) y compilarlas en paralelo usando múltiples procesos de Jekyll. Este enfoque evita problemas de seguridad de hilos pero requiere más configuración.

**Pasos**:
- **Dividir el Sitio**: Organiza tu sitio en colecciones (por ejemplo, `posts`, `pages`, `docs`) o directorios y crea archivos `_config.yml` separados para cada uno (,).[](https://amcrouch.medium.com/configuring-environments-when-building-sites-with-jekyll-dd6eb2603c39)[](https://coderwall.com/p/tfcj2g/using-different-build-configuration-in-jekyll-site)
  ```yaml
  # _config_posts.yml
  collections:
    posts:
      output: true
  destination: ./_site/posts

  # _config_pages.yml
  collections:
    pages:
      output: true
  destination: ./_site/pages
  ```
- **Actualizar el Flujo de Trabajo de GitHub Actions**: Modifica tu flujo de trabajo para ejecutar múltiples compilaciones de Jekyll en paralelo, cada una con un archivo de configuración diferente.
  ```yaml
  name: Build Jekyll Site
  on:
    push:
      branches: [main]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Setup Ruby
          uses: ruby/setup-ruby@v1
          with:
            ruby-version: '3.1'
            bundler-cache: true
        - name: Build Posts
          run: bundle exec jekyll build --config _config_posts.yml
        - name: Build Pages
          run: bundle exec jekyll build --config _config_pages.yml
        - name: Combine Outputs
          run: |
            mkdir -p ./_site
            cp -r ./_site/posts/* ./_site/
            cp -r ./_site/pages/* ./_site/
        - name: Deploy
          uses: actions/upload-artifact@v4
          with:
            name: site
            path: ./_site
  ```
- **Combinar Salidas**: Después de las compilaciones paralelas, fusiona los directorios de salida en una sola carpeta `_site` para la implementación.

**Desafíos**:
- Manejar interdependencias entre colecciones (por ejemplo, `site.related_posts`).
- Mayor complejidad en la configuración y la implementación.
- Puede no escalar bien para sitios con contenido estrechamente acoplado.

#### 3. **Usar un grupo de hilos para sitios grandes**
Una solicitud de extracción para el plugin `amp-jekyll` sugirió usar un grupo de hilos para procesar páginas, con un número configurable de hilos para evitar sobrecargar el sistema (). Este enfoque equilibra el rendimiento y el uso de recursos.[](https://github.com/juusaw/amp-jekyll/pull/26)

**Pasos**:
- **Implementar un Grupo de Hilos**: Modifica o crea un plugin para usar `Thread::Queue` de Ruby para gestionar un número fijo de hilos de trabajo (por ejemplo, 4 u 8, dependiendo de tu sistema).
  ```ruby
  require 'thread'

  module Jekyll
    module ThreadPoolRendering
      def render_pages(*args)
        queue = Queue.new
        site.pages.each { |page| queue << page }
        threads = (1..4).map do # 4 hilos
          Thread.new do
            until queue.empty?
              page = queue.pop(true) rescue nil
              page&.render_with_liquid(site)
            end
          end
        end
        threads.each(&:join)
        super
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::ThreadPoolRendering)
  ```
- **Agregar Opción de Configuración**: Permite a los usuarios activar/desactivar el multihilo o establecer el número de hilos en `_config.yml`:
  ```yaml
  multithreading:
    enabled: true
    thread_count: 4
  ```
- **Integrar con el Flujo de Trabajo**: Asegúrate de que el plugin esté incluido en tu repositorio y se cargue durante la compilación de GitHub Actions.

**Desafíos**:
- Problemas de seguridad de hilos similares al primer enfoque.
- Sobrecarga por cambio de contexto para sitios grandes con muchas tareas cortas ().[](https://github.com/juusaw/amp-jekyll/pull/26)
- Requiere pruebas para garantizar la compatibilidad con todos los plugins.

#### 4. **Optimizar sin multihilo**
Si el multihilo resulta demasiado complejo o arriesgado, puedes optimizar el proceso de compilación de un solo hilo:
- **Habilitar Compilaciones Incrementales**: Usa `jekyll build --incremental` para recompilar solo los archivos cambiados (,). Agrega a tu flujo de trabajo:[](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/commands/build.rb)[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
      incremental: true
  ```
- **Reducir el Uso de Plugins**: Los plugins personalizados pueden ralentizar significativamente las compilaciones (). Audita y elimina los plugins innecesarios.[](https://github.com/jekyll/jekyll/issues/4297)
- **Usar Convertidores Más Rápidos**: Cambia de Kramdown a un procesador de markdown más rápido como CommonMark, o prueba Pandoc para casos de uso específicos ().[](https://github.com/jekyll/jekyll/issues/9485)
- **Almacenar en Caché las Dependencias**: Asegúrate de que `bundler-cache: true` esté en tu flujo de trabajo de GitHub Actions para evitar reinstalar gemas ().[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

### Recomendaciones
- **Comenzar con Compilaciones Incrementales**: Esta es la forma más simple de acelerar las compilaciones sin arriesgar problemas de seguridad de hilos. Agrega `--incremental` a tu flujo de trabajo y prueba su impacto.
- **Experimentar con un Plugin de Grupo de Hilos**: Si tienes experiencia en Ruby, intenta implementar un plugin de grupo de hilos con un número configurable de hilos (Opción 3). Comienza con un sitio pequeño para probar la seguridad de hilos.
- **Evitar el Multihilo Completo por Ahora**: Dadas las preocupaciones de seguridad de hilos con Liquid y los plugins (), el multihilo completo puede requerir una refactorización significativa o un fork personalizado de Liquid, lo que puede no ser práctico a menos que estés contribuyendo al desarrollo central de Jekyll.[](https://github.com/jekyll/jekyll/issues/9485)
- **Monitorear los Tiempos de Compilación**: Usa los registros de GitHub Actions para medir los tiempos de compilación e identificar cuellos de botella. Por ejemplo, un sitio que tarda 6 minutos en compilarse () sugiere que los plugins o el procesamiento de activos grandes pueden ser el problema.[](https://github.com/jekyll/jekyll/issues/1855)

### Ejemplo de GitHub Actions con Compilaciones Incrementales
Aquí hay una versión actualizada de tu flujo de trabajo con compilaciones incrementales habilitadas:
```yaml
name: Build Jekyll Site
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
          incremental: true
      - name: Deploy
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: ./_site
```

### Advertencias
- **Seguridad de Hilos**: El multihilo en Jekyll es experimental y puede romper plugins o producir salida incorrecta (). Prueba exhaustivamente en un sitio pequeño primero.[](https://github.com/jekyll/jekyll/issues/9485)
- **Límites de GitHub Actions**: Las compilaciones paralelas (Opción 2) aumentan el uso de recursos, así que asegúrate de que tu flujo de trabajo se mantenga dentro de los límites del nivel gratuito de GitHub.
- **Potencial de Jekyll 5**: Las futuras versiones de Jekyll pueden abordar el multihilo de forma nativa, como se ha discutido (). Por ahora, se necesitan soluciones personalizadas.[](https://github.com/jekyll/jekyll/issues/9485)

Si necesitas ayuda para implementar un enfoque específico (por ejemplo, escribir un plugin o dividir compilaciones), ¡avísame y puedo proporcionar una guía o código más detallado!