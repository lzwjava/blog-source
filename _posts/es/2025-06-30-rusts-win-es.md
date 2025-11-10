---
audio: false
generated: true
lang: es
layout: post
title: Mejora de Rendimiento de Rust en Discord
translated: true
type: note
---

La adopción de Rust por parte de Discord fue impulsada por los cuellos de botella de rendimiento en su servicio "Read States" basado en Go, que realiza un seguimiento de los mensajes leídos por los usuarios en todos los canales. El cambio a Rust produjo mejoras significativas en la latencia, eliminó los picos de recolección de basura y mostró las fortalezas de Rust en la gestión de memoria y la concurrencia. Aquí hay un desglose detallado:

---

### **Por qué Discord Cambió a Rust**
1.  **Problemas de Recolección de Basura (GC) en Go**
    - El servicio de Go de Discord experimentaba picos de latencia cada ~2 minutos debido al GC conservador y no generacional de Go, que *tenía que escanear toda la caché LRU* (que contenía millones de objetos) incluso con una producción mínima de basura.
    - Ajustar el GC de Go (por ejemplo, modificando el tamaño de la caché) no logró resolver los picos o empeoró la latencia del percentil 99.

2.  **Gestión de Memoria de Rust**
    - El modelo de propiedad de Rust *libera la memoria inmediatamente* tras la expulsión de la caché LRU, evitando las pausas inducidas por el GC. Este enfoque determinista eliminó los picos de latencia.
    - La ausencia de sobrecarga de GC en tiempo de ejecución significó un rendimiento consistente bajo carga alta (cientos de miles de actualizaciones/seg).

3.  **Optimización del Rendimiento**
    - Incluso una implementación ingenua de Rust igualó el rendimiento de Go. Optimizaciones posteriores (por ejemplo, usar `BTreeMap` en lugar de `HashMap`, reducir las copias de memoria) *redujeron el uso de la CPU en un 70%* y recortaron los tiempos de respuesta promedio a microsegundos.

4.  **Ecosistema y Soporte Async**
    - Discord adoptó tempranamente las funciones async nightly de Rust (posteriormente estabilizadas), permitiendo servicios en red eficientes sin las concesiones del GC.

---

### **Resultados del Cambio**
- **Latencia**: Se eliminaron los picos de GC de 2 minutos, logrando tiempos de respuesta submilisegundos.
- **Eficiencia de Recursos**: Se redujo el uso de CPU y memoria, permitiendo que la capacidad de la caché escalara a 8 millones de estados de lectura sin degradación del rendimiento.
- **Confiabilidad**: Menos errores en tiempo de ejecución gracias a las comprobaciones de seguridad en tiempo de compilación de Rust.

---

### **Ventajas de Rust para Discord**
1.  **Rendimiento**
    - Latencia baja predecible, ideal para servicios en tiempo real.
    - El control granular de la memoria supera a los lenguajes dependientes de GC.

2.  **Seguridad**
    - El modelo de propiedad previene fugas de memoria, punteros nulos y carreras de datos.
    - Seguridad en concurrencia sin sincronización manual.

3.  **Herramientas Modernas**
    - Cargo (gestor de paquetes) y genéricos ricos redujeron el código repetitivo en comparación con Go.

4.  **Crecimiento del Ecosistema**
    - Las actualizaciones (por ejemplo, el runtime async Tokio) proporcionaron mejoras de rendimiento gratuitas.

---

### **Desventajas y Desafíos**
1.  **Curva de Aprendizaje**
    - La propiedad y los tiempos de vida de Rust requieren una inversión inicial.

2.  **Limitaciones Iniciales de Async**
    - La dependencia inicial de funciones nightly inestables supuso riesgos de mantenimiento.

3.  **Ecosistema Más Pequeño**
    - Menos bibliotecas en comparación con Go o C++, aunque está creciendo rápidamente.

---

### **Conclusiones Clave**
El éxito de Discord con Rust subraya su idoneidad para *servicios de alta escala y sensibles a la latencia* donde las pausas de GC son inaceptables. Si bien la transición requirió superar la pronunciada curva de aprendizaje de Rust, la recompensa incluyó **un rendimiento más rápido, un menor uso de recursos y menos errores en tiempo de ejecución**. Para los equipos que priorizan la mantenibilidad y el rendimiento a largo plazo, Rust ofrece ventajas convincentes sobre lenguajes dependientes de GC como Go.

Para obtener información técnica más profunda, consulta la [publicación de blog original de Discord](https://discord.com/blog/why-discord-is-switching-from-go-to-rust).