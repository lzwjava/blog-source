---
audio: false
generated: false
image: false
lang: es
layout: post
title: Configuración de un Servidor en Azure
translated: true
type: post
---

Configurar un servidor en Microsoft Azure y configurarlo para abrir puertos específicos es esencial para diversas aplicaciones, como servicios de alojamiento, proxies y más. Esta guía te llevará paso a paso a través del proceso de creación de una Máquina Virtual (VM) en Azure y la configuración del firewall para abrir el puerto 1080.

## Tabla de Contenidos

1. [Requisitos previos](#prerequisites)
2. [Creación de una máquina virtual en Azure](#creating-an-azure-virtual-machine)
3. [Configuración del firewall para abrir el puerto 1080](#configuring-the-firewall-to-open-port-1080)
4. [Prueba de la configuración](#testing-the-configuration)
5. [Conclusión](#conclusion)

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Una cuenta activa de [Microsoft Azure](https://azure.microsoft.com/).
- Conocimientos básicos sobre el uso del Portal de Azure.
- Un cliente SSH (como Terminal en macOS/Linux o PuTTY en Windows) para acceder a la máquina virtual.

## Creación de una Máquina Virtual en Azure

1. Inicia sesión en el Portal de Azure:
   Dirígete al [Portal de Azure](https://portal.azure.com/) e inicia sesión con tus credenciales.

2. Crear una nueva máquina virtual:
   - Haz clic en "Crear un recurso" en la esquina superior izquierda.
   - Selecciona "Máquina virtual" de la lista de recursos disponibles.

3. Configurar los aspectos básicos de la VM:
   - Suscripción: Elige tu suscripción de Azure.
   - Grupo de recursos: Crea un nuevo grupo de recursos o selecciona uno existente.
   - Nombre de la máquina virtual: Ingresa un nombre para tu VM (por ejemplo, `AzureServer`).
   - Región: Selecciona la región más cercana a tu audiencia objetivo.
   - Imagen: Elige una imagen del sistema operativo (por ejemplo, Ubuntu 22.04 LTS).
   - Tamaño: Selecciona un tamaño de VM según tus necesidades de rendimiento.
   - Autenticación: Elige la clave pública SSH para un acceso seguro. Sube tu clave pública SSH.

4. Configurar la red:
   - Asegúrate de que la máquina virtual esté colocada en la red virtual y subred adecuadas.
   - Deja habilitada la IP pública para permitir el acceso externo.

5. Revisar y Crear:
   - Revisa tus configuraciones.
   - Haz clic en "Crear" para desplegar la VM. La implementación puede tardar unos minutos.

## Configuración del Firewall para Abrir el Puerto 1080

Una vez que tu máquina virtual esté en funcionamiento, deberás configurar el Grupo de Seguridad de Red (NSG) de Azure para permitir el tráfico en el puerto 1080.

1. Navega a la Configuración de Red de tu VM:
   - En el Portal de Azure, ve a "Máquinas virtuales".
   - Selecciona tu VM (`AzureServer`).
   - Haz clic en "Redes" en la barra lateral izquierda.

2. Identifica el Grupo de Seguridad de Red (NSG):
   - En "Interfaz de Red", localiza el NSG asociado.
   - Haz clic en el NSG para gestionar sus reglas.

3. Agregar una regla de seguridad de entrada:
   - En la configuración del NSG, ve a "Reglas de seguridad de entrada".
   - Haz clic en "Agregar" para crear una nueva regla.

4. Configura la Regla:
   - Origen: Cualquiera (o especifica un rango para mayor seguridad).
   - Rangos de puertos de origen: `*`
   - Destino: Cualquiera
   - Rangos de puertos de destino: `1080`
   - Protocolo: TCP
   - Acción: Permitir
   - Prioridad: `1000` (asegúrate de que no entre en conflicto con reglas existentes).
   - Nombre: `Allow-1080-TCP`

5. Guardar la Regla:
   - Haz clic en "Agregar" para aplicar la nueva regla.

## Probando la Configuración

Después de configurar el firewall, es esencial verificar que el puerto 1080 esté abierto y accesible.

1. Usa Telnet para Verificar la Accesibilidad del Puerto:
   Desde tu máquina local, ejecuta:

```bash
telnet <TU_IP_VM> 1080
```

   - Reemplaza `<YOUR_VM_IP>` con la dirección IP pública de tu máquina virtual.
   - Si la conexión es exitosa, el puerto está abierto y accesible.

2. Herramientas Alternativas para Verificar Puertos:
   - Netcat (`nc`):
     ```bash
     nc -zv <TU_IP_VM> 1080
     ```
   - Verificadores de Puertos en Línea:
     Utiliza servicios en línea como [canyouseeme.org](https://canyouseeme.org/) para verificar si el puerto 1080 está abierto.

3. Resolución de problemas:
   - Problemas de conexión: Verifica que las reglas del NSG estén configuradas correctamente y que cualquier firewall local en la VM esté configurado para permitir tráfico en el puerto 1080.
   - IP incorrecta: Asegúrate de estar utilizando la dirección IP pública correcta de tu VM.

## Conclusión

Siguiendo esta guía, has configurado con éxito una Máquina Virtual de Azure y has configurado el firewall para abrir el puerto 1080. Esta configuración sienta las bases para implementar diversas aplicaciones o servicios que requieren acceso a puertos específicos.

Para configuraciones adicionales, como configurar servicios de proxy u otras aplicaciones en el puerto 1080, consulta nuestras publicaciones dedicadas sobre [Configuración de Proxy V2Ray](#) y [Generación de una URL vmess personalizada](#).