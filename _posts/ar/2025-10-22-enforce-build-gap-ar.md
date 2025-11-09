---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: فرض فاصل زمني للبناء لمدة ٣٠ دقيقة
translated: true
type: note
---

### تعديل سير العمل لفرض فجوة زمنية مدتها 30 دقيقة بين عمليات البناء

لضمان عدم تشغيل سير عمل النشر الخاص بـ Jekyll بشكل متكرر جداً (أي بفجوة لا تقل عن 30 دقيقة بين عمليات التشغيل المتتالية)، يمكنك إضافة خطوة شرطية مبكراً في وظيفة `build`. ستقوم هذه الخطوة باستعلام GitHub API عن الطابع الزمني لآخر تشغيل ناجح لسير العمل هذا. إذا كان التشغيل الحالي ضمن 30 دقيقة من اكتمال ذلك التشغيل، فستخرج الوظيفة مبكراً برسالة (متخطية عملية البناء).

هذا النهج:
- يستخدم GitHub REST API (لا حاجة لأدوات خارجية).
- يتحقق فقط من عمليات التشغيل السابقة **الناجحة** (الحالة: "completed"، النتيجة: "success").
- يحسب فرق الوقت بالثواني ويقارنه بـ 1800 (30 دقيقة).
- يعمل مع مشغلات `push` و `workflow_dispatch` الحالية.
- لا يتعارم مع إعداد التزامن (والذي يتعامل مع عمليات التشغيل المتداخلة).

#### مقتطف YAML المحدث
أدخل هذه الخطوة الجديدة مباشرة بعد خطوة "Checkout Repository" في وظيفة `build` الخاصة بك. يبقى باقي سير العمل دون تغيير.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: فرض فجوة بناء مدتها 30 دقيقة
        id: cooldown
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # جلب آخر تشغيل ناجح لسير العمل هذا
          RUNS_RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${{ github.repository }}/actions/workflows/${{ github.workflow_ref }}/runs?status=completed&conclusion=success&per_page=1&sort=timestamp&direction=desc")

          # استخراج الطابع الزمني completed_at لآخر تشغيل ناجح (تنسيق ISO 8601)
          LAST_COMPLETED_AT=$(echo "$RUNS_RESPONSE" | jq -r '.[0].completed_at // empty')
          
          if [ -z "$LAST_COMPLETED_AT" ] || [ "$LAST_COMPLETED_AT" = "null" ]; then
            echo "لم يتم العثور على تشغيل ناجح سابق. المتابعة بعملية البناء."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

          # تحويل الطوابع الزمنية إلى ثواني Unix للمقارنة
          CURRENT_TIME=$(date -u +%s)
          LAST_TIME=$(date -d "$LAST_COMPLETED_AT" +%s)
          TIME_DIFF=$((CURRENT_TIME - LAST_TIME))

          echo "اكتمل آخر تشغيل ناجح في: $LAST_COMPLETED_AT (الفرق: ${TIME_DIFF}s)"

          if [ $TIME_DIFF -lt 1800 ]; then  # 1800 ثانية = 30 دقيقة
            echo "تم تخطي البناء: أقل من 30 دقيقة منذ آخر تشغيل ناجح."
            echo "skip_build=true" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "فجوة زمنية كافية. المتابعة بعملية البناء."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

      # تخطي البناء بالكامل إذا فشلت فحص فترة التهدئة (أضف هذا الشرط إلى الخطوات اللاحقة أو ضع البناء داخل شرط if)
      - name: Set up Python 3.13.2
        if: steps.cooldown.outputs.skip_build != 'true'
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      # ... (كرر الشرط 'if: steps.cooldown.outputs.skip_build != 'true'' على جميع الخطوات المتبقية بعد هذه)
```

#### التغييرات الرئيسية موضحة
1. **استعلام API**:
   - يستخدم `curl` للوصول إلى نقطة نهاية GitHub Actions API الخاصة بتشغيلات سير العمل.
   - يرشح للحصول على `status=completed` و `conclusion=success` للحصول فقط على عمليات التشغيل المنتهية والناجحة.
   - يقتصر على `per_page=1` ويرتب حسب `timestamp desc` للحصول على أحدث تشغيل.
   - يستخرج `completed_at` (وقت الانتهاء الدقيق للتشغيل السابق).

2. **حساب الوقت**:
   - يحول كل من الوقت الحالي ووقت اكتمال التشغيل الأخير إلى طوابع زمنية Unix باستخدام `date`.
   - يحسب الفرق بالثواني.
   - إذا كان الفرق `< 1800` ثانية، يضبط `skip_build=true` ويخرج من الخطوة مبكراً.

3. **التنفيذ الشرطي**:
   - أضف `if: steps.cooldown.outputs.skip_build != 'true'` إلى **كل خطوة لاحقة** (مثل إعداد Python، تثبيت التبعيات، وصولاً إلى مزامنة الموقع المُنشأ).
   - يضمن هذا أن الوظيفة تبلغ عن "تم التخطي" في واجهة GitHub إذا تم تشغيل فترة التهدئة، ولكنها لا تزال تسجل السبب.

4. **حالات الطوارئ التي تم التعامل معها**:
   - لا توجد عمليات تشغيل سابقة: تتابع (أول بناء).
   - عمليات تشغيل سابقة فاشلة أو قيد التنفيذ: تتجاهلها وتتابع.
   - أخطاء API: ترجع إلى المتابعة (الافتراضي الآمن).
   - `jq` مثبت مسبقاً على `ubuntu-latest`، لذلك لا حاجة لإعداد إضافي.

#### اختبار التغيير
- قم بإيداع هذا في فرع `main` الخاص بك (سيؤدي هذا إلى تشغيل سير العمل).
- قم بتشغيل عدة عمليات `push` / `dispatches` سريعة متعددة: يجب أن يتخطى التشغيل الثاني الذي يحدث خلال 30 دقيقة.
- راقب سجلات الوظيفة للعثور على رسالة "تم تخطي البناء".
- إذا كنت تريد ضبط الفجوة (مثلاً إلى ساعة واحدة)، غيّر `1800` إلى `3600`.

#### البدائل
- **مشغل مجدول**: إذا كنت تريد عمليات بناء *دورية* كل 30 دقيقة (بغض النظر عن عمليات `push`)، أضف هذا إلى قسم `on:`:
  ```yaml
  schedule:
    - cron: '*/30 * * * *'  # كل 30 دقيقة
  ```
  لكن هذا لا يفرض فجوة على مشغلات `push` — استخدمه إلى جانب خطوة التهدئة إذا لزم الأمر.
- **إجراء مخصص**: لإمكانية إعادة الاستخدام، قم بتغليف منطق التهدئة في سير عمل قابل لإعادة الاستخدام أو إجراء مركب.
- **القيود**: يتحقق هذا من وقت اكتمال التشغيل، وليس وقت البدء. إذا كان التشغيل السابق لا يزال قيد التشغيل لأكثر من 30 دقيقة، فسيقوم التزامن بإلغائه على أي حال.

إذا كان هذا لا يتناسب مع هدفك الدقيق (مثلاً، إذا كنت تقصد التجد*يد على الأقل* كل 30 دقيقة)، قدم المزيد من التفاصيل!