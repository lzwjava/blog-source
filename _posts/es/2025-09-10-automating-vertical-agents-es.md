---
audio: false
date: 2025-09-10
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Automatización de agentes verticales con validación
translated: true
type: note
---

Respuesta corta: tienes **mayormente razón**. La forma escalable es construir **agentes verticales codificados** que llamen a APIs de LLM, más una **validación automática** sólida. Aún querrás un bucle de "humano-en-excepción", no de "nunca-humano", porque la realidad incluye interrupciones de la API, desviaciones y casos extremos. Pero en tareas bien delimitadas con buenas comprobaciones, puedes ejecutar **completamente automatizado**.

A continuación tienes un plan práctico que puedes implementar.

# Lo que realmente se necesita para estar "completamente automatizado"

* **Andamiaje determinista**: planes/plantillas de código generados una vez, luego **parametrizados**; no "re-prompt desde cero" en cada ejecución.
* **E/S tipada y con esquema**: fuerza al LLM a devolver JSON que tu código valide antes de usar.
* **Comprobaciones fundamentadas**: valida las salidas contra herramientas, compiladores, pruebas unitarias, linters, mocks HTTP, esquemas SQL, etc.
* **Puerta de riesgo**: aplica cambios automáticamente solo cuando la confianza y las comprobaciones pasen; de lo contrario, crea un ticket/PR para revisión.
* **Observabilidad**: registros, trazas, medidores de costo/latencia, tasas de éxito, umbrales de desviación/alarma.
* **Defensa en profundidad**: comprobaciones cruzadas multi-modelo, votos de auto-consistencia, ejecución en sandbox, límites de tamaño de diff, listas de permitidos/denegados.

# Arquitectura de referencia (mínima pero sólida)

* **Controlador**: lee tareas de una cola (Kafka/SQS/Redis/DB simple).
* **Planificador** (LLM): convierte la tarea en un plan concreto y pasos estructurados.
* **Ejecutores** (herramientas + LLM donde se necesite): ediciones de código, llamadas a API, operaciones de archivos.
* **Validadores**: comprobaciones de esquema/tipo, análisis estático, pruebas unitarias, pruebas golden.
* **Motor de Políticas**: decide auto-fusionar vs. "necesita humano".
* **Informador**: abre PRs, crea issues, publica resúmenes en Slack/Email.

# Patrones de validación que realmente funcionan

* Esquema JSON + reintentos hasta que sea válido.
* Análisis AST + semántica básica (ej., asegurar que la clase/método existe).
* Ejecutar **ruff/mypy/flake8**, **pytest** con umbral de cobertura, **bandit** para seguridad.
* Para texto/datos: invariantes regex, respuestas de referencia, umbrales BLEU/ROUGE, o reglas de negocio personalizadas.
* Para llamar a sistemas externos: simular/emular primero; canary en prod con modo **solo-lectura** o **en sombra**; luego despliegue progresivo.

---

# Inicio: Esqueleto de "agente vertical" en Python

Esto ejecuta tareas en paralelo, fuerza salida JSON, valida, ejecuta comprobaciones locales, y o bien aplica automáticamente o abre un PR. Sustituye el stub `call_llm()` por tu proveedor/router.

```python
import asyncio, json, os, re, subprocess, time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List, Tuple, Callable

# ---------- Especificación de tarea ----------
@dataclass
class Task:
    id: str
    kind: str            # ej., "refactor", "write_test", "doc_summarize"
    repo_path: str
    target: str          # archivo/ruta/módulo o URL
    spec: Dict[str, Any] # detalles de forma libre

# ---------- Llamada LLM (sustituye tu router aquí) ----------
async def call_llm(system: str, user: str, schema_hint: str, max_retries=3) -> Dict[str, Any]:
    """
    Devuelve JSON estructurado. Tu impl real: router Anthropic/OpenAI/Gemini/Mistral con
    forzado de herramienta / modo JSON / 'respond_with_schema' etc.
    """
    last_err = None
    for _ in range(max_retries):
        # >>> reemplazar con llamada real a API en modo JSON <<<
        fake = {"plan": ["edit file", "run tests"], "edits":[{"path":"foo.py","patch":"print('ok')\n"}], "confidence": 0.92}
        try:
            # Validar campos básicos temprano
            if not isinstance(fake.get("edits"), list): raise ValueError("bad edits")
            return fake
        except Exception as e:
            last_err = e
    raise RuntimeError(f"LLM failed to produce valid JSON: {last_err}")

# ---------- Validadores ----------
def json_schema_validate(payload: Dict[str, Any]) -> Tuple[bool, str]:
    if "edits" not in payload: return False, "missing edits"
    for e in payload["edits"]:
        if "path" not in e or "patch" not in e:
            return False, f"bad edit item: {e}"
    return True, "ok"

def apply_patch(repo_path: str, path: str, patch: str) -> None:
    abs_path = os.path.join(repo_path, path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, "a", encoding="utf-8") as f:
        f.write("\n" + patch)

def run_cmd(cmd: List[str], cwd: Optional[str]=None, timeout: int=300) -> Tuple[int, str]:
    proc = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    try:
        out, _ = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        return 124, "timeout"
    return proc.returncode, out

def static_checks(repo_path: str) -> Tuple[bool, str]:
    # Intercambia con tus herramientas: ruff, mypy, eslint, mvn test, gradle, etc.
    codes = []
    outputs = []

    # Ejemplo de comprobaciones Python; proteger si faltan herramientas.
    for cmd in [["python","-m","py_compile","."]]:
        rc, out = run_cmd(cmd, cwd=repo_path)
        codes.append(rc); outputs.append(out or "")
    ok = all(rc == 0 for rc in codes)
    return ok, "\n".join(outputs)

def unit_tests(repo_path: str) -> Tuple[bool, str]:
    # Reemplazar con pytest/mvn/gradle/npm test según sea necesario
    if not os.path.exists(os.path.join(repo_path, "tests")):
        return True, "no tests dir, skipping"
    rc, out = run_cmd(["pytest","-q"], cwd=repo_path)
    return rc == 0, out

def policy_decision(confidence: float, static_ok: bool, tests_ok: bool, max_diff_lines: int, diff_lines: int) -> str:
    if confidence >= 0.9 and static_ok and tests_ok and diff_lines <= max_diff_lines:
        return "AUTO_APPLY"
    return "REVIEW"

def compute_diff_size(repo_path: str) -> int:
    rc, out = run_cmd(["git","-c","color.ui=never","diff"], cwd=repo_path)
    if rc != 0: return 10**9
    return len(out.splitlines())

# ---------- Worker ----------
async def worker(task: Task, max_diff_lines=800) -> Dict[str, Any]:
    system_prompt = "You are a strict code agent. Output JSON only and follow the schema."
    user_prompt = json.dumps(asdict(task), ensure_ascii=False)
    schema_hint = '{"plan":[str], "edits":[{"path":str,"patch":str}], "confidence": float}'

    payload = await call_llm(system_prompt, user_prompt, schema_hint)
    ok, why = json_schema_validate(payload)
    if not ok:
        return {"task": task.id, "status":"FAILED", "reason": f"schema: {why}"}

    # Aplicar ediciones en rama sandbox
    run_cmd(["git","checkout","-B", f"agent/{task.id}"], cwd=task.repo_path)
    for e in payload["edits"]:
        apply_patch(task.repo_path, e["path"], e["patch"])
    run_cmd(["git","add","-A"], cwd=task.repo_path)
    run_cmd(["git","commit","-m", f"agent: {task.kind} {task.target}"], cwd=task.repo_path)

    # Validar
    static_ok, static_out = static_checks(task.repo_path)
    tests_ok, tests_out = unit_tests(task.repo_path)
    diff_lines = compute_diff_size(task.repo_path)
    decision = policy_decision(payload.get("confidence",0.0), static_ok, tests_ok, max_diff_lines, diff_lines)

    result = {
        "task": task.id,
        "decision": decision,
        "confidence": payload.get("confidence"),
        "static_ok": static_ok,
        "tests_ok": tests_ok,
        "diff_lines": diff_lines,
    }

    if decision == "AUTO_APPLY":
        # fusionar a main; o push & auto-fusionar vía reglas CI
        run_cmd(["git","checkout","main"], cwd=task.repo_path)
        run_cmd(["git","merge","--no-ff", f"agent/{task.id}"], cwd=task.repo_path)
        result["status"] = "APPLIED"
    else:
        # abrir PR vía tu bot CI en lugar de fusionar directamente
        result["status"] = "REVIEW"
        result["note"] = "Opened PR or created issue for human-on-exception."
    return result

# ---------- Orchestrador ----------
async def run_queue(tasks: List[Task], concurrency: int = 4) -> List[Dict[str, Any]]:
    sem = asyncio.Semaphore(concurrency)
    results = []
    async def run_one(t: Task):
        async with sem:
            try:
                res = await worker(t)
            except Exception as e:
                res = {"task": t.id, "status":"FAILED", "reason": repr(e)}
            results.append(res)
    await asyncio.gather(*(run_one(t) for t in tasks))
    return results

# Ejemplo de uso:
# asyncio.run(run_queue([Task(id="1", kind="refactor", repo_path="/path/to/repo", target="foo.py", spec={"goal":"extract fn"})]))
```

## Cómo esto te lleva a "sin chat, solo código"

* El **planificador** produce ediciones estructuradas.
* Los **validadores** controlan la corrección.
* El **motor de políticas** aplica automáticamente los diffs seguros, deriva el resto a revisión.
* No "hablas" con un chatbot. Envías tareas (YAML/JSON o CLI), y el sistema ejecuta.

---

# Mejoras que probablemente añadirás

* **Router multi-modelo** con alternativas y votación de auto-consistencia.
* **Aplicación de modo JSON** con una herramienta que re-prompt hasta que sea válido para el esquema.
* **Validadores de dominio**: ejecución en seco de migraciones de DB, comprobaciones de contrato de API (OpenAPI), pruebas de carga.
* **Almacén de artefactos** para planes, diffs, registros; dashboards Grafana para SLIs/SLOs.
* **Gobernanza de secretos y datos**: tokens con alcance, redacción, repositorios permitidos.

---

# Cuándo puedes realmente ir "completamente desatendido"

* La tarea es **reducida** y repetible (ej., sincronización de docs, stubs de prueba boilerplate, refactors rutinarios).
* Tienes **buenas pruebas oráculo** o invariantes fuertes.
* Has ejecutado **en sombra/canary** exitosamente sin intervención por un tiempo.
* El radio de explosión es limitado (diffs pequeños, reversible, en sandbox).

Para todo lo demás, mantén **humano-en-excepción**. Aún así obtendrás el 80-95% de las ganancias de productividad sin arriesgar fallos silenciosos.

Si quieres, puedo adaptar el esqueleto a tu stack exacto (Python/Java Maven, Ruff/Mypy/PyTest, o Maven/Gradle + SpotBugs/Checkstyle/JUnit) y conectarlo a tu configuración de router.