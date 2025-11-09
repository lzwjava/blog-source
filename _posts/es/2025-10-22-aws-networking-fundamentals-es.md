---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Fundamentos de Redes Virtuales de AWS
translated: true
type: note
---

### Conceptos Básicos de Redes Virtuales en AWS

AWS proporciona un entorno de red flexible y aislado a través de su servicio **Virtual Private Cloud (VPC)**. Esto actúa como tu propia sección lógicamente aislada de la Nube de AWS, donde puedes lanzar recursos como instancias EC2, bases de datos RDS y más. A continuación, desglosaré los componentes clave que mencionaste (red virtual, puerta de enlace, subredes) y algunos relacionados ("etc.") en términos simples, y cómo se integran.

#### Red Virtual (VPC - Virtual Private Cloud)
- **Qué es**: La base de las redes en AWS. Una VPC es una red virtual dedicada a tu cuenta de AWS, similar a una red tradicional de centro de datos pero en la nube. Se extiende a una o más Zonas de Disponibilidad (AZ) en una región.
- **Características clave**:
  - Defines su rango de direcciones IP usando bloques CIDR (por ejemplo, 10.0.0.0/16, que permite ~65,000 direcciones IP).
  - Está aislada por defecto—no hay tráfico entrante o saliente a menos que lo configures.
  - Soporta IPv4 e IPv6.
- **¿Por qué usarla?**: Controla el acceso, la seguridad y la conectividad para tus recursos. Cada cuenta de AWS obtiene una VPC por defecto, pero puedes crear VPCs personalizadas para entornos de producción.
- **Ejemplo**: Piensa en una VPC como el patio trasero privado en el "vecindario" de AWS—tú decides las cercas, puertas y caminos dentro de él.

#### Subredes
- **Qué son**: Subdivisiones del rango de direcciones IP de una VPC. Cada subred está vinculada a una sola Zona de Disponibilidad y actúa como una zona segmentada dentro de tu red.
- **Tipos**:
  - **Subred pública**: Los recursos aquí pueden acceder a internet directamente (a través de una Internet Gateway).
  - **Subred privada**: Aislada del acceso directo a internet; se utiliza para recursos sensibles como bases de datos.
- **Características clave**:
  - El tamaño se define por CIDR (por ejemplo, 10.0.1.0/24 para ~250 IPs).
  - Puedes tener múltiples subredes por AZ para alta disponibilidad.
  - Los recursos (por ejemplo, instancias EC2) se lanzan en una subred.
- **¿Por qué usarlas?**: Mejora la seguridad y la tolerancia a fallos—por ejemplo, coloca servidores web en subredes públicas y servidores de aplicaciones en subredes privadas.
- **Ejemplo**: Si tu VPC es una ciudad, las subredes son barrios: los públicos cerca de la carretera (internet), los privados en comunidades cerradas.

#### Puertas de Enlace
Las puertas de enlace conectan tu VPC con el mundo exterior u otras redes. Hay algunos tipos:

- **Internet Gateway (IGW)**:
  - **Qué es**: Un componente de alta disponibilidad que se adjunta a tu VPC, permitiendo la comunicación bidireccional con la internet pública.
  - **Cómo funciona**: Enruta el tráfico desde las subredes públicas a internet (y viceversa). Requiere actualizaciones en la tabla de rutas para dirigir el tráfico (por ejemplo, 0.0.0.0/0 → igw-xxxx).
  - **¿Por qué usarla?**: Para aplicaciones de cara al público como sitios web. Es gratuita y escala automáticamente.
  - **Ejemplo**: La puerta de entrada a internet—adjúntala, actualiza las rutas, y tus recursos públicos pueden navegar o ser navegados.

- **NAT Gateway (Network Address Translation)**:
  - **Qué es**: Se sitúa en una subred pública y permite que los recursos de subredes privadas inicien tráfico saliente a internet (por ejemplo, para actualizaciones de software) sin exponerlos al tráfico entrante.
  - **Cómo funciona**: Traduce las IPs privadas a una IP elástica pública. Es más confiable que las instancias NAT.
  - **¿Por qué usarlo?**: Acceso saliente seguro para recursos privados. Cuesta ~$0.045/hora + transferencia de datos.
  - **Ejemplo**: Una válvula unidireccional—los servidores privados pueden "llamar" para obtener paquetes, pero nadie puede tocar la puerta sin invitación.

- **Otras puertas de enlace** (brevemente):
  - **Virtual Private Gateway (VGW)**: Para conexiones VPN a tu red local.
  - **Transit Gateway**: Conecta múltiples VPCs y redes locales como un concentrador.

#### Otros Componentes Relacionados ("Etc.")
- **Tablas de Ruta**: Definen cómo se enruta el tráfico dentro de tu VPC (por ejemplo, hacia IGW, NAT o conexiones de peering). Cada subred tiene una tabla de rutas asociada—piensa en ella como un mapa de tráfico.
- **Network ACLs (Access Control Lists)**: Firewalls sin estado a nivel de subred, que controlan el tráfico entrante/saliente por IP/protocolo (por ejemplo, permitir el puerto 80).
- **Security Groups**: Firewalls con estado a nivel de instancia, que actúan como porteros personales para EC2/RDS (por ejemplo, permitir SSH desde tu IP).
- **VPC Peering**: Conecta dos VPCs (incluso en diferentes cuentas/regiones) para comunicación privada, como un túnel directo.
- **Elastic Network Interfaces (ENIs)**: Tarjetas de red virtuales para instancias, que permiten múltiples IPs o adjuntos.

#### Cómo Encaja Todo
1. Crea una VPC con un bloque CIDR.
2. Añade subredes (públicas/privadas) a través de las AZs.
3. Adjunta una Internet Gateway para acceso público.
4. Configura las tablas de ruta para dirigir el tráfico (por ejemplo, las subredes públicas enrutan hacia IGW).
5. Lanza recursos en las subredes y asegúralos con Security Groups/NACLs.
6. Para el acceso saliente privado, añade un NAT Gateway.

Esta configuración asegura escalabilidad, seguridad y resiliencia. Para practicar, comienza con el asistente de VPC de AWS en la consola—configura automáticamente una configuración básica.

Si necesitas diagramas, ejemplos de código o detalles sobre una parte específica (por ejemplo, peering), ¡avísame!

**Referencias**:
- [Documentación de AWS VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Guía de Subredes de AWS](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [Resumen de Puertas de Enlace de AWS](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)