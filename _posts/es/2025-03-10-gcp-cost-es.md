---
audio: false
generated: true
lang: es
layout: post
title: Estimación de Costos de GCP para VPN en Taipéi
translated: true
type: note
---

Para estimar el costo de usar un servidor en Taipei como VPN con Google Cloud, considerando que vives en Guangzhou y esperas 50 GB de datos de red por mes usando una instancia E2 micro, debemos desglosar los costos en varios componentes: la instancia de máquina virtual (VM), el tráfico de salida de red (egress) y el almacenamiento de disco persistente. Aquí tienes un cálculo detallado basado en los precios de Google Cloud para la región asia-east1 (Taipei), donde estará alojado tu servidor.

### 1. Costo de la Instancia VM (E2 Micro en Taipei)
La E2 micro es un tipo de máquina de núcleos compartidos con 0.25 vCPU y 1 GB de memoria. Según los precios de Google Cloud para Compute Engine en la región asia-east1:
- **Tarifa por hora para E2 micro**: $0.0084 por hora.
- **Horas en un mes**: Suponiendo que un mes típico tiene 730 horas (una aproximación estándar basada en 365 días ÷ 12 meses ≈ 30.42 días × 24 horas).
- **Costo mensual**:  
  $0.0084/hora × 730 horas ≈ $6.132.

Por lo tanto, ejecutar la instancia E2 micro continuamente durante un mes cuesta aproximadamente **$6.13**.

### 2. Costo del Tráfico de Salida de Red (Egress)
Dado que estás usando el servidor de Taipei como VPN desde Guangzhou, tu configuración implica ejecutar un servidor VPN (por ejemplo, OpenVPN) en la instancia E2 micro, no el servicio Cloud VPN de Google Cloud. Tus 50 GB de datos de red mensuales representan el tráfico total procesado a través de la VPN. Así es como fluye el tráfico:
- **Desde tu dispositivo en Guangzhou al servidor VPN**: Esto es tráfico de entrada (ingress) a Google Cloud (gratuito).
- **Desde el servidor VPN a internet**: Esto es tráfico de salida (egress) (con cargo).
- **Desde internet de vuelta al servidor VPN**: Esto es tráfico de entrada (ingress) (gratuito).
- **Desde el servidor VPN de vuelta a tu dispositivo**: Esto es tráfico de salida (egress) (con cargo).

Si tus 50 GB se refieren al tráfico total del túnel VPN (datos enviados desde tu dispositivo más datos recibidos de vuelta), el tráfico de salida facturado por Google Cloud incluye:
- Datos enviados desde el servidor VPN a internet.
- Datos enviados desde el servidor VPN de vuelta a tu dispositivo.

Suponiendo que los 50 GB son el total de datos transferidos (por ejemplo, envías solicitudes y recibes respuestas, como navegación o streaming), el tráfico de salida total es de aproximadamente 50 GB. Esto simplifica la estimación, ya que la división exacta entre datos enviados y recibidos depende del uso (por ejemplo, el streaming tiene más datos recibidos, mientras que las subidas tienen más datos enviados). Para uso general de internet, trataremos los 50 GB como el egress total.

Google Cloud cobra por el egress a internet según la región de origen (asia-east1 para Taipei):
- **Nivel de precios**: Para Asia (excluyendo China, India, Indonesia y Filipinas), la tarifa es $0.12 por GiB por los primeros 1 TB de egress mensual.
- **Conversión**: Google Cloud usa GiB (1 GiB = 1024³ bytes), mientras que tú especificaste 50 GB (1 GB = 1000³ bytes). Precisamente, 1 GB ≈ 0.931 GiB, por lo que 50 GB ≈ 46.55 GiB. Sin embargo, para simplificar y por práctica común en estimaciones aproximadas, aproximaremos 50 GB ≈ 50 GiB, ya que la diferencia es menor para volúmenes pequeños.
- **Costo de egress**:  
  50 GiB × $0.12/GiB = $6.00.

Por lo tanto, el costo de egress de red es aproximadamente **$6.00** por mes.

### 3. Costo del Disco Persistente
La instancia E2 micro requiere un disco de arranque. Si bien el nivel gratuito de Google Cloud ofrece 30 GB de almacenamiento de disco persistente estándar en ciertas regiones de EE. UU., Taipei (asia-east1) no está incluida, por lo que incurrirás en cargos:
- **Tamaño del disco**: Suponiendo un disco persistente estándar típico de 30 GB (podrías usar menos, como 10 GB, pero 30 GB es común para una VM básica).
- **Precio**: $0.040 por GB por mes en asia-east1 para disco persistente estándar.
- **Costo mensual**:  
  30 GB × $0.040/GB = $1.20.

El disco persistente añade **$1.20** por mes.

### 4. Dirección IP Externa
Tu servidor VPN necesita una dirección IP externa para ser accesible desde Guangzhou. Para las VM de Compute Engine:
- Si la IP está adjunta a una VM en ejecución, no hay cargo adicional.
- Si está reservada pero sin usar, hay una pequeña tarifa (no aplicable aquí ya que la VM funciona continuamente).

Dado que tu E2 micro usará la IP externa, este costo está **incluido en el precio de la VM**.

### Costo Total Estimado
Sumando todos los componentes:
- **Instancia VM**: $6.13
- **Tráfico de salida (egress)**: $6.00
- **Disco persistente**: $1.20
- **IP Externa**: $0.00 (incluida)

**Total**: $6.13 + $6.00 + $1.20 = **$13.33 por mes**.

### Notas Adicionales
- **Tráfico de entrada (ingress)**: Gratuito, por lo que los datos que entran a la VM (desde ti o desde internet) no generan costos.
- **Sin nivel gratuito**: El nivel gratuito de E2 micro aplica solo a regiones específicas de EE. UU. (no Taipei), y el egress gratuito de 1 GB es desde América del Norte (no Asia), excluyendo destinos en China, por lo que no aplica aquí.
- **Suposiciones de uso**: Los $13.33 suponen que 50 GB es el tráfico de salida total. Si son solo datos enviados o recibidos, ajusta el costo de egress proporcionalmente (por ejemplo, si 50 GB son datos recibidos, el egress hacia ti es de $6.00, pero el egress hacia internet podría ser menor).
- **Sin Cloud VPN**: Dado que estás ejecutando tu propio software VPN (por ejemplo, OpenVPN), no hay cargos adicionales por puerta de enlace o túnel de Cloud VPN.

### Respuesta Final
El costo estimado de usar un servidor en Taipei (asia-east1) como VPN en Google Cloud con una instancia E2 micro, 50 GB de datos de red mensuales y un disco de 30 GB es de aproximadamente **$13.33 por mes**. Esto incluye la instancia VM ($6.13), el tráfico de salida hacia internet y tu dispositivo ($6.00) y el disco persistente ($1.20).