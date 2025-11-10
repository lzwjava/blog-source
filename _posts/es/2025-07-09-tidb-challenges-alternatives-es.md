---
audio: false
generated: true
lang: es
layout: post
title: Desafíos de TiDB y Alternativas para 2025
translated: true
type: note
---

Los desafíos de diseño de TiDB surgen de intentar implementar los conceptos de Google Spanner y F1 sin el hardware especializado que los hace prácticos. Estos son los problemas clave:

## Problemas de Diseño Centrales

**Dependencia del Hardware**: TiDB utiliza "el Asignador de Timestamps introducido en Percolator", pero "si hay múltiples centros de datos, especialmente si estos DCs están distribuidos geológicamente, la latencia es muy alta" porque carece del hardware especializado de reloj atómico de Google (TrueTime) que hace que el diseño de Spanner funcione de manera eficiente.

**Sobrecarga de Recursos**: La naturaleza distribuida de TiDB requiere más recursos en comparación con las bases de datos relacionales tradicionales, necesitando múltiples componentes (servidores TiDB, servidores PD, nodos TiKV) en máquinas separadas, lo que aumenta los costos de hardware y operativos.

**Complejidad Operativa**: Es un desafío solucionar problemas en una base de datos distribuida porque la información sobre el sistema está dispersa en diferentes máquinas.

## Qué Está Usando la Gente en su Lugar en 2025

Según los resultados de la búsqueda, las organizaciones están eligiendo varias alternativas:

**Soluciones Cloud-Native**: Muchos se están trasladando a servicios completamente gestionados como Google Cloud SQL, Amazon Aurora y otros servicios de base de datos en la nube que manejan la complejidad operativa.

**Casos de Uso Especializados**: Algunas empresas como Plaid todavía están en transición a TiDB para mediados de 2025, pero están lidiando con desafíos de migración significativos, incluida la eliminación de claves externas y la aplicación de claves primarias para la compatibilidad.

**Enfoques Tradicionales con Sharding**: Muchas organizaciones están volviendo a estrategias probadas de sharding con MySQL/PostgreSQL con mejores herramientas en lugar de lidiar con la complejidad de SQL distribuido.

**Alternativas Modernas**: Las empresas están explorando otras bases de datos distribuidas como CockroachDB, YugabyteDB, o soluciones específicas que no intentan replicar la arquitectura de Spanner sin su base de hardware.

El problema fundamental es que TiDB intentó recrear los beneficios de Spanner sin la infraestructura especializada de Google, lo que lleva a una mayor latencia, mayor complejidad y sobrecarga operativa que a menudo supera los beneficios de escalado para la mayoría de los casos de uso.