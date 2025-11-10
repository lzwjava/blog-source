---
audio: false
generated: true
image: false
lang: es
layout: post
title: Relaciones de Modelo, No Datos
translated: true
type: note
---

Tienes toda la razón: las relaciones "uno a uno, uno a muchos, muchos a muchos" están en todas partes: familias, equipos, pagos; clases, repositorios, pull requests. Aquí tienes una guía compacta para **establecer relaciones** de modo que los diseños se mantengan simples y se ajusten a cómo se usan las cosas.

# Una guía práctica de modelado

## 1) Comienza desde el comportamiento, no desde los datos

*   Escribe las **5 principales tareas del usuario** ("hacer un pedido", "aprobar un gasto", "asignar un revisor").
*   Debajo de cada tarea, enumera los **sustantivos** (entidades) y los **verbos** (relaciones/acciones).
*   Mantén solo las relaciones que **cambian los resultados** en esas tareas; todo lo demás son metadatos.

## 2) Decide primero la propiedad y los límites

*   Pregunta: *¿Quién posee el ciclo de vida de quién?*
    *   Si A no puede existir sin B → A es **parte de** B (composición).
    *   Si A y B viven independientemente → relación de **referencia**.
*   Usa **contextos delimitados**: el mismo "Cliente" puede ser diferente en Facturación vs. Marketing. No forces un megamodelo único.

## 3) Elige la **cardinalidad más simple** que funcione

*   Prefiere **1→1** solo cuando dos registros sean operacionalmente inseparables pero necesiten diferente seguridad o volatilidad (ej., Usuario ↔ Credenciales).
*   Prefiere **1→N** cuando haya una propiedad clara y un acceso frecuente del padre a los hijos (Pedido → LíneasDePedido).
*   Usa **M↔N** solo cuando ambos lados sean pares y la vinculación sea un concepto de negocio propio (Estudiante ↔ Curso mediante "Matrícula" que tiene nota, estado, fechas).

## 4) Haz las relaciones explícitas con invariantes

Para cada relación, escribe invariantes en lenguaje sencillo:

*   **Cardinalidad**: "Un usuario tiene como máximo un email principal."
*   **Opcionalidad**: "Una factura debe tener ≥1 línea de artículo."
*   **Temporal**: "La membresía es válida durante \[inicio, fin)."
*   **Unicidad**: "Un código de producto es único por inquilino."
    Estos se convierten directamente en restricciones, índices y verificaciones.

## 5) Patrones de modelado por cardinalidad (sin tablas 😉)

### Uno a uno

*   Úsalo al dividir campos volátiles/seguros o cuando una entidad crece de forma modular.
*   Impónlo con una clave única en la clave foránea.
*   Considera **incrustar** (documentos) si siempre se lee junto.

### Uno a muchos

*   Si los hijos nunca se mueven entre padres → mantén la **clave del padre** en el hijo; cascada de eliminaciones como política.
*   Si ocurre reasignación de padre → permite FK anulable + regla de negocio para transiciones.
*   Si las lecturas son centradas en el padre → desnormaliza campos de resumen en el padre (recuentos, última_actualización).

### Muchos a muchos

*   Promueve el enlace a una **entidad de primera clase** (Matrícula, Membresía, Asignación).
*   Pon los **datos de negocio** en el enlace (rol, prioridad, peso, marcas de tiempo).
*   Si el enlace no tiene atributos y es enorme, elige el almacenamiento y los índices para las consultas del lado más pesado.

## 6) Elige el almacenamiento según los patrones de acceso

*   **Relacional**: mayor integridad, uniones complejas, reporting.
*   **Documento**: agregado primero, flujos de lectura centrados en el padre, actualizaciones localizadas.
*   **Grafo**: consultas de ruta, recomendaciones, herencia de permisos, recorridos de profundidad variable.
    Elige uno **por contexto delimitado**; sincroniza mediante eventos, no tablas compartidas.

## 7) La superficie de la API refleja las relaciones—intencionadamente

*   Los **agregados** se convierten en los recursos principales de la API.
*   Las **colecciones hijas** como rutas anidadas (ej., `/pedidos/{id}/articulos`).
*   Las **entidades de unión** obtienen su propio recurso cuando importan (`/matriculas`).
*   Para flexibilidad del cliente, expón **GraphQL** solo cuando el dominio sea similar a un grafo o los clientes varíen mucho; de lo contrario, mantén REST simple.

## 8) Mantenlo evolucionable (temporal + cambio suave)

*   Rastrea el **tiempo válido** en enlaces importantes (`valido_desde`, `valido_hasta`), no solo `actualizado_el`.
*   Prefiere **eliminaciones suaves** en las filas de relación para poder reconstruir el historial.
*   Usa **IDs sustitutivos** para todas las entidades y filas de enlace; nunca incrustes significado en los IDs.

## 9) Simplifica agresivamente

*   Fusiona entidades si los usuarios nunca perciben la diferencia.
*   Colapsa divisiones 1→1 cuando desaparezcan las razones de seguridad/rendimiento.
*   Reemplaza redes M↔N amplias con una **jerarquía** si las reglas de negocio tienen forma de árbol.
*   Introduce **roles** en lugar de múltiples tipos de enlace (ej., una Membresía con rol=propietario/visor en lugar de enlaces separados).

## 10) Investiga a la inversa (ingeniería inversa) un enredo existente

*   Mapea las **consultas reales** (registros lentos, dashboards). Mantén solo las relaciones utilizadas por ≥1 consulta crítica.
*   Dibuja **mapas de contexto**: qué equipo/sistema posee qué entidades y quién consume qué eventos.
*   Identifica **uniones calientes** → desnormaliza, almacena en caché o conviértelas en agregados.
*   Eleva enlaces M↔N ruidosos a **conceptos de primera clase** con invariantes claros.
*   Añade **contratos**: restricciones, pruebas y linters para el esquema y la API para prevenir la desviación.

# Errores comunes a evitar

*   Tratar M↔N como "solo una tabla de unión" cuando en realidad es el corazón del negocio (ej., permisos, asignaciones).
*   Sobre-normalizar rutas de lectura que necesitan baja latencia; arréglalo con **modelos de lectura** (CQRS) o vistas materializadas.
*   Sub-especificar la opcionalidad: `NULL` explota la complejidad. Prefiere estados explícitos "Desconocido/NoAplicable" cuando sea significativo.
*   Ignorar el **multitenencia**: siempre delimita la unicidad y las consultas por inquilino desde el principio.
*   Olvidar la **direccionalidad**: "sigue a" vs "amigos" no es lo mismo.

# Una lista de verificación ligera que puedes reutilizar

*   ¿Cuáles son las principales tareas y sus métricas de éxito?
*   ¿Cuáles son los agregados (propiedad/ciclo de vida)?
*   ¿Cuáles son los invariantes (cardinalidad, opcionalidad, temporal, unicidad)?
*   ¿Qué relaciones llevan atributos de negocio (promover a entidades)?
*   ¿Qué patrones de acceso dominan (elegir almacenamiento/índices en consecuencia)?
*   ¿Qué simplificaciones son seguras hoy (fusionar/dividir/desnormalizar)?
*   ¿Qué contratos hacen cumplir esto (restricciones, pruebas de API, esquemas de eventos)?

Si quieres, dame una pequeña porción de tu dominio (tres entidades + la tarea principal del usuario), y esbozaré las relaciones, invariantes y una forma de almacenamiento/API que puedas implementar directamente.