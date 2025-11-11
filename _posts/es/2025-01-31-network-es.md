---
audio: false
generated: false
lang: es
layout: post
title: Tecnología de Redes Informáticas
translated: true
type: note
---

A continuación se presenta una lista de 100 puntos clave que cubren ampliamente el alcance de un curso o plan de autoestudio de "Tecnología de Redes Informáticas", tocando conceptos fundamentales, protocolos y aplicaciones prácticas.

1.  Definición de una Red Informática: Un sistema de dispositivos interconectados que comparten recursos y datos.
2.  Funciones Principales de las Redes: Compartición de recursos, comunicación, transmisión de datos y colaboración.
3.  Evolución de las Redes: Desde ARPANET y las primeras LANs hasta la Internet global que tenemos hoy.
4.  Tipos Comunes de Redes: LAN (Red de Área Local), MAN (Red de Área Metropolitana), WAN (Red de Área Amplia).
5.  Estructuras de Topología: Bus, estrella, anillo, malla e híbrida.
6.  Intranet vs. Extranet vs. Internet: Diferencias de alcance y casos de uso típicos.
7.  Organizaciones de Estándares: IEEE, IETF, ISO—definiendo y manteniendo estándares y protocolos de red.
8.  Modelo de Referencia OSI: Un marco conceptual de siete capas para comprender las funciones de la red.
9.  Modelo TCP/IP: Un modelo pragmático de cuatro capas (o a veces cinco) que sustenta Internet.
10. Comparación de OSI y TCP/IP: Similitudes (enfoque por capas) y diferencias (número de capas y abstracción).

11. Propósito de la Capa Física: Se ocupa de la transmisión de bits sin procesar sobre un medio físico.
12. Medios de Transmisión Comunes: Cable de par trenzado, cable coaxial, fibra óptica e inalámbrico.
13. Ancho de Banda vs. Rendimiento: Tasa máxima teórica vs. tasa real de transferencia de datos.
14. Codificación de Señal: Métodos (por ejemplo, codificación Manchester) para representar bits de datos para su transmisión.
15. Técnicas de Modulación: AM, FM, PM utilizadas en conversiones analógico-digitales o digital-analógicas.
16. Dispositivos de la Capa Física: Hubs, repetidores—principalmente repiten señales sin inspección.
17. Propósito de la Capa de Enlace de Datos: Maneja el entramado, direccionamiento, detección/corrección de errores y control de flujo.
18. Entramado: Encapsular paquetes en encabezados y trailers de la capa de enlace de datos.
19. Dirección MAC (Control de Acceso al Medio): Un identificador de hardware único para las tarjetas de interfaz de red.
20. Mecanismos de Detección de Errores: Verificación de paridad, CRC (Comprobación de Redundancia Cíclica), sumas de comprobación.
21. Conceptos Básicos de Ethernet: La tecnología LAN más común; utiliza una estructura de trama con MAC de origen/destino.
22. Formato de Trama Ethernet: Preámbulo, MAC de destino, MAC de origen, tipo/longitud, carga útil, CRC.
23. Conmutación: Reenvío de tramas utilizando tablas de direcciones MAC en una LAN.
24. Proceso de Aprendizaje en Switches: Construir una tabla de direcciones MAC a medida que los dispositivos se comunican.
25. VLAN (Red de Área Local Virtual): Segmentar lógicamente una LAN física en múltiples redes virtuales.
26. Propósito de la Capa de Red: Enrutamiento, direccionamiento lógico (IP) y determinación de ruta.
27. Formato de Dirección IPv4: Dirección de 32 bits, típicamente representada en notación decimal punteada.
28. Clases IPv4 (Obsoletas): Clase A, B, C, D, E (contexto histórico, reemplazado por CIDR).
29. CIDR (Enrutamiento Inter-Dominio sin Clases): Enfoque moderno para una asignación de direcciones IP más flexible.
30. IPv4 vs. IPv6: Diferencias clave (direccionamiento de 128 bits, formato de encabezado expandido, auto-configuración).
31. Subnetting: Dividir una red grande en subredes más pequeñas para un uso eficiente de direcciones.
32. NAT (Traducción de Dirección de Red): Mapear direcciones IP privadas a una IP pública para conservar direcciones IPv4.
33. ARP (Protocolo de Resolución de Direcciones): Resuelve direcciones IP a direcciones MAC dentro de una LAN.
34. ICMP (Protocolo de Mensajes de Control de Internet): Herramienta de diagnóstico—utilizado por ping, traceroute.
35. Enrutamiento vs. Conmutación: El enrutamiento es a nivel IP (Capa 3), mientras que la conmutación es a nivel MAC (Capa 2).
36. Enrutamiento Estático: Configurar manualmente las rutas en la tabla de enrutamiento de un router.
37. Protocolos de Enrutamiento Dinámico: RIP (Protocolo de Información de Enrutamiento), OSPF (Primero la Ruta Más Corta), BGP (Protocolo de Pasarela de Frontera).
38. Conceptos Básicos de Router: Determina el siguiente salto de red para un paquete basándose en direcciones IP.
39. Propósito de la Capa de Transporte: Entrega de datos de extremo a extremo, fiabilidad y control de flujo.
40. TCP (Protocolo de Control de Transmisión): Protocolo orientado a la conexión que proporciona transferencia de datos fiable.
41. Estructura del Segmento TCP: Puerto de origen, puerto de destino, número de secuencia, número de acuse de recibo, etc.
42. Handshake de Tres Vías de TCP: Proceso SYN, SYN-ACK, ACK para el establecimiento de conexión.
43. Cierre de Conexión de Cuatro Vías de TCP: Secuencia FIN, FIN-ACK, ACK para cerrar una conexión.
44. Control de Flujo TCP: Mecanismos como ventana deslizante para gestionar las tasas de transferencia de datos.
45. Control de Congestión TCP: Algoritmos (inicio lento, evitación de congestión, recuperación rápida, retransmisión rápida).
46. UDP (Protocolo de Datagramas de Usuario): Sin conexión, sobrecarga mínima, sin garantía de entrega.
47. Estructura del Segmento UDP: Puerto de origen, puerto de destino, longitud, suma de comprobación, datos.
48. Números de Puerto: Identificadores para servicios (por ejemplo, 80 para HTTP, 443 para HTTPS, 53 para DNS).
49. Socket: Combinación de una dirección IP y un puerto utilizado para identificar un endpoint.
50. Propósito de la Capa de Aplicación: Proporciona servicios de red a las aplicaciones de usuario.
51. HTTP (Protocolo de Transferencia de Hipertexto): La base de la comunicación de datos en la web.
52. Métodos HTTP: GET, POST, PUT, DELETE, HEAD, etc.
53. HTTPS: HTTP cifrado usando TLS/SSL para comunicación web segura.
54. DNS (Sistema de Nombres de Dominio): Asigna nombres de dominio (por ejemplo, example.com) a direcciones IP.
55. Proceso de Resolución DNS: Consultas recursivas e iterativas, servidores raíz, servidores TLD, servidores autoritativos.
56. FTP (Protocolo de Transferencia de Archivos): Protocolo heredado para transferencias de archivos sobre TCP (puertos 20/21).
57. Protocolos de Correo Electrónico: SMTP (Enviar), POP3 e IMAP (Recuperar).
58. DHCP (Protocolo de Configuración Dinámica de Host): Asigna automáticamente direcciones IP a los dispositivos.
59. Telnet vs. SSH: Protocolos de acceso remoto—SSH está cifrado, Telnet no.
60. Modelo Cliente-Servidor: Una arquitectura común donde un cliente solicita servicios a un servidor.
61. Modelo P2P (Peer-to-Peer): Cada nodo puede tanto solicitar como proporcionar servicios.
62. Tecnologías Web: URLs, URIs, cookies, sesiones, estructura básica de aplicaciones web.
63. Principios de Seguridad de Red: Confidencialidad, integridad, disponibilidad (tríada CIA).
64. Amenazas de Seguridad Comunes: Malware (virus, gusanos, troyanos), ataques DDoS, phishing, inyección SQL.
65. Firewalls: Filtra el tráfico basándose en reglas, ubicado en los límites de la red.
66. IDS/IPS (Sistemas de Detección/Prevención de Intrusiones): Monitorea el tráfico en busca de actividades sospechosas.
67. VPN (Red Privada Virtual): Túnel cifrado sobre una red pública, asegurando conexiones remotas.
68. TLS/SSL (Seguridad de la Capa de Transporte / Capa de Socket Segura): Cifrado para la transferencia segura de datos.
69. Conceptos Básicos de Criptografía: Cifrado simétrico vs. asimétrico, intercambio de claves, firmas digitales.
70. Certificados Digitales: Proporcionados por CAs (Autoridades de Certificación) para validar la identidad y permitir HTTPS.
71. Políticas de Seguridad de Red: Directrices que rigen el uso seguro de la red, controles de acceso y auditoría.
72. DMZ (Zona Desmilitarizada): Una subred que expone servicios externos al público.
73. Seguridad WLAN: Redes inalámbricas (Wi-Fi) aseguradas por WPA2, WPA3, etc.
74. Seguridad Física: Asegurar que la infraestructura de red (servidores, cables, routers) esté alojada de forma segura.
75. Ingeniería Social: Tácticas de intrusión no técnicas—phishing, pretexting, baiting.
76. Ataques a Capas OSI: Diferentes amenazas/defensas en cada capa (por ejemplo, suplantación ARP en la capa de enlace de datos).
77. Herramientas de Administración de Red: ping, traceroute, netstat, nslookup, dig.
78. Analizadores de Paquetes: Herramientas como Wireshark o tcpdump para analizar el tráfico a nivel de paquete.
79. Protocolos de Gestión de Red: SNMP (Protocolo Simple de Gestión de Red).
80. Registro y Monitoreo: Syslog, registros de eventos, soluciones SIEM para detección en tiempo real.

81. Configuración Básica de LAN: Determinar rangos de IP, máscaras de subred, puerta de enlace, servidores DNS.
82. Tipos de Cable: CAT5, CAT5e, CAT6, fibra óptica, cuándo se usa cada uno típicamente.
83. Cableado Estructurado: Estándares para instalaciones de red profesionales a gran escala.
84. Configuración de Switch: Crear VLANs, puertos troncales y protocolos de árbol de expansión.
85. Configuración de Router: Configurar rutas (estáticas/dinámicas), NAT, ACL (Listas de Control de Acceso).
86. Reglas Básicas de Firewall: Denegar todo el tráfico entrante excepto el requerido, permitir todo el saliente o limitar según sea necesario.
87. Planes de Direccionamiento de Red: Asignar direcciones IP de manera eficiente basándose en departamentos o subredes.
88. Redundancia y Conmutación por Error: Usar enlaces de respaldo, balanceo de carga o VRRP/HSRP para alta disponibilidad.
89. QoS (Calidad de Servicio): Priorizar cierto tráfico (por ejemplo, VoIP) para garantizar el rendimiento.
90. Conceptos Básicos de Redes en la Nube: Redes virtuales, grupos de seguridad, balanceadores de carga en entornos cloud.
91. SDN (Redes Definidas por Software): Separar el plano de control del plano de datos para una gestión centralizada.
92. Virtualización: Usar hipervisores (VMware, Hyper-V, KVM) para crear servidores/redes virtuales.
93. Contenedores y Microservicios: Redes Docker, conceptos de redes en Kubernetes.
94. Implementación de IPv6: Pila dual (IPv4/IPv6), auto-configuración IPv6 (SLAAC), túneles IPv6.
95. Balanceo de Carga con DNS: Distribuir tráfico a través de múltiples servidores mediante round robin de DNS.
96. Computación en el Borde: Procesamiento en el borde de la red para reducir la latencia para IoT y servicios en tiempo real.
97. 5G y Evolución Inalámbrica: Mayores tasas de datos, menor latencia, uso en IoT y banda ancha móvil.
98. Pasos para la Resolución de Problemas de Red: Identificar el problema, aislar, probar hipótesis, corregir, verificar.
99. Documentación: Importancia de mantener diagramas de red y configuraciones de dispositivos precisos.
100. Aprendizaje Continuo: Las redes están en constante evolución, requiriendo estudio continuo de nuevos protocolos y mejores prácticas.

Estos 100 puntos resumen los temas esenciales en redes informáticas, abarcando teoría fundamental, protocolos, hardware, direccionamiento, seguridad y tendencias modernas. Deberían ayudar a guiar tu repaso y estudio para exámenes o la comprensión práctica de las redes informáticas.