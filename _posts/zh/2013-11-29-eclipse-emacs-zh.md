---
audio: false
lang: zh
layout: post
title: 变身Eclipse为Emacs
translated: true
---

作为一个使用了半年的Emacs用户，我简直无法想象以前是怎么编码的，把手从标准位置移开去点击鼠标或按箭头键，感觉都很笨拙和难以忍受。现在，当我告诉朋友我设置了Alt+P和Alt+N快捷键来快速在XML文件和图形布局之间切换时，他们的回答只是“好的”，暗示使用鼠标切换也可以。对我来说，这简直是噩梦；速度太慢了！如果你是Emacs用户，你会理解的。

本文描述了构建快速的Eclipse“编辑”环境的一些简单技术。基本上，你的手可以保持在标准位置，这样你就可以以最大效率编码！

最重要的是安装Emacs+插件。请参阅“Emacs+: Emacs Experience in Eclipse”。

为了充分利用代码助手，你需要让它能够由任何字符触发，并在按下空格或=时防止自动完成。我推荐从CSDN下载此jar文件。有了它和一个快速的Google搜索，你可以在瞬间导入包。

接下来，让我们自定义一些快捷键：

1）将Alt+P绑定到“Previous Sub-Tab”，将Alt+N绑定到“Next Sub-Tab”。

子标签是编辑器下方的标签栏，例如在编辑XML文件时的“图形布局”和“XML”标签。这使你可以立即查看布局。

2）将Ctrl+C, Ctrl+C绑定到“Run”。

这是从sbcl的配置中复制的。默认是Ctrl+F11，对于如此频繁使用的快捷键来说，距离太远了，使得Emacs用户感到可怕！我愚蠢地按了几天的Ctrl+F11才改变它。

3）将Ctrl+X, Ctrl+O绑定到“Next View”，当在Windows和编辑文本时。

这使你可以在编写Java代码时从编辑器瞬间跳转到控制台。

4）将Ctrl+X, O绑定到“Next Editor”，当在Windows和编辑文本时。

这使你可以快速在Java文件之间切换。

5）将Ctrl+Q绑定到“Quick Fix”。

这样，当你输入`@string/xx`，光标在`xx`上时，按Ctrl+Q然后回车，会瞬间跳转到`string.xml`，光标位于`<string name="xx">TODO</string>`中的`TODO`。

6）将Ctrl+Shift+W绑定到“Close”（在Windows中）并删除原始绑定（关闭所有）。
原来的关闭快捷键是Ctrl+W，这与我们在浏览器、聊天框和文件资源管理器中的习惯一致。然而，它与Emacs的剪切命令冲突。实际上，按Ctrl+Shift+W一秒钟就可以关闭许多文件。因此，将Ctrl+Shift+W从“关闭所有”改为“关闭”不会损失任何东西。

有一个问题：安装Emacs+后，在编辑代码时，代码助手出现时，按上下箭头键不会选择代码助手候选项表中的项；而是在正在编辑的代码中上下移动。默认是用F2激活它。激活代码助手将焦点放在代码助手上，然后你只能使用上下箭头键选择。如果我们能使用Ctrl+P和Ctrl+N！编辑代码会快得像闪电！但是问题在于安装了Emacs+插件后，虽然Eclipse更像Emacs，但这种功能丢失了。在一个干净的Eclipse中，选择Emacs（而不是Emacs+Scheme）键盘布局，你可以在代码助手出现时使用Ctrl+N和Ctrl+P选择完成项。有人在Stack Overflow上问过这个问题，但还没有答案。

如果我们能使用Ctrl+P和Ctrl+N来选择完成项，那就真是太棒了！