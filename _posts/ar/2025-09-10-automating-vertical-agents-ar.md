---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: أتمتة الوكلاء الرأسية مع التحقق
translated: true
type: note
---

إجابة قصيرة: أنت **محق في الغالب**. الطريقة القابلة للتوسع هي بناء **وكلاء رأسيين مبرمجين** يستدعون واجهات برمجة تطبيقات النماذج اللغوية الكبيرة، بالإضافة إلى **تحقق آلي** قوي. لا تزال تريد حلقة "تدخل بشري في حالات الاستثناء"، وليس "لا تدخل بشري أبدًا"، لأن الواقع يتضمن عثرات في واجهات برمجة التطبيقات، وانحرافًا، وحالات طوارئ. ولكن في المهام المحددة جيدًا مع فحوصات جيدة، يمكنك التشغيل **آليًا بالكامل**.

أدناه مخطط عملي يمكنك تنفيذه.

# ما يتطلبه الأمر حقًا ليكون "آليًا بالكامل"

* **هيكلة حتمية**: خطط/قوالب كود يتم إنشاؤها مرة واحدة، ثم **تحديدها بمعاملات**؛ لا "تعيد المطالبة من الصفر" في كل تشغيل.
* **مدخلات ومخرجات مهيكلة ومرمزة**: أجبر النموذج اللغوي الكبير على إرجاع JSON يقوم برنامجك بالتحقق منه قبل الاستخدام.
* **فحوصات مؤسسة**: تحقق من المخرجات مقابل الأدوات، والمترجمين، واختبارات الوحدة، وأدوات التحقق من الجودة، ومحاكيات HTTP، ومخططات SQL، إلخ.
* **بوابات المخاطر**: طبق التغييرات تلقائيًا فقط عندما تتحقق الثقة والفحوصات؛ وإلا ارفع تذكرة/طلب سحب للمراجعة.
* **القدرة على المراقبة**: السجلات، والتتبع، ومقاييس التكلفة/زمن الاستجابة، ومعدلات النجاح، وعتبات الانحراف/الإنذار.
* **دفاع متعمق**: فحوصات متقاطعة متعددة النماذج، تصويت على التناسق الذاتي، تنفيذ في بيئة معزولة، حدود حجم الاختلافات، قوائم السماح/المنع.

# بنية مرجعية (دنيا ولكن متينة)

* **المتحكم**: يقرأ المهام من قائمة انتظار (Kafka / SQS / Redis / قاعدة بيانات بسيطة).
* **المخطط** (النموذج اللغوي الكبير): يحول المهمة إلى خطة ملموسة وخطوات مهيكلة.
* **المُنفذون** (أدوات + النموذج اللغوي الكبير عند الحاجة): تعديلات الكود، استدعاءات واجهة برمجة التطبيقات، عمليات الملفات.
* **أدوات التحقق**: فحوصات المخطط/النوع، التحليل الثابت، اختبارات الوحدة، الاختبارات الأساسية.
* **محرك السياسات**: يقرر الدمج التلقائي مقابل "يحتاج إلى تدخل بشري".
* **المراسل**: يفتح طلبات السحب، ينشئ قضايا، ينشر ملخصات على Slack/البريد الإلكتروني.

# أنماط التحقق التي تعمل بالفعل

* مخطط JSON + إعادة المحاولة حتى يصبح صالحًا.
* تحليل شجرة التركيب النحوي + دلالات أساسية (على سبيل المثال، التأكد من وجود الفئة/الطريقة).
* تشغيل **ruff/mypy/flake8**، **pytest** بحد تغطية، **bandit** للأمان.
* للنص/البيانات: ثوابت التعبير النمطي، إجابات مرجعية، عتبات BLEU/ROUGE، أو قواعد أعمال مخصصة.
* لاستدعاء الأنظمة الخارجية: محاكاة/استبعاد أولاً؛ اختبار تجريبي في الإنتاج بوضع **للقراءة فقط** أو **ظلي**؛ ثم النشر التدريجي.

---

# بداية: هيكل عميل "رأسي" بلغة Python

يشغل هذا المهام بالتوازي، يفرض إخراج JSON، يتحقق، يشغل فحوصات محلية، وإما يطبق تلقائيًا أو يفتح طلب سحب. استبدل الدالة `call_llm()` بواجهة مزودك/موجهك.

```python
import asyncio, json, os, re, subprocess, time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List, Tuple, Callable

# ---------- مواصفات المهمة ----------
@dataclass
class Task:
    id: str
    kind: str            # مثال: "refactor", "write_test", "doc_summarize"
    repo_path: str
    target: str          # ملف/مسار/وحدة أو URL
    spec: Dict[str, Any] # تفاصيل حرة الشكل

# ---------- استدعاء النموذج اللغوي الكبير (استبدل بالموجه هنا) ----------
async def call_llm(system: str, user: str, schema_hint: str, max_retries=3) -> Dict[str, Any]:
    """
    إرجاع JSON مهيكل. تطبيقك الحقيقي: موجه Anthropic/OpenAI/Gemini/Mistral مع
    إجبار الأداة / وضع JSON / 'respond_with_schema' إلخ.
    """
    last_err = None
    for _ in range(max_retries):
        # >>> استبدال باستدعاء API حقيقي في وضع JSON <<<
        fake = {"plan": ["edit file", "run tests"], "edits":[{"path":"foo.py","patch":"print('ok')\n"}], "confidence": 0.92}
        try:
            # تحقق من الحقول الأساسية مبكرًا
            if not isinstance(fake.get("edits"), list): raise ValueError("bad edits")
            return fake
        except Exception as e:
            last_err = e
    raise RuntimeError(f"LLM failed to produce valid JSON: {last_err}")

# ---------- أدوات التحقق ----------
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
    # استبدل بأدواتك: ruff, mypy, eslint, mvn test, gradle, إلخ.
    codes = []
    outputs = []

    # مثال على فحوصات Python; احمِ في حال عدم وجود الأدوات.
    for cmd in [["python","-m","py_compile","."]]:
        rc, out = run_cmd(cmd, cwd=repo_path)
        codes.append(rc); outputs.append(out or "")
    ok = all(rc == 0 for rc in codes)
    return ok, "\n".join(outputs)

def unit_tests(repo_path: str) -> Tuple[bool, str]:
    # استبدل بـ pytest/mvn/gradle/npm test حسب الحاجة
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

# ---------- العامل ----------
async def worker(task: Task, max_diff_lines=800) -> Dict[str, Any]:
    system_prompt = "You are a strict code agent. Output JSON only and follow the schema."
    user_prompt = json.dumps(asdict(task), ensure_ascii=False)
    schema_hint = '{"plan":[str], "edits":[{"path":str,"patch":str}], "confidence": float}'

    payload = await call_llm(system_prompt, user_prompt, schema_hint)
    ok, why = json_schema_validate(payload)
    if not ok:
        return {"task": task.id, "status":"FAILED", "reason": f"schema: {why}"}

    # تطبيق التعديلات في فرع بيئة الاختبار المعزولة
    run_cmd(["git","checkout","-B", f"agent/{task.id}"], cwd=task.repo_path)
    for e in payload["edits"]:
        apply_patch(task.repo_path, e["path"], e["patch"])
    run_cmd(["git","add","-A"], cwd=task.repo_path)
    run_cmd(["git","commit","-m", f"agent: {task.kind} {task.target}"], cwd=task.repo_path)

    # التحقق
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
        # دمج إلى main; أو ادفع ودمج تلقائيًا عبر قواعد CI
        run_cmd(["git","checkout","main"], cwd=task.repo_path)
        run_cmd(["git","merge","--no-ff", f"agent/{task.id}"], cwd=task.repo_path)
        result["status"] = "APPLIED"
    else:
        # افتح طلب سحب عبر بوت CI بدلاً من الدمج مباشرة
        result["status"] = "REVIEW"
        result["note"] = "Opened PR or created issue for human-on-exception."
    return result

# ---------- المنظم ----------
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

# مثال للاستخدام:
# asyncio.run(run_queue([Task(id="1", kind="refactor", repo_path="/path/to/repo", target="foo.py", spec={"goal":"extract fn"})]))
```

## كيف يوصلك هذا إلى "لا محادثة، فقط كود"

* **المخطط** ينتج تعديلات مهيكلة.
* **أدوات التحقق** تتحكم في الصحة.
* **محرك السياسات** يطبق الاختلافات الآمنة تلقائيًا، ويوجه الباقي للمراجعة.
* أنت لا "تتحدث" إلى روبوت محادثة. تقدم المهام (YAML/JSON أو CLI)، والنظام ينفذ.

---

# الترقيات التي من المحتمل أن تضيفها

* **موجه متعدد النماذج** مع بدائل احتياطية وتصويت على التناسق الذاتي.
* **فرض وضع JSON** بأداة تعيد المطالبة حتى يصبح صالحًا للمخطط.
* **أدوات تحقق نطاقية**: تجربة تشغيل هجرات قاعدة البيانات، فحوصات عقد واجهة برمجة التطبيقات (OpenAPI)، اختبارات الحمل.
* **مستودع القطع الأثرية** للخطط، والاختلافات، والسجلات؛ لوحات تحكم Grafana لمؤشرات مستوى الخدمة/أهداف مستوى الخدمة.
* **أسرار وحوكمة البيانات**: رموز محددة النطاق، إخفاء، مستودعات مسموح بها.

---

# متى يمكنك حقًا الانتقال إلى "لا مراقبة بالكامل"

* المهمة **ضيقة** وقابلة للتكرار (مثال: مزامنة المستندات، نماذج اختبارية قياسية، إعادة هيكلة روتينية).
* لديك **اختبارات أوراكل جيدة** أو ثوابت قوية.
* قمت بتشغيل **الوضع الظلي/التجريبي** بنجاح دون تدخل لفترة.
* نطاق التأثير محدود (اختلافات صغيرة، قابلة للعكس، معزولة).

لأي شيء آخر، حافظ على **التدخل البشري في حالات الاستثناء**. ستظل تحصل على 80-95% من مكاسب الإنتاجية دون المخاطرة بفشل صامت.

إذا أردت، يمكنني تكييف الهيكل لمكدسك المحدد (Python/Java Maven, Ruff/Mypy/PyTest, أو Maven/Gradle + SpotBugs/Checkstyle/JUnit) وتوصيله بإعدادات الموجه الخاصة بك.