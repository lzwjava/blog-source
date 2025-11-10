---
audio: false
generated: true
lang: es
layout: post
title: Construcción de Sistemas NL a SQL Precisos y Seguros
translated: true
type: note
---

### Áreas clave de enfoque al construir un sistema de lenguaje natural a SQL

Construir un sistema de lenguaje natural a SQL (NL-to-SQL) implica traducir consultas de usuarios en lenguaje cotidiano a sentencias SQL ejecutables, a menudo utilizando modelos de IA como LLMs (por ejemplo, variantes de GPT o modelos especializados como los de Hugging Face). Basándonos en tu esquema de PostgreSQL y consulta de ejemplo, aquí están las áreas principales en las que enfocarse:

#### 1. **Precisión y Comprensión del Esquema**
   - **Conciencia del Esquema**: Proporciona siempre el esquema completo de la base de datos (tablas, columnas, tipos de datos, relaciones) en el prompt de IA. Esto ayuda al modelo a generar SQL correcto. En tu caso, enfatiza columnas como `first_name`, `created_at`, `date_of_birth` y `last_login` para evitar alucinaciones (por ejemplo, inventar campos inexistentes).
   - **Manejo de la Ambigüedad**: El lenguaje natural es vago—por ejemplo, "alrededor del día del mes pasado" podría significar ±1 día, pero aclara mediante prompts para interpretar términos difusos (por ejemplo, "semana reciente" como 7 días). Usa ejemplos en los prompts para guiar las interpretaciones.
   - **Tipos de Datos y Funciones**: Enfócate en la sintaxis específica de PostgreSQL, como usar `AGE()` para fechas, `ILIKE` para cadenas que no distinguen entre mayúsculas y minúsculas, y la conversión adecuada de tipos (por ejemplo, `CAST(created_at AS DATE)` en tu ejemplo). Entrena o ajusta el modelo en las diferencias de dialectos SQL.
   - **Casos Extremos**: Maneja consultas complejas como joins (si hay múltiples tablas), agregaciones (por ejemplo, COUNT, SUM) o subconsultas. Prueba consultas que involucren campos sensibles como `password_hash` o `account_balance`.

#### 2. **Rendimiento y Optimización**
   - Genera SQL eficiente: Anima al modelo a usar índices (por ejemplo, en `created_at` o `first_name`), limitar resultados (agrega `LIMIT` por defecto) y evitar escaneos completos de tabla.
   - Escalabilidad: Para conjuntos de datos grandes, integra herramientas de optimización de consultas o valida el SQL generado contra un plan de ejecución (explain plan).

#### 3. **Manejo de Errores y Validación**
   - Analiza y valida el SQL generado antes de la ejecución (por ejemplo, usando una librería analizadora de SQL como `sqlparse` en Python).
   - Proporciona respuestas alternativas: Si la consulta no es clara, pide al usuario una aclaración en lugar de generar SQL inválido.

#### 4. **Seguridad y Protección**
   - **Prevención de Inyección SQL**: El riesgo proviene de ejecutar el SQL generado. Nunca concatenes la entrada del usuario directamente en cadenas SQL. En su lugar:
     - Usa **consultas parametrizadas** o sentencias preparadas al ejecutar (por ejemplo, en Python con `psycopg2`: `cursor.execute("SELECT * FROM users WHERE first_name = %s", (name,))`).
     - Instruye a la IA para que genere SQL con marcadores de posición (por ejemplo, `WHERE first_name ILIKE %s`) y vincule los valores por separado.
     - Sanea las entradas de lenguaje natural: Pre-procesa las consultas de los usuarios para eliminar patrones maliciosos (por ejemplo, usando regex para detectar palabras clave de SQL como "DROP" o ";").
     - Limita a solo lectura: Restringe la IA a generar solo consultas SELECT—bloquea DDL (por ejemplo, CREATE/DROP) o DML (por ejemplo, INSERT/UPDATE) mediante instrucciones en el prompt como "Solo genera sentencias SELECT; no modifiques datos".
   - **Control de Acceso a Datos**:
     - **Seguridad a Nivel de Fila (RLS)**: En PostgreSQL, habilita políticas RLS en las tablas (por ejemplo, `ALTER TABLE users ENABLE ROW LEVEL SECURITY; CREATE POLICY user_policy ON users USING (role = current_user);`). Esto asegura que las consultas solo devuelvan filas a las que el usuario tiene acceso.
     - **Vistas y Roles**: Crea vistas restringidas (por ejemplo, `CREATE VIEW safe_users AS SELECT id, username, first_name FROM users;`) y otorga acceso mediante roles de base de datos. La IA debería consultar vistas en lugar de tablas base.
     - **Capa de API**: Envuelve el sistema en una API (por ejemplo, usando FastAPI) que autentique a los usuarios y aplique controles de acceso (por ejemplo, tokens JWT para determinar los roles de usuario).
     - **Ejecución en Sandbox**: Ejecuta las consultas en una base de datos de réplica de solo lectura o en un entorno containerizado (por ejemplo, Docker) para aislarlas de los datos de producción.
     - **Registro de Auditoría**: Registra todo el SQL generado y su ejecución para su monitorización.
   - **Privacidad de Datos**: Evita exponer columnas sensibles (por ejemplo, `password_hash`, `email`) incluyéndolas en una lista negra en los prompts: "No selecciones campos sensibles como password_hash, email a menos que sea explícitamente necesario y esté autorizado."
   - **Límite de Tasa y Cuotas**: Previene el abuso limitando las consultas por usuario/sesión.

#### 5. **Ingeniería de Prompts para una Conversión Controlada**
   - La calidad de NL-to-SQL depende en gran medida de cómo instruyas a la IA. Usa prompts estructurados con estos elementos:
     - **Plantilla de Prompt del Sistema**:
       ```
       Eres un generador experto de SQL para PostgreSQL. Dado el esquema a continuación y una consulta en lenguaje natural, genera una consulta SELECT segura y precisa.

       Esquema:
       [Inserta el esquema completo aquí, por ejemplo, CREATE TABLE users (...)]

       Reglas:
       - Solo genera sentencias SELECT. No INSERT, UPDATE, DELETE o DDL.
       - Usa marcadores de posición parametrizados (por ejemplo, %s) para los valores proporcionados por el usuario para prevenir inyecciones.
       - Maneja las fechas con funciones de PostgreSQL como AGE(), CURRENT_DATE, INTERVAL.
       - Para términos ambiguos (por ejemplo, "alrededor del mes pasado"), interpreta como [regla específica, por ejemplo, ±1 día del mismo día del mes pasado].
       - Limita los resultados a 100 filas a menos que se especifique lo contrario.
       - Si la consulta involucra edad, calcúlala a partir del año actual o del año especificado (por ejemplo, EXTRACT(YEAR FROM AGE(CURRENT_DATE, date_of_birth)) = 20).
       - No selecciones columnas sensibles como password_hash, email.
       - Si no está claro, responde con "Aclara: [pregunta]".

       Consulta del Usuario: [consulta en LN]
       ```
     - **Ejemplos en los Prompts**: Incluye 2-3 ejemplos de pocos shots, como tu consulta proporcionada y el SQL generado, para guiar al modelo.
     - **Cadena de Razonamiento**: Instruye al modelo para que razone paso a paso: "Primero, identifica los filtros clave. Segundo, mapea a las columnas. Tercero, construye la cláusula WHERE".
     - **Ajuste Fino**: Si usas un modelo personalizado, ajústalo en conjuntos de datos como Spider o WikiSQL, aumentados con ejemplos específicos de tu esquema.
     - **Pruebas**: Evalúa con métricas como precisión de ejecución (¿se ejecuta sin errores?) y coincidencia semántica (¿devuelve los resultados esperados?).

#### Posibles Mejoras para tu Consulta de Ejemplo
Aunque no es la pregunta principal, tu SQL generado tiene algunos elementos buenos pero podría ser más seguro/más preciso:
- Usa parámetros: Cambia a `WHERE first_name ILIKE %s` y vincula 'andy'.
- Edad "a partir de 2025": Usa `EXTRACT(YEAR FROM AGE('2025-12-31'::date, date_of_birth)) = 20` para fijarla a un fin de año específico.
- Agrega `ORDER BY last_login DESC LIMIT 10;` por seguridad.

Implementar esto de forma segura requiere una capa de backend (por ejemplo, no ejecutar SQL directamente desde la salida de la IA). Comienza con un script pequeño usando una librería LLM (por ejemplo, LangChain para cadenas NL-to-SQL).

¡Si necesitas ejemplos de código o ayuda con partes específicas (por ejemplo, una implementación en Python), proporciona más detalles!

**Referencias**  
[Documentación de PostgreSQL: Seguridad a Nivel de Fila](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)  
[Tutorial de LangChain NL-to-SQL](https://python.langchain.com/docs/tutorials/sql_qa/)  
[Prevención de Inyección SQL en Python](https://realpython.com/prevent-python-sql-injection/)