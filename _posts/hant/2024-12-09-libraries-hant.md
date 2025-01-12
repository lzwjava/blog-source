---
lang: hant
layout: post
title: 使用库时考虑升级
---

在我创业项目[Fun Live](https://github.com/lzwjava/live-server)中，我采用了CodeIgniter框架。尽管项目已告一段落，但几年后，我萌生了重启它以作纪念的念头。然而，回溯至2016年，我使用的是CodeIgniter 3版本，而如今最新的已是CodeIgniter 4了。

升级过程之所以棘手，是因为我的代码与CodeIgniter框架紧密耦合。根据[https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html)上的升级指南显示，更新代码库需要投入大量精力。

这次经历让我学到了重要的一课：在编写代码时，我们应该仔细考虑如何处理未来的更新。思考代码的哪些部分由我们控制，哪些部分由第三方依赖控制，这一点至关重要。