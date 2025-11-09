---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Conceptos Básicos de Redes Virtuales de Azure
translated: true
type: note
---

### Conceptos Básicos de Azure Virtual Networking

Azure proporciona un entorno de red escalable y seguro a través de su servicio **Virtual Network (VNet)**, que es el equivalente central a AWS VPC. Crea un espacio privado y aislado en la nube de Azure para tus recursos como máquinas virtuales, App Services o clústeres de Kubernetes. A continuación, explicaré los componentes clave (red virtual, puertas de enlace, subredes, etc.) con similitudes y diferencias respecto a AWS, estructurado de manera similar para facilitar la comparación.

#### Virtual Network (VNet)
- **Qué es**: La red aislada fundamental en Azure, que abarca una región y permite que los recursos se comuniquen de forma privada. Defines su espacio de direcciones con bloques CIDR (por ejemplo, 10.0.0.0/16).
- **Características clave**:
  - Acceso a internet saliente por defecto para los recursos (a diferencia de AWS, donde es opcional).
  - Soporta IPv4 e IPv6; aislada por defecto.
  - No hay costo por la VNet en sí—se paga por recursos asociados como puertas de enlace.
- **Similar a AWS VPC**: Ambos son nubes privadas para el aislamiento, escalado y conectividad de recursos. Las VNets de Azure se extienden automáticamente por las zonas de disponibilidad (AZ); las VPC de AWS requieren una configuración explícita de las AZ.
- **¿Por qué usarla?**: Comunicación segura entre recursos, acceso a internet y enlaces locales. Cada suscripción de Azure tiene acceso, pero creas VNets personalizadas para tener control.
- **Ejemplo**: Al igual que AWS VPC, es tu "propiedad privada" en la nube—tú estableces los límites, pero Azure maneja algunos valores por defecto como el acceso a internet saliente.

#### Subredes
- **Qué son**: Divisiones del espacio de direcciones de una VNet, donde se despliegan los recursos. Cada subred está limitada a la VNet y puede abarcar todas las AZ en una región.
- **Tipos**:
  - **Subred pública**: Los recursos pueden tener IPs públicas para acceso a internet entrante/saliente (a través de Azure Load Balancer o endpoints públicos).
  - **Subred privada**: Sin acceso público directo; ideal para bases de datos o aplicaciones internas.
- **Características clave**:
  - Definidas por CIDR (por ejemplo, 10.0.1.0/24).
  - Múltiples por VNet para segmentación; el tráfico entre ellas puede filtrarse.
- **Similar a las subredes de AWS**: Ambas segmentan redes para seguridad y organización. La extensión automática de Azure por las AZ simplifica la Alta Disponibilidad; AWS asocia las subredes a AZ específicas.
- **¿Por qué usarlas?**: Aísla cargas de trabajo—por ejemplo, frontends en subredes públicas, backends en privadas.
- **Ejemplo**: Las subredes son "distritos" en tu ciudad VNet: las públicas con acceso a la calle (internet), las privadas detrás de muros.

#### Puertas de Enlace
Las puertas de enlace en Azure manejan la conectividad externa, pero con algunos valores por defecto que difieren de AWS.

- **Equivalente a Internet Gateway**:
  - **Qué es**: No hay un IGW directo; el acceso a internet saliente está habilitado por defecto para los recursos de la VNet. El acceso entrante requiere una IP pública o un Load Balancer.
  - **Cómo funciona**: El tráfico se enruta a través de las rutas del sistema de Azure (0.0.0.0/0 a internet). Usa IPs públicas para acceso bidireccional.
  - **Similar a AWS IGW**: Ambos permiten el acceso público a internet, pero Azure es más "siempre activo" para el tráfico saliente; AWS requiere una asociación y configuración de rutas explícitas.
  - **¿Por qué usarlo?**: Exposición pública simple para aplicaciones web. Gratuito para el enrutamiento básico.

- **NAT Gateway**:
  - **Qué es**: Un servicio gestionado en una subred pública para acceso a internet solo saliente desde subredes privadas (por ejemplo, actualizaciones de VM).
  - **Cómo funciona**: Comparte una IP elástica para la traducción; altamente disponible entre AZs.
  - **Similar a AWS NAT Gateway**: Ambos proporcionan salida segura sin exposición entrante. El de Azure está más integrado y es escalable por defecto.
  - **¿Por qué usarlo?**: Protege los recursos privados permitiendo acceso unidireccional. Cuesta ~$0.045/hora + datos.

- **Otras puertas de enlace**:
  - **VPN Gateway**: Para VPNs sitio a sitio o punto a sitio hacia entornos locales (como AWS VGW).
  - **ExpressRoute Gateway**: Enlaces privados de alto ancho de banda hacia entornos locales (como AWS Direct Connect).

#### Otros Componentes Relacionados ("Etc.")
- **Tablas de Ruta**: Controlan el flujo de tráfico de la subred (por ejemplo, hacia internet o VNets emparejadas). Existen rutas del sistema por defecto; las personalizadas las anulan para rutas específicas. Similar a las tablas de ruta de AWS, pero Azure propaga rutas BGP dinámicamente desde entornos locales.
- **Grupos de Seguridad de Red (NSGs)**: Firewalls con estado para subredes o recursos, con reglas por IP/puerto/protocolo. Como una combinación de los AWS Security Groups (a nivel de instancia, con estado) y NACLs (a nivel de subred, pero los de Azure son con estado). Usa Application Security Groups para etiquetado lógico.
- **Emparejamiento de VNets**: Conecta VNets (misma/diferente región/cuenta) para tráfico privado, como el emparejamiento de VPC de AWS.
- **Service Endpoints/Private Link**: Acceso privado seguro a servicios de Azure (por ejemplo, Storage) sin internet, similar a AWS VPC Endpoints.
- **Network Virtual Appliances**: Firewalls o routers basados en VM en la VNet, similares a AWS Network Firewall.

#### Cómo Encaja Todo
1.  Crea una VNet con CIDR.
2.  Añade subredes (públicas/privadas) que abarquen las AZs.
3.  Los recursos obtienen acceso a internet saliente por defecto; añade IPs públicas/Load Balancers para el acceso entrante.
4.  Usa NAT Gateway para el acceso saliente desde subredes privadas.
5.  Aplica tablas de ruta y NSGs para el control del tráfico.
6.  Empareja VNets o añade puertas de enlace para configuraciones híbridas.

El modelo de Azure enfatiza los valores por defecto (por ejemplo, internet saliente) para una configuración más rápida, mientras que AWS ofrece opciones más granulares. Ambos priorizan la seguridad y la resiliencia.

Para practicar, prueba el asistente de VNet en el portal de Azure.

[Información general sobre Azure Virtual Network](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)