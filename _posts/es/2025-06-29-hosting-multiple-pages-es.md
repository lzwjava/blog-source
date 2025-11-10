---
audio: false
generated: true
lang: es
layout: post
title: Alojar Múltiples Páginas de GitHub con Organizaciones
translated: true
type: note
---

Sí, crear una organización de GitHub es una forma viable de alojar sitios adicionales de GitHub Pages con subdominios únicos `*.github.io`, ya que cada organización puede tener su propio sitio `organization.github.io`, separado de tu sitio personal `username.github.io`. Así es como puedes hacerlo y lo que necesitas saber:

### Puntos Clave
- **Limitación de Cuenta Personal**: Cada cuenta de usuario de GitHub puede tener solo un Sitio de Usuario, alojado en `username.github.io`, que está vinculado a un repositorio llamado `username.github.io`. Si ya has usado este para tu cuenta personal, no puedes crear otro subdominio `*.github.io` bajo la misma cuenta.
- **Sitios de Organización**: Cada organización de GitHub también puede tener su propio Sitio de Organización, alojado en `organization.github.io`, creando un repositorio llamado `organization.github.io`. Esto te permite crear subdominios `*.github.io` adicionales configurando múltiples organizaciones.
- **Sitios de Proyecto**: Tanto las cuentas de usuario como las de organización pueden alojar múltiples Sitios de Proyecto (por ejemplo, `username.github.io/project` o `organization.github.io/project`) desde otros repositorios, pero estos son subrutas, no subdominios. Si específicamente quieres subdominios distintos (por ejemplo, `sub.example.github.io`), no puedes lograrlo directamente con GitHub Pages sin un dominio personalizado, ya que GitHub no admite subdominios personalizados como `sub.example.github.io` bajo el dominio `github.io`.[](https://github.com/orgs/community/discussions/54144)

### Pasos para Crear una Organización de GitHub para Subdominios `*.github.io` Adicionales
1. **Crear una Organización de GitHub**:
   - Ve a GitHub e inicia sesión con tu cuenta.
   - Haz clic en el icono "+" en la esquina superior derecha y selecciona **New organization**.
   - Sigue las indicaciones para configurar la organización, eligiendo un nombre único (por ejemplo, `myorg`). Este nombre determinará el subdominio (por ejemplo, `myorg.github.io`).
   - Nota: Las organizaciones se pueden crear de forma gratuita, pero algunas características (como repositorios privados) pueden requerir un plan de pago, dependiendo de tus necesidades. GitHub Pages para repositorios públicos está disponible con GitHub Free.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

2. **Crear el Repositorio de GitHub Pages de la Organización**:
   - En la nueva organización, crea un repositorio llamado exactamente `myorg.github.io` (reemplaza `myorg` con el nombre de tu organización).
   - Este repositorio alojará el Sitio de Organización, accesible en `https://myorg.github.io`.

3. **Configurar GitHub Pages**:
   - Ve a la pestaña **Settings** del repositorio `myorg.github.io`.
   - Desplázate a la sección **Pages**.
   - En **Source**, selecciona la rama que quieres publicar (por ejemplo, `main` o `gh-pages`) y guarda.
   - Una vez configurado, el sitio estará disponible en `https://myorg.github.io` después de unos minutos.[](https://dev.to/mohammedasker/how-to-get-github-subdomain-with-github-pages-4g0p)

4. **Agregar Contenido**:
   - Agrega un archivo `index.html` o usa un generador de sitios estáticos como Jekyll a la rama de publicación del repositorio.
   - Confirma y envía tus cambios. Por ejemplo:
     ```bash
     git clone https://github.com/myorg/myorg.github.io
     cd myorg.github.io
     echo "Hello World" > index.html
     git add --all
     git commit -m "Initial commit"
     git push origin main
     ```
   - Visita `https://myorg.github.io` para verificar que el sitio esté disponible.[](https://dev.to/mohammedasker/how-to-get-github-subdomain-with-github-pages-4g0p)

5. **Repetir para Subdominios Adicionales**:
   - Crea organizaciones adicionales (por ejemplo, `myorg2`, `myorg3`) y repite el proceso para obtener `myorg2.github.io`, `myorg3.github.io`, etc.
   - Cada organización puede tener un subdominio `*.github.io`, permitiéndote crear tantos subdominios como organizaciones tengas.

### Limitaciones y Consideraciones
- **Subdominios Personalizados en `github.io`**: No puedes crear subdominios como `sub.myorg.github.io` directamente con GitHub Pages. El dominio `github.io` es gestionado por GitHub, y solo se admiten `username.github.io` o `organization.github.io`. Para usar subdominios personalizados (por ejemplo, `blog.example.com`), debes poseer un dominio personalizado y configurar los ajustes DNS (registros CNAME) para que apunten a `myorg.github.io`.[](https://github.com/orgs/community/discussions/54144)[](https://github.com/orgs/community/discussions/64133)
- **Repositorio Único por Subdominio**: Cada subdominio `*.github.io` está vinculado a un único repositorio (`username.github.io` o `organization.github.io`). No puedes servir múltiples subdominios desde un solo repositorio sin un dominio personalizado y servicios de alojamiento o proxy adicionales.[](https://webmasters.stackexchange.com/questions/144484/separate-subdomains-on-one-github-page)
- **Sobrecarga de Gestión**: Cada organización requiere una gestión separada (por ejemplo, miembros, permisos, facturación). Asegúrate de que estás cómodo gestionando múltiples organizaciones.
- **DNS y Dominios Personalizados**: Si quieres usar un dominio personalizado (por ejemplo, `example.com` o `sub.example.com`) en lugar de `*.github.io`, puedes configurarlo en los ajustes **Pages** del repositorio y agregar un registro CNAME con tu proveedor de DNS. Por ejemplo, apunta `sub.example.com` a `myorg.github.io`. Asegúrate de verificar el dominio para prevenir riesgos de toma de control.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)[](https://dev.to/scc33/how-to-host-a-site-with-a-subdomain-on-github-pages-5a1j)
- **Repositorios Privados**: GitHub Pages para repositorios privados requiere planes GitHub Pro, Team o Enterprise. Si estás usando planes gratuitos, asegúrate de que tu repositorio `myorg.github.io` sea público.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

### Alternativa para Múltiples Subdominios
Si tu objetivo es tener múltiples subdominios (por ejemplo, `blog.example.com`, `shop.example.com`) bajo un único dominio personalizado, puedes:
1. Comprar un dominio personalizado (por ejemplo, `example.com`) de un registrador como Namecheap o GoDaddy.
2. Crear múltiples repositorios en tu organización (por ejemplo, `myorg/blog`, `myorg/shop`).
3. Habilitar GitHub Pages para cada repositorio, estableciendo dominios personalizados como `blog.example.com` y `shop.example.com` en sus respectivos ajustes **Pages**.
4. Configurar registros CNAME con tu proveedor de DNS para que `blog.example.com` apunte a `myorg.github.io` y `shop.example.com` apunte a `myorg.github.io`. Ten en cuenta que todos los repositorios sin su propio dominio personalizado aparecerán bajo el dominio personalizado de la organización como subrutas (por ejemplo, `example.com/blog`).[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)[](https://stackoverflow.com/questions/68505452/github-pages-with-single-custom-subdomain-for-multiple-repositories-using-paths)
5. Ten en cuenta que servir múltiples subdominios desde un único repositorio no es compatible de forma nativa por GitHub Pages y puede requerir servicios externos como una CDN o un proxy inverso.[](https://webmasters.stackexchange.com/questions/144484/separate-subdomains-on-one-github-page)

### Ejemplo de Escenario
- Has usado `username.github.io` para tu sitio personal.
- Crea una organización llamada `myorg` y un repositorio `myorg.github.io` para obtener `myorg.github.io`.
- Crea otra organización llamada `myorg2` y un repositorio `myorg2.github.io` para obtener `myorg2.github.io`.
- Para subdominios personalizados, posee `example.com` y configura `blog.example.com` (apuntando a `myorg.github.io`) y `shop.example.com` (apuntando a `myorg2.github.io`) a través de registros CNAME.

### Notas Finales
- Crear múltiples organizaciones es una forma sencilla de obtener subdominios `*.github.io` adicionales sin necesidad de un dominio personalizado.
- Si quieres subdominios verdaderos (por ejemplo, `sub.myorg.github.io`), necesitarás un dominio personalizado y configuración DNS, ya que el `github.io` de GitHub no admite esto de forma nativa.
- Siempre verifica los dominios personalizados para evitar riesgos de seguridad como tomas de control de dominio.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- Los cambios de DNS pueden tardar hasta 24 horas en propagarse.[](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

Si tienes más preguntas o necesitas ayuda con configuraciones específicas, ¡avísame!