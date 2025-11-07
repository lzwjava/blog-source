---
audio: false
generated: true
image: false
lang: es
layout: post
model: moonshotai/kimi-k2-thinking
title: Reversión de Transacciones y Detección de Errores en DB2
translated: true
---

## Cuando DB2 Realiza Rollback Debido a Errores del Sistema

IBM DB2 revierte automáticamente las transacciones cuando encuentra errores críticos del sistema que amenazan la integridad de los datos. Los escenarios comunes incluyen:

- **Deadlocks o timeouts**: SQLCODE -911 con SQLSTATE 40001, el código de razón "2" indica que la transacción se revirtió debido a un deadlock
- **Process abend (finalización anormal)**: En todos los entornos DB2, la terminación del proceso desencadena un rollback implícito
- **Fallos de recursos del sistema**: Fallos de memoria, disco o red que impiden la finalización de la transacción
- **Conflictos de timestamp**: SQLCODE -818 ocurre cuando las marcas de tiempo internas no coinciden entre el módulo y el DBRM
- **Redes de seguridad de connection pooling**: Algunas implementaciones revierten automáticamente las conexiones cuando se liberan para evitar que las transacciones no confirmadas causen problemas de bloqueo

## Cómo Detectar Información Detallada del Error

### 1. Mecanismos Principales de Detección de Errores

**SQLCODE y SQLSTATE**
Después de cada sentencia SQL, DB2 establece estas variables:

```sql
-- Verificar inmediatamente después de la ejecución de la sentencia
IF SQLCODE < 0 THEN
    -- Ocurrió un error
    ROLLBACK;
END IF;
```

Los códigos de clase SQLSTATE identifican específicamente los tipos de error:
- **Clase 58**: Error del sistema (ej. recurso no disponible, intervención del operador)
- **Clase 40**: Rollback de transacción
- **Clase 25**: Estado de transacción no válido

**Sentencia GET DIAGNOSTICS**
Para obtener información detallada del error en stored procedures de SQL PL:

```sql
DECLARE v_sqlcode INTEGER;
DECLARE v_sqlstate CHAR(5);
DECLARE v_sqlmessage VARCHAR(256);

GET DIAGNOSTICS CONDITION 1
    v_sqlcode = DB2_RETURNED_SQLCODE,
    v_sqlstate = RETURNED_SQLSTATE,
    v_sqlmessage = MESSAGE_TEXT;
```

### 2. Detección de Errores en Línea de Comandos

Al ejecutar scripts mediante la línea de comandos `db2`, verificar los códigos de salida:

- **Código de salida 8**: Error del sistema
- **Código de salida 4**: Error de DB2 (violación de restricción, objeto no encontrado)
- **Código de salida 2**: Advertencia de DB2
- **Código de salida 1**: No se encontraron filas

**Patrón de script recomendado**:
```bash
db2 -l migration.log +c -stf migration.sql
if [ $? -ge 4 ]; then
    db2 rollback
    tail -10 migration.log  # Revisar el error detallado
else
    db2 commit
fi
```

### 3. Manejo de Errores en Stored Procedures

Para una detección integral de errores en SQL PL, usar handlers declarados:

```sql
CREATE PROCEDURE my_procedure()
BEGIN
    DECLARE v_sqlcode INTEGER DEFAULT 0;
    DECLARE v_sqlstate CHAR(5) DEFAULT '00000';
    DECLARE v_error_message VARCHAR(256);
    
    -- Declarar exit handler para cualquier excepción
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            v_sqlcode = DB2_RETURNED_SQLCODE,
            v_sqlstate = RETURNED_SQLSTATE,
            v_error_message = MESSAGE_TEXT;
            
        -- Registrar detalles del error en tabla o archivo
        INSERT INTO error_log (sqlcode, sqlstate, message, timestamp)
        VALUES (v_sqlcode, v_sqlstate, v_error_message, CURRENT_TIMESTAMP);
        
        ROLLBACK;
    END;
    
    -- Su lógica transaccional aquí
    UPDATE employee SET salary = salary + 1000 WHERE job = 'MANAGER';
    INSERT INTO audit_log VALUES (CURRENT_TIMESTAMP, 'Salary update');
    
    COMMIT;
END
```

### 4. Archivos de Log de Diagnóstico de DB2

Para errores a nivel del sistema, verificar siempre:

- **db2diag.log**: Log de diagnóstico principal con información detallada de errores del sistema
- **Notification log**: Contiene resúmenes de errores
- **Logs de línea de comandos**: Usar la opción `-l logfile.txt` para capturar errores

## Mejores Prácticas para la Detección de Errores

1. **Verificar siempre SQLCODE/SQLSTATE inmediatamente** después de operaciones críticas
2. **Usar GET DIAGNOSTICS** para un contexto de error enriquecido en stored procedures
3. **Implementar monitoreo del porcentaje de rollback de transacciones**: cualquier valor superior al 1% justifica una investigación
4. **Habilitar opciones de comando** para la ejecución de scripts:
   ```bash
   db2 +c -s -v -l error.log -f script.sql
   ```
   Donde `+c` desactiva el autocommit y `-s` se detiene en error
5. **Usar savepoints** para rollbacks parciales dentro de transacciones complejas
6. **Registrar detalles del error** en tablas persistentes antes del rollback para preservar la información de diagnóstico

## SQLSTATEs de Error del Sistema Clave para Monitorear

| SQLSTATE | Descripción | Acción |
|----------|-------------|--------|
| **58004** | Error del sistema (varias causas) | Revisar db2diag.log inmediatamente |
| **58008** | Error de comunicación | Verificar red/conectividad |
| **HY000** | Error general del driver | Revisar logs del driver ODBC/JDBC |
| **40001** | Deadlock/timeout | Reintentar transacción con backoff |

Para entornos de producción, las herramientas de monitoreo deben alertar sobre **SQLCODE < 0** y **SQLSTATEs de Clase 58** para detectar proactivamente problemas a nivel del sistema antes de que se propaguen.