---
audio: false
generated: true
lang: ar
layout: post
title: 'Git المتقدم: إعادة التوجيه، الدمج، حل التعارضات، والدمج المكثف'
translated: true
type: note
---

يغطي هذا الدليل الاستخدام المتقدم لـ `git rebase` و `git merge`، وحل التعارضات، واستخدام استراتيجيات `ours` و `theirs`، ودمج (squash) commits. سأقدم شرحًا موجزًا وأمثلة عملية لكل موضوع، مع التركيز على سير العمل المتقدمة التي تفترض الإلمام بأوامر Git الأساسية.

## 1. Git Merge: استخدام متقدم
`git merge` يجمع تسلسلات متعددة من التطوير في تاريخ موحد واحد. يشمل الاستخدام المتقدم التعامل مع عمليات الدمج المعقدة، واستخدام استراتيجيات الدمج، وإدارة commitات الدمج.

### استراتيجيات الدمج الرئيسية
- **Recursive (الافتراضي)**: يتعامل مع أسلاف مشتركة متعددة وهو مناسب لمعظم عمليات الدمج.
  - مثال: `git merge --strategy=recursive branch-name`
- **Ours**: يحتفظ بالتغييرات في الفرع الحالي، ويتجاهل التغييرات من الفرع المدمج.
  - مثال: `git merge --strategy=ours feature-branch`
- **Theirs**: ليست استراتيجية حقيقية ولكن يمكن محاكاتها (انظر أدناه لحل التعارض).
- **Octopus**: يدمج عدة فروع في وقت واحد (يستخدم لأكثر من فرعين).
  - مثال: `git merge branch1 branch2 branch3`

### خيارات الدمج المتقدمة
- `--no-ff`: يجبر على إنشاء commit دمج حتى لو كان الدمج السريع (fast-forward) ممكنًا، مما يحفظ تاريخ الفرع.
  - مثال: `git merge --no-ff feature-branch`
- `--squash`: يدمج جميع commits من الفرع المدمج في commit واحد على الفرع الحالي.
  - مثال: `git merge --squash feature-branch && git commit`
- `--allow-unrelated-histories`: يدمج فروعًا ليس لها تاريخ مشترك.
  - مثال: `git merge --allow-unrelated-histories external-repo-branch`

### مثال: الدمع بدون دمج سريع (No Fast-Forward)
```bash
git checkout main
git merge --no-ff feature-branch
# ينشئ commit دمج، مما يحفظ تاريخ feature-branch
```

## 2. Git Rebase: استخدام متقدم
`git rebase` يعيد كتابة التاريخ عن طريق نقل أو تعديل commits لإنشاء تاريخ خطي. إنه قوي لتنظيف الفروع لكنه يغير التاريخ، لذا استخدمه بحذر على الفروع المشتركة.

### أنواع Rebase
- **Rebase قياسي**: يعيد تشغيل commits من الفرع الحالي على الفرع الأساسي.
  - مثال: `git rebase main` (أثناء التواجد على `feature-branch`)
- **Rebase تفاعلي**: يسمح بتحرير أو دمج أو إعادة ترتيب commits.
  - مثال: `git rebase -i main`

### أوامر Rebase التفاعلي
شغِّل `git rebase -i <base>` (مثال: `git rebase -i HEAD~3` لآخر 3 commits). هذا يفتح محررًا بأوامر مثل:
- `pick`: احتفظ بال commit كما هو.
- `reword`: حرر رسالة commit.
- `edit`: أوقف rebase لتعديل commit.
- `squash`: ادمج مع commit السابق.
- `fixup`: مثل squash، لكنه يتجاهل رسالة commit.
- `drop`: احذف commit.

### مثال: Rebase تفاعلي
لدمج آخر 3 commits:
```bash
git rebase -i HEAD~3
# في المحرر، غيّر "pick" إلى "squash" أو "fixup" لـ commits المراد دمجها
# احفظ واخرج لإكمال العملية
```

### Rebase على قاعدة مختلفة
لنقل فرع إلى قاعدة جديدة (مثال: نقل `feature-branch` من `old-base` إلى `main`):
```bash
git rebase --onto main old-base feature-branch
```

### Rebase مع commits دمج
بشكل افتراضي، يقوم rebase بتسطيح commits الدمج. للحفاظ عليها:
```bash
git rebase -i --preserve-merges main
```

### إحباط Rebase
إذا حدث خطأ ما:
```bash
git rebase --abort
```

## 3. حل تعارضات الدمج/Rebase
تحدث التعارضات عندما لا يستطيع Git التوفيق التلقائي بين التغييرات. كل من `merge` و `rebase` يمكن أن يؤديان إلى تعارضات، يتم حلها بشكل similar.

### خطوات حل التعارضات
1. **تحديد التعارضات**: يتوقف Git ويقوم بإدراج الملفات المتعارضة.
   - للدمج: `git status` يعرض الملفات ذات التعارضات.
   - لـ rebase: يتم حل التعارضات commitًا تلو الآخر أثناء `git rebase -i`.
2. **تحرير الملفات المتعارضة**: افتح الملفات وابحث عن علامات التعارض:
   ```text
   <<<<<<< HEAD
   تغييراتك
   =======
   التغييرات الواردة
   >>>>>>> branch-name
   ```
   قم بالتحرير يدويًا للاحتفاظ بالتغييرات المطلوبة، ثم أزل العلامات.
3. **وضع علامة "تم الحل"**:
   - للدمج: `git add <file>`
   - لـ rebase: `git add <file>`، ثم `git rebase --continue`
4. **إكمال العملية**:
   - الدمج: `git commit` (قد ينشئ Git رسالة commit تلقائيًا).
   - Rebase: `git rebase --continue` حتى يتم تطبيق جميع commits.

### مثال: حل تعارض دمج
```bash
git checkout main
git merge feature-branch
# حدث تعارض
git status  # يسرد الملفات المتعارضة
# حرر الملفات لحل التعارضات
git add resolved-file.txt
git commit  # إنهاء الدمج
```

### مثال: حل تعارض rebase
```bash
git checkout feature-branch
git rebase main
# حدث تعارض
# حرر الملفات المتعارضة
git add resolved-file.txt
git rebase --continue
# كرر حتى يكتمل rebase
```

## 4. استخدام Ours و Theirs في حل التعارض
أثناء التعارضات، قد ترغب في تفضيل تغييرات جانب واحد (`ours` أو `theirs`). يعتمد معنى `ours` و `theirs` على العملية.

### الدمج: Ours مقابل Theirs
- `ours`: التغييرات من الفرع الحالي (مثال: `main`).
- `theirs`: التغييرات من الفرع الذي يتم دمجه (مثال: `feature-branch`).
- استخدم علم `--strategy-option` (`-X`):
  - الاحتفاظ بـ `ours`: `git merge -X ours feature-branch`
  - الاحتفاظ بـ `theirs`: `git merge -X theirs feature-branch`

### Rebase: Ours مقابل Theirs
- `ours`: التغييرات من الفرع الأساسي (مثال: `main`).
- `theirs`: التغييرات من الفرع الذي يتم عمل rebase له (مثال: `feature-branch`).
- الاستخدام أثناء حل تعارض rebase:
  ```bash
  git checkout --ours file.txt  # الاحتفاظ بإصدار الفرع الأساسي
  git checkout --theirs file.txt  # الاحتفاظ بإصدار فرع rebase
  git add file.txt
  git rebase --continue
  ```

### مثال: الدمج مع Theirs
لدمج `feature-branch` في `main` وتفضيل تغييرات `feature-branch`:
```bash
git checkout main
git merge -X theirs feature-branch
```

### مثال: Rebase مع Ours
أثناء عمل rebase لـ `feature-branch` على `main`، قم بحل تعارض بالاحتفاظ بإصدار `main`:
```bash
git checkout feature-branch
git rebase main
# حدث تعارض
git checkout --ours file.txt
git add file.txt
git rebase --continue
```

## 5. دمج Commits
دمج (Squashing) commits يجمع عدة commits في commit واحد، مما ينشئ تاريخًا أنظف. يتم هذا عادةً باستخدام rebase تفاعلي.

### خطوات دمج Commits
1. ابدأ rebase تفاعلي لـ commits المطلوبة:
   ```bash
   git rebase -i HEAD~n  # n = عدد commits المراد دمجها
   ```
2. في المحرر، غيّر `pick` إلى `squash` (أو `fixup`) لـ commits المراد دمجها في commit السابق.
3. احفظ واخرج. قد يطالبك Git بتحرير رسالة commit للـ commit المدمج.
4. ادفع التاريخ المحدث (دفع قسري إذا كان مشتركًا بالفعل):
   ```bash
   git push --force-with-lease
   ```

### مثال: دمج 3 commits
```bash
git rebase -i HEAD~3
# المحرر يعرض:
# pick abc123 Commit 1
# pick def456 Commit 2
# pick ghi789 Commit 3
# غيّر إلى:
# pick abc123 Commit 1
# squash def456 Commit 2
# squash ghi789 Commit 3
# احفظ واخرج
# حرر رسالة commit المدمجة إذا طُلب منك
git push --force-with-lease
```

### الدمج أثناء الدمج (Squash During Merge)
لدمج جميع commits من فرع أثناء عملية دمج:
```bash
git checkout main
git merge --squash feature-branch
git commit  # إنشاء commit واحد
```

## أفضل الممارسات والنصائح
- **النسخ الاحتياطي قبل Rebase**: إعادة الكتابة rebase التاريخ. أنشئ فرع نسخ احتياطي:
  ```bash
  git branch backup-branch
  ```
- **تجنب عمل Rebase للفروع المشتركة**: إعادة كتابة التاريخ على الفروع العامة يمكن أن يسبب مشاكل للمتعاونين. استخدم `merge` بدلاً من ذلك.
- **استخدم `--force-with-lease` للسلامة**: عند دفع التاريخ المعاد كتابته، هذا يمنع الكتابة فوق تغييرات الآخرين.
- **اختبار بعد حل التعارضات**: تأكد من أن مشروعك يُبنى وتمر الاختبارات بعد حل التعارضات.
- **استخدم أدوات للتعارضات**: أدوات واجهة المستخدم الرسومية مثل VS Code أو SourceTree أو `git mergetool` يمكنها تبسيط حل التعارض.
- **تواصل مع الفريق**: إذا كنت تعمل في فريق، قم بتنسيق عمليات rebase لتجنب التعارضات.

## المزالق الشائعة
- **فقدان العمل في Rebase**: احتفظ دائمًا بنسخة احتياطية أو استخدم `git reflog` لاستعادة commits المفقودة.
- **إساءة استخدام Ours/Theirs**: تحقق مرة أخرى من أي فرع هو `ours` مقابل `theirs` في سياقات الدمج مقابل rebase.
- **الدفع القسري بدون تنسيق**: الدفع القسري للفروع المشتركة يمكن أن يعطل زملاء الفريق. استخدم `--force-with-lease` وتواصل.

## الاستعادة من الأخطاء
- **عرض التاريخ**: استخدم `git reflog` لرؤية الحالات السابقة واستعادة commits المفقودة:
  ```bash
  git reflog
  git checkout <commit-hash>
  ```
- **إعادة التعيين إلى حالة ما قبل الدمج**:
  ```bash
  git reset --hard HEAD^  # تراجع عن آخر commit دمج
  ```
- **إحباط الدمج**: إذا ساءت عملية الدمج:
  ```bash
  git merge --abort
  ```

يوفر هذا الدليل أساسًا متينًا لسير عمل Git المتقدمة. بالنسبة لسيناريوهات أو أخطاء محددة، دعني أعلم، ويمكنني البحث بشكل أعمق أو البحث عن حلول في الوقت الفعلي!