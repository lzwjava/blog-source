---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: सत्यापन के साथ ऊर्ध्वाधर एजेंटों का स्वचालन
translated: true
type: note
---

संक्षिप्त उत्तर: आप **ज्यादातर सही** हैं। स्केलेबल तरीका है **वर्टिकल, कोडेड एजेंट** बनाना जो LLM एपीआई को कॉल करते हैं, साथ ही मजबूत **ऑटोमैटिक वैलिडेशन** हो। आप अभी भी "ह्यूमन-ऑन-एक्सेप्शन" लूप चाहते हैं, "ह्यूमन-नेवर" नहीं, क्योंकि वास्तविकता में एपीआई हिचकिचाहट, ड्रिफ्ट और एज केस शामिल हैं। लेकिन अच्छी तरह से स्कोप किए गए टास्क्स और अच्छी जांचों के साथ, आप **पूरी तरह से ऑटोमेटेड** चला सकते हैं।

नीचे एक प्रैक्टिकल ब्लूप्रिंट है जिसे आप इम्प्लीमेंट कर सकते हैं।

# "पूरी तरह से ऑटोमेटेड" के लिए वास्तव में क्या चाहिए

* **डिटरमिनिस्टिक स्कैफोल्डिंग**: कोड प्लान/टेम्पलेट एक बार जनरेट होते हैं, फिर **पैरामीटराइज्ड** होते हैं; हर रन "स्क्रैच से दोबारा प्रॉम्प्ट" न करें।
* **टाइप्ड, स्कीमा वाला I/O**: LLM को JSON रिटर्न करने के लिए मजबूर करें जिसे आपका कोड इस्तेमाल से पहले वैलिडेट करे।
* **ग्राउंडेड चेक**: आउटपुट को टूल्स, कंपाइलर्स, यूनिट टेस्ट, लिंटर्स, HTTP मॉक, SQL स्कीमा आदि के खिलाफ वैलिडेट करें।
* **रिस्क गेटिंग**: केवल तब ऑटो-एप्लाई करें जब कॉन्फिडेंस + चेक पास हों; अन्यथा रिव्यू के लिए टिकट/PR बनाएं।
* **ऑब्जर्वेबिलिटी**: लॉग, ट्रेस, कॉस्ट/लेटेंसी मीटर, सक्सेस रेट, ड्रिफ्ट/अलार्म थ्रेशोल्ड।
* **डिफेंस इन डेप्थ**: मल्टी-मॉडल क्रॉस-चेक, सेल्फ-कंसिस्टेंसी वोट, सैंडबॉक्स एक्ज़ेक, डिफ साइज लिमिट, अलाउलिस्ट/डिनाइलिस्ट।

# रेफरेंस आर्किटेक्चर (मिनिमल लेकिन सॉलिड)

* **कंट्रोलर**: कतार (Kafka/SQS/Redis/सिंपल DB) से टास्क पढ़ता है।
* **प्लानर** (LLM): टास्क को कंक्रीट प्लान और स्ट्रक्चर्ड स्टेप्स में बदलता है।
* **एक्ज़ीक्यूटर** (टूल्स + जहां जरूरी हो LLM): कोड एडिट, एपीआई कॉल, फाइल ऑपरेशन।
* **वैलिडेटर**: स्कीमा/टाइप चेक, स्टैटिक एनालिसिस, यूनिट टेस्ट, गोल्डन टेस्ट।
* **पॉलिसी इंजन**: ऑटो-मर्ज बनाम "नीड्स ह्यूमन" का फैसला करता है।
* **रिपोर्टर**: PR खोलता है, इश्यू बनाता है, Slack/Email सारांश पोस्ट करता है।

# वैलिडेशन पैटर्न जो वास्तव में काम करते हैं

* JSON स्कीमा + वैलिड होने तक रिट्राई।
* AST पार्स + बेसिक सेमेंटिक्स (जैसे, क्लास/मेथड का अस्तित्व सुनिश्चित करना)।
* **ruff/mypy/flake8**, कवरेज थ्रेशोल्ड के साथ **pytest**, सुरक्षा के लिए **bandit** चलाएं।
* टेक्स्ट/डेटा के लिए: रेगेक्स इनवेरिएंट्स, रेफरेंस आंसर, BLEU/ROUGE थ्रेशोल्ड, या बिज़नेस नियम।
* एक्सटर्नल सिस्टम कॉल करने के लिए: पहले मॉक/स्टब करें; **रीड-ओनली** या **शैडो** मोड के साथ प्रोड में कैनरी; फिर प्रोग्रेसिव रोलआउट।

---

# स्टार्टर: Python "वर्टिकल एजेंट" स्केलेटन

यह टास्क को पैरेलल में चलाता है, JSON आउटपुट फोर्स करता है, वैलिडेट करता है, लोकल चेक चलाता है, और या तो ऑटो-एप्लाई करता है या PR खोलता है। `call_llm()` स्टब को अपने प्रोवाइडर/राउटर से बदलें।

```python
import asyncio, json, os, re, subprocess, time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List, Tuple, Callable

# ---------- टास्क स्पेक ----------
@dataclass
class Task:
    id: str
    kind: str            # जैसे, "refactor", "write_test", "doc_summarize"
    repo_path: str
    target: str          # फाइल/पाथ/मॉड्यूल या URL
    spec: Dict[str, Any] # फ्री-फॉर्म डिटेल्स

# ---------- LLM कॉल (यहां अपना राउटर स्टब करें) ----------
async def call_llm(system: str, user: str, schema_hint: str, max_retries=3) -> Dict[str, Any]:
    """
    स्ट्रक्चर्ड JSON रिटर्न करें। आपका रियल इम्प्ल: Anthropic/OpenAI/Gemini/Mistral राउटर के साथ
    टूल फोर्सिंग / JSON मोड / 'respond_with_schema' आदि।
    """
    last_err = None
    for _ in range(max_retries):
        # >>> JSON मोड में रियल एपीआई कॉल से बदलें <<<
        fake = {"plan": ["edit file", "run tests"], "edits":[{"path":"foo.py","patch":"print('ok')\n"}], "confidence": 0.92}
        try:
            # बेसिक फील्ड्स को जल्दी वैलिडेट करें
            if not isinstance(fake.get("edits"), list): raise ValueError("bad edits")
            return fake
        except Exception as e:
            last_err = e
    raise RuntimeError(f"LLM failed to produce valid JSON: {last_err}")

# ---------- वैलिडेटर ----------
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
    # अपने टूल्स से बदलें: ruff, mypy, eslint, mvn test, gradle, आदि।
    codes = []
    outputs = []

    # उदाहरण Python चेक; अगर टूल्स मिसिंग हों तो गार्ड करें।
    for cmd in [["python","-m","py_compile","."]]:
        rc, out = run_cmd(cmd, cwd=repo_path)
        codes.append(rc); outputs.append(out or "")
    ok = all(rc == 0 for rc in codes)
    return ok, "\n".join(outputs)

def unit_tests(repo_path: str) -> Tuple[bool, str]:
    # जरूरत के हिसाब से pytest/mvn/gradle/npm test से बदलें
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

# ---------- वर्कर ----------
async def worker(task: Task, max_diff_lines=800) -> Dict[str, Any]:
    system_prompt = "You are a strict code agent. Output JSON only and follow the schema."
    user_prompt = json.dumps(asdict(task), ensure_ascii=False)
    schema_hint = '{"plan":[str], "edits":[{"path":str,"patch":str}], "confidence": float}'

    payload = await call_llm(system_prompt, user_prompt, schema_hint)
    ok, why = json_schema_validate(payload)
    if not ok:
        return {"task": task.id, "status":"FAILED", "reason": f"schema: {why}"}

    # सैंडबॉक्स ब्रांच में एडिट्स एप्लाई करें
    run_cmd(["git","checkout","-B", f"agent/{task.id}"], cwd=task.repo_path)
    for e in payload["edits"]:
        apply_patch(task.repo_path, e["path"], e["patch"])
    run_cmd(["git","add","-A"], cwd=task.repo_path)
    run_cmd(["git","commit","-m", f"agent: {task.kind} {task.target}"], cwd=task.repo_path)

    # वैलिडेट करें
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
        # मुख्य में मर्ज करें; या पुश करें और CI रूल्स के जरिए ऑटो-मर्ज करें
        run_cmd(["git","checkout","main"], cwd=task.repo_path)
        run_cmd(["git","merge","--no-ff", f"agent/{task.id}"], cwd=task.repo_path)
        result["status"] = "APPLIED"
    else:
        # सीधे मर्ज करने के बजाय अपने CI बॉट के जरिए PR खोलें
        result["status"] = "REVIEW"
        result["note"] = "Opened PR or created issue for human-on-exception."
    return result

# ---------- ऑर्केस्ट्रेटर ----------
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

# उदाहरण उपयोग:
# asyncio.run(run_queue([Task(id="1", kind="refactor", repo_path="/path/to/repo", target="foo.py", spec={"goal":"extract fn"})]))
```

## यह आपको "नो चैट, जस्ट कोड" कैसे देता है

* **प्लानर** स्ट्रक्चर्ड एडिट्स तैयार करता है।
* **वैलिडेटर** शुद्धता को गेट करते हैं।
* **पॉलिसी इंजन** सुरक्षित डिफ को ऑटो-एप्लाई करता है, बाकी को रिव्यू के लिए रूट करता है।
* आप चैटबॉट से "बात" नहीं करते। आप टास्क सबमिट करते हैं (YAML/JSON या CLI), और सिस्टम एक्ज़ीक्यूट करता है।

---

# अपग्रेड जो आप शायद जोड़ेंगे

* **मल्टी-मॉडल राउटर** फॉलबैक और सेल्फ-कंसिस्टेंसी वोटिंग के साथ।
* **JSON-मोड एनफोर्समेंट** एक ऐसे टूल के साथ जो स्कीमा-वैलिड होने तक दोबारा प्रॉम्प्ट करे।
* **डोमेन वैलिडेटर**: DB माइग्रेशन ड्राई-रन, एपीआई कॉन्ट्रैक्ट चेक (OpenAPI), लोड टेस्ट।
* **आर्टिफैक्ट स्टोर** प्लान, डिफ, लॉग के लिए; SLI/SLO के लिए Grafana डैशबोर्ड।
* **सीक्रेट्स और डेटा गवर्नेंस**: स्कोप्ड टोकन, रिडक्शन, अलाउलिस्टेड रेपो।

---

# जब आप वास्तव में "पूरी तरह से अनअटेंडेड" जा सकते हैं

* टास्क **नैरो** और रिपीटेबल है (जैसे, डॉक सिंक, बॉयलरप्लेट टेस्ट स्टब्स, रूटीन रिफैक्टर)।
* आपके पास **अच्छे ओरेकल टेस्ट** या मजबूत इनवेरिएंट्स हैं।
* आपने **शैडो/कैनरी** जीरो-टच के साथ सफलतापूर्वक कुछ समय तक चलाया है।
* ब्लास्ट रेडियस लिमिटेड है (छोटे डिफ, रिवर्सिबल, सैंडबॉक्स्ड)।

बाकी सबके लिए, **ह्यूमन-ऑन-एक्सेप्शन** बनाए रखें। आपको साइलेंट फेल्योर का जोखिम उठाए बिना अभी भी 80-95% प्रोडक्टिविटी विंस मिल जाएंगी।

अगर आप चाहें, तो मैं इस स्केलेटन को आपके एक्ज़ैक्ट स्टैक (Python/Java Maven, Ruff/Mypy/PyTest, या Maven/Gradle + SpotBugs/Checkstyle/JUnit) के अनुकूल बना सकता हूं और इसे आपके राउटर कॉन्फिग से वायर कर सकता हूं।