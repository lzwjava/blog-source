---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 编程中重复的好处
translated: true
type: post
---

> export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:"$HOME/Library/Python/3.9/bin":/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin

在這個情況下，避免使用變量：

`"$HOME/Library/Python/3.9/bin"`

> export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin

第二個版本看起來有點重複，因為`/Users/lzwjava`目錄出現多次，但它更清晰且更容易閱讀。

在編程中，重複實際上可能是有益的。我們並不需要總是用變量或函數來抽象或簡化一切。在這個例子中，主目錄`/Users/lzwjava`不太可能頻繁更改，所以重複它是完全可以接受的。

這就像我們如何稱呼人的名字一樣：如果我們過度使用代詞如“他”、“她”或“他們”，就會不清楚我們在談論誰。名字本身不太可能改變，直接使用它們可以增加清晰度。

抽象和簡化很重要，但在某些情況下，它們會引入不必要的複雜性。有時候，重複反而更簡單且更容易理解。