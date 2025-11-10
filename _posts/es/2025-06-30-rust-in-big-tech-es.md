---
audio: false
generated: true
lang: es
layout: post
title: El auge de Rust en las grandes tecnológicas
translated: true
type: note
---

Rust está ganando una tracción significativa en las grandes tecnológicas debido a su fuerte enfoque en la seguridad de la memoria, el rendimiento y la concurrencia. Muchas empresas tecnológicas importantes están adoptando Rust para varios proyectos críticos. Aquí hay un desglose de algunos ejemplos prominentes:

**1. Amazon (AWS)**
* **Firecracker:** Un microVM diseñado para ejecutar cargas de trabajo de contenedores de forma segura y a escala, que impulsa AWS Lambda y Fargate.
* **AWS Nitro System:** Se utiliza para desarrollar nuevos componentes, incluidos entornos EC2 seguros y aislados.
* **Otros Servicios:** Rust se utiliza en componentes de Amazon S3, Amazon EC2, Amazon CloudFront y Amazon Route 53.
* **Bottlerocket:** Un sistema operativo de contenedores basado en Linux escrito en Rust.

**2. Microsoft**
* **Componentes de Windows:** Microsoft está reescribiendo activamente partes de Windows, incluidos componentes del kernel, en Rust para mejorar la seguridad y la mantenibilidad.
* **Servicios de Azure:** Rust está integrado en Azure IoT Edge y Kusto (el motor central de consultas y almacenamiento para Azure Data Explorer).
* **`windows-rs`:** Un proyecto que permite llamar a las APIs de Windows usando Rust.

**3. Meta (Facebook)**
* **Herramientas Internas de Control de Fuentes:** Meta reconstruyó partes de su sistema interno de control de fuentes (Mononoke) en Rust para manejar su gran monorepositorio con mejor concurrencia y velocidad.
* **Blockchain Diem (anteriormente Libra):** La blockchain para este proyecto de criptomoneda fue escrita principalmente en Rust.

**4. Google**
* **Android Open Source Project (AOSP):** Rust se utiliza cada vez más para escribir componentes seguros del sistema en Android, reduciendo los errores de memoria en funciones críticas como el procesamiento de medios y el acceso al sistema de archivos.
* **Fuchsia OS:** Una proporción significativa del código interno de Fuchsia OS está escrita en Rust.
* **Chromium:** Existe soporte experimental para Rust en Chromium.

**5. Dropbox**
* **Motor de Sincronización (Sync Engine):** Rust reemplazó código antiguo de Python y C++ en el motor de sincronización de archivos de Dropbox, lo que condujo a una reducción del uso de la CPU, una mejor concurrencia y una sincronización más fluida.
* **Sistema Central de Almacenamiento de Archivos:** Varios componentes de su sistema central de almacenamiento de archivos están escritos en Rust.

**6. Discord**
* **Servicios Backend:** Discord utiliza Rust para servicios backend críticos como el enrutamiento de mensajes y el seguimiento de presencia, mejorando el rendimiento y la confiabilidad. Cambiaron de Go a Rust para su servicio "Read States" para evitar picos de latencia.
* **Lados del Cliente y del Servidor:** Tanto el lado del cliente como el del servidor de la base de código de Discord tienen componentes en Rust.

**7. Cloudflare**
* **Pingora:** Un proxy web de alto rendimiento escrito en Rust para reemplazar a NGINX, lo que resultó en un uso reducido de la CPU y una mejor gestión de conexiones.
* **Lógica Central del Edge (Core Edge Logic):** Rust se utiliza en la lógica central del edge de Cloudflare como reemplazo de lenguajes no seguros para la memoria como C.
* **Cloudflare Workers:** Admite la implementación de código serverless con Rust.

**8. Mozilla**
* **Firefox (Stylo):** Mozilla, el creador original de Rust, utilizó el lenguaje para construir Stylo, el motor CSS en Firefox, mejorando significativamente el rendimiento y la seguridad.
* **Servo:** Un motor de navegador web prototipo construido completamente en Rust.

**9. npm (Node Package Manager)**
* **Servicios de Autenticación:** npm utilizó Rust para reescribir partes de sus servicios de autenticación para mejorar la seguridad, manejar la carga y reducir los retrasos.

**Otros Adoptantes y Proyectos Notables:**
* **Kernel de Linux:** Rust es ahora el segundo lenguaje oficial para el desarrollo del kernel de Linux, permitiendo controladores de dispositivos y otros módulos más seguros.
* **Figma:** Su motor de sincronización multijugador fue reescrito de TypeScript a Rust para mejorar el rendimiento.
* **1Password:** Impulsa sus últimas aplicaciones de escritorio y móviles con una única base de código Rust compartida.
* **Hugging Face:** Muchos componentes en su ecosistema de IA, incluidos `safetensors`, `tokenizer` y `candle`, están implementados usando Rust.
* **Polkadot:** Esta plataforma blockchain está construida completamente en Rust por seguridad y velocidad.
* **Solana:** Otra plataforma blockchain de alto rendimiento que aprovecha Rust.
* **Navegador Brave:** Utiliza Rust en algunos de sus componentes.
* **Atlassian:** Utiliza Rust en un servicio para analizar petabytes de código fuente.
* **Huawei:** Migró partes de su base de código a Rust para equipos de telecomunicaciones y herramientas de infraestructura.

La adopción de Rust por parte de estas importantes empresas tecnológicas subraya su creciente importancia para construir software confiable, eficiente y seguro, particularmente para la programación a nivel de sistema, la infraestructura y las aplicaciones de alto rendimiento.