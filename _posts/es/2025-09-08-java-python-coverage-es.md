---
audio: false
date: 2025-09-08
generated: true
image: false
lang: es
layout: post
title: Cobertura Java Multi-módulo con Python
translated: true
type: note
---

Al analizar tu configuración, estás enfrentando un desafío complejo pero interesante: usar pruebas de integración de Python para generar cobertura en un proyecto Java multi-módulo. Permíteme analizar la situación y sugerir una estrategia integral.

## Desafíos Actuales

1. **Pruebas entre lenguajes**: Tests de Python ejecutando código Java
2. **Cobertura multi-módulo**: Necesidad de capturar cobertura en todos los módulos desde las pruebas de integración
3. **Interdependencias de módulos**: `PlaygroundUtils` no tiene endpoints directos pero se ejecuta a través de `PlaygroundWeb`
4. **Preocupación sobre escalabilidad**: Cómo manejar esto para 10+ módulos

## Estrategia Recomendada

### Opción 1: Agente Único de JaCoCo, Reporte Combinado (Recomendado)

Este es el enfoque más escalable para tu caso de uso:

## Mejoras Clave y Estrategia

### 1. **Enfoque de Agente Único de JaCoCo**
- Usar UN archivo `jacoco-it.exec` en el nivel padre
- Configurar el agente con `append=true` e `includes=org.lzw.*`
- Esto captura TODA la cobertura de módulos en una sola ejecución

### 2. **Agregación de Reportes**
- Usar `jacoco:report-aggregate` para crear un reporte unificado
- Esto automáticamente encuentra todas las clases de los módulos y genera cobertura para ellas

### 3. **Ejecución Basada en Perfiles**
- Separar responsabilidades: perfil `run-integration-tests` para ejecutar tests
- Perfil `integration-test-coverage` para generar reportes
- Hace el build más modular y mantenible

### 4. **Escalabilidad para 10+ Módulos**

Para proyectos más grandes, considera este enfoque mejorado:

## Resumen y Mejores Prácticas

### Para tu Configuración Actual de 2 Módulos:
1. **Usa un único archivo exec de JaCoCo** en el nivel padre con `append=true`
2. **Ejecuta Jetty una vez** con el agente configurado para capturar todos los módulos
3. **Usa `report-aggregate`** para generar un reporte unificado

### Para Escalar a 10+ Módulos:
1. **Agrupación de Módulos**: Crear grupos lógicos (core, service, web) y generar reportes separados
2. **Seguimiento de Cobertura**: Implementar un helper en Python para rastrear qué módulos están cubiertos
3. **Pruebas Paralelas**: Ejecutar diferentes suites de pruebas en paralelo para feedback más rápido
4. **Cobertura Incremental**: Usar perfiles de Maven para ejecutar cobertura para grupos específicos de módulos

### Puntos Clave de Configuración:
- **`append=true`**: Asegura que múltiples ejecuciones de pruebas acumulen cobertura
- **`includes=org.lzw.*`**: Captura todos tus módulos en un solo agente
- **Separación de perfiles**: Mantener las pruebas de integración separadas de los builds regulares
- **Archivo exec único**: Elimina la necesidad de ejecutar Jetty múltiples veces

### Uso desde Línea de Comandos:
```bash
# Cobertura completa con pruebas de integración
mvn clean verify -Prun-integration-tests,integration-test-coverage

# Solo cobertura de pruebas unitarias
mvn clean test

# Cobertura para grupo específico de módulos
mvn clean verify -Pcoverage-by-layer
```

Este enfoque escala bien porque:
1. Solo inicias/detienes Jetty una vez sin importar el número de módulos
2. JaCoCo maneja automáticamente archivos de clase multi-módulo
3. Las pruebas de Python no necesitan conocer la estructura de módulos de Java
4. Los reportes pueden agregarse o dividirse según sea necesario para diferentes audiencias

La idea clave es que el agente de JaCoCo puede capturar cobertura para TODAS las clases en la JVM, no solo el módulo que se está probando. Al usar un archivo exec compartido y el goal aggregate, obtienes datos de cobertura completos en una sola ejecución de pruebas.