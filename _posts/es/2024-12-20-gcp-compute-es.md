---
audio: false
generated: false
image: false
lang: es
layout: post
title: Configuración de un Servidor en Google Cloud
translated: true
type: post
---

Configurar un servidor proxy en Google Cloud te permite enrutar tu tráfico de internet de manera segura a través de una instancia en la nube, mejorando la privacidad y evitando restricciones. En esta guía, te llevaremos paso a paso por el proceso de configurar un servidor proxy básico en Google Cloud y configurar las reglas de firewall necesarias para permitir el tráfico.

## Índice de Contenidos
1. [Creación de una Instancia de VM en Google Cloud](#creación-de-una-instancia-de-vm-en-google-cloud)
2. [Configuración del Servidor Proxy](#configuración-del-servidor-proxy)
3. [Configuración de Reglas de Firewall](#configuración-de-reglas-de-firewall)
4. [Prueba del Servidor Proxy](#prueba-del-servidor-proxy)
5. [Conclusión](#conclusión)

---

## Creando una Instancia de Máquina Virtual en Google Cloud

Antes de configurar el servidor proxy, necesitarás crear una instancia de máquina virtual (VM) en Google Cloud.

1. Inicia sesión en Google Cloud Console: Ve a [Google Cloud Console](https://console.cloud.google.com/) e inicia sesión en tu cuenta.

2. Crea una nueva instancia de VM:
   - Navega a Compute Engine > Instancias de VM.
   - Haz clic en Crear instancia.
   - Elige la Región y el Tipo de máquina que desees. Para simplificar, puedes usar la configuración predeterminada o elegir una configuración ligera como la instancia `e2-micro`.
   - En la sección de Firewall, selecciona tanto Permitir tráfico HTTP como Permitir tráfico HTTPS para habilitar el acceso web.

3. Configura el acceso SSH:
   - En la sección de Claves SSH, añade tu clave pública SSH para acceder a la instancia de forma remota. Esto es crucial para configurar tu servidor proxy más adelante.

4. Haz clic en Crear para lanzar tu VM.

Una vez que la máquina virtual esté configurada, puedes conectarte a ella usando SSH desde la consola de Google Cloud o a través de la terminal con:

```bash
gcloud compute ssh <tu-nombre-de-vm>
```

---

## Configuración del Servidor Proxy

Una vez que tu máquina virtual esté configurada, puedes configurar cualquier software de servidor proxy de tu elección. El software proxy debe estar instalado y configurado para aceptar conexiones en el puerto deseado (por ejemplo, `3128` para configuraciones de proxy comunes). Asegúrate de que el software permita conexiones desde clientes remotos.

---

## Configuración de Reglas de Firewall

Para permitir el tráfico a tu servidor proxy, necesitarás configurar las reglas del firewall de Google Cloud para abrir el puerto necesario.

1. Navega a las Reglas del Firewall en la Consola de Google Cloud:
   - Ve a VPC Network > Firewall Rules en la Consola de Google Cloud.

2. Crear una Nueva Regla de Firewall:
   - Haz clic en Crear Regla de Firewall.
   - Ingresa un nombre para la regla, como `allow-proxy-access`.
   - Establece la Dirección del tráfico en Entrante (tráfico entrante).
   - Establece la Acción en caso de coincidencia en Permitir.
   - Establece los Destinos en Todas las instancias en la red o Etiquetas de destino especificadas (si prefieres un mayor control).
   - En Rangos de IP de origen, puedes configurarlo como `0.0.0.0/0` para permitir el acceso desde todas las direcciones IP, o limitarlo a IPs o rangos específicos para una mayor seguridad.
   - En Protocolos y puertos, selecciona Protocolos y puertos especificados e ingresa el puerto utilizado por tu servidor proxy (por ejemplo, `tcp:3128`).

3. Guardar la Regla del Firewall:
   Después de configurar la regla, haz clic en Crear para habilitar el firewall.

---

## Probando el Servidor Proxy

Después de configurar el firewall, es momento de probar tu servidor proxy.

1. Probar el Proxy desde tu Máquina Local:

Puedes configurar el navegador o los ajustes del proxy del sistema en tu máquina local para utilizar la dirección IP externa de tu VM en Google Cloud y el puerto en el que tu servidor proxy está escuchando (por ejemplo, `3128`).

2. Prueba con la Línea de Comandos:

   También puedes probar el proxy con `curl` configurando las variables de entorno del proxy:

```bash
export http_proxy=http://<tu-ip-externa-de-la-vm>:3128
export https_proxy=http://<tu-ip-externa-de-la-vm>:3128
curl -I http://example.com
```

Si la conexión es exitosa, deberías ver una respuesta del sitio web.

---

## Conclusión

Al seguir esta guía, has aprendido cómo configurar un servidor proxy en Google Cloud y configurar reglas de firewall para permitir el tráfico entrante. Esta configuración proporciona una manera sencilla de enrutar tu tráfico de internet de forma segura a través de la nube, sortear restricciones de red y mejorar la privacidad.