---
audio: true
lang: hant
layout: post
title: 编程中重复的好处
---

> export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:"$HOME/Library/Python/3.9/bin":/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin

在这种情况下，避免使用该变量：

`"$HOME/Library/Python/3.9/bin"` 翻译为：

`"$HOME/圖書館/Python/3.9/bin"`

> export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin

第二个版本中，`/Users/lzwjava`目录多次出现，显得有些重复，但整体上更加简洁易读。

编程中的重复实际上可能是有益的。我们并不总是需要用变量或函数来抽象或简化一切。在这种情况下，主目录 `/Users/lzwjava` 不太可能频繁更改，因此完全可以接受重复使用它。

这类似于我们如何指代人名：如果我们过度使用“他”、“她”或“他们”这样的代词，就会让人不清楚我们在谈论谁。名字本身不太可能改变，直接使用它们可以增加清晰度。

抽象和简化很重要，但在某些情况下，它们会引入不必要的复杂性。有时，重复更简单，也更容易理解。