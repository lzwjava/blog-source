---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: 検証機能付き垂直エージェントの自動化
translated: true
type: note
---

端的な答え：あなたの考えは**ほぼ正しい**です。スケーラブルな方法は、LLM APIを呼び出す**垂直的でコード化されたエージェント**を構築し、強力な**自動検証**を組み合わせることです。現実にはAPIの不具合、ドリフト、エッジケースが存在するため、「人間が関与しない」ではなく「例外時に人間が関与する」ループを維持すべきです。しかし、適切に範囲が定められ、チェックが十分なタスクでは、**完全自動化**で実行できます。

以下は実装可能な実践的な設計図です。

# 「完全自動化」に本当に必要なもの

* **決定的なスキャフォールディング**: コードの計画/テンプレートを一度生成し、その後は**パラメータ化**する。毎回「ゼロから再プロンプト」しない。
* **型付けされスキーマ化されたI/O**: LLMにJSONを返させ、使用前にコードで検証する。
* **接地されたチェック**: ツール、コンパイラ、ユニットテスト、リンター、HTTPモック、SQLスキーマなどに対して出力を検証する。
* **リスクゲーティング**: 信頼度とチェックが合格した場合のみ変更を自動適用し、それ以外はレビューのためにチケット/PRを発行する。
* **オブザーバビリティ**: ログ、トレース、コスト/レイテンシ計測、成功率、ドリフト/アラーム閾値。
* **多層防御**: マルチモデル相互チェック、自己一貫性投票、サンドボックス実行、差分サイズ制限、許可リスト/拒否リスト。

# リファレンスアーキテクチャ（最小限だが堅牢）

* **コントローラー**: キュー（Kafka/SQS/Redis/シンプルなDB）からタスクを読み取る。
* **プランナー** (LLM): タスクを具体的な計画と構造化されたステップに変換する。
* **エグゼキューター** (ツール + 必要に応じてLLM): コード編集、API呼び出し、ファイル操作。
* **バリデータ**: スキーマ/型チェック、静的解析、ユニットテスト、ゴールデンテスト。
* **ポリシーエンジン**: 自動マージと「人間のレビュー必要」を決定する。
* **レポーター**: PRの作成、Issueの作成、Slack/Emailサマリーの投稿。

# 実際に機能する検証パターン

* JSONスキーマ + 有効になるまでリトライ。
* AST解析 + 基本的な意味論（例：クラス/メソッドが存在することを確認）。
* **ruff/mypy/flake8**, カバレッジ閾値を伴う**pytest**, セキュリティのための**bandit**を実行。
* テキスト/データの場合: 正規表現による不変条件、参照回答、BLEU/ROUGE閾値、または独自のビジネスルール。
* 外部システム呼び出しの場合: まずモック/スタブでテスト。本番環境では**読み取り専用**または**シャドウ**モードでカナリアリリース。その後段階的なロールアウト。

---

# スターター: Python「垂直エージェント」スケルトン

これはタスクを並列実行し、JSON出力を強制し、検証し、ローカルチェックを実行し、自動適用するかPRをオープンします。`call_llm()` スタブをあなたのプロバイダー/ルーターと交換してください。

```python
import asyncio, json, os, re, subprocess, time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List, Tuple, Callable

# ---------- タスク仕様 ----------
@dataclass
class Task:
    id: str
    kind: str            # 例: "refactor", "write_test", "doc_summarize"
    repo_path: str
    target: str          # ファイル/パス/モジュール または URL
    spec: Dict[str, Any] # 自由形式の詳細

# ---------- LLM呼び出し (ここにあなたのルーターをスタブ実装) ----------
async def call_llm(system: str, user: str, schema_hint: str, max_retries=3) -> Dict[str, Any]:
    """
    構造化されたJSONを返す。実際の実装: Anthropic/OpenAI/Gemini/Mistral ルーターに
    ツール強制 / JSONモード / 'respond_with_schema' などを組み込む。
    """
    last_err = None
    for _ in range(max_retries):
        # >>> JSONモードでの実際のAPI呼び出しに置き換える <<<
        fake = {"plan": ["edit file", "run tests"], "edits":[{"path":"foo.py","patch":"print('ok')\n"}], "confidence": 0.92}
        try:
            # 基本的なフィールドを早期に検証
            if not isinstance(fake.get("edits"), list): raise ValueError("bad edits")
            return fake
        except Exception as e:
            last_err = e
    raise RuntimeError(f"LLM failed to produce valid JSON: {last_err}")

# ---------- バリデータ ----------
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
    # あなたのツールと交換: ruff, mypy, eslint, mvn test, gradle, etc.
    codes = []
    outputs = []

    # Pythonチェックの例; ツールがない場合はガードする。
    for cmd in [["python","-m","py_compile","."]]:
        rc, out = run_cmd(cmd, cwd=repo_path)
        codes.append(rc); outputs.append(out or "")
    ok = all(rc == 0 for rc in codes)
    return ok, "\n".join(outputs)

def unit_tests(repo_path: str) -> Tuple[bool, str]:
    # pytest/mvn/gradle/npm test など必要に応じて置き換え
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

# ---------- ワーカー ----------
async def worker(task: Task, max_diff_lines=800) -> Dict[str, Any]:
    system_prompt = "You are a strict code agent. Output JSON only and follow the schema."
    user_prompt = json.dumps(asdict(task), ensure_ascii=False)
    schema_hint = '{"plan":[str], "edits":[{"path":str,"patch":str}], "confidence": float}'

    payload = await call_llm(system_prompt, user_prompt, schema_hint)
    ok, why = json_schema_validate(payload)
    if not ok:
        return {"task": task.id, "status":"FAILED", "reason": f"schema: {why}"}

    # サンドボックスブランチに編集を適用
    run_cmd(["git","checkout","-B", f"agent/{task.id}"], cwd=task.repo_path)
    for e in payload["edits"]:
        apply_patch(task.repo_path, e["path"], e["patch"])
    run_cmd(["git","add","-A"], cwd=task.repo_path)
    run_cmd(["git","commit","-m", f"agent: {task.kind} {task.target}"], cwd=task.repo_path)

    # 検証
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
        # mainにマージ。またはプッシュしてCIルール経由で自動マージ。
        run_cmd(["git","checkout","main"], cwd=task.repo_path)
        run_cmd(["git","merge","--no-ff", f"agent/{task.id}"], cwd=task.repo_path)
        result["status"] = "APPLIED"
    else:
        # 直接マージする代わりにCIボット経由でPRをオープン
        result["status"] = "REVIEW"
        result["note"] = "Opened PR or created issue for human-on-exception."
    return result

# ---------- オーケストレーター ----------
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

# 使用例:
# asyncio.run(run_queue([Task(id="1", kind="refactor", repo_path="/path/to/repo", target="foo.py", spec={"goal":"extract fn"})]))
```

## これが「チャットではなく、コードだけ」を実現する方法

* **プランナー**が構造化された編集を生成する。
* **バリデータ**が正確さをゲートする。
* **ポリシーエンジン**が安全な差分を自動適用し、残りをレビューに回す。
* チャットボットと「会話」するのではなく、タスク（YAML/JSONまたはCLI）を送信し、システムが実行する。

---

# おそらく追加するアップグレード

* **マルチモデルルーター**とフォールバック、自己一貫性投票。
* スキーマが有効になるまで再プロンプトするツールによる**JSONモード強制**。
* **ドメイン固有のバリデータ**: DBマイグレーションのドライラン、API契約チェック（OpenAPI）、負荷テスト。
* 計画、差分、ログのための**成果物ストア**。SLI/SLOのためのGrafanaダッシュボード。
* **シークレットとデータガバナンス**: スコープ付きトークン、編集、許可リスト化されたリポジトリ。

---

# 真に「完全無人化」できる条件

* タスクが**限定的**で繰り返し可能である（例：ドキュメント同期、ボイラープレートテストスタブ、定期的なリファクタリング）。
* **優れたオラクルテスト**または強力な不変条件がある。
* **シャドウ/カナリア**実行をしばらく成功裏にゼロタッチで行っている。
* ブラスト半径が限定されている（小さな差分、元に戻せる、サンドボックス化されている）。

それ以外のすべての場合、**例外時に人間が関与**を維持してください。これにより、サイレント障害のリスクなしに、生産性向上の80〜95%を得ることができます。

必要であれば、このスケルトンをあなたの正確なスタック（Python/Java Maven, Ruff/Mypy/PyTest, または Maven/Gradle + SpotBugs/Checkstyle/JUnit）に適合させ、あなたのルーター設定に接続できます。