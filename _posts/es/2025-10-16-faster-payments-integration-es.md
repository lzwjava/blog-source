---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Pautas de Integración del Sistema de Pagos Rápidos
translated: true
type: note
---

El sistema de pago más rápido (FPS) en Hong Kong, operado por Hong Kong Interbank Clearing Limited (HKICL) bajo la supervisión de la Autoridad Monetaria de Hong Kong (HKMA), no proporciona un SDK disponible públicamente para que los bancos integren. La integración se maneja mediante conectividad directa a la infraestructura FPS, con especificaciones técnicas compartidas de forma privada con los bancos participantes (conocidos como Settlement Participants) durante el proceso de incorporación. Estas especificaciones guían a los bancos en la mejora de sus sistemas para el acceso, pero no se mencionan SDK listos para usar o kits de desarrollo en la documentación oficial.

Con respecto a las APIs, el FPS en sí mismo actualmente no ofrece APIs dedicadas para integración externa o de terceros. Sin embargo, se alinea con el Marco de API Abierta más amplio de la HKMA para el Sector Bancario de Hong Kong (introducido en 2018 y actualizado a través de fases hasta 2025), que alienta a los bancos a exponer ciertas funciones a través de APIs para proveedores de servicios de terceros (por ejemplo, para información de cuentas o iniciación de pagos). Las transacciones FPS pueden aprovechar este marco indirectamente para funciones como la iniciación de pagos, pero aún no hay APIs específicas para FPS disponibles; el acceso sigue restringido sobre una base de necesidad de conocer por razones de seguridad y regulatorias. La HKMA continúa monitoreando y puede expandir el soporte de APIs en el futuro.

### Detalles Clave de Integración para Bancos
- **Métodos de Conectividad**: Los bancos se conectan en modo tiempo real a través de mensajería IBM MQ para procesamiento instantáneo o en modo lote a través de transferencias de archivos (por ejemplo, a través de la red segura ICLNET de HKICL). El sistema funciona las 24 horas, los 7 días de la semana.
- **Estándares de Mensajería**: Todas las comunicaciones utilizan el formato ISO 20022, que admite datos enriquecidos, caracteres chinos e interoperabilidad.
- **Proceso de Incorporación**: Los bancos se inscriben con la HKMA (para HKD) o con el Bank of China (Hong Kong) para RMB, firman acuerdos de Reglas FPS, adaptan sus sistemas a las especificaciones proporcionadas, se someten a pruebas de HKICL y entran en funcionamiento. Todos los bancos con licencia deben participar como liquidantes directos.
- **Otras Características**: Admite IDs proxy (por ejemplo, teléfono/correo electrónico), códigos QR (estándar EMV) y transferencias multi-moneda (HKD/RMB). La autenticación sigue las pautas de dos factores de la HKMA, y los bancos establecen sus propios límites de transacción.

Para obtener especificaciones técnicas detalladas, los bancos deben contactar a HKICL directamente una vez inscritos, ya que no están disponibles para descarga pública.

[Sistema de Pago Más Rápido (FPS) - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/financial-market-infrastructure/faster-payment-system-fps/)  
[Documentación del Esquema - HKICL FPS](https://fps.hkicl.com.hk/eng/fps/about_fps/scheme_documentation.php)  
[Estudio de Caso del Banco Mundial sobre FPS: Hong Kong](https://fastpayments.worldbank.org/sites/default/files/2021-09/World_Bank_FPS_Hong_Kong_SAR_China_FPS_Case_Study.pdf)  
[Marco de API Abierta para el Sector Bancario - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/fintech/open-application-programming-interface-api-for-the-banking-sector/)