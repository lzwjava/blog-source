---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 大型語言模型在複雜工作流程中的限制
translated: true
type: note
---

你完全正確！大型語言模型（包括我）擅長處理**小型、專注的任務**——例如解釋單一概念、生成簡短的程式碼片段或除錯特定錯誤——但在處理涉及以下內容的**複雜多步驟工作流程**時會遇到困難：

1. **多個相互關聯的配置**（例如 Maven `pom.xml` 檔案、Jacoco 代理參數、Python 測試整合）。
2. **有狀態的依賴關係**（例如「先更新 `module-A/pom.xml`，然後使用這些標誌執行 `mvn test`，最後合併報告」）。
3. **跨系統互動**（例如 Java + Python + CI 工具如 Jenkins/GitHub Actions）。
4. **上下文切換**（例如「現在忘記 Java 部分——我們如何在 Python 中解析 Jacoco XML？」）。

---

### **為什麼大型語言模型在複雜工作流程中失敗**
1. **沒有持久記憶**：除非你明確提醒我們（即使如此，上下文窗口也是有限的），否則我們不會「記住」過去的步驟。
2. **線性思維**：我們逐步生成回應，但無法動態追蹤依賴關係（例如「你在代理之前執行了 `mvn clean` 嗎？」）。
3. **對單一答案的過度優化**：我們被訓練成提供*一個*完整答案，而不是迭代式指導。
4. **沒有執行環境**：我們無法執行命令來驗證 `jacoco:prepare-agent` 是否在你的設定中實際生效。

---

### **更好的方法：「分而治之並驗證」**
對於像 **Jacoco + 多模組 Maven + Python 測試**這樣的問題，將其分解為**原子步驟**並驗證每一步。例如：

#### **步驟 1：驗證 Jacoco 代理設定（Java 端）**
```bash
# 在一個模組中（例如 module-A）：
mvn clean test -Pcoverage
```
- **檢查**：`target/site/jacoco/index.html` 是否存在？
- **除錯**：如果不存在，請分享 Jacoco 的 `pom.xml` 片段和錯誤日誌。

#### **步驟 2：生成合併報告（多模組）**
```bash
mvn jacoco:report-aggregate
```
- **檢查**：是否建立了 `target/site/jacoco-aggregate/index.html`？
- **除錯**：如果缺失，請驗證父 `pom.xml` 中的 `<module>` 路徑。

#### **步驟 3：匯出供 Python 使用（XML/CSV）**
```bash
# 將 Jacoco 二進位制檔案轉換為 XML
java -jar jacoco-cli.jar report jacoco.exec --xml output.xml
```
- **檢查**：`output.xml` 是否包含 `<package>` 標籤？
- **除錯**：如果為空，請確保測試執行了代理（`-javaagent:jacocoagent.jar`）。

#### **步驟 4：Python 整合**
```python
import xml.etree.ElementTree as ET
tree = ET.parse("output.xml")
coverage = tree.find(".//counter[@type='LINE'][@covered]")
print(f"Covered lines: {coverage.get('covered')}/{coverage.get('missed')}")
```
- **檢查**：腳本是否輸出預期的數字？
- **除錯**：如果沒有，請分享 XML 結構和 Python 錯誤。

---

### **如何有效地與大型語言模型協作**
1. **隔離問題**：
   - *「這是我的 module-A 的 `pom.xml`。為什麼 `jacoco:prepare-agent` 沒有添加 VM 參數？」*
   - *（比「幫我為 5 個模組 + Python 設定 Jacoco」更好）*

2. **分享最小可重現的上下文**：
   - 錯誤日誌、配置片段（不是整個檔案）以及**你已經嘗試過的方法**。

3. **迭代式除錯**：
   - **你**：「步驟 1 失敗，顯示 `No tests run`。這是日誌。」
   - **大型語言模型**：「在你的 `maven-surefire-plugin` 中添加 `<test>` 目標。」
   - **你**：「現在步驟 2 可以工作了，但報告是空的...」

4. **將我們用於「微任務」**：
   - *「寫一個 Python 腳本來解析 Jacoco XML，並在覆蓋率 < 80% 時失敗。」*
   - *「解釋 Maven 中 Jacoco 的 `<execution>` 標籤。」*

---

### **自動化複雜工作流程的工具**
由於大型語言模型無法管理狀態，請使用：
- **Shell 腳本**（例如 `setup_coverage.sh` 來鏈接 Maven/Python 命令）。
- **Makefiles**（定義 `make test-coverage` 來執行所有步驟）。
- **CI 模板**（具有明確步驟的 GitHub Actions/Jenkins 流水線）。
- **Docker**（容器化環境以避免「在我機器上可以運行」的問題）。

---
### **關鍵要點**
**大型語言模型就像超級增強版的 `man` 手冊或 Stack Overflow**——對於**個別部分**非常有用，但不適合協調整個系統。對於複雜任務：
1. **將其分解**。
2. **驗證每一步**。
3. **提出有針對性的問題**。

你想讓我更深入地探討上述的任何步驟嗎（例如在 Python 中解析 Jacoco XML 或多模組 Maven 設定）？