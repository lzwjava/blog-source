---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: رؤية القائمة المنسدلة والبدائل
translated: true
type: note
---

في مقتطف HTML المقدم، أنت تستخدم عناصر `<select>`، والتي تُعرض افتراضيًا كقوائم منسدلة. هذا يعني أن المستخدمين يمكنهم رؤية الخيار المحدد حاليًا فقط بنظرة سريعة—بينما تكون الخيارات الأخرى مخفية حتى النقر على القائمة المنسدلة أو توسيعها (عبر التفاعل باستخدام لوحة المفاتيح/الماوس). هذا هو السلوك القياسي لعنصر `<select>` في HTML، حيث تم تصميمه للاختيار المدمج من قائمة دون تشويش واجهة المستخدم.

لا يحتوي HTML على عنصر "مفتاح تبديل" مدمج خصيصًا لتبديل رؤية الخيارات في `<select>`. ومع ذلك، هناك عدة طرق لتحقيق ما تصفه (جعل جميع الخيارات مرئية بدون قائمة منسدلة، أو توفير مفتاح تبديل لإظهار/إخفائها). سأوضح إيجابيات/سلبيات وأمثلة كود أدناه. تستخدم هذه الأساليب HTML/CSS الأصلي حيثما أمكن، مع JavaScript اختياري للتفاعلية. نظرًا لأن الكود الخاص بك يبدو جزءًا من موقع Jekyll (بناءً على قالب Liquid)، يجب أن تندمج هذه الحلول بسهولة.

### 1. **استخدام أزرار الراديو بدلاً من `<select>` (خيارات مرئية دائمًا)**
   - **لماذا؟** تعرض أزرار الراديو (`<input type="radio">`) جميع الخيارات في سطر أو في قائمة، مما يجعلها مرئية بالكامل دون أي تفاعل. هذا رائع للقوائم القصيرة (مثل type-select الذي يحتوي على خيارين) ولكن يمكن أن يصبح مزدحمًا للقوائم الأطول (مثل language-sort الذي يحتوي على 9 خيارات).
   - **الإيجابيات:** لا حاجة لـ JS؛ سهل الوصول؛ يرى المستخدمون كل شيء فورًا.
   - **السلبيات:** يأخذ مساحة أكبر؛ يتطلب JS للتعامل مع منطق "الاختيار" إذا كنت بحاجة إلى تشغيل إجراءات (مثل ترتيب/تصفية المنشورات).
   - **كود المثال:**
     استبدل `<select>` الخاص بك بمجموعة من أزرار الراديو. ضعهم داخل `<fieldset>` لدلالات وسهولة الوصول.

     ```html
     <div class="sort-container">
       <!-- Type selection as radios -->
       <fieldset>
         <legend>Type</legend>
         <label>
           <input type="radio" name="type" value="posts" checked> Posts
         </label>
         <label>
           <input type="radio" name="type" value="notes"> Notes
         </label>
       </fieldset>

       <!-- Language sort as radios -->
       <fieldset>
         <legend>Sort by Language</legend>
         <label>
           <input type="radio" name="sort" value="en" checked> English
         </label>
         <label>
           <input type="radio" name="sort" value="zh"> 中文
         </label>
         <label>
           <input type="radio" name="sort" value="ja"> 日本語
         </label>
         <!-- Add more labels for es, hi, fr, de, ar, hant -->
       </fieldset>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} Translated by <a href="https://openrouter.ai">AI</a>)
         </span>
       </div>
     </div>
     ```

     - أضف CSS للتنسيق (على سبيل المثال، لجعلها تبدو كأزرار):
       ```css
       fieldset {
         border: none; /* Remove default border */
         display: flex;
         gap: 10px;
       }
       label {
         background: #f0f0f0;
         padding: 5px 10px;
         border-radius: 5px;
         cursor: pointer;
       }
       input[type="radio"] {
         appearance: none; /* Hide default radio circle */
       }
       input[type="radio"]:checked + span { /* If using <span> inside label for text */
         background: #007bff;
         color: white;
       }
       ```
     - للوظيفة: استخدم JS للاستماع للتغييرات (مثل `addEventListener('change')`) وتحديث واجهة المستخدم أو تشغيل عملية الفرز.

### 2. **استخدام الأزرار أو عناصر Div للخيارات القابلة للنقر ("مجموعة أزرار" مخصصة)**
   - **لماذا؟** إذا كنت تريد واجهة تشبه الأزرار أكثر، استخدم عناصر `<button>` أو `<div>` مُنسقة كأزرار. هذا يعرض جميع الخيارات بشكل مرئي ويسمح بالتبديل المخصص.
   - **الإيجابيات:** تنسيق مرن؛ يمكن محاكاة علامات التبويب أو الحبوب؛ سهل جعله متجاوبًا.
   - **السلبيات:** يتطلب JS لإدارة الحالات النشطة والإجراءات؛ ليس صحيحًا دلاليًا مثل عناصر النموذج (استخدم سمات ARIA لسهولة الوصول).
   - **كود المثال:**
     ```html
     <div class="sort-container">
       <!-- Type as button group -->
       <div class="button-group" role="group" aria-label="Type selection">
         <button data-type="posts" class="active">Posts</button>
         <button data-type="notes">Notes</button>
       </div>

       <!-- Language as button group -->
       <div class="button-group" role="group" aria-label="Language selection">
         <button data-sort="en" class="active">English</button>
         <button data-sort="zh">中文</button>
         <button data-sort="ja">日本語</button>
         <!-- Add more buttons for other languages -->
       </div>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} Translated by <a href="https://openrouter.ai">AI</a>)
         </span>
       </div>
     </div>
     ```

     - CSS لتنسيق الأزرار:
       ```css
       .button-group {
         display: flex;
         gap: 5px;
         flex-wrap: wrap; /* For long lists */
       }
       button {
         padding: 5px 10px;
         border: 1px solid #ccc;
         border-radius: 5px;
         cursor: pointer;
       }
       button.active {
         background: #007bff;
         color: white;
       }
       ```
     - JS للتعامل مع النقرات (أضف هذا في وسم `<script>` أو ملف خارجي):
       ```javascript
       document.querySelectorAll('.button-group button').forEach(button => {
         button.addEventListener('click', function() {
           // Remove active from siblings
           this.parentNode.querySelectorAll('button').forEach(btn => btn.classList.remove('active'));
           this.classList.add('active');
           // Trigger your sort logic here, e.g., update post-number or filter content
           console.log('Selected:', this.dataset.type || this.dataset.sort);
         });
       });
       ```

### 3. **إضافة مفتاح تبديل لتوسيع الخيارات (أسلوب هجين)**
   - **لماذا؟** إذا كنت تريد الحفاظ على `<select>` المدمج ولكن السماح للمستخدمين "بالتبديل" إلى عرض يُظهر جميع الخيارات، استخدم خانة اختيار مُنسقة كمفتاح تبديل لإظهار/إخفاء قائمة موسعة.
   - **الإيجابيات:** يحافظ على التصميم المدمج الافتراضي؛ HTML أصلي للتبديل.
   - **السلبيات:** يتطلب CSS/JS؛ يضيف تعقيدًا.
   - **المثال:** استخدم `<input type="checkbox">` للتبديل، وبدّل رؤية div يحتوي على جميع الخيارات المدرجة.
     ```html
     <div class="sort-container">
       <!-- Your original selects here -->

       <!-- Toggle switch -->
       <label class="switch">
         <input type="checkbox" id="show-all-toggle">
         <span>Show All Options</span>
       </label>

       <!-- Hidden expanded view -->
       <div id="expanded-options" style="display: none;">
         <!-- List all type and sort options as plain text or buttons -->
         <ul>
           <li>Posts</li>
           <li>Notes</li>
           <li>English</li>
           <li>中文</li>
           <!-- etc. -->
         </ul>
       </div>

       <!-- Your post-number span -->
     </div>
     ```

     - CSS للتبديل:
       ```css
       .switch input {
         opacity: 0;
         width: 0;
         height: 0;
       }
       .switch span {
         /* Style as a toggle slider */
         position: relative;
         display: inline-block;
         width: 40px;
         height: 20px;
         background: #ccc;
         border-radius: 20px;
         transition: background 0.3s;
       }
       .switch input:checked + span {
         background: #007bff;
       }
       /* Add a slider knob with ::before or ::after */
       ```
     - JS للتبديل:
       ```javascript
       document.getElementById('show-all-toggle').addEventListener('change', function() {
         document.getElementById('expanded-options').style.display = this.checked ? 'block' : 'none';
       });
       ```

### التوصيات
- بالنسبة لـ **type-select** الخاص بك (خياران فقط)، تعمل أزرار الراديو أو الأزرار بشكل جيد وتحافظ على البساطة.
- بالنسبة لـ **sort-select** (9 لغات)، الأزرار في مجموعة جيدة إذا سمحت المساحة؛ وإلا، التزم باستخدام `<select>` وأضف تلميحًا أو تسمية توضيحية تشرح ذلك.
- اختبر سهولة الوصول (على سبيل المثال، باستخدام قارئات الشاشة) والاستجابة للجوال.
- إذا كان هذا لموقع ديناميكي، قم بدمجه مع JS الحالي لتحديث `post-number` بناءً على الاختيارات.

إذا كان هذا لا يتطابق مع ما قصدته بـ "مفتاح تبديل"، أو إذا شاركت المزيد من السياق (على سبيل المثال، ما الذي تفعله عناصر الاختيار)، يمكنني تحسين هذا!