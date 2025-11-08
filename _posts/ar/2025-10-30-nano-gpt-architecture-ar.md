---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: ملخص بنية نموذج نانو جي بي تي
translated: true
type: note
---

### نظرة عامة على بنية نموذج NanoGPT

ينفذ NanoGPT نموذج محول (transformer) من نوع المُشَفِّر فقط (decoder-only) شبيه بـ GPT-2 في PyTorch. يتم تعريف البنية في ملف `model.py`، مع تكوين `GPTConfig` قابل للتخصيص يحدد المعاملات الفائقة (hyperparameters). يستخدم التكوين الافتراضي (على سبيل المثال، للنسخة "gpt2"):

- **عدد كتل المحولات (transformer blocks)**: 12 (`n_layer = 12`)
- **بُعد التضمين (حجم الطبقة)**: 768 (`n_embd = 768`)
- **عدد رؤوس الانتباه (attention heads)**: 12 (`n_head = 12`)
- **الحجم الوسيط لـ MLP**: 3072 (`n_embd * 4`، حيث أن معامل التمدد هو 4)

كل كتلة محول (الفئة `Block`) هي كتلة مشفّر قياسية مع اتصالات متبقية (residual connections) وتطبيع طبقي (layer normalization). وهي تتضمن:
- **LayerNorm 1** (`ln1`): يُطبق قبل الانتباه الذاتي (self-attention).
- **انتباه ذاتي متعدد الرؤوس** (`attn`): انتباه سببي (مقنع) لمنع النظر إلى المستقبل.
- إضافة متبقية بعد الانتباه.
- **LayerNorm 2** (`ln2`): يُطبق قبل الـ MLP.
- **MLP** (`mlp`): شبكة تغذية أمامية بسيطة (feed-forward network).
- إضافة متبقية بعد الـ MLP.

النموذج العام (الفئة `GPT`) يركّب هذه الكتل الـ 12 بعد تضمينات الرمز (token) والموضع (position)، يليها تطبيع طبقي نهائي (`ln_f`) وإسقاط خطي (linear projection) إلى حجم المفردات (vocabulary size).

#### هيكل الـ MLP
الـ MLP (الفئة `MLP` داخل `Block`) هي شبكة تغذية أمامية من طبقتين:
- الطبقة الخطية الأولى (`c_fc`): تُسقط من `n_embd` (768) إلى الحجم الوسيط (3072).
- تفعيل GELU: يُطبق بشكل عنصري بعد الإسقاط الأول.
- الطبقة الخطية الثانية (`c_proj`): تُسقط مرة أخرى من 3072 إلى `n_embd` (768).

هذا يتبع النمط "fc -> gelu -> projection" الذي ذكرته.

#### تدفق التمرير الأمامي (Forward Pass)
تمريرات الأمام هي من النمط المتبقي (residual-style)، مع pre-norm (تطبيع طبقي قبل الطبقات الفرعية). إليك تفصيل عالي المستوى:

1.  **التمرير الأمامي الرئيسي (GPT.forward)**:
    - تضمينات الرمز (Token embeddings): الرموز المدخلة (الشكل `[B, T]`) → تضمينات (الشكل `[B, T, n_embd]`).
    - تضمينات الموضع (Positional embeddings): تُضاف إلى تضمينات الرمز.
    - المرور عبر كومة كتل المحولات الـ `n_layer` (12): `x = block(x)` لكل كتلة.
    - التطبيع الطبقي النهائي: `x = self.ln_f(x)`.
    - الإسقاط الخطي: `logits = self.lm_head(x)` → شكل المخرجات `[B, T, vocab_size]`.

    مقتطف (مبسط):
    ```python
    def forward(self, idx, targets=None):
        # ... embedding + positional
        for block in self.blocks:
            x = block(x)
        x = self.ln_head(x)
        logits = self.head(x)
        # ... loss if targets
        return logits
    ```

2.  **التمرير الأمامي في كتلة المحول (Block.forward)**:
    - تطبيق `ln1` على المدخل `x`.
    - الانتباه الذاتي: `x = x + attn(ln1(x))` (متبقي).
    - تطبيق `ln2` على النتيجة.
    - MLP: `x = x + mlp(ln2(x))` (متبقي).

    مقتطف (مبسط):
    ```python
    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x
    ```

3.  **التمرير الأمامي في الانتباه الذاتي (MultiheadAttention.forward)**:
    - مدخل LayerNorm → حساب إسقاطات Q, K, V (الطبقات الخطية `c_attn`).
    - تقسيم إلى رؤوس، تطبيق قناع سببي، انتباه النقطة الحاصل المقيّس (scaled dot-product attention).
    - دمج الرؤوس، الإسقاط مرة أخرى باستخدام `c_proj`.
    - إضافة متبقية (ولكن في الكتلة، تتم الإضافة خارجيًا).

    المفتاح: يضمن القناع السببي (Causal mask) تجاهل الرموز المستقبلية. يتم الحفاظ على شكل المخرجات كـ `[B, T, n_embd]`.

    مقتطف (حساب الانتباه الأساسي، مبسط):
    ```python
    def forward(self, x):
        B, T, C = x.shape
        qkv = self.c_attn(x).split(self.n_embd, dim=2)  # Q,K,V
        # ... reshape to heads, mask, attn = q @ k.transpose / sqrt
        # attn = attn.masked_fill(mask == 0, -1e9)
        # y = attn @ v
        # ... concat and project
        return self.c_proj(y.reshape(B, T, C))
    ```

4.  **التمرير الأمامي في الـ MLP (MLP.forward)**:
    - الإسقاط الأول: `x = self.c_fc(x)` → إلى الحجم الوسيط.
    - GELU: `x = F.gelu(x)`.
    - الإسقاط الثاني: `x = self.c_proj(x)` → مرة أخرى إلى `n_embd`.

    مقتطف:
    ```python
    def forward(self, x):
        x = self.c_fc(x)
        x = F.gelu(x)
        x = self.c_proj(x)
        return x
    ```

هذا الإعداد يحاكي بنية GPT-2 عن كثب، بحوالي ~124 مليون معامل (parameter) في التكوين الافتراضي. للحصول على الكود الدقيق، راجع المستودع.

[model.py source](https://github.com/karpathy/nanoGPT/blob/master/model.py)