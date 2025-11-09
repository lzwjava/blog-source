---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: प्रतिस्पर्धात्मक प्रोग्रामिंग में डीएफएस के लाभ
translated: true
type: note
---

### प्रतिस्पर्धात्मक प्रोग्रामिंग में DFS का उपयोग क्यों करें?

डेप्थ-फर्स्ट सर्च (DFS) एक मौलिक ग्राफ ट्रैवर्सल एल्गोरिदम है जो प्रतिस्पर्धात्मक प्रोग्रामिंग में व्यापक रूप से उपयोग किया जाता है क्योंकि यह कनेक्टिविटी, पाथ और रिकर्सिव स्ट्रक्चर से जुड़ी समस्याओं को कुशलतापूर्वक एक्सप्लोर करता है। यहाँ बताया गया है कि यह विशेष रूप से मूल्यवान क्यों है:

- **गहन एक्सप्लोरेशन के लिए दक्षता**: DFS बैकट्रैक करने से पहले एक पाथ में गहराई तक जाता है, जो उन समस्याओं के लिए आदर्श बनाता है जहाँ आपको एकल पाथ ढूंढने, साइकिलों का पता लगाने, या सभी संभावनाओं को संपूर्ण रूप से एक्सप्लोर करने की आवश्यकता होती है (उदाहरण के लिए, बैकट्रैकिंग परिदृश्यों में)। इसकी टाइम कॉम्प्लेक्सिटी ग्राफ के लिए O(V + E) (V = वर्टिसेज़, E = एजेज़) है, जो अधिकांश प्रतियोगिता कंस्ट्रेंट के लिए लीनियर और तेज़ है।

- **रिकर्सिव समस्याओं को स्वाभाविक रूप से संभालता है**: कई समस्याओं को रिकर्सिव सबप्रॉब्लम्स वाले ट्री या ग्राफ के रूप में मॉडल किया जा सकता है (जैसे, भूलभुलैया, पहेलियाँ, या ट्री ट्रैवर्सल)। DFS रिकर्शन के लिए कॉल स्टैक का उपयोग करता है, जो कोड को सरल और इटरेटिव दृष्टिकोण की तुलना में मेमोरी-एफिशिएंट बनाए रखता है।

- **ग्राफ समस्याओं के लिए बहुमुखी**: यह कनेक्टेड कंपोनेंट्स का पता लगाने, ब्रिज/आर्टिकुलेशन पॉइंट्स ढूंढने, टोपोलॉजिकल सॉर्टिंग, या बाइपार्टाइट ग्राफ को हल करने के लिए बहुत अच्छा है। प्रतियोगिताओं में, ग्राफ अक्सर छिपे होते हैं (जैसे, स्ट्रिंग्स या ग्रिड्स के रूप में), और DFS वहाँ चमकता है।

- **बैकट्रैकिंग शक्ति**: N-Queens, सुडोकू, या सबसेट/पर्म्युटेशन जनरेट करने जैसी कॉम्बिनेटोरियल समस्याओं के लिए, बैकट्रैकिंग के साथ DFS अमान्य पाथों को जल्दी प्रून कर देता है, जिससे ब्रूट-फोर्स विस्फोट से बचा जाता है।

- **स्पेस ट्रेड-ऑफ**: यह गहरे ग्राफ के लिए BFS की तुलना में कम मेमोरी का उपयोग करता है (केवल रिकर्शन स्टैक), जो मेमोरी-टाइट प्रतियोगिताओं में मायने रखता है।

कुल मिलाकर, DFS तब गो-टू टूल है जब समस्या "गहराई से एक्सप्लोर करो और फंस जाओ तो बैकट्रैक करो" का संकेत देती है, खासकर Codeforces या LeetCode जैसे प्लेटफॉर्म पर।

### DFS उदाहरण

यहाँ तीन सामान्य उदाहरण स्यूडोकोड (स्पष्टता के लिए Python-स्टाइल में) के साथ दिए गए हैं। ये चित्रण के लिए सरल किए गए हैं—उन्हें पूर्ण समस्याओं के लिए एडाप्ट करें।

#### 1. **अनडायरेक्टेड ग्राफ में साइकिल का पता लगाना**
   - **समस्या**: एक ग्राफ दिया गया है, जांचें कि क्या इसमें कोई साइकिल है।
   - **DFS क्यों?**: गहराई से ट्रैवर्स करें; यदि आप करंट पाथ में किसी नोड पर दोबारा जाते हैं, तो एक साइकिल है।
   - **स्यूडोकोड**:
     ```python:disable-run
     def has_cycle(graph, start, visited, parent):
         visited[start] = True
         for neighbor in graph[start]:
             if not visited[neighbor]:
                 if has_cycle(graph, neighbor, visited, start):
                     return True
             elif neighbor != parent:
                 return True  # Back edge to ancestor
         return False

     # Usage
     visited = {node: False for node in graph}
     cycle_exists = any(has_cycle(graph, node, visited, -1) for node in graph if not visited[node])
     ```

#### 2. **ग्राफ में कनेक्टेड कंपोनेंट्स ढूँढना**
   - **समस्या**: एक अनडायरेक्टेड ग्राफ में सभी अलग-अलग कनेक्टेड समूहों की पहचान करें।
   - **DFS क्यों?**: एक नोड से शुरू करें, सभी पहुँच योग्य नोड्स को एक कंपोनेंट के रूप में चिह्नित करें, फिर अगले अनविजिटेड नोड पर जाएँ।
   - **स्यूडोकोड**:
     ```python
     def dfs(graph, start, visited, component):
         visited[start] = True
         component.append(start)
         for neighbor in graph[start]:
             if not visited[neighbor]:
                 dfs(graph, neighbor, visited, component)

     # Usage
     visited = {node: False for node in graph}
     components = []
     for node in graph:
         if not visited[node]:
             component = []
             dfs(graph, node, visited, component)
             components.append(component)
     ```

#### 3. **भूलभुलैया/पाथ फाइंडिंग (बैकट्रैकिंग)**
   - **समस्या**: एक ग्रिड भूलभुलैया (0 = खुला, 1 = दीवार) में स्टार्ट से एंड तक एक रास्ता ढूंढें।
   - **DFS क्यों?**: रिकर्सिवली रास्ते आज़माएँ; डेड एंड पर बैकट्रैक करें।
   - **स्यूडोकोड** (ग्रिड को 2D लिस्ट के रूप में):
     ```python
     def solve_maze(grid, x, y, end_x, end_y, path):
         if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1:
             return False
         if x == end_x and y == end_y:
             path.append((x, y))
             return True
         path.append((x, y))
         grid[x][y] = 1  # Mark as visited
         # Try directions: down, right, up, left
         if (solve_maze(grid, x+1, y, end_x, end_y, path) or
             solve_maze(grid, x, y+1, end_x, end_y, path) or
             solve_maze(grid, x-1, y, end_x, end_y, path) or
             solve_maze(grid, x, y-1, end_x, end_y, path)):
             return True
         path.pop()  # Backtrack
         grid[x][y] = 0  # Unmark
         return False

     # Usage: path = []; solve_maze(grid, 0, 0, rows-1, cols-1, path)
     ```

ये उदाहरण DFS की रिकर्सिव एलिगेंस दिखाते हैं—इसे एक्शन में देखने के लिए "Number of Islands" (LeetCode) या "Cycle Detection" (HackerRank) जैसी समस्याओं पर अभ्यास करें!