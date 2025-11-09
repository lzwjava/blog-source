---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: سير عمل البناء والنشر الآلي لجيكيل
translated: true
type: note
---

يمكنك القيام بذلك بالكامل في GitHub Actions: بناء الموقع على الـ runner، ثم استخراج الـ repo الوجهة إلى مجلد فراعي ودفع محتويات `_site/` إليه.

أدناه سير عمل جاهز يمكنك إضافته إلى الـ repo **المصدر** الخاص بك (حيث توجد نصوص Python البرمجية ومحتوى Jekyll):

```yaml
# .github/workflows/build-and-deploy.yml
name: Build & Deploy Jekyll to External Repo

on:
  push:
    branches: [ main ]
  workflow_dispatch:

# سنستخدم PAT لدفع الـ repo الوجهة
permissions:
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Check out source repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: Install Jekyll deps
        run: |
          bundle install --jobs 4 --retry 3

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Python deps
        if: hashFiles('requirements.txt') != ''
        run: pip install -r requirements.txt

      - name: Run your local workflow pipeline (CI mode)
        env:
          # أضف أي مفاتيح تحتاجها نصوصك البرمجية هنا
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        run: |
          # قم بتشغيل نفس الخطوات التي تنسقها نصك البرمجي بالضبط.
          # إذا أردت، يمكنك استدعاء نصك البرمجي مباشرة:
          python scripts/workflow_local.py
          # أو، إذا كنت تفضل الخطوات الصريحة:
          # python scripts/generate/update_notes_link.py
          # python scripts/translation/update_lang.py --max_files 9 --model gemini-flash --commits 1000
          # python -m unittest discover -s tests/workflow
          # python scripts/release/update_release.py

      - name: Build Jekyll (to _site)
        run: |
          # إذا كانت الوحدة النمطية Python الخاصة بك تضبط DEFAULT_DESTINATION في مكان آخر، فلا يزال بإمكانك التجاوز هنا.
          bundle exec jekyll build --destination _site

      - name: Check out destination repo
        uses: actions/checkout@v4
        with:
          repository: lzwjava/lzwjava.github.io   # <-- الـ DESTINATION_REPO_URL الهدف الخاص بك
          token: ${{ secrets.WORKFLOW_ACCESS_TOKEN }}      # <-- PAT مع نطاق "repo"
          path: destination
          fetch-depth: 0

      - name: Sync built site to destination repo
        run: |
          mkdir -p destination/_site
          rsync -av --delete _site/ destination/_site/
          cd destination
          # اختياري: تأكد من أن Pages لا تعالج Jekyll مرة أخرى
          touch _site/.nojekyll

          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit --amend --no-edit
            # اضبط الفرع إذا كان الوجهة يستخدم شيئًا آخر (مثل gh-pages)
            git push --force-with-lease origin HEAD:main
          else
            echo "No changes to deploy."
          fi

      - name: (Optional) Upload built site artifact
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site
```

### ما تحتاج إلى إعداده

* **PAT لدفع الوجهة**: أنشئ Personal Access Token كلاسيكي مع نطاق `repo` على حساب GitHub الخاص بك (أو استخدم token محدد الصلاحيات يمنح صلاحية كتابة لـ repo الوجهة). احفظه في إعدادات الـ repo المصدر كـ `WORKFLOW_ACCESS_TOKEN` (أي `Settings → Secrets and variables → Actions → New repository secret`).
* **أسماء الفروع و الـ repo**: في خطوة `Check out destination repo`، اضبط `repository:` على الـ repo الخارجي (يمكن أن يكون عامًا أو خاصًا). في أمر الدفع، اضبط الفرع الذي تريد النشر إليه (غالبًا `main` أو `gh-pages`).
* **إعدادات GitHub Pages** (إذا كنت تخدم من الـ repo الوجهة): في **Settings → Pages** الخاص بذلك الـ repo، اختر **Branch** الصحيح (مثل `main` / root)، واحتفظ بـ `CNAME`/النطاق المخصص كما تحب.
* **توقعات السجل**: تقوم خطوة النشر بتعديل آخر commit وتستخدم `--force-with-lease`؛ تأكد من أن هذا الفرع مخصص لقطع artefact النشر بحيث يكون إعادة كتابة التاريخ مقبولة.

### ملاحظات حول نص Python البرمجي الخاص بك

* لا تحتاج إلى `open_destination_repo_in_browser()` في CI، لذا لا بأس بتركها كما هي؛ ببساطة لن يتم استدعاؤها هنا. سير العمل يدفع مباشرة من الـ runner.
* أنت أيضًا لا تحتاج إلى `push_destination_repo()` في CI. سير العمل يتعامل مع الاستخراج الثاني والدفع، لذا يمكنك الاحتفاظ بنصك البرمجي دون تغيير للتشغيل المحلي.
* إذا كانت `build_site()` الخاصة بك تكتب إلى `DEFAULT_DESTINATION` مختلف، فلا يزال بإمكانك التجاوز عن طريق تشغيل خطوة بناء Jekyll الصريحة الموضحة أعلاه، والتي تكتب إلى `_site/`. تقوم خطوة النشر بالمزامنة من `_site/`.

### هل الـ repo الوجهة خاص؟

* هذا لا بأس به. تخدم GitHub Pages فقط الـ repos العامة (أو الفروع العامة في المنظمات التي تم تمكين Pages فيها)، ولكن إذا كان هدفك هو مجرد دفع artefacts إلى repo خاص لأي سبب، فإن ما ورد أعلاه لا يزال يعمل. إذا كنت تريد حقًا استضافة Pages، فتأكد من تكوين repo/فرع الوجهة لخدمة Pages (عام حيثما مطلوب) أو استخدم مضيفًا بديلاً (مثل Cloudflare Pages، Netlify) وقم بالنشر هناك بدلاً من ذلك.

هذا كل شيء—ستقوم الآن بالبناء على الـ runners الخاصة بـ GitHub ودفع `_site/` إلى repo آخر في السحابة.