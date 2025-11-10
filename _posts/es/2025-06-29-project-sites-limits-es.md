---
audio: false
generated: true
lang: es
layout: post
title: Reglas de URL de Sitios de Proyecto de GitHub Pages
translated: true
type: note
---

Con GitHub Pages, puedes crear **Sitios de Proyecto** bajo tu cuenta personal además de tu Sitio de Usuario (`username.github.io`). Sin embargo, el formato de la URL para los Sitios de Proyecto está limitado a patrones específicos, y no todas las configuraciones de subdominio o subruta son compatibles de forma nativa. Abordemos tu pregunta sobre si puedes usar `username.github.io/project1` o `project1.username.github.io` para Sitios de Proyecto.

### Puntos Clave
- **Sitio de Usuario**: Un único repositorio llamado `username.github.io` sirve contenido en `https://username.github.io`.
- **Sitios de Proyecto**: Cualquier otro repositorio en tu cuenta personal puede configurarse como un Sitio de Proyecto, servido en `https://username.github.io/nombre-del-repositorio` (una subruta, no un subdominio).
- **Limitación de Subdominio**: GitHub Pages no admite de forma nativa subdominios como `project1.username.github.io` bajo el dominio `github.io`. El dominio `github.io` es gestionado por GitHub, y solo `username.github.io` (para usuarios) u `organization.github.io` (para organizaciones) son compatibles como subdominios de primer nivel. Los subdominios personalizados como `project1.username.github.io` requieren un dominio personalizado y configuración de DNS.

### ¿Puedes Usar `username.github.io/project1`?
**Sí**, puedes usar `username.github.io/project1` para un Sitio de Proyecto. Esta es la forma estándar en que GitHub Pages maneja los Sitios de Proyecto:
- Crea un repositorio en tu cuenta personal (por ejemplo, `username/project1`).
- Habilita GitHub Pages para ese repositorio:
  - Ve a la pestaña **Settings** del repositorio.
  - Desplázate a la sección **Pages**.
  - En **Source**, selecciona la rama a publicar (por ejemplo, `main` o `gh-pages`) y guarda.
- Una vez configurado, el sitio será accesible en `https://username.github.io/project1`.
- Puedes crear múltiples Sitios de Proyecto (por ejemplo, `username.github.io/project2`, `username.github.io/project3`) habilitando GitHub Pages en repositorios adicionales (`username/project2`, `username/project3`, etc.).
- **Contenido**: Añade un `index.html` o usa un generador de sitios estáticos como Jekyll en la rama de publicación de cada repositorio.

### ¿Puedes Usar `project1.username.github.io`?
**No**, GitHub Pages no admite subdominios como `project1.username.github.io` de forma nativa bajo el dominio `github.io`. El dominio `github.io` solo permite:
- `username.github.io` para Sitios de Usuario.
- `organization.github.io` para Sitios de Organización.
- Subrutas como `username.github.io/nombre-del-repositorio` para Sitios de Proyecto.

Para lograr una URL como `project1.username.github.io**, necesitarías:
1. **Un Dominio Personalizado**: Comprar un dominio (por ejemplo, `example.com`) en un registrador como Namecheap o GoDaddy.
2. **Configuración de DNS**: Configurar un registro CNAME para apuntar un subdominio (por ejemplo, `project1.example.com`) a tu sitio de GitHub Pages (por ejemplo, `username.github.io` o `username.github.io/project1`).
3. **Configuración de GitHub Pages**:
   - En la configuración de **Pages** del repositorio, configura el dominio personalizado (por ejemplo, `project1.example.com`).
   - Opcionalmente, habilita "Enforce HTTPS" para mayor seguridad.
4. **Resultado**: Puedes mapear `project1.example.com` al contenido del repositorio `project1`, pero no `project1.username.github.io`, ya que GitHub controla el dominio `github.io` y no permite subdominios personalizados bajo él.

### Ejemplo de Configuración para `username.github.io/project1`
1. Crea un repositorio llamado `project1` bajo tu cuenta (`username/project1`).
2. Añade contenido (por ejemplo, `index.html`):
   ```bash
   git clone https://github.com/username/project1
   cd project1
   echo "Hello from Project 1" > index.html
   git add --all
   git commit -m "Initial commit"
   git push origin main
   ```
3. Habilita GitHub Pages:
   - Ve a `username/project1` → **Settings** → **Pages**.
   - Establece la fuente a `main` (u otra rama) y guarda.
4. Visita `https://username.github.io/project1` para ver el sitio en vivo (puede tardar unos minutos en propagarse).

### Ejemplo para Subdominio Personalizado con un Dominio Personalizado
Si quieres `project1.example.com`:
1. Posee un dominio (por ejemplo, `example.com`).
2. En la configuración de tu proveedor de DNS, añade un registro CNAME:
   - Nombre: `project1`
   - Valor: `username.github.io`
3. En la configuración de **Pages** del repositorio `project1`, establece el dominio personalizado a `project1.example.com`.
4. Sube contenido al repositorio `project1`, y será servido en `project1.example.com`.

### Limitaciones
- **Solo Subrutas para `github.io`**: Sin un dominio personalizado, los Sitios de Proyecto siempre se sirven como subrutas (`username.github.io/project1`), no como subdominios (`project1.username.github.io`).
- **Un Sitio de Usuario**: Tu repositorio `username.github.io` está reservado para tu Sitio de Usuario. Los Sitios de Proyecto usan otros repositorios y aparecen como subrutas.
- **Los Subdominios Personalizados Requieren un Dominio Personalizado**: Para obtener `project1.algo`, necesitas poseer `algo` (por ejemplo, `example.com`) y configurar el DNS.
- **Repositorios Privados**: Los Sitios de Proyecto en repositorios privados requieren GitHub Pro, Team o Enterprise. Para cuentas gratuitas, los repositorios deben ser públicos.

### Resumen
- **Usa `username.github.io/project1`**: Sí, esto es compatible de forma nativa creando un repositorio (`username/project1`) y habilitando GitHub Pages. Puedes crear múltiples Sitios de Proyecto de esta manera (por ejemplo, `username.github.io/project2`, etc.).
- **Usa `project1.username.github.io`**: No, esto no es compatible bajo `github.io**. Necesitarías un dominio personalizado (por ejemplo, `project1.example.com`) y configuración de DNS para lograr un efecto similar.
- **Múltiples Subdominios**: Para obtener múltiples subdominios `*.github.io`, crea organizaciones de GitHub (como se discutió previamente) para `org1.github.io`, `org2.github.io`, etc., o usa un dominio personalizado para subdominios como `project1.example.com`.

Si necesitas ayuda para configurar un Sitio de Proyecto específico, configurar un dominio personalizado o gestionar múltiples sitios, ¡avísame!