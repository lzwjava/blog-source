---
audio: false
generated: false
image: true
lang: es
layout: post
title: Cómo acceder a Google
translated: true
type: post
---

Esta publicación fue escrita originalmente en chino.

---

Esta lección cubre lo siguiente:

1. Cómo acceder al sitio web oficial de un servicio VPN.
2. Cómo usar una VPN en Windows.
3. Introducción al software Clash.
4. Intentar abrir Google, Twitter, YouTube y TikTok.

Empecemos. Aquí hay una descripción escrita de cómo le enseñé a Xiao Wang a acceder a Google.

Usaremos una plataforma llamada "Summoner". El sitio web es `https://zhshi.gitlab.io`.

<img src="/assets/images/google/zhs.png" alt="zhs" />

Sin embargo, es posible que no sea accesible porque está bloqueado por la Gran Muralla de Fuego.

![zhs_user](/assets/images/google/zhs_user.png)

Así es como se ve al iniciar sesión.

En realidad, hay dos maneras de eludir el cortafuegos. Una es comprar nuestro propio servidor en el extranjero. La otra es usar una plataforma VPN, que proporciona muchas direcciones de servidores en el extranjero.

"Eludir el cortafuegos" significa primero acceder a un servidor en el extranjero desde dentro del país. Este servidor en el extranjero puede entonces acceder a sitios web que están bloqueados.

Una plataforma de este tipo se llama "Summoner". Pero si el sitio web oficial es inaccesible, ¿cómo obtenemos las direcciones de servidores en el extranjero que proporciona? Xiao Wang está usando una VPN por primera vez, y le estoy enseñando a distancia. ¿Cómo debería enseñarle?

En este punto, pensé en habilitar la computadora con Windows de Xiao Wang para eludir el cortafuegos. Le proporcionaré a Xiao Wang una dirección. Luego, Xiao Wang puede abrir el sitio web "Summoner", registrar una cuenta y usar las direcciones del servidor en el extranjero en su propia cuenta.

![clash_win](/assets/images/google/clash_win.png)

![win_version](/assets/images/google/win_version.png)

A continuación, compruebe si su computadora es de 64 bits o de 32 bits. Si es de 64 bits, descargue `Clash.for.Windows.Setup.0.14.8.exe`. Si es de 32 bits, descargue `Clash.for.Windows.Setup.0.14.8.ia32.exe`.

La computadora de Xiao Wang es de 64 bits. Pero la descarga es muy lenta en su caso. Así que lo descargué en mi computadora y se lo envié por correo electrónico de QQ.

Lo descargó del correo electrónico de QQ, lo instaló y lo abrió.

![clash_win_exe](/assets/images/google/clash_win_exe.png)

Primero le di mi dirección de configuración de Summoner. Esta dirección de configuración descargará un archivo que contiene muchas direcciones de servidores VPN. En `Perfiles`, pegue la dirección y haga clic en `Descargar`.

![zhs_url](/assets/images/google/zhs_url.png)

Mira, ya se descargó. Observa la segunda configuración de arriba. Hay una marca de verificación verde delante, lo que indica que estamos usando esta configuración.

![zhs_proxy](/assets/images/google/zhs_proxy.png)

A continuación, abra la pestaña `Proxies`. Verá algunas cosas aquí. Estas son algunas de las configuraciones de `Clash`. En pocas palabras, significa que los sitios web nacionales no usarán la VPN, mientras que los sitios web extranjeros sí.

Tenga en cuenta que el valor actual de `Proxy` es `DIRECT`, lo que significa que es una conexión directa. Lo cambiaremos a un nodo.

![zhs_node](/assets/images/google/zhs_node.png)

Seleccionamos el nodo `US Rose`.

![clash_system](/assets/images/google/clash_system.png)

A continuación, active la configuración de `Proxy del sistema` para habilitarla. Esto significa configurar el software `Clash` como la capa proxy del sistema. Entonces, el tráfico del sistema primero irá al software `Clash` y luego accederá a la red externa.

<img src="/assets/images/google/google.png" alt="google" style="zoom:40%;" />

Xiao Wang abrió Google. Luego, probó TikTok, YouTube y Twitter.

Bueno, entonces Xiao Wang ha estado usando mi cuenta de Summoner. ¿Cómo se registra? Necesita abrir el sitio web oficial de Summoner.

<img src="/assets/images/google/zhs_register.png" alt="zhs_register" style="zoom:50%;" />

Después de registrarse, descubrió que la recarga para comprar servicios requiere algunos pasos. Aquí hay una captura de pantalla de mi cuenta.

![zeng](/assets/images/google/zeng.png)

Dice que necesita estar vinculado a Telegram.

<img src="/assets/images/google/zhs_telegram.png" alt="zhs_telegram" style="zoom:50%;" />

Xiao Wang fue al sitio web de Telegram y descargó la versión de escritorio de Telegram para Windows.

![telegram](/assets/images/google/telegram.png)

Después de descargarlo e instalarlo, preste atención al texto de arriba.

> Después de instalar Telegram y registrarse, haga clic para chatear con `小兔` o `城主`, copie el código QR a continuación y envíelo, o `haga clic aquí para copiar automáticamente el código y enviarlo al Bot para vincular`.

Cuando haga clic en `小兔`, saltará automáticamente al software `Telegram` y abrirá una ventana de chat con `小兔`. Luego, envíele el código.

![telegram_username](/assets/images/google/telegram_username.png)

Sin embargo, la cuenta de `Telegram` de Xiao Wang está recién registrada y no tiene un `nombre de usuario`. Es como usar WeChat sin configurar un ID de WeChat.

Busque el menú de Telegram y configúrelo. Luego, envíe el código nuevamente para vincular.

<img src="/assets/images/google/zhs_set.png" alt="zhs_set" style="zoom:50%;" />

A continuación, puede donar para apoyarlo. Puede empezar recargando 30 yuanes durante dos meses.

Vuelva a la página de inicio de Summoner. Aquí, busque el botón "Click to Copy", obtenga la dirección y luego descargue la configuración en el software `Clash`.

Luego, Xiao Wang puede eliminar la dirección que le di. Xiao Wang ahora tiene su propia cuenta de Summoner.