---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Eliminar Bifurcaciones No Deseadas de GitHub
translated: true
type: note
---

Entendido. Versión corta: no puedes eliminar directamente el fork de otra persona. Pero puedes (a) pedírselo, (b) purgar contenido sensible y bloquear futuras filtraciones, y (c) usar las vías oficiales de GitHub (DMCA o Soporte) cuando esté justificado. Aquí tienes un plan limpio, sin tablas, que funciona bien para blogs personales.

### 1) Primero, envía un mensaje a quien hizo el fork (la vía más rápida)

Abre un *issue* en su fork o envíales un correo electrónico. Aquí tienes una plantilla concisa que puedes pegar:

> Hola @tornadobaflocer — este fork contiene mis notas personales e historial de actividad. Publiqué el repositorio solo para usar el dominio `lzwjava.github.io`, no para redistribución. Por favor, elimina este fork. Voy a hacer el código fuente privado y mantendré públicos solo los activos compilados del sitio.
> Gracias por tu comprensión.

Si lo eliminan, has terminado. Si no, continúa.

### 2) Entiende lo que GitHub hará y no hará

* Eliminar o hacer privado tu repositorio **público** **no** elimina los forks públicos existentes. Los forks públicos permanecen públicos y se separan en su propia "red". ([Stack Overflow][1])
* Solo puedes eliminar un fork si eres **administrador de ese fork** (que no es tu caso aquí). ([Stack Overflow][2])

### 3) Si el fork copia tu contenido con derechos de autor sin permiso

Puedes presentar una solicitud de retirada DMCA ante GitHub. Es la vía oficial para eliminar contenido infractor en los forks. Lee la política y la guía "cómo enviar"; explican qué información debes incluir. ([GitHub Docs][3])

Consejo: Si tu repositorio no tenía **ninguna licencia**, se aplica el derecho de autor por defecto, lo que fortalece una solicitud de retirada (la gente no tenía derechos de reutilización). DMCA sigue siendo válido incluso si tenías una licencia permisiva, pero es más matizado.

### 4) Evita que futuros forks expongan tu código fuente

Mantén el **dominio** público, pero mantén el **código fuente** privado dividiendo los repositorios:

* **Repositorio de código fuente privado** (ej., `blog-source`): tu contenido de Jekyll/Hugo, borradores, notas, configuraciones.
* **Repositorio de despliegue público** llamado **`lzwjava.github.io`**: contiene **solo el sitio construido** (HTML/CSS/JS). Sin borradores, sin historial.

Los sitios de GitHub Pages son públicos incluso cuando el repositorio es privado (excepto en Enterprise Cloud con Pages privadas). Así que para un blog personal, la configuración de dos repositorios "solo despliegue" es el patrón seguro. ([GitHub Docs][4])

Opciones de despliegue que puedes usar hoy:

* Empuja la salida `public/` o `docs/` del generador a `lzwjava.github.io`. ([Quarto][5])
* O usa un flujo de trabajo de GitHub Actions en `blog-source` que construya y fuerce un *push* de la salida al repositorio `lzwjava.github.io` en su rama por defecto. (Docs: elige el flujo "Publicar desde una rama" o "Publicar con Actions"). ([GitHub Docs][6])

### 5) Purga cualquier dato sensible del historial (el tuyo y el de cualquier copia restante)

* Rota cualquier *token*/clave expuesta (asume que están comprometidas).
* Reescribe el historial para eliminar archivos/rutas sensibles con `git filter-repo` (GitHub ahora lo recomienda) o BFG (más rápido para casos comunes). Luego haz un *force-push*. ([GitHub Docs][7])

Esto no arreglará los forks de otras personas por sí solo, pero limpia tu repositorio canónico y respalda cualquier reclamo de retirada al mostrar que el contenido ha sido eliminado.

### 6) Fortalecimiento opcional

* Añade una LICENCIA clara (si quieres restringir explícitamente la reutilización).
* Añade un descargo de responsabilidad en el README: "Este repositorio existe solo para la salida compilada del sitio. **No** hagas fork del código fuente; es privado."
* Si alguna vez alojas en una **organización**, puedes desactivar el *forking* de repositorios privados para toda la organización y por repositorio (no evita la clonación de código público, pero ayuda para repositorios privados). ([GitHub Docs][8])

---

## Próximos pasos concretos (orden que funciona)

1. Pídele a @tornadobaflocer que elimine el fork (usa el mensaje de arriba).
2. Inmediatamente mueve tu código fuente a un nuevo repositorio **privado** (`blog-source`).
3. Haz de `lzwjava.github.io` un repositorio **público, solo de despliegue** con solo los archivos construidos. Configura Pages para publicar desde su rama/carpeta. ([GitHub Docs][6])
4. Reescribe el historial de tu antiguo repositorio público para eliminar los datos sensibles, luego archívalo o elimínalo. ([GitHub Docs][7])
5. Si se niegan y quieres que lo retiren, envía una **solicitud de retirada DMCA** a GitHub. ([GitHub Docs][9])

Si quieres, puedo redactar el aviso DMCA en el formato exacto que pide GitHub, y un flujo de trabajo mínimo de GitHub Actions que construya tu sitio desde `blog-source` y envíe solo los archivos compilados a `lzwjava.github.io`.

[1]: https://stackoverflow.com/questions/53052745/what-happens-to-the-forks-when-deleting-the-original-repository?utm_source=chatgpt.com "What happens to the forks when deleting the original repository?"
[2]: https://stackoverflow.com/questions/50280412/github-delete-a-fork-that-was-created-from-my-repo?utm_source=chatgpt.com "Github - Delete a fork that was created from my repo"
[3]: https://docs.github.com/articles/dmca-takedown-policy?utm_source=chatgpt.com "DMCA Takedown Policy"
[4]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "Creating a GitHub Pages site"
[5]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[6]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site?utm_source=chatgpt.com "Configuring a publishing source for your GitHub Pages site"
[7]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository?utm_source=chatgpt.com "Removing sensitive data from a repository"
[8]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository?utm_source=chatgpt.com "Managing the forking policy for your repository"
[9]: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice?utm_source=chatgpt.com "Guide to Submitting a DMCA Takedown Notice"