---
audio: false
date: 2025-09-10
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Automatisierung vertikaler Agenten mit Validierung
translated: true
type: note
---

Kurze Antwort: Du hast **größtenteils recht**. Der skalierbare Weg ist, **vertikale, programmierte Agenten** zu bauen, die LLM-APIs aufrufen, plus eine starke **automatische Validierung**. Man möchte immer noch eine "Human-on-Exception"-Schleife, nicht "Human-Never", weil die Realität API-Aussetzer, Drift und Edge Cases beinhaltet. Aber bei gut abgegrenzten Aufgaben mit guten Prüfungen kann man **vollautomatisiert** laufen.

Unten findest du einen praktischen Bauplan, den du implementieren kannst.

# Was "vollautomatisiert" wirklich erfordert

*   **Deterministisches Scaffolding**: Code-Pläne/Vorlagen werden einmal generiert, dann **parametrisiert**; nicht "jeden Lauf von Grund auf neu prompten".
*   **Getypete, schema-basierte E/A**: Zwinge das LLM, JSON zurückzugeben, das dein Code vor der Verwendung validiert.
*   **Gegründete Prüfungen**: Validiere Ausgaben gegen Tools, Compiler, Unit Tests, Linter, HTTP Mocks, SQL-Schemata etc.
*   **Risiko-Gating**: Wende Änderungen nur automatisch an, wenn Konfidenz + Prüfungen bestehen; andernfalls erstelle ein Ticket/PR zur Überprüfung.
*   **Beobachtbarkeit**: Logs, Traces, Kosten/Latenz-Messungen, Erfolgsquoten, Drift/Alarm-Schwellenwerte.
*   **Verteidigung in der Tiefe**: Multi-Model-Cross-Checks, Self-Consistency-Abstimmungen, Sandbox-Ausführung, Diff-Größenlimits, Allowlists/Denylists.

# Referenzarchitektur (minimal, aber solide)

*   **Controller**: Liest Aufgaben aus einer Warteschlange (Kafka/SQS/Redis/einfache DB).
*   **Planner** (LLM): Wandelt eine Aufgabe in einen konkreten Plan und strukturierte Schritte um.
*   **Executors** (Tools + LLM falls nötig): Code-Bearbeitungen, API-Aufrufe, Dateioperationen.
*   **Validators**: Schema/Type-Checks, Statische Analyse, Unit Tests, Golden Tests.
*   **Policy Engine**: Entscheidet über Auto-Merge vs. "Benötigt Mensch".
*   **Reporter**: Öffnet PRs, erstellt Issues, sendet Slack/E-Mail-Zusammenfassungen.

# Validierungsmuster, die tatsächlich funktionieren

*   JSON-Schema + Wiederholungen bis gültig.
*   AST-Parse + grundlegende Semantik (z.B. sicherstellen, dass Klasse/Methode existiert).
*   Führe **ruff/mypy/flake8**, **pytest** mit Coverage-Threshold, **bandit** für Sicherheit aus.
*   Für Text/Daten: Regex-Invarianten, Referenzantworten, BLEU/ROUGE-Schwellenwerte oder maßgeschneiderte Geschäftsregeln.
*   Für den Aufruf externer Systeme: Mock/Stub zuerst; Canary in Prod mit **Read-Only** oder **Shadow**-Modus; dann progressiver Rollout.

---

# Starter: Python "Vertikaler Agent" Skelett

Dieses führt Aufgaben parallel aus, erzwingt JSON-Ausgabe, validiert, führt lokale Checks aus und wendet entweder automatisch an oder öffnet einen PR. Ersetze den `call_llm()` Stub durch deinen Provider/Router.

```python
import asyncio, json, os, re, subprocess, time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List, Tuple, Callable

# ---------- Task spec ----------
@dataclass
class Task:
    id: str
    kind: str            # e.g., "refactor", "write_test", "doc_summarize"
    repo_path: str
    target: str          # file/path/module or URL
    spec: Dict[str, Any] # free-form details

# ---------- LLM call (stub your router here) ----------
async def call_llm(system: str, user: str, schema_hint: str, max_retries=3) -> Dict[str, Any]:
    """
    Return structured JSON. Your real impl: Anthropic/OpenAI/Gemini/Mistral router with
    tool forcing / JSON mode / 'respond_with_schema' etc.
    """
    last_err = None
    for _ in range(max_retries):
        # >>> replace with real API call in JSON mode <<<
        fake = {"plan": ["edit file", "run tests"], "edits":[{"path":"foo.py","patch":"print('ok')\n"}], "confidence": 0.92}
        try:
            # Validate basic fields early
            if not isinstance(fake.get("edits"), list): raise ValueError("bad edits")
            return fake
        except Exception as e:
            last_err = e
    raise RuntimeError(f"LLM failed to produce valid JSON: {last_err}")

# ---------- Validators ----------
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
    # Swap in your tools: ruff, mypy, eslint, mvn test, gradle, etc.
    codes = []
    outputs = []

    # Example Python checks; guard if tools missing.
    for cmd in [["python","-m","py_compile","."]]:
        rc, out = run_cmd(cmd, cwd=repo_path)
        codes.append(rc); outputs.append(out or "")
    ok = all(rc == 0 for rc in codes)
    return ok, "\n".join(outputs)

def unit_tests(repo_path: str) -> Tuple[bool, str]:
    # Replace with pytest/mvn/gradle/npm test as needed
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

    # Apply edits in sandbox branch
    run_cmd(["git","checkout","-B", f"agent/{task.id}"], cwd=task.repo_path)
    for e in payload["edits"]:
        apply_patch(task.repo_path, e["path"], e["patch"])
    run_cmd(["git","add","-A"], cwd=task.repo_path)
    run_cmd(["git","commit","-m", f"agent: {task.kind} {task.target}"], cwd=task.repo_path)

    # Validate
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
        # merge to main; or push & auto-merge via CI rules
        run_cmd(["git","checkout","main"], cwd=task.repo_path)
        run_cmd(["git","merge","--no-ff", f"agent/{task.id}"], cwd=task.repo_path)
        result["status"] = "APPLIED"
    else:
        # open PR via your CI bot instead of merging directly
        result["status"] = "REVIEW"
        result["note"] = "Opened PR or created issue for human-on-exception."
    return result

# ---------- Orchestrator ----------
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

# Example usage:
# asyncio.run(run_queue([Task(id="1", kind="refactor", repo_path="/path/to/repo", target="foo.py", spec={"goal":"extract fn"})]))
```

## Wie dich das zu "kein Chat, nur Code" bringt

*   Der **Planner** erzeugt strukturierte Bearbeitungen.
*   Die **Validators** überwachen die Korrektheit.
*   Die **Policy Engine** wendet sichere Diffs automatisch an, leitet den Rest zur Überprüfung weiter.
*   Du "sprichst" nicht mit einem Chatbot. Du übergibst Aufgaben (YAML/JSON oder CLI), und das System führt sie aus.

---

# Upgrades, die du wahrscheinlich hinzufügen wirst

*   **Multi-Model-Router** mit Fallbacks und Self-Consistency-Abstimmung.
*   **JSON-Mode-Erzwingung** mit einem Tool, das so lange neu promptet, bis es schema-valide ist.
*   **Domain Validators**: DB-Migrationen Dry-Run, API-Contract-Checks (OpenAPI), Lasttests.
*   **Artifact Store** für Pläne, Diffs, Logs; Grafana-Dashboards für SLIs/SLOs.
*   **Secrets & Data Governance**: Gescopte Tokens, Redaktion, Erlaubte Repos.

---

# Wann du wirklich "vollkommen unbeaufsichtigt" gehen kannst

*   Die Aufgabe ist **eng** und wiederholbar (z.B. Doc-Sync, Boilerplate-Test-Stubs, Routine-Refactors).
*   Du hast **gute Oracle-Tests** oder starke Invarianten.
*   Du hast **Shadow/Canary** erfolgreich eine Zeit lang mit Zero-Touch laufen lassen.
*   Die Auswirkungsradius ist begrenzt (kleine Diffs, reversibel, gesandboxt).

Für alles andere, behalte **Human-on-Exception**. Du wirst immer noch 80–95% der Produktivitätsgewinne erhalten, ohne stille Fehler zu riskieren.

Falls du möchtest, kann ich das Skelett an deinen genauen Stack anpassen (Python/Java Maven, Ruff/Mypy/PyTest, oder Maven/Gradle + SpotBugs/Checkstyle/JUnit) und es an deine Router-Konfiguration anbinden.