---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: 'Administrador de Acceso a la Red Cisco AnyConnect: Descripción General'
translated: true
type: note
---

Cisco AnyConnect Secure Mobility Client es un conjunto de módulos de software que proporciona acceso VPN seguro, seguridad de red y funciones de endpoint basadas en políticas. Uno de los módulos opcionales de este conjunto es **Cisco Network Access Manager (NAM).**

### Qué hace Cisco AnyConnect NAM
- **Gestión de Conexiones de Red**: NAM reemplaza a los administradores de red nativos, tanto inalámbricos como cableados, de Windows. Se encarga de configurar, conectar y asegurar redes cableadas e inalámbricas.
- **Soporte Avanzado para 802.1X**: Proporciona una **autenticación 802.1X** integral para conexiones de red cableadas e inalámbricas (EAP-TLS, PEAP, EAP-FAST, etc.), utilizada a menudo en entornos empresariales donde se requiere autenticación basada en certificados o postura del endpoint.
- **Aplicación de Políticas**: Los administradores pueden definir políticas que determinen cómo los dispositivos de los usuarios finales se conectan a las redes, priorizando requisitos de seguridad, definiendo SSIDs permitidos o restringiendo conexiones inseguras.
- **Comportamiento Consistente en Todas las Plataformas**: Ofrece control centralizado para que los usuarios tengan la misma experiencia de acceso a la red sin importar en qué PC estén.

### Puntos Clave
- **Soporte de Plataformas**: Históricamente, NAM solo era compatible con Windows. Cisco eliminó el soporte para NAM a partir de versiones posteriores de AnyConnect (desde la v4.9 en adelante), ya que los administradores de red nativos del sistema operativo (Windows Native Wi-Fi, supplicant de macOS, etc.) se volvieron más robustos.
- **Uso Típico**: Se implementa principalmente en empresas, universidades o redes gubernamentales que requieren un inicio de sesión seguro basado en certificados para Wi-Fi o LAN cableada antes o durante el inicio de sesión del sistema.

👉 En resumen: **Cisco AnyConnect NAM (Network Access Manager)** es un administrador de conexiones de red avanzado que reemplaza al supplicant nativo de Windows para manejar conexiones cableadas/inalámbricas seguras utilizando autenticación 802.1X y políticas definidas por la empresa.

---

¿Te gustaría que también explique **cómo se compara NAM con el módulo VPN de AnyConnect, que es el más comúnmente utilizado** (ya que la mayoría de la gente hoy en día solo conoce la parte de VPN)?