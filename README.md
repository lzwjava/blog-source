# lzwjava.github.io

Main improvements from the Jekyll blog using the jekyll-theme-cayman:

* Use large language models for translation
* Integrate with XeLaTeX to generate PDFs
* Integrate Google Cloud Text-to-Speech to generate audios
* Redefine some CSS
* MathJax support
* Night mode
* Select options for posts
* Keep the library updated
* Use awesome-cv to generate CVs
* Use feed.xml to support RSS feeds
* Chinese and English bilingual support

Getting started:

```shell
gem install jekyll bundler

jekyll new myblog

cd myblog

bundle install

bundle exec jekyll serve

bundle add webrick

jekyll serve
```

Markdown style:

```shell
rougify help style

rougify style github > _sass/syntax.css

rougify style gruvbox.dark > _sass/syntax.css

rougify style base16.monokai.dark > _sass/syntax.css
```

Audio and PDF pipeline:

```bash
conda activate google-cloud-env

python audio-pipeline.py --task posts --n 10

python audio-pipeline.py --task pages

python audio-pipeline.py --task notes

python pdf-pipeline.py --task pages

python pdf-pipeline.py --task posts --n 10

python pdf-pipeline.py --task notes
```

Updated guide:

- `-en`: English posts
- `-zh`: Chinese posts

`_posts` and `pages` support both `-en` and `-zh`.

`Notes` directory do not need to provide both Chinese and English articles; prefer to keep them in English, as they are mainly for self-learning.

Reference:

https://mcpride.github.io/posts/development/2018/03/06/syntax-highlighting-with-jekyll/