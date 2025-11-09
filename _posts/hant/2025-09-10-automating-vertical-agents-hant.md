---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 自動化驗證垂直代理
translated: true
type: note
---

簡短回答：你**大致正確**。可擴展的方式是建立**垂直的、編碼化的代理**來呼叫 LLM API，再加上強大的**自動化驗證**。你仍然需要「異常時人工介入」的循環，而非「完全無需人工」，因為現實情況包含 API 不穩定、模型漂移和邊緣案例。但在範圍明確且檢查機制完善的任務上，你可以實現**全自動運行**。

以下是一個可實際執行的藍圖。

# 實現「全自動」的真正要素

* **確定性框架**：程式碼計劃/範本只需生成一次，之後進行**參數化**；不要每次執行都「從頭開始重新提示」。
* **類型化、結構化的輸入輸出**：強制 LLM 回傳 JSON，並由你的程式碼在使用前進行驗證。
* **基礎檢查**：根據工具、編譯器、單元測試、linter、HTTP 模擬、SQL 結構描述等來驗證輸出。
* **風險控管**：僅在信心度與檢查通過時自動應用變更；否則提交工單/PR 進行審核。
* **可觀測性**：日誌、追蹤、成本/延遲計量、成功率、漂移/警報閾值。
* **深度防禦**：多模型交叉檢查、自我一致性投票、沙箱執行、差異大小限制、允許清單/拒絕清單。

# 參考架構（精簡而穩固）

* **控制器**：從佇列（Kafka/SQS/Redis/簡單資料庫）讀取任務。
* **規劃器**（LLM）：將任務轉換為具體計劃和結構化步驟。
* **執行器**（工具 + 必要時使用 LLM）：程式碼編輯、API 呼叫、檔案操作。
* **驗證器**：結構描述/類型檢查、靜態分析、單元測試、黃金測試。
* **策略引擎**：決定自動合併或「需要人工處理」。
* **報告器**：開啟 PR、建立問題、發送 Slack/Email 摘要。

# 實際有效的驗證模式

* JSON 結構描述 + 重試直至有效。
* AST 解析 + 基本語意檢查（例如，確保類別/方法存在）。
* 執行 **ruff/mypy/flake8**、**pytest**（含覆蓋率閾值）、**bandit** 進行安全檢查。
* 對於文字/資料：正規表示式不變量、參考答案、BLEU/ROUGE 閾值，或自訂業務規則。
* 對於呼叫外部系統：先進行模擬/存根測試；在生產環境中以**唯讀**或**影子**模式進行金絲雀部署；然後逐步推廣。

---

# 入門：Python「垂直代理」骨架

此程式碼可並行執行任務，強制輸出 JSON，進行驗證，執行本地檢查，並自動應用變更或開啟 PR。請將 `call_llm()` 的存根替換為你的供應商/路由器。

```python
import asyncio, json, os, re, subprocess, time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List, Tuple, Callable

# ---------- 任務規格 ----------
@dataclass
class Task:
    id: str
    kind: str            # 例如："refactor", "write_test", "doc_summarize"
    repo_path: str
    target: str          # 檔案/路徑/模組或 URL
    spec: Dict[str, Any] # 自由形式的詳細資訊

# ---------- LLM 呼叫（在此替換為你的路由器） ----------
async def call_llm(system: str, user: str, schema_hint: str, max_retries=3) -> Dict[str, Any]:
    """
    回傳結構化 JSON。你的實際實作：Anthropic/OpenAI/Gemini/Mistral 路由器，並帶有
    工具強制 / JSON 模式 / 'respond_with_schema' 等功能。
    """
    last_err = None
    for _ in range(max_retries):
        # >>> 替換為 JSON 模式下的真實 API 呼叫 <<<
        fake = {"plan": ["edit file", "run tests"], "edits":[{"path":"foo.py","patch":"print('ok')\n"}], "confidence": 0.92}
        try:
            # 早期驗證基本欄位
            if not isinstance(fake.get("edits"), list): raise ValueError("bad edits")
            return fake
        except Exception as e:
            last_err = e
    raise RuntimeError(f"LLM failed to produce valid JSON: {last_err}")

# ---------- 驗證器 ----------
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
    # 替換為你的工具：ruff, mypy, eslint, mvn test, gradle 等。
    codes = []
    outputs = []

    # 範例 Python 檢查；若工具缺失則跳過。
    for cmd in [["python","-m","py_compile","."]]:
        rc, out = run_cmd(cmd, cwd=repo_path)
        codes.append(rc); outputs.append(out or "")
    ok = all(rc == 0 for rc in codes)
    return ok, "\n".join(outputs)

def unit_tests(repo_path: str) -> Tuple[bool, str]:
    # 根據需要替換為 pytest/mvn/gradle/npm test
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

# ---------- 工作器 ----------
async def worker(task: Task, max_diff_lines=800) -> Dict[str, Any]:
    system_prompt = "You are a strict code agent. Output JSON only and follow the schema."
    user_prompt = json.dumps(asdict(task), ensure_ascii=False)
    schema_hint = '{"plan":[str], "edits":[{"path":str,"patch":str}], "confidence": float}'

    payload = await call_llm(system_prompt, user_prompt, schema_hint)
    ok, why = json_schema_validate(payload)
    if not ok:
        return {"task": task.id, "status":"FAILED", "reason": f"schema: {why}"}

    # 在沙箱分支中應用編輯
    run_cmd(["git","checkout","-B", f"agent/{task.id}"], cwd=task.repo_path)
    for e in payload["edits"]:
        apply_patch(task.repo_path, e["path"], e["patch"])
    run_cmd(["git","add","-A"], cwd=task.repo_path)
    run_cmd(["git","commit","-m", f"agent: {task.kind} {task.target}"], cwd=task.repo_path)

    # 驗證
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
        # 合併到 main；或透過 CI 規則推送並自動合併
        run_cmd(["git","checkout","main"], cwd=task.repo_path)
        run_cmd(["git","merge","--no-ff", f"agent/{task.id}"], cwd=task.repo_path)
        result["status"] = "APPLIED"
    else:
        # 透過你的 CI 機器人開啟 PR，而非直接合併
        result["status"] = "REVIEW"
        result["note"] = "Opened PR or created issue for human-on-exception."
    return result

# ---------- 協調器 ----------
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

# 使用範例：
# asyncio.run(run_queue([Task(id="1", kind="refactor", repo_path="/path/to/repo", target="foo.py", spec={"goal":"extract fn"})]))
```

## 這如何實現「無需對話，只需程式碼」

* **規劃器**產生結構化的編輯內容。
* **驗證器**確保正確性。
* **策略引擎**自動應用安全的差異，將其餘部分轉交審核。
* 你無需與聊天機器人「對話」。你提交任務（YAML/JSON 或 CLI），系統便會執行。

---

# 你可能會加入的升級功能

* **多模型路由器**，帶有後備機制和自我一致性投票。
* **JSON 模式強制**，使用工具重新提示直至結構描述有效。
* **領域驗證器**：資料庫遷移乾跑、API 合約檢查（OpenAPI）、負載測試。
* **成品儲存庫**用於計劃、差異、日誌；Grafana 儀表板用於 SLI/SLO。
* **密碼與資料治理**：範圍化令牌、資料遮罩、允許清單儲存庫。

---

# 何時才能真正實現「完全無人值守」

* 任務**範圍狹窄**且可重複（例如，文件同步、樣板測試存根、常規重構）。
* 你擁有**良好的預言測試**或強不變量。
* 你已成功運行**影子/金絲雀**部署一段時間，實現零接觸。
* 影響範圍有限（差異小、可逆、沙箱化）。

對於其他情況，請保持**異常時人工介入**。你仍然可以獲得 80-95% 的生產力提升，而無需承擔無聲失敗的風險。

如果你需要，我可以根據你的具體技術堆疊（Python/Java Maven、Ruff/Mypy/PyTest，或 Maven/Gradle + SpotBugs/Checkstyle/JUnit）調整此骨架，並將其連接到你的路由器配置。