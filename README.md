# lzwjava.github.io

Welcome to my personal blog! Here, I share my thoughts, experiences, and knowledge on various topics.

## improvements

Main improvements from the Jekyll blog using the jekyll-theme-cayman:

* Translation with Large Language Models: Utilize advanced language models to provide accurate and contextually relevant translations, making the content accessible to a global audience.
* PDF Generation with XeLaTeX: Integrate XeLaTeX to generate high-quality, professionally formatted PDFs, ideal for printing and offline reading.
* Audio Generation with Google Cloud Text-to-Speech: Leverage Google Cloud's Text-to-Speech service to create audio versions of posts, enhancing accessibility for visually impaired users and those who prefer listening to content.
* Custom CSS Styling: Redefine and enhance the blog's CSS to create a visually appealing and user-friendly design, ensuring a pleasant reading experience.
* MathJax Support: Implement MathJax to render complex mathematical expressions and equations beautifully, making technical content more accessible and easier to understand.
* Night Mode: Introduce a night mode feature to reduce eye strain and improve readability in low-light environments, providing a more comfortable experience for late-night readers.
* Post Selection Options: Offer various selection options for posts, such as filtering by category or tag, to enhance navigation and help users find content that interests them.
* Regular Library Updates: Keep the blog's library and dependencies up-to-date with the latest features, security patches, and improvements to ensure optimal performance and functionality.
* CV Generation with awesome-cv: Use the awesome-cv tool to create professional and visually appealing CVs directly from the blog, making it easy to showcase skills and experience.
* RSS Feed Support with feed.xml: Implement feed.xml to provide RSS feeds, allowing users to subscribe to the blog and stay updated with the latest content through their preferred feed reader.
* Bilingual Support: Offer content in both Chinese and English to cater to a diverse audience, fostering inclusivity and broadening the blog's reach.


### Getting started

```shell
gem install jekyll bundler

jekyll new myblog

cd myblog

bundle install

bundle exec jekyll serve

bundle exec jekyll serve --draft

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