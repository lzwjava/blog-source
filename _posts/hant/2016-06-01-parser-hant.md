---
lang: hant
layout: post
title: Creak：一个 Swift 的 HTML 解析库
---

[Creak](https://github.com/lzwjava/Creak) 旨在高效解析HTML文档，并构建代表文档元素的树状结构。这一解析过程涉及多个关键步骤与组件，它们协同工作以实现这一目标。以下是Creak解析HTML的详细说明：

### 解析过程概述

1. **初始化**：加載並清理 HTML 字串。
2. **標記化**：將 HTML 字串分解為表示 HTML 不同部分的標記，例如標籤和文本。
3. **樹結構構建**：使用標記構建表示 HTML 文件元素和文本的樹結構。

### 关键组件

- **Dom 类**：负责管理整个解析流程，并存储解析后HTML树的根节点。
- **Content 类**：提供将HTML字符串标记化的实用功能。
- **HtmlNode 和 TextNode 类**：分别代表HTML文档中的元素节点和文本节点。
- **Tag 类**：表示HTML标签及其相关属性。

### 详细解析步骤

1. **理解问题**：首先，我们需要明确问题的具体内容和要求。这包括识别问题的关键要素、已知条件和需要求解的目标。

2. **收集信息**：根据问题的需求，收集相关的数据和信息。这可能涉及查阅资料、进行实验或使用已有的数据集。

3. **分析数据**：对收集到的数据进行整理和分析，找出其中的规律和趋势。可以使用统计方法、图表分析等手段来帮助理解数据。

4. **建立模型**：根据问题的特点，选择合适的数学模型或理论框架来描述问题。这可能包括建立方程、绘制图形或使用算法。

5. **求解模型**：运用数学工具或计算方法，对建立的模型进行求解。这可能涉及代数运算、微积分、数值分析等。

6. **验证结果**：将求解得到的结果与实际情况进行对比，验证其准确性和合理性。如果结果不符合预期，可能需要重新审视模型或数据。

7. **得出结论**：根据验证后的结果，得出最终的结论或解决方案。确保结论清晰、准确，并且能够有效解决问题。

8. **撰写报告**：将整个解析过程、使用的方法、得到的结果和结论整理成报告，以便他人理解和参考。

通过以上步骤，我们可以系统地解析复杂问题，确保每一步都经过仔细的思考和验证，从而提高解决问题的效率和准确性。

#### 1. 初始化

`Dom` 类负责初始化解析过程。`loadStr` 方法接收原始 HTML 字符串，对其进行清理，并初始化 `Content` 对象。

```swift
public func loadStr(str: String) -> Dom {
    raw = str
    let html = clean(str)
    content = Content(content: html)
    parse()
    return self
}
```

翻譯成繁體中文：

```swift
public func loadStr(str: String) -> Dom {
    raw = str
    let html = clean(str)
    content = Content(content: html)
    parse()
    return self
}
```

這段程式碼的功能是將一個字串加載到 `Dom` 物件中。首先，它將原始字串 `str` 存儲到 `raw` 變數中，然後使用 `clean` 函數對字串進行清理，並將清理後的結果存儲到 `html` 變數中。接著，它將 `html` 作為內容創建一個 `Content` 物件，並將其存儲到 `content` 變數中。最後，它調用 `parse` 函數進行解析，並返回 `self`，即當前的 `Dom` 物件。

#### 2. 标记化

`Content` 类提供了用于对 HTML 字符串进行标记化的实用函数。它包含了一系列方法，例如从当前字符位置复制字符、跳过字符，以及处理标签和属性等标记的操作。

- **copyUntil**：從當前位置複製字符，直到遇到指定字符。
- **skipByToken**：根據指定的標記跳過字符。

這些方法用於識別和提取HTML的不同部分，例如標籤、屬性和文本內容。

#### 3. 树结构构建

`Dom` 類中的 `parse` 方法會遍歷 HTML 字符串，識別標籤和文本，並構建由 `HtmlNode` 和 `TextNode` 組成的樹狀結構。

```swift
private func parse() {
    root = HtmlNode(tag: "root")
    var activeNode: InnerNode? = root
    while activeNode != nil {
        let str = content.copyUntil("<")
        if (str == "") {
            let info = parseTag()
            if !info.status {
                activeNode = nil
                continue
            }
            
            if info.closing {
                let originalNode = activeNode
                while activeNode?.tag.name != info.tag {
                    activeNode = activeNode?.parent
                    if activeNode == nil {
                        activeNode = originalNode
                        break
                    }
                }
                if activeNode != nil {
                    activeNode = activeNode?.parent
                }
                continue
            }
            
            if info.node == nil {
                continue
            }
            
            let node = info.node!
            activeNode!.addChild(node)
            if !node.tag.selfClosing {
                activeNode = node
            }
        } else if (trim(str) != "") {
            let textNode = TextNode(text: str)
            activeNode?.addChild(textNode)
        }
    }
}
```

翻譯如下：

```swift
private func parse() {
    root = HtmlNode(tag: "root")
    var activeNode: InnerNode? = root
    while activeNode != nil {
        let str = content.copyUntil("<")
        if (str == "") {
            let info = parseTag()
            if !info.status {
                activeNode = nil
                continue
            }
            
            if info.closing {
                let originalNode = activeNode
                while activeNode?.tag.name != info.tag {
                    activeNode = activeNode?.parent
                    if activeNode == nil {
                        activeNode = originalNode
                        break
                    }
                }
                if activeNode != nil {
                    activeNode = activeNode?.parent
                }
                continue
            }
            
            if info.node == nil {
                continue
            }
            
            let node = info.node!
            activeNode!.addChild(node)
            if !node.tag.selfClosing {
                activeNode = node
            }
        } else if (trim(str) != "") {
            let textNode = TextNode(text: str)
            activeNode?.addChild(textNode)
        }
    }
}
```

這段程式碼的主要功能是解析HTML內容，並將其轉換為節點樹結構。以下是程式碼的詳細解釋：

1. **初始化根節點**：`root` 被初始化為一個標籤名為 "root" 的 `HtmlNode` 物件。

2. **遍歷節點**：`activeNode` 被設置為當前活動的節點，初始時為根節點。`while` 迴圈會持續執行，直到 `activeNode` 為 `nil`。

3. **解析內容**：`content.copyUntil("<")` 會從當前內容中複製直到遇到 `<` 符號。如果複製的內容為空，則進入標籤解析流程。

4. **解析標籤**：`parseTag()` 函數用於解析標籤，並返回一個包含標籤信息的結構體 `info`。如果 `info.status` 為 `false`，則將 `activeNode` 設置為 `nil` 並繼續下一次迴圈。

5. **處理閉合標籤**：如果 `info.closing` 為 `true`，則表示當前解析到的是閉合標籤。程式會向上遍歷節點樹，直到找到與閉合標籤名稱匹配的節點，然後將 `activeNode` 設置為該節點的父節點。

6. **處理非閉合標籤**：如果 `info.node` 不為 `nil`，則將該節點添加到當前活動節點的子節點中。如果該節點不是自閉合標籤，則將 `activeNode` 設置為該節點。

7. **處理文本節點**：如果複製的內容不為空，則將其作為文本節點添加到當前活動節點的子節點中。

這段程式碼的主要目的是將HTML內容解析為節點樹結構，以便後續處理或渲染。

- **根節點**：解析從根節點 (`HtmlNode`，標籤為 "root") 開始。
- **活動節點**：`activeNode` 變量追蹤當前處理的節點。
- **文本內容**：如果發現文本內容，會創建一個 `TextNode` 並添加到當前節點。
- **標籤解析**：如果發現標籤，會調用 `parseTag` 方法處理它。

#### 标签解析

`parseTag` 方法负责标签的识别和处理。

```swift
private func parseTag() -> ParseInfo {
    var result = ParseInfo()
    if content.char() != ("<" as Character) {
        return result
    }
    
    if content.fastForward(1).char() == "/" {
        var tag = content.fastForward(1).copyByToken(Content.Token.Slash, char: true)
        content.copyUntil(">")
        content.fastForward(1)
        
        tag = tag.lowercaseString
        if selfClosing.contains(tag) {
            result.status = true
            return result
        } else {
            result.status = true
            result.closing = true
            result.tag = tag
            return result
        }
    }
    
    let tag = content.copyByToken(Content.Token.Slash, char: true).lowercaseString
    let node = HtmlNode(tag: tag)
    
    while content.char() != ">" &&
       content.char() != "/" {
        let space = content.skipByToken(Content.Token.Blank, copy: true)
        if space?.characters.count == 0 {
            content.fastForward(1)
            continue
        }
        
        let name = content.copyByToken(Content.Token.Equal, char: true)
        if name == "/" {
            break
        }
        
        if name == "" {
            content.fastForward(1)
            continue
        }
        
        content.skipByToken(Content.Token.Blank)
        if content.char() == "=" {
            content.fastForward(1).skipByToken(Content.Token.Blank)
            var attr = AttrValue()
            let quote: Character? = content.char()
            if quote != nil {
                if quote == "\"" {
                    attr.doubleQuote = true
                } else {
                    attr.doubleQuote = false
                }
                content.fastForward(1)
                var string = content.copyUntil(String(quote!), char: true, escape: true)
                var moreString = ""
                repeat {
                    moreString = content.copyUntilUnless(String(quote!), unless: "=>")
                    string += moreString
                } while moreString != ""
                attr.value = string
                content.fastForward(1)
                node.setAttribute(name, attrValue: attr)
            } else {
                attr.doubleQuote = true
                attr.value = content.copyByToken(Content.Token.Attr, char: true)
                node.setAttribute(name, attrValue: attr)
            }
        } else {
            node.tag.setAttribute(name, attrValue: AttrValue(nil, doubleQuote: true))
            if content.char() != ">" {
                content.rewind(1)
            }
        }
    }
    
    content.skipByToken(Content.Token.Blank)
    if content.char() == "/" {
        node.tag.selfClosing = true
        content.fastForward(1)
    } else if selfClosing.contains(tag) {
        node.tag.selfClosing = true
    }
    
    content.fastForward(1)
    
    result.status = true
    result.node = node
    
    return result
}
```

- **标签识别**：該方法識別標籤是開標籤還是閉標籤。
- **屬性**：解析標籤的屬性並將其添加到 `HtmlNode`。
- **自閉合標籤**：適當地處理自閉合標籤。

### 结论

通过本次实验，我们深入了解了Python编程语言的基础知识，包括变量、数据类型、条件语句、循环结构以及函数的定义与调用。实验过程中，我们不仅掌握了如何编写简单的Python程序，还学会了如何调试代码、处理错误以及优化程序性能。

此外，我们还探讨了Python在数据分析、机器学习等领域的应用，通过实际案例学习了如何使用Pandas进行数据处理、利用Matplotlib进行数据可视化，以及使用Scikit-learn库构建简单的机器学习模型。这些技能为我们今后在数据科学和人工智能领域的研究与实践奠定了坚实的基础。

总的来说，本次实验不仅增强了我们的编程能力，还拓宽了我们的知识视野，使我们能够更好地应对未来在计算机科学和相关领域的挑战。

Creak 的解析过程包括初始化 HTML 内容、将其标记化并构建节点的树结构。`Dom` 类负责整体解析的管理，而 `Content` 类则提供标记化 HTML 字符串的实用函数。`HtmlNode` 和 `TextNode` 类分别表示 HTML 文档中的元素和文本，`Tag` 类则负责管理标签的属性。这种高效且有组织的方法使 Creak 成为 Swift 中解析 HTML 的强大工具。