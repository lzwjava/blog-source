---
audio: false
date: 2025-09-10
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Automatisation des agents verticaux avec validation
translated: true
type: note
---

Réponse courte : vous avez **en grande partie raison**. La méthode évolutive consiste à construire des **agents verticaux codés** qui appellent des API LLM, avec une **validation automatique** robuste. Vous voulez toujours une boucle « humain-sur-exception », pas « humain-jamais », car la réalité inclut des hoquets d'API, de la dérive et des cas limites. Mais pour des tâches bien définies avec de bons contrôles, vous pouvez fonctionner en **entièrement automatisé**.

Voici un plan pratique que vous pouvez mettre en œuvre.

# Ce que « entièrement automatisé » requiert vraiment

* **Échafaudage déterministe** : des plans/modèles de code générés une fois, puis **paramétrés** ; ne pas « re-demander à partir de zéro » à chaque exécution.
* **E/S typées, avec schémas** : forcer le LLM à retourner du JSON que votre code valide avant utilisation.
* **Contrôles ancrés** : valider les sorties par rapport à des outils, des compilateurs, des tests unitaires, des linters, des mocks HTTP, des schémas SQL, etc.
* **Porte de risque** : n'appliquer les changements automatiquement que lorsque la confiance et les contrôles sont passés ; sinon, créer un ticket/PR pour revue.
* **Observabilité** : journaux, traces, métriques de coût/latence, taux de réussite, seuils de dérive/alarme.
* **Défense en profondeur** : vérifications croisées multi-modèles, votes d'auto-cohérence, exécution en bac à sable, limites de taille de diff, listes autorisées/interdites.

# Architecture de référence (minimale mais solide)

* **Contrôleur** : lit les tâches depuis une file d'attente (Kafka/SQS/Redis/BDD simple).
* **Planificateur** (LLM) : transforme la tâche en un plan concret et des étapes structurées.
* **Exécuteurs** (outils + LLM si nécessaire) : modifications de code, appels d'API, opérations sur fichiers.
* **Validateurs** : vérifications de schéma/type, analyse statique, tests unitaires, golden tests.
* **Moteur de stratégie** : décide de la fusion automatique ou du « besoin d'un humain ».
* **Rapporteur** : ouvre des PR, crée des issues, poste des résumés sur Slack/Email.

# Modèles de validation qui fonctionnent réellement

* Schéma JSON + nouvelles tentatives jusqu'à validation.
* Analyse AST + sémantique basique (par ex., s'assurer qu'une classe/méthode existe).
* Exécuter **ruff/mypy/flake8**, **pytest** avec un seuil de couverture, **bandit** pour la sécurité.
* Pour le texte/les données : des invariants regex, des réponses de référence, des seuils BLEU/ROUGE, ou des règles métier spécifiques.
* Pour appeler des systèmes externes : d'abord mock/stub ; canary in prod en mode **lecture seule** ou **shadow** ; puis déploiement progressif.

---

# Pour commencer : squelette d'« agent vertical » en Python

Ceci exécute les tâches en parallèle, force une sortie JSON, valide, exécute des contrôles locaux, et soit applique automatiquement, soit ouvre une PR. Remplacez l'ébauche `call_llm()` par votre fournisseur/routeur.

```python
import asyncio, json, os, re, subprocess, time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List, Tuple, Callable

# ---------- Spécification de tâche ----------
@dataclass
class Task:
    id: str
    kind: str            # ex. : "refactor", "write_test", "doc_summarize"
    repo_path: str
    target: str          # fichier/chemin/module ou URL
    spec: Dict[str, Any] # détails libres

# ---------- Appel LLM (remplacez par votre routeur ici) ----------
async def call_llm(system: str, user: str, schema_hint: str, max_retries=3) -> Dict[str, Any]:
    """
    Retourne du JSON structuré. Votre implémentation réelle : routeur Anthropic/OpenAI/Gemini/Mistral avec
    forçage d'outil / mode JSON / 'respond_with_schema' etc.
    """
    last_err = None
    for _ in range(max_retries):
        # >>> remplacer par un vrai appel d'API en mode JSON <<<
        fake = {"plan": ["edit file", "run tests"], "edits":[{"path":"foo.py","patch":"print('ok')\n"}], "confidence": 0.92}
        try:
            # Valider les champs de base tôt
            if not isinstance(fake.get("edits"), list): raise ValueError("bad edits")
            return fake
        except Exception as e:
            last_err = e
    raise RuntimeError(f"LLM a échoué à produire un JSON valide : {last_err}")

# ---------- Validateurs ----------
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
    # Remplacez par vos outils : ruff, mypy, eslint, mvn test, gradle, etc.
    codes = []
    outputs = []

    # Exemple de vérifications Python ; protéger si outils manquants.
    for cmd in [["python","-m","py_compile","."]]:
        rc, out = run_cmd(cmd, cwd=repo_path)
        codes.append(rc); outputs.append(out or "")
    ok = all(rc == 0 for rc in codes)
    return ok, "\n".join(outputs)

def unit_tests(repo_path: str) -> Tuple[bool, str]:
    # Remplacer par pytest/mvn/gradle/npm test selon les besoins
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

    # Appliquer les modifications dans une branche sandbox
    run_cmd(["git","checkout","-B", f"agent/{task.id}"], cwd=task.repo_path)
    for e in payload["edits"]:
        apply_patch(task.repo_path, e["path"], e["patch"])
    run_cmd(["git","add","-A"], cwd=task.repo_path)
    run_cmd(["git","commit","-m", f"agent: {task.kind} {task.target}"], cwd=task.repo_path)

    # Valider
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
        # fusionner dans main ; ou pousser & auto-fusionner via les règles CI
        run_cmd(["git","checkout","main"], cwd=task.repo_path)
        run_cmd(["git","merge","--no-ff", f"agent/{task.id}"], cwd=task.repo_path)
        result["status"] = "APPLIED"
    else:
        # ouvrir une PR via votre bot CI au lieu de fusionner directement
        result["status"] = "REVIEW"
        result["note"] = "Opened PR or created issue for human-on-exception."
    return result

# ---------- Orchestrateur ----------
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

# Exemple d'utilisation :
# asyncio.run(run_queue([Task(id="1", kind="refactor", repo_path="/path/to/repo", target="foo.py", spec={"goal":"extract fn"})]))
```

## Comment ceci vous mène à « pas de chat, juste du code »

* Le **planificateur** produit des modifications structurées.
* Les **validateurs** vérifient la justesse.
* Le **moteur de stratégie** applique automatiquement les diffs sûrs, achemine le reste vers la revue.
* Vous ne « parlez » pas à un chatbot. Vous soumettez des tâches (YAML/JSON ou CLI), et le système exécute.

---

# Améliorations que vous ajouterez probablement

* **Routeur multi-modèles** avec solutions de repli et vote d'auto-cohérence.
* **Application du mode JSON** avec un outil qui redemande jusqu'à ce que le schéma soit valide.
* **Validateurs de domaine** : dry-run de migrations de BDD, vérifications de contrats d'API (OpenAPI), tests de charge.
* **Stockage d'artefacts** pour les plans, diffs, journaux ; tableaux de bord Grafana pour les SLI/SLO.
* **Gouvernance des secrets et des données** : tokens scopés, rédaction, dépôts autorisés.

---

# Quand vous pouvez vraiment passer en « entièrement sans surveillance »

* La tâche est **étroite** et répétable (par ex., synchronisation de docs, squelettes de tests boilerplate, refactorisations de routine).
* Vous avez **de bons tests oracle** ou des invariants forts.
* Vous avez exécuté avec succès un mode **shadow/canary** en sans-contact pendant un moment.
* Le rayon d'impact est limité (petits diffs, réversible, isolé).

Pour tout le reste, gardez **l'humain-sur-exception**. Vous obtiendrez toujours 80 à 95 % des gains de productivité sans risquer des échecs silencieux.

Si vous voulez, je peux adapter le squelette à votre stack exacte (Python/Java Maven, Ruff/Mypy/PyTest, ou Maven/Gradle + SpotBugs/Checkstyle/JUnit) et le connecter à votre configuration de routeur.